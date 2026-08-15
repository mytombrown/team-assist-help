#!/usr/bin/env python3
"""
Red proof for TA-T-101 — evidence the check can actually fail.

TA-65 asked for a date that shows whether the help was updated after a version
push. The ways to get that wrong all *look* right on the page, and all pass a
test that merely asserts "a date is present":

  1. a site-wide build stamp — every article reads today
  2. a frozen date — nothing moves, ever
  3. a site date counting held drafts — the homepage announces an update to
     content the review gate is still holding back, so no reader can see it

This sabotages the generator each way in a throwaway clone and asserts
tools/check_last_updated.py goes RED. If any sabotage comes back green, the
test has stopped guarding the invariant and TA-65 has quietly regressed.

    python3 tools/_ta_t_101_red_proof.py

Kept out of the built site by `exclude: tools/` in _config.yml.
"""

import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).parent.parent
DERIVE = 'when = git("log", "-1", "--format=%cI", "--", rel, root=root)'
SITE_DATE = "return max(when for slug, when in dates.items() if slug in published)"

SABOTAGES = [
    ("site-wide build stamp", DERIVE,
     'when = git("log", "-1", "--format=%cI", root=root)',
     "moves NO other article's date"),
    ("frozen date", DERIVE,
     'when = "2026-08-01T00:00:00-05:00"',
     "MOVES its own date"),
    ("site date counts held drafts", SITE_DATE,
     "return max(dates.values())",
     "editing a held draft does NOT move the site date"),
]


def run_sabotage(label, original, replacement, must_mention):
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="ta-t-101-redproof-"))
    try:
        dest = tmp / "help"
        subprocess.run(["git", "clone", "--quiet", "--no-hardlinks", str(ROOT), str(dest)],
                       check=True, capture_output=True)
        # carry the working tree's version of everything the check reads
        for rel in ("tools/last_updated.py", "tools/check_last_updated.py",
                    "_layouts/article.html", "_layouts/default.html", "index.html",
                    ".gitignore", ".github/workflows/pages.yml"):
            shutil.copy2(ROOT / rel, dest / rel)

        src = (dest / "tools/last_updated.py").read_text(encoding="utf-8")
        if original not in src:
            print(f"  ✗ {label}: red proof is stale — the line it sabotages has moved")
            return False
        (dest / "tools/last_updated.py").write_text(
            src.replace(original, replacement + "  # SABOTAGE"), encoding="utf-8")

        proc = subprocess.run([sys.executable, "tools/check_last_updated.py"],
                              cwd=dest, capture_output=True, text=True)
        output = proc.stdout + proc.stderr
        if proc.returncode == 0:
            print(f"  ✗ {label}: check passed anyway — TA-T-101 does not guard this")
            return False
        if must_mention not in output:
            print(f"  ✗ {label}: check failed, but not on the arm that should catch it "
                  f"(expected a failure mentioning {must_mention!r})")
            return False
        print(f"  ✓ {label}: check went RED on {must_mention!r}")
        return True
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    print(f"TA-T-101 red proof — sabotaging the generator {len(SABOTAGES)} ways:")
    results = [run_sabotage(*s) for s in SABOTAGES]
    if all(results):
        print("\nTA-T-101 fails when it should. The test has teeth.")
        return 0
    print("\nRED PROOF FAILED — TA-T-101 is not guarding what TA-65 asked for.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
