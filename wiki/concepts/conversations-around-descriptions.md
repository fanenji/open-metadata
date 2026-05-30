---
type: concept
title: Conversations Around Descriptions
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-collaboration, conversations, descriptions]
related: [conversation-threads, tasks, how-to-request-for-description, activity-feed]
sources: ["request-for-description-official-documentation---o-20260514.md"]
---
# Conversations Around Descriptions

Conversations Around Descriptions is an informal collaboration feature in OpenMetadata that allows users to initiate threaded discussions directly from the description field of a data asset. It is distinct from the formal [[description-request-workflow]] which uses [[tasks]].

## How It Works

1. **Initiation** — A user clicks the Conversation icon next to a description field on a data asset page.
2. **Discussion** — A threaded conversation starts directly within the data asset page. Users can:
   - Add **@mentions** to tag a user or team
   - Add **#mentions** to tag a data asset
3. **Interaction** — Participants can:
   - Reply to continue the discussion
   - Add Reactions (emojis)
   - Edit their own replies
   - Delete their own replies

## Relationship to Other Features

- **Distinct from Tasks** — Conversations are informal and do not have a structured review/approval workflow. They complement the formal [[description-request-workflow]] by enabling open discussion.
- **Part of Conversation Threads** — This is a specific use case of the broader [[conversation-threads]] feature, scoped to description fields.
- **UI Integration** — Conversations appear in the [[activity-feed]] alongside Tasks and other updates.

## Open Questions

- What are the permission requirements for initiating a conversation vs. a description request?
- Can conversations be escalated or converted into formal Tasks?