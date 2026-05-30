---
type: source
title: "Source: superset---openmetadata-documentation-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["superset---openmetadata-documentation-20260514.md"]
tags: []
related: []
---

# Source: superset---openmetadata-documentation-20260514.md

## Analysis of: Superset - OpenMetadata Documentation

### Key Entities

| Name | Type | Role | In Wiki? |
|------|------|------|----------|
| **Superset** | Dashboard platform (Apache Superset) | Central — the source system being connected to | Yes ([[superset-connector]]) |
| **OpenMetadata** | Metadata platform | Central — the system performing ingestion | Yes ([[openmetadata]]) |
| **Superset REST APIs** | API interface | Central — the mechanism for metadata extraction | Implicit in [[superset-connector]] |
| **db authentication mode** | Auth method | Central — one of two supported modes | Not explicitly documented |
| **ldap authentication mode** | Auth method | Peripheral — mentioned as supported but not detailed | Not documented |
| **OAuth authentication** | Auth method | Peripheral — explicitly unsupported by Superset APIs | Not documented |
| **Admin user credentials** | Credential type | Central — default "admin/admin" user for API auth | Not documented |
| **Database credentials** | Credential type | Central — MySQL or PostgreSQL connection details for direct DB access | Not documented |

### Key Concepts

| Name | Definition | Why It Matters | In Wiki? |
|------|-----------|----------------|----------|
| **Superset SSO Authentication** | The two supported methods (db and ldap) for authenticating to Superset REST APIs to extract metadata | Determines how users configure the Superset connector; OAuth is explicitly unsupported | No — this is a specific limitation not captured |
| **API Authentication Modes** | Superset's built-in auth modes (`db` for database-backed, `ldap` for LDAP-backed) | Users must choose one of these two; no OAuth option available | No |
| **Direct Database Extraction** | Alternative method: bypass Superset APIs entirely by connecting directly to Superset's MySQL/PostgreSQL database | Provides a workaround when API auth is problematic; also mentioned in [[superset-connector]] | Partially — [[superset-connector]] mentions "API and database extraction methods" |

### Main Arguments & Findings

- **Core claim**: OpenMetadata's Superset connector uses Superset REST APIs, which only support `db` and `ldap` authentication modes — OAuth is not supported.
- **Two authentication paths**:
    1. Use the default admin credentials (`admin`/`admin`) via `db` mode
    2. Provide direct MySQL or PostgreSQL database connection details to bypass the API
- **Evidence strength**: Official documentation from OpenMetadata v1.12.x; authoritative but brief (single page).

### Connections to Existing Wiki

- **Directly extends** [[superset-connector]] — adds specific SSO/authentication details not present in the existing page
- **Relates to** [[openmetadata-connectors]] — as a specific connector configuration detail
- **Relates to** [[service-connection]] — as a specific service connection configuration scenario
- **Contrasts with** [[postgresql-connector]] and [[oracle-connector]] — which have more detailed authentication documentation

