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

Az APK teljes képernyős és álló tájolású. A játék helyi másolatot használ, így internet nélkül is megy.

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
