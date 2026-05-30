---
type: concept
title: Audit Logs
created: 2026-05-14
updated: 2026-05-14
tags: [administration, security, compliance, logging]
related: [openmetadata-administration, roles-and-policies]
sources: ["admin-guide-openmetadata-administration-documentat-20260514.md"]
---
# Audit Logs

Audit Logs provide a record of platform activities for compliance and security review. They enable accountability and traceability by capturing who did what and when within the OpenMetadata platform.

## Purpose

- **Compliance** — Demonstrate adherence to regulatory requirements by maintaining an immutable activity record.
- **Security** — Detect unauthorized access attempts or suspicious behavior.
- **Troubleshooting** — Investigate changes that may have led to data issues or misconfigurations.

## Scope

The documentation indicates that Audit Logs are an administrative tool, suggesting that access to audit records is restricted to users with the Administrator role.

## Open Questions

- What specific events are logged (e.g., login attempts, metadata changes, permission modifications)?
- What is the retention policy for audit logs?
- Are audit logs stored in the metadata database, Elasticsearch, or a separate system?
- Can audit logs be exported or forwarded to external SIEM systems?