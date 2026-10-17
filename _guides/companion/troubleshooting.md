---
title: "Something isn't working — what do I do?"
app: companion
category: help
order: 1
tags: "problem, help, not working, can't connect, offline, failed, timed out, not found, pin, locked, restore purchases, log, support, contact, camera, local network"
quick: "Check the phone and Companion are on the same network, Local Network is allowed, and the Host and Port are right. Still stuck? Share the log from Settings → Diagnostics with support."
related:
  - connect-to-companion
  - use-the-dashboard
  - share-keys-operator
  - multi-instance
---

## Companion not found

- **Same network.** Phone and Companion must share one Wi-Fi or LAN.
- **Allow Local Network.** iPhone Settings → Privacy & Security → Local Network → turn on **Surface Remote**.
- **Wait a moment.** The list refreshes every 20 seconds.
- **Type it in.** Enter **Host** and **Port** on Connect.
- **"Couldn't reach …"** — the found Companion did not answer. Type the address.

## Won't connect

- **Failed: Invalid host** — check the **Host** box.
- **Failed: Connection timed out** — Companion did not answer. Check the IP and **Port**.
- **Satellite WebSocket on.** Turn it on in Companion. Its usual port is 16623.
- **Companion refused the surface** — Companion turned the phone away. The reason follows the message.
- **Keeps dropping** — leave **Auto reconnect** on in **Settings** → **Connection**.

## Keys are locked

- **Locked by Companion** — Companion has a PIN set.
- **Tap the digits** on the keypad. Keys come back once Companion unlocks.

## Dashboard empty or blocked

- **"This Companion can't share keys with a Dashboard."** — needs Companion 5 with Satellite subscriptions on.

## Operator problems

- **Show QR fails** — add the custom variable `surfaceremote_roles` in Companion.
- **"Companion's HTTP API is off."** — turn it on in Companion's settings.
- **"That QR is not a Surface Remote Operator code."** — scan the QR from **Dashboard** → **Share**.
- **Camera won't open** — iPhone Settings → **Surface Remote** → turn on Camera.
- **Keys off** — the Operator phone can't check access with Companion. Check its network.
- **Revoked** — ask the owner for a new QR.

## Screen goes dark

- **Settings** → **App** → turn on **Keep screen awake while connected**.
- **Only while connected.**

## Purchase missing

- **Tap Restore Purchases** in **Settings** → **Purchases**.
- **Use the same Apple Account** you bought with.
- **"The App Store is not reachable right now."** — try again on a working connection.
- **"Waiting for approval."** — the purchase is waiting to be approved on your Apple Account.

## Contact support

- **Open Settings** → **Diagnostics**.
- **Tap Share Log.** Send it by Mail or Messages.
- **Email** [{{ site.support_email }}](mailto:{{ site.support_email }}).
