#!/usr/bin/env python3
"""
Generates every article in _articles/ .

Run once to scaffold. After that, edit the markdown files directly — re-running
this overwrites them.

Articles written from settled decisions are clear. Articles drafted from a feature
list rather than from observed app behavior carry `needs_review: true` and a
`review_note` naming exactly what must be confirmed. tools/check_review.py refuses
to let those go live.
"""

import pathlib

OUT = pathlib.Path(__file__).parent.parent / "_articles"
OUT.mkdir(exist_ok=True)

A = []


def art(slug, category, order, title, tags, quick, body,
        needs_review=False, review_note="", related=None):
    A.append(dict(slug=slug, category=category, order=order, title=title, tags=tags,
                  quick=quick.strip(), body=body.strip(), needs_review=needs_review,
                  review_note=review_note.strip(), related=related or []))


# ============================================================ GETTING STARTED

art("who-can-use", "getting-started", 1,
    "Who can use Team Assist?",
    "who, age, adult, 18, minor, child, kid, parent, guardian, eligible, restriction",
    "Team Assist is for adults only — coaches and trainers, parents or guardians, and "
    "athletes aged 18 or over. Athletes under 18 don't have accounts.",
    """
Everyone who uses Team Assist is an adult. There are three kinds of account:

- **Coaches and trainers** — the people running sessions.
- **Parents and guardians** — an adult acting in relation to an athlete under 18.
- **Athletes aged 18 or over** — using it for themselves.

**Athletes under 18 are not users.** They don't have accounts, don't sign in, and don't
appear in messages. Their coach keeps a record for them in the app, and where there's
anything to discuss, it happens with their parent or guardian.

That's a deliberate design choice rather than a limitation. Keeping minors out of the
account system entirely means no information is collected from them, there's no
messaging between an adult and a child, and far less of their information exists at all.

## What this means when you sign up

You'll be asked to confirm you're 18 or over. Team Assist checks this with Apple, which
tells us whether you're an adult without telling us your date of birth — we never see it
and never store it.

If the check can't confirm you're an adult, the app won't open. You'll see a screen
explaining why, with the option to complete the confirmation and try again. There's no
partial or limited version.

## If you coach athletes under 18

Nothing stops you. Add them to your roster and work with them as you would anyone else —
sessions, teams, billing and notes all work normally.

The difference is that the athlete has no account. If you want a parent or guardian to
see what you publish, or to message you about their child, invite them and they'll have
their own account.

You don't have to invite anyone. An athlete record works perfectly well on its own.
""",
    related=["no-account", "invitations", "privacy-and-data"])

art("no-account", "getting-started", 2,
    "Do I need to create an account?",
    "account, sign up, register, login, password, email, icloud, apple, free",
    "There's nothing to sign up for and no password. Team Assist uses the Apple Account "
    "already on your iPhone. You do need to confirm you're 18 or over.",
    """
There's no Team Assist account to create. The app uses the Apple Account your iPhone is
already signed into.

The one thing you'll be asked is to confirm you're an adult, since
[Team Assist is for adults only]({{ '/who-can-use/' | relative_url }}). That check goes
through Apple, which confirms your age band without sharing your date of birth.

Two things follow from having no separate account with us.

**Your information follows your Apple Account, not your phone.** Sign into the same
account on another device and it comes with you.

**There's no password for us to reset.** Getting into Team Assist means getting into your
Apple Account, which Apple manages. If you're locked out of that, Apple is who can help —
we have no way in.

To see which Apple Account your iPhone is using, open Settings and look at the name at
the top.
""",
    related=["who-can-use", "your-identity", "requirements"])

