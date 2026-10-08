"""Offline test for gen_pages.py. Run: python test_pages.py"""
import datetime as dt, json, os, re, shutil, tempfile
import gen_pages as g

TODAY = dt.date(2026, 10, 5)
def n(nid, iso, cpv, title_ces, title_orig_key, title_orig, deadline):
    return {"publication-number": nid, "notice-type": "cn-standard", "buyer-country": [iso],
            "classification-cpv": [cpv], "buyer-name": {title_orig_key: ["Buyer " + nid]},
            "notice-title": {"ces": title_ces, title_orig_key: title_orig},
            "deadline-receipt-tender-date-lot": [deadline + "+01:00"], "publication-date": "2026-10-01+02:00"}

notices = [n(f"{700 + i}-2026", "DEU", "48000000", "Německo – Software – Digitale Plattform %d" % i, "deu",
             "Deutschland – Software – Digitale Plattform %d" % i, f"2026-11-{i + 1:02d}") for i in range(14)]
notices += [n("800-2026", "CZE", "72000000", "Česko – IT služby – Údržba systému", "ces", "Česko – IT služby – Údržba systému", "2026-11-10"),
            n("801-2026", "AUT", "45000000", "Rakousko – Stavební práce – Neubau Schule", "deu", "Österreich – Bauarbeiten – Neubau Schule", "2026-10-01")]  # expired

os.environ.pop("DEEPL_API_KEY", None)
tmp = tempfile.mkdtemp(); here = os.getcwd()
for f in ("index.html", "gen_pages.py", "guides.py", "sector_texts.py", "soukromi.html"): shutil.copy(f, tmp)
os.chdir(tmp)
calls = []
def fake(texts):
    calls.append(len(texts)); return ["Digitální platforma " + t.rsplit(" ", 1)[1] for t in texts]

dup = dict(notices[0]); dup["publication-number"] = "799-2026"      # same title+buyer, another lot
dup["buyer-name"] = notices[0]["buyer-name"]
rows = g.normalise(notices + [dup], TODAY)
assert len(rows) == 15                                      # expired Austrian one dropped, lot duplicate merged
stats = g.build(rows, TODAY, translator=fake)
page = open("_site/zakazky/it-software-nemecko/index.html", encoding="utf-8").read()
assert "<h1>Veřejné zakázky v Německu: IT a software</h1>" in page
assert page.count('<li><a class="tt"') == 10                # teaser capped at 10
assert "Digitální platforma 0</a>" in page and "Originál: Digitale Plattform 0" in page
assert "…a další 4 otevřené zakázky v tomto oboru." in page and "Aktuálně je 14 otevřených zakázek." in page
assert "strojově přeložené do češtiny" in page
cz = open("_site/zakazky/it-software-cesko/index.html", encoding="utf-8").read()
assert "Údržba systému</a>" in cz and "Originál" not in cz   # no translation for Czech tenders
assert 'name="robots" content="noindex' in cz               # only 1 tender → noindex
assert sum(calls) == 10                                      # only the 10 shown German titles were translated
before = sum(calls)
g.build(rows, TODAY, translator=fake)
assert sum(calls) == before                                  # second build served from cache
sm = open("_site/sitemap.xml").read()
assert "/zakazky/it-software-nemecko/" in sm and "/zakazky/it-software-cesko/" not in sm
assert "/navody/jak-podat-nabidku-v-nemecku/" in sm and "/navody/" in sm
guide = open("_site/navody/jak-podat-nabidku-v-polsku/index.html", encoding="utf-8").read()
assert "<h1>Jak se přihlásit do veřejné zakázky v Polsku</h1>" in guide and "JEDZ" in guide
assert 'href="/navody/jak-podat-nabidku-v-nemecku/"' in page          # sector page links its country guide
assert "gc.zgo.at/count.js" in page and page.count("gc.zgo.at") == 1  # analytics injected once
assert 'data-goatcounter-click="cta"' in page
home = open("_site/index.html", encoding="utf-8").read()
assert 'data-goatcounter-click="stripe-starter"' in home and 'data-goatcounter-click="stripe-pro"' in home
priv = open("_site/soukromi.html", encoding="utf-8").read()
assert "GoatCounter" in priv and priv.index("GoatCounter") < priv.index("</main>")
assert os.path.exists("_site/zakazky/ostraha-nemecko/index.html")
assert "Bauabzugsteuer" not in page and "EVB-IT" in page             # hand-written context on it-software-nemecko
assert page.count("/navody/jak-podat-nabidku-v-nemecku/") >= 1
jeo = open("_site/navody/jak-vyplnit-jeo-espd/index.html", encoding="utf-8").read()
assert "Část IV" in jeo and 'href="/navody/jak-podat-nabidku-v-polsku/"' in jeo   # general guide + related links
assert "/navody/elektronicky-podpis-nabidky-v-zahranici/" in sm
def broken(texts): raise RuntimeError("down")
os.remove(g.CACHE); g.build(rows, TODAY, translator=broken)  # translation failure never breaks the build
assert "Digitale Plattform 0</a>" in open("_site/zakazky/it-software-nemecko/index.html", encoding="utf-8").read()
os.remove(g.CACHE); g.build(rows, TODAY)                     # no key: originals, no crash
os.chdir(here); shutil.rmtree(tmp)
print("all page tests passed", stats)
