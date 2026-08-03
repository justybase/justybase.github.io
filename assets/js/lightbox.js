(function () {
  const figures = Array.from(document.querySelectorAll('.screenshot'));
  if (!figures.length) return;

  const overlay = document.createElement('div');
  overlay.className = 'lightbox';
  overlay.setAttribute('role', 'dialog');
  overlay.setAttribute('aria-modal', 'true');
  overlay.setAttribute('aria-label', 'Screenshot preview');
  overlay.innerHTML =
    '<button class="lightbox-close" type="button" aria-label="Close preview">×</button>' +
    '<button class="lightbox-nav lightbox-nav-prev" type="button" aria-label="Previous screenshot">←</button>' +
    '<button class="lightbox-nav lightbox-nav-next" type="button" aria-label="Next screenshot">→</button>' +
    '<div class="lightbox-stage"><img src="" alt=""></div>' +
    '<p class="lightbox-caption"></p>';
  document.body.appendChild(overlay);

  const imgEl = overlay.querySelector('.lightbox-stage img');
  const captionEl = overlay.querySelector('.lightbox-caption');
  const closeBtn = overlay.querySelector('.lightbox-close');
  const prevBtn = overlay.querySelector('.lightbox-nav-prev');
  const nextBtn = overlay.querySelector('.lightbox-nav-next');

  let current = -1;

  function open(index) {
    current = index;
    const img = figures[index].querySelector('img');
    imgEl.src = img.currentSrc || img.src;
    imgEl.alt = img.alt;
    const caption = figures[index].querySelector('figcaption');
    captionEl.textContent = caption ? caption.textContent : '';
    overlay.classList.add('is-open');
    document.body.classList.add('has-lightbox');
    closeBtn.focus();
  }

  function close() {
    overlay.classList.remove('is-open');
    document.body.classList.remove('has-lightbox');
    current = -1;
    imgEl.removeAttribute('src');
  }

  function step(delta) {
    if (figures.length < 2) return;
    open((current + delta + figures.length) % figures.length);
  }

  figures.forEach(function (figure, index) {
    const img = figure.querySelector('img');
    if (!img) return;
    img.tabIndex = 0;
    img.setAttribute('role', 'button');
    img.setAttribute('aria-haspopup', 'dialog');
    img.addEventListener('click', function () { open(index); });
    img.addEventListener('keydown', function (event) {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        open(index);
      }
    });
  });

  closeBtn.addEventListener('click', close);
  prevBtn.addEventListener('click', function () { step(-1); });
  nextBtn.addEventListener('click', function () { step(1); });
  overlay.addEventListener('click', function (event) {
    if (event.target === overlay) close();
  });
  document.addEventListener('keydown', function (event) {
    if (!overlay.classList.contains('is-open')) return;
    if (event.key === 'Escape') close();
    else if (event.key === 'ArrowLeft') step(-1);
    else if (event.key === 'ArrowRight') step(1);
  });
})();