art("what-is-team-assist", "getting-started", 3,
    "What is Team Assist?",
    "what is, overview, about, coach, start, purpose, features",
    "Team Assist is an iPhone app for coaches and trainers — scheduling sessions, managing "
    "a roster, running sessions, handling billing, and sharing with connected parents and athletes.",
    """
Team Assist brings the parts of coaching that usually live in several different places
into one app: who you work with, when you're seeing them, what you do in the session, and
what they owe.

The main areas are:

- **Dashboard** — your starting point when you open the app.
- **Schedule and sessions** — when you're working and with whom.
- **Clients and roster** — the people you coach.
- **Teams** — groups of athletes.
- **Run Playbook** — running a session, including recording audio on your device.
- **Finance center** — packages, billing and templates.
- **Athlete portal** — publishing information to connected parents and adult athletes.
- **Team chat** — messaging.

There's also an Apple Watch companion, a Home Screen widget, and a share extension for
getting things into Team Assist from other apps.

Each has its own article in this help centre.
""",
    needs_review=True,
    review_note="Feature names are correct and confirmed. The one-line descriptions of "
                "what each one does are inferred from the name — confirm or correct each "
                "line before publishing.",
    related=["who-can-use", "no-account"])

art("install", "getting-started", 4,
    "How do I get Team Assist?",
    "install, download, app store, testflight, get, setup, beta",
    "Team Assist is an iPhone app. [Needs confirming: whether it's currently on the App "
    "Store or distributed through TestFlight.]",
    """
> This article can't be finished until the distribution route is settled. Both versions
> are drafted — keep the one that's true and delete the other.

**If it's on the App Store:** search for Team Assist in the App Store on your iPhone and
tap Get. It installs like any other app.

**If it's a TestFlight beta:** open the invite link you were sent on your iPhone. If you
don't have TestFlight, the link takes you to the App Store to install it first — it's
free and made by Apple. Then tap Accept, then Install. Beta builds carry a small orange
dot beside the app name and expire 90 days after release, at which point TestFlight
offers you the newer build.

Once it's installed, open it and confirm you're 18 or over. There's no account to create.
""",
    needs_review=True,
    review_note="Decide App Store versus TestFlight and delete the branch that doesn't "
                "apply. If both are true during a transition, say so explicitly.",
    related=["no-account", "requirements", "who-can-use"])

art("requirements", "getting-started", 5,
    "What do I need to run Team Assist?",
    "requirements, ios, iphone, ipad, compatibility, version, android, watch",
    "An iPhone, and you must be 18 or over. [Needs confirming: the minimum iOS version, "
    "and whether iPad is supported.]",
    """
Team Assist is an iPhone app, and it's for adults — see
[who can use Team Assist]({{ '/who-can-use/' | relative_url }}).

> The minimum iOS version needs to come from the project's deployment target rather than
> a guess. An inaccurate answer here produces support mail from people whose install
> failed silently, which is the worst kind of support mail because they don't know why.

There's an Apple Watch companion, which needs an Apple Watch paired to the iPhone running
Team Assist.

Android isn't available.
""",
    needs_review=True,
    review_note="Fill in: minimum iOS version from the Xcode deployment target, whether "
                "iPad is supported or iPhone-only, and the minimum watchOS version. Also "
                "confirm the Android line — accurate today, but it changes at release.",
    related=["install", "watch-widget-share"])

# ============================================================ COACHING

art("dashboard", "coaching", 1,
    "The dashboard",
    "dashboard, home, main screen, overview, start",
    "The dashboard is what you see when you open Team Assist. [Needs confirming: what it "
    "actually shows.]",
    """
> This article needs writing from the app. The dashboard is the first thing every coach
> sees, so it's worth being precise about what's on it and what each part does.

Structure to fill in: what appears on the dashboard, what's tappable and where each thing
leads, whether anything about it can be customised, and what it looks like on day one
before there's any data — the empty state is what new users actually encounter.
""",
    needs_review=True,
    review_note="Entirely unwritten. Needs: what the dashboard displays, what's "
                "interactive, whether it's configurable, and the first-run empty state.",
    related=["schedule-sessions", "what-is-team-assist"])

