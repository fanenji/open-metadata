---
type: concept
title: Geospatial Docker Base Images
created: 2026-03-15
updated: 2026-03-15
tags: [docker, geospatial, gdal, python, containerization, best-practices]
related: [container-image-strategy-for-data-pipelines, kubernetes-jobs-cronjobs, kubernetes-etl-deployment-strategies]
sources: ["Kubernetes Development on macOS Guide.md"]
---
# Geospatial Docker Base Images

Building Docker images for geospatial Python workloads (GDAL, GeoPandas, Rasterio) requires careful management of complex system-level dependencies. This concept covers strategies for optimizing geospatial container images.

## Recommended Base Images

- **osgeo/gdal:ubuntu-small-latest**: Lightweight GDAL image with core dependencies.
- **osgeo/gdal:ubuntu-full-latest**: Full GDAL image with additional command-line tools.
- Using official or community-maintained base images bypasses the complexities of compiling GDAL from scratch.

## Multi-Stage Build Strategy

Multi-stage builds are essential for geospatial containers due to the large size of GDAL dependencies.

1. **Builder Stage**: Based on `osgeo/gdal:ubuntu-full-3.6.3` (use specific, stable tags).
   - Install Python, pip, and build tools (`libspatialindex-dev` for GeoPandas performance).
   - Install Python dependencies from `requirements.txt` into a target directory.
2. **Runtime Stage**: Based on `python:3.x-slim`.
   - Create a non-root user.
   - Copy installed Python packages from builder stage.
   - Copy application code.
   - Set entrypoint/command.

## Dockerfile Optimization

- **Layer Caching**: Place commands that change less frequently (base packages) before commands that change often (application code).
- **Combine RUN Commands**: Use `&&` to chain related commands and reduce layer count.
- **Clean Up**: Remove package manager caches (`apt-get clean && rm -rf /var/lib/apt/lists/*`) in the same RUN command.
- **Minimal Base**: Use `python:3.x-slim` or `alpine` for the final stage.
- **Non-Root User**: Create and use a non-root user for the final stage for security.

## Custom Base Image

If multiple ETL jobs or services share the exact same complex geospatial stack, consider building a custom internal base image containing these dependencies. Subsequent application images can use this custom base, speeding up builds and ensuring consistency.

## Example Dockerfile Structure

```dockerfile
# Stage 1: Build environment with dependencies
FROM osgeo/gdal:ubuntu-full-3.6.3 AS builder
WORKDIR /install
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix="/install" -r requirements.txt

# Stage 2: Final runtime image
FROM python:3.10-slim AS runtime
WORKDIR /app
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser
COPY --from=builder /install /usr/local/
COPY ./src /app/src
COPY etl_script.py .
CMD ["python", "etl_script.py"]
```