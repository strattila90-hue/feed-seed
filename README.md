# 🌱 Feed&Seed

Nyugtató, retro pixel art természetjáték. Egyetlen facsemetét gondozol: elülteted a magot, vizet adsz neki, és figyeled, ahogy a fa, a gyökerei, a körülötte élő növényzet és végül egy egész biom kifejlődik. Böngészőben és telepíthető PWA-ként / Android APK-ként is fut.

**Játék:** https://strattila90-hue.github.io/feed-seed/

## Játékmenet

1. Koppints a képernyőre, a mag a földbe kerül.
2. Koppintásra vízcseppek hullanak, ezek életet adnak a fának.
3. **1–8. szint:** a fa és a gyökérzet nő, szintenként új növények jelennek meg (virág, gomba, páfrány, bokor, magas virág, egyre dúsabb fű). A talajban hangyák, giliszták és bogarak élnek.
4. **9–13. szint (biom):** tó, pillangók, madarak, szentjánosbogarak és erdőszél, közben nappal és éjszaka váltakozik.

A fa víz nélkül is nő lassan, amíg van nedvesség a talajban, ezért a játék napi néhány perc játékidőre van méretezve.

## A fa fejlődése

A fa valós növekedési szakaszokon megy át: csíranövény (sziklevelek, majd valódi levelek, csúcsrügy), csemete, fiatal fa, lombosodó fa és kifejlett fa. A törzs kúpos, a friss csúcshajtás zöld, alatta fásodott kéreg, évgyűrű-hegekkel. Az oldalágak fentről lefelé öregebbek, az alsók a leghosszabbak. A lombkorona később, a fa magasodásával fejlődik, először csak az ágvégeken jelennek meg levelek. Minden szint elején zárt rügyek vannak, aztán rügyfakadás, hajtásnövekedés és a levelek kibomlása következik (a fiatal levél világosabb zöld).

## Végtelen játék

A szintek nem érnek véget. A 13. szint után (az igényelt tapasztalat lassan nő) minden szint új dolgot hoz:
- **Új állatok:** nyúl, béka, méh, szarvas, bagoly és róka, a **Természetnapló** a menüből mutatja a felfedezetteket és a következő ismeretlen élőlényt.
- **Évszakok:** a fa lombhullató: ősszel színeződik és hullat, télen kopasz és havazik, tavasszal újra lombosodik, nyáron virágzik és gyümölcsöt hoz.
- **Események:** eső (a fa gyorsabban nő), eső utáni szivárvány, éjszaka hulló csillag, amire ha rákoppintasz, bónusz növekedést kapsz.
- **Ősfa:** a 13. szint fölött a fa tovább vastagodik és magasodik (kb. 30. szintig).

## Fák, piac és csapások

- **Élethű ágrendszer:** a fa rekurzívan ágazik (főág, mellékág, ág, vessző), az alsó ágak a legrégebbiek, és fajonként más a koronaforma. A kamera közelebb van a fához.
- **Több fa:** a piacon magot vásárolhatsz (tölgy, nyír, fenyő, szakura, akác). Válaszd ki a magot alul, és koppints a talajra az ültetéshez. A kifejlett fák érmét termelnek.
- **Érmék:** szintlépésből, vízcseppekből, kifejlett fákból és a csapások túléléséből jönnek.
- **Természeti csapások (⚡ gomb):** vihar (villám, letört ágak), aszály, erdőtűz (koppintással oltható), fagy és sáskajárás (koppintással elkergethető). Károsítják az erdő egészségét (♥), ami lassítja a növekedést, de túlélésükért érme jár. A piacon védelmet is vehetsz.

## Felhők, időjárás, napszak, óriásfák, zene

- **Felhők:** 11 valódi felhőtípus (cirrus, cirrostratus, cirrocumulus, altocumulus, altostratus, stratocumulus, stratus, cumulus, cumulus congestus, nimbostratus, cumulonimbus) önálló életciklussal: keletkeznek, sodródnak, „gomolyognak”, átalakulnak (a cumulus tornyosuló gomolyfelhővé, majd zivatarfelhővé nőhet), és elenyésznek. Egy felhőre koppintva kiírja a nevét és a szerepét.
- **Időjárás:** az időjárási helyzet (derült, labilis, csapadékos) az évszaktól és a napszaktól függ. A nimbostratus tartós esőt vagy havat, a cumulonimbus zivatart hoz (villám, jég). Az eső után szivárvány jelenhet meg, és naplementekor a felhők pirosas árnyalatot kapnak.
- **Csapások:** a vihar és a szupercella ugyanezt a felhőrendszert használja (üllős cumulonimbus, forgó fal, jég), a tornádó a felhő aljából ereszkedik le.
- **Napszak:** a menüben vagy a ⚡ panelen állítható: Auto, Reggel, Dél, Alkony, Éjjel.
- **Óriásfák:** a piac Óriások fülén a világ legmagasabb fái: Douglas-fenyő (100 m), eukaliptusz (100 m), óriás mamutfenyő (84 m, a legnagyobb térfogatú), Hyperion (115 m, a legmagasabb ismert fa). Szinthez kötött, a zárolt tételek előre láthatók.
- **Zene:** a menüben hat stílus közül választhatsz: Nyugodt, Lo-fi, Gitár, Természet, Zongora, Ki. A hang mind a készüléken generálódik.
- **Megjelenés:** lekerekített gombok, nagyobb, képes áruházkártyák.

