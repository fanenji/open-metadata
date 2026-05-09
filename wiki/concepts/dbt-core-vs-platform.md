---
type: concept
title: dbt Core vs. dbt Platform
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, comparison, architecture, decision-framework]
related: [dbt-core, dbt-cloud, dbt-project-scaffolding, dbt-git-branching-strategies]
sources: ["Report dettagliato su dbt software.md"]
---
# dbt Core vs. dbt Platform

The choice between dbt Core (open-source CLI) and dbt Platform (managed SaaS) is a foundational architectural decision that impacts operational model, costs, and team skills. The report provides a detailed comparison across multiple dimensions.

## Comparison Table

| Feature | dbt Core | dbt Platform (Cloud) |
|---------|----------|---------------------|
| **Development Environment** | Local IDE (VSCode, Atom) + CLI | Web-based IDE (Studio IDE) + CLI |
| **Job Scheduling** | External orchestrator (cron, Airflow, Dagster, Argo) | Integrated scheduler with UI |
| **CI/CD** | Manual configuration in CI/CD tools (GitHub Actions, Jenkins) | Built-in integration with GitHub, GitLab, Azure DevOps |
| **Documentation Hosting** | Local generation, separate hosting required | Automatic managed hosting with access control |
| **Monitoring & Alerting** | External integration required | Built-in alerting (email, Slack) and dashboards |
| **Cost** | Free (infrastructure costs only) | Subscription-based (per user/usage) |
| **Management** | User responsible for installation, updates, maintenance | Fully managed by dbt Labs |

## Decision Framework

**Choose dbt Core when:**
- Team has existing orchestration infrastructure
- Team has DevOps skills to configure custom CI/CD pipelines
- Budget is limited or prefers FOSS solutions
- Full control over the environment is required
- Team prefers their own development tools

**Choose dbt Platform when:**
- Team wants a unified, out-of-the-box experience
- Rapid time-to-value is a priority
- Team wants to reduce operational and maintenance overhead
- Built-in scheduling, CI/CD, and monitoring are desired
- Team is willing to pay for a managed solution

## Impact on Architecture

The choice affects how the entire data pipeline is managed:
- **Core** requires integrating with external tools for scheduling, CI/CD, and monitoring, creating a more complex but flexible architecture.
- **Platform** provides an integrated experience but creates vendor lock-in to dbt Labs' ecosystem.