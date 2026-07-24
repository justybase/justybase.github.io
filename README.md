# JustyBase GitHub Pages

Static, dependency-free landing pages for the JustyBase product hub:

- `/` — brand homepage with four flagship products and an open-source catalog
- `/vscode/` — JustyBase Netezza SQL Tools for VS Code
- `/csharp-tool/` — redirect to `/#products` (legacy placeholder removed)

## Homepage model

**Flagship products** (featured cards):

1. [justybase-vscode](https://github.com/justybase/justybase-vscode) → `/vscode/`
2. [JustyBase.NetezzaSql](https://github.com/justybase/JustyBase.NetezzaSql)
3. [nzpy_extended](https://github.com/justybase/nzpy_extended)
4. [justybase_netezza_node_driver](https://github.com/justybase/justybase_netezza_node_driver)

**Open source catalog** (compact list): JustyBase.Netezza, JustyBase.NetezzaDriver, dbeaver-netezza-tools-plugin, SpreadSheetTasks, xlspy.

## Add a product page

1. Copy an existing product directory (for example `vscode/`) and rename it.
2. Update its `index.html` content.
3. Add a matching product card to the `Products` grid in the root `index.html`, or a row in the open-source catalog.
4. Keep using `../assets/css/style.css` and the existing relative-link pattern so the page works both on GitHub Pages and when opened locally.

The VS Code page links to README content, documentation, screenshots, and release assets in the separate [`justybase-vscode`](https://github.com/justybase/justybase-vscode) repository. Those files are the product source of truth and are intentionally not duplicated here. Screenshot URLs are served directly from that repository; if their paths change, update `vscode/index.html` manually.

## Deployment

This repository is designed for GitHub Pages without a build step or GitHub Actions workflow. Enable Pages for the `main` (or `master`) branch using the repository root as the publishing source.

The published site is available at https://justybase.github.io/.
