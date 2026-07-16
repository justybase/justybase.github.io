# JustyBase GitHub Pages

Static, dependency-free landing pages for the JustyBase product hub:

- `/` — the brand homepage
- `/vscode/` — JustyBase Netezza SQL Tools for VS Code
- `/csharp-tool/` — reserved “coming soon” page for the future C# tool

## Add a product page

1. Copy an existing product directory (for example `csharp-tool/`) and rename it.
2. Update its `index.html` content and the `TODO` marker if the product is still in development.
3. Add a matching product card to the `Products` grid in the root `index.html`.
4. Keep using `../assets/css/style.css` and the existing relative-link pattern so the page works both on GitHub Pages and when opened locally.

The VS Code page links to README content, documentation, screenshots, and release assets in the separate [`justybase-vscode`](https://github.com/justybase/justybase-vscode) repository. Those files are the product source of truth and are intentionally not duplicated here. Screenshot URLs are served directly from that repository; if their paths change, update `vscode/index.html` manually.

## Deployment

This repository is designed for GitHub Pages without a build step or GitHub Actions workflow. Enable Pages for the `main` (or `master`) branch using the repository root as the publishing source.

The published site is available at https://justybase.github.io/.
