---
type: concept
title: How to Request for Description
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-collaboration, tasks, descriptions, how-to]
related: [tasks, description-request-workflow, how-to-request-for-tags, conversation-threads, activity-feed, conversations-around-descriptions]
sources: ["request-for-description-official-documentation---o-20260514.md"]
---
# How to Request for Description

This page documents the step-by-step procedure for requesting a description update on a data asset in OpenMetadata v1.12.x. It mirrors the parallel [[how-to-request-for-tags]] workflow.

## Prerequisites

- Access to a data asset with a description field
- (Optional) A user or team to assign as reviewer

## Procedure

### Requesting a Description Update

1. Navigate to the data asset page.
2. Click the **? icon** next to the Description field.
3. A [[tasks|Task]] creation dialog opens with pre-populated fields:
   - **Title** — Auto-populated (e.g., "Update Description for [Asset Name]")
   - **Current** — Shows the existing description for reference
   - **New** — Enter the proposed new description
   - **Difference** — Auto-generated diff between Current and New
4. **Assignees** — Select one or more users or teams to review the request.
5. Click **Submit** to create the Task.

### After Submission

- The Task appears in the [[activity-feed]] and Tasks tab for the data asset.
- Assignees can:
  - **Accept the Suggestion** — Approve the proposed description
  - **Edit and Accept the Suggestion** — Modify before approving
  - **Add a Comment** — Provide feedback
  - **Add Other Users as Assignees** — Bring in additional reviewers

### Starting a Conversation (Alternative)

Instead of a formal request, users can start an informal threaded discussion:

1. Click the **Conversation icon** next to the description.
2. Type a message, using **@mention** to tag users/teams or **#mention** to tag data assets.
3. Participants can reply, add reactions, edit, or delete replies.

See [[conversations-around-descriptions]] for more details.

## Related Pages

- [[how-to-request-for-tags]] — Parallel workflow for tag change requests
- [[tasks]] — Task system in OpenMetadata
- [[conversation-threads]] — General conversation feature
- [[description-request-workflow]] — Conceptual overview of the workflow