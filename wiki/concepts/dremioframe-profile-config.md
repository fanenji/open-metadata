---
type: concept
title: DremioFrame Profile Configuration
created: 2026-04-29
updated: 2026-04-29
tags: [dremio, configuration, yaml, python]
related: [dremioframe, dremio]
sources: ["DremioFrame - Dremio Dataframe Library.md"]
---
# DremioFrame Profile Configuration

DremioFrame Profile Configuration is a YAML-based configuration system for managing Dremio connections within the [[dremioframe|DremioFrame]] library. Profiles are stored in `~/.dremio/profiles.yaml` and allow users to define multiple connection configurations.

## Profile Structure

```yaml
profiles:
  my_profile:
    type: cloud  # or "software"
    auth:
      type: pat  # Personal Access Token
      token: "your-pat"
    project_id: "your-project-id"
default_profile: my_profile
```

## Usage

Profiles can be used to create DremioClient instances:

```python
from dremioframe.client import DremioClient

# Uses the default profile
client = DremioClient()

# Or specify a profile
client = DremioClient(profile="my_profile")
```

## Environment Variables

DremioFrame also supports configuration via environment variables:
- `DREMIO_PAT` — Personal Access Token for Dremio Cloud
- `DREMIO_PROJECT_ID` — Project ID for Dremio Cloud
- `DREMIO_SOFTWARE_HOST` — Hostname for Dremio Software
- `DREMIO_SOFTWARE_PAT` — PAT for Dremio Software
- `DREMIO_SOFTWARE_USER` — Username for Dremio Software (v25)
- `DREMIO_SOFTWARE_PASSWORD` — Password for Dremio Software (v25)

## Related

- [[dremioframe]] — The parent library
- [[dremio]] — The target system