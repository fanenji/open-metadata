---
type: concept
title: Container Separation Principle
created: 2026-02-13
updated: 2026-02-13
tags: [docker, containerization, architecture, best-practices]
related: [migration-strategy-two-phase, fastapi, java-groovy-tomcat-stack, container-image-strategy-for-data-pipelines]
sources: ["Migrazione API REST Java:Groovy a Python:FastAPI.md"]
---
# Container Separation Principle

The principle that different technology stacks during a phased migration should run in separate containers, not combined in a single container. This is a key architectural decision in the two-phase migration strategy.

## Rationale

1. **Single Responsibility Principle**: Each container should run a single process or service. Combining Tomcat (Java) and Uvicorn (Python) in one container violates this principle and requires complex process management (e.g., supervisorctl).

2. **Image Bloat**: A combined container would contain both the full Java/Groovy/Tomcat stack and the full Python/FastAPI stack, making it unnecessarily large, slow to build, and slow to deploy.

3. **Dependency Complexity**: Managing system and language dependencies for two different technology stacks (JVM vs Python interpreter) in the same Dockerfile increases the probability of conflicts.

4. **Security Surface Area**: A larger image with more software has a larger attack surface. Keeping the Python image minimal reduces risk.

5. **Testing Simplicity**: Separate containers allow running both systems side-by-side on different ports (e.g., 8080 for Java, 8000 for Python) for direct API response comparison.

6. **Clean Final Artifact**: The goal is a Python-only container for production. Building this separately from the start ensures the final artifact is clean and optimized.

## Application in Migration

During Phase 2 of the two-phase migration:
- **Container 1**: Runs the original Java/Groovy/Tomcat application (from Phase 1)
- **Container 2**: Runs the new Python/FastAPI application (under development)
- Both run simultaneously on different ports for side-by-side comparison using the [[api-regression-test-suite]]

## Related

- [[migration-strategy-two-phase]] — The migration strategy that requires this principle
- [[fastapi]] — Target framework in its own container
- [[java-groovy-tomcat-stack]] — Legacy stack in its own container
- [[container-image-strategy-for-data-pipelines]] — Related Docker image design principles