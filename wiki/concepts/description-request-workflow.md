---
type: concept
title: Description Request Workflow
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-collaboration, tasks, descriptions]
related: [tasks, how-to-request-for-description, how-to-request-for-tags, conversation-threads, activity-feed]
sources: ["request-for-description-official-documentation---o-20260514.md"]
---
# Description Request Workflow

The Description Request Workflow is a formal, Task-based collaboration mechanism in OpenMetadata that allows users to propose updates to data asset descriptions and have them reviewed by designated assignees. It is part of the broader [[data-collaboration]] feature set.

## Workflow Steps

1. **Initiation** — A user clicks the "?" icon next to a description field on a data asset page.
2. **Task Creation** — A [[tasks|Task]] is created with pre-populated fields: Title (auto-filled), Current description, New description field, and an auto-generated Difference view.
3. **Assignment** — The user specifies one or more Assignees (users or teams) and submits the Task.
4. **Review** — The Task appears in the [[activity-feed]] and Tasks tab for the data asset. Assignees can:
   - Accept the suggestion as-is
   - Edit and accept the suggestion
   - Add comments
   - Add other users as assignees
5. **Resolution** — Once an assignee accepts or edits and accepts, the description is updated.

## Relationship to Other Features

- **Parallel to Tag Requests** — The workflow mirrors the [[how-to-request-for-tags]] process; both use Tasks for formal review.
- **Distinct from Conversations** — Unlike the formal Task workflow, [[conversation-threads]] around descriptions are informal discussions without a structured review process.
- **UI Integration** — Tasks are displayed in the [[activity-feed]] and Tasks tab, providing visibility across the platform.

## Open Questions

- What are the permission requirements for initiating a description request?
- Can description requests and conversations be linked or merged?
- Is there a notification mechanism for assignees when a description request is created?