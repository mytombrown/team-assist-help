#!/usr/bin/env python3
"""
Anchor gate (TA-569).

Search results link to the H2 section that answers the question, not the top
of the article (search.json emits one entry per H2, keyed by the id kramdown
generates). That only works if every H2 GETS an id and no two H2s in one
article collide. kramdown's auto_ids derives the id from the heading text:
lowercase, drop everything that is not a letter, digit, space or hyphen, turn
spaces into hyphens, strip leading digits and hyphens. A heading made only of
punctuation or digits gets the id "section", and a duplicate gets "-1"
appended — both are links nobody wrote and nobody will maintain.

    python3 tools/check_anchors.py

Exit 0 = every H2 in every article has a unique, non-generic id.
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent.parent
ARTICLES = ROOT / "_articles"


def kramdown_id(text):
    # Mirrors kramdown's generate_id: strip inline markup, downcase, keep
    # [a-z0-9 -], spaces to hyphens, then drop leading non-letters.
    t = re.sub(r"[*_`\[\]]", "", text)
    t = re.sub(r"\([^)]*\)", "", t)          # link targets
    t = t.lower()
    t = re.sub(r"[^a-z0-9 -]", "", t)
    t = t.strip().replace(" ", "-")
    t = re.sub(r"^[^a-z]+", "", t)
    return t or "section"


def main():
    problems = []
    checked = 0
    for f in sorted(ARTICLES.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)
        seen = {}
        for m in re.finditer(r"^##\s+(.+?)\s*#*\s*$", body, re.M):
            heading = m.group(1)
            checked += 1
            explicit = re.search(r"\{#([^}]+)\}\s*$", heading)
            hid = explicit.group(1) if explicit else kramdown_id(heading)
            if hid == "section":
                problems.append(f"{f.name}: H2 '{heading}' produces no usable anchor")
            elif hid in seen:
                problems.append(
                    f"{f.name}: H2 '{heading}' collides with '{seen[hid]}' on #{hid}"
                )
            seen[hid] = heading
    if problems:
        print("Problems:")
        for p in problems:
            print(f"  ✗ {p}")
        return 1
    print(f"ok: {checked} H2 headings, every one anchored and unique within its article")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
