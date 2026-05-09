---
type: source
title: dbt-osmosis Synthesize Testing Notes
created: 2026-03-10
updated: 2026-03-10
tags: [dbt, dbt-osmosis, llm, documentation, schema]
related: [dbt-osmosis, dbt-llm-documentation-generation, dbt-schema-synchronization, dbt-osmosis-llm-module, dbt-osmosis-benchmarking, dbt-osmosis-custom-prompt-guide]
sources: ["dbt-osmosis synthetize.md"]
---
# dbt-osmosis Synthesize Testing Notes

Internal project notes documenting practical testing of the `dbt-osmosis yaml refactor --synthesize` command for automated schema YAML documentation generation. The testing was performed on the `demo_dremio` dbt project using a customized fork of dbt-osmosis version 1.2.2 hosted on a GitLab instance.

## Key Findings

- The `--synthesize` command successfully auto-generates table and column descriptions from SQL model definitions.
- Generated descriptions are in English and preserve any existing manually written descriptions.
- Quality of generated descriptions degrades when processing many models simultaneously; generating fewer descriptions yields better, more detailed results.
- Two LLM backends were tested successfully: Ollama (http://10.11.9.76:11434/v1) and LM Studio (http://127.0.0.1:1234/v1), both via OpenAI-compatible API endpoints.

## Customization Gaps Identified

- No support for Italian language descriptions.
- No custom prompt management interface.
- Insufficient detail in generated descriptions for production use.

## TODO Items

- Implement custom prompt management.
- Enable Italian language descriptions.
- Increase detail level in generated descriptions.
- Document the processing flow of the `llm.py` module.
- Create a benchmarking script to produce summary tables from test runs.
- Test additional LLM models.
- Evaluate dedicated models for different documentation tasks (see [[Model Suggestions for llm.py]]).

## Related Resources

- Official documentation: https://z3z1ma.github.io/dbt-osmosis/
- GitLab fork: https://gitlab-test.dataliguria.it/data-platform/dbt/dbt-osmosis-1.2.2
- Model suggestions: [[Model Suggestions for llm.py]]