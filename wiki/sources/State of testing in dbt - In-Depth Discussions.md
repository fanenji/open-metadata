---
type: source
title: "State of testing in dbt - In-Depth Discussions"
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, testing, community, software-testing]
related: [dbt-testing-patterns, dbt-testing-motivation, dbt-mocking-patterns, dbt-smoke-testing, dbt-unit-testing-challenges, dbt-testing-workflow, CI-CD-for-data-pipelines, shift-left-data-quality, dbt-expectations, dbt-anomaly-detection-tests, dbt-data-contract-implementation]
sources: ["State of testing in dbt - In-Depth Discussions.md"]
authors: [boxysean]
year: 2020
url: "https://discourse.getdbt.com/t/state-of-testing-in-dbt/1778"
venue: dbt Community Forum
---
# State of testing in dbt - In-Depth Discussions

A deep-dive by boxysean (dbt Labs) into the state of testing in dbt, published on the dbt Community Forum in November 2020. The post motivates the importance of testing, presents community research on testing practices and challenges, draws conclusions, and makes suggestions for advancing testing in dbt.

## Key Arguments

- dbt's primitive tests (schema tests and data tests) are insufficient for advanced testing needs, leaving a gap that community members are trying to fill.
- Development-time testing in dbt has a high barrier to entry, requiring expert-level knowledge or significant individual time investment.
- There is community demand for capabilities known in software testing (mocking, unit testing, TDD, BDD) that dbt does not natively support.

## Community Research Findings

The post documents six community attempts/descriptions of advanced testing:

- **Petyo Pahunchev**: Identified a gap in deterministic re-creation of conditions; proposed BDD methodology.
- **Michael Kaminsky**: Outlined TDD challenges in ELT, including long pipeline execution times (10+ minutes) and difficulty generating realistic test cases.
- **MichelleArk**: Described difficulties with unit testing in SQL, noting that equality checks feel "unnatural."
- **Fabrice Etanchaud**: Noted that the `--defer` flag may enable automated non-regression testing.
- **Claire**: Successfully used fixed dataset testing with fake data covering edge cases, but noted reproducibility issues.
- **Claus**: Demonstrated running primitive dbt tests as smoke tests in a blue/green deployment pipeline.
- **gnilrets (Sterling)**: Built an external testing framework outside of dbt.

## Suggestions

1. **Product**: Map out the current development-time testing workflow and design an improved workflow.
2. **Technical**: Make mocking a dbt model and source a well-designed, first-class construct in dbt.
3. **Documentation**: Motivate testing in dbt docs, present trade-offs, and promote best practices.

## Connections

This source provides the foundational motivation and community context for [[dbt-testing-patterns]]. It introduces software testing concepts (smoke testing, unit testing, mocking, TDD, BDD) that are relevant to [[CI-CD-for-data-pipelines]] and [[shift-left-data-quality]]. The community's desire for mocking connects to [[dbt-data-contract-implementation]] as a potential enforcement mechanism.
