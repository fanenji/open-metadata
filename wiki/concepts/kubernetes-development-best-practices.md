---
type: concept
title: Kubernetes Development Best Practices
created: 2026-02-13
updated: 2026-02-13
tags: [kubernetes, devops, best-practices, containerization, configuration]
related: [local-kubernetes-development-macos, kubernetes-geospatial-etl-deployment, kubernetes-fastapi-deployment, kubernetes-secrets-management, container-image-strategy-for-data-pipelines, helm]
sources: ["Kubernetes Dev Environment on MacBook_ .md"]
---
# Kubernetes Development Best Practices

General guidelines and best practices for developing and deploying applications for a Kubernetes environment, covering containerization, configuration management, health checks, resource management, and the inner development loop.

## Containerization Strategies

- **Dockerfile Optimization:** Structure Dockerfiles to leverage build caching. Place commands that change less frequently (e.g., installing base packages) before commands that change often (e.g., copying application code). Combine related `RUN` commands using `&&` to reduce layer count. Clean up temporary files within the same `RUN` command.
- **Minimal Base Images:** Use minimal base images (e.g., `python:3.x-slim`, `alpine`, or `distroless`) to reduce image size and attack surface. Avoid installing unnecessary packages.
- **Multi-Stage Builds:** Use multiple `FROM` statements to separate build-time dependencies from runtime dependencies. Build the application in an initial "builder" stage, then copy only the necessary artifacts into a final, minimal runtime stage. This significantly reduces final image size and improves security.

## Configuration Management (ConfigMaps & Secrets)

- **Purpose:** Decouple configuration from container images. Use ConfigMaps for non-sensitive configuration data. Use Secrets for sensitive data (API keys, passwords, tokens, certificates).
- **Usage Patterns:** Inject ConfigMap/Secret data into Pods as environment variables (`env`, `envFrom`) or as files mounted into volumes (`volumes`, `volumeMounts`). Mounting as volumes is often preferred for configuration files and allows for automatic updates.
- **Best Practices:** Store configuration files (YAML) in version control. Never store sensitive data directly in manifests. Apply the principle of least privilege using RBAC to restrict access to Secrets. Enable encryption at rest for Secrets in etcd for production environments. Rotate secrets regularly.

## Application Health Checks (Probes)

- **Liveness Probe:** Determines if a container is running correctly. If it fails repeatedly, Kubernetes restarts the container. Use this to detect deadlocks or unresponsive processes.
- **Readiness Probe:** Determines if a container is ready to accept traffic. If it fails, the Pod is removed from Service endpoints. Crucial for applications that need time to initialize before serving requests.
- **Startup Probe:** Checks if an application within a container has started successfully. Disables liveness and readiness probes until it succeeds. Useful for slow-starting applications to prevent premature restarts.

## Resource Management (Requests & Limits)

- **Requests:** The minimum amount of CPU/Memory guaranteed to a container. Used by the scheduler to place Pods on nodes with sufficient capacity. Setting requests is crucial for scheduling and guaranteeing baseline resources.
- **Limits:** The maximum amount of CPU/Memory a container can use. Exceeding the CPU limit leads to throttling. Exceeding the memory limit can lead to the container being OOMKilled.
- **Best Practices:** Always set resource requests. Set limits to prevent runaway resource consumption, but be cautious not to set them too low. Setting requests equal to limits provides "Guaranteed" Quality of Service (QoS). Monitor actual usage to right-size requests and limits.

## Local Development Loop Tools

- **Skaffold:** Automates build, push, and deploy workflow. Monitors source code and triggers rebuilds/redeploys. CLI-focused. Integrates well with CI/CD.
- **Tilt:** Provides a real-time, interactive development environment with a web UI. Offers smart rebuilds and live updates. Good for teams needing a visual interface.
- **DevSpace:** CLI tool for building/deploying images, log streaming, file synchronization, port forwarding, and terminal access.
- **Telepresence:** Connects a local process or container directly to the cluster's network, allowing local debugging of services as if they were running in the cluster.