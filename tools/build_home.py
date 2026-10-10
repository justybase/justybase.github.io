#!/usr/bin/env python3
"""Generate the bilingual homepages: index.html (EN) and pl/index.html (PL).

Run from the repository root:  python3 tools/build_home.py
Edit the PROJECTS data and the copy dictionaries below, never the generated HTML.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://justybase.github.io/"
GH = "https://github.com/justybase/"
RAW = "https://raw.githubusercontent.com/justybase/"

# ---------------------------------------------------------------- copy
COPY = {
    "en": {
        "lang": "en", "title": "JustyBase — Netezza and SQL developer tools",
        "desc": "Portfolio of JustyBase: SQL IDEs, a VS Code extension, database drivers (.NET, Node.js, Python, Rust) and spreadsheet libraries for Netezza, Db2 and data workflows.",
        "og_desc": "SQL IDEs, drivers and libraries for Netezza, Db2 and data workflows — C#, TypeScript, Rust and Python.",
        "util_l": "DATABASE TOOLING / PORTFOLIO", "util_r": "Open source · Built for real-world data work",
        "nav": ["Apps", "Libraries", "Stack", "Approach"], "nav_aria": "Main navigation",
        "gh": "GitHub ↗", "theme_dark": "Dark mode", "theme_light": "Light mode",
        "aria_dark": "Switch to dark theme", "aria_light": "Switch to light theme",
        "lang_switch": "Polski", "lang_aria": "Przełącz na język polski",
        "eyebrow": "Developer tools for data teams",
        "h1": ["Serious tools for ", "serious data."],
        "lead": "I build database tooling for Netezza and SQL workflows — desktop IDEs, a VS Code extension, native drivers and fast spreadsheet libraries across .NET, TypeScript, Rust and Python.",
        "cta1": "See the projects", "cta2": "Browse on GitHub ↗",
        "stats": [("15", "open-source projects"), ("6", "languages in use"), ("3", "SQL workspaces")],
        "hero_cap": "JustyBase desktop SQL workspace",
        "hero_alt": "JustyBase SQL editor with schema explorer and query results in dark theme",
        "apps_idx": "01 / APPLICATIONS", "apps_h": "Flagship apps.",
        "apps_p": "Three SQL workspaces for the path from editor to query result — each with its own product page.",
        "libs_idx": "02 / LIBRARIES & DRIVERS", "libs_h": "The toolkit underneath.",
        "libs_p": "Drivers, parsers and file-format libraries that power the apps — and stand on their own.",
        "filters": [("all", "All"), ("drivers", "Drivers"), ("spreadsheets", "Spreadsheets"), ("tools", "SQL & tools")],
        "filter_aria": "Filter projects", "page": "Product page", "src": "View on GitHub",
        "stack_idx": "03 / STACK", "stack_h": "Languages and platforms.",
        "stack_p": "Native protocols over bridges: most drivers speak the database wire protocol directly.",
        "stack": [
            ("C# / .NET", "Avalonia and WinForms IDEs, ADO.NET drivers, Native AOT builds"),
            ("TypeScript / Node.js", "VS Code extension, pure-JS Netezza driver, XLSB/XLSX I/O"),
            ("Rust", "Pure-Rust Netezza client and streaming spreadsheet library"),
            ("Python + C", "nzpy fork with a C extension, up to 90× faster; xlspy"),
            ("Java", "DBeaver plugin for Netezza import/export and DDL"),
            ("Databases", "Netezza, Db2, PostgreSQL, Oracle, MSSQL, MySQL, DuckDB, Snowflake, Access"),
        ],
        "app_idx": "03 / APPROACH", "app_h": "Clarity is a feature.",
        "app_p": "Database work is already complex. The tools around it should make state, intent and results easier to see — from the editor through drivers and SQL toolkits to spreadsheet I/O.",
        "principles": [("Context", "schema-aware workflows"), ("Control", "explicit actions and feedback"), ("Continuity", "the editor stays the workspace")],
        "cta_h": "Let's talk data tooling.", "cta_p": "Everything here is open source. Browse the code, open an issue, or start a conversation on GitHub.",
        "cta_b": "github.com/justybase ↗",
        "foot": "© JustyBase · Tools for thoughtful developers.",
    },
    "pl": {
        "lang": "pl", "title": "JustyBase — narzędzia dla Netezza i SQL",
        "desc": "Portfolio JustyBase: środowiska SQL, rozszerzenie VS Code, sterowniki baz danych (.NET, Node.js, Python, Rust) i biblioteki arkuszy dla Netezza, Db2 i przepływów danych.",
        "og_desc": "Środowiska SQL, sterowniki i biblioteki dla Netezza, Db2 i pracy z danymi — C#, TypeScript, Rust i Python.",
        "util_l": "NARZĘDZIA BAZODANOWE / PORTFOLIO", "util_r": "Open source · Tworzone do realnej pracy z danymi",
        "nav": ["Aplikacje", "Biblioteki", "Stos", "Podejście"], "nav_aria": "Nawigacja główna",
        "gh": "GitHub ↗", "theme_dark": "Tryb ciemny", "theme_light": "Tryb jasny",
        "aria_dark": "Przełącz na ciemny motyw", "aria_light": "Przełącz na jasny motyw",
        "lang_switch": "English", "lang_aria": "Switch to English",
        "eyebrow": "Narzędzia dla zespołów danych",
        "h1": ["Poważne narzędzia do ", "poważnych danych."],
        "lead": "Tworzę narzędzia bazodanowe dla Netezza i pracy z SQL — desktopowe IDE, rozszerzenie VS Code, natywne sterowniki i szybkie biblioteki arkuszy w .NET, TypeScript, Rust i Pythonie.",
        "cta1": "Zobacz projekty", "cta2": "Przeglądaj na GitHubie ↗",
        "stats": [("15", "projektów open source"), ("6", "używanych języków"), ("3", "środowiska SQL")],
        "hero_cap": "Desktopowe środowisko SQL JustyBase",
        "hero_alt": "Edytor SQL JustyBase z eksploratorem schematu i wynikami zapytań w ciemnym motywie",
        "apps_idx": "01 / APLIKACJE", "apps_h": "Flagowe aplikacje.",
        "apps_p": "Trzy środowiska SQL na drodze od edytora do wyniku zapytania — każde z własną stroną produktu.",
        "libs_idx": "02 / BIBLIOTEKI I STEROWNIKI", "libs_h": "Zestaw narzędzi pod spodem.",
        "libs_p": "Sterowniki, parsery i biblioteki formatów plików, które napędzają aplikacje — i działają także samodzielnie.",
        "filters": [("all", "Wszystkie"), ("drivers", "Sterowniki"), ("spreadsheets", "Arkusze"), ("tools", "SQL i narzędzia")],
        "filter_aria": "Filtruj projekty", "page": "Strona produktu", "src": "Zobacz na GitHubie",
        "stack_idx": "03 / STOS", "stack_h": "Języki i platformy.",
        "stack_p": "Natywne protokoły zamiast mostków: większość sterowników mówi bezpośrednio protokołem bazy danych.",
        "stack": [
            ("C# / .NET", "IDE w Avalonia i WinForms, sterowniki ADO.NET, buildy Native AOT"),
            ("TypeScript / Node.js", "Rozszerzenie VS Code, czysto JS-owy sterownik Netezza, odczyt i zapis XLSB/XLSX"),
            ("Rust", "Czysto Rustowy klient Netezza i strumieniowa biblioteka arkuszy"),
            ("Python + C", "Fork nzpy z rozszerzeniem w C, do 90× szybszy; xlspy"),
            ("Java", "Wtyczka DBeaver: import/eksport i DDL dla Netezza"),
            ("Bazy danych", "Netezza, Db2, PostgreSQL, Oracle, MSSQL, MySQL, DuckDB, Snowflake, Access"),
        ],
        "app_idx": "03 / PODEJŚCIE", "app_h": "Przejrzystość to funkcja.",
        "app_p": "Praca z bazami danych jest już wystarczająco złożona. Narzędzia wokół niej powinny ułatwiać zobaczenie stanu, intencji i wyników — od edytora, przez sterowniki i biblioteki SQL, po import i eksport arkuszy.",
        "principles": [("Kontekst", "przepływy świadome schematu"), ("Kontrola", "jawne akcje i informacja zwrotna"), ("Ciągłość", "edytor pozostaje przestrzenią pracy")],
        "cta_h": "Porozmawiajmy o narzędziach dla danych.", "cta_p": "Wszystko tutaj jest open source. Przejrzyj kod, zgłoś issue albo zacznij rozmowę na GitHubie.",
        "cta_b": "github.com/justybase ↗",
        "foot": "© JustyBase · Narzędzia dla myślących programistów.",
    },
}

# ---------------------------------------------------------------- projects
ICON_DB = '<ellipse cx="12" cy="5" rx="7" ry="3"/><path d="M5 5v7c0 1.66 3.13 3 7 3s7-1.34 7-3V5M5 12v7c0 1.66 3.13 3 7 3s7-1.34 7-3v-7"/>'
APPS = [
    {"page": "vscode/", "repo": "justybase-vscode", "name": "JustyBase Core (NetezzaSQL)", "tag": "VS CODE",
     "img": RAW + "justybase-vscode/master/docs/screenshots/workspace-overview.png",
     "tags": ["NETEZZA", "POSTGRESQL", "ORACLE", "DB2", "DUCKDB", "AI COPILOT"],
     "en": ("Netezza-first SQL extension for Visual Studio Code with a built-in JavaScript driver, schema browser, result explorer, ERD and ETL designer, notebooks and an AI SQL assistant. Optional packs add Db2, PostgreSQL, Snowflake, Oracle, MSSQL, MySQL and DuckDB.",
            "Connections, schema, SQL and results in the VS Code workspace"),
     "pl": ("Rozszerzenie SQL dla Visual Studio Code zorientowane na Netezza: wbudowany sterownik JavaScript, przeglądarka schematu, eksplorator wyników, ERD i projektant ETL, notebooki oraz asystent SQL z AI. Opcjonalne paczki dodają Db2, PostgreSQL, Snowflake, Oracle, MSSQL, MySQL i DuckDB.",
            "Połączenia, schemat, SQL i wyniki w przestrzeni roboczej VS Code")},
    {"page": "justybase/", "repo": "justybase", "name": "JustyBase", "tag": "DESKTOP · AVALONIA",
     "img": RAW + "justybase/main/pictures/evo_dark.png",
     "tags": [".NET 10", "AVALONIA", "NATIVE AOT", "GIT", "LOCAL AI"],
     "en": ("Local-first, cross-platform SQL IDE for IBM Netezza (Windows, Linux, macOS) with a fast editor, schema exploration, Git-aware workflows, data export to Excel, CSV and Parquet, and optional local AI assistance.",
            "SQL editor, schema explorer and results in one desktop workspace"),
     "pl": ("Wieloplatformowe IDE SQL dla IBM Netezza (Windows, Linux, macOS) działające lokalnie: szybki edytor, eksplorator schematu, przepływy z Gitem, eksport do Excela, CSV i Parquet oraz opcjonalna lokalna pomoc AI.",
            "Edytor SQL, eksplorator schematu i wyniki w jednym środowisku desktopowym")},
    {"page": "legacy/", "repo": "JustyBase.Legacy", "name": "JustyBase.Legacy", "tag": "WINDOWS · .NET",
     "img": RAW + "JustyBase.Legacy/main/docs/images/editor-showcase-dark.png",
     "tags": ["WINFORMS", ".NET 10", "NETEZZA", "INSTALLER"],
     "en": ("Windows SQL client for Netezza-first authoring: SQL editor, virtual-mode result grid, object explorer, docked preferences, AES-GCM encrypted connection profiles and tagged Inno Setup releases with CI quality gates.",
            "SQL editor, result grid and database explorer — dark theme"),
     "pl": ("Windowsowy klient SQL do pracy z Netezza: edytor SQL, siatka wyników w trybie wirtualnym, eksplorator obiektów, ustawienia w zakładce, szyfrowane (AES-GCM) profile połączeń oraz wydania z instalatorem Inno Setup i bramkami jakości w CI.",
            "Edytor SQL, siatka wyników i eksplorator bazy — ciemny motyw")},
]

# category: drivers | spreadsheets | tools
LIBS = [
    ("JustyBase.NetezzaDriver", "NetezzaDriver", "C#", "drivers", ".NET",
     "Pure C# ADO.NET driver for IBM Netezza — no native dependencies, no ODBC. Sync/async API, pooling, catalog introspection, AOT-compatible.",
     "Czysty sterownik ADO.NET w C# dla IBM Netezza — bez zależności natywnych i ODBC. API sync/async, pule połączeń, introspekcja katalogu, zgodność z AOT.", None),
    ("JustyBase.Db2", "JustyBase.Db2", "C#", "drivers", ".NET",
     "Open-source managed .NET driver for IBM Db2 over the DRDA protocol, with ADO.NET support.",
     "Zarządzany sterownik .NET o otwartym kodzie dla IBM Db2 działający na protokole DRDA, z obsługą ADO.NET.", None),
    ("@justybase/netezza-driver", "justybase_netezza_node_driver", "TypeScript", "drivers", "NODE.JS",
     "Pure TypeScript Netezza / PureData driver for Node.js with pooling, SSL and an ADO.NET-style Connection / Command / Reader API.",
     "Czysty sterownik Netezza / PureData w TypeScript dla Node.js: pule połączeń, SSL i API w stylu ADO.NET (Connection / Command / Reader).", None),
    ("nz_rust", "justybase_nz-rust", "Rust", "drivers", "RUST",
     "Pure Rust client for IBM Netezza and PureData — sync client, Tokio-friendly async facade, pools, cancellation and bounded-memory streaming. Preview.",
     "Czysty klient Rust dla IBM Netezza i PureData — klient synchroniczny, asynchroniczna fasada dla Tokio, pule, anulowanie i strumieniowanie w ograniczonej pamięci. Wersja preview.", None),
    ("nzpy_extended", "nzpy_extended", "Python", "drivers", "PYTHON",
     "High-performance Netezza driver for Python — hard fork of IBM nzpy with a C extension (up to 90× faster), async API, pooling and streaming bulk load.",
     "Wydajny sterownik Netezza dla Pythona — fork IBM nzpy z rozszerzeniem w C (do 90× szybszy), API async, pule połączeń i strumieniowy bulk load.", "pip install nzpy-extended"),
    ("JustyBase.UCanAccessCs", "JustyBase.UCanAccessCs", "C#", "drivers", ".NET",
     "Pure .NET ADO.NET provider for Microsoft Access .mdb / .accdb files — no Access, ODBC or ACE required.",
     "Czysty dostawca ADO.NET dla plików Microsoft Access .mdb / .accdb — bez Accessa, ODBC i ACE.", None),
    ("SpreadSheetTasks", "SpreadSheetTasks", "C#", "spreadsheets", ".NET",
     "The .NET library for fast reading and writing of Excel files (.xlsx, .xlsb).",
     "Biblioteka .NET do szybkiego odczytu i zapisu plików Excela (.xlsx, .xlsb).", None),
    ("justybase_spreadsheet_rust", "justybase_spreadsheet_rust", "Rust", "spreadsheets", "RUST",
     "High-performance Rust library for streaming-friendly XLSX and XLSB reading, writing and worksheet updates.",
     "Wydajna biblioteka Rust do strumieniowego odczytu, zapisu i aktualizacji arkuszy XLSX oraz XLSB.", None),
    ("@justybase/spreadsheet-tasks", "justybase_spreadsheet_tasks", "TypeScript", "spreadsheets", "NODE.JS",
     "High-performance TypeScript library for XLSB / XLSX read and write — XLSB markedly faster than XLSX.",
     "Wydajna biblioteka TypeScript do odczytu i zapisu XLSB / XLSX — XLSB wyraźnie szybszy niż XLSX.", None),
    ("xlspy", "xlspy", "Python", "spreadsheets", "PYTHON",
     "Python library for efficient XLSB / XLSX read and write, with optional C acceleration.",
     "Biblioteka Pythona do wydajnego odczytu i zapisu XLSB / XLSX, z opcjonalną akceleracją w C.", None),
    ("JustyBase.NetezzaSql", "JustyBase.NetezzaSql", "C#", "tools", ".NET",
     ".NET libraries for Netezza SQL parsing, authoring, DDL generation and catalog metadata queries.",
     "Biblioteki .NET do parsowania SQL Netezza, edycji, generowania DDL i zapytań o metadane katalogu.", None),
    ("dbeaver-netezza-tools-plugin", "dbeaver-netezza-tools-plugin", "Java", "tools", "DBEAVER",
     "DBeaver extension for clipboard / Excel import-export, table creation and Netezza-friendly DDL.",
     "Rozszerzenie DBeaver: import i eksport przez schowek / Excela, tworzenie tabel i DDL przyjazny dla Netezza.", None),
]
LANG_CLASS = {"C#": "cs", "TypeScript": "ts", "Rust": "rs", "Python": "py", "Java": "java", "JavaScript": "js"}


def render(lang: str) -> str:
    c = COPY[lang]
    pl = lang == "pl"
    up = "../" if pl else ""            # prefix back to site root
    self_url = SITE + ("pl/" if pl else "")
    alt_href = "../" if pl else "pl/"
    en_url, pl_url = SITE, SITE + "pl/"
    app_p = lambda a: a[lang]

    def app_card(i, a):
        text, cap = app_p(a)
        flip = " app-flip" if i % 2 else ""
        tags = "".join(f"<span>{escape(t)}</span>" for t in a["tags"])
        return f'''
        <article class="app-feature{flip}">
          <figure class="screenshot app-shot">
            <img src="{a["img"]}" alt="{escape(cap)}" loading="{"eager" if i == 0 else "lazy"}">
            <figcaption>{escape(cap)}</figcaption>
          </figure>
          <div class="app-body">
            <p class="app-kicker"><span class="num">0{i + 1}</span> {escape(a["tag"])}</p>
            <h3>{escape(a["name"])}</h3>
            <p>{escape(text)}</p>
            <div class="card-meta">{tags}</div>
            <div class="button-row">
              <a class="button button-primary" href="{a["page"]}">{c["page"]}</a>
              <a class="button button-secondary" href="{GH}{a["repo"]}">GitHub ↗</a>
            </div>
          </div>
        </article>'''

    def lib_card(l):
        name, repo, language, cat, tag, en, pln, install = l
        text = pln if pl else en
        inst = f'<p class="card-install"><code>{escape(install)}</code></p>' if install else ""
        return f'''
          <article class="lib-card" data-category="{cat}">
            <div class="lib-top"><span class="lang"><i class="dot dot-{LANG_CLASS[language]}"></i>{language}</span><span class="lib-tag">{tag}</span></div>
            <h3><a href="{GH}{repo}">{escape(name)}</a></h3>
            <p>{escape(text)}</p>
            {inst}
            <a class="card-link" href="{GH}{repo}">{c["src"]}</a>
          </article>'''

    filters = "".join(
        f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{escape(v)}</button>'
        for k, v in c["filters"])
    stats = "".join(f'<div><strong>{n}</strong><span>{escape(t)}</span></div>' for n, t in c["stats"])
    stack = "".join(f'<li><b>{escape(a)}</b><span>{escape(b)}</span></li>' for a, b in c["stack"])
    principles = "".join(f'<span><b>{a}</b> — {b}</span>' for a, b in c["principles"])
    nav = c["nav"]
    h1a, h1b = c["h1"]

    return f'''<!doctype html>
<html lang="{c["lang"]}">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{escape(c["desc"])}">
    <link rel="canonical" href="{self_url}">
    <link rel="alternate" hreflang="en" href="{en_url}">
    <link rel="alternate" hreflang="pl" href="{pl_url}">
    <link rel="alternate" hreflang="x-default" href="{en_url}">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="JustyBase">
    <meta property="og:locale" content="{"pl_PL" if pl else "en_US"}">
    <meta property="og:title" content="{escape(c["title"])}">
    <meta property="og:description" content="{escape(c["og_desc"])}">
    <meta property="og:url" content="{self_url}">
    <meta property="og:image" content="{SITE}assets/img/justybase-mark.svg">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{escape(c["title"])}">
    <meta name="twitter:description" content="{escape(c["og_desc"])}">
    <title>{escape(c["title"])}</title>
    <link rel="icon" type="image/svg+xml" href="{up}assets/img/favicon.svg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;700&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{up}assets/css/style.css">
    <script src="{up}assets/js/theme.js" defer></script>
    <script src="{up}assets/js/lightbox.js" defer></script>
    <script src="{up}assets/js/filter.js" defer></script>
    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "JustyBase",
        "url": "{SITE}",
        "logo": "{SITE}assets/img/justybase-mark.svg",
        "sameAs": ["https://github.com/justybase"]
      }}
    </script>
  </head>
  <body>
    <div class="utility-bar">
      <div class="container utility-inner">
        <span>{c["util_l"]}</span>
        <span>{c["util_r"]}</span>
      </div>
    </div>
    <header class="site-header">
      <nav class="nav" aria-label="{c["nav_aria"]}">
        <a class="brand" href="./"><img src="{up}assets/img/justybase-mark.svg" alt="">JustyBase</a>
        <div class="nav-links">
          <a href="#apps">{nav[0]}</a>
          <a href="#libraries">{nav[1]}</a>
          <a href="#stack">{nav[2]}</a>
          <a href="#approach">{nav[3]}</a>
          <a href="https://github.com/justybase">{c["gh"]}</a>
          <a class="lang-switch" href="{alt_href}" hreflang="{"en" if pl else "pl"}" lang="{"en" if pl else "pl"}" aria-label="{c["lang_aria"]}">{c["lang_switch"]}</a>
          <button class="theme-toggle" type="button" data-theme-toggle aria-pressed="false" data-label-dark="{c["theme_dark"]}" data-label-light="{c["theme_light"]}" data-aria-dark="{c["aria_dark"]}" data-aria-light="{c["aria_light"]}" aria-label="{c["aria_dark"]}"><span data-theme-icon aria-hidden="true">◐</span><span data-theme-label>{c["theme_dark"]}</span></button>
        </div>
      </nav>
    </header>

    <main>
      <section class="hero container">
        <div class="hero-content">
          <div class="hero-brand">
            <img src="{up}assets/img/justybase-mark.svg" alt="" width="48" height="48">
            <span>JustyBase</span>
          </div>
          <p class="eyebrow">{c["eyebrow"]}</p>
          <h1>{h1a}<span class="accent">{h1b}</span></h1>
          <p class="hero-copy">{c["lead"]}</p>
          <div class="button-row">
            <a class="button button-primary" href="#apps">{c["cta1"]}</a>
            <a class="button button-secondary" href="https://github.com/justybase">{c["cta2"]}</a>
          </div>
          <div class="hero-stats">{stats}</div>
        </div>
        <figure class="screenshot screenshot-hero hero-screenshot">
          <img src="{RAW}justybase/main/pictures/evo_dark.png" alt="{escape(c["hero_alt"])}" loading="eager">
          <figcaption>{c["hero_cap"]}</figcaption>
        </figure>
      </section>

      <section class="section container" id="apps">
        <div class="section-heading">
          <div><p class="section-index">{c["apps_idx"]}</p><h2>{c["apps_h"]}</h2></div>
          <p>{c["apps_p"]}</p>
        </div>
        <div class="app-list">{"".join(app_card(i, a) for i, a in enumerate(APPS))}
        </div>
      </section>

      <section class="section container" id="libraries">
        <div class="section-heading">
          <div><p class="section-index">{c["libs_idx"]}</p><h2>{c["libs_h"]}</h2></div>
          <p>{c["libs_p"]}</p>
        </div>
        <div class="filter-bar" role="group" aria-label="{c["filter_aria"]}">{filters}</div>
        <div class="lib-grid">{"".join(lib_card(l) for l in LIBS)}
        </div>
      </section>

      <section class="section container" id="stack">
        <div class="section-heading">
          <div><p class="section-index">{c["stack_idx"]}</p><h2>{c["stack_h"]}</h2></div>
          <p>{c["stack_p"]}</p>
        </div>
        <ul class="stack-grid">{stack}</ul>
      </section>

      <section class="section section-approach container" id="approach">
        <div class="approach-grid">
          <div><p class="section-index">{c["app_idx"]}</p><h2>{c["app_h"]}</h2></div>
          <div class="approach-copy">
            <p>{c["app_p"]}</p>
            <div class="principles">{principles}</div>
          </div>
        </div>
      </section>

      <section class="section container">
        <div class="cta-band">
          <div><h2>{c["cta_h"]}</h2><p>{c["cta_p"]}</p></div>
          <a class="button button-primary" href="https://github.com/justybase">{c["cta_b"]}</a>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <div class="container footer-inner">
        <p>{c["foot"]}</p>
        <a class="text-link" href="https://github.com/justybase">github.com/justybase ↗</a>
      </div>
    </footer>
  </body>
</html>
'''


(ROOT / "pl").mkdir(exist_ok=True)
(ROOT / "index.html").write_text(render("en"), encoding="utf-8")
(ROOT / "pl" / "index.html").write_text(render("pl"), encoding="utf-8")
print("written index.html, pl/index.html")
