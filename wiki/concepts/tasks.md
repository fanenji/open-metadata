---
type: concept
title: Tasks
created: 2026-05-14
updated: 2026-05-15
tags:
  - openmetadata
  - collaboration
  - tasks
  - workflows
  - metadata-enrichment
related: ["data-collaboration", "activity-feed", "tag-request-workflow", "glossary-terms", "announcements", "conversation-threads", "tasks", "data-asset-ownership", "classification-tags", "bottom-up-top-down-enrichment"]sources:
  - data-collaboration-openmetadata-collaboration-feat-20260514.md
  - create-tasks-openmetadata-collaboration-workflow---20260514.md
---

# Tasks

**Tasks** in OpenMetadata are structured, assignable requests that extend [[conversation-threads]] into a formal, trackable workflow around metadata changes. They enable users to request specific actions on data assets — such as updating descriptions, adding tags, or initiating glossary‑term approval — and ensure those requests are assigned, reviewed, and resolved within the platform.

## Core Concept

Tasks transform free‑form conversations about metadata into actionable, accountable requests. Unlike unstructured discussion, tasks carry a defined purpose (what needs to change), an assignee (often the asset owner), and a resolution path (accept, edit, or reject). This structured approach guarantees that metadata enrichment requests are tracked, assigned to accountable parties, and resolved without falling through the cracks.

## Design Principles

1. **Structured collaboration** – Tasks have a clear goal (description or tag change) and a deterministic resolution workflow, unlike open‑ended conversation threads.
2. **Owner‑centric accountability** – By default, tasks are assigned to the [[data-asset-ownership|owner of the data asset]], reinforcing the ownership model and ensuring the most responsible person is notified.
3. **Top‑down enrichment** – Tasks allow any platform user to drive metadata enrichment from the top down, requesting that owners or stewards add documentation and classification tags. They complement bottom‑up, infrastructure‑driven metadata collection (see [[bottom-up-top-down-enrichment]]).

## Task Types

- **Request for Description** – A task to create or update the description of a data asset.
- **Request for Tags** – A task to request [[classification-tags]] for a data asset. This workflow is detailed in [[tag-request-workflow]].
- **Glossary Term Approval** – A task to initiate an approval workflow for applying [[glossary-terms]] to data assets, extending existing glossary workflows.

## Workflow

1. A user creates a task on a data asset, specifying the type of request and the desired change.
2. The task is assigned to the appropriate user or team (by default, the data owner or steward).
3. The assignee reviews the request and can accept, edit, or reject it.
4. The task is resolved, and the change is applied to the data asset.

## Relationship to Other Features

- **[[activity-feed|Activity Feed]]** – Tasks appear in the Activity Feed, the central UI component for collaboration.
- **[[data-collaboration|Data Collaboration]]** – Tasks are one of the three pillars of Data Collaboration, alongside [[conversation-threads]] and [[announcements]].
- **[[conversation-threads]]** – Tasks are a structured extension of conversation threads, adding task types, assignment, and resolution logic.
- **[[data-asset-ownership]]** – Ownership determines the default task assignee, enforcing accountability.
- **[[classification-tags]]** – The “Request for Tags” task type directly interacts with the classification system.
- **[[tag-request-workflow]]** – The “Request for Tags” task type is documented in detail within this concept.
- **[[glossary-terms]]** – Glossary Term Approval tasks extend glossary workflows with a formal approval step.
- **[[bottom-up-top-down-enrichment]]** – Tasks serve as the primary mechanism for top‑down metadata enrichment, complementing automated, bottom‑up collection.