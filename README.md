# Team Assist Help

Public help documentation for Team Assist. A Jekyll site on GitHub Pages, in its own
repository so help edits can never touch the legally-reviewed pages in
`team-assist-legal`.

**6 of 22 articles are verified. 16 are not, and the site will not deploy while that's
true.** That's deliberate — see the publish gate below.

## Setting it up

1. Create a public repo `team-assist-help` and push this directory to `main`.
2. Settings → Pages → **Source: GitHub Actions** (not "Deploy from a branch" — that
   skips the publish gate).
3. Route 53: CNAME `help` → `mytombrown.github.io` in the `mytombrown.com` zone.
4. Settings → Pages → Custom domain `help.mytombrown.com`, then **Enforce HTTPS** once
   the certificate issues.
5. Replace `assets/team-assist-icon.png` — the one there is a generated placeholder,
   not your logo.

The first build will fail at the publish gate. That's expected.

## The publish gate

```
python3 tools/check_review.py            # fails while any article is unverified
python3 tools/check_review.py --report   # status only, never fails
```

Articles drafted without seeing the app carry `needs_review: true`, a `review_note`
saying what must be confirmed, and `published: false` so Jekyll excludes them from the
built site entirely. The gate fails if a held article would publish (or a cleared one
is still unpublished); held articles no longer block the rest of the site from
deploying.

The workflow runs the gate on every push. Pull requests report only, so drafts can be
reviewed in a branch. `main` fails, so unverified content cannot reach the live site by
accident.

To clear an article: check it against the app, fix what's wrong, delete the
`needs_review` and `review_note` lines.

The gate also catches missing `title`/`category`/`quick` and any article whose
`category` isn't declared in `_config.yml` — which would otherwise make it vanish from
the index while still being live at its own URL.

## Editing

Articles are markdown in `_articles/`:

```yaml
---
title: "Why does chat say it's retrying?"
slug: chat-status-banner
category: chat            # must match an id in _config.yml
order: 2                  # position within its category
tags: "banner retry sync stuck failed offline"
quick: "One or two sentences. Must stand completely alone."
needs_review: true        # delete once verified
review_note: "What still has to be confirmed."
related:
  - chat-basics
---
```

`quick` is the most important field — it appears in search results, so most people read
it without opening the article. If it says "it depends, see below", it isn't finished.

`tags` never display. They exist so search finds the article when someone uses a word
that isn't in the title. Include the wrong words people actually type.

Article URLs come from `slug`. Changing one breaks links already shared in support
email, so treat them as permanent once live.

## Previewing

The real build is Jekyll, run by GitHub Actions. Locally, without Ruby:

```
pip install markdown
python3 tools/preview.py
python3 -m http.server -d _preview 8000
```

`tools/preview.py` reimplements the layouts closely enough to check design, content and
search. It is **not** Jekyll — if they disagree, Jekyll is right. `_preview/` is
disposable and gitignored.

With Ruby: `bundle install && bundle exec jekyll serve`.

## What's here

| Path | |
|---|---|
| `_articles/` | The content. Normally the only thing you edit. |
| `_config.yml` | Site settings, category list, support email, legal URLs. |
| `_layouts/` | Page templates. |
| `assets/` | Stylesheet, search script, app icon. |
| `search.json` | Jekyll-generated search index. |
| `tools/check_review.py` | The publish gate. |
| `tools/preview.py` | Ruby-free local preview. |
| `tools/make_articles.py` | Generated the initial articles. Re-running overwrites them — you almost certainly don't want to. |

## Constraints this site is built under

- **Only "Team Assist."** Never the repo, Xcode project, scheme or source folder names.
- **No internal architecture.** No storage or messaging mechanisms, no gateway or API
  hostnames.
- **Never restate the privacy policy.** Link to it. A summary that drifts out of step
  with the policy is worse than no summary.
- **Nothing about Android.** Pre-release, no public listing. There are no Android
  articles here.
- **Adults only.** Users are coaches, parents or guardians, and athletes 18 or over.
  Athletes under 18 are never users. Don't write anything implying otherwise.
- **No age policy beyond the 18+ requirement**, and nothing marketing to children.
- **Never infer a feature from its name.** The reason 16 articles are flagged rather
  than written is that a plausible guess about what "Run Playbook" does is still a guess.
