---
type: entity
title: Freelens
created: 2026-02-13
updated: 2026-02-13
tags: [kubernetes, ide, client, open-source]
related: [kubeconfig, kubernetes, kubectl]
sources: ["Freelens Kubernetes Client Setup_ .md"]
---
# Freelens

Freelens is an open-source, graphical Kubernetes IDE (Integrated Development Environment) that provides a visual interface for managing Kubernetes clusters. It is a community-driven fork of the proprietary Lens application. Freelens reduces the need for command-line `kubectl` usage for day-to-day operations by offering a sidebar-based cluster browser, resource visualization, and integrated terminal access.

## Installation on macOS

Freelens can be installed on macOS via two methods:

1. **Direct Download:** Download the `.dmg` or `.pkg` installer from the [official Freelens website](https://freelensapp.github.io/) and install manually.
2. **Homebrew:** Install using the command `brew install --cask freelens`.

## Configuration

Freelens relies on the standard Kubernetes [[kubeconfig]] file for authentication and cluster discovery. By default, it reads `~/.kube/config`. Clusters can be added automatically (if `kubectl` is already configured) or manually by pasting kubeconfig content or selecting a file from the filesystem.

## Related

- [[kubeconfig]] — The configuration file Freelens uses to connect to clusters.
- [[kubernetes]] — The container orchestration platform Freelens manages.
- [[kubectl]] — The command-line alternative to Freelens.