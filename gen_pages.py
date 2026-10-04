"""Generate public, SEO-friendly pages of currently open public tenders (Czech + Slovak buyers) from TED.

Runs daily in GitHub Actions (see .github/workflows/pages.yml) and writes the whole site into _site/:
static landing pages copied as-is + /zakazky/<sector>-<country>/ pages + sitemap.xml + robots.txt.

  python gen_pages.py                      # live: query TED
  python gen_pages.py --fixture f.json     # offline: use saved TED notices
"""
import argparse, datetime as dt, html, json, os, re, shutil, time
from urllib.parse import quote

BASE = "https://tenderwatching.com"
API = "https://api.ted.europa.eu/v3/notices/search"
OPEN_TYPES = ["cn-standard", "cn-social", "cn-desg", "pin-cfc-standard", "pin-cfc-social", "qu-sy", "subco"]
FIELDS = ["publication-number", "notice-type", "notice-title", "buyer-name", "buyer-country",
          "classification-cpv", "deadline-receipt-tender-date-lot", "publication-date"]
COUNTRIES = {"cesko": ("CZE", "Česko", "v Česku"), "slovensko": ("SVK", "Slovensko", "na Slovensku")}
# slug: (title, CPV prefixes, short description used in the intro)
SECTORS = {
    "it-software":      ("IT a software", ["72", "48", "302"], "vývoj a údržba softwaru, IT služby, hardware a licence"),
    "stavby":           ("Stavební práce", ["45"], "stavby, rekonstrukce, silnice a inženýrské sítě"),
    "fotovoltaika":     ("Fotovoltaika a solární energie", ["0933"], "fotovoltaické elektrárny, solární panely a jejich instalace"),
    "energetika":       ("Energetika", ["09", "31", "65"], "dodávky energie, elektrozařízení a energetické služby"),
    "zdravotnictvi":    ("Zdravotnictví a zdravotnická technika", ["33"], "zdravotnické přístroje, materiál a vybavení nemocnic"),
    "doprava":          ("Doprava a vozidla", ["34", "60"], "vozidla, dopravní prostředky a přepravní služby"),
    "projekce":         ("Projekce a inženýring", ["71"], "architektonické, projekční a inženýrské služby"),
    "poradenstvi":      ("Poradenství a služby pro firmy", ["79"], "poradenství, marketing, personalistika a administrativní služby"),
    "uklid-odpady":     ("Úklid, odpady a životní prostředí", ["90"], "svoz a zpracování odpadu, úklid a ekologické služby"),
    "vzdelavani":       ("Vzdělávání a školení", ["80"], "školení, kurzy a vzdělávací programy"),
    "potraviny":        ("Potraviny a stravování", ["15", "553", "555"], "dodávky potravin, catering a školní stravování"),
    "nabytek-vybaveni": ("Nábytek a vybavení", ["39"], "nábytek, vybavení interiérů a kancelářské potřeby"),
}
MAX_LIST = 150   # per sector page; the rest goes behind the email CTA
MIN_INDEX = 3   # pages with fewer open tenders get noindex (avoid thin content)
LANG_PREF = ["ces", "slk", "eng"]


def as_list(v):
    return [] if v is None else [str(x) for x in v] if isinstance(v, list) else [str(v)]


def pick(m):
    if not isinstance(m, dict):
        return (as_list(m) or [""])[0]
    for l in LANG_PREF:
        if m.get(l):
            return (as_list(m[l]) or [""])[0]
    return next(((as_list(x) or [""])[0] for x in m.values() if x), "")


def split_title(t):
    parts = t.split(" – ", 2)
    return (parts[1], parts[2]) if len(parts) == 3 else ("", t)


def fetch(days=40):
    import requests
    s = requests.Session()
    q = (f"publication-date>=today(-{days}) AND notice-type IN ({' '.join(OPEN_TYPES)}) "
         f"AND buyer-country IN ({' '.join(c[0] for c in COUNTRIES.values())})")   # no SORT BY: caps iteration at 750
    body = {"query": q, "fields": FIELDS, "limit": 250, "paginationMode": "ITERATION"}
    out = []
    while True:
        for i in range(4):
            try:
                r = s.post(API, json=body, timeout=60); r.raise_for_status(); data = r.json(); break
            except (requests.RequestException, ValueError):
                if i == 3: raise
                time.sleep(2 ** i * 5)
        out += data.get("notices", [])
        if not data.get("iterationNextToken") or not data.get("notices"):
            return out
        body["iterationNextToken"] = data["iterationNextToken"]
        time.sleep(0.3)