## Élethű időjárás és grafika

- **Időjárási modell:** légnyomás (hPa) és nyomástendencia határozza meg a helyzetet: süllyedő nyomás → front, csapadék; meleg, párás nappal → zivatarhajlam; magas nyomás → derült idő. A szélirány frontátvonuláskor megfordul.
- **Páratartalom és harmatpont:** a relatív páratartalom éjjel, eső után nő, napsütésben és szélben csökken; a harmatpont a Magnus-képlettel számolódik.
- **Köd:** ha a hőmérséklet megközelíti a harmatpontot, gyenge szélben (főleg hajnalban) ködréteg képződik, amit a nap feloszlat.
- **Szél:** a nyomásból és a nyomásváltozásból jön, folyamatos széllökésekkel; dönti az esőt, hajlítja a fákat, viszi a leveleket és a felhőket.
- **Csapadéktípus:** 2 °C fölött eső, −1 és 2 °C között havas eső, alatta lebegő hópelyhek. Rétegfelhőből szitálás, zivatarfelhőből felhőszakadás. Mennydörgés a villám távolságával arányos késéssel, eső- és szélzaj.
- **Nedves talaj:** eső után sötétebb föld, tócsák tükröződéssel és hullámgyűrűkkel, amelyek napsütésben felszáradnak, fagyban befagynak.
- **Időjárás-jelző:** a bal felső sávban hőmérséklet, páratartalom, szél; rákoppintva részletes jelentés (légnyomás, tendencia, harmatpont, Beaufort-fok).
- **Grafika:** távoli hegyvonulat légköri perspektívával, fenyves erdősáv, sima égi színátmenet, fényudvar a nap és a fények körül, napsugarak, tükröződő tó, elágazó villám, aranyórás színezés, esőben és ködben fakóbb színek.
- **Élethű lomb:** a korona szabálytalan körvonalú levélcsomókból áll, a fény felől világosabb, alul és belül árnyékosabb, a széle áttört, kilógó levelekkel. A fenyő lombja lapítottabb, az akác és a baobab ernyős, a fűz és a nyír ágai lecsüngenek, télen hó ül a lombon.
- **Egyedi gyökérzet:** minden fának saját, a magjából generált gyökérrendszere van, fajra jellemző formával: karógyökér (tölgy, fenyő, akác), szívgyökér (nyír, szakura, juhar, eukaliptusz, Douglas-fenyő), tányérgyökér (fűz, baobab, mamutfenyő, Hyperion), bojtos gyökér (bokrok). A gyökerek a fával együtt nőnek: előbb a fő gyökerek, aztán az oldalgyökerek és a hajszálgyökerek; a vastag gyökerek a törzs közelében a legerősebbek.
- **Grafika: Éles** mód a menüben (Auto → Éles → Takarékos): kb. kétszer annyi képpont, finomabb részletek.

## Végtelen erdő, érintés, teljesítmény

- **Végtelen világ:** az erdő vízszintesen végtelen. Húzd el az ujjad a kamera mozgatásához (lendülettel), vagy tartsd az ujjad a képernyő szélén a görgetéshez. A 🏠 gomb visszavisz a főfához. A zöld terület a szinttel és az ültetett fák körül nő.
- **Eső:** koppintás egy vízcsepp-csokrot ad, a nyomvatartás folyamatos esőt, ami követi az ujjadat (a felhő is).
- **Fák és bokrok:** 8 fafaj (tölgy, nyír, fenyő, szakura, akác, fűz, juhar, baobab) és 4 bokor (rózsa, levendula, áfonya, hortenzia). A bokrok gyorsan nőnek és virágoznak.
- **Piac gyerekbarát felülettel:** nagy képes kártyák fülekkel (Fák, Bokrok, Díszek, Védelem): méhkas (méz = érme), madáretető, lámpás, szökőkút, esővíz-hordó, trágya és védelmek.
- **Évszakok és hőmérséklet:** a hőmérséklet (🌡) a napszaktól és az évszaktól függ, télen hó borítja a talajt és az ágakat, a tó befagy, a növekedés télen lassabb.
- **Teljesítmény:** a háttér (ég, hegyek, talaj) és a fák képként gyorsítótárazva rajzolódnak, a felbontás a készülékhez igazodik (lassú telefonon automatikusan csökken), a menüben a **Grafika: Takarékos** mód 30 fps-re korlátoz és kíméli az akkumulátort.
- **Offline:** a játék a telepítés után internet nélkül is megy (gyorsítótár-első service worker), betöltéskor betöltőképernyő látszik.
- **Ikon:** a `tools/make_icon.py` generálja az ikont, a `tools/android_icons.py` pedig az Android indítóikonokat az APK építésekor.

