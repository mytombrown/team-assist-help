---
title: "How do I find duplicate files?"
app: filesweep
category: how-to
order: 1
tags: "duplicates, duplicate files, copies, same file, double, twice, dupes, free space, keep oldest, keep newest"
quick: "Click Find Duplicates, then Search. Files with the same content are grouped. In each group, every copy but the oldest is checked for you."
related:
  - move-or-delete
  - find-file-type
  - troubleshooting
---

## Run the search

1. **Click Find Duplicates** at the top.
2. **Pick what to check** in **Only**: **All files**, **Images**, **Videos**, **Audio**, **Documents**, **Archives** or **Custom…**.
3. **Optional:** set a **Size** limit.
4. **Click Search.**

## How it decides

- **Same content.** Files must match byte for byte, not just by name.
- **Different names still match.** `IMG_1.jpg` and `copy.jpg` match if the content is the same.
- **Empty files** (0 bytes) are ignored.

## Reading the results

- **Each group** shows how many copies, their size **each**, and the space taken by **extra** copies.
- **Oldest copy first** in each group.
- **Checked for you:** every copy but the oldest.
- **KEEP** marks copies that are not checked.

## Change what's checked

- **Click a row** to check or uncheck it.
- **Select › All but oldest copy** — keep the oldest one.
- **Select › All but newest copy** — keep the newest one.
- **Select › None** — uncheck everything.
- **Leave one copy** unchecked in every group. The app won't move or delete all copies.

## Custom file types

- **Pick Custom…** in **Only**.
- **Type the endings,** like `jpg, png, mov`.

## Next

- [Move or delete the copies]({{ '/filesweep/move-or-delete/' | relative_url }})
