#!/usr/bin/env python3
"""
Ruby-free local preview.

Renders the site to _preview/ so you can look at it without installing Jekyll.
It reimplements the layouts closely enough to check design, content and search,
but it is NOT Jekyll — GitHub Actions runs the real build. If the two disagree,
the Jekyll output is the truth.

    pip install markdown
    python3 tools/preview.py
    python3 -m http.server -d _preview 8000
"""

import html
import json
import pathlib
import re
import shutil
import sys

try:
    import markdown as md
except ImportError:
    sys.exit("needs the markdown package:  pip install markdown")

ROOT = pathlib.Path(__file__).parent.parent
OUT = ROOT / "_preview"
MD = md.Markdown(extensions=["extra", "sane_lists"])


def render_md(text):
    MD.reset()
    return MD.convert(text)


def load_config():
    raw = (ROOT / "_config.yml").read_text(encoding="utf-8")
    cfg = {
        "title": re.search(r"^title:\s*(.+)$", raw, re.M).group(1).strip(),
        "support_email": re.search(r'^support_email:\s*"?([^"\n]+)', raw, re.M).group(1).strip(),
        "beta_notice": "", "legal": {}, "categories": [],
    }
    m = re.search(r'^beta_notice:\s*"?([^"\n]+)', raw, re.M)
    if m and m.group(1).strip() != "false":
        cfg["beta_notice"] = m.group(1).strip()
    for key in ("privacy", "delete_account"):
        mm = re.search(rf'^\s+{key}:\s*"([^"]+)"', raw, re.M)
        if mm:
            cfg["legal"][key] = mm.group(1)
    block = re.search(r"^categories:\n((?:\s+-.*\n(?:\s+\w+:.*\n)*)+)", raw, re.M)
    if block:
        for c in re.findall(r"-\s*id:\s*(\S+)\n\s*title:\s*(.+)\n(?:\s*blurb:\s*(.+)\n)?",
                            block.group(1)):
            cfg["categories"].append({"id": c[0], "title": c[1].strip(),
                                      "blurb": (c[2] or "").strip()})
    return cfg