art("schedule-sessions", "coaching", 2,
    "Scheduling sessions",
    "schedule, session, calendar, book, appointment, time, reschedule, cancel",
    "The schedule is where your sessions live. [Needs confirming: how sessions are created, "
    "edited, repeated and cancelled.]",
    """
> Drafted structure only — the specifics need to come from the app.

To complete: how a coach creates a session and what's required versus optional, whether
sessions repeat and how a repeating series is edited or broken, how to reschedule or
cancel and whether connected adults are notified, whether sessions connect to the
iPhone's own Calendar, and how sessions relate to clients and teams.

Worth covering explicitly: what happens to a session's associated information —
recordings, notes, billing — when the session is deleted. People ask.
""",
    needs_review=True,
    review_note="Needs the full session lifecycle: create, edit, repeat, reschedule, "
                "cancel, delete. Confirm whether connected parents or adult athletes are "
                "notified of changes, and whether there's Calendar integration.",
    related=["roster-and-teams", "run-playbook", "athlete-visibility"])

art("roster-and-teams", "coaching", 3,
    "Clients, roster and teams",
    "client, roster, athlete, team, group, add, remove, contact, list",
    "Your roster holds the people you coach; teams group athletes together. Athletes work "
    "fully whether or not anyone has an account. [Needs confirming: how each works.]",
    """
An athlete record stands on its own. It doesn't need a parent or adult athlete connected
to be complete — scheduling, teams, billing and notes all work regardless. See
[inviting a parent or an adult athlete]({{ '/invitations/' | relative_url }}) for what
connecting someone adds.

> The relationship between an individual client, a roster entry, and a team member is the
> kind of thing that's obvious inside the app and confusing from outside. It needs
> describing precisely.

To complete: how someone is added to the roster, what information is held about them, how
teams are created and who can be in one, whether an athlete can be on several teams or be
both an individual client and a team member, and how someone is removed — including what
happens to their history.
""",
    needs_review=True,
    review_note="Clarify the data model in plain language: client versus roster entry "
                "versus team member. Confirm what happens to past sessions and billing "
                "when someone is removed.",
    related=["invitations", "athlete-visibility", "schedule-sessions"])

art("run-playbook", "coaching", 4,
    "Run Playbook",
    "playbook, run, session, record, recording, audio, microphone, live",
    "Run Playbook is for running a session as it happens, and can record audio on your "
    "device. [Needs confirming: how it works in practice.]",
    """
> Audio recording deserves unusually careful documentation. People want to know where a
> recording goes, who can hear it, and how to delete it — and they want to know before
> they record, not after.

To complete: how a playbook is started and what a coach sees during a session, how
recording is started and stopped and whether it's obvious that it's running, where
recordings are stored, how long they're kept, whether anyone other than the coach can
access them, how to delete one, and what happens if the session is interrupted by a phone
call or the app going to the background.

Also needed: the microphone permission prompt — when it appears, and what happens if a
coach declines it.

Anything about who else can hear a recording must be consistent with the
[privacy policy]({{ site.legal.privacy }}) rather than stated independently here.
""",
    needs_review=True,
    review_note="Highest-priority article to get right, because it involves recording "
                "people — including minors. Needs: recording storage and retention, "
                "deletion path, who can access recordings, microphone permission "
                "behavior, interruption handling. Check the wording against the privacy "
                "policy, and note that recording sessions involving minors is flagged in "
                "the Legal Revision Brief as needing counsel's attention.",
    related=["schedule-sessions", "privacy-and-data"])

art("finance-center", "coaching", 5,
    "Finance center",
    "finance, billing, invoice, payment, package, template, money, charge, paid",
    "The finance center handles packages, billing and templates. [Needs confirming: what "
    "it does and, importantly, what it doesn't.]",
    """
> The critical question for this article is whether Team Assist processes payments or only
> records them. Those are very different products, and users will assume the more capable
> one unless told otherwise.

To complete: what a package is and how one is set up, what billing templates do, whether
money actually moves through the app or whether it tracks amounts you collect elsewhere,
how a coach marks something as paid, and what reporting exists.

If payments are recorded rather than processed, say so plainly and early. A coach who
assumes their client can pay through the app and finds out otherwise mid-conversation will
not be pleased.
""",
    needs_review=True,
    review_note="Answer first: does the app process payments, or record them? Then what "
                "packages and templates are, how payment status is tracked, and what "
                "reporting exists. Any payment processor involved has App Store review "
                "implications worth checking separately.",
    related=["subscription-billing"])

