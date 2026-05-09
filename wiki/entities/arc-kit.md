---
type: entity
title: ArcKit
created: 2026-03-15
updated: 2026-03-15
tags: [toolkit, ai, architecture, governance]
related: [claude-code, architecture-decision-records, model-context-modeling-mcp]
sources: ["ArcKit — AI Toolkit for Solution & Enterprise Architects.md"]
---
# ArcKit

**ArcKit** is an open-source (MIT licensed) Enterprise Architecture Governance toolkit designed to automate the creation of architectural artifacts. It operates primarily as a plugin for AI coding assistants, most notably **Claude Code**.

## Core Functionality
ArcKit provides over 50 AI-assisted slash commands that generate structured governance artifacts, including:
- **Requirements Documents**: Functional, non-functional, data, and integration requirements.
- **Architecture Decision Records (ADRs)**: Context, alternatives, decisions, and consequences.
- **Compliance Assessments**: Specifically tailored for UK Government standards (e.g., TCoP, Secure by Design, GDPR).
- **Strategic Artifacts**: Wardley Maps, vendor evaluations, and procurement documents (RFP, SOW).

## Technical Implementation
- **Skills**: Implemented as structured Markdown templates that constrain AI generation to ensure predictable, auditable outputs.
- **Hooks**: Automated scripts that execute locally to provide security (secret detection, file protection) and validation (output consistency).
- **Integration**: Works with Claude Code, Google Gemini CLI, OpenAI Codex CLI, and OpenCode CLI.
- **Security Model**: Supports "defense in depth" via local execution of safety hooks and can be configured with **AWS Bedrock** for zero-retention, highly regulated environments.

## Role in the AI Stack
ArcKit facilitates **knowledge compounding** by producing machine-readable, structured Markdown files that serve as an organizational memory, allowing future AI agents to reference past decisions and requirements.