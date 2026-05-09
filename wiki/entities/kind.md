---
type: entity
title: Kind (Kubernetes IN Docker)
created: 2026-03-15
updated: 2026-03-15
tags: [kubernetes, macos, development-tool, open-source, testing]
related: [local-kubernetes-tooling-comparison, k3d, minikube, orbstack, docker-desktop, kubernetes]
sources: ["Kubernetes Development on macOS Guide.md"]
---
# Kind (Kubernetes IN Docker)

Kind (Kubernetes IN Docker) is a tool for running local Kubernetes clusters using Docker containers as cluster nodes. It was designed primarily for testing Kubernetes itself but is widely used for local development and CI/CD pipelines.

## Key Features

- **Lightweight**: Runs cluster nodes as Docker containers, making it very lightweight.
- **Fast Startup**: Starts very quickly compared to VM-based solutions.
- **Multi-Node**: Supports multi-node clusters easily.
- **CI/CD Friendly**: Excellent for CI/CD pipelines and ephemeral cluster scenarios.
- **YAML Configuration**: Cluster configuration is done via YAML files, including support for extra mounts for host directory access.

## Limitations

- **Requires Docker**: Needs Docker to be installed.
- **CLI-Only**: No GUI, managed entirely via CLI.
- **Host Path Mounting**: Requires configuration at cluster creation time (extraMounts) to access macOS host directories.

## Use Cases

- Excellent for CI/CD pipelines and testing.
- Good for developers who need ephemeral, fast-to-create clusters.
- Suitable for multi-node cluster testing.