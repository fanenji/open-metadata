---
type: concept
title: Maintainability Definition
created: 2026-04-29
updated: 2026-04-29
tags: [maintainability, software-engineering, architecture]
related: [reliability-definition, scalability-definition]
sources: ["Designing Data-intensive Applications with Martin Kleppmann.md"]
---
# Maintainability Definition

Maintainability is the third pillar of DDIA's framework (alongside reliability and scalability). It refers to the ease with which a system can be operated, evolved, and understood over its lifetime.

## Key Aspects

- **Operability**: Making it easy for operations teams to keep the system running.
- **Simplicity**: Reducing complexity to make the system easier to understand and modify.
- **Evolvability**: Making it easy to change the system in response to new requirements.

## Relevance to Data Platform

Maintainability is a critical concern for the Data Platform, especially as it grows in complexity. Practices like [[dbt-project-scaffolding]], [[CI-CD-for-data-pipelines]], and [[data-contract-platform]] all contribute to maintainability.
