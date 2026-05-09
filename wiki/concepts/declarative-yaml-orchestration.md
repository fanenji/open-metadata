---
type: concept
title: Declarative YAML Orchestration
created: 2024-03-13
updated: 2026-05-07
tags: ["orchestration", "yaml", "workflow", "declarative", "kestra", "devops"]
related: ["kestra", "apache-airflow", "event-driven-orchestration", "data-mesh", "pipeline-blueprints", "elt-pattern"]
sources: ["Kestra vs Airflow (Video).md", "Airlag vs Dagster vs Kestra.md"]
---

# Declarative YAML Orchestration

**Declarative YAML Orchestration** is a paradigm where workflows are defined via configuration files (YAML) rather than imperative programming languages (like Python). This approach is central to [[Kestra]]'s design and represents a significant departure from [[Apache Airflow]]'s Python-first model.

## Key Characteristics

- **Configuration over Code**: Workflows specify *what* to do rather than *how* to do it.
- **Speed of Development**: Pre-defined blocks and plugins allow rapid assembly of workflows.
- **Maintainability**: Reduces "code sprawl" and complexity compared to large-scale Python DAGs.
- **Standardization**: Uses "Pipeline Blueprints" to enable rapid, error-resistant deployment through templated configurations.
- **Lower Barrier to Entry**: Non-engineers (data analysts, domain teams) can read and author workflows without programming knowledge.
- **Self-Service Enablement**: Combined with a strong UI, YAML definitions allow domain teams in a [[data-mesh]] architecture to build pipelines independently.
- **Version Control Friendly**: YAML files are easily diffed, reviewed, and managed in Git-based CI/CD workflows.

## Advantages

- Readable by non-developers.
- Reduces boilerplate compared to Python DAGs.
- Enables in-browser editors with validation and autocompletion.
- Simplifies CI/CD integration (e.g., GitHub Actions, GitLab CI, Terraform provider).

## Limitations

- Complex logic may become unwieldy in YAML.
- Requires strong cloud/DevOps skills for maintenance and optimization.
- May limit highly complex, non-linear logic that requires heavy custom computation.
- Not suitable for teams that prefer code-centric development (see [[Mage]]).

## Related Concepts

- [[event-driven-orchestration]] — Often combined with declarative YAML for real-time pipelines.
- [[data-mesh]] — YAML-based orchestration enables domain teams to self-serve.
- [[elt-pattern]] — Declarative YAML can define both ETL and ELT workflows.
- [[pipeline-blueprints]] — Templated configurations for standardization.