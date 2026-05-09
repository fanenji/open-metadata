---
type: entity
title: Java/Groovy/Tomcat Stack
created: 2026-02-13
updated: 2026-02-13
tags: [java, groovy, tomcat, legacy, migration]
related: [migration-strategy-two-phase, container-separation-principle, fastapi]
sources: ["Migrazione API REST Java:Groovy a Python:FastAPI.md"]
---
# Java/Groovy/Tomcat Stack

The legacy technology stack being migrated from in the two-phase migration strategy. This stack consists of Groovy/Java applications deployed on Apache Tomcat, running on Windows Server 2019.

## Components

- **Java**: OpenJDK 8 (Java 1.8)
- **Groovy**: Version 2.4.8 — JVM-based scripting language used for API implementation
- **Tomcat**: Version 8.5.54 — Java application server for deploying REST APIs
- **Operating System**: Windows Server 2019 (source), Ubuntu 22.04 (Phase 1 target)

## Dockerfile Pattern

The Phase 1 Dockerfile creates a container with:
- Ubuntu 22.04 base image
- OpenJDK 8 installed via apt
- Tomcat 8.5.54 downloaded from Apache archives and extracted to `/opt/tomcat`
- Groovy 2.4.8 downloaded from Maven Central and extracted to `/opt/groovy`
- Non-root user (`tomcat`) for security
- Default command: `catalina.sh run` (Tomcat in foreground)

## Migration Path

1. **Phase 1**: Package this stack into a Docker container running on Ubuntu 22.04
2. **Phase 2**: Re-implement the API logic in Python/FastAPI, running in a separate container
3. **End state**: The Java/Groovy/Tomcat container is decommissioned

## Related

- [[migration-strategy-two-phase]] — The migration strategy that uses this stack as the source
- [[container-separation-principle]] — Why this stack must be in its own container during Phase 2
- [[fastapi]] — The target framework replacing this stack