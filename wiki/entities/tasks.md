---
type: entity
title: Tasks
created: 2026-05-14
updated: 2026-05-15
tags:
  - openmetadata
  - collaboration
  - tasks
  - metadata-enrichment
  - data-collaboration
related:
  - conversation-threads
  - data-asset-ownership
  - classification-tags
  - tag-request-workflow
  - bottom-up-top-down-enrichment
  - how-to-request-for-description
  - how-to-request-for-tags
  - activity-feed
  - data-collaboration
sources:
  - create-tasks-openmetadata-collaboration-workflow---20260514.md
  - request-for-description-official-documentation---o-20260514.md
---
# Tasks

**Tasks** is a collaboration feature in [[OpenMetadata]] that extends [[conversation-threads]] to enable structured, trackable metadata change requests. They are system objects that facilitate formal, review-based workflows around data assets, created when a user requests a change such as a description update or a tag change, requiring assignee review and approval. Tasks provide a formal mechanism for users to request the creation or updating of descriptions and tags, driving [[bottom-up-top-down-enrichment|top-down metadata enrichment]].

## Task Types

Tasks support two distinct types of metadata change requests.

### Request for Description

When a user clicks the "?" icon next to a description field, a Task is created with the following pre-populated fields:

- **Title** — Auto-populated based on the request context
- **Current** — Shows the existing description for comparison
- **New** — Field for the proposed new description
- **Difference** — Auto-generated diff between Current and New descriptions

Users must specify **Assignees** (one or more users or teams) before submitting. By default, the task is assigned to the [[data-asset-ownership|owner]] of the data asset; if the asset has no owner, any appropriate user or team can be selected. The requester may also add additional assignees beyond the default.

Once submitted, the Task appears in the [[activity-feed]] and the Tasks tab for the data asset.

#### Assignee Actions

Assignees can:

- **Accept the Suggestion** — Approve the proposed description as-is
- **Edit and Accept the Suggestion** — Modify the proposed description before approving
- **Add a Comment** — Provide feedback or request changes
- **Add Other Users as Assignees** — Bring in additional reviewers

If accepted, the description is updated on the data asset.

See [[how-to-request-for-description]] for a step-by-step guide.

### Request for Tags

A request to create or update [[classification-tags]] on a data asset. The workflow parallels the description request and uses similar UI elements. For a step-by-step guide, see [[how-to-request-for-tags]] and the [[tag-request-workflow]].

## Assignment Logic

Tasks follow an owner-centric assignment model:

- **Default assignment:** The task is assigned to the [[data-asset-ownership|owner]] of the target data asset.
- **Fallback:** If the data asset has no owner, the task can be assigned to any appropriate user or team.
- **Flexibility:** When creating a task, the user must specify one or more assignees; the default is the owner if one exists, but the requester can modify or add assignees.

This design reinforces the importance of [[data-asset-ownership]] as a foundational governance concept — ownership determines accountability for metadata enrichment requests.

## Relationship to Conversation Threads

Tasks are explicitly defined as an extension of [[conversation-threads]]. While conversation threads provide free-form, threaded discussions around data assets, Tasks add structure by:

- Defining explicit task types (description or tags)
- Implementing a default assignment model based on ownership
- Providing a resolution workflow (create/update the requested metadata)

## Task Lifecycle and UI

Both types of tasks appear in the [[activity-feed]] and a dedicated Tasks tab on the data asset profile. The lifecycle includes:

1. **Creation** — Via the "?" icon for description requests, or through the equivalent tag request interface (see [[how-to-request-for-tags]]).
2. **Assignment** — Default to owner, with optional additional assignees.
3. **Review** — Assignees review the suggestion, add comments, edit, or accept.
4. **Resolution** — If accepted, the requested metadata is applied to the asset. If edited and accepted, the modified suggestion is applied.

The official documentation is brief and does not cover the full task lifecycle.

## Open Questions

The following aspects remain undocumented:

- Can tasks be reassigned after creation?
- What happens when a task is resolved? Is there a notification?
- Are there task statuses (open, in-progress, resolved, rejected)?
- Can tasks be created for entities other than data assets (e.g., glossary terms)?
- How does the task UI differ from the conversation thread UI?

## Related Workflows

- [[how-to-request-for-description]] — Step-by-step guide for description requests
- [[how-to-request-for-tags]] — Parallel workflow for tag change requests
- [[conversation-threads]] — Informal discussions around data assets (distinct from formal Tasks)
- [[tag-request-workflow]] — Overlapping workflow for tag requests