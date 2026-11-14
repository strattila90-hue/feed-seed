# 🌱 Feed&Seed

Nyugtató, retro pixel art természetjáték. Egyetlen facsemetét gondozol: elülteted a magot, vizet adsz neki, és figyeled, ahogy a fa, a gyökerei, a körülötte élő növényzet és végül egy egész biom kifejlődik. Böngészőben és telepíthető PWA-ként / Android APK-ként is fut.

**Játék:** https://strattila90-hue.github.io/feed-seed/

## Játékmenet

1. Koppints a képernyőre, a mag a földbe kerül.
2. Koppintásra vízcseppek hullanak, ezek életet adnak a fának.
3. **1–8. szint:** a fa és a gyökérzet nő, szintenként új növények jelennek meg (virág, gomba, páfrány, bokor, magas virág, egyre dúsabb fű). A talajban hangyák, giliszták és bogarak élnek.
4. **9–13. szint (biom):** tó, pillangók, madarak, szentjánosbogarak és erdőszél, közben nappal és éjszaka váltakozik.

A fa víz nélkül is nő lassan, amíg van nedvesség a talajban, ezért a játék napi néhány perc játékidőre van méretezve.

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

## APK készítése

1. Nyisd meg a [pwabuilder.com](https://www.pwabuilder.com) oldalt, és add meg a játék Pages-címét.
2. Válaszd az **Android** csomagot, és töltsd le.
3. Beállításoknál használd a `fullscreen` / immersive módot, hogy semmi ne lógjon be.
4. A kapott APK-t telepítheted a telefonra (ismeretlen forrásból telepítés engedélyezése kell hozzá).

## Fejlesztés

Nincs build lépés. Helyben így indíthatod:

```bash
python3 -m http.server 8000
```

Majd nyisd meg a `http://localhost:8000` címet. A játék értékei (szintenkénti szükséges tapasztalat, passzív növekedés, vízcseppek értéke) az `index.html` elején és a `gain()` / `update()` függvényekben állíthatók.

Frissítéskor növeld a `sw.js`-ben a `feedseed-v2` gyorsítótár-verziót, hogy a telepített változat is frissüljön.
