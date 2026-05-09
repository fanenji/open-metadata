---
type: concept
title: Git-friendly Reproducible Python
created: 2026-05-06
updated: 2026-05-06
tags: [notebook, git, reproducibility, python, version-control]
related: [marimo, reactive-notebook]
sources: ["Marimo - next-generation Python notebook.md"]
---
# Git-friendly Reproducible Python

Git-friendly reproducible Python refers to the practice of storing computational notebooks as plain Python files (`.py`) rather than proprietary or JSON-based formats (e.g., Jupyter's `.ipynb`). This enables standard version control workflows, including meaningful diffs, code reviews, and collaboration.

## Key Characteristics

- **Plain Text Storage:** Notebooks are saved as standard Python scripts, not binary or JSON blobs.
- **Meaningful Diffs:** Changes to code, parameters, and outputs are visible in standard Git diffs.
- **Reproducibility:** The plain Python format can be executed directly as a script, ensuring that the same code produces the same results.
- **Collaboration:** Enables standard Git workflows (branching, merging, pull requests) for notebook development.

## Relevance to Data Platform

Adopting Git-friendly notebook formats aligns with the wiki's emphasis on [[CI-CD-for-data-pipelines]] and [[data-contract-versioning-strategy]]. It enables notebook-based analysis to be versioned, reviewed, and deployed alongside other data platform code.

## Related Concepts

- [[reactive-notebook]] — The reactive execution model that complements Git-friendly storage in [[marimo]].