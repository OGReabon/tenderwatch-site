"""Czech how-to guides for bidding in foreign public tenders. Rendered by gen_pages.py into /navody/<slug>/.

Facts checked October 2026; thresholds are the EU thresholds valid from 1 January 2026 (excl. VAT).
Keep claims general and link to the official sources — rules differ per contracting authority.
"""

THRESHOLDS = """<h2>Od jaké hodnoty jde zakázka do celé EU</h2>
<p>Zakázky nad tzv. evropskými finančními limity se musí zveřejnit v Úředním věstníku EU (TED) a může se do nich přihlásit
kterákoli firma z EU za stejných podmínek jako domácí. Od 1.&nbsp;1.&nbsp;2026 platí (bez DPH):</p>
<ul>
<li><strong>stavební práce:</strong> 5&nbsp;404&nbsp;000&nbsp;€</li>
<li><strong>dodávky a služby – ústřední orgány státu:</strong> 140&nbsp;000&nbsp;€</li>
<li><strong>dodávky a služby – kraje, města, nemocnice a další zadavatelé:</strong> 216&nbsp;000&nbsp;€</li>
<li><strong>sektoroví zadavatelé (energetika, voda, doprava):</strong> 432&nbsp;000&nbsp;€ u dodávek a služeb</li>
</ul>
<p>Menší (podlimitní) zakázky se zveřejňují jen v národních systémech a v jazyce dané země.</p>"""

ESPD = """<p><strong>Jednotné evropské osvědčení pro veřejné zakázky (JEO, anglicky ESPD)</strong> je formulář, kterým
v nadlimitní zakázce předběžně čestně prohlásíte, že splňujete podmínky účasti. Originální doklady (výpis z rejstříku trestů,
potvrzení finančního úřadu, reference) pak zpravidla dokládá jen vybraný dodavatel. Zahraniční zadavatel nesmí odmítnout
české doklady jen proto, že jsou české — často ale chce jejich překlad. Jaké doklady se v které zemi vydávají, ukazuje
databáze <a href="https://ec.europa.eu/tools/ecertis/" rel="noopener">eCertis</a> Evropské komise.</p>"""

COMMON_TAIL = """<h2>Jak zakázky vůbec najít</h2>
<p>Všechny nadlimitní zakázky z celé EU jsou na portálu <a href="https://ted.europa.eu/cs/" rel="noopener">TED</a>.
Každý pracovní den jich přibude přes tisíc, většinou v jazyce zadavatele. TenderWatch je každé ráno projde za vás, vybere ty,
které odpovídají vašemu oboru a zemím, a pošle vám je e-mailem s názvem přeloženým do češtiny a s lhůtou pro podání nabídky.</p>
<p class="upd">Tento návod je obecný přehled, ne právní rada. Rozhodující jsou vždy zadávací podmínky konkrétní zakázky.
Aktualizováno v říjnu 2026.</p>"""

