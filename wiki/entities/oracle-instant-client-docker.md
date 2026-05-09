---
type: entity
title: Oracle Instant Client Docker
created: 2026-04-29
updated: 2026-04-29
tags: [oracle, docker, gdal, instant-client, database]
related: [gdal-docker-build-strategy, proj-grid-file-management, gdal-multi-stage-dockerfile]
sources: ["ETL - CONVERSAZIONI LLM.md"]
---
# Oracle Instant Client Docker

Pattern for installing Oracle Instant Client in Docker images using local zip files, specifically for GDAL compilation with OCI support.

## Version

Version 19.26 is used in the source conversations. Two variants exist:
- **Basic** (full client): Used in the multi-stage build
- **Basic Light** (minimal client): Used in the simpler Dockerfile

Both require the **SDK** package for GDAL compilation.

## Directory Structure

```
.
├── oracle_zip_amd64/
│   ├── instantclient-basic-linux.x64-19.26.0.0.0dbru.zip
│   └── instantclient-sdk-linux.x64-19.26.0.0.0dbru.zip
├── oracle_zip_arm64/
│   ├── instantclient-basic-linux.arm64-19.26.0.0.0dbru.zip
│   └── instantclient-sdk-linux.arm64-19.26.0.0.0dbru.zip
```

## Installation Steps

1. Copy zip files into the Docker build context
2. Unzip to `/opt/oracle` or `/usr/lib/oracle`
3. Create symbolic links: `libclntsh.so -> libclntsh.so.19.1`
4. Configure dynamic linker: add path to `/etc/ld.so.conf.d/`
5. Run `ldconfig`

## Environment Variables

- `ORACLE_HOME`: Path to the instant client directory
- `LD_LIBRARY_PATH`: Include `$ORACLE_HOME`
- `TNS_ADMIN`: Path to network/admin directory (optional)
- `PATH`: Include `$ORACLE_HOME`

## Licensing Note

Oracle Instant Client requires a valid Oracle license. The zip files must be downloaded from Oracle's website and stored locally. They cannot be redistributed in Docker images.

## Related Pages
- [[gdal-docker-build-strategy]] — GDAL Docker build patterns
- [[proj-grid-file-management]] — PROJ configuration
- [[gdal-multi-stage-dockerfile]] — Multi-stage build reference