# Contributing

## English

Thanks for helping out!

- **Run locally:** `python3 -m http.server 8000`, then open http://localhost:8000. There is no build step.
- **Checks:** the repo has no automated tests. Before opening a PR, extract the `<script>` blocks of `index.html` and run `node --check` on them, then load the page in a browser, play for a minute and make sure the console shows no errors (`?debug` shows an overlay).
- **Style:** everything lives in `index.html` (canvas, CSS, JS); keep it dependency-free, keep the retro pixel-art look and keep the UI text Hungarian (an English UI is welcome as a separate, well-scoped change). Avoid very long lines and per-frame allocations.
- **Releases:** when you change `index.html`, bump `VER` in `index.html` and the cache name (`C`) in `sw.js`, otherwise installed copies will not update.
- **PRs:** fork, create a branch, make one focused change, describe it and attach a screenshot if it is visual.

## Magyar

Köszönjük a segítséget!

- **Helyi futtatás:** `python3 -m http.server 8000`, majd http://localhost:8000. Nincs build lépés.
- **Ellenőrzés:** nincsenek automata tesztek. PR előtt az `index.html` `<script>` blokkjait kinyerve futtasd le a `node --check`-et, majd töltsd be az oldalt böngészőben, játssz egy percet, és nézd meg, hogy a konzolban nincs hiba (`?debug` overlay).
- **Stílus:** minden az `index.html`-ben van (canvas, CSS, JS); maradjon függőségmentes, retro pixel art kinézetű, a felület magyar nyelvű (angol felület külön, jól körülírt változtatásként jöhet). Kerüld az óriás sorokat és a képkockánkénti foglalásokat.
- **Kiadás:** az `index.html` módosításakor növeld a `VER`-t az `index.html`-ben és a gyorsítótár nevét (`C`) az `sw.js`-ben, különben a telepített példányok nem frissülnek.
- **PR menete:** fork, ág, egy összefüggő változtatás, leírás, vizuális változásnál képernyőkép.
