---
type: concept
title: Process Wrapper Pattern
created: 2024-05-22
updated: 2024-05-22
tags: [testing, automation, cli]
related: [ogr2ogr]
sources: ["CONVERSIONI GROEVY -> PYTHON.md"]
---
# Process Wrapper Pattern

A technique used to control external CLI dependencies (like `ogr2ogr`) during integration tests. By using a "wrapper" script (e.g., a `.bat` or `.sh` file), the tester can simulate success, failure, or timeouts without needing to mock the Python `subprocess` module.