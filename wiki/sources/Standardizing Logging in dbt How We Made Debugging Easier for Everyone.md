---
type: source
title: "Standardizing Logging in dbt: How We Made Debugging Easier for Everyone"
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, logging, debugging, macros, standardization]
related: [dbt-standardized-logging-macro, dbt-macros, dbt-dispatch-pattern, dbt-jinja-variables, reliable-data-engineering]
sources: ["Standardizing Logging in dbt How We Made Debugging Easier for Everyone.md"]
---
# Standardizing Logging in dbt: How We Made Debugging Easier for Everyone

**Author:** [[Reliable Data Engineering]]
**Published:** 2025-07-11
**URL:** https://medium.com/@reliabledataengineering/standardizing-logging-in-dbt-how-we-made-debugging-easier-for-everyone-f63e459f20d6

## Summary

This article describes a practical solution for standardizing logging in dbt projects by overriding dbt's built-in `log` macro. The author's team faced challenges with inconsistent log formats and lack of caller context as their dbt project grew. The solution is a custom macro that automatically detects the caller context (macro, model, pre-hook, post-hook, or materialization) using dbt's `context_macro_stack` and outputs structured, labeled log lines.

## Key Contributions

- **Macro Override Pattern**: Overriding dbt's built-in `log` macro to enforce standardized logging across the entire project without relying on developer discipline.
- **Caller Context Detection**: Using `context_macro_stack` to identify which macro, hook, or materialization invoked the log call.
- **Pre-hook/Post-hook Detection**: Logic to label log lines as originating from pre-hooks or post-hooks by inspecting hook configurations.
- **Materialization Labeling**: Cleanly labeling log lines from materialization macros.

## Code Example

The macro filters out system noise (e.g., `run_hooks`, `log`), detects the caller, and outputs structured log lines like:
```
10:28:42 [pre-hook][generate_schema_name]: Generating bronze schema
10:28:43 [materialization][snapshot]: Dropping backup snapshot table if exists
```

## Caveats

- The code contains a known syntax error (missing parenthesis in a Jinja conditional), noted in the article's comments.
- The override approach is aggressive; if a team prefers not to override `log`, they must rename the macro and rely on developer discipline.
- The evidence is anecdotal — based on a single team's experience with no quantitative metrics.

## Connections

- Strengthens [[dbt-macros]] with a concrete advanced use case.
- Extends [[dbt-dispatch-pattern]] by presenting an alternative override strategy.
- Uses [[dbt-jinja-variables]] such as `context_macro_stack`, `model.resource_type`, `pre_hooks`, `post_hooks`.
- Related to [[dbt-osmosis]] as both address standardization in dbt projects at different levels.
