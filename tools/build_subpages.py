#!/usr/bin/env python3
"""Generate Polish product pages (pl/<page>/index.html) from the English ones,
and wire language switchers / hreflang into the English pages.

Run from the repository root:  python3 tools/build_subpages.py
The English page is the source of truth; the dictionaries below hold the Polish copy.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://justybase.github.io/"

COMMON = [
    ('<nav class="nav" aria-label="Main navigation">', '<nav class="nav" aria-label="Nawigacja główna">'),
    ('<a href="../#apps">Products</a>', '<a href="../#apps">Aplikacje</a>'),
    ('Source ↗</a>', 'Kod źródłowy ↗</a>'),
    ('aria-label="Switch to dark theme"', 'data-label-dark="Tryb ciemny" data-label-light="Tryb jasny" data-aria-dark="Przełącz na ciemny motyw" data-aria-light="Przełącz na jasny motyw" aria-label="Przełącz na ciemny motyw"'),
    ('<span data-theme-label>Dark mode</span>', '<span data-theme-label>Tryb ciemny</span>'),
    ('<a class="breadcrumb" href="../">← JustyBase</a>', '<a class="breadcrumb" href="../">← JustyBase</a>'),
    ('<a class="text-link" href="../">← Back to JustyBase</a>', '<a class="text-link" href="../">← Powrót do JustyBase</a>'),
    ('Documentation &amp; source', 'Dokumentacja i kod źródłowy'),
    ('Documentation & source', 'Dokumentacja i kod źródłowy'),
    ('Read the full README ↗', 'Przeczytaj pełny README ↗'),
    ('View releases ↗', 'Zobacz wydania ↗'),
    ('Browse documentation ↗', 'Przeglądaj dokumentację ↗'),
    ('GitHub Releases ↗', 'Wydania na GitHubie ↗'),
    ('Download installer ↗', 'Pobierz instalator ↗'),
    ('Download ZIP ↗', 'Pobierz ZIP ↗'),
    ('Download ↗', 'Pobierz ↗'),
    ('IN THE WORKSPACE', 'W PRZESTRZENI ROBOCZEJ'),
    ('PRODUCT MODEL', 'MODEL PRODUKTU'),
    ('/ DOWNLOAD', '/ POBIERANIE'),
    ('/ FEATURES', '/ FUNKCJE'),
    ('Light and dark themes are both first-class. Screenshots are served from the product repository.', 'Motywy jasny i ciemny są równorzędne. Zrzuty ekranu pochodzą z repozytorium produktu.'),
    ('<strong>Important:</strong>', '<strong>Ważne:</strong>'),
]

PAGES = {
    "vscode": {
        "title": ("JustyBase SQL Editor for VS Code — JustyBase", "JustyBase SQL Editor dla VS Code — JustyBase"),
        "pairs": [
            ('VS Code extension · Netezza SQL editor + database packs', 'Rozszerzenie VS Code · edytor SQL Netezza + paczki baz danych'),
            ('<span class="accent">for VS Code.</span>', '<span class="accent">dla VS Code.</span>'),
            ('JustyBase SQL Editor is a Netezza-first SQL extension for Visual Studio Code. It brings Netezza and PureData SQL development, schema browsing, query results, and database workflows into one editor. The Netezza package is the required base; install optional packs for PostgreSQL, MySQL, Oracle, Db2, DuckDB, and more.',
             'JustyBase SQL Editor to rozszerzenie SQL dla Visual Studio Code zorientowane na Netezza. Łączy w jednym edytorze pracę z SQL Netezza i PureData, przeglądanie schematu, wyniki zapytań i przepływy bazodanowe. Paczka Netezza jest wymaganym pakietem podstawowym; opcjonalne paczki dodają PostgreSQL, MySQL, Oracle, Db2, DuckDB i inne.'),
            ('Install the base package</a>', 'Zainstaluj pakiet podstawowy</a>'),
            ('Open Marketplace ↗', 'Otwórz Marketplace ↗'),
            ('Required base: Netezza', 'Wymagany pakiet podstawowy: Netezza'),
            ('<span>Optional database packs</span>', '<span>Opcjonalne paczki baz danych</span>'),
            ('Connections, schema, SQL, and results in the VS Code workspace', 'Połączenia, schemat, SQL i wyniki w przestrzeni roboczej VS Code'),
            ('SUPPORT MODEL', 'MODEL WSPARCIA'),
            ('Netezza is the base. Other databases are companions.', 'Netezza to podstawa. Inne bazy danych to dodatki.'),
            ('REQUIRED</div>', 'WYMAGANE</div>'),
            ('OPTIONAL</div>', 'OPCJONALNE</div>'),
            ('Install this package first. It provides the shared VS Code workspace, connection and schema experience, results grid, import/export, notebooks, Copilot integration, and the complete Netezza/PureData dialect stack.',
             'Zainstaluj tę paczkę jako pierwszą. Zapewnia wspólną przestrzeń roboczą VS Code, obsługę połączeń i schematu, siatkę wyników, import/eksport, notebooki, integrację z Copilotem i pełny stos dialektu Netezza/PureData.'),
            ('FULL DIALECT TOOLING', 'PEŁNE NARZĘDZIA DIALEKTU'),
            ('BUILT-IN NETEZZA DRIVER', 'WBUDOWANY STEROWNIK NETEZZA'),
            ('<h3>Database packs</h3>', '<h3>Paczki baz danych</h3>'),
            ('Install one matching pack for each additional database. They reuse the same workspace for connections, schema, queries, results, and exports, with database-specific capabilities where implemented.',
             'Zainstaluj jedną pasującą paczkę dla każdej dodatkowej bazy. Korzystają z tej samej przestrzeni roboczej dla połączeń, schematu, zapytań, wyników i eksportów, z funkcjami specyficznymi dla bazy tam, gdzie je zaimplementowano.'),
            ('SQLite · built in', 'SQLite · wbudowane'),
            ('optional packs do not replace the base Netezza extension. The deepest parser, linting, procedure diagnostics, and Netezza-specific workflows remain in the main extension; other databases receive the shared workflow plus the support implemented by their pack.',
             'opcjonalne paczki nie zastępują podstawowego rozszerzenia Netezza. Najgłębszy parser, linting, diagnostyka procedur i przepływy specyficzne dla Netezza pozostają w głównym rozszerzeniu; pozostałe bazy otrzymują wspólny przepływ pracy oraz wsparcie zaimplementowane w ich paczce.'),
            ('MANUAL INSTALL', 'INSTALACJA RĘCZNA'),
            ('Install the right pieces.', 'Zainstaluj właściwe elementy.'),
            ('Download the latest verified VSIX files from GitHub Releases. Install the base package before any optional pack.', 'Pobierz najnowsze zweryfikowane pliki VSIX z wydań na GitHubie. Pakiet podstawowy instaluj przed jakąkolwiek paczką opcjonalną.'),
            ('REQUIRED BASE</div>', 'PAKIET PODSTAWOWY</div>'),
            ('Install the base VSIX first. It is the main JustyBase extension and the foundation for all optional database packs.', 'Najpierw zainstaluj VSIX pakietu podstawowego. To główne rozszerzenie JustyBase i fundament wszystkich opcjonalnych paczek baz danych.'),
            ('Download latest release ↗', 'Pobierz najnowsze wydanie ↗'),
            ('OPTIONAL · ONE VSIX EACH', 'OPCJONALNE · PO JEDNYM VSIX'),
            ('After installing the base package, add only the database runtimes you need.', 'Po instalacji pakietu podstawowego dodaj tylko te środowiska baz danych, których potrzebujesz.'),
            ('OPTIONAL · PLATFORM BUILDS', 'OPCJONALNE · BUILDY PLATFORMOWE'),
            ('<h3>Db2 and DuckDB</h3>', '<h3>Db2 i DuckDB</h3>'),
            ('These packs are shipped as separate VSIX files per platform. Choose the file matching your operating system and CPU architecture.', 'Te paczki są dostarczane jako osobne pliki VSIX dla każdej platformy. Wybierz plik pasujący do systemu operacyjnego i architektury procesora.'),
            ('>macOS · Apple Silicon<', '>macOS · Apple Silicon<'),
            ('The current release provides macOS Apple Silicon builds for these two packs. Check the release assets if you need a different architecture.', 'Bieżące wydanie zawiera dla tych dwóch paczek buildy macOS Apple Silicon. Jeśli potrzebujesz innej architektury, sprawdź zasoby wydania.'),
            ('<p>Install the <strong>JustyBase SQL Editor</strong> package.</p>', '<p>Zainstaluj paczkę <strong>JustyBase SQL Editor</strong>.</p>'),
            ('Install the optional pack for each additional database you use.', 'Zainstaluj opcjonalną paczkę dla każdej dodatkowej bazy, z której korzystasz.'),
            ('Reload VS Code, then open the JustyBase view and connect.', 'Przeładuj VS Code, następnie otwórz widok JustyBase i połącz się.'),
            ('Checking latest release…', 'Sprawdzanie najnowszego wydania…'),
            ('>Windows<', '>Windows<'),
            ('One familiar workflow.', 'Jeden znajomy przepływ pracy.'),
            ('Optional database packs use the same connection, schema, results, and import/export workspace.', 'Opcjonalne paczki baz danych korzystają z tej samej przestrzeni połączeń, schematu, wyników i importu/eksportu.'),
            ('Netezza-aware authoring — parser-backed diagnostics and Copilot help catch mistakes before execution.', 'Pisanie świadome Netezza — diagnostyka oparta na parserze i pomoc Copilota wychwytują błędy przed wykonaniem.'),
            ('Explore results instead of writing another query — profiles, distributions, and summaries.', 'Eksploruj wyniki zamiast pisać kolejne zapytanie — profile, rozkłady i podsumowania.'),
            ('Visualize result sets as interactive charts without leaving the SQL workspace.', 'Wizualizuj zbiory wyników jako interaktywne wykresy bez opuszczania przestrzeni SQL.'),
            ('Use AI with explicit control — explain, fix, optimize, or generate SQL.', 'Używaj AI z pełną kontrolą — wyjaśniaj, naprawiaj, optymalizuj lub generuj SQL.'),
            ('The README and docs in the extension repository remain the source of truth for supported capabilities, compatibility, and release details.', 'README i dokumentacja w repozytorium rozszerzenia pozostają źródłem prawdy o obsługiwanych funkcjach, zgodności i szczegółach wydań.'),
            ('Project website ↗', 'Strona projektu ↗'),
            ('Documentation guide ↗', 'Przewodnik po dokumentacji ↗'),
            ('JustyBase SQL Editor FAQ', 'FAQ JustyBase SQL Editor'),
            ('What is JustyBase SQL Editor?', 'Czym jest JustyBase SQL Editor?'),
            ('It is a Netezza-first database and SQL extension for Visual Studio Code, with a built-in driver and a shared workspace for connections, schemas, queries, and results.', 'To rozszerzenie bazodanowe i SQL dla Visual Studio Code zorientowane na Netezza, z wbudowanym sterownikiem i wspólną przestrzenią roboczą dla połączeń, schematów, zapytań i wyników.'),
            ('Is the Netezza package required?', 'Czy paczka Netezza jest wymagana?'),
            ('Yes. The Netezza package provides the shared JustyBase workspace and is required before installing optional database packs.', 'Tak. Paczka Netezza zapewnia wspólną przestrzeń roboczą JustyBase i jest wymagana przed instalacją opcjonalnych paczek baz danych.'),
            ('Which databases have optional packs?', 'Które bazy danych mają opcjonalne paczki?'),
            ('Optional packs are available for PostgreSQL, MySQL, Oracle, Microsoft SQL Server, Db2, DuckDB, Snowflake, and Vertica. SQLite support is built in.', 'Opcjonalne paczki są dostępne dla PostgreSQL, MySQL, Oracle, Microsoft SQL Server, Db2, DuckDB, Snowflake i Vertica. Obsługa SQLite jest wbudowana.'),
            ('<p>JustyBase SQL Editor for VS Code</p>', '<p>JustyBase SQL Editor dla VS Code</p>'),
            ("`Download base package · ${release.tag_name}`", "`Pobierz pakiet podstawowy · ${release.tag_name}`"),
            ('`Latest verified release: ${release.tag_name}`', '`Najnowsze zweryfikowane wydanie: ${release.tag_name}`'),
            ("'Latest release lookup unavailable — open the latest release and choose the matching VSIX asset.'", "'Nie można sprawdzić najnowszego wydania — otwórz je i wybierz odpowiedni plik VSIX.'"),
            ('"Netezza and PureData SQL tooling for Visual Studio Code with schema browsing, query results, import/export, notebooks, and optional database packs."', '"Narzędzia SQL dla Netezza i PureData w Visual Studio Code: przeglądanie schematu, wyniki zapytań, import/eksport, notebooki i opcjonalne paczki baz danych."'),
            ('"url": "https://justybase.github.io/vscode/"', '"url": "https://justybase.github.io/pl/vscode/"'),
        ],
        "meta": ("Netezza-first SQL extension", "Rozszerzenie SQL dla VS Code"),
    },
}

PAGES["justybase"] = {
    "pairs": [
        ('Cross-platform desktop · Netezza-first', 'Aplikacja desktopowa · wiele platform · Netezza w centrum'),
        ('<span class="accent">. Desktop SQL, kept close to the data.</span>', '<span class="accent">. Desktopowy SQL, blisko danych.</span>'),
        ('A cross-platform SQL IDE for IBM Netezza Performance Server, built with Avalonia UI and .NET 10. Write and run SQL, explore schemas, work with Git-backed files, inspect results, and use optional local AI assistance in one focused desktop workspace.',
         'Wieloplatformowe IDE SQL dla IBM Netezza Performance Server, zbudowane w Avalonia UI i .NET 10. Pisz i uruchamiaj SQL, eksploruj schematy, pracuj z plikami w Gicie, analizuj wyniki i korzystaj z opcjonalnej lokalnej pomocy AI w jednym, skupionym środowisku desktopowym.'),
        ('>Download JustyBase<', '>Pobierz JustyBase<'),
        ('SQL editor, schema explorer, and query results in one desktop workspace', 'Edytor SQL, eksplorator schematu i wyniki zapytań w jednym środowisku desktopowym'),
        ('Netezza is the current focus. The workspace is built to grow.', 'Netezza jest obecnym celem. Środowisko zbudowano z myślą o rozwoju.'),
        ('CURRENT FOCUS', 'OBECNY CEL'),
        ('IN DEVELOPMENT', 'W ROZWOJU'),
        ('JustyBase combines Netezza-first SQL authoring, schema exploration, multi-connection work, result inspection, and data import/export in a native desktop application.',
         'JustyBase łączy pisanie SQL zorientowane na Netezza, eksplorację schematu, pracę z wieloma połączeniami, analizę wyników oraz import/eksport danych w natywnej aplikacji desktopowej.'),
        ('NETEZZA CORE', 'RDZEŃ NETEZZA'),
        ('DESKTOP IDE', 'IDE DESKTOPOWE'),
        ('CROSS-PLATFORM', 'WIELOPLATFORMOWE'),
        ('<h3>Additional database engines</h3>', '<h3>Dodatkowe silniki baz danych</h3>'),
        ('PostgreSQL, Db2, Snowflake, Oracle, DuckDB, MySQL, and SQLite are represented in the plugin architecture, but the repository marks them as coming soon or work in progress.',
         'PostgreSQL, Db2, Snowflake, Oracle, DuckDB, MySQL i SQLite są uwzględnione w architekturze wtyczek, ale repozytorium oznacza je jako „wkrótce” lub prace w toku.'),
        ('<strong>AI is opt-in:</strong> embedded FIM runs locally with a user-selected GGUF model. Ollama and LM Studio use local endpoints; remote AI providers receive only the context selected for the active request.',
         '<strong>AI jest opcjonalne:</strong> wbudowane FIM działa lokalnie z wybranym przez użytkownika modelem GGUF. Ollama i LM Studio używają lokalnych endpointów; zdalni dostawcy AI otrzymują wyłącznie kontekst wybrany dla bieżącego żądania.'),
        ('Light and dark themes are both first-class. Screenshots are served from the source repository.', 'Motywy jasny i ciemny są równorzędne. Zrzuty ekranu pochodzą z repozytorium źródłowego.'),
        ('Choose your desktop.', 'Wybierz swój system.'),
        ('Release builds are Native AOT packages for Windows x64, Linux x64, and macOS Apple Silicon. Windows also has an installer.', 'Wydania to paczki Native AOT dla Windows x64, Linux x64 i macOS Apple Silicon. Dla Windows dostępny jest także instalator.'),
        ('RECOMMENDED · WINDOWS', 'ZALECANE · WINDOWS'),
        ('PORTABLE · WINDOWS', 'PRZENOŚNE · WINDOWS'),
        ('PORTABLE · LINUX', 'PRZENOŚNE · LINUX'),
        ('PORTABLE · MACOS', 'PRZENOŚNE · MACOS'),
        ('<h3>Windows installer</h3>', '<h3>Instalator Windows</h3>'),
        ('Velopack installer for Windows x64. The simplest way to install JustyBase on a regular desktop.', 'Instalator Velopack dla Windows x64. Najprostszy sposób instalacji JustyBase na zwykłym komputerze.'),
        ('Portable Windows x64 package. Extract it and run without a traditional installation.', 'Przenośna paczka Windows x64. Rozpakuj i uruchom bez tradycyjnej instalacji.'),
        ('Native AOT Linux x64 archive for a portable desktop setup.', 'Archiwum Native AOT dla Linux x64 do przenośnej instalacji desktopowej.'),
        ('<h3>macOS Apple Silicon ZIP</h3>', '<h3>ZIP dla macOS Apple Silicon</h3>'),
        ('Native AOT package for macOS ARM64, intended for Apple Silicon Macs.', 'Paczka Native AOT dla macOS ARM64, przeznaczona dla komputerów Mac z Apple Silicon.'),
        ('Download Linux build ↗', 'Pobierz build dla Linuksa ↗'),
        ('Download macOS build ↗', 'Pobierz build dla macOS ↗'),
        ('Download the package matching your operating system and architecture.', 'Pobierz paczkę pasującą do systemu operacyjnego i architektury.'),
        ('Run the Windows installer, or extract the portable ZIP on Linux or macOS.', 'Uruchom instalator Windows lub rozpakuj przenośny ZIP na Linuksie albo macOS.'),
        ('Add a Netezza connection, open a SQL document, and start working.', 'Dodaj połączenie z Netezza, otwórz dokument SQL i zacznij pracę.'),
        ('Checking available release assets…', 'Sprawdzanie dostępnych zasobów wydania…'),
        ('A SQL workspace with useful edges.', 'Środowisko SQL z przydatnymi detalami.'),
        ('Focused tools for the loop from SQL file to database result, with local-first assistance when you want it.', 'Skupione narzędzia na całej drodze od pliku SQL do wyniku z bazy, z lokalną pomocą, gdy jej potrzebujesz.'),
        ('<h2>SQL editor</h2><p>Syntax highlighting, folding, autocomplete, Quick Open, and Netezza-oriented authoring for everyday query work.</p>', '<h2>Edytor SQL</h2><p>Podświetlanie składni, zwijanie kodu, autouzupełnianie, Quick Open i pisanie zorientowane na Netezza w codziennej pracy z zapytaniami.</p>'),
        ('<h2>Schema exploration</h2><p>Inspect database objects and connections without leaving the editor workspace.</p>', '<h2>Eksploracja schematu</h2><p>Przeglądaj obiekty bazy i połączenia bez opuszczania edytora.</p>'),
        ('<h2>Git-aware workflow</h2><p>Review status, stage changes, inspect history and diffs, and commit SQL-backed work from the application.</p>', '<h2>Przepływ z Gitem</h2><p>Sprawdzaj status, dodawaj zmiany, przeglądaj historię i różnice oraz zatwierdzaj pracę z SQL bezpośrednio w aplikacji.</p>'),
        ('<h2>Data tools</h2><p>Group and filter results, then export data to Excel, CSV, or Parquet.</p>', '<h2>Narzędzia do danych</h2><p>Grupuj i filtruj wyniki, a następnie eksportuj dane do Excela, CSV lub Parquet.</p>'),
        ('<h2>Optional local AI</h2><p>Use embedded FIM with GGUF models, or connect to Ollama and LM Studio. AI features are disabled by default.</p>', '<h2>Opcjonalne lokalne AI</h2><p>Używaj wbudowanego FIM z modelami GGUF lub połącz się z Ollama i LM Studio. Funkcje AI są domyślnie wyłączone.</p>'),
        ('<h2>Native AOT</h2><p>Release packages target fast, self-contained desktop startup across Windows, Linux, and Apple Silicon.</p>', '<h2>Native AOT</h2><p>Paczki wydań zapewniają szybki start samodzielnej aplikacji w Windows, Linuksie i na Apple Silicon.</p>'),
        ('See the workflow.', 'Zobacz przepływ pracy.'),
        ('Import workflow for moving data into the workspace — dark theme', 'Import danych do przestrzeni roboczej — ciemny motyw'),
        ('Settings and application configuration — dark theme', 'Ustawienia i konfiguracja aplikacji — ciemny motyw'),
        ('Import workflow — light theme', 'Import danych — jasny motyw'),
        ('Settings and application configuration — light theme', 'Ustawienia i konfiguracja aplikacji — jasny motyw'),
        ('The README and docs in the product repository remain the source of truth for supported databases, AI privacy, architecture, builds, and contribution workflows.', 'README i dokumentacja w repozytorium produktu pozostają źródłem prawdy o obsługiwanych bazach, prywatności AI, architekturze, buildach i współtworzeniu.'),
        ('<h2>JustyBase FAQ</h2>', '<h2>FAQ JustyBase</h2>'),
        ('What is JustyBase?', 'Czym jest JustyBase?'),
        ('It is a cross-platform desktop SQL IDE focused on IBM Netezza Performance Server, with SQL editing, schema exploration, Git workflows, data tools, and optional local AI assistance.', 'To wieloplatformowe desktopowe IDE SQL skupione na IBM Netezza Performance Server: edycja SQL, eksploracja schematu, przepływy Git, narzędzia do danych i opcjonalna lokalna pomoc AI.'),
        ('Which operating systems are supported?', 'Które systemy operacyjne są obsługiwane?'),
        ('The release workflow packages Windows x64, Linux x64, and macOS ARM64 builds. The macOS package targets Apple Silicon.', 'Proces wydawniczy buduje paczki dla Windows x64, Linux x64 i macOS ARM64. Paczka dla macOS jest przeznaczona dla Apple Silicon.'),
        ('Which databases are supported today?', 'Które bazy danych są dziś obsługiwane?'),
        ('Netezza is the current supported focus. Other engines are present in the plugin architecture but are marked in the repository as coming soon or work in progress.', 'Obecnie wspierana jest Netezza. Pozostałe silniki są w architekturze wtyczek, ale repozytorium oznacza je jako „wkrótce” lub prace w toku.'),
        ('Does AI send my SQL to a remote service?', 'Czy AI wysyła mój SQL do zdalnej usługi?'),
        ('AI is opt-in. Embedded FIM runs locally; Ollama and LM Studio use configured local endpoints. Remote provider behavior depends on the provider and the context you explicitly send.', 'AI jest opcjonalne. Wbudowane FIM działa lokalnie; Ollama i LM Studio używają skonfigurowanych lokalnych endpointów. Zachowanie zdalnych dostawców zależy od dostawcy i kontekstu, który jawnie wyślesz.'),
        ('<p>JustyBase · Cross-platform desktop SQL IDE</p>', '<p>JustyBase · Wieloplatformowe desktopowe IDE SQL</p>'),
        ("'No packaged release yet — open GitHub Releases for source and release updates.'", "'Brak jeszcze spakowanego wydania — zajrzyj na GitHub Releases po kod i aktualizacje.'"),
        ('`Latest packaged release: ${release.tag_name}`', '`Najnowsze wydanie: ${release.tag_name}`'),
        ("'Release lookup unavailable — open GitHub Releases and choose the package for your platform.'", "'Nie można sprawdzić wydania — otwórz GitHub Releases i wybierz paczkę dla swojej platformy.'"),
        ('"Cross-platform desktop SQL IDE for IBM Netezza with SQL editing, schema exploration, Git workflows, data tools, and optional local AI assistance."', '"Wieloplatformowe desktopowe IDE SQL dla IBM Netezza: edycja SQL, eksploracja schematu, przepływy Git, narzędzia do danych i opcjonalna lokalna pomoc AI."'),
        ('"url": "https://justybase.github.io/justybase/"', '"url": "https://justybase.github.io/pl/justybase/"'),
    ],
}

PAGES["legacy"] = {
    "pairs": [
        ('Windows desktop · Netezza-first', 'Windows desktop · Netezza w centrum'),
        ('A Windows SQL client for IBM Netezza / PureData. Write and run SQL, browse catalog objects, tune preferences in a docked settings tab, and keep connection profiles encrypted on disk — built on .NET 10.',
         'Windowsowy klient SQL dla IBM Netezza / PureData. Pisz i uruchamiaj SQL, przeglądaj obiekty katalogu, konfiguruj preferencje w zadokowanej zakładce i trzymaj profile połączeń zaszyfrowane na dysku — zbudowany na .NET 10.'),
        ('>Download for Windows<', '>Pobierz dla Windows<'),
        ('Self-contained · .NET 10', 'Samodzielny · .NET 10'),
        ('SQL editor, result grid, and database explorer — dark theme', 'Edytor SQL, siatka wyników i eksplorator bazy — ciemny motyw'),
        ('Netezza is the shipped default. Other engines stay optional.', 'Netezza jest domyślnym silnikiem w wydaniu. Pozostałe są opcjonalne.'),
        ('SHIPPED DEFAULT', 'DOMYŚLNIE W WYDANIU'),
        ('CONTRIBUTOR BUILDS', 'BUILDY DLA KONTRYBUTORÓW'),
        ('The release binary is a Netezza-first desktop IDE: SQL authoring, catalog browsing, results, and encrypted connection profiles for Windows x64. Packages are self-contained — no separate .NET runtime install.',
         'Binarka wydania to desktopowe IDE zorientowane na Netezza: pisanie SQL, przeglądanie katalogu, wyniki i szyfrowane profile połączeń dla Windows x64. Paczki są samodzielne — bez osobnej instalacji środowiska .NET.'),
        ('SELF-CONTAINED', 'SAMODZIELNE'),
        ('<h3>Optional providers</h3>', '<h3>Opcjonalni dostawcy</h3>'),
        ('MS SQL, Oracle, DB2, and PostgreSQL are available as optional compile-time flags for contributors. They are not included in the default release binary.', 'MS SQL, Oracle, DB2 i PostgreSQL są dostępne jako opcjonalne flagi kompilacji dla kontrybutorów. Nie wchodzą w skład domyślnej binarki wydania.'),
        ('download the public release for Netezza workflows. Extra database providers require building from source with the matching flags enabled.', 'pobierz publiczne wydanie do pracy z Netezza. Dodatkowi dostawcy baz wymagają zbudowania ze źródeł z włączonymi odpowiednimi flagami.'),
        ('Installer or portable ZIP.', 'Instalator lub przenośny ZIP.'),
        ('Get the latest Windows x64 build from GitHub Releases. Both packages are self-contained.', 'Pobierz najnowszy build Windows x64 z GitHub Releases. Obie paczki są samodzielne.'),
        ('RECOMMENDED</div>', 'ZALECANE</div>'),
        ('PORTABLE</div>', 'PRZENOŚNE</div>'),
        ('<h3>Inno Setup installer</h3>', '<h3>Instalator Inno Setup</h3>'),
        ('Standard Windows installer for JustyBase.Legacy. Best for a normal desktop install with Start Menu shortcuts.', 'Standardowy instalator Windows dla JustyBase.Legacy. Najlepszy do normalnej instalacji ze skrótami w menu Start.'),
        ('<h3>ZIP package</h3>', '<h3>Paczka ZIP</h3>'),
        ('Self-contained portable archive. Extract and run without an installer — useful for locked-down or temporary machines.', 'Samodzielne archiwum przenośne. Rozpakuj i uruchom bez instalatora — przydatne na maszynach z ograniczeniami lub tymczasowych.'),
        ('<p>Download the <strong>installer</strong> or the <strong>portable ZIP</strong> for Windows x64.</p>', '<p>Pobierz <strong>instalator</strong> lub <strong>przenośny ZIP</strong> dla Windows x64.</p>'),
        ('Run the setup, or extract the ZIP and launch the application.', 'Uruchom instalator albo rozpakuj ZIP i uruchom aplikację.'),
        ('Add an encrypted Netezza connection profile and open a SQL tab.', 'Dodaj zaszyfrowany profil połączenia z Netezza i otwórz zakładkę SQL.'),
        ('Checking latest release…', 'Sprawdzanie najnowszego wydania…'),
        ('Built for serious Netezza work.', 'Stworzony do poważnej pracy z Netezza.'),
        ('Editor, results, catalog, and preferences in one desktop workspace.', 'Edytor, wyniki, katalog i preferencje w jednym środowisku desktopowym.'),
        ('<h2>Netezza-first SQL editor</h2>', '<h2>Edytor SQL dla Netezza</h2>'),
        ('Syntax highlighting, completion, and linting aimed at NPS SQL so authoring stays close to the dialect you ship.', 'Podświetlanie składni, uzupełnianie i linting dostrojone do SQL NPS, aby pisanie pozostawało blisko dialektu, który wdrażasz.'),
        ('<h2>Virtual-mode result grid</h2>', '<h2>Siatka wyników w trybie wirtualnym</h2>'),
        ('Handle large result sets with filtering and export to CSV or Excel without freezing the UI.', 'Obsługuj duże zbiory wyników z filtrowaniem i eksportem do CSV lub Excela bez zawieszania interfejsu.'),
        ('<h2>Object explorer</h2>', '<h2>Eksplorator obiektów</h2>'),
        ('Browse connections, databases, and tables; open DDL and navigate into catalog objects from the tree.', 'Przeglądaj połączenia, bazy i tabele; otwieraj DDL i przechodź do obiektów katalogu z drzewa.'),
        ('<h2>Docked preferences</h2>', '<h2>Zadokowane preferencje</h2>'),
        ('General, Colors &amp; Editor, Snippets, Execution, and Results live as a document tab — not a modal dialog.', 'Ogólne, Kolory i edytor, Snippety, Wykonywanie i Wyniki żyją jako zakładka dokumentu — nie modalne okno.'),
        ('<h2>Encrypted profiles</h2>', '<h2>Szyfrowane profile</h2>'),
        ('Connection credentials protected with AES-GCM and DPAPI for the current Windows user.', 'Dane logowania chronione AES-GCM i DPAPI dla bieżącego użytkownika Windows.'),
        ('<h2>Release-grade pipeline</h2>', '<h2>Potok klasy wydawniczej</h2>'),
        ('Smoke tests, coverage gates, NuGet audit, and ~1,100+ automated cases behind tagged installer and ZIP releases.', 'Testy dymne, bramki pokrycia, audyt NuGet i ponad 1100 automatycznych przypadków stoją za oznaczonymi wydaniami instalatora i ZIP.'),
        ('See the desktop IDE.', 'Zobacz desktopowe IDE.'),
        ('Object explorer — catalog tree and table selection', 'Eksplorator obiektów — drzewo katalogu i wybór tabel'),
        ('Preferences as a docked document tab', 'Preferencje jako zadokowana zakładka dokumentu'),
        ('Login — encrypted connection profiles', 'Logowanie — szyfrowane profile połączeń'),
        ('Editor showcase — light theme', 'Edytor — jasny motyw'),
        ('The README, architecture decision records, and release notes in the repository remain the source of truth for build steps, security, and contributor workflows.', 'README, rekordy decyzji architektonicznych i notatki wydań w repozytorium pozostają źródłem prawdy o krokach budowania, bezpieczeństwie i współtworzeniu.'),
        ('Browse ADRs ↗', 'Przeglądaj ADR ↗'),
        ('<h2>JustyBase.Legacy FAQ</h2>', '<h2>FAQ JustyBase.Legacy</h2>'),
        ('What is JustyBase.Legacy?', 'Czym jest JustyBase.Legacy?'),
        ('It is a Windows desktop SQL client focused on IBM Netezza / PureData — a Netezza-first IDE for authoring SQL, browsing the catalog, reviewing results, and managing encrypted connection profiles.', 'To desktopowy klient SQL dla Windows skupiony na IBM Netezza / PureData — IDE do pisania SQL, przeglądania katalogu, analizy wyników i zarządzania szyfrowanymi profilami połączeń.'),
        ('Is it Windows-only?', 'Czy działa tylko w Windows?'),
        ('Yes. Public releases target Windows x64. Release packages are self-contained and do not require a separate .NET runtime install.', 'Tak. Publiczne wydania są dla Windows x64. Paczki są samodzielne i nie wymagają osobnej instalacji środowiska .NET.'),
        ('Does the download include MS SQL, Oracle, DB2, or PostgreSQL?', 'Czy pobierana wersja zawiera MS SQL, Oracle, DB2 lub PostgreSQL?'),
        ('No. The shipped binary is Netezza-first. Other providers are optional compile-time flags for contributors who build from source.', 'Nie. Dostarczana binarka skupia się na Netezza. Inni dostawcy to opcjonalne flagi kompilacji dla kontrybutorów budujących ze źródeł.'),
        ('Installer or ZIP — which should I use?', 'Instalator czy ZIP — co wybrać?'),
        ('Use the Inno Setup installer for a normal desktop install. Use the portable ZIP when you need to extract and run without installing.', 'Instalator Inno Setup wybierz do zwykłej instalacji. Przenośny ZIP — gdy chcesz rozpakować i uruchomić bez instalowania.'),
        ('<p>JustyBase.Legacy · Windows SQL client for Netezza</p>', '<p>JustyBase.Legacy · Windowsowy klient SQL dla Netezza</p>'),
        ('`Download installer · ${release.tag_name}`', '`Pobierz instalator · ${release.tag_name}`'),
        ('`Download ZIP · ${release.tag_name}`', '`Pobierz ZIP · ${release.tag_name}`'),
        ('`Latest release: ${release.tag_name}`', '`Najnowsze wydanie: ${release.tag_name}`'),
        ("'Latest release lookup unavailable — open GitHub Releases and choose the installer or ZIP asset.'", "'Nie można sprawdzić najnowszego wydania — otwórz GitHub Releases i wybierz instalator lub ZIP.'"),
        ('"Windows desktop SQL client for IBM Netezza / PureData with a Netezza-first editor, result grid, object explorer, and encrypted connection profiles."', '"Desktopowy klient SQL dla Windows i IBM Netezza / PureData z edytorem, siatką wyników, eksploratorem obiektów i szyfrowanymi profilami połączeń."'),
        ('"url": "https://justybase.github.io/legacy/"', '"url": "https://justybase.github.io/pl/legacy/"'),
    ],
}


def english_page(page, html):
    """Idempotently add hreflang links and a language switcher to the EN page."""
    html = html.replace('href="../#products"', 'href="../#apps"')
    if "hreflang" not in html:
        links = (f'    <link rel="alternate" hreflang="en" href="{SITE}{page}/">\n'
                 f'    <link rel="alternate" hreflang="pl" href="{SITE}pl/{page}/">\n'
                 f'    <link rel="alternate" hreflang="x-default" href="{SITE}{page}/">\n')
        html = re.sub(r'(    <link rel="canonical"[^\n]*\n)', lambda m: m.group(1) + links, html, count=1)
        switch = f'<a class="lang-switch" href="../pl/{page}/" hreflang="pl" lang="pl" aria-label="Przełącz na język polski">Polski</a>\n          '
        html = html.replace('<button class="theme-toggle"', switch + '<button class="theme-toggle"', 1)
    return html


def polish_page(page, html, spec):
    for old, new in COMMON + spec["pairs"]:
        html = html.replace(old, new)
    for old, new in [("../assets/", "../../assets/")]:
        html = html.replace(old, new)
    html = html.replace('<html lang="en">', '<html lang="pl">')
    # head metadata
    html = re.sub(r'<meta name="description" content="[^"]*">',
                  lambda m: f'<meta name="description" content="{spec["desc"]}">', html, count=1)
    html = re.sub(r'<title>[^<]*</title>', f'<title>{spec["title"]}</title>', html, count=1)
    html = html.replace(f'<link rel="canonical" href="{SITE}{page}/">', f'<link rel="canonical" href="{SITE}pl/{page}/">')
    html = html.replace('<meta property="og:url" content="' + f'{SITE}{page}/">', '<meta property="og:url" content="' + f'{SITE}pl/{page}/">')
    html = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{spec["title"]}">', html)
    html = re.sub(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{spec["title"]}">', html)
    html = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{spec["desc"]}">', html)
    html = re.sub(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{spec["desc"]}">', html)
    html = html.replace('<meta property="og:site_name" content="JustyBase">', '<meta property="og:site_name" content="JustyBase">\n    <meta property="og:locale" content="pl_PL">')
    html = html.replace('hreflang="en" href="' + f'{SITE}{page}/">', 'hreflang="en" href="' + f'{SITE}{page}/">')
    # language switcher -> English
    html = re.sub(r'<a class="lang-switch"[^>]*>Polski</a>',
                  '<a class="lang-switch" href="../../' + page + '/" hreflang="en" lang="en" aria-label="Switch to English">English</a>', html)
    return html


DESC = {
    "vscode": "Rozszerzenie SQL dla Visual Studio Code zorientowane na Netezza: przeglądanie schematu, wyniki zapytań, import/eksport, notebooki oraz opcjonalne paczki baz danych.",
    "justybase": "JustyBase — wieloplatformowe desktopowe IDE SQL dla IBM Netezza w Avalonia i .NET 10. Edytor SQL, eksplorator schematu, przepływy Git, narzędzia do danych i opcjonalna lokalna AI.",
    "legacy": "JustyBase.Legacy — windowsowy klient SQL dla IBM Netezza / PureData: edytor, siatka wyników, eksplorator obiektów i szyfrowane profile połączeń.",
}
TITLE = {
    "vscode": "JustyBase SQL Editor dla VS Code — JustyBase",
    "justybase": "JustyBase — wieloplatformowe desktopowe IDE SQL",
    "legacy": "JustyBase.Legacy — windowsowy klient SQL dla Netezza",
}

for page, spec in PAGES.items():
    spec["desc"], spec["title"] = DESC[page], TITLE[page]
    src = ROOT / page / "index.html"
    en = english_page(page, src.read_text(encoding="utf-8"))
    src.write_text(en, encoding="utf-8")
    missing = [old for old, _ in spec["pairs"] if old not in en]
    if missing:
        raise SystemExit(f"{page}: untranslated keys not found in source: {missing[:3]}")
    out = ROOT / "pl" / page / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(polish_page(page, en, spec), encoding="utf-8")
    print("written", out.relative_to(ROOT))
