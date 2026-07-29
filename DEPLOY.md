# DEPLOY.md — instructions for Claude Code

Tom: you don't need to read this. Just run `claude` in this folder and say:

> Read DEPLOY.md and follow it.

---

Everything below is for Claude Code.

---

You are in the root of a Jekyll site that needs deploying to GitHub Pages at
`help.mytombrown.com`. **This directory is the repo root.** It is not yet a git repo and
has never been pushed.

**Work through this in order and stop at the first thing that fails.** Do not work around
a failure — report it. Several steps touch live DNS, so a confident wrong move is worse
than stopping.

## Step 0 — preflight, change nothing

Report all of these before doing anything:

- `gh auth status` — is the GitHub CLI authenticated, as which account, with what scopes?
- `aws sts get-caller-identity` — are AWS credentials configured, for which account?
- Confirm this directory contains `_config.yml`, `_articles/`, `_layouts/`, `CNAME` and
  `.github/workflows/pages.yml`.
- `cat CNAME` — confirm it reads `help.mytombrown.com`.
- Confirm no `team-assist-help` repo already exists on the account.

If `gh` isn't authenticated, stop and say so. If AWS isn't configured, continue — step 3
has a manual fallback.

## Step 1 — create the repo and push

Create a **public** repo named `team-assist-help` (GitHub Pages needs public on the free
plan) and push this directory to `main`.

Don't add a README, licence or .gitignore at creation — this directory already has what it
needs and an auto-generated file will conflict with the push.

Report the repo URL.

## Step 2 — enable Pages with the Actions build type

The source must be **GitHub Actions**, not branch-based deployment. Branch deployment skips
the workflow, which contains a publish gate that must run.

Roughly:

```
gh api -X POST repos/{owner}/team-assist-help/pages -f build_type=workflow
```

Verify that against current `gh` docs rather than trusting the syntax above, then read the
Pages config back to confirm.

## Step 3 — the DNS record

A CNAME in the `mytombrown.com` hosted zone:

| Field | Value |
|---|---|
| Name | `help.mytombrown.com` |
| Type | `CNAME` |
| Value | `mytombrown.github.io` |
| TTL | 300 |

**Read this before touching Route 53.** The same hosted zone contains the record for
`legal.mytombrown.com`, which serves a live privacy policy referenced by an Android app and
by Google Play Console. Breaking it is a production incident.

Therefore:

- List the existing records first and show them to Tom before making any change.
- Use `CREATE`, never `UPSERT` or `DELETE`.
- The change batch must contain exactly one record, for `help.mytombrown.com`.
- If a record for `help` already exists, stop and report it rather than overwriting.

If AWS credentials aren't available, skip this and print the record for Tom to add by hand,
then wait for confirmation before continuing.

Verify with `dig +short help.mytombrown.com` before moving on.

## Step 4 — custom domain and HTTPS

Set the Pages custom domain to `help.mytombrown.com`, then wait for GitHub to issue the
certificate — usually a few minutes, occasionally up to an hour. Poll rather than assuming;
report status as it changes.

Once issued, enable HTTPS enforcement. Apple requires the Support URL to be HTTPS, so this
isn't optional.

## Step 5 — the app icon

`assets/team-assist-icon.png` is a generated placeholder, not the real logo. Find the actual
Team Assist app icon in the Xcode asset catalogue, export a square PNG at 180×180 or larger,
and replace it. Commit and push.

If you can't locate the asset catalogue, say so and leave the placeholder — but tell Tom, so
it doesn't ship by accident.

## The first build will fail. That is correct.

The workflow runs `tools/check_review.py` before building. Sixteen of twenty-two articles
carry `needs_review: true` because they were drafted from a feature list rather than from
the app, and the gate refuses to publish unverified content. The build failing at that step
is the gate doing its job.

**Do not:**

- remove, disable, or weaken the publish gate;
- edit `tools/check_review.py`;
- remove `needs_review` flags from any article;
- change the workflow so the check only warns;
- move articles out of `_articles/` to get the build green.

Only Tom can verify those articles, and clearing a flag means asserting the content is
accurate. Report the failure and stop — a red build is the expected end state of this task.

## Step 6 — verify what's verifiable

- `dig +short help.mytombrown.com` returns the GitHub Pages target
- Pages config shows the custom domain and the Actions build type
- The workflow ran and failed at the review-check step, not at build or deploy
- `python3 tools/check_review.py --report` reports 6 ready, 16 awaiting review

## Report back with

The repo URL, the Pages configuration, whether the DNS record was created or still needs
doing by hand, certificate status, whether the icon was replaced, and the exact failure
output from the workflow run.

If anything in Route 53 looked different from what's described above, say so before
proceeding rather than adapting to it.
