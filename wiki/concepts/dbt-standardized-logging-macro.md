---
type: concept
title: Standardized dbt Logging Macro
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, logging, macros, debugging, standardization]
related: [dbt-macros, dbt-dispatch-pattern, dbt-jinja-variables, reliable-data-engineering]
sources: ["Standardizing Logging in dbt How We Made Debugging Easier for Everyone.md"]
---
# Standardized dbt Logging Macro

The **standardized dbt logging macro** is a custom macro that overrides dbt's built-in `log` macro to enforce a consistent log format with automatic caller context detection. It was introduced by [[Reliable Data Engineering]] to solve production debugging challenges in growing dbt projects.

## Core Innovation: Caller Context Detection

The macro uses dbt's `context_macro_stack` to inspect the call stack and determine which macro, hook, or materialization invoked the log call. It filters out system noise (e.g., `run_hooks`, `log`) and labels the output accordingly.

## Key Features

- **Macro Override Pattern**: Replaces dbt's built-in `log` macro to enforce adoption without relying on developer discipline.
- **Pre-hook/Post-hook Detection**: Inspects `pre_hooks` and `post_hooks` configurations to label log lines from hooks.
- **Materialization Labeling**: Cleanly labels log lines from materialization macros (e.g., `[materialization][snapshot]`).
- **Structured Output**: Produces log lines like `[pre-hook][generate_schema_name]: Generating bronze schema`.

## Trade-offs

- **Override vs. Rename**: Overriding enforces consistency automatically but is aggressive. Renaming the macro (e.g., `standard_log`) requires developer discipline.
- **Syntax Error**: The published code contains a missing parenthesis in a Jinja conditional, noted in the article's comments.
- **Performance**: Stack inspection may have overhead in large projects with thousands of log calls.

## Connections

- Strengthens [[dbt-macros]] with a concrete advanced use case.
- Contrasts with [[dbt-dispatch-pattern]] — the override approach is an alternative to the dispatch pattern for enforcing standards.
- Uses [[dbt-jinja-variables]] such as `context_macro_stack`, `model.resource_type`, `pre_hooks`, `post_hooks`.

## Open Questions

- How does this macro interact with dbt Cloud's built-in logging and alerting?
- Does overriding `log` break any dbt packages that rely on the default behavior?
- What is the performance overhead of stack inspection in large projects?