def normalise(notices, today):
    rows = {}
    for x in notices:
        if x.get("notice-type") and x["notice-type"] not in OPEN_TYPES:
            continue
        dl = sorted(d[:10] for d in as_list(x.get("deadline-receipt-tender-date-lot")))
        if not dl or dl[0] < today.isoformat():
            continue                     # only tenders you can still bid on, with a known deadline
        cat, title = split_title(pick(x.get("notice-title")))
        nid = x.get("publication-number")
        rows[nid] = dict(id=nid, title=title.strip(), category=cat, buyer=pick(x.get("buyer-name")),
                         countries=list(dict.fromkeys(as_list(x.get("buyer-country")))),
                         cpvs=list(dict.fromkeys(as_list(x.get("classification-cpv")))),
                         deadline=dl[0], published=str(x.get("publication-date", ""))[:10])
    return sorted(rows.values(), key=lambda r: (r["deadline"], r["id"]))


def lc(t):
    """Lower-case a sector name for use mid-sentence, but keep acronyms like IT."""
    return t if t.split()[0].isupper() else t[0].lower() + t[1:]


def fmt(d):
    y, m, dd = d.split("-"); return f"{int(dd)}. {int(m)}. {y}"


def days_word(n):
    return "den" if n == 1 else "dny" if 2 <= n <= 4 else "dní"


def zakazky(n):
    return "zakázka" if n == 1 else "zakázky" if 2 <= n <= 4 else "zakázek"


def chrome():
    """Reuse the landing page's CSS and footer so generated pages stay in sync with the main site."""
    src = open("index.html", encoding="utf-8").read()
    css = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
    footer = re.search(r"<footer>.*?</footer>", src, re.S).group(0)
    footer = footer.replace('href="soukromi.html"', 'href="/soukromi.html"')
    return css, footer


EXTRA_CSS = """
.list{list-style:none;padding:0;margin:0}
.list li{padding:14px 0;border-top:1px solid var(--line)}
.list a.tt{font-weight:600;color:var(--forest);text-decoration:none}
.list a.tt:hover{text-decoration:underline}
.meta{display:block;font-size:14px;color:var(--moss);margin-top:2px}
.dl{font-weight:600;color:var(--ink)}
.box{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:20px 22px;margin:28px 0}
.box p{margin:0 0 12px}
.chips{display:flex;flex-wrap:wrap;gap:8px;padding:0;list-style:none}
.chips a{display:inline-block;padding:6px 12px;border:1px solid var(--line);border-radius:99px;text-decoration:none;font-size:15px}
.crumb{font-size:14px;color:var(--moss);margin:8px 0 0}
.upd{font-size:14px;color:var(--moss)}
"""


def page(title, desc, path, body, css, footer, noindex=False):
    canon = f"{BASE}{path}"
    robots = '<meta name="robots" content="noindex,follow">' if noindex else ""
    return f"""<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">{robots}
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;600;800&display=swap" rel="stylesheet">
<style>{css}{EXTRA_CSS}</style>
</head>
<body>
<div class="wrap">
<header><a class="logo" href="/">TenderWatch</a><nav><a href="/zakazky/">Aktuální zakázky</a><a href="/#pricing">Ceník</a></nav></header>
<main class="doc" style="max-width:none">
{body}
</main>
{footer}
"""


def cta(sector_title, country_name):
    return (f'<div class="box"><p><strong>Nechte si nové zakázky posílat každé ráno.</strong> '
            f'TenderWatch každý pracovní den projde všechna nová oznámení v TED a pošle vám jen ta, '
            f'která odpovídají vašemu oboru ({html.escape(lc(sector_title))}, {html.escape(country_name)}) '
            f'— česky, s lhůtou a odkazem.</p>'
            f'<a class="cta" href="/">Vyzkoušet 14 dní zdarma</a></div>')


def item(r, today):
    d = (dt.date.fromisoformat(r["deadline"]) - today).days
    cat = f'{html.escape(r["category"])} · ' if r["category"] else ""
    return (f'<li><a class="tt" href="https://ted.europa.eu/cs/notice/-/detail/{quote(r["id"])}" rel="nofollow noopener">'
            f'{html.escape(r["title"] or "(bez názvu)")}</a>'
            f'<span class="meta">{cat}{html.escape(r["buyer"])}</span>'
            f'<span class="meta"><span class="dl">Lhůta {fmt(r["deadline"])}</span> (zbývá {d} {days_word(d)})</span></li>')


def matches(r, prefixes, iso):
    return iso in r["countries"] and any(c.startswith(p) for c in r["cpvs"] for p in prefixes)


