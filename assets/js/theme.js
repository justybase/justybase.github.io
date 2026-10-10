(function applyThemePreference() {
  function safeGet() { try { return window.localStorage.getItem('justybase-theme'); } catch (e) { return null; } }
  const root = document.documentElement;
  const toggle = document.querySelector('[data-theme-toggle]');
  const storedTheme = safeGet();
  const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  const initialTheme = storedTheme === 'dark' || storedTheme === 'light' ? storedTheme : systemTheme;

  function updateToggle(theme) {
    if (!toggle) return;
    const dark = theme === 'dark';
    toggle.setAttribute('aria-pressed', String(dark));
    const d = toggle.dataset;
    toggle.setAttribute('aria-label', dark ? (d.ariaLight || 'Switch to light theme') : (d.ariaDark || 'Switch to dark theme'));
    toggle.querySelector('[data-theme-icon]').textContent = dark ? '☼' : '◐';
    toggle.querySelector('[data-theme-label]').textContent = dark ? (d.labelLight || 'Light mode') : (d.labelDark || 'Dark mode');
  }

  function setTheme(theme, persist) {
    root.dataset.theme = theme;
    updateToggle(theme);
    if (persist) try { window.localStorage.setItem('justybase-theme', theme); } catch (e) {};
  }

  setTheme(initialTheme, false);
  if (toggle) {
    toggle.addEventListener('click', function toggleTheme() {
      setTheme(root.dataset.theme === 'dark' ? 'light' : 'dark', true);
    });
  }
})();
