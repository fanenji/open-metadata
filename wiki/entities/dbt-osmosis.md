---
type: entity
title: dbt-osmosis
created: 2026-03-27
updated: 2026-05-07
tags:
  - automation
  - dbt
  - refactoring
  - schema-management
  - documentation
  - governance
  - open-source
  - dbt-osmosis
  - schema-synchronization
  - documentation-generation
  - llm
related: ["dbt-workflow", "software-defined-assets", "dbt-schema-synchronization", "dbt-pre-commit-patterns", "dbt-project-scaffolding", "dbt-data-contract-implementation", "dbt-llm-documentation-generation", "dbt-osmosis-llm-module", "dbt-osmosis-custom-prompt-guide", "dbt-osmosis-benchmarking", "dbt"]sources:
  - "Ambiente sviluppo su Container.md"
  - "dbt-osmosis Automation for Schema and Documentation Management in dbt.md"
  - "DBT-OSMOSIS.md"
---
# dbt-osmosis

dbt-osmosis is an open-source utility designed for automated refactoring and synthesis of YAML configurations within dbt projects. It automates schema YAML synchronization, documentation generation, and governance enforcement, filling the automation gap between dbt core (modeling/testing) and IDE plugins (developer productivity) by making documentation a code lifecycle concern. It provides a command-line interface (`dbt-osmosis yaml refactor`) that synchronizes YAML schema files with the actual warehouse schema and can optionally generate documentation using a configured LLM provider.

## Key Features

- **Schema Synchronization**: Automated two-way sync between warehouse schema and dbt YAML files via `dbt-osmosis yaml refactor`.
- **Documentation Generation**: Automatic creation of column stubs, placeholder descriptions, and upstream description inheritance.
- **LLM-Powered Documentation Generation**: Automated documentation synthesis using a large language model, triggered via the `--synthesize` flag.
- **Interactive Workbench**: CLI tool for running SQL/Jinja within dbt context without full `dbt run`.
- **pre-commit Integration**: Enforces YAML consistency as a repo policy via the `dbt-osmosis-yaml` hook.

## Usage

### Correct Execution Order

To properly update YAML and documentation after modifying SQL models, run the following commands in order:

```bash
dbt build
dbt docs generate
dbt-osmosis yaml refactor
```

Running `dbt-osmosis yaml refactor` alone after modifying SQL will **not** update documentation.

### LLM-Powered Documentation Generation

The `--synthesize` flag enables automatic documentation generation using a configured LLM provider:

```bash
dbt-osmosis yaml refactor --synthesize
```

Configuration is done via environment variables (see [[dbt-osmosis-llm-module]] for details). For benchmarking plans, see [[dbt-osmosis-benchmarking]].

### Custom Prompt

A custom prompt file can be used to guide the LLM's behavior. See [[dbt-osmosis-custom-prompt-guide]].

## Configuration

In `dbt_project.yml`:

```yaml
models:
  test_osmosis_ste:
    +dbt-osmosis: "_{model}.yml"
    space_test_osmosis_ste:
      ...
vars:
  dbt-osmosis:
    sources:
      rete:
        path: "space_test_osmosis_ste/Source/source_table.yml"
```

## Installation

```bash
pip install dbt-osmosis dbt-dremio==1.10
```

For LLM synthesis support:

```bash
pip install "dbt-osmosis[openai]"
```

## Comparison with IDE Plugins

| Tool | Strength | Limitation |
|------|----------|------------|
| dbt VS Code Extension (official) | IntelliSense, live error checking, refactoring of ref() | Doesn't manage YAML or docs |
| dbt Power User (community) | Navigation, snippets, lineage, query execution | Doesn't enforce schema consistency |
| dbt-osmosis | Sync, auto-docs, CI/CD, workbench | Doesn't provide IDE autocompletion |

## Use Cases

- Large teams requiring automated schema consistency
- Legacy projects needing YAML bootstrapping
- Regulated industries needing automated documentation enforcement
- Mature data cultures treating documentation as a living asset

## Strategic Positioning

dbt-osmosis serves as a key component of the [[dbt-workflow]] pipeline, ensuring that metadata and properties are correctly applied across the project. In the context of [[software-defined-assets]], it helps maintain clean and synchronized configuration files by automating the "synthesis" of YAML properties. The tool is positioned as the third pillar of the dbt ecosystem: dbt core for modeling/testing, IDE extensions for developer productivity, and dbt-osmosis for governance and documentation automation.

## Known Issues

- **UI/Interaction Bug**: The 'y' confirmation prompt does not appear during certain interactive sessions.
- **Potential Conflicting Behaviors**: dbt-osmosis may conflict with dbt's native [[dbt-data-contract-implementation]] when both modify YAML files simultaneously.
- **Column Type Inference**: The tool does not infer column types from warehouse metadata (raised in community responses).
- **Version Conflict Handling**: The recommended approach for handling version conflicts in multi-developer environments is not documented.
- **data_type Bug (v1.14)**: Column data types are not populated due to a bug introduced in version 1.14. A fix is available in the internal GitLab repository at `https://10.11.9.20/data-platform/dbt/models/dbt-osmosis` (branch `fix/data_type`).
- **Column Comments Not Captured**: dbt-osmosis does not read existing column comments from the database. This is a limitation of the underlying database (e.g., Dremio does not expose column comments).

## Related

- [[dbt-osmosis-llm-module]]
- [[dbt-osmosis-custom-prompt-guide]]
- [[dbt-osmosis-benchmarking]]
- [[dbt-schema-synchronization]]
- [[dbt-project-scaffolding]]
- [[dbt-llm-documentation-generation]]