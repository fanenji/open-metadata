---
type: concept
title: Containerized Development Environment
created: 2026-03-27
updated: 2026-03-27
tags: [devops, docker, reproducibility]
related: [dbt-workflow, dbt-creator, dbt-osmosis]
sources: ["Ambiente sviluppo su Container.md"]
---
# Containerized Development Environment

A **Containerized Development Environment** is a "VM-like" workspace encapsulated within a Docker container. Its primary goal is to provide a consistent, reproducible, and portable environment for all developers, eliminating the "works on my machine" phenomenon.

## Key Characteristics
- **Consistency**: Every developer uses an identical Docker image containing specific versions of Python (3.12), dbt, and essential tools.
- **Integrated Tooling**: The environment comes pre-configured with IDEs (Code-server/VSCode, Jupyter) and access to data services (Dremio, OpenMetadata).
- **Portability**: The environment is designed to run locally on developer machines via Docker Compose but is architected to be migrated to a centralized, on-demand Kubernetes (RKE2) infrastructure using a Jupyter proxy.
- **Persistence**: Uses bind mounts to ensure that development work performed within the container is persisted on the host machine's disk.

## Architecture
The environment acts as a client to various on-prem and cloud-native services:
- **GitLab**: Servs as the VCS and package registry.
- **Dremio**: Acts as the primary data source and sink.
- **Ollama**: Provides LLM capabilities via API.