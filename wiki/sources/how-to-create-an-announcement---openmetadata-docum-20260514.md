---
type: source
title: "Source: how-to-create-an-announcement---openmetadata-docum-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["how-to-create-an-announcement---openmetadata-docum-20260514.md"]
tags: []
related: []
---

# Source: how-to-create-an-announcement---openmetadata-docum-20260514.md

## Analysis: How to Create an Announcement - OpenMetadata Documentation

### Key Entities

- **Announcements** — Central entity; a scheduled, time-bound notification about upcoming changes to a data asset. Role: central.
- **Data Asset** — The target of an announcement (e.g., table, topic, dashboard). Role: peripheral (context).
- **OpenMetadata UI** — The interface through which announcements are created and viewed. Role: peripheral (implementation detail).
- **Explore** — The UI section where users navigate to find data assets. Role: peripheral (navigation context).

**Wiki existence check:** `[[announcements]]` already exists in the wiki index. This source is a procedural sub-page of that concept.

### Key Concepts

- **Announcement Creation Workflow** — A 4-step UI process: navigate to a data asset → click ellipsis → select Announcements → fill in title, start/end dates, description → submit. Why it matters: it's the only documented method for creating announcements.
- **Scheduled Display** — Announcements are shown only during the defined time window (Start Date to End Date). Why it matters: ensures time-bound relevance without manual cleanup.
- **Targeted Visibility** — Announcements are displayed only to users who own or follow the specific data asset. Why it matters: prevents notification noise for unrelated users.
- **Backward Incompatible Changes** — The source explicitly warns users to watch for announcements about backward incompatible changes. Why it matters: positions announcements as a critical operational tool for data teams.

**Wiki existence check:** All concepts are already covered in `[[announcements]]`.

### Main Arguments & Findings

- **Core claim:** Announcements are created via a simple UI workflow on individual data assets.
- **Supporting evidence:** Step-by-step procedural documentation from the official OpenMetadata docs.
- **Evidence strength:** High — this is official documentation for v1.12.x.

### Connections to Existing Wiki

- **`[[announcements]]`** — This source is the procedural sub-page of the existing concept page. It adds the specific creation workflow details.
- **`[[activity-feed]]`** — Announcements are displayed in the Activity Feed (mentioned in the existing `[[announcements]]` page).
- **`[[data-collaboration]]`** — Announcements are part of the Data Collaboration feature set (evident from the navigation breadcrumb).

**Impact:** This source **extends** the existing `[[announcements]]` page with concrete procedural steps. It does not challenge or contradict existing content.

### Contradictions & Tensions

- **No contradictions** with existing wiki content.
- **Internal tension:** The source says announcements are displayed to "all the users who own or follow that particular data asset." The existing `[[announcements]]` page says they are "displayed as banners and in the Activity Feed." These are complementary, not contradictory — the existing page describes *where* they appear, this source describes 
