(function projectFilter() {
  const buttons = Array.from(document.querySelectorAll('[data-filter]'));
  const cards = Array.from(document.querySelectorAll('[data-category]'));
  if (!buttons.length) return;
  buttons.forEach(function (button) {
    button.addEventListener('click', function () {
      const value = button.dataset.filter;
      buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(b === button)); });
      cards.forEach(function (card) { card.hidden = value !== 'all' && card.dataset.category !== value; });
    });
  });
})();
