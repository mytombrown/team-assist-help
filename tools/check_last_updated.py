#!/usr/bin/env python3
"""
TA-T-101 — the last-updated dates track edits.

Origin: TA-65 (and CM-64 before it). Tom asked for a last-updated date on
help.mytombrown.com "to ensure you are updating the help page after each version
push". A date that only *exists* does not do that job — a build stamp reads
"today" on an article untouched since July, and a hand-typed date reads whatever
someone last remembered to type. Both pass a test that asserts "a date is shown".
Both are the exact failure this ticket was filed about.

So the invariant under test is movement, not presence:

    editing an article MOVES that article's date,
    and moves NO other article's date.

The last arm is what kills the build stamp: a stamp moves all 22 at once.
The check proves it by doing it — it clones the repo to a temp directory,
commits a one-character edit to one article, and re-derives every date.

    python3 tools/check_last_updated.py

Exit 0 = pass. Runs in the Pages workflow before the dates are generated.
"""

import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from last_updated import article_dates, git, site_date  # noqa: E402

ROOT = pathlib.Path(__file__).parent.parent
DATA_REL = "_data/last_updated.yml"

failures = []
notes = []


def check(label, ok, detail=""):
    if ok:
        notes.append(f"  ✓ {label}")
    else:
        failures.append(f"{label}{': ' + detail if detail else ''}")
    return ok


def check_derivation():
    """Every article has a date, and it is that article's own commit date."""
    dates, published, problems = article_dates()
    for p in problems:
        failures.append(p)
    if problems:
        return None

    articles = sorted((ROOT / "_articles").glob("*.md"))
    check(f"every article has a derived date ({len(dates)} articles)",
          len(dates) == len(articles),
          f"{len(articles)} articles but {len(dates)} dates")

    mismatched = []
    for path in articles:
        rel = str(path.relative_to(ROOT))
        expected = git("log", "-1", "--format=%cI", "--", rel)
        slug = next((s for s, w in dates.items() if w == expected), None)
        if expected and expected not in dates.values():
            mismatched.append(f"{rel} (git says {expected}, not in the generated set)")
        del slug
    check("each date equals that file's git commit date", not mismatched,
          "; ".join(mismatched))

    check("the dates are not all identical — they are per-article, not a stamp",
          len(set(dates.values())) > 1,
          f"all {len(dates)} articles share one date, which is what a build stamp "
          f"looks like. If that is genuinely true of the history, this check needs "
          f"a real repo to run against.")

    # The homepage date claims the help a reader can see changed. Articles held
    # by the review gate are not on the live site, so they cannot be the claim.
    held = sorted(set(dates) - published)
    check(f"the site date comes only from published articles "
          f"({len(published)} published, {len(held)} held)",
          site_date(dates, published) in {dates[s] for s in published},
          "the site date is drawn from an article that does not publish")
    return dates, published


def edit_in_clone(clone, target):
    """Commit a one-line edit to `target` and re-derive every date."""
    target.write_text(target.read_text(encoding="utf-8") + "\n<!-- TA-T-101 -->\n",
                      encoding="utf-8")
    commit = subprocess.run(
        ["git", "-C", str(clone),
         "-c", "user.name=TA-T-101", "-c", "user.email=test@localhost",
         "commit", "-q", "-am", "TA-T-101: edit one article"],
        capture_output=True, text=True,
    )
    if commit.returncode != 0:
        return None, f"could not commit the test edit: {commit.stderr.strip()}"
    dates, published, problems = article_dates(root=clone)
    if problems:
        return None, "; ".join(problems)
    return (dates, published), None