GUIDES = {
    "jak-podat-nabidku-v-nemecku": {
        "country": "nemecko",
        "title": "Jak se přihlásit do veřejné zakázky v Německu – návod pro české firmy",
        "h1": "Jak se přihlásit do veřejné zakázky v Německu",
        "desc": "Kde hledat německé veřejné zakázky, jak funguje e-Vergabe, v jakém jazyce podat nabídku a jaké doklady připravit. Praktický návod pro české firmy.",
        "body": """<p class="lede">Německo je největší trh veřejných zakázek v EU a pro české firmy nejbližší.
Zadavatelé z Bavorska a Saska běžně dostávají nabídky z Česka. Tady je, co potřebujete vědět, než podáte první nabídku.</p>
""" + THRESHOLDS + """
<h2>Kde se německé zakázky zveřejňují</h2>
<p>Německo nemá jeden povinný portál. Každý zadavatel používá některou z platforem pro elektronické zadávání
(<em>e-Vergabe</em>), například <a href="https://www.evergabe-online.de/" rel="noopener">evergabe-online.de</a> (spolkové úřady),
<a href="https://www.service.bund.de/" rel="noopener">service.bund.de</a> nebo zemské a komerční portály. Nadlimitní zakázky jsou
navíc vždy v TED a od roku 2024 je sbírá i centrální datová služba
<a href="https://oeffentlichevergabe.de/" rel="noopener">oeffentlichevergabe.de</a>. Odkaz na konkrétní platformu najdete v oznámení.</p>

<h2>Postup krok za krokem</h2>
<ol>
<li><strong>Stáhněte zadávací dokumentaci.</strong> Na platformách e-Vergabe je ke stažení zdarma; registrace (také zdarma) se vyplatí,
protože jen registrovaní dostávají upozornění na vysvětlení a změny zadávacích podmínek.</li>
<li><strong>Zkontrolujte podmínky účasti</strong> (<em>Eignungskriterien</em>): obrat, reference, pojištění, certifikace.</li>
<li><strong>Připravte JEO</strong> (německy <em>EEE – Einheitliche Europäische Eigenerklärung</em>) nebo vlastní čestná prohlášení,
pokud je zadavatel připustí.</li>
<li><strong>Podejte nabídku elektronicky</strong> přes platformu uvedenou v oznámení, nejpozději do lhůty (<em>Angebotsfrist</em>).
Nabídka podaná pozdě nebo e-mailem se nehodnotí.</li>
</ol>

<h2>V jakém jazyce</h2>
<p>Zadávací dokumentace i nabídka jsou prakticky vždy <strong>v němčině</strong>. Doklady v jiném jazyce zadavatel obvykle přijme
jen s německým překladem; úředně ověřený překlad chce jen někdy, záleží na zadávacích podmínkách. Dotazy k zadávací dokumentaci
(<em>Bieterfragen</em>) pokládejte také německy a přes platformu, ne telefonem.</p>

<h2>Podpis a forma nabídky</h2>
<p>U většiny nadlimitních zakázek na dodávky a služby stačí nabídka v tzv. <em>Textform</em> — tedy elektronicky bez kvalifikovaného
elektronického podpisu, s uvedením jména osoby, která nabídku podává. Pokud zadavatel výjimečně vyžaduje kvalifikovaný podpis,
uvede to v oznámení; český kvalifikovaný podpis je v celé EU uznávaný.</p>

<h2>Doklady a předkvalifikace</h2>
""" + ESPD + """
<p>Kdo se o německé zakázky uchází pravidelně, může se nechat zapsat do předkvalifikačních seznamů (<em>Präqualifizierung</em>,
pro stavebnictví seznam <a href="https://www.pq-verein.de/" rel="noopener">PQ-VOB</a>, pro dodávky a služby
<a href="https://amtliches-verzeichnis.ihk.de/" rel="noopener">AVPQ</a> u obchodních komor). Zápis pak nahrazuje většinu
jednotlivých dokladů v každé nabídce.</p>

<h2>Na co si dát pozor</h2>
<ul>
<li><strong>Mzdové zákony.</strong> V řadě spolkových zemí platí zákony o dodržování tarifních mezd (<em>Tariftreuegesetze</em>) a
k nabídce se přikládá prohlášení o jejich dodržení. Pro práci v Německu platí také německá minimální mzda a pravidla vysílání pracovníků.</li>
<li><strong>Wettbewerbsregister.</strong> U zakázek od 30&nbsp;000&nbsp;€ si zadavatel ověřuje vybraného dodavatele v rejstříku
vyloučených firem. U zahraniční firmy to obvykle doplňuje výpisem z rejstříku trestů.</li>
<li><strong>Zakázky jsou rozdělené na části</strong> (<em>Lose</em>). Často se vyplatí podat nabídku jen na jednu regionální část.</li>
</ul>
""" + COMMON_TAIL,
    },
    "jak-podat-nabidku-v-rakousku": {
        "country": "rakousko",
        "title": "Jak se přihlásit do veřejné zakázky v Rakousku – návod pro české firmy",
        "h1": "Jak se přihlásit do veřejné zakázky v Rakousku",
        "desc": "Kde hledat rakouské veřejné zakázky, jak funguje USP a ANKÖ, v jakém jazyce podat nabídku a jaké doklady připravit. Praktický návod pro české firmy.",
        "body": """<p class="lede">Rakousko má relativně malý, ale dobře přehledný trh veřejných zakázek a české firmy z jižních Čech a Moravy
na něm uspívají hlavně ve stavebnictví, strojírenství a IT. Přehled toho podstatného:</p>
""" + THRESHOLDS + """
<h2>Kde se rakouské zakázky zveřejňují</h2>
<p>Centrálním přehledem je spolková služba <em>Ausschreibungen Austria</em> na portálu <a href="https://www.usp.gv.at/" rel="noopener">USP</a>,
kam zadavatelé podle zákona o zadávání (<em>BVergG 2018</em>) hlásí základní údaje o zakázkách včetně podlimitních. Samotné nabídky
se podávají přes elektronickou platformu, kterou zadavatel uvede v oznámení — často <a href="https://www.auftrag.at/" rel="noopener">auftrag.at</a>
(ANKÖ), <a href="https://www.vemap.com/" rel="noopener">vemap</a> nebo platformy zemských vlád. Nadlimitní zakázky jsou vždy i v TED.</p>

<h2>Postup krok za krokem</h2>
<ol>
<li><strong>Zaregistrujte se na platformě</strong> uvedené v oznámení a stáhněte zadávací dokumentaci.</li>
<li><strong>Ověřte podmínky účasti</strong> (<em>Eignung</em>): oprávnění k podnikání v oboru, finanční a technická způsobilost, reference.</li>
<li><strong>Připravte JEO</strong> nebo čestné prohlášení (<em>Eigenerklärung</em>), které zadavatel připouští.</li>
<li><strong>Podejte nabídku elektronicky</strong> v systému do konce lhůty (<em>Angebotsfrist</em>). U nadlimitních zakázek je elektronické
podání povinné; zda je nutný kvalifikovaný elektronický podpis, stanoví zadávací podmínky. Český kvalifikovaný podpis Rakousko uznává.</li>
</ol>

<h2>V jakém jazyce</h2>
<p>Řízení probíhá <strong>v němčině</strong> a nabídka se podává německy, pokud zadavatel výslovně nepřipustí jiný jazyk.
Doklady v češtině přikládejte s německým překladem. Pozor na rakouskou terminologii — <em>Leistungsverzeichnis</em> (soupis prací)
často vychází ze standardizovaných rakouských katalogů, které je potřeba vyplnit přesně podle předlohy.</p>

<h2>Doklady a seznam ANKÖ</h2>
""" + ESPD + """
<p>V Rakousku se hodně využívá <a href="https://www.ankoe.at/" rel="noopener">seznam způsobilých podniků ANKÖ</a>
(<em>Liste geeigneter Unternehmen</em>). Firma do něj jednou nahraje doklady o způsobilosti a zadavatelé si je pak ověří sami,
místo aby je chtěli u každé nabídky. Zápis je placený (podle rozsahu zhruba od 80 do 340&nbsp;€ ročně bez DPH), zahraniční firmy
se mohou zapsat také. Pro občasnou nabídku není nutný.</p>

<h2>Na co si dát pozor</h2>
<ul>
<li><strong>Oprávnění k podnikání.</strong> Pro výkon prací v Rakousku (zejména řemesel a stavebních prací) může být potřeba
oznámení nebo uznání kvalifikace podle rakouského živnostenského řádu.</li>
<li><strong>Vysílání pracovníků.</strong> Práce na místě podléhá rakouským minimálním mzdám podle kolektivních smluv a předchozímu
hlášení vyslaných zaměstnanců (ZKO).</li>
<li><strong>Lhůty pro námitky jsou krátké</strong> — obvykle 10 dní (v elektronické komunikaci) od oznámení rozhodnutí zadavatele.</li>
</ul>
""" + COMMON_TAIL,
    },
    "jak-podat-nabidku-v-polsku": {
        "country": "polsko",
        "title": "Jak se přihlásit do veřejné zakázky v Polsku – návod pro české firmy",
        "h1": "Jak se přihlásit do veřejné zakázky v Polsku",
        "desc": "Jak funguje polská platforma e-Zamówienia, v jakém jazyce podat nabídku, co je JEDZ a wadium a jaké doklady připravit. Praktický návod pro české firmy.",
        "body": """<p class="lede">Polsko patří k největším trhům veřejných zakázek ve střední Evropě a díky evropským fondům vypisuje velké
zakázky na infrastrukturu, IT i vybavení nemocnic. Pro české firmy je jazykově i geograficky blízko. Co je dobré vědět:</p>
""" + THRESHOLDS + """
<h2>Kde se polské zakázky zveřejňují</h2>
<p>Hlavním systémem je státní platforma <a href="https://ezamowienia.gov.pl/" rel="noopener">e-Zamówienia</a>. Je na ní národní věstník
(<em>Biuletyn Zamówień Publicznych</em>) s podlimitními zakázkami a přes ni se ve velké části řízení i podávají nabídky. Část zadavatelů
používá vlastní certifikované platformy (např. platformazakupowa.pl), odkaz je vždy v oznámení. Nadlimitní zakázky jsou i v TED.</p>

<h2>Postup krok za krokem</h2>
<ol>
<li><strong>Založte si účet na e-Zamówienia</strong> a přidejte k němu svou firmu. Pro zahraniční firmy je postup popsaný
v anglických návodech na portálu; s registrací pomáhá i helpdesk (+48&nbsp;22&nbsp;458&nbsp;77&nbsp;99).</li>
<li><strong>Stáhněte zadávací dokumentaci</strong> (<em>SWZ – specyfikacja warunków zamówienia</em>) a přečtěte si podmínky účasti
(<em>warunki udziału</em>) a důvody vyloučení.</li>
<li><strong>Vyplňte JEO</strong> (polsky <em>JEDZ – Jednolity Europejski Dokument Zamówienia</em>), který je u nadlimitních zakázek povinný.</li>
<li><strong>Složte jistotu, pokud ji zadavatel chce</strong> (<em>wadium</em>). U nadlimitních zakázek může činit až 3&nbsp;% předpokládané
hodnoty a lze ji poskytnout převodem nebo bankovní či pojišťovací zárukou.</li>
<li><strong>Podepište a podejte nabídku elektronicky.</strong> U nadlimitních zakázek musí být nabídka podepsaná
<strong>kvalifikovaným elektronickým podpisem</strong>; český kvalifikovaný podpis Polsko uznává.</li>
</ol>

<h2>V jakém jazyce</h2>
<p>Zadávací řízení se podle polského zákona o zadávání veřejných zakázek (<em>Prawo zamówień publicznych</em>) vede <strong>v polštině</strong>.
Zadavatel může výjimečně připustit i jiný jazyk, ale počítejte s tím, že nabídku podáte polsky a doklady v češtině přiložíte
s polským překladem. Polština je češtině blízká, u odborných a právních textů se ale vyplatí profesionální překladatel.</p>

<h2>Doklady</h2>
""" + ESPD + """

<h2>Na co si dát pozor</h2>
<ul>
<li><strong>Lhůty jsou striktní</strong> a platforma po jejich uplynutí nabídku nepřijme. Nahrávání velkých souborů a podepisování
nechte s rezervou.</li>
<li><strong>Vysvětlení zadávací dokumentace</strong> se zveřejňuje na stránce zakázky — sledujte ji až do podání nabídky.</li>
<li><strong>Odvolání</strong> se podává ke Krajowa Izba Odwoławcza a lhůty jsou krátké (obvykle 10 dní u nadlimitních zakázek).</li>
</ul>
""" + COMMON_TAIL,
    },
}
