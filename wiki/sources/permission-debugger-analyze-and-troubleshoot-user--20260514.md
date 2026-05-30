---
type: source
title: "Permission Debugger: Analyze and Troubleshoot User Access"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, permission-debugger, authorization, rbac, abac, administration]
related: [permission-debugger, hybrid-rbac-abac-model, authorization-rules, authorization-policies, resource-attributes, viewbasic-viewall-operations, roles-and-policies, audit-logs]
sources: ["permission-debugger-analyze-and-troubleshoot-user--20260514.md"]
authors: ["OpenMetadata Documentation"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/permission-debugger"
venue: "OpenMetadata Official Documentation v1.12.x"
---

# Permission Debugger: Analyze and Troubleshoot User Access

Official documentation for the Permission Debugger feature in OpenMetadata v1.12.x. This source provides the definitive procedural guide for using the diagnostic UI tool that simulates permission checks for a given user on a selected resource and operation.

## Key Content

- **Navigation path**: Settings > Access Control > Permission Debugger
- **Three-step workflow**: Select User → Define Permission Check (Resource, Operation, optional Resource FQN) → Evaluate
- **Full resource type enumeration**: user, team, table, database, glossary, tag, glossaryTerm, searchIndex, mlModel, container, topic, pipeline, dashboard, databaseSchema
- **Operation examples**: ViewAll, EditAll, Deploy, Trigger, Kill, GenerateToken
- **Two worked examples** demonstrating the contrast between DENIED (EditAll, 0 matching rules) and ALLOWED (ViewAll, 1,046 matching rules) for the same user and resource
- **Evaluation Summary metrics**: Policies Evaluated, Rules Evaluated, Matching Rules, Allow Rules, Deny Rules, Evaluation Time
- **Use cases**: debugging permission issues, validating new policies, understanding access decisions