/* VALAR — main.js · Scripts compartilhados */

// Fade-in de seções via IntersectionObserver
(function () {
  if (!('IntersectionObserver' in window)) {
    document.querySelectorAll('section').forEach(function (s) {
      s.classList.add('is-visible');
    });
    return;
  }
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });

  document.querySelectorAll('section').forEach(function (s) {
    if (s.id !== 'hero') {
      observer.observe(s);
    } else {
      s.classList.add('is-visible');
    }
  });
}());

// Menu mobile hambúrguer (com ESC, scroll-lock e backdrop)
(function () {
  var btn = document.querySelector('.nav__hamburger');
  var menu = document.getElementById('mobile-menu');
  if (!btn || !menu) return;

  // Criar backdrop dinamicamente
  var backdrop = document.createElement('div');
  backdrop.className = 'nav__backdrop';
  backdrop.setAttribute('aria-hidden', 'true');
  document.querySelector('.nav').appendChild(backdrop);

  function openMenu() {
    btn.setAttribute('aria-expanded', 'true');
    btn.setAttribute('aria-label', 'Fechar menu de navegação');
    menu.hidden = false;
    menu.classList.add('is-open');
    backdrop.classList.add('is-active');
    document.body.classList.add('nav-open');
  }

  function closeMenu() {
    btn.setAttribute('aria-expanded', 'false');
    btn.setAttribute('aria-label', 'Abrir menu de navegação');
    menu.hidden = true;
    menu.classList.remove('is-open');
    backdrop.classList.remove('is-active');
    document.body.classList.remove('nav-open');
  }

  btn.addEventListener('click', function () {
    if (btn.getAttribute('aria-expanded') === 'true') {
      closeMenu();
    } else {
      openMenu();
    }
  });

  // Fechar ao clicar em link interno
  menu.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      closeMenu();
    });
  });

  // Fechar ao clicar no backdrop
  backdrop.addEventListener('click', function () {
    closeMenu();
  });

  // Fechar com tecla ESC
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && btn.getAttribute('aria-expanded') === 'true') {
      closeMenu();
      btn.focus();
    }
  });
}());
