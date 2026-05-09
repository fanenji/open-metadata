---
type: entity
title: Nessie CLI (pynessie)
created: 2026-05-07
updated: 2026-05-07
tags: [nessie, cli, data-lakehouse, catalog-versioning]
related: [nessie-catalog-versioning, nessie-spark-integration, data-lakehouse-versioning-strategies]
sources: ["Dremio Open Source Explore Nessie.md"]
---
# Nessie CLI (pynessie)

The Nessie CLI (`pynessie`) is a Python-based command-line tool for interacting with a Project Nessie server. It allows users to manage branches, view content, and commit changes to the catalog.

## Installation

```bash
pip install pynessie
```

## Key Commands

| Command | Purpose |
|---------|---------|
| `nessie branch` | List all branches |
| `nessie branch <new_branch>` | Create a new branch from the main branch |
| `nessie branch <new_branch> <old_branch>` | Create a branch from the specified branch |
| `nessie branch <new_branch> <hash>` | Create a new branch from the specified hash |
| `nessie content list -r <branch>` | List content in a branch |
| `nessie content view -r <branch> <key>` | View a particular content item in a branch |
| `nessie content commit -m <message> -r <branch> <key>` | Commit the particular content to the specified branch with the specified commit message |

## Usage Context

The CLI is used alongside a Nessie server (typically started via Docker) to manage catalog-level versioning. It complements SQL-based operations performed by engines like Spark, Flink, or Hive.

## References

- [Nessie CLI Documentation](https://nessie.readthedocs.io/en/latest/cli.html#branch-command)