/* Client-side search over search.json.
   No dependencies, no build step, no network calls beyond the index itself. */
(function () {
  "use strict";

  var q = document.getElementById("q");
  var results = document.getElementById("results");
  var browse = document.getElementById("browse");
  if (!q || !results || !browse) return;

  var INDEX = null, pending = null, timer = null;

  var esc = function (s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  };

  function load() {
    if (INDEX) return Promise.resolve(INDEX);
    if (pending) return pending;
    var base = document.body.getAttribute("data-baseurl") || "";
    pending = fetch(base + "/search.json")
      .then(function (r) { return r.json(); })
      .then(function (data) {
        INDEX = data.map(function (a) {
          a._hay = (a.title + " " + (a.tags || "") + " " + a.quick + " " + a.body + " " + (a.categoryTitle || "")).toLowerCase();
          return a;
        });
        return INDEX;
      })
      .catch(function () { INDEX = []; return INDEX; });
    return pending;
  }

  function highlight(text, terms) {
    var out = esc(text);
    terms.forEach(function (t) {
      if (t.length < 2) return;
      out = out.replace(new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig"), "<mark>$1</mark>");
    });
    return out;
  }

  var wordRe = {};
  function word(t) {
    // Whole-word matcher, cached. Without this, searching "age" matches
    // "package" and "manage" and ranks the wrong article first.
    if (!wordRe[t]) {
      wordRe[t] = new RegExp("\\b" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "i");
    }
    return wordRe[t];
  }

  function score(a, terms) {
    var s = 0;
    var title = a.title.toLowerCase();
    var tags = (a.tags || "").toLowerCase();
    var quick = a.quick.toLowerCase();

    for (var i = 0; i < terms.length; i++) {
      var t = terms[i];
      if (a._hay.indexOf(t) === -1) return 0;   // every term must appear somewhere
      var w = word(t);

      // Whole-word hits score far above incidental substring hits.
      if (w.test(title)) s += 30;
      else if (title.indexOf(t) !== -1) s += 6;

      if (w.test(tags)) s += 18;
      else if (tags.indexOf(t) !== -1) s += 3;

      if (w.test(quick)) s += 10;
      else if (quick.indexOf(t) !== -1) s += 2;

      if (w.test(a._hay)) s += 4;   // whole word anywhere at all
      s += 1;
    }

    if (title.indexOf(terms.join(" ")) !== -1) s += 40;   // exact phrase in title
    return s;
  }

  function render(raw) {
    var terms = raw.toLowerCase().split(/\s+/).filter(Boolean);
    var hits = INDEX
      .map(function (a) { return { a: a, s: score(a, terms) }; })
      .filter(function (h) { return h.s > 0; })
      .sort(function (x, y) { return y.s - x.s; });

    if (!hits.length) {
      var email = results.getAttribute("data-email") || "";
      results.innerHTML =
        '<div class="empty"><strong>No results for &ldquo;' + esc(raw) + '&rdquo;</strong>' +
        '<p>Try a different word, or email <a href="mailto:' + email + '">' + email + "</a>.</p></div>";
      return;
    }

    results.innerHTML =
      '<p class="res-count">' + hits.length + " result" + (hits.length > 1 ? "s" : "") + "</p>" +
      hits.map(function (h) {
        return '<a class="res" href="' + h.a.url + '">' +
          '<span class="crumb">' + esc(h.a.categoryTitle || "") + "</span>" +
          '<span class="t">' + highlight(h.a.title, terms) +
          (h.a.draft ? ' <span class="flag">draft</span>' : "") + "</span>" +
          '<span class="s">' + highlight(h.a.quick, terms) + "</span></a>";
      }).join("");
  }

  function run() {
    var raw = q.value.trim();
    if (!raw) {
      results.hidden = true;
      browse.hidden = false;
      results.innerHTML = "";
      return;
    }
    load().then(function () {
      results.hidden = false;
      browse.hidden = true;
      render(raw);
    });
  }

  q.addEventListener("input", function () {
    clearTimeout(timer);
    timer = setTimeout(run, 90);
  });
  q.addEventListener("focus", load);

  document.addEventListener("keydown", function (e) {
    var typing = /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName);
    if (e.key === "/" && !typing) { e.preventDefault(); q.focus(); q.select(); }
    else if (e.key === "Escape" && document.activeElement === q) {
      q.value = ""; run(); q.blur();
    } else if (e.key === "Enter" && document.activeElement === q) {
      var first = results.querySelector(".res");
      if (first) { e.preventDefault(); window.location = first.getAttribute("href"); }
    }
  });

  // Open the right category if someone arrives at /#chat from a breadcrumb.
  if (location.hash.length > 1) {
    var sec = document.getElementById(location.hash.slice(1));
    if (sec) {
      Array.prototype.forEach.call(sec.querySelectorAll("details.qa"), function (d) { d.open = true; });
    }
  }
})();
