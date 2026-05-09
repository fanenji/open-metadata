---
type: entity
title: fal-tool
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, python, slack, alerting]
related: [dbt, slack, data-quality-resolution-workflow]
sources: ["Modern data warehouse modeling and ensuring data quality with dbt and OpenMetadata.md"]
---
# fal-tool

A tool that enables running Python scripts within dbt projects. In the context of the modern data warehouse guide, `fal` is used to execute a Slack bot script that sends alert messages about dbt model status (success/failure) to a Slack channel.

## Usage Pattern

1. Install `dbt-fal` library.
2. Write a Python script (e.g., `slack_bot.py`) that uses the Slack SDK to post messages.
3. Declare the fal script in the dbt schema YAML file under the model's `meta.fal.scripts` key.
4. Run `dbt-fal run` to execute the Python script alongside dbt models.

## Related Wiki Pages

- [[dbt]] — The transformation tool that fal extends.
- [[data-quality-resolution-workflow]] — Alerting is part of the resolution workflow.