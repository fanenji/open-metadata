---
type: concept
title: Glossary Approval Workflow
created: 2026-05-14
updated: 2026-05-15
tags:
  - governance
  - glossary
  - approval
  - workflow
  - openmetadata
  - data-governance
related:
  - glossary-tags
  - roles-and-policies
  - data-steward-role
  - glossary-terms
  - glossary-export
  - how-to-add-glossary-terms
sources:
  - "OpenMetadata Community Meeting Oct 2023 Release 1 2 0 datamesh openmetadata.md"
  - "glossary-export-openmetadata-export-guide---openme-20260514.md"
---
# Glossary Approval Workflow

The Glossary Approval Workflow is a governance mechanism introduced in [[OpenMetadata]] 1.2.0 that requires designated reviewers to approve [[glossary-tags|glossary]] terms before they move from draft to approved state. It enables organizations to establish governance controls over glossary term creation and modification, routing changes through a review process where designated approvers can accept or reject proposed changes. The workflow is referenced in conjunction with [[glossary-export|Glossary Export]] and Bulk Import features.

## Purpose

Instead of allowing any user to directly add or edit terms, changes are directed through a review process that ensures glossary terms reflect the consensus of subject matter experts rather than top-down mandates. This supports a shift toward decentralized governance where domain experts control terminology.

## How It Works

1. **Enablement**: An approval workflow is turned on for a glossary by setting reviewers. Without reviewers, terms are created directly in an approved state.
2. **Draft state**: When reviewers are set, any new glossary term is created in draft mode.
3. **Task creation**: A task is automatically created and assigned to the glossary reviewers.
4. **Reviewer-only approval**: Only designated reviewers can approve or reject a term. Even administrators cannot override this — ensuring tight governance control.
5. **Conversation threads**: Reviewers can discuss terms via conversation threads, explaining why a term was rejected or what changes are needed before approval.
6. **Task tracking**: Reviewers can track all pending approval tasks from their personal task list.

## Governance Implications

By preventing administrators from overriding reviewer decisions, the workflow ensures that glossary terms reflect the consensus of subject matter experts. This represents a move toward decentralized, domain-led governance.

## Current Limitations (1.2.0)

- **Draft → Approved only**: The workflow currently covers only the draft-to-approved transition. Other state transitions (approved → deprecated, approved → draft) are not yet covered.
- **Starting point**: The team has indicated this is the beginning of a broader workflow system for governance and is seeking community feedback on additional workflow types.

## Relationship to Other Features

- **[[glossary-tags]]** — The core governance objects linked from the approval workflow.
- **[[glossary-terms]]** — The specific terms within the glossary that undergo approval.
- **[[glossary-export]]** — The export feature for downloading glossary terms as CSV.
- **[[how-to-add-glossary-terms]]** — The bulk import feature for uploading glossary terms via CSV.
- **[[roles-and-policies]]** — Related to access control and permissions for reviewers.
- **[[data-steward-role]]** — The data steward role often serves as a reviewer in the workflow.