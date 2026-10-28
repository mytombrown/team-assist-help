---
title: "How do I test ad cues (SCTE-35)?"
app: srtstreamtester
category: how-to
order: 4
tags: "scte-35, scte35, ad cues, ad break, splice, time_signal, splice_insert, cue, pre-roll, upid, verdict, recommended tests"
quick: "The Ad cues (SCTE-35) card has three steps: Watch the cues as they land, Send a test cue when you are sending, and a Verdict that names what to change."
related:
  - send-my-camera
  - watch-a-stream
  - read-the-numbers
---

## Where it is

- **The Ad cues (SCTE-35) card** shows during a session.
- **Watching:** turn it on or off with the **SCTE-35** button.

## Free or Pro

- **Free:** the card says **SCTE-35 cues found** and how many.
- **SRT Tester Pro** ($9.99, one time) shows the steps below.
- **Unlock:** tap **Unlock Pro** on the card, or the **★** on the Setup screen.
- **New device?** Open the ★ and tap **Restore Purchases**.

## 1 Watch

- **Every cue** shows as it lands, newest first, in plain words.
- **The small line** under it is the technical detail.
- **The +/- seconds** is how far ahead of the video it landed.

## 2 Send (sending only)

- **Send a test cue** puts a real ad-break cue into your stream.
- **Options:** **Cue type**, **Segment**, **Duration**, **Immediate (no time stamp)**, **Pre-roll** and **Label (UPID)**.
- **With a duration**, the end cue goes out by itself.
- **Watching?** Cues come from the far end. Send one from there.

## 3 Verdict

- **One line**, green or red, on whether the cues are usable.
- **What to change:** names the setting to fix on the encoder.

## Recommended tests

- **Tests that fit your link.** Each has a **Run** button.
- **Passed** or **Failed** is based on what actually arrives.
