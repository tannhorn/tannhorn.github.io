(function () {
  "use strict";

  var navs = document.querySelectorAll("[data-section-nav]");
  if (!navs.length) return;

  navs.forEach(function (nav) {
    var narrowViewport = window.matchMedia("(max-width: 720px)");
    var links = Array.prototype.slice.call(nav.querySelectorAll('.section-nav__list a[href^="#"]'));
    var sections = links
      .map(function (link) {
        return document.getElementById(link.getAttribute("href").slice(1));
      })
      .filter(Boolean);

    function setCurrent(id) {
      links.forEach(function (link) {
        var current = link.getAttribute("href") === "#" + id;
        link.classList.toggle("is-current", current);
        if (current) {
          link.setAttribute("aria-current", "location");
        } else {
          link.removeAttribute("aria-current");
        }
      });
    }

    function setCurrentFromHash() {
      var id = window.location.hash.slice(1);
      if (id && document.getElementById(id)) setCurrent(id);
    }

    setCurrentFromHash();
    window.addEventListener("hashchange", setCurrentFromHash);

    function updateDisclosure() {
      nav.open = !narrowViewport.matches;
    }

    updateDisclosure();
    if (narrowViewport.addEventListener) {
      narrowViewport.addEventListener("change", updateDisclosure);
    } else {
      narrowViewport.addListener(updateDisclosure);
    }

    links.forEach(function (link) {
      link.addEventListener("click", function () {
        if (narrowViewport.matches) nav.open = false;
      });
    });

    if (!("IntersectionObserver" in window)) return;

    var observer = new IntersectionObserver(
      function (entries) {
        var visible = entries
          .filter(function (entry) { return entry.isIntersecting; })
          .sort(function (a, b) { return a.boundingClientRect.top - b.boundingClientRect.top; });
        if (visible.length) setCurrent(visible[0].target.id);
      },
      { rootMargin: "-18% 0px -70%", threshold: 0 }
    );

    sections.forEach(function (section) { observer.observe(section); });
  });
})();
