---
type: entity
title: ArgoCD
created: 2026-05-08
updated: 2026-05-08
tags: [gitops, kubernetes, ci-cd, deployment]
related: [kubernetes, gitlab-ci, ci-cd-rollback-strategies, error-recovery-mechanisms, blue-green-deployment, canary-release]
sources: ["research-error-recovery-mechanisms-2026-05-08.md"]
---
# ArgoCD

ArgoCD is a GitOps continuous delivery tool for Kubernetes. It treats rollbacks as Git operations — an automated CI pipeline can detect deployment failures (unhealthy pods, failed health checks) and automatically execute an ArgoCD rollback or `git revert`.

## Key Features

- Native rollback to a previous sync revision.
- Automated rollback based on health check failures.
- Integration with GitLab CI and other CI/CD tools for end-to-end automated recovery.
