---
title: "How do I add a lot of athletes at once from a spreadsheet?"
slug: import-athletes-csv
category: coaching
order: 8
tags: "import, CSV, spreadsheet, Excel, Numbers, Google Sheets, template, bulk, many athletes, roster, parents, upload, add athletes, list"
quick: "On the Athletes tab, tap the table icon next to All Athletes (or Add › Import from CSV). Get the template, fill it in (one athlete per row), save it as CSV, and upload it. Check the preview, then tap Add. Nobody is invited or messaged."
related:
  - roster-and-teams
  - invitations
---

<!-- Written from build 227 source (Version 1.2.1 (227)): AthleteCSVImportView.swift,
     AthleteCSVImportPolicy.swift, ClientsView.swift on future/1.3 41099522.
     No screenshots yet. -->

Have your roster in a spreadsheet already? Import it in one go instead of adding
athletes one at a time. Each row adds an athlete and their parent.

## Open the import

1. Open the **Athletes** tab.
2. At the top of the list, next to **All Athletes**, tap the small table icon.
   (Where the list has an **Add** button, you can also tap **Add** and choose
   **Import from CSV**.) The **Import from CSV** screen opens.

## 1. Get the template

Tap **Get the template**. Save it to Files, or send it to your computer.

The template has these columns. The ones with a **\*** must be filled in:

| Column | About it |
|---|---|
| **Athlete Name\*** | |
| **Parent Name\*** | |
| **Parent Phone\*** | Used to spot an athlete you already have. |
| Parent Email | |
| Second Parent Name | |
| Second Parent Phone | |
| Group | The team. A new team is made if you don't have it yet. |
| Notes | |

It comes with one example row (Jordan Smith). You can leave it in or delete it —
it is never added.

## 2. Fill it in

Open the template in Numbers, Excel or Google Sheets. Put **one athlete per row**.
When you're done, **save it as CSV**.

## 3. Upload it

Back on the **Import from CSV** screen, tap **Upload CSV** and pick your file.
Picked the wrong one? Tap **Choose a different file**.

## Check the preview

Before anything is added, Team Assist sorts every row into one of three lists:

- **New** — these will be added.
- **Already here — skipped** — the same athlete name and parent phone as an
  athlete you already have, or as an earlier row in the file.
- **Needs fixing — not added** — each one says its row number and what is wrong,
  like "Missing Parent Phone" or "Parent Phone looks wrong".

## Add them

Tap **Add** at the bottom (it reads, for example, **Add 17 athletes**). You see
"Added 17 athletes." Tap **Done**.

Rows that needed fixing: fix them in the spreadsheet and upload it again. The
athletes you already added are skipped, so nothing is added twice.

## Nothing is sent

Importing only adds contacts. **No invites or messages are sent.** When you're
ready, send each athlete's family their invite — see
[how do I invite a parent or an adult athlete?]({{ '/invitations/' | relative_url }}).

## If the file won't load

- **"That file is missing the … column. Start from the template."** — a required
  column was renamed or deleted. Start again from **Get the template**.
- **"That file is empty."** — the file has no rows.
- **"That file is not text. Save it as CSV and try again."** — it was saved as a
  spreadsheet (.xlsx or .numbers), not CSV. Export or save it as CSV.
