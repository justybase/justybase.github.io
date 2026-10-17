# JustyBase GitHub Pages

Static, dependency-free landing pages for the JustyBase product hub:

- `/` and `/pl/` — bilingual (EN / PL) portfolio homepage: flagship apps, filterable libraries & drivers, stack, approach
- `/justybase/`, `/legacy/`, `/vscode/` — product pages, each with a Polish twin under `/pl/<page>/`
- `/csharp-tool/` — redirect to `/#apps` (legacy placeholder removed)

## Bilingual content

Homepages are generated from `tools/build_home.py` (project data + EN/PL copy in one place); Polish product pages are generated from the English ones by `tools/build_subpages.py`. After editing, run from the repo root:

```bash
python3 tools/build_home.py
python3 tools/build_subpages.py
```

Edit the English product pages directly and add/adjust the matching Polish strings in the script. Language switcher links and `hreflang` tags are wired automatically; the theme/lightbox scripts read the page `lang`.

## Projects shown

Apps: justybase-vscode, justybase, JustyBase.Legacy. Drivers: NetezzaDriver, Db2, node driver, nz_rust, nzpy_extended, UCanAccessCs. Spreadsheets: SpreadSheetTasks, spreadsheet_rust, spreadsheet_tasks (TS), xlspy. SQL & tools: dbeaver plugin. Archived repos and the org `.github`/demo repos are intentionally omitted.

## Visual direction

The site uses one restrained visual system and shows product UI only through screenshots served from the product repositories. There are no fabricated editor mockups or placeholder query results. Light and dark themes are supported via `assets/js/theme.js`.

## Add a product page

1. Copy an existing product directory (for example `vscode/` or `legacy/`) and rename it.
2. Update its `index.html` content.
3. Add a matching product card to the `Products` grid in the root `index.html`, or a row in the open-source catalog.
4. Keep using `../assets/css/style.css` and the existing relative-link pattern so the page works both on GitHub Pages and when opened locally.

Product pages link to README content, documentation, screenshots, and release assets in their source repositories. Those files are the product source of truth and are intentionally not duplicated here. Screenshot URLs are served directly from those repositories; if paths change, update the matching product page manually.

## Deployment

This repository is designed for GitHub Pages without a build step or GitHub Actions workflow. Enable Pages for the `main` (or `master`) branch using the repository root as the publishing source.

The published site is available at https://justybase.github.io/.
