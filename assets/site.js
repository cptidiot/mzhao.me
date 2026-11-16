// Site-wide theme toggle. The stored choice wins; with none, the page follows the system.
(function () {
  var KEY = 'theme';
  function stored() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function current() {
    var s = document.documentElement.getAttribute('data-theme');
    if (s) return s;
    return window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  var saved = stored();
  if (saved === 'dark' || saved === 'light') document.documentElement.setAttribute('data-theme', saved);
  document.addEventListener('click', function (e) {
    var btn = e.target.closest && e.target.closest('[data-theme-toggle]');
    if (!btn) return;
    var next = current() === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    try { localStorage.setItem(KEY, next); } catch (err) {}
  });
})();
