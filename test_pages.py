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
for f in ("index.html", "gen_pages.py"): shutil.copy(f, tmp)
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
assert "…a dalších 4 otevřené zakázky v tomto oboru." in page
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
def broken(texts): raise RuntimeError("down")
os.remove(g.CACHE); g.build(rows, TODAY, translator=broken)  # translation failure never breaks the build
assert "Digitale Plattform 0</a>" in open("_site/zakazky/it-software-nemecko/index.html", encoding="utf-8").read()
os.remove(g.CACHE); g.build(rows, TODAY)                     # no key: originals, no crash
os.chdir(here); shutil.rmtree(tmp)
print("all page tests passed", stats)
