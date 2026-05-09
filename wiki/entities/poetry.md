type: entity
title: Poetry
created: 2026-04-08
updated: 2026-04-08
tags: [python, dependency-management, packaging]
related: [pyenv, pyproject-toml]
sources: ["A Modern Geospatial Workflow PyEnv, Poetry, DuckDB, and JuPySQL.md"]
---
# Poetry

**Poetry** is a modern tool for dependency management and packaging in Python. It provides a robust way to manage virtual environments and project dependencies through a single, deterministic configuration file.

### Core Components
- **`pyproject.toml`:** The central configuration file that replaces `requirements.txt` and `setup.py`, defining dependencies, build systems, and project metadata.
- **Deterministic Builds:** Uses a lock file to ensure that every installation of the project uses the exact same versions of all dependencies.
- **Virtual Environment Management:** Automatically creates and manages isolated environments for each project.

Poetry is recommended as a more stable and reproducible alternative to the traditional [[conda]] workflow, especially in complex scientific computing environments.