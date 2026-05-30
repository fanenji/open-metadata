---
type: concept
title: Tag Request Workflow
created: 2026-05-14
updated: 2026-05-15
tags: [data-governance, collaboration, classification, tags, classification-tags, governance, task, openmetadata, tasks]
related: [classification-tags, data-steward-role, openmetadata-collaboration, conversations-around-classification, how-to-classify-data-assets-official-documentation-20260514, how-to-add-tags-openmetadata-user-tagging-guide, how-to-classify-data-assets-official-documentation, how-to-request-for-tags-official-documentation]
sources: ["how-to-classify-data-assets-official-documentation-20260514.md", "how-to-request-for-classification-tags-official-do-20260514.md", "how-to-request-for-tags-official-documentation---o-20260514.md", "how-to-classify-data-assets-official-documentation-20260514"]
---
# Tag Request Workflow

The Tag Request Workflow is a collaborative governance feature in OpenMetadata that enables users to request additions or changes to [[classification-tags]] on data assets when they lack direct tagging permissions or seek a second opinion. Implemented through the platform's Task system, it supports a governed, review-based approach to data classification rather than relying solely on direct user edits. This workflow facilitates team discussion, review, consensus, and an auditable record of classification change requests.

## Purpose

- **Collaborative governance** — Enables team discussion around how data should be classified and fosters consensus on classification decisions.
- **Review and approval** — Provides a mechanism for [[data-steward-role|Data Stewards]] (or designated reviewers) to evaluate tag requests before they are applied.
- **Auditability** — Creates a persistent record of who requested what changes, the resulting discussion, and the final resolution.
- **Accessible change proposal** — Allows users without direct tag-add permissions to propose tag changes in a structured manner.
- **Structured workflow** — Provides a task-based, step-by-step process for governing classification changes.

## Requesting a Tag Change

### Initiate a Request

1. Navigate to the data asset page (table, topic, dashboard, etc.).
2. Click the **?** icon located next to the tags section. This action opens a pre-populated Task creation form.

### Task Creation Form

The form includes the following fields and interface:

- **Title** — Automatically generated based on the context.
- **Assignees** — One or more users or teams responsible for reviewing the request.
- **Update Tags** — A three-tab interface showing:
  - **Current tags**: The existing classification tags on the asset.
  - **New tags**: The proposed tags to add or change.
  - **Difference**: A delta view comparing the current set of tags with the proposed set.

After configuring the assignees and the proposed tags, click **Submit** to create the task.

### Task Appearance

Once submitted, the task appears in the **Activity Feeds & Tasks** tab for the data asset. It remains visible to all relevant collaborators.

## Review and Resolution

Assignees (and any additional users brought into the workflow) have the following options when reviewing a tag request:

- **Accept the Suggestion** — Approve the proposed tag changes as-is.
- **Edit and Accept the Suggestion** — Modify the proposed tags before approving.
- **Add a Comment** — Provide feedback, ask for clarification, or add context without immediately resolving the request.
- **Add Other Users as Assignees** — Bring additional reviewers into the conversation.

Resolution actions (acceptance or editing) should automatically apply the tag changes to the asset, creating an auditable transcript of the decision.

## Related Concepts

- [[classification-tags]] — The metadata labels that are the subject of the workflow.
- [[conversations-around-classification]] — Threaded discussions that can occur around individual tags, complementing the formal request workflow.
- [[openmetadata-collaboration]] — OpenMetadata’s broader set of native collaboration features (tasks, conversations, etc.).
- [[how-to-classify-data-assets-official-documentation-20260514]] — Guide for directly classifying data assets, the alternative to the request workflow.
- [[how-to-add-tags-openmetadata-user-tagging-guide]] — Direct tag addition workflow for users with appropriate permissions.
- [[how-to-classify-data-assets-official-documentation]] — Broader classification guide covering both direct and request-based approaches.
- [[how-to-request-for-tags-official-documentation]] — Companion documentation for requesting tags.

## Open Questions

- What is the end-to-end flow after review: does approval/rejection automatically apply the tags? Under what conditions?
- Who can approve tag requests? Is approval limited to Data Stewards or is it configurable per asset or team?
- What notifications are generated during the request workflow? Are assignees and requestors notified of status changes?