---
type: concept
title: Python Dependency Management Strategy
created: 2026-05-07
updated: 2026-05-07
tags: [python, dependency-management, docker, kubernetes, best-practices]
related: [container-image-strategy-for-data-pipelines, kubernetes-etl-deployment-strategies, dbt-project-scaffolding, git-friendly-reproducible-python]
sources: ["Venv in Docker_Kubernetes_ Pro e Contro_ .md"]
---
# Python Dependency Management Strategy

A decision framework for managing Python dependencies in containerized environments (Docker/Kubernetes), synthesizing recommendations from the "Venv in Docker/Kubernetes" source.

## Core Decision: Venv in Docker/Kubernetes

### When to Omit Venv
- Simple projects with minimal base images.
- Single application per container (Docker best practice).
- Docker isolation is sufficient for dependency management.
- Goal is maximum simplicity in Dockerfile.

### When to Use Venv
- Complex projects with many dependencies.
- Multi-stage Docker builds for image optimization.
- Need for consistency with local development environments.
- Complex CI/CD environments with multiple tools in build image.
- Adherence to Python conventions is a priority.

## Core Decision: requirements.txt vs pyproject.toml

### Recommended Approach
1. **Define** dependencies in `pyproject.toml` (modern standard per PEP 518/517/621).
2. **Lock** exact versions using a lock file (e.g., `poetry.lock`, `pdm.lock`) generated from `pyproject.toml`.
3. **Install** in Docker using either:
   - The tool's native install command (e.g., `poetry install --no-dev`).
   - An exported, pinned `requirements.txt` (e.g., `poetry export -f requirements.txt`).

### Why pyproject.toml
- Unified project configuration (metadata, build system, dependencies).
- Supports dependency groups (dev, test, production).
- Integrates with modern tools for lock file generation.
- Standardized and future-proof.

### Role of requirements.txt
- Still useful as a generated artifact for `pip install` in Docker.
- Should not be the primary definition source.
- When used, should be pinned and generated from a lock file.

## Open Questions for the Data Platform
1. Which dependency management tool to standardize on (Poetry, PDM, Hatch, pip-tools)?
2. Should venv always be used in Docker images for consistency, or allow per-project decisions?
3. How should lock files be managed in CI/CD — checked into version control or regenerated per build?

## Related Pages
- [[container-image-strategy-for-data-pipelines]] — Design principles for Docker images.
- [[kubernetes-etl-deployment-strategies]] — Deployment strategies on Kubernetes.
- [[dbt-project-scaffolding]] — dbt project structure, relevant for Python dependency choices.
- [[git-friendly-reproducible-python]] — Reproducibility patterns.