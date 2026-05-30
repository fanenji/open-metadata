---
type: source
title: "Source: how-to-request-for-description---openmetadata-docu-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["how-to-request-for-description---openmetadata-docu-20260514.md"]
tags: []
related: []
---

# Source: how-to-request-for-description---openmetadata-docu-20260514.md

## Key Entities

- **OpenMetadata** (platform) — Central entity; the system where description requests and conversations occur.
- **Task** (system object) — Created when a user requests a description update; pre-populated with Title, requires Assignees (users/teams), New description, and shows Current and Difference views.
- **Activity Feeds & Tasks** (UI component) — Tab where created tasks are displayed for the data asset.
- **Assignees** (users/teams) — Recipients of the task who can Accept, Edit and Accept, add Comments, or reassign.
- **Conversation** (system feature) — Threaded discussion around a data asset's description, supporting @mentions (users/teams) and #mentions (data assets), plus Reply, Reactions, Edit, and Delete.

All entities likely already exist in the wiki (e.g., [[openmetadata-collaboration]], [[tag-request-workflow]] for analogous task patterns).

## Key Concepts

- **Description Request Workflow** — Collaborative process where users create a Task to propose a new description for a data asset; used when the user lacks edit permissions or wants review.
- **Conversations around Description** — Threaded discussions initiated from the description field of a data asset, enabling collaborative refinement without formal task creation.
- **Task-based Collaboration** — Pattern where user actions (requests) generate structured Tasks with assignees, status, and resolution options (Accept/Edit and Accept).

These concepts extend the existing [[tag-request-workflow]] pattern to descriptions. They are not yet documented as separate wiki pages but are analogous to existing content.

## Main Arguments & Findings

- **Core claim:** OpenMetadata provides two distinct collaborative mechanisms for managing data asset descriptions: formal Task-based requests and informal Conversations.
- **Evidence:** Procedural documentation with UI screenshots and step-by-step instructions.
- **Strength:** Official documentation from the vendor; high authority but low analytical depth (procedural, not evaluative).

## Connections to Existing Wiki

- **Strengthens** [[openmetadata-collaboration]] — Adds specific workflow details for description management.
- **Extends** [[tag-request-workflow]] — The description request follows the same Task-based pattern as tag requests, confirming a consistent collaboration paradigm.
- **Related to** [[glossary-tags]], [[classification-tags]] — Description management is part of the broader metadata enrichment ecosystem.
- **Related to** [[data-steward-role]] — The request workflow is designed for scenarios where users lack edit permissions, which ties to role-based access control.

## Contradictions & Tensions

- **No contradictions** with existing wiki content.
- **Internal tension:** The document describes two parallel mechanisms (Task request vs. Conversation) but does not explain when to use one over the other, or whether they can be used simultaneously on the same description.
- **Caveat:** The document assumes the use
