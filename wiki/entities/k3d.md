---
type: entity
title: k3d
created: 2026-03-15
updated: 2026-03-15
tags: [kubernetes, macos, development-tool, open-source, lightweight]
related: [local-kubernetes-tooling-comparison, kind, minikube, orbstack, rancher-desktop, kubernetes]
sources: ["Kubernetes Development on macOS Guide.md"]
---
# k3d

k3d is a wrapper around k3s (Rancher's lightweight Kubernetes distribution) that runs cluster nodes in Docker containers. It is known for extremely fast cluster creation and deletion.

## Key Features

- **Extremely Fast**: Known for the fastest cluster creation and deletion among local K8s tools.
- **Resource Efficient**: Lightweight due to k3s and Docker container-based nodes.
- **Multi-Node**: Supports multi-node clusters easily.
- **User-Friendly CLI**: Managed via a simple, well-designed CLI.
- **Host Path Mounting**: Supports mounting host directories into node containers at cluster creation time via `-v` flags.

## Limitations

- **Requires Docker**: Needs Docker to be installed.
- **CLI-Only**: No GUI, managed entirely via CLI.
- **k3s-Specific**: Uses k3s, which may have slight differences from full Kubernetes.

## Use Cases

- Best choice for CLI-focused, fast, ephemeral cluster workflows.
- Excellent for local development and CI when speed and efficiency are paramount.
- Ideal for developers who prefer command-line tools over GUIs.