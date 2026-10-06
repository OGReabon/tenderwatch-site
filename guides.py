"""Czech how-to guides for bidding in foreign public tenders. Rendered by gen_pages.py into /navody/<slug>/.

Facts checked October 2026; thresholds are the EU thresholds valid from 1 January 2026 (excl. VAT).
Keep claims general and link to the official sources — rules differ per contracting authority.
"""

THRESHOLDS = """<h2>Kdy je zakázka otevřená firmám z celé EU</h2>
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
které odpovídají vašemu oboru a zemím, a pošle vám je e-mailem s názvem přeloženým do češtiny a lhůtou pro podání nabídek.</p>
<p class="upd">Tento návod je obecný přehled, ne právní rada. Rozhodující jsou vždy zadávací podmínky konkrétní zakázky.
Aktualizováno v říjnu 2026.</p>"""

GUIDES = {
    "jak-podat-nabidku-v-nemecku": {
        "country": "nemecko",
        "title": "Jak se přihlásit do veřejné zakázky v Německu – návod pro české firmy",
        "h1": "Jak se přihlásit do veřejné zakázky v Německu",
        "desc": "Kde hledat německé veřejné zakázky, jak funguje e-Vergabe, v jakém jazyce podat nabídku a jaké doklady připravit. Praktický návod pro české firmy.",
        "body": """<p class="lede">Německo je největší trh veřejných zakázek v EU a pro české firmy nejbližší.
Pro firmy ze západních a severních Čech bývají zakázky v Bavorsku a Sasku blíž než ty na druhém konci republiky. Tady je, co potřebujete vědět, než podáte první nabídku.</p>
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
<li><strong>Podejte nabídku elektronicky</strong> přes platformu uvedenou v oznámení, nejpozději do konce lhůty (<em>Angebotsfrist</em>).
Nabídka podaná pozdě nebo e-mailem se nehodnotí.</li>
</ol>

<h2>V jakém jazyce</h2>
<p>Zadávací dokumentace i nabídka jsou prakticky vždy <strong>v němčině</strong>. Doklady v jiném jazyce zadavatel obvykle přijme
jen s německým překladem; úředně ověřený překlad chce jen někdy, záleží na zadávacích podmínkách. Dotazy k zadávací dokumentaci
(<em>Bieterfragen</em>) kladte také německy, a to přes platformu, ne telefonem.</p>

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
k nabídce se přikládá prohlášení o jejich dodržování. Pro práci v Německu platí také německá minimální mzda a pravidla vysílání pracovníků.</li>
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
        "body": """<p class="lede">Rakousko má menší, ale přehledný trh veřejných zakázek a pro firmy z jižních Čech a jižní Moravy je doslova za humny.
Přehled toho podstatného:</p>
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
zakázky na infrastrukturu, IT i vybavení nemocnic. Pro české firmy je blízko jazykově i geograficky. Co je dobré vědět:</p>
""" + THRESHOLDS + """
<h2>Kde se polské zakázky zveřejňují</h2>
<p>Hlavním systémem je státní platforma <a href="https://ezamowienia.gov.pl/" rel="noopener">e-Zamówienia</a>. Je na ní národní věstník
(<em>Biuletyn Zamówień Publicznych</em>) s podlimitními zakázkami a přes ni se ve velké části řízení i podávají nabídky. Část zadavatelů
používá vlastní certifikované platformy (např. platformazakupowa.pl), odkaz je vždy v oznámení. Nadlimitní zakázky jsou i v TED.</p>

<h2>Postup krok za krokem</h2>
<ol>
<li><strong>Založte si účet na platformě e-Zamówienia</strong> a přidejte k němu svou firmu. Pro zahraniční firmy je postup popsaný
v anglických návodech na portálu; s registrací pomáhá i helpdesk (+48&nbsp;22&nbsp;458&nbsp;77&nbsp;99).</li>
<li><strong>Stáhněte zadávací dokumentaci</strong> (<em>SWZ – specyfikacja warunków zamówienia</em>) a přečtěte si podmínky účasti
(<em>warunki udziału</em>) a důvody vyloučení.</li>
<li><strong>Vyplňte JEO</strong> (polsky <em>JEDZ – Jednolity Europejski Dokument Zamówienia</em>), který je u nadlimitních zakázek povinný.</li>
<li><strong>Složte jistotu</strong> (<em>wadium</em>), pokud ji zadavatel požaduje. U nadlimitních zakázek může činit až 3&nbsp;% předpokládané
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
    "jak-vyplnit-jeo-espd": {
        "country": None,
        "title": "Jak vyplnit JEO (ESPD) pro zahraniční veřejnou zakázku – návod",
        "h1": "Jak vyplnit JEO (ESPD) pro zahraniční zakázku",
        "desc": "Co je Jednotné evropské osvědčení pro veřejné zakázky (JEO, ESPD, EEE, JEDZ), jak ho vyplnit po částech a na co si dát pozor u zahraničních zadavatelů.",
        "body": """<p class="lede">Jednotné evropské osvědčení pro veřejné zakázky (JEO) je stejný formulář ve všech zemích EU.
Kdo ho jednou vyplní pro českou zakázku, zvládne ho i pro německou nebo polskou. Liší se jen název a jazyk.</p>

<h2>Co JEO je a k čemu slouží</h2>
<p>JEO je čestné prohlášení, kterým v nadlimitní zakázce předběžně potvrdíte, že nejste vyloučeni (například kvůli trestnému
činu nebo dluhům na daních) a že splňujete podmínky účasti, které zadavatel stanovil. Originální doklady pak zpravidla
dokládá jen dodavatel, kterého zadavatel vybere. Formulář vychází z prováděcího nařízení Komise (EU) 2016/7.</p>
<ul>
<li><strong>Česky:</strong> JEO – Jednotné evropské osvědčení pro veřejné zakázky</li>
<li><strong>Anglicky:</strong> ESPD – European Single Procurement Document</li>
<li><strong>Německy:</strong> EEE – Einheitliche Europäische Eigenerklärung</li>
<li><strong>Polsky:</strong> JEDZ – Jednolity Europejski Dokument Zamówienia</li>
</ul>

<h2>Kde formulář získáte</h2>
<p>Zadavatel ho obvykle přikládá k zadávací dokumentaci jako soubor (často XML, který načtete do nástroje pro vyplnění, nebo PDF/Word),
případně ho vyplníte přímo v elektronické platformě, přes kterou se podává nabídka. Vždy použijte verzi od zadavatele —
část I je v ní už předvyplněná údaji o zakázce.</p>

<h2>Vyplnění po částech</h2>
<ol>
<li><strong>Část I – informace o zakázce.</strong> Vyplňuje zadavatel. Jen zkontrolujte, že jde o správnou zakázku a část (<em>Los</em>, <em>część</em>).</li>
<li><strong>Část II – informace o vás.</strong> Název, IČO (uveďte i DIČ / VAT ID), adresa, kontakt, velikost firmy (malý a střední podnik ano/ne),
kdo firmu zastupuje. Pokud se spoléháte na kapacity jiné firmy (subdodavatele), uvádí se to zde a ta firma předkládá vlastní JEO.</li>
<li><strong>Část III – důvody vyloučení.</strong> Prohlášení o trestných činech, daních, sociálním a zdravotním pojištění, úpadku a dalších
důvodech. U většiny firem jsou odpovědi „ne“. Kde je to možné, uveďte odkaz na veřejný rejstřík, ve kterém si to zadavatel ověří.</li>
<li><strong>Část IV – kritéria pro výběr.</strong> Obrat, pojištění, reference, certifikáty. Zadavatel někdy dovolí vyplnit jen souhrnnou
odpověď (tzv. oddíl α – „splňuji všechna požadovaná kritéria“). Jinak vyplňte konkrétní údaje přesně podle požadavků v oznámení.</li>
<li><strong>Část V – omezení počtu účastníků.</strong> Jen v užších řízeních a jednacích řízeních, kde zadavatel vybírá omezený počet firem.</li>
<li><strong>Část VI – závěrečné prohlášení a podpis.</strong> Podepisuje osoba oprávněná jednat za firmu, způsobem, který zadavatel požaduje
(viz <a href="/navody/elektronicky-podpis-nabidky-v-zahranici/">elektronický podpis v zahraničí</a>).</li>
</ol>

<h2>Na co si dát pozor</h2>
<ul>
<li><strong>Jazyk.</strong> Formulář je ve všech jazycích EU stejný, odpovědi ale pište v jazyce zadávacího řízení.</li>
<li><strong>Nepravdivé údaje</strong> jsou důvodem k vyloučení i v jiných zakázkách. Co neumíte doložit, neuvádějte.</li>
<li><strong>Doklady mějte připravené dopředu.</strong> Po výběru bývá na jejich předložení jen několik dní. Které doklady se v jiné zemi
vydávají místo českých, ukazuje databáze <a href="https://ec.europa.eu/tools/ecertis/" rel="noopener">eCertis</a>.</li>
<li><strong>Podlimitní zakázky</strong> JEO často nevyžadují; zadavatel pak chce vlastní formulář čestného prohlášení.</li>
</ul>
""" + COMMON_TAIL,
    },
    "preklad-dokladu-zahranicni-zakazka": {
        "country": None,
        "title": "Překlad dokladů pro zahraniční veřejnou zakázku – kdy stačí prostý a kdy úřední",
        "h1": "Překlad dokladů pro zahraniční veřejnou zakázku",
        "desc": "Které doklady do zahraniční veřejné zakázky překládat, kdy stačí prostý překlad a kdy je potřeba úřední, a jak ušetřit pomocí vícejazyčných formulářů EU.",
        "body": """<p class="lede">Zahraniční zadavatel nesmí české doklady odmítnout jen proto, že jsou české. Téměř vždy ale chce překlad
do svého jazyka. Dobrá zpráva: úřední překlad bývá potřeba méně často, než se firmy obávají.</p>

<h2>Co se obvykle překládá</h2>
<ul>
<li>výpis z obchodního nebo živnostenského rejstříku,</li>
<li>výpis z rejstříku trestů firmy a statutárních orgánů,</li>
<li>potvrzení o bezdlužnosti (finanční úřad, sociální a zdravotní pojištění),</li>
<li>reference, osvědčení o odborné způsobilosti a certifikáty,</li>
<li>případně pojistná smlouva nebo výkazy (obrat).</li>
</ul>
<p>Certifikáty vydané v mezinárodně používaném znění (ISO certifikáty bývají dvojjazyčné) překládat obvykle nemusíte.</p>

<h2>Prostý, nebo úřední překlad?</h2>
<p>Rozhoduje zadávací dokumentace. Ve většině řízení stačí <strong>prostý překlad</strong> — překlad, který si můžete nechat udělat
kýmkoli. <strong>Úřední překlad</strong> (v Česku soudní tlumočník s pečetí, v Německu <em>beglaubigte Übersetzung</em>,
v Polsku <em>tłumaczenie przysięgłe</em>) chtějí zadavatelé hlavně u dokladů, které mají právní účinky, nebo když mají o správnosti
překladu pochybnost. Pokud dokumentace nic neříká, zeptejte se v rámci dotazů k zadávací dokumentaci — je to běžný dotaz.</p>

<h2>Jak ušetřit</h2>
<ul>
<li><strong>Apostila mezi zeměmi EU obvykle není potřeba.</strong> Nařízení (EU) 2016/1191 zrušilo ověřování u řady veřejných listin
mezi členskými státy. K vybraným listinám (mimo jiné k výpisu z rejstříku trestů) lze navíc získat
<strong>vícejazyčný standardní formulář</strong>, který překlad nahrazuje.</li>
<li><strong>Využijte veřejné rejstříky.</strong> Do JEO uveďte odkaz na veřejně dostupný rejstřík; zadavatel si údaje ověří sám
a překlad celého výpisu pak často nevyžaduje.</li>
<li><strong>Nechte si přeložit „sadu“ jednou.</strong> Doklady jako výpis z rejstříku nebo reference se v nabídkách opakují.
Kvalitní překlad do němčiny nebo polštiny se vám vrátí v dalších zakázkách — jen hlídejte stáří dokladů (často max. 3 měsíce).</li>
</ul>

<h2>Na co si dát pozor</h2>
<ul>
<li><strong>Stáří dokladu</strong> se počítá od vydání originálu, ne od překladu.</li>
<li><strong>Překládejte i razítka a poznámky</strong> na dokladech, nejen hlavní text.</li>
<li><strong>Nabídka samotná</strong> (cena, technický popis, výkaz výměr) se překladem nedokládá — píše se rovnou v jazyce řízení.</li>
</ul>
""" + COMMON_TAIL,
    },
    "jistota-wadium-zahranicni-zakazka": {
        "country": None,
        "title": "Jistota (Vadium, wadium, bid bond) v zahraniční veřejné zakázce – návod",
        "h1": "Jistota v zahraniční zakázce: Vadium, wadium, bid bond",
        "desc": "Co je jistota za nabídku (Vadium, wadium, bid bond), kdy ji zahraniční zadavatelé chtějí, v jaké formě ji složit a kdy o ni můžete přijít.",
        "body": """<p class="lede">Jistota je peněžní záruka, kterou zadavatel může požadovat spolu s nabídkou. Chrání ho pro případ, že vybraný
dodavatel smlouvu nakonec nepodepíše. V Polsku je běžná, v Německu u nabídek spíše výjimečná. Než ji složíte, ověřte si formu a lhůty.</p>

<h2>Jak se jí říká</h2>
<ul>
<li><strong>Česko:</strong> jistota (poskytnutí jistoty)</li>
<li><strong>Polsko:</strong> <em>wadium</em></li>
<li><strong>Rakousko:</strong> <em>Vadium</em></li>
<li><strong>Německo:</strong> <em>Sicherheitsleistung</em> / <em>Bietersicherheit</em></li>
<li><strong>Anglicky:</strong> bid bond, tender guarantee</li>
</ul>

<h2>Kdy ji zadavatelé chtějí</h2>
<p>Zda a v jaké výši jistotu požaduje, uvádí zadavatel v oznámení a zadávací dokumentaci. <strong>V Polsku</strong> je wadium častou
součástí větších zakázek; u nadlimitních zakázek může činit až 3&nbsp;% předpokládané hodnoty. <strong>V Rakousku</strong> se Vadium
objevuje hlavně ve stavebnictví. <strong>V Německu</strong> se jistota za nabídku vyžaduje jen zřídka — běžnější je záruka
za řádné plnění nebo za vady, kterou skládá až vítěz.</p>

<h2>V jaké formě</h2>
<ol>
<li><strong>Převod peněz</strong> na účet zadavatele. Nejjednodušší způsob, peníze jsou ale vázané až do výběru vítěze
(a u odvolání i déle). Počítejte s tím, že platba musí být <em>připsaná</em> před koncem lhůty pro podání nabídek.</li>
<li><strong>Bankovní záruka.</strong> Vystaví ji vaše banka; stojí poplatek a banka si obvykle hlídá úvěrový rámec.</li>
<li><strong>Pojišťovací záruka</strong> (v Polsku <em>gwarancja ubezpieczeniowa</em>). Bývá levnější a rychlejší; nabízí ji řada pojišťoven
i pro české firmy.</li>
</ol>
<p>U elektronických řízení musí být záruka zpravidla <strong>v elektronické podobě podepsané vystavitelem</strong> a podaná spolu s nabídkou.
Pozor na znění: záruka musí být neodvolatelná, na požádání (bez námitek) a platit po celou dobu, po kterou je nabídka závazná.
Zadavatelé často přikládají vzor; banka nebo pojišťovna by se ho měla držet.</p>

<h2>Kdy o jistotu přijdete</h2>
<ul>
<li>když po výběru odmítnete uzavřít smlouvu nebo ji neuzavřete včas,</li>
<li>když nedodáte požadované doklady nebo nesložíte záruku za plnění,</li>
<li>když se ukáže, že údaje v nabídce byly nepravdivé.</li>
</ul>
<p>Ostatním účastníkům zadavatel jistotu vrací po skončení řízení; lhůty stanoví národní zákon.</p>
""" + COMMON_TAIL,
    },
    "elektronicky-podpis-nabidky-v-zahranici": {
        "country": None,
        "title": "Elektronický podpis nabídky v zahraniční veřejné zakázce – platí český?",
        "h1": "Elektronický podpis nabídky v zahraniční zakázce",
        "desc": "Platí český kvalifikovaný elektronický podpis v německých, rakouských a polských zakázkách? Kdy je podpis potřeba, jaký formát zvolit a jak ho ověřit.",
        "body": """<p class="lede">Ano — český kvalifikovaný elektronický podpis platí v celé EU. Rozhodující je, jestli ho zadavatel vůbec vyžaduje
a v jakém formátu soubory podepsat.</p>

<h2>Proč český podpis platí všude</h2>
<p>Nařízení eIDAS (EU) č.&nbsp;910/2014 stanoví, že kvalifikovaný elektronický podpis založený na kvalifikovaném certifikátu vydaném
v jednom členském státě se uznává ve všech ostatních. Seznam kvalifikovaných poskytovatelů je veřejný v
<a href="https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls" rel="noopener">EU Trust List</a>.
V Česku kvalifikované certifikáty vydávají například PostSignum (Česká pošta), I.CA nebo eIdentity.</p>

<h2>Kvalifikovaný, zaručený, nebo žádný?</h2>
<ul>
<li><strong>Kvalifikovaný podpis</strong> — kvalifikovaný certifikát + kvalifikované zařízení (čipová karta, token nebo vzdálené podepisování
u poskytovatele). Má účinky vlastnoručního podpisu a vyhoví všude.</li>
<li><strong>Zaručený podpis s kvalifikovaným certifikátem</strong> — certifikát je kvalifikovaný, ale uložený například jen v počítači.
Některým zadavatelům stačí, jiným ne.</li>
<li><strong>Bez podpisu</strong> — v Německu u většiny zakázek stačí <em>Textform</em>, tedy nabídka podaná přes platformu se jménem osoby.</li>
</ul>

<h2>Co chtějí jednotlivé země</h2>
<ul>
<li><strong>Německo:</strong> obvykle stačí <em>Textform</em>; pokud zadavatel výjimečně chce kvalifikovaný podpis, uvede to v oznámení.
Viz <a href="/navody/jak-podat-nabidku-v-nemecku/">návod pro Německo</a>.</li>
<li><strong>Rakousko:</strong> záleží na zadávacích podmínkách a platformě; kvalifikovaný podpis bývá požadován častěji.
Viz <a href="/navody/jak-podat-nabidku-v-rakousku/">návod pro Rakousko</a>.</li>
<li><strong>Polsko:</strong> nabídka v nadlimitní zakázce musí být podepsaná kvalifikovaným elektronickým podpisem.
Viz <a href="/navody/jak-podat-nabidku-v-polsku/">návod pro Polsko</a>.</li>
</ul>

<h2>Formát podpisu</h2>
<p>PDF se nejčastěji podepisují ve formátu <strong>PAdES</strong> (podpis je přímo v PDF), ostatní soubory ve formátu <strong>XAdES</strong>
nebo <strong>CAdES</strong> (podpis v samostatném souboru, případně obálce). Platformy často podepisování nabízejí přímo v prohlížeči
nebo uvádějí, které formáty přijímají. Podepisujte finální verzi — každá změna souboru po podpisu ho zneplatní.</p>

<h2>Jak si podpis předem ověřit</h2>
<ol>
<li>Podepište zkušební soubor stejným postupem, jakým budete podepisovat nabídku.</li>
<li>Nahrajte ho do bezplatného validátoru Evropské komise
<a href="https://ec.europa.eu/digital-building-blocks/DSS/webapp-demo/validation" rel="noopener">DSS Demonstration WebApp</a>.
Výsledek by měl být „TOTAL_PASSED“ a podpis by měl být označen jako kvalifikovaný (QES).</li>
<li>Zkontrolujte platnost certifikátu — musí platit v okamžiku podpisu. Obnovu neodkládejte na poslední týden před lhůtou.</li>
</ol>
""" + COMMON_TAIL,
    },
}
