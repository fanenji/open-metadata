---
type: concept
title: GDAL OCI Driver
created: 2026-04-29
updated: 2026-04-29
tags: [gdal, oracle, oci, geospatial, database-driver]
related: [gdal-docker-build-strategy, oracle-instant-client-docker, gdal-multi-stage-dockerfile]
sources: ["ETL - CONVERSAZIONI LLM.md"]
---
# GDAL OCI Driver

The Oracle Spatial interface compiled into GDAL, enabling direct read/write access to Oracle Spatial data. The driver is identified as `OCI` in GDAL's format list and supports both raster and vector data with read/write capabilities.

## Compilation Requirements

To compile GDAL with OCI support, the following are required:
- Oracle Instant Client SDK (version 19.26 in the source conversations)
- `libaio1` (async I/O library for Oracle)
- Proper `ORACLE_HOME` and `LD_LIBRARY_PATH` environment variables

## Build Configuration

### CMake (Multi-stage build)
```cmake
-DGDAL_USE_ORACLE=ON \
-DOracle_INCLUDE_DIR=$ORACLE_HOME/sdk/include \
-DOracle_LIBRARY=$ORACLE_HOME/libclntsh.so \
-DOracle_LIBRARY_DIR=$ORACLE_HOME \
-DOracle_ROOT=$ORACLE_HOME
```

### ./configure (Simpler build)
```bash
./configure \
    --with-oci \
    --with-oci-include=${ORACLE_HOME}/sdk/include \
    --with-oci-lib=${ORACLE_HOME}
```

## Verification

After building, verify OCI support with:
```bash
gdalinfo --formats | grep -i OCI
```

Expected output:
```
OCI -raster,vector- (rw+): Oracle Spatial
```

The `(rw+)` indicates read/write support for vector data.

## Related Pages
- [[gdal-docker-build-strategy]] — GDAL Docker build patterns
- [[oracle-instant-client-docker]] — Oracle client installation
- [[gdal-multi-stage-dockerfile]] — Multi-stage build reference