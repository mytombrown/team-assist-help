---
title: "What do the numbers mean?"
app: srtstreamtester
category: how-to
order: 3
tags: "stats, statistics, link, health, verdict, round-trip, rtt, loss, dropped, buffer, undecrypted, bandwidth, bitrate, codec, resolution, frame rate, captions, transport, event log, charts"
quick: "The Link card shows how healthy the connection is, with a one-line verdict. Tap any number (hover on the Mac) to see what it means."
related:
  - watch-a-stream
  - send-my-camera
  - troubleshooting
---

## Get help on any number

- **iPhone and iPad:** tap the tile.
- **Mac:** hover over it.

## Link

- **Verdict line:** green **Link healthy.** or an orange warning.
- **Round-trip:** time to the other end and back. Set latency to 3–4× this.
- **Receive rate** / **Send rate:** data moving now.
- **Loss, last second:** packets that did not arrive.
- **Dropped:** packets that came too late. These cause glitches.
- **Buffer:** video waiting in the latency buffer. Near zero means drops are coming.
- **Undecrypted:** more than zero means the passphrases do not match.
- **Link bandwidth:** what the network path can carry. Keep the bitrate well under it.
- **Orange numbers** need a look.

## Stream (watching only)

- **Video:** codec, **Profile / level**, **Resolution**, **Frame rate**, **Scan**, bitrate, **Keyframe every**.
- **Captions:** **CEA-608** and **CEA-708** say **Seen** or **None seen**.
- **Audio:** codec, **Language**, **Channels**, **Sample rate**, bitrate.
- **Transport:** packet counts and errors such as **Continuity errors** and **PCR jitter**.

## Charts and log

- **Round-Trip Time** and **Throughput** charts show the last 10 minutes.
- **Event Log** lists what happened, newest first. Red lines are errors.
