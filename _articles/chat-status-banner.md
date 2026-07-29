---
title: "Why does chat say it's retrying?"
slug: chat-status-banner
category: chat
order: 2
tags: "banner, retry, sync, degraded, delayed, not sending, stuck, failed, offline"
quick: "A banner appears when messages aren't syncing normally. Messages you've sent are held and delivered once the connection recovers — they aren't lost."
needs_review: true
review_note: "The banner exists and the reassurance is right in spirit, but confirm: the banner's exact wording, what retry actually does, whether queued messages survive app termination, and whether a message ever gives up permanently. Do not describe why syncing degrades — that's internal architecture and out of scope for public docs."
related:
  - chat-basics
  - report-a-problem
---

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
