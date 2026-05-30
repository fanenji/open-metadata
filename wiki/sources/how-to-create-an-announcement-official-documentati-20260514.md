---
type: source
title: "Source: how-to-create-an-announcement-official-documentati-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["how-to-create-an-announcement-official-documentati-20260514.md"]
tags: []
related: []
---

# Source: how-to-create-an-announcement-official-documentati-20260514.md

## Analysis of: how-to-create-an-announcement-official-documentati-20260514.md

### Key Entities

| Name | Type | Role | In Wiki? |
|------|------|------|----------|
| Announcements | Feature/Concept | Central — the subject of the document | Yes ([[announcements]]) |
| Data Asset | Entity | Central — the target of announcements | Yes (implied across wiki) |
| Explore | UI Feature | Peripheral — navigation entry point | No (not a dedicated page) |
| Vertical Ellipsis (⋮) | UI Element | Peripheral — action trigger | No |

### Key Concepts

| Name | Definition | Why It Matters | In Wiki? |
|------|------------|----------------|----------|
| Announcement Creation | UI workflow to create a scheduled, time-bound notification about changes to a data asset | Core user action for data collaboration; enables proactive communication about breaking changes | Partially — [[announcements]] covers purpose/display but not the creation workflow |
| Announcement Visibility | Announcements are displayed to users who **own or follow** the data asset | Defines the audience scope; important for understanding who sees the notification | Not explicitly documented |
| Backward Incompatible Change Alert | Quick Tip advising users to watch announcements for breaking changes | Highlights the primary practical value of announcements for data teams | Not documented |

### Main Arguments & Findings

- **Core Claim:** Announcements can be created via a simple 5-step UI workflow (Explore → Asset → Ellipsis → Announcements → Add → Fill form → Submit).
- **Required Fields:** Title, Start Date, End Date, Description.
- **Audience Scope:** Announcements are displayed to users who **own or follow** the specific data asset.
- **Pro Tip:** Announcements should be used for deletion, deprecation, and other important changes, with tentative dates.
- **Evidence Strength:** Official documentation; authoritative but minimal — a single procedural page with no troubleshooting, examples, or edge cases.

### Connections to Existing Wiki

- **Strengthens** [[announcements]] — provides the missing procedural "how-to" counterpart to the conceptual overview.
- **Extends** [[activity-feed]] — announcements are displayed in the Activity Feed; this document explains how they get created.
- **Related to** [[data-asset-ownership]] — the audience scope (owners/followers) ties directly to ownership and following mechanisms.
- **Related to** [[how-to-follow-a-data-asset]] — following is a prerequisite for receiving announcements.

### Contradictions & Tensions

- **No contradictions** with existing wiki content.
- **Internal tension:** The document states announcements are shown to "all the users who own or follow" the asset, but [[announcements]] describes them as displayed "as banners and in the Activity Feed" without specifying audience scope. This is a gap, not a contradiction.
- **Missing detail:** No mention of whether announcements are visible to users who don't own/follow the asset (e.g., team membe
