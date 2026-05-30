---
type: source
title: "Source: how-to-request-for-tags---openmetadata-documentati-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["how-to-request-for-tags---openmetadata-documentati-20260514.md"]
tags: []
related: []
---

# Source: how-to-request-for-tags---openmetadata-documentati-20260514.md

## Analysis of: how-to-request-for-tags---openmetadata-documentati-20260514.md

### Key Entities

| Name | Type | Role | In Wiki? |
|------|------|------|----------|
| Tags | Concept | Central (the object of requests) | Yes ([[classification-tags]]) |
| Task | Feature | Central (mechanism for requesting) | Yes (mentioned in [[tag-request-workflow]]) |
| Activity Feeds | UI Component | Central (displays tasks) | Yes ([[activity-feed]]) |
| Conversation Threads | Feature | Central (around tags) | Yes ([[conversation-threads]], [[conversations-around-classification]]) |
| Assignees | Role/Concept | Central (users who review/accept requests) | Implicit in [[tag-request-workflow]] |
| @mentions / #mentions | Feature | Peripheral (in conversations) | Yes ([[conversations-around-classification]]) |

### Key Concepts

| Name | Definition | Why It Matters | In Wiki? |
|------|------------|----------------|----------|
| Tag Request Workflow | Process where a user creates a Task to propose tag changes on a data asset, which assignees can Accept or Edit & Accept | Core collaborative governance mechanism; enables users without direct tag permissions to propose changes | Yes ([[tag-request-workflow]]) |
| Conversations around Tags | Threaded discussions initiated from individual tags on data assets | Enables contextual collaboration directly on the data asset page | Yes ([[conversations-around-classification]]) |
| Task-based Tag Update | A Task with three tabs (Current, New, Difference) for reviewing tag changes | Provides structured review workflow with diff visualization | Yes ([[tag-request-workflow]]) |

### Main Arguments & Findings

- **Core claim**: Users can request tag updates via Tasks when they need a second opinion or lack direct tag permissions.
- **Evidence**: Procedural documentation with step-by-step instructions.
- **Strength**: Official documentation; authoritative but procedural (not empirical).

### Connections to Existing Wiki

- **Strengthens**: [[tag-request-workflow]] — provides the exact UI procedure (click ? icon, fill assignees, three-tab interface, Submit).
- **Extends**: [[classification-tags]] — adds the request workflow as a method for applying tags.
- **Related**: [[activity-feed]], [[conversation-threads]], [[conversations-around-classification]] — all referenced as the context where tasks and conversations appear.

### Contradictions & Tensions

- **Internal**: The document mentions "Conversations around Tags" as a separate feature from "Request for Tags," but both use the same UI (clicking icons next to tags). The distinction between a Task (request) and a Conversation (discussion) is clear but could be confusing to users.
- **No conflicts** with existing wiki content.

### Recommendations

- **Create/Update pages**:
  - Update [[tag-request-workflow]] to include the exact UI steps (click ? icon, three-tab interface, Accept/Edit & Accept).
  - Update [[conversations-around-classification]] to include the Conversation icon cl
