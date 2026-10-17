---
title: "How do I share keys with another phone (Operator)?"
app: companion
category: how-to
order: 3
tags: "operator, share, qr code, scan, second phone, volunteer, guest, role, revoke, remove access, limited keys"
quick: "On your Dashboard tap Share, pick keys, name the role and tap Show QR. On the other phone tap Connect → Operator and scan it. Revoke stops it."
related:
  - use-the-dashboard
  - troubleshooting
---

## What it does

- **Shares chosen keys.** The other phone sees only those keys.
- **No tabs.** The Operator gets no settings and no other pages.
- **Goes straight to Companion.** Your phone can be turned off.

## One-time setup in Companion

- **Add a custom variable** named `surfaceremote_roles`.
- **Turn on Companion's HTTP API.** The app uses port 8000.
- **The app tells you** if either is missing.

## Make a QR (your phone)

- **Build your Dashboard first.** See [Dashboard]({{ '/companion/use-the-dashboard/' | relative_url }}).
- **Tap Share** on the Dashboard.
- **Type a Role name.**
- **Pick the keys** under **Keys the Operator will see**.
- **Tap Show QR.**

## Scan it (other phone)

- **Open Connect.**
- **Tap Operator.**
- **Allow the camera.**
- **Point it at the QR.**
- **Keys appear.** The top bar shows the role name and **Live**.
- **Tap Leave Operator** to stop.

## Revoke

- **Tap Share** on your Dashboard.
- **Find it** under **Shared roles**.
- **Tap Revoke.**
- **Keys stop** on the other phone within a few seconds.
- **The other phone** says **Access revoked. Ask the owner for a new QR.**
- **Tap QR** to show a role's code again.
