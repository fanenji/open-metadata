---
type: source
title: Ambiente sviluppo su Container
created: 2026-03-27
updated: 2026-03-27
tags: [development, docker, dbt, infrastructure]
authors: [S. Parodi]
year: 2026
url: ""
venue: ""
sources: ["Ambiente sviluppo su Container.md"]
---
# Ambiente sviluppo su Container

This source document describes the implementation and workflow of a containerized development environment designed for consistent Python and dbt development.

## Core Components
The environment is encapsulated in a Docker container and includes:
- **IDEs**: Jupyter and Code-server (VSCode in browser).
- **Data Frameworks**: dbt (Data Build Tool).
- **Data Sources/Sinks**: Dremio.
- **Metadata Management**: OpenMetadata.
- **Orchestration**: Kestra.
- **AI Capabilities**: Ollama server.
- **Version Control**: GitLab (used for package repositories and VCS).

## Development Workflow
The environment follows a standardized lifecycle:
1. **Bootstrap**: Using `dbt-creator` to initialize new dbt projects from templates.
2. **Development**: Coding within the containerized VSCode/Jupyter interface.
3. **Automated Pipeline (`dbt-workflow`)**:
   - Pulling repositories.
   - Installing dependencies (`dbt deps`).
   - Running transformations (`dbt build`).
   - Refactoring YAML via `dbt-osmosis`.
   - Generating documentation.
   - Running `pre-commit` checks.
   - Injecting metadata into OpenMetadata.
   - Committing and pushing changes to GitLab.

## Infrastructure Strategy
The architecture is designed to be portable, running locally via Docker Compose but prepared for future migration to a managed Jupyter proxy environment on a private Kubernetes (RKE2) infrastructure.