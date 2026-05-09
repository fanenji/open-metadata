---
type: entity
title: Minikube
created: 2026-03-15
updated: 2026-03-15
tags: [kubernetes, macos, development-tool, open-source]
related: [local-kubernetes-tooling-comparison, orbstack, docker-desktop, kind, k3d, rancher-desktop, kubernetes]
sources: ["Kubernetes Development on macOS Guide.md"]
---
# Minikube

Minikube is one of the original tools for running local Kubernetes clusters. It runs a single-node cluster (multi-node is possible) typically inside a VM (VirtualBox, VMware Fusion, HyperKit on Mac) or using a Docker driver.

## Key Features

- **Flexibility**: Supports multiple drivers (VirtualBox, VMware, HyperKit, Docker) and Kubernetes version selection.
- **Addons**: Supports various addons for extended functionality (ingress, dashboard, metrics-server, etc.).
- **Full-Featured**: Provides a full-featured, configurable single-node cluster experience.
- **Mature**: Well-established with extensive documentation and community support.

## Limitations

- **Resource Intensive**: VM overhead can make it more resource-intensive than container-based solutions like Kind or k3d.
- **Slower Startup**: Slower to start compared to OrbStack, Kind, or k3d.
- **Host Path Mounting**: Requires `minikube mount` command to mount macOS host directories into the VM for data access.

## Use Cases

- Suitable for developers needing a full-featured, configurable single-node cluster.
- Good for testing Kubernetes features and addons.
- Less ideal for rapid iteration or resource-constrained environments.