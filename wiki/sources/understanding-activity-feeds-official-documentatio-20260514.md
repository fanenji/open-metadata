---
type: source
title: "Source: understanding-activity-feeds-official-documentatio-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["understanding-activity-feeds-official-documentatio-20260514.md"]
tags: []
related: []
---

# Source: understanding-activity-feeds-official-documentatio-20260514.md

## Key Entities

- **Activity Feeds Widget** — Central UI component; displays all activities around owned/followed data assets. Already exists in wiki as [[activity-feed]].
- **OpenMetadata Icon** — UI element used to access the landing page with activity feeds. Peripheral; not in wiki.
- **Users** — Actors who reply, edit, delete, and share reactions. Peripheral; covered by [[teams-and-users]].

## Key Concepts

- **Activity Feeds** — Real-time display of all activities related to data assets a user owns, follows, or is mentioned in. Core collaboration feature. Already exists in wiki as [[activity-feed]].
- **@Mentions** — Filtered view showing only feeds where the user is mentioned. Peripheral; not explicitly in wiki.
- **Tasks** — Filtered view showing open tasks created by or assigned to the user. Already exists in wiki under [[openmetadata-collaboration]] and [[announcements]].
- **Reactions** — Emoji-based feedback mechanism on feed items. Peripheral; not in wiki.

## Main Arguments & Findings

- **Core claim:** Activity Feeds are the central hub for data collaboration, displaying all activities around owned/followed data.
- **Evidence:** Official documentation page; no empirical evidence provided.
- **Strength:** Low — purely descriptive documentation with no supporting data or user studies.

## Connections to Existing Wiki

- Directly relates to [[activity-feed]] — this source provides the official definition and feature description.
- Connects to [[openmetadata-collaboration]] — activity feeds are a core collaboration feature.
- Connects to [[announcements]] — tasks and announcements appear in the activity feed.
- Connects to [[persona-and-landing-page-customization]] — the activity feed is a pluggable panel on the landing page.

## Contradictions & Tensions

- No contradictions with existing wiki content.
- The source describes three feed filters (All, @Mentions, Tasks) but the existing [[activity-feed]] page does not document these filter categories explicitly.
- The source mentions "Reactions" (emojis) which are not documented in the existing wiki.

## Recommendations

- **Update [[activity-feed]]** to include the three filter categories (All, @Mentions, Tasks) and the Reactions feature.
- **Emphasize** that activity feeds are the primary collaboration surface and are accessible from the landing page via the OpenMetadata icon.
- **De-emphasize** — this is a short, high-level overview; no need for a separate page.
- **Open question:** How do activity feeds interact with the Persona system? Does the feed content change based on persona?
