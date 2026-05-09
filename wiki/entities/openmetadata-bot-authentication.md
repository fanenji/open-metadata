---
type: entity
title: OpenMetadata Bot Authentication
created: 2026-04-08
updated: 2026-04-08
tags: [openmetadata, authentication, security, bot]
related: [openmetadata, local-llm-openmetadata-extension, data-consumer-role]
sources: ["Local LLM for OpenMetadata - Visual Studio Marketplace.md"]
---
# OpenMetadata Bot Authentication

A JWT-based authentication pattern for programmatic access to [[openmetadata]] APIs. Used by the [[local-llm-openmetadata-extension]] to authenticate as a service account.

## Setup Process

1. Log into OpenMetadata (default: admin/admin).
2. Navigate to **Settings** → **Bots**.
3. Click **Add Bot** with a name (e.g., `vscode-llm-bot`) and description.
4. Click **Generate Token** and copy the JWT token (starts with `eyJ`).
5. Assign the **Data Consumer** role to the bot.

## Usage

The bot token is configured in the extension's settings as `openmetadataExplorer.openmetadataAuthToken`. It enables the extension to query metadata, search tables, and retrieve lineage information without user interaction.

## Security Considerations

- Tokens should be kept secret and not committed to version control.
- The **Data Consumer** role provides read-only access appropriate for discovery tools.
- Token rotation and expiration policies should follow organizational security standards.