// Shared behaviour for Gloss pages: injects header + footer so every page stays consistent.
(function () {
  var APP = 'https://apps.apple.com/us/app/gloss-ai-skin-analysis/id6792349354';
  var root = document.body.getAttribute('data-root') || './';
  var logo = '<svg viewBox="0 0 200 200" aria-hidden="true"><defs><linearGradient id="gl" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e8709f"/><stop offset="1" stop-color="#c2417a"/></linearGradient></defs><circle cx="100" cy="100" r="70" fill="none" stroke="#fbe6ee" stroke-width="24"/><path d="M100 30 A70 70 0 1 1 46.9 63.5" fill="none" stroke="url(#gl)" stroke-width="24" stroke-linecap="round"/><circle cx="46.9" cy="63.5" r="12" fill="#f0c29a"/></svg>';
  var header = document.createElement('header');
  header.className = 'site-header';
  header.innerHTML = '<div class="wrap wide">' +
    '<a class="brand" href="' + root + '">' + logo + 'Gloss</a>' +
    '<nav class="nav">' +
      '<a href="' + root + 'tools/">Free tools</a>' +
      '<a class="hide-sm" href="' + root + 'support.html">Support</a>' +
      '<a class="btn small" href="' + APP + '" rel="noopener">Get the app</a>' +
    '</nav></div>';
  document.body.insertBefore(header, document.body.firstChild);

  var footer = document.createElement('footer');
  footer.className = 'site-footer';
  footer.innerHTML = '<div class="wrap wide">' +
    '<div>Gloss · AI skin analysis for iPhone. Cosmetic tracking only, not medical advice.</div>' +
    '<div class="links">' +
      '<a href="' + root + 'tools/">Free tools</a>' +
      '<a href="' + root + 'support.html">Support</a>' +
      '<a href="' + root + 'privacy-policy.html">Privacy</a>' +
      '<a href="' + root + 'terms.html">Terms</a>' +
      '<a href="' + APP + '" rel="noopener">App Store</a>' +
    '</div></div>';
  document.body.appendChild(footer);

  // Any element with data-app-link becomes the App Store URL.
  document.querySelectorAll('[data-app-link]').forEach(function (a) { a.href = APP; a.rel = 'noopener'; });
})();
