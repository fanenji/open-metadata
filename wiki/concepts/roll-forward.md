---
type: concept
title: Roll-Forward
created: 2026-05-08
updated: 2026-05-08
tags: [roll-forward, deployment, recovery, ci-cd, database-migrations]
related: [rollback, feature-toggles, error-recovery-mechanisms, ci-cd-rollback-strategies]
sources: ["research-error-recovery-mechanisms-2026-05-08.md"]
---
# Roll-Forward

Fixing a failure by deploying a new, corrected version of code or transformations rather than reverting to an old one. Common in fast CI/CD cycles where a fix commit is rapidly promoted through the pipeline.

## Advantages

- Avoids schema state complexity associated with down-migrations.
- Aligns with forward-only migration philosophies.
- Keeps deployment history linear and auditable.

## Trade-offs

- Requires teams to always be able to deploy a fix quickly — not always realistic.
- May be slower than a feature flag toggle for immediate recovery.