def build(rows, today, out="_site"):
    css, footer = chrome()
    if os.path.exists(out):
        shutil.rmtree(out)
    shutil.copytree(".", out, ignore=shutil.ignore_patterns("_site", ".git", ".github", "*.py", "__pycache__", "*.json", "README*"))
    urls, pages = ["/", "/en/", "/soukromi.html", "/privacy.html", "/zakazky/"], {}
    stamp = f'<p class="upd">Aktualizováno {fmt(today.isoformat())} · zdroj: TED, Úřad pro publikace EU</p>'

    for cslug, (iso, cname, cin) in COUNTRIES.items():
        country_rows = [r for r in rows if iso in r["countries"]]
        sector_links = []
        for sslug, (stitle, prefixes, sdesc) in SECTORS.items():
            hits = [r for r in rows if matches(r, prefixes, iso)]
            path = f"/zakazky/{sslug}-{cslug}/"
            n = len(hits)
            title = f"Veřejné zakázky {stitle} – {cname} | otevřené výzvy"
            desc = (f"{n} {zakazky(n)} v oboru {lc(stitle)} {cin}, do kterých se dá ještě přihlásit. "
                    f"Seznam s lhůtami pro podání nabídek, aktualizovaný každý pracovní den.")
            intro = (f'<p class="lede">Aktuálně otevřené veřejné zakázky {cin} v oboru <strong>{html.escape(lc(stitle))}</strong> '
                     f'({html.escape(sdesc)}). {"Je jich " + str(n) + "." if n else "Momentálně žádná otevřená výzva."} '
                     f'Seřazeno podle nejbližší lhůty pro podání nabídek.</p>')
            body = (f'<p class="crumb"><a href="/zakazky/">Aktuální zakázky</a> › {html.escape(cname)}</p>'
                    f'<h1>Veřejné zakázky: {html.escape(stitle)} – {html.escape(cname)}</h1>{stamp}{intro}'
                    + (f'<ul class="list">{"".join(item(r, today) for r in hits[:MAX_LIST])}</ul>' if hits else "")
                    + (f'<p><strong>…a dalších {n - MAX_LIST} {zakazky(n - MAX_LIST)}.</strong> Celý seznam vám rádi pošleme e-mailem.</p>' if n > MAX_LIST else "")
                    + cta(stitle, cname)
                    + f'<p class="upd">Zobrazujeme nadlimitní zakázky zveřejněné v Úředním věstníku EU (TED) za posledních 40 dní. '
                      f'Podlimitní zakázky z národních věstníků zatím nepokrýváme.</p>')
            pages[path] = page(title, desc, path, body, css, footer, noindex=n < MIN_INDEX)
            if n >= MIN_INDEX:
                urls.append(path)
            sector_links.append((stitle, path, n))
        # country overview
        path = f"/zakazky/{cslug}/"
        n = len(country_rows)
        chips = "".join(f'<li><a href="{p}">{html.escape(t)} ({k})</a></li>' for t, p, k in sector_links)
        body = (f'<h1>Veřejné zakázky – {html.escape(cname)}</h1>{stamp}'
                f'<p class="lede">{n} otevřených nadlimitních veřejných zakázek {cin}, do kterých se dá ještě podat nabídka. Vyberte obor:</p>'
                f'<ul class="chips">{chips}</ul>'
                f'<h2>Nejbližší lhůty</h2><ul class="list">{"".join(item(r, today) for r in country_rows[:30])}</ul>'
                + cta("všechny obory", cname))
        pages[path] = page(f"Veřejné zakázky {cname} – otevřené výzvy podle oboru",
                           f"{n} otevřených veřejných zakázek {cin} podle oboru, s lhůtami. Aktualizováno každý pracovní den.",
                           path, body, css, footer)
        urls.append(path)

    # hub
    blocks = "".join(
        f'<h2>{html.escape(cname)}</h2><ul class="chips"><li><a href="/zakazky/{cslug}/"><strong>Všechny obory</strong></a></li>'
        + "".join(f'<li><a href="/zakazky/{s}-{cslug}/">{html.escape(t)}</a></li>' for s, (t, _, _) in SECTORS.items())
        + "</ul>" for cslug, (_, cname, _) in COUNTRIES.items())
    pages["/zakazky/"] = page("Aktuální veřejné zakázky v Česku a na Slovensku podle oboru | TenderWatch",
                              "Otevřené veřejné zakázky z Česka a Slovenska podle oboru, s lhůtami pro podání nabídek. Aktualizováno každý pracovní den.",
                              "/zakazky/", f'<h1>Aktuální veřejné zakázky</h1>{stamp}'
                              f'<p class="lede">{len(rows)} otevřených nadlimitních veřejných zakázek z Česka a Slovenska. Vyberte zemi a obor.</p>'
                              + blocks + cta("váš obor", "Česko i Slovensko"), css, footer)

    for path, content in pages.items():
        full = os.path.join(out, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(full), exist_ok=True)
        open(full, "w", encoding="utf-8").write(content)
    sm = "".join(f"<url><loc>{BASE}{u}</loc><lastmod>{today.isoformat()}</lastmod></url>" for u in urls)
    open(os.path.join(out, "sitemap.xml"), "w").write(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
    open(os.path.join(out, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    return {"open_tenders": len(rows), "pages": len(pages), "indexed": len(urls)}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--fixture"); ap.add_argument("--today")
    a = ap.parse_args()
    today = dt.date.fromisoformat(a.today) if a.today else dt.date.today()
    notices = json.load(open(a.fixture, encoding="utf-8")) if a.fixture else fetch()
    print(json.dumps(build(normalise(notices, today), today)))