art("athlete-portal", "coaching", 6,
    "Publishing to connected parents and athletes",
    "publish, portal, share, send, parent, guardian, athlete, view, visible",
    "Publishing makes information available to the connected adults for an athlete — a "
    "parent or guardian, or an athlete aged 18 or over. [Needs confirming: what can be published.]",
    """
Publishing sends information to the adults connected to an athlete. For an athlete under
18 that's their parent or guardian; for an athlete 18 or over it can be the athlete
themselves.

Nothing is ever published to someone under 18. They have no account to receive it.

If nobody is connected to an athlete, there's nobody to publish to. That's a normal
state, not an error.

> To complete: what a coach can publish, how publishing is done, what the recipient sees
> and where, whether publishing can be undone, and whether they're notified.
>
> Also needs confirming: whether there is a shipping way for a connected parent to view
> published content, given the parent-facing app is pre-release. If there isn't yet, this
> article should say so plainly rather than describe a loop that isn't closed.
""",
    needs_review=True,
    review_note="Who receives published content is settled and correct. Still needed: "
                "content types, whether publishing is reversible, notification behavior, "
                "and whether a connected parent currently has any shipping way to view it "
                "given the parent app is pre-release.",
    related=["athlete-visibility", "invitations", "who-can-use"])

art("watch-widget-share", "coaching", 7,
    "Apple Watch, the widget, and sharing into Team Assist",
    "watch, apple watch, widget, home screen, share, share sheet, extension, today",
    "Team Assist includes an Apple Watch companion, a Home Screen widget, and a share "
    "extension. [Needs confirming: what each one does.]",
    """
> Three small features grouped together because each needs a paragraph rather than a page.
> Split them out if any turns out to be substantial.

**Apple Watch.** To complete: what the Watch app shows and lets you do, whether it works
away from the iPhone, and how it's installed.

**Home Screen widget.** To complete: which sizes exist, what each shows, whether it's
configurable, and how often it refreshes.

**Share extension.** To complete: what can be shared into Team Assist from other apps,
where it lands, and how a coach finds it afterwards.
""",
    needs_review=True,
    review_note="Three separate features to document. Each needs its actual behavior "
                "confirmed — nothing here should be inferred from the feature name.",
    related=["dashboard", "requirements"])

# ============================================================ CHAT

art("chat-basics", "chat", 1,
    "Using team chat",
    "chat, message, messaging, talk, send, conversation, group, dm, parent",
    "Chat is between adults — you and the parents or adult athletes connected to you. "
    "[Needs confirming: who can start conversations, and what can be sent.]",
    """
Everyone with an account is an adult, so every conversation in Team Assist is between
adults. For an athlete under 18 that means you're messaging their parent or guardian.

**Nobody under 18 appears in chat.** They have no account, so there's nothing to message.

> To complete: who can start a conversation and with whom, whether group conversations
> exist, what can be sent besides text, whether messages can be edited or deleted,
> notification behavior, and how far back history goes.

If a message can't be unsent, say so — it's the single most-asked question about any chat
feature.

For what the status banner means, see
[chat status and the retry banner]({{ '/chat-status-banner/' | relative_url }}).
""",
    needs_review=True,
    review_note="Who can be in a conversation is settled. Still needed: conversation "
                "creation, group versus one-to-one, supported content types, edit and "
                "delete behavior, notifications, history retention.",
    related=["chat-status-banner", "invitations", "who-can-use"])

