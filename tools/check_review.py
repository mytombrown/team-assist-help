#!/usr/bin/env python3
"""
Publish gate.

Refuses to let unverified content reach the live site. Exits non-zero if any
article still carries `needs_review: true`, and reports what each is waiting on.

    python3 tools/check_review.py            # report status, fail if drafts remain
    python3 tools/check_review.py --report    # report only, always exit 0

A flag in front matter is easy to forget; a build that refuses to publish is not.
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent.parent
ARTICLES = ROOT / "_articles"


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else ""


def field(fm, name):
    m = re.search(rf"^{name}:\s*(.*)$", fm, re.M)
    return m.group(1).strip().strip('"') if m else None


def main():
    report_only = "--report" in sys.argv

    if not ARTICLES.is_dir():
        print(f"error: {ARTICLES} not found", file=sys.stderr)
        return 1

    files = sorted(ARTICLES.glob("*.md"))
    if not files:
        print("error: no articles found", file=sys.stderr)
        return 1

    config = (ROOT / "_config.yml").read_text(encoding="utf-8")
    known = set(re.findall(r"^\s*-\s*id:\s*(\S+)", config, re.M))

    drafts, ready, problems = [], [], []

    for f in files:
        text = f.read_text(encoding="utf-8")
        fm = front_matter(text)
        if not fm:
            problems.append(f"{f.name}: no front matter")
            continue

        for required in ("title", "category", "quick"):
            if not field(fm, required):
                problems.append(f"{f.name}: missing `{required}`")

        cat = field(fm, "category")
        if cat and cat not in known:
            problems.append(
                f"{f.name}: category `{cat}` is not declared in _config.yml, "
                f"so this article will not appear on the index"
            )

        if field(fm, "needs_review") == "true":
            drafts.append((f.name, field(fm, "review_note") or ""))
        else:
            ready.append(f.name)

    print(f"{len(ready)} ready, {len(drafts)} awaiting review, {len(files)} total\n")

    if ready:
        print("Verified and publishable:")
        for name in ready:
            print(f"  ✓ {name}")
        print()

    if drafts:
        print("Awaiting verification:")
        for name, note in drafts:
            print(f"  • {name}")
            if note:
                print(f"      {note if len(note) <= 96 else note[:93] + '...'}")
        print()

    if problems:
        print("Problems:")
        for p in problems:
            print(f"  ✗ {p}")
        print()
        return 1

    if drafts:
        if report_only:
            print(
                f"{len(drafts)} article(s) still unverified — the site will NOT deploy\n"
                "until these are cleared. Verify each against the app, then remove\n"
                "`needs_review: true` and its `review_note` from that file."
            )
            return 0
        print(
            "Not safe to publish. Verify each article above against the app, then\n"
            "remove `needs_review: true` and its `review_note` from that file.\n"
            "Run with --report to see status without failing."
        )
        return 1

    print("All articles verified — safe to publish.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
