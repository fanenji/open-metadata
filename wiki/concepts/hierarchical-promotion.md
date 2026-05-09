type: concept
title: Hierarchical Promotion
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, git, branching-strategy]
related: [indirect-promotion, direct-promotion, dbt-git-branching-strategies]
sources: ["getting-started-with-git-branching-strategies-and-dbt.md"]
---
# Hierarchical Promotion

**Hierarchical Promotion** is the most common form of [[indirect-promotion]]. It is a branching strategy where branches derive from and merge back in the same order. For example:

1. A middle branch (e.g., `qa`) is derived from `main`.
2. Feature branches derive from the middle branch.
3. Feature branches merge back to the middle branch.
4. The middle branch merges back to `main`.

This structure creates a clear hierarchy of code promotion: `feature` → `qa` → `main`. It is the simplest form of indirect promotion and the one most commonly implemented in indirect workflows.