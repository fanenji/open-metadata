---
type: note
topic: data-platform
created: 2026-02-17
tags:
  - data-platform
  - openmetadata
---


# INSTALLAZIONE IN LOCALE

Installazione con docker in ~/Development/DP/openmetadata-docker

```yaml
curl -sL -o docker-compose.yml https://github.com/open-metadata/OpenMetadata/releases/download/1.11.0-release/docker-compose.yml
```


# PROGETTO TEST DBT


Creato progetto

/Users/stefano/Development/DP/dbt-projects/test_local_openmetadata

Installato pacchetto python

```yaml
pip install "openmetadata-ingestion[dbt]"
```

```bash
# DBT 
# https://docs.open-metadata.org/latest/connectors/ingestion/workflows/dbt
# https://docs.open-metadata.org/latest/connectors/ingestion/workflows/dbt/auto-ingest-dbt-core

pip install "openmetadata-ingestion[dbt]"==1.10.14

metadata --debug ingest-dbt
```

Configurazione dbt-project.yml

```yaml
vars:
  # Required OpenMetadata configuration
  openmetadata_host_port: "http://openmetadata-server.openmetadata-docker.orb.local"
  openmetadata_jwt_token: "your-jwt-token-here"
  openmetadata_service_name: "your-database-service-name"
```



# MCP

## CLAUDE CODE

Configurazione in
- ~/.claude/settings.json
- ~/Library/Application\ Support/Claude/claude_desktop_config.json

```other
{
  "mcpServers": {
    "openmetadata": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://openmetadata-test.dataliguria.it/mcp",
        "--auth-server-url=https://openmetadata-test.dataliguria.it/mcp",
        "--client-id=openmetadata",
        "--verbose",
        "--clean",
        "--header",
        "Authorization:${AUTH_HEADER}"
      ],
      "env": {
        "AUTH_HEADER": "Bearer [REDACTED]"
      }
    }
  }
}
```

## OPENCODE

**test opencode con devstral local**

test mcp openmetadata (vedi config in claude code)

/Users/stefano/.config/opencode/opencode.json

```other
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "my-local-mcp-server": {
      "type": "local",
      // Or ["bun", "x", "my-mcp-command"]
      "command": ["npx", "-y", "my-mcp-command"],
      "enabled": true,
      "environment": {
        "MY_ENV_VAR": "my_env_var_value",
      },
    },
  },
}
```


