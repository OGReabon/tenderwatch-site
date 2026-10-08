"""Hand-written context for the most important sector/country pages (/zakazky/<sector>-<country>/).
Gives each page its own substance beyond the generated tender list. Facts checked October 2026;
keep claims general — rules differ per contracting authority.
"""

TEXTS = {
    "stavby-nemecko": {
        "h2": "Stavební zakázky v Německu: co je dobré vědět",
        "body": """<p>Většinu stavebních zakázek v Německu vypisují obce, okresy a spolkové země: školy, školky, úpravy silnic,
sportoviště, rekonstrukce úředních budov. Zadávání stavebních prací se řídí pravidly <em>VOB/A</em> a smlouvy obvykle
vycházejí z obchodních podmínek <em>VOB/B</em>. Kdo je zná, rozumí většině německých stavebních zadávacích dokumentací.</p>
<ul>
<li><strong>Zakázky se dělí podle řemesel</strong> (<em>Fachlose</em>): zvlášť zemní práce, hrubá stavba, elektro, vzduchotechnika, okna.
Menší firma tak může soutěžit jen o svou část, ne o celou stavbu.</li>
<li><strong>Soupis prací</strong> (<em>Leistungsverzeichnis</em>) se často předává ve formátu GAEB. Rozpočtový software, který GAEB
umí načíst a vyexportovat, ušetří hodiny přepisování.</li>
<li><strong>Srážková daň ze stavebních prací</strong> (<em>Bauabzugsteuer</em>): objednatel strhává 15&nbsp;% z každé faktury, pokud
nepředložíte potvrzení o osvobození (<em>Freistellungsbescheinigung</em>) od německého finančního úřadu. O potvrzení požádejte
s předstihem, vyřízení trvá týdny.</li>
<li><strong>Řemeslné práce</strong> mohou vyžadovat oznámení nebo uznání kvalifikace u německé řemeslné komory, minimální mzdu
a nahlášení vyslaných pracovníků.</li>
</ul>
<p>Kdo podává nabídky pravidelně, ušetří čas zápisem do předkvalifikačního seznamu PQ-VOB.
Podrobnosti v návodu <a href="/navody/jak-podat-nabidku-v-nemecku/">Jak se přihlásit do veřejné zakázky v Německu</a>.</p>""",
    },
    "it-software-nemecko": {
        "h2": "IT zakázky v Německu: co je dobré vědět",
        "body": """<p>IT nakupují v Německu ministerstva, spolkové a zemské úřady, nemocnice, univerzity i obce. Velkou část zakázek
vypisují veřejní IT provozovatelé, například ITZBund (pro spolkovou správu) nebo Dataport (pro několik severních spolkových zemí).
Časté jsou rámcové smlouvy na několik let.</p>
<ul>
<li><strong>Smluvní vzory EVB-IT.</strong> Většina IT smluv státní správy vychází ze standardizovaných podmínek
<em>EVB-IT</em> (zvlášť pro nákup hardwaru, softwaru, služeb nebo vývoje). Vyplatí se je projít předem, odchylky obvykle
vyjednat nejdou.</li>
<li><strong>Hodnocení podle UfAB.</strong> Spolkové úřady často hodnotí nabídky metodikou <em>UfAB</em>, která kombinuje cenu
a kvalitu podle bodovací tabulky. Kritéria a váhy jsou v zadávací dokumentaci, takže se dá cílit přesně na body.</li>
<li><strong>Ochrana dat a bezpečnost.</strong> U cloudu a provozu systémů se běžně požaduje zpracování dat v EU, smlouva podle
GDPR a někdy doložení bezpečnostních standardů (například BSI C5 u cloudových služeb).</li>
<li><strong>Jazyk.</strong> Nabídka, dokumentace a často i podpora uživatelů musí být v němčině.</li>
</ul>
<p>Postup podání krok za krokem najdete v návodu <a href="/navody/jak-podat-nabidku-v-nemecku/">Jak se přihlásit do veřejné zakázky
v Německu</a>.</p>""",
    },
    "zdravotnictvi-nemecko": {
        "h2": "Zakázky ve zdravotnictví v Německu: co je dobré vědět",
        "body": """<p>Zdravotnické přístroje, spotřební materiál a vybavení nakupují v Německu hlavně veřejné a univerzitní nemocnice
a zemské a obecní kliniky. Řada nemocnic nakupuje přes nákupní sdružení, takže jedna zakázka může pokrýt dodávky pro
desítky zařízení. Digitalizaci nemocnic v posledních letech financuje spolkový program <em>Krankenhauszukunftsgesetz</em>
(KHZG), proto přibylo i zakázek na nemocniční software a IT.</p>
<ul>
<li><strong>Označení CE podle MDR</strong> je podmínkou pro zdravotnické prostředky; zadavatelé často chtějí kopie certifikátů
a prohlášení o shodě už v nabídce.</li>
<li><strong>Návod k použití v němčině.</strong> Nařízení MDR vyžaduje informace pro uživatele v jazyce státu, kde se prostředek
používá. Počítejte s německou dokumentací a často i se školením personálu v němčině.</li>
<li><strong>Servis.</strong> U přístrojů se hodnotí i dostupnost servisu, doba odezvy a náhradní díly. Smluvní servisní partner
v Německu bývá výhoda.</li>
<li><strong>Rámcové smlouvy</strong> na spotřební materiál běží obvykle 2–4 roky; o odběr se pak soutěží v jednotlivých objednávkách.</li>
</ul>
<p>Obecný postup podání nabídky: <a href="/navody/jak-podat-nabidku-v-nemecku/">Jak se přihlásit do veřejné zakázky v Německu</a>.</p>""",
    },
    "stavby-rakousko": {
        "h2": "Stavební zakázky v Rakousku: co je dobré vědět",
        "body": """<p>Rakouské stavební zakázky vypisují hlavně obce, spolkové země, ÖBB (železnice), ASFINAG (dálnice) a bytová
družstva s veřejnou podporou. Pro firmy z jižních Čech a jižní Moravy jsou často blíž než zakázky na druhém konci republiky.</p>
<ul>
<li><strong>Smluvní podmínky ÖNORM B 2110.</strong> Většina stavebních smluv se na tuto normu odkazuje; upravuje fakturaci,
změny, přejímky i záruky.</li>
<li><strong>Standardizované soupisy prací.</strong> Rakouští zadavatelé používají standardní popisy položek
(<em>Leistungsbeschreibungen</em>, např. pro pozemní stavby nebo dopravní infrastrukturu). Položky musíte ocenit přesně podle
předlohy, vlastní úpravy textu nejsou dovolené.</li>
<li><strong>Nejen nejnižší cena.</strong> U stavebních zakázek nad 1 milion € musí zadavatel podle rakouského zákona hodnotit
ekonomicky nejvýhodnější nabídku (<em>Bestbieterprinzip</em>), tedy i kvalitu, lhůty nebo zkušenosti týmu.</li>
<li><strong>Vysílání pracovníků.</strong> Práce na místě podléhá rakouským kolektivním mzdám a předchozímu nahlášení vyslaných
zaměstnanců; kontroly jsou časté a pokuty vysoké.</li>
</ul>
<p>Zápis do seznamu ANKÖ ušetří dokládání způsobilosti u každé nabídky. Více v návodu
<a href="/navody/jak-podat-nabidku-v-rakousku/">Jak se přihlásit do veřejné zakázky v Rakousku</a>.</p>""",
    },
    "stavby-polsko": {
        "h2": "Stavební zakázky v Polsku: co je dobré vědět",
        "body": """<p>Polsko staví díky evropským fondům ve velkém. Největšími zadavateli jsou GDDKiA (silnice a dálnice), PKP PLK
(železnice), města a vojvodství. Vedle velkých infrastrukturních zakázek vychází i spousta menších na školy, sportoviště
a rekonstrukce veřejných budov.</p>
<ul>
<li><strong>Smlouvy podle FIDIC.</strong> Velcí infrastrukturní zadavatelé často používají smluvní podmínky vycházející z FIDIC,
které české stavební firmy znají z domácích zakázek.</li>
<li><strong>Jistota a zajištění plnění.</strong> Počítejte s jistotou za nabídku (<em>wadium</em>) a u vítěze se zajištěním řádného
plnění (<em>zabezpieczenie należytego wykonania</em>), obojí lze krýt bankovní nebo pojišťovací zárukou.</li>
<li><strong>Valorizace ceny.</strong> Delší smlouvy musí podle polského zákona obsahovat doložku o změně ceny při růstu nákladů
(<em>waloryzacja</em>). Podmínky valorizace se mezi zadavateli liší, vyplatí se je číst pozorně.</li>
<li><strong>Odborné osoby.</strong> Zadavatelé obvykle požadují stavbyvedoucího a další osoby s autorizací (<em>uprawnienia budowlane</em>);
zahraniční kvalifikace je potřeba nechat uznat u polské komory.</li>
</ul>
<p>Registrace na platformě, jazyk a podpis nabídky: <a href="/navody/jak-podat-nabidku-v-polsku/">Jak se přihlásit do veřejné zakázky
v Polsku</a>.</p>""",
    },
    "it-software-polsko": {
        "h2": "IT zakázky v Polsku: co je dobré vědět",
        "body": """<p>Digitalizace polské státní správy, zdravotnictví a samospráv je z velké části financovaná z evropských fondů,
mimo jiné z programu <em>Fundusze Europejskie na Rozwój Cyfrowy</em> (FERC). IT nakupují ministerstva, státní IT centra,
nemocnice, univerzity i města.</p>
<ul>
<li><strong>Všechno v polštině.</strong> Nabídka, dokumentace systému, školení i podpora uživatelů se obvykle požadují v polštině.
U vývoje počítejte s polsky mluvícím projektovým manažerem nebo partnerem.</li>
<li><strong>Interoperabilita a přístupnost.</strong> Systémy pro veřejnou správu musí splňovat národní pravidla interoperability
(<em>Krajowe Ramy Interoperacyjności</em>) a webové aplikace standard přístupnosti WCAG 2.1.</li>
<li><strong>Reference.</strong> Podmínky účasti často požadují konkrétní reference podobného rozsahu z posledních let,
doložené potvrzením objednatele.</li>
<li><strong>Kvalifikovaný podpis.</strong> Nabídku v nadlimitní zakázce je nutné podepsat kvalifikovaným elektronickým podpisem;
český podpis platí, viz <a href="/navody/elektronicky-podpis-nabidky-v-zahranici/">elektronický podpis v zahraničí</a>.</li>
</ul>
<p>Celý postup od registrace po podání: <a href="/navody/jak-podat-nabidku-v-polsku/">Jak se přihlásit do veřejné zakázky v Polsku</a>.</p>""",
    },
}
