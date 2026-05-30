---
type: concept
title: Integration Approaches Comparison
created: 2026-05-14
updated: 2026-05-14
tags: [integration, api, sdk, custom-connectors, decision-matrix]
related: [custom-connectors, python-sdk, ingestion-framework, openmetadata-connectors, bot-authentication]
sources: ["Mini-Webinar on Custom Connectors dataintegration connectors ingestion datacatalog metadata.md"]
---
# Integration Approaches Comparison

OpenMetadata offers three primary approaches for integrating external systems, each with distinct trade-offs. This page provides a decision matrix to help choose the right approach.

## Approach Overview

### 1. Raw API Calls
- **Description**: Direct REST API calls to the OpenMetadata server
- **Flexibility**: Maximum — any operation supported by the server is accessible
- **Requirements**: Minimal — any HTTP client library
- **Validation**: None — requires deep knowledge of the OpenMetadata standard and JSON Schema
- **UI Integration**: None — must manage scheduling and execution externally
- **Best for**: Simple, one-off operations; environments without Python/Java

### 2. Python/Java SDK
- **Description**: Generated client libraries with type-safe classes and helper methods
- **Flexibility**: High — all server operations available through typed interfaces
- **Requirements**: Python or Java environment
- **Validation**: IDE-level type checking and validation
- **UI Integration**: None — must manage scheduling and execution externally
- **Best for**: CI/CD pipelines; automated metadata updates; script-based integrations

### 3. Custom Connector (Ingestion Framework)
- **Description**: Extend the ingestion framework's `Source` class to create a reusable, UI-integrated connector
- **Flexibility**: Moderate — must fit the ingestion framework's workflow structure
- **Requirements**: Python environment; Docker for deployment
- **Validation**: Inherits SDK validation; framework handles translation and API calls
- **UI Integration**: Full — service creation, scheduling, log viewing from the UI
- **Best for**: Internal business systems; recurring metadata ingestion; team-wide use

### 4. Built-in Connector
- **Description**: One of the 90+ pre-built connectors shipped with OpenMetadata
- **Flexibility**: Limited to the connector's capabilities
- **Requirements**: None — available out of the box
- **Validation**: Full — maintained by the OpenMetadata team
- **UI Integration**: Full
- **Best for**: Popular data sources (Snowflake, PostgreSQL, etc.)

## Decision Matrix

| Criteria | Raw API | SDK | Custom Connector | Built-in |
|----------|---------|-----|------------------|----------|
| Need maximum flexibility | ✅ | ✅ | ⚠️ | ❌ |
| Need UI scheduling/logs | ❌ | ❌ | ✅ | ✅ |
| One-time operation | ✅ | ⚠️ | ❌ | ❌ |
| Recurring ingestion | ❌ | ⚠️ | ✅ | ✅ |
| No Python/Java available | ✅ | ❌ | ❌ | ✅ |
| Internal/proprietary source | ✅ | ✅ | ✅ | ❌ |
| Quick setup | ✅ | ⚠️ | ❌ | ✅ |

## Recommendation Flow

1. Is there a built-in connector? → Use it
2. Is it a simple, one-off operation? → Use raw API calls
3. Do you need UI integration and scheduling? → Build a custom connector
4. Do you have a CI/CD pipeline? → Use the SDK
5. Otherwise → Evaluate trade-offs between SDK and custom connector