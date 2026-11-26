---
title: "How do I add it to OBS or vMix?"
app: overlaystudio
category: how-to
order: 3
tags: "obs, vmix, browser source, web browser, link, feed, url, program, 720, 1080, 4k, 1920, 3840, vertical, 9:16, 16:9, format, size, frame rate, network, transparent"
quick: "In Play, click Feed links and copy the Program link. Add it to OBS as a Browser source or to vMix as a Web Browser input."
related:
  - run-a-show
  - share-outside
  - troubleshooting
---

## Set the format first

1. **In Play,** click **Options**.
2. **Format:** 16:9, or 9:16 for vertical video.
3. **Size:** 720, 1080 or 4K.

The Program link sends exactly that. Preview and Program take the same shape.

| Format | 720 | 1080 | 4K |
|---|---|---|---|
| 16:9 | 1280 × 720 | 1920 × 1080 | 3840 × 2160 |
| 9:16 | 720 × 1280 | 1080 × 1920 | 2160 × 3840 |

## Get the link

1. **Click Feed links**.
2. **Choose** Program or Selected template.
3. **Click the copy button** next to the link you need:
   - **This Mac:** OBS or vMix runs on this same Mac.
   - **Your network:** it runs on another computer on your network.

## OBS

1. **Under Sources,** click **+** and choose **Browser**.
2. **Paste the link** into URL.
3. **Set the size** to match your format (the table above).

## vMix

1. **Click Add Input,** then **Web Browser**.
2. **Paste the link.**
3. **Set the same size.**

## Good to know

- **The background is transparent,** so your video shows through.
- **No frame rate to set.** OBS or vMix draws the page at your show's frame rate.
- **Only templates in your show's format** can be added. A 9:16 show lists 9:16 templates; a 16:9 show lists 16:9.
- **A button made in the other format** (before you changed it) is fitted and centred, never stretched. It shows 16:9 or 9:16.
- **Changed the format mid-show?** The page resizes itself. Change the size in OBS or vMix to match.
- **Keep Overlay Studio open.** The feed comes from the app.
- **Keep the Mac awake** during a show.
