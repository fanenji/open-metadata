---
type: concept
title: LLM-Generated dbt Tests
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, llm, data-quality, testing, automation]
related: [dbt-testing-patterns, ai-copilot-for-data-engineering, dbt-osmosis-llm-module, dbt-expectations, data-quality-dimensions]
sources: ["Integrating LLMs and AI Agents into Data Engineering Workflows 1.md"]
---
# LLM-Generated dbt Tests

LLM-Generated dbt Tests is a pattern where Large Language Models are used to automatically produce dbt test YAML files from natural language descriptions. Instead of manually writing boilerplate test configurations, data engineers describe the desired quality checks in plain English, and an LLM generates the corresponding YAML.

## Example

A prompt like "Generate a dbt data test to check if 'customer_id' column in 'orders' table is never null and amounts are always greater than zero" produces:

```yaml
version: 2

models:
  - name: orders
    columns:
      - name: customer_id
        tests:
          - not_null
      - name: amount
        tests:
          - dbt_utils.expression_is_true:
              expression: "amount > 0"
```

## Implementation

The article by [[Ritam Mukherjee]] demonstrates using the OpenAI API (GPT-4o) to generate the YAML, save it to a file, and run `dbt test` via subprocess.

## Limitations vs. Existing Approaches

- **Simplicity**: Generated tests are basic (not_null, expression_is_true) compared to the 60+ sophisticated tests in [[dbt-expectations]]
- **Hallucination Risk**: LLMs may generate incorrect or non-functional test configurations
- **Human Review Required**: All generated tests must be reviewed before deployment
- **No Production Validation**: The approach has not been validated at scale

## Connections to Existing Wiki

- Extends [[dbt-testing-patterns]] with an LLM-assisted generation layer
- Related to [[dbt-osmosis-llm-module]] which provides a more integrated LLM-powered documentation generation approach
- Complements [[dbt-expectations]] by automating the creation of simpler tests
- Targets specific [[data-quality-dimensions]] based on the prompt