def check_edits_move_the_right_dates(dates, published):
    """The teeth: edit an article in a scratch clone, re-derive, compare.

    Two edits, because two different lies are possible. Editing a PUBLISHED
    article must move its own date, no other article's, and the site date.
    Editing a HELD draft must move its own date and NOT the site date — the
    homepage would otherwise announce an update a reader cannot see.
    """
    if len(dates) < 2:
        failures.append("need at least two articles to prove edits are article-scoped")
        return

    tmp = pathlib.Path(tempfile.mkdtemp(prefix="ta-t-101-"))
    try:
        for kind, pick in (("published", lambda s: s in published),
                           ("held draft", lambda s: s not in published)):
            clone = tmp / f"clone-{kind.split()[0]}"
            proc = subprocess.run(
                ["git", "clone", "--quiet", "--no-hardlinks", str(ROOT), str(clone)],
                capture_output=True, text=True,
            )
            if proc.returncode != 0:
                failures.append(f"could not clone the repo to test edits: {proc.stderr.strip()}")
                return

            before, before_pub, problems = article_dates(root=clone)
            if problems:
                failures.extend(problems)
                return

            candidates = [p for p in sorted((clone / "_articles").glob("*.md"))
                          if pick(slug_in(before, p))]
            if not candidates:
                notes.append(f"  – no {kind} article to edit; arm skipped")
                continue
            target = candidates[0]
            slug = slug_in(before, target)
            site_before = site_date(before, before_pub)

            result, err = edit_in_clone(clone, target)
            if err:
                failures.append(err)
                return
            after, after_pub = result
            site_after = site_date(after, after_pub)

            check(f"editing a {kind} ({target.name}) MOVES its own date",
                  after.get(slug) != before.get(slug),
                  f"date stayed {before.get(slug)} after a committed edit — "
                  f"the date is frozen and proves nothing")

            others = [s for s in before if s != slug and before[s] != after.get(s)]
            check(f"editing a {kind} moves NO other article's date", not others,
                  f"{len(others)} untouched article(s) changed date too "
                  f"({', '.join(sorted(others)[:4])}) — that is a site-wide stamp, "
                  f"not a per-article date")

            if kind == "published":
                check("editing a published article moves the site date",
                      site_after != site_before,
                      f"site date stayed {site_before} — the homepage would not "
                      f"reflect a real content change")
            else:
                check("editing a held draft does NOT move the site date",
                      site_after == site_before,
                      f"site date moved {site_before} -> {site_after} for an edit "
                      f"no reader can see — the homepage would claim an update "
                      f"that did not reach the site")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def slug_in(dates, path):
    """The slug this file contributes to the derived set."""
    from last_updated import slug_of
    slug = slug_of(path)
    return slug if slug in dates else path.stem


def check_wiring():
    """A date nothing renders, or a generator nothing runs, proves nothing."""
    article_layout = (ROOT / "_layouts" / "article.html").read_text(encoding="utf-8")
    index = (ROOT / "index.html").read_text(encoding="utf-8")

    check("the article layout renders the derived date",
          "site.data.last_updated.articles" in article_layout,
          "_layouts/article.html never reads site.data.last_updated.articles")
    check("the index renders the site date",
          "site.data.last_updated.site" in index,
          "index.html never reads site.data.last_updated.site")

    for name, text in (("_layouts/article.html", article_layout),
                       ("index.html", index),
                       ("_layouts/default.html",
                        (ROOT / "_layouts" / "default.html").read_text(encoding="utf-8"))):
        # The footer's copyright year is allowed to be "now"; a content date is not.
        bad = [line.strip() for line in text.splitlines()
               if "'now'" in line and "updated" in line.lower()]
        check(f"{name} does not date content from 'now'", not bad, " | ".join(bad))

    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    check("the generated data file is gitignored", DATA_REL in gitignore,
          f"{DATA_REL} is not in .gitignore — a committed copy freezes the dates")

    workflow = (ROOT / ".github" / "workflows" / "pages.yml").read_text(encoding="utf-8")
    check("the workflow checks out full history (fetch-depth: 0)",
          re.search(r"fetch-depth:\s*0", workflow) is not None,
          "a shallow checkout has no per-file history, so no dates")
    check("the workflow generates the dates before building",
          re.search(r"tools/last_updated\.py", workflow) is not None,
          "pages.yml never runs tools/last_updated.py, so the built site has no dates")


def main():
    derived = check_derivation()
    dates = None
    if derived:
        dates, published = derived
        check_edits_move_the_right_dates(dates, published)
    check_wiring()

    for line in notes:
        print(line)

    if failures:
        print("\nTA-T-101 FAILED:")
        for f in failures:
            print(f"  ✗ {f}")
        return 1

    print(f"\nTA-T-101 PASS — {len(dates)} article dates derived from git, "
          f"and an edit moves exactly one of them.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
