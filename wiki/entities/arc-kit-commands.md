---
type: entity
title: ArcKit Commands
created: 2026-05-06
updated: 2026-05-06
tags: [automation, ai-commands, architecture-governance]
related: [arc-kit, architecture-governance]
sources: ["ArcKit — AI Toolkit for Solution & Enterprise Architects-20260506.md"]
---
# ArcKit Commands

**ArcKit Commands** refer to the suite of over 50 AI-assisted slash commands provided by the [[arc-kit]] toolkit. These commands are implemented as "skills"—structured Markdown templates that guide AI assistants to produce predictable, auditable governance artifacts.

### Key Command Categories

#### Governance Artifacts
- `/arckit:principles`: Defines architecture principles.
- `/arckit:requirements`: Generates functional, non-functional, data, and integration requirements.
- `/arckit:adr`: Generates a structured Architecture Decision Record (ADR).
- `/arckit:data-model`: Creates a data model including a GDPR matrix.
- `/arckit:diagram`: Generates architecture diagrams.

#### UK Government Compliance
- `/arckit:tcop`: Assesses against the 13 points of the Technology Code of Practice.
- `/arckit:secure`: Generates Secure by Design assessments (NCSC CAF, Cyber Essentials, UK GDPR).
- `/arckit:dpia`: Generates a Data Protection Impact Assessment.
- `/arckit:ai-playbook`: Evaluates against the UK Government AI Playbook and ATRS.
- `/arckit:sobc`: Generates a Strategic Outline Business Case (HM Treasury Green Book).
- `/rag:risk`: Generates a risk register (HM Treasury Orange Book).

#### Research & Procurement
- `/arckit:research`: Performs technology evaluation via web search.
- `/arckit:vendor`: Conducts vendor capability evaluations.
- `/arckit:rfp`: Generates a Request for Proposal.
- `/arckit:sow`: Generates a Statement of Work.

### Operational Mechanics
The commands rely on a **dependency chain**; for example, an ADR command expects previously generated requirements to exist so it can reference specific Requirement IDs, ensuring traceability.