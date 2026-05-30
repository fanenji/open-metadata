---
type: concept
title: Conversations around Classification
created: 2026-05-14
updated: 2026-05-15
tags: [classification-tags, collaboration, conversation, activity-feed, openmetadata, tags, classification, conversations]
related: [classification-tags, tag-request-workflow, openmetadata-collaboration, how-to-request-for-tags-official-documentation]
sources:
  - "how-to-request-for-classification-tags-official-do-20260514.md"
  - "how-to-request-for-tags-official-documentation---o-20260514.md"
---

# Conversations around Classification

Conversations around Classification is a feature in OpenMetadata that enables threaded discussions directly on individual [[classification-tags]] assigned to data assets. It provides a lightweight collaboration mechanism for discussing tag assignments, classifications, and governance decisions in context, extending the platform’s [[openmetadata-collaboration]] capabilities to the tag level.

## Starting a Conversation

1. Navigate to a data asset page and locate a classification tag.
2. Click the **Conversation icon** displayed next to the tag.
3. A conversation thread opens directly within the data asset page.
4. Use **@mention** to tag a specific user or team.
5. Use **#mention** to reference another data asset by name.

## Conversation Capabilities

Within a tag conversation, participants can:

- **@mention** – notify a user or team
- **#mention** – reference a data asset
- **Reply** – continue the discussion thread
- **React** – add emoji reactions to messages
- **Edit** – modify previously posted messages
- **Delete** – remove messages from the thread

## Purpose and Relationship to Tag Requests

Conversations around Classification serve as an open-ended discussion mechanism suited for:

- Debating the appropriateness of existing tags
- Discussing governance standards before formal requests
- Collaborative decision-making without immediate action
- Contextual discussion around specific tag assignments

This contrasts with the formal [[tag-request-workflow]], which is a structured, Task-based process for proposing and approving tag changes. Both features complement direct tag application and together form the collaborative governance layer of OpenMetadata's classification system.

## Related Concepts

- [[classification-tags]] – the metadata labels being discussed
- [[tag-request-workflow]] – formal workflow for requesting tag changes
- [[openmetadata-collaboration]] – broader collaboration features in OpenMetadata