def parse_article(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return None
    fm_raw, body = m.group(1), m.group(2)

    def f(name, default=""):
        mm = re.search(rf"^{name}:\s*(.*)$", fm_raw, re.M)
        return mm.group(1).strip().strip('"') if mm else default

    return {
        "slug": f("slug", path.stem), "title": f("title"), "category": f("category"),
        "order": int(f("order", "99") or 99), "tags": f("tags"), "quick": f("quick"),
        "needs_review": f("needs_review") == "true", "review_note": f("review_note"),
        "related": re.findall(r"^\s+-\s*(\S+)\s*$", fm_raw, re.M),
        "body": body.strip(), "url": f"/{f('slug', path.stem)}/",
    }


def expand(text, cfg):
    text = text.replace("{{ site.support_email }}", cfg["support_email"])
    text = text.replace("{{ site.legal.privacy }}", cfg["legal"].get("privacy", "#"))
    text = text.replace("{{ site.legal.delete_account }}", cfg["legal"].get("delete_account", "#"))
    return re.sub(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}", r"\1", text)


def page(cfg, title, inner, is_home=False):
    beta = (f'<div class="beta"><div class="wrap"><b>Note</b> '
            f'{html.escape(cfg["beta_notice"])}</div></div>') if cfg["beta_notice"] else ""
    full = cfg["title"] if is_home else f'{title} — {cfg["title"]}'
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(full)}</title>
<link rel="stylesheet" href="/assets/css/style.css"></head>
<body data-baseurl="">
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap site-head">
<a class="brand" href="/"><img src="/assets/team-assist-icon.png" alt="" width="40" height="40">
<span>Team Assist <b>Help</b></span></a>
<nav class="site-nav"><a href="/">Help</a>
<a href="{cfg['legal'].get('privacy','#')}">Privacy</a>
<a href="{cfg['legal'].get('delete_account','#')}">Delete account</a></nav>
</div></header>
{beta}
<main id="main" class="wrap">{inner}</main>
<footer class="site"><div class="wrap">
<p>&copy; 2026 Thomas M Brown. Team Assist.</p>
<p><a href="/">Help</a><a href="{cfg['legal'].get('privacy','#')}">Privacy policy</a>
<a href="{cfg['legal'].get('delete_account','#')}">Delete account</a>
<a href="mailto:{cfg['support_email']}">{cfg['support_email']}</a></p>
</div></footer></body></html>
"""


def main():
    cfg = load_config()
    arts = [a for a in (parse_article(p) for p in sorted((ROOT / "_articles").glob("*.md"))) if a]
    by_slug = {a["slug"]: a for a in arts}

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "assets", OUT / "assets")

    parts = ['<div class="hero"><h1>How can we help?</h1>',
             "<p>Find a quick answer, or open an article to read the whole thing.</p>",
             '<div class="searchwrap">',
             '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
             'stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>',
             '<input id="q" type="search" placeholder="Search help…" autocomplete="off" '
             'aria-label="Search help articles"><span class="kbd">/</span></div></div>',
             f'<div id="results" hidden data-email="{cfg["support_email"]}"></div>',
             '<div id="browse">']

    for cat in cfg["categories"]:
        items = sorted([a for a in arts if a["category"] == cat["id"]], key=lambda a: a["order"])
        if not items:
            continue
        parts.append(f'<section class="cat" id="{cat["id"]}"><div class="cat-head">'
                     f'<h2>{html.escape(cat["title"])}</h2>'
                     f'<span>{html.escape(cat["blurb"])}</span></div>')
        for a in items:
            flag = '<span class="flag">draft</span>' if a["needs_review"] else ""
            parts.append(
                '<details class="qa"><summary>'
                '<svg class="caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">'
                '<path d="M9 5l7 7-7 7"/></svg>'
                f'<span>{html.escape(a["title"])}</span>{flag}</summary>'
                '<div class="qa-body"><div class="quick"><span class="quick-tag">Quick answer</span>'
                f'{render_md(expand(a["quick"], cfg))}</div>'
                f'<p class="more"><a href="{a["url"]}">Read the full answer →</a></p>'
                "</div></details>")
        parts.append("</section>")
    parts.append('</div><script src="/assets/js/search.js" defer></script>')

    (OUT / "index.html").write_text(page(cfg, "Help", "".join(parts), is_home=True),
                                    encoding="utf-8")

    cat_title = {c["id"]: c["title"] for c in cfg["categories"]}
    for a in arts:
        review = ""
        if a["needs_review"]:
            note = (f'<span class="review-note">{html.escape(a["review_note"])}</span>'
                    if a["review_note"] else "")
            review = ('<div class="review"><b>Not yet verified.</b> This article was drafted '
                      "from a feature list rather than from the app itself. Everything below "
                      "needs checking against what Team Assist actually does before it is "
                      f"treated as accurate. {note}</div>")
        rel = ""
        if a["related"]:
            links = "".join(
                f'<li><a href="{by_slug[s]["url"]}">{html.escape(by_slug[s]["title"])}</a></li>'
                for s in a["related"] if s in by_slug)
            if links:
                rel = f'<aside class="related"><h2>Related</h2><ul>{links}</ul></aside>'

        inner = (
            f'<nav class="crumbs"><a href="/">Help</a><span>›</span>'
            f'<a href="/#{a["category"]}">{html.escape(cat_title.get(a["category"], a["category"]))}</a></nav>'
            f'<article class="article"><h1>{html.escape(a["title"])}</h1>{review}'
            f'<div class="quick"><span class="quick-tag">Quick answer</span>'
            f'{render_md(expand(a["quick"], cfg))}</div>'
            f'<div class="detail">{render_md(expand(a["body"], cfg))}</div>{rel}'
            f'<aside class="stuck"><p>Still stuck? Email '
            f'<a href="mailto:{cfg["support_email"]}">{cfg["support_email"]}</a>. '
            "Including your iPhone model, iOS version and what you were doing usually turns a "
            "three-message exchange into one.</p></aside></article>")
        d = OUT / a["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(page(cfg, a["title"], inner), encoding="utf-8")

    index = [{"title": a["title"], "url": a["url"], "category": a["category"],
              "categoryTitle": cat_title.get(a["category"], ""), "quick": a["quick"],
              "tags": a["tags"],
              "body": re.sub(r"<[^>]+>", " ", render_md(expand(a["body"], cfg)))[:4000],
              "draft": a["needs_review"]} for a in arts]
    (OUT / "search.json").write_text(json.dumps(index, indent=1), encoding="utf-8")

    print(f"preview built: {OUT}  ({len(arts)} articles)")


if __name__ == "__main__":
    main()
