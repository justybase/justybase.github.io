# JustyBase GitHub Pages

Static, dependency-free landing pages for the JustyBase product hub:

- `/` — brand homepage with four flagship products and an open-source catalog
- `/legacy/` — JustyBase.Legacy Windows SQL client for Netezza
- `/vscode/` — JustyBase Netezza SQL Tools for VS Code
- `/csharp-tool/` — redirect to `/#products` (legacy placeholder removed)

## Homepage model

**Flagship products** (featured cards):

1. [JustyBase.Legacy](https://github.com/justybase/JustyBase.Legacy) → `/legacy/`
2. [justybase-vscode](https://github.com/justybase/justybase-vscode) → `/vscode/`
3. [nzpy_extended](https://github.com/justybase/nzpy_extended)
4. [justybase_netezza_node_driver](https://github.com/justybase/justybase_netezza_node_driver)

**Open source catalog** (compact list): JustyBase.NetezzaSql, JustyBase.Netezza, JustyBase.NetezzaDriver, dbeaver-netezza-tools-plugin, SpreadSheetTasks, justybase_spreadsheet_tasks, xlspy.

## Add a product page

1. Copy an existing product directory (for example `vscode/` or `legacy/`) and rename it.
2. Update its `index.html` content.
3. Add a matching product card to the `Products` grid in the root `index.html`, or a row in the open-source catalog.
4. Keep using `../assets/css/style.css` and the existing relative-link pattern so the page works both on GitHub Pages and when opened locally.

Product pages link to README content, documentation, screenshots, and release assets in their source repositories. Those files are the product source of truth and are intentionally not duplicated here. Screenshot URLs are served directly from those repositories; if paths change, update the matching product page manually.

## Deployment

This repository is designed for GitHub Pages without a build step or GitHub Actions workflow. Enable Pages for the `main` (or `master`) branch using the repository root as the publishing source.

The published site is available at https://justybase.github.io/.
