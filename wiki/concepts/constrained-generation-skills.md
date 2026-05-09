---
type: concept
title: Constrained Generation (Skills)
created: 2026-05-06
updated: 2026-05-06
tags: [ai, security, prompt-engineering]
related: [arc-kit, architecture-governance]
sources: ["ArcKit — AI Toolkit for Software & Enterprise Architects-20260506.md"]
---
# Constrained Generation (Skills)

**Constrained Generation** is a technique used within the [[arc-kit]] toolkit to ensure the quality and reliability of AI-generated architectural artifacts. In this context, these templates are referred to as **"skills."**

Instead of relying on free-form prompting, which is prone to hallucinations, "skills" restrict the AI's output to predefined, structured Markdown templates. Each skill specifies:
1. **Output Format**: The exact structure the document must follow.
2. **Required Inputs**: The specific context or data needed to populate the template.
3. **Validation Criteria**: Rules to ensure the generated content meets organizational standards.

### Benefits in Architecture
- **Prevention of Hallucinations**: By enforcing a strict structure (e.g., an ADR must have context, decision, and consequences), the AI is prevented from inventing nonexistent context.
- **Traceability**: Skills can enforce a dependency chain, such as requiring an ADR to reference existing [[arc-kit-commands|requirement IDs]].
- **Auditability**: The predictable nature of the output makes it easier for human architects to review and audit the decision-making process.
---END and FILE---

---FILE: wiki/concepts/automated-safety-nets-hooks.md---
---
type: concept
title: Automated Safety Nets (Hooks)
created: 2026-05-06
updated: 2026-05-06
tags: [security, automation, ai-governance]
related: [arc-kit, model-context-protocol]
sources: ["ArcKit — AI Toolkit for Solution & Enterprise Architects-20260506.md"]
---
# Automated Safety Nets (Hooks)

**Automated Safety Nets**, or **"Hooks,"** are local scripts that execute automatically during an AI-driven architectural workflow to enforce security, integrity, and organizational standards.

In the [[arc-kit]] ecosystem, hooks act as a layer of defense-in-depth, intercepting actions before they are finalized or before data is sent to an LLM.

### Types of Hooks

#### 1. Workflow Hooks
These manage the lifecycle of the architectural session:
- **Session Initialization**: Loads project context into the AI's working memory.
- **Context Injection**: Automatically provides state from previous sessions.
- **Filename Enforcement**: Validates that generated artifacts follow organizational naming conventions (e.g., `ARC-ADR-001.md`).
- **Output Validation**: Checks that generated content (like Wardley Map coordinates) is mathematically consistent.

#### 
#### 2. Security Hooks
These protect sensitive information and prevent data leakage:
- **File Protection**: Blocks the AI from writing to sensitive files like `.env` or credential stores using path-based rules, keyword matching, and regex scanning.
- **Secret Detection**: Scans user prompts for API keys, tokens, or passwords *before* they are transmitted to the LLM provider.
- **Secret File Scanning**: Examines the content being written to files to prevent the accidental hardcoding of credentials.

### Importance in Regulated Environments
For organizations in highly regulated sectors (such as the NHS or UK Government), these hooks provide the necessary technical controls to enable the use of LLMs while maintaining compliance with standards like **UK GDPR** and the **NCSC Cyber Assessment Framework**.