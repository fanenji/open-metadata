---
type: concept
title: Kubernetes FastAPI Deployment
created: 2026-02-13
updated: 2026-02-13
tags: [kubernetes, fastapi, python, deployment, api]
related: [kubernetes-development-best-practices, kubernetes-secrets-management, fastapi, container-image-strategy-for-data-pipelines]
sources: ["Kubernetes Dev Environment on MacBook_ .md"]
---
# Kubernetes FastAPI Deployment

Patterns for containerizing and deploying FastAPI applications on Kubernetes, including Dockerfile examples, Deployment manifests, and Service manifests.

## FastAPI Containerization

- **Base Image:** Start with a minimal Python image, like `python:3.10-slim`.
- **Working Directory:** Set `WORKDIR /app`.
- **Dependencies:** Copy `requirements.txt` (containing `fastapi`, `uvicorn[standard]`, and other dependencies) and install using `pip install --no-cache-dir -r requirements.txt`.
- **Code:** Copy application source code.
- **Port:** Expose the port the application server will listen on (e.g., `EXPOSE 8000`).
- **Command:** Specify the command to run the ASGI server: `CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]`. The `--host 0.0.0.0` is crucial to accept connections from outside the container.
- **User:** Consider running as a non-root user for better security.
- **Multi-stage:** Use multi-stage builds if complex build steps are needed.

## Kubernetes Deployment Manifest

Key elements of a Deployment manifest for FastAPI:

- `replicas`: Number of identical Pods (e.g., 1 or 2 for local dev).
- `selector.matchLabels`: Must match the labels defined in the Pod template.
- `template.spec.containers`: Define the application container with image, ports, resources, probes, and environment/volume configuration.
- `livenessProbe` / `readinessProbe`: Configure `httpGet` probes pointing to a health check endpoint (e.g., `/health`).

## Kubernetes Service Manifest

- `selector`: Must match the labels of the Pods managed by the Deployment.
- `ports`: Maps the Service port to the Pods' `targetPort`.
- `type`: For local development with tools like OrbStack or Rancher Desktop, `type: LoadBalancer` usually provides the easiest access. `NodePort` is a solid alternative. `ClusterIP` is accessible from macOS host when using OrbStack.