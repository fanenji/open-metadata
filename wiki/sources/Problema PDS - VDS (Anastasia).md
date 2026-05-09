---
type: source
title: "Problema PDS - VDS (Anastasia)"
created: 2026-01-30
updated: 2026-01-30
tags: [data-quality, ci-cd, problem-statement]
related: [source-downstream-validation-gap, dual-pipeline-strategy, rollback-on-error-strategy, branch-based-ingestion-pattern, shift-left-data-quality, ci-cd-for-data-pipelines]
sources: ["Problema PDS - VDS (Anastasia).md"]
---
# Problema PDS - VDS (Anastasia)

A brief problem statement and solution brainstorm document from the Data Platform project. It identifies a critical gap where modifications to a Primary Data Source (PDS) pass source-level tests but break downstream View/Data Sources (VDS). Three operational solutions are proposed: a dual pipeline (stage/prod), rollback to last valid tag on error, and branch-based ingestion isolation. The document itself questions the severity of the problem, noting "Study the problem. Is it really important?"

## Key Points

- **Core Problem:** Problematic modifications to the PDS are not blocked by source-level tests, causing downstream VDS to break.
- **Proposed Solutions:**
  1. **Dual Pipeline (Stage/Prod):** Run two parallel pipelines; promote to prod only if stage passes.
  2. **Rollback on Error:** Revert VDS to the last valid tag when errors occur.
  3. **Branch-Based Ingestion:** Isolate PDS changes on an "ingestion" branch, merging to main only after validation.
- **Open Question:** The document explicitly flags uncertainty about the problem's real-world importance.

## Connections

- [[source-downstream-validation-gap]] — The core failure pattern documented here.
- [[dual-pipeline-strategy]] — Solution 1: stage/prod dual pipeline.
- [[rollback-on-error-strategy]] — Solution 2: rollback to last valid tag.
- [[branch-based-ingestion-pattern]] — Solution 3: ingestion branch isolation.
- [[shift-left-data-quality]] — This problem is a caveat to shift-left: source tests alone are insufficient.
- [[CI-CD-for-data-pipelines]] — These solutions are operational CI/CD tactics.