art("chat-status-banner", "chat", 2,
    "Why does chat say it's retrying?",
    "banner, retry, sync, degraded, delayed, not sending, stuck, failed, offline",
    "A banner appears when messages aren't syncing normally. Messages you've sent are held "
    "and delivered once the connection recovers — they aren't lost.",
    """
Team chat sometimes shows a banner saying syncing is degraded, with an option to retry. It
means messages are taking longer than usual to send or receive.

**What it doesn't mean:** it doesn't mean your messages are gone. Anything you've sent is
held and delivered once things recover.

**What to do:** usually nothing. Give it a moment and it clears on its own. If it
persists, tapping retry prompts another attempt. Checking that you have a working internet
connection is worth doing first — the banner can't tell the difference between a problem
at our end and your phone being on a hotel Wi-Fi that hasn't finished connecting.

If the banner stays up for a long stretch with a good connection, that's worth
[reporting]({{ '/report-a-problem/' | relative_url }}) with rough times, which makes it
much easier to trace.
""",
    needs_review=True,
    review_note="The banner exists and the reassurance is right in spirit, but confirm: "
                "the banner's exact wording, what retry actually does, whether queued "
                "messages survive app termination, and whether a message ever gives up "
                "permanently. Do not describe why syncing degrades — that's internal "
                "architecture and out of scope for public docs.",
    related=["chat-basics", "report-a-problem"])

# ============================================================ CONNECTIONS

art("invitations", "connections", 1,
    "Inviting a parent or an adult athlete",
    "invite, invitation, connect, link, add, accept, pending, request, parent, guardian",
    "You invite an adult — a parent or guardian for an athlete under 18, or the athlete "
    "themselves if they're 18 or over. Inviting anyone is optional.",
    """
Everyone with an account is an adult, so an invitation always goes to an adult.

When you invite someone in connection with an athlete, you choose which:

- **A parent or guardian**, for an athlete under 18. They get their own account and become
  the person you deal with about that athlete.
- **The athlete**, if they're 18 or over.

You make that choice at the point of inviting. Team Assist doesn't ask for the athlete's
age and doesn't store one — you know who you're working with.

## You don't have to invite anyone

An athlete record works fully without any invitation ever being sent. Sessions, teams,
billing, notes and reporting all behave normally. Plenty of athletes will never have anyone
connected, and that's a finished setup rather than an unfinished one.

What an invitation adds is a channel: someone who can see what you publish and message you
about that athlete.

## Athletes under 18 are never invited

They don't have accounts, so there's nothing to invite them to. Everything relating to them
goes through their parent or guardian, if one is connected.

> Still to document: exactly what an invited person receives, how they accept, how pending
> and accepted invitations are shown to you, whether invitations expire, and how a
> connection is ended by either side.
""",
    needs_review=True,
    review_note="The model here is settled and correct. What's missing is the mechanics: "
                "what the invited person receives, the acceptance flow, how pending versus "
                "accepted is displayed, expiry, and how either side ends a connection.",
    related=["who-can-use", "athlete-visibility", "roster-and-teams"])

art("athlete-visibility", "connections", 2,
    "Who can see what",
    "visibility, sees, privacy, who can see, access, permission, linked, parent, athlete",
    "Only connected adults see anything — a parent or guardian, or an adult athlete — and "
    "only what comes from coaches they're actively connected to. Athletes under 18 see nothing.",
    """
**Athletes under 18 see nothing, because they have no account.** There's no app for them to
open and nothing addressed to them. Anything you publish about them is visible to their
parent or guardian, if one is connected.

For the adults who do have accounts, visibility follows the active connection.

A connected parent or guardian sees what comes from coaches they're currently connected to,
about the athlete they're connected for. An adult athlete sees what comes from coaches
they're currently connected to.

Anything from a coach they aren't connected to isn't visible — including a coach they were
connected to previously but no longer are.

This matters most where an athlete works with more than one coach. Each coach's sessions
are separate, and being connected to one reveals nothing about another.

> Still to document: exactly which details of a session a connected adult sees, and whether
> ending a connection hides past sessions or only future ones.
""",
    related=["who-can-use", "invitations", "privacy-and-data"])

# ============================================================ ACCOUNT

