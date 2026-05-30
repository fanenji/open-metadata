---
type: concept
title: Evaluation Summary (Permission Debugger)
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, permission-debugger, authorization, diagnostics, metrics]
related: [permission-debugger, authorization-policies, authorization-rules, hybrid-rbac-abac-model]
sources: ["permission-debugger-analyze-and-troubleshoot-user--20260514.md"]
---

# Evaluation Summary (Permission Debugger)

The Evaluation Summary is the quantitative output of the [[permission-debugger|Permission Debugger]] in OpenMetadata. It provides administrators with detailed metrics about the authorization decision process, exposing exactly how many policies and rules were evaluated, how many matched, and the final outcome.

## Metrics

| Metric | Description |
|--------|-------------|
| **Policies Evaluated** | The number of [[authorization-policies]] that were included in the evaluation for the given user, resource, and operation. |
| **Rules Evaluated** | The total count of individual [[authorization-rules]] across all evaluated policies. |
| **Matching Rules** | The subset of evaluated rules whose conditions (including SpEL expressions) matched the user identity, [[resource-attributes]], and requested operation. This is the most critical diagnostic metric. |
| **Allow Rules** | Matching rules with an Effect of `Allow`. |
| **Deny Rules** | Matching rules with an Effect of `Deny`. |
| **Evaluation Time** | The wall-clock time (in milliseconds) required to complete the full evaluation. |

## Interpretation

- **Matching Rules = 0**: No policy rule applies to this user-resource-operation combination. Under the default-deny posture of the [[hybrid-rbac-abac-model]], this results in a DENIED decision.
- **Deny Rules > 0**: At least one matching rule has a Deny effect. Due to Deny precedence in [[authorization-policies]], the decision will be DENIED regardless of Allow rule count.
- **Allow Rules > 0 and Deny Rules = 0**: Access is granted (ALLOWED), provided at least one rule matches.

## Diagnostic Value

The Evaluation Summary is the primary diagnostic output for troubleshooting access issues. A low or zero Matching Rules count indicates that no policy covers the scenario, guiding administrators to create or adjust [[authorization-policies]]. The Evaluation Time metric provides a baseline for performance expectations, though scaling characteristics with larger policy sets remain an open question.