## Csapások testreszabása

- **Játékban:** a ⚡ gomb panelében minden csapásnál a ◀ ▶ gombokkal állíthatod az erősséget (Gyenge, Közepes, Erős), felül pedig az automatikus csapások gyakoriságát (Ki, Ritka, Gyakori). A beállítás mentődik.
- **Csapások:** vihar, szupercella (jég, villám, esetleg tornádó), tornádó, erdőtűz, árvíz, aszály, fagy, sáskajárás.
- **Kódban:** az `index.html`-ben a `DZ` táblázat soronként írja le a csapásokat (név, ikon, időtartam, sebzés/mp és egyedi értékek, pl. tornádó sebessége és sugara, jégszem/mp, tűzfrontok száma, árvízszint). Az `INT` táblázat az erősségi fokozatok szorzói (sebzés, jutalom, időtartam). Átírás után csak a `sw.js` gyorsítótár-verzióját kell növelni.

## Képernyők

A játék telefonon és tableten is fut, álló és fekvő tájolásban. A kép mindig négyzetes pixelekből áll (nincs torzítás), a felbontás a kijelző méretéhez igazodik, a fa, a talaj és az élőlények mérete arányosan változik, a biom pedig fekvő módban is kitölti a teljes szélességet. A kijelzőbevágás (notch) mellett a kezelőfelület a biztonságos területen marad. Forgatáskor a játékállás megmarad.

## Funkciók

- Főmenü, szünet gomb, teljes képernyős játék
- Automatikus mentés (5 mp-enként, kilépéskor és háttérbe váltáskor), induláskor ott folytatja, ahol abbahagytad
- Generatív, nyugtató háttérzene (WebAudio, nincs külső hangfájl), a menüben kikapcsolható
- Offline működés (service worker)

## Fájlok

| Fájl | Szerep |
|---|---|
| `index.html` | A teljes játék (canvas, CSS, JS) |
| `manifest.json` | PWA-adatok (teljes képernyő, álló tájolás) |
| `sw.js` | Offline gyorsítótár |
| `icon-192.png`, `icon-512.png` | Ikonok |
| `tools/` | Ikon-generátor és Android ikon-csere (az APK-építéshez) |

## Közzététel GitHub Pages-en

1. Töltsd fel a fájlokat a repó gyökerébe.
2. **Settings → Pages → Deploy from a branch → `main` / `(root)`**
3. Pár perc múlva elérhető a fenti címen.

## APK készítése (automatikusan, GitHub Actions)

A repóban benne van a `.github/workflows/build-apk.yml`, ami minden `main`-re küldött módosításnál (vagy az **Actions → Build APK → Run workflow** gombbal) legyártja az Androidos APK-t Capacitorral.

1. Töltsd fel a repóba az összes fájlt, a `.github` mappát is (`package.json`, `capacitor.config.json`, `.gitignore`).
2. Várd meg, amíg lefut az **Actions** fül alatt a *Build APK* (kb. 4–6 perc).
3. Az APK két helyen érhető el: a futás alján az **Artifacts → feed-seed-apk**, illetve a repó **Releases → latest** oldalán.
4. Telepítsd a telefonra (ismeretlen forrásból telepítés engedélyezése kell). Az APK debug-aláírású, Play Áruházba való feltöltéshez saját kulcs kell.

Az APK teljes képernyős, és követi a telefon forgatását (álló és fekvő). A játék helyi másolatot használ, így internet nélkül is megy.

## Fejlesztés

Nincs build lépés. Helyben így indíthatod:

```bash
python3 -m http.server 8000
```

Majd nyisd meg a `http://localhost:8000` címet. A játék értékei (szintenkénti szükséges tapasztalat, passzív növekedés, vízcseppek értéke) az `index.html` elején és a `gain()` / `update()` függvényekben állíthatók.

Frissítéskor növeld a `sw.js`-ben a `feedseed-v2` gyorsítótár-verziót, hogy a telepített változat is frissüljön.

## Hibakeresés

- Nyisd meg a játékot `?debug` paraméterrel (`.../feed-seed/?debug`), vagy koppints ötször a főmenü címére (APK-ban is működik): bal alul megjelenik az FPS, a felbontás, a szint, a részecskék száma és az utolsó hibák.
- A hibák a böngésző konzoljában is megjelennek `[Feed&Seed]` előtaggal (Chrome: `chrome://inspect` a telefonhoz).
- Ha elromlik a mentés, törölheted: konzolban `localStorage.removeItem('feedseed_v1')`.
