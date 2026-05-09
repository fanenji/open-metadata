---
type: concept
title: Multi-Stage Docker Build
created: 2026-04-29
updated: 2026-04-29
tags: [docker, build, optimization, container]
related: [gdal-docker-build-strategy, gdal-multi-stage-dockerfile, container-image-strategy-for-data-pipelines, kubernetes-etl-deployment-strategies]
sources: ["ETL - CONVERSAZIONI LLM.md"]
---
# Multi-Stage Docker Build

A Docker build pattern that uses multiple `FROM` statements in a single Dockerfile to separate the build environment from the runtime environment. This technique significantly reduces final image size by excluding build tools, compilers, and intermediate files.

## How It Works

1. **Builder Stage(s)**: Contains all compilation tools (g++, cmake, swig), development libraries, and source code. The application is compiled and all necessary artifacts are produced here.
2. **Final Stage**: Starts from a clean base image. Installs only runtime dependencies. Copies only the compiled artifacts and runtime libraries from the builder stage using `COPY --from=builder`.

## Benefits

- **Smaller Images**: Build tools (g++, cmake, etc.) can add hundreds of MB to an image
- **Cleaner Runtime**: No unnecessary files or tools in the final image
- **Security**: Reduced attack surface by excluding compilers and development tools
- **Separation of Concerns**: Build configuration is isolated from runtime configuration

## Example Pattern

```dockerfile
# Stage 1: Builder
FROM ubuntu:22.04 AS builder
RUN apt-get install -y build-essential cmake g++ ...
COPY source.tar.gz /tmp/
RUN ./configure && make && make install

# Stage 2: Final
FROM ubuntu:22.04
RUN apt-get install -y libruntime1 ...
COPY --from=builder /usr/local/bin/app /usr/local/bin/
COPY --from=builder /usr/local/lib/libapp.so* /usr/local/lib/
```

## Related Pages
- [[gdal-docker-build-strategy]] — GDAL-specific multi-stage build
- [[gdal-multi-stage-dockerfile]] — Reference implementation
- [[container-image-strategy-for-data-pipelines]] — General container design
- [[kubernetes-etl-deployment-strategies]] — ETL deployment on Kubernetes