art("your-identity", "account", 1,
    "How your identity works",
    "identity, apple account, apple id, icloud, sign in, switch, new phone, device, adult",
    "Team Assist uses the Apple Account already on your iPhone, plus a one-time "
    "confirmation that you're 18 or over. Your information follows that account, not the device.",
    """
There's no separate Team Assist login. The app uses the Apple Account your iPhone is signed
into, which you can see at the top of the Settings app, and confirms once that you're an
adult.

**Getting a new iPhone.** Sign into the same Apple Account, install Team Assist, and open
it. Your information comes down on its own — nothing to export or transfer. Give it time on
Wi-Fi, and don't wipe the old phone until you've confirmed everything arrived.

**Using a different Apple Account.** Each Apple Account holds an entirely separate set of
information. Switching doesn't merge anything and doesn't delete anything — it shows you a
different set. If you're choosing between a personal and a work account, choose before you
put much in, because there's no way to move between them afterwards.

**If everything looks empty.** Check which Apple Account you're signed into before assuming
the worst. Being in the wrong one is by far the most common cause, and switching back brings
everything into view exactly as it was.

**The age confirmation.** If Team Assist can't confirm you're 18 or over — including if the
check is unavailable or you decline it — the app won't open, and you'll be offered the
chance to complete it. Nothing is lost while that's outstanding.
""",
    related=["who-can-use", "no-account", "privacy-and-data"])

art("privacy-and-data", "account", 2,
    "Privacy and your data",
    "privacy, data, policy, collect, gdpr, information, secure, personal, children, minor",
    "Our privacy policy is the authoritative description of what Team Assist handles and "
    "how, published at legal.mytombrown.com/privacy.",
    """
What Team Assist collects, why, and how long it's kept is set out in full in the privacy
policy. That document is authoritative, and this help centre deliberately doesn't restate
it — a summary that drifts out of step with the policy is worse than no summary at all.

**[Read the privacy policy]({{ site.legal.privacy }})**

Two things worth knowing that sit alongside it:

**Team Assist is for adults.** Nobody under 18 has an account, so no information is ever
collected from a child. Information about an athlete under 18 is entered by an adult —
their coach, or their parent or guardian. See
[who can use Team Assist]({{ '/who-can-use/' | relative_url }}).

**We never receive your date of birth.** The adult confirmation at sign-up goes through
Apple, which tells us whether you're 18 or over without telling us when you were born.

To have information removed, see
[deleting your account or data]({{ '/delete-your-data/' | relative_url }}).

For a privacy question the policy doesn't answer, email
[{{ site.support_email }}](mailto:{{ site.support_email }}).
""",
    related=["who-can-use", "delete-your-data", "your-identity"])

art("delete-your-data", "account", 3,
    "Deleting your account or data",
    "delete, remove, erase, close account, wipe, gdpr, request, data, child, minor",
    "Deletion is handled through the request page at legal.mytombrown.com/delete-account, "
    "which explains what to send and what happens next.",
    """
There's a dedicated page for deletion requests, which works whether or not you can sign in.

**[Go to the account deletion page]({{ site.legal.delete_account }})**

In short: email the support address with the account email address, saying whether you want
everything removed or only certain information. You may be asked for limited details to
confirm the account is yours, and you'll be told when it's done.

One thing worth repeating from that page, because it matters: **never send your password,
verification code, or recovery credentials.** Nobody at Team Assist will ask for them, and
anyone who does isn't us.

## Records about an athlete under 18

An athlete under 18 has no account, so there's no account to delete. What exists is a record
their coach keeps.

If you're a parent or guardian and want that record removed, use the same page and explain
the situation — who you are, which athlete, and which coach.

> Still to document: exactly who may request removal of a minor's record, what's needed to
> verify it, and what happens if a coach and a parent disagree.
""",
    needs_review=True,
    review_note="The account-deletion part is accurate and matches the live page. The "
                "minor's-record part is with legal review — question 4 in the Legal "
                "Revision Brief. Don't publish specifics until counsel answers.",
    related=["privacy-and-data", "contact-support", "who-can-use"])

# ============================================================ BILLING

art("subscription-billing", "billing", 1,
    "Subscriptions and payments",
    "subscription, price, cost, free, paid, cancel, refund, billing, charge, trial",
    "[Needs confirming: whether Team Assist has a paid tier at all. If it doesn't, delete "
    "this whole section rather than leaving it vague.]",
    """
> Nothing confirms whether Team Assist has a subscription or in-app purchases, so this
> article is a skeleton rather than a draft. Vague answers about money make people uneasy —
> either fill this in properly or delete the whole billing section.

If there **is** a paid tier, this article needs: what's free and what isn't, what it costs,
whether there's a trial, and how to see current status.

The parts that are true of any App Store subscription, once there is one:

- Subscriptions are billed by Apple, so cancelling is done in iPhone Settings — tap your
  name, then Subscriptions. It can't be done inside the app.
- Cancelling leaves access running until the end of the period already paid for.
- Refunds go through Apple at reportaproblem.apple.com.

Note this is separate from the [finance center]({{ '/finance-center/' | relative_url }}),
which is about billing your own clients rather than anything you pay us.
""",
    needs_review=True,
    review_note="First answer whether any StoreKit or in-app purchase code exists. If not, "
                "delete this article and remove the billing category from _config.yml. If "
                "it does, fill in pricing, trial terms and what's gated.",
    related=["finance-center"])

# ============================================================ SUPPORT

art("contact-support", "support", 1,
    "Contacting support",
    "contact, support, email, help, human, talk, reach, question",
    "Email appstoresupportwithasmile@icloud.com. Including your iPhone model, iOS version "
    "and what you were doing usually saves a round trip.",
    """
Email is the way to reach us:
**[{{ site.support_email }}](mailto:{{ site.support_email }})**

Helpful things to include:

- What you expected to happen, and what happened instead.
- The steps to make it happen again, if you can find them.
- Your iPhone model and iOS version, both in Settings under General, then About.
- A screenshot, if there's anything to see.

**Never send your password, verification code, or recovery credentials.** We will never ask
for them.

For deletion requests, the [account deletion page]({{ site.legal.delete_account }}) explains
exactly what to send.
""",
    related=["report-a-problem", "delete-your-data"])

art("report-a-problem", "support", 2,
    "Reporting a bug",
    "bug, report, feedback, problem, issue, broken, crash, wrong",
    "Email support with what you expected, what happened instead, and the steps to reproduce "
    "it. A reproducible report is one that can be fixed.",
    """
Send bug reports to [{{ site.support_email }}](mailto:{{ site.support_email }}).

What separates a report that gets fixed from one that doesn't is reproducibility. "Chat is
broken" is hard to act on. "Sent a message on Wi-Fi, the retry banner appeared and stayed up
for ten minutes, message arrived eventually" describes something that can be traced.

Worth including:

- What you expected, what happened, and the steps in between.
- Roughly when it happened, which helps enormously for anything sync-related.
- Your iPhone model and iOS version, from Settings, then General, then About.
- A screenshot if there's something visible.

If the app crashed, iOS may offer to share crash data with developers. Allowing that is
genuinely useful and doesn't include anything you've created in the app.

> If Team Assist is distributed through TestFlight, this article should point at TestFlight's
> Send Beta Feedback instead, since it attaches device, build and log details automatically.
""",
    needs_review=True,
    review_note="Add the TestFlight feedback route if beta distribution applies, and confirm "
                "the iOS crash-sharing sentence is accurate for this app.",
    related=["contact-support", "chat-status-banner"])


# ============================================================ write files

def esc(s):
    return s.replace('"', '\\"')


for a in A:
    fm = ["---", f'title: "{esc(a["title"])}"', f'slug: {a["slug"]}',
          f'category: {a["category"]}', f'order: {a["order"]}',
          f'tags: "{esc(a["tags"])}"', f'quick: "{esc(a["quick"])}"']
    if a["needs_review"]:
        fm.append("needs_review: true")
        if a["review_note"]:
            fm.append(f'review_note: "{esc(a["review_note"])}"')
    if a["related"]:
        fm.append("related:")
        fm += [f"  - {r}" for r in a["related"]]
    fm.append("---")
    (OUT / f'{a["slug"]}.md').write_text("\n".join(fm) + "\n\n" + a["body"] + "\n",
                                         encoding="utf-8")

drafts = sum(1 for a in A if a["needs_review"])
print(f"wrote {len(A)} articles ({drafts} awaiting review, {len(A) - drafts} ready)")
