---
type: concept
title: Kubernetes Probes
created: 2026-03-15
updated: 2026-03-15
tags: [kubernetes, health-checks, reliability, best-practices]
related: [kubernetes, kubernetes-secrets-management, kubernetes-jobs-cronjobs, fastapi]
sources: ["Kubernetes Development on macOS Guide.md"]
---
# Kubernetes Probes

Kubernetes probes are health checks that help Kubernetes understand the state of containers to manage their lifecycle effectively. They are essential for building reliable, self-healing applications.

## Types of Probes

### Liveness Probe
- Determines if a container is running correctly.
- If it fails repeatedly, Kubernetes restarts the container.
- Use for detecting deadlocks or unresponsive processes.
- **Avoid** using for fatal errors where the app should crash naturally.

### Readiness Probe
- Determines if a container is ready to accept traffic.
- If it fails, the Pod is removed from Service endpoints.
- Crucial for applications that need time to initialize (load data, warm caches).
- Should generally check the application's own state, not external dependencies.

### Startup Probe
- Checks if an application within a container has started successfully.
- Disables liveness and readiness probes until it succeeds.
- Useful for slow-starting applications to prevent premature restarts by the liveness probe.

## Configuration Parameters

- `initialDelaySeconds`: Wait before first probe.
- `periodSeconds`: Check frequency.
- `timeoutSeconds`: Probe timeout.
- `successThreshold`: Consecutive successes to mark healthy.
- `failureThreshold`: Consecutive failures to mark unhealthy.

## Probe Actions

- **httpGet**: HTTP GET request to a specific path and port.
- **tcpSocket**: TCP connection attempt to a port.
- **exec**: Execute a command inside the container.

## Best Practices

- Always configure at least a readiness probe for services that accept traffic.
- Use startup probes for applications with variable startup times.
- Set appropriate `initialDelaySeconds` to avoid premature restarts.
- Keep probe endpoints lightweight and fast.
- For FastAPI services, create a dedicated `/health` endpoint.