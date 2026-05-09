---
type: concept
title: dbt Mocking Patterns
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, testing, mocking, patterns]
related: [dbt-testing-patterns, dbt-unit-testing-challenges, dbt-testing-motivation, dbt-testing-workflow, dbt-data-contract-implementation]
sources: ["State of testing in dbt - In-Depth Discussions.md"]
---
# dbt Mocking Patterns

Mocking is a technique used in unit testing to simulate the behavior of a model or source without requiring real data or external dependencies. In dbt, mocking is particularly challenging because SQL transformations operate on database tables, and there is no built-in mechanism to substitute a model's input with a controlled test dataset.

## The Challenge

Community members have identified mocking as a critical missing capability in dbt:

- **Petyo Pahunchev** noted that there is "no tool to let us deterministically re-create a set of conditions, execute our code and validate the output."
- **MichelleArk** described difficulties with hand-constructing static CSVs and building macros to assert model behavior, noting that "writing assertions for unit tests feels quite unnatural in SQL."
- **jtcohen** described how to mock a dbt model using macros and run-time variables, but this approach requires expert-level dbt knowledge.

## Suggested Approach

The post suggests making "mocking" a dbt model and dbt source a well-designed and first-class construct in dbt. A well-defined approach to mocking would benefit many community members who are currently building ad-hoc solutions.

## Current Workarounds

- **Fixed dataset testing**: Using a curated set of fake data covering all known edge cases (Claire's approach). Works during development but is not easily reproducible.
- **External testing frameworks**: Building testing frameworks outside of dbt (gnilrets' approach).
- **Macro-based mocking**: Using dbt macros and run-time variables to substitute model inputs (jtcohen's approach).

## Connections

Mocking is a key enabler for [[dbt-unit-testing-challenges]] and is closely related to [[dbt-testing-patterns]]. It also connects to [[dbt-data-contract-implementation]] as a potential enforcement mechanism for data contracts during development.
