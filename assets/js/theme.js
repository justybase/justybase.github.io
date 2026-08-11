(function applyThemePreference() {
  const root = document.documentElement;
  const toggle = document.querySelector('[data-theme-toggle]');
  const storedTheme = window.localStorage.getItem('justybase-theme');
  const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  const initialTheme = storedTheme === 'dark' || storedTheme === 'light' ? storedTheme : systemTheme;

  function updateToggle(theme) {
    if (!toggle) return;
    const dark = theme === 'dark';
    toggle.setAttribute('aria-pressed', String(dark));
    toggle.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
    toggle.querySelector('[data-theme-icon]').textContent = dark ? '☼' : '◐';
    toggle.querySelector('[data-theme-label]').textContent = dark ? 'Light mode' : 'Dark mode';
  }

  function setTheme(theme, persist) {
    root.dataset.theme = theme;
    updateToggle(theme);
    if (persist) window.localStorage.setItem('justybase-theme', theme);
  }

  setTheme(initialTheme, false);
  if (toggle) {
    toggle.addEventListener('click', function toggleTheme() {
      setTheme(root.dataset.theme === 'dark' ? 'light' : 'dark', true);
    });
  }
})();
