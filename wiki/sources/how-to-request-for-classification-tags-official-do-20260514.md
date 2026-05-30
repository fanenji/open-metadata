---
type: source
title: "How to Request for Classification Tags | Official Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [classification-tags, collaboration, governance, task, conversation]
related: [classification-tags, tag-request-workflow, openmetadata-collaboration, how-to-classify-data-assets-official-documentation-20260514]
sources: ["how-to-request-for-classification-tags-official-do-20260514.md"]
authors: ["OpenMetadata"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/request-tags"
venue: "OpenMetadata Documentation v1.12.x"
---
# How to Request for Classification Tags | Official Documentation

Official procedural guide for requesting classification tag changes and initiating conversations around tags in OpenMetadata v1.12.x. Documents two collaborative governance mechanisms: the tag request workflow (Task-based) and tag-specific conversation threads.

## Tag Request Workflow

Users who lack direct tagging permissions or want a second opinion can request tag changes via a Task:

1. Click the **? icon** next to the tags on a data asset page
2. A Task is created with pre-populated details
3. Fill in assignees (multiple users can be added)
4. The **Update Tags** section displays three tabs:
   - **Current tags** — existing classification
   - **New tags** — proposed changes
   - **Difference** — delta view between current and proposed
5. Click **Submit** to create the task

Once created, the task appears in the **Activity Feeds & Tasks** tab for that data asset. Assignees can:
- **Accept the Suggestion**
- **Edit and Accept the Suggestion**
- **Add a Comment**
- **Add other users as Assignees**

## Conversations around Classification

Users can initiate threaded discussions directly from individual tags:

1. Click the **Conversation icon** next to a tag
2. Start a conversation within the data asset page
3. Use **@mention** to tag a user or team
4. Use **#mention** to tag a data asset
5. Participants can **Reply**, add **Reactions**, **Edit**, or **Delete** messages

This feature extends the broader [[openmetadata-collaboration]] capabilities to the tag level, enabling focused governance discussions.