---
type: concept
title: CLI Ingestion with Basic Auth
created: 2026-05-14
updated: 2026-05-14
tags: [administration, ingestion, cli, authentication, basic-auth, jwt]
related:
  - openmetadata-administration
  - ingestion-framework
  - google-oauth
  - bot-authentication
  - security-config
  - metadata-cli
  - metadata-ingestion-workflow
  - kubernetes-native-orchestrator
sources:
  - admin-guide-openmetadata-administration-documentat-20260514.md
  - how-to-run-ingestion-pipeline-via-cli-with-basic-a-20260514.md
---

# CLI Ingestion with Basic Auth

CLI Ingestion with Basic Auth is a method for executing OpenMetadata ingestion pipelines from the command line. It provides an alternative to the default OAuth-based authentication, enabling workflows where OAuth token management is impractical. Although it is named after the platform’s **Basic Auth** mode (enabled by default since v0.12.1), the actual credential is a **JWT token** obtained from the `ingestion-bot` — it does **not** use HTTP Basic Authentication (username/password) in the traditional sense.

## Terminology Note

Despite the name “Basic Auth,” this method does **not** use HTTP Basic Authentication. The term refers to the platform’s authentication mode being enabled (Basic Auth, as opposed to the pre‑0.12.1 no‑auth default). The actual authentication is performed via a JWT token, which is a form of token‑based authentication. See [[bot-authentication|Bot Authentication]] for the underlying mechanism.

## Use Cases

- **Automation** — Scripted ingestion pipelines in environments where OAuth token management or UI interaction is impractical.
- **Legacy Systems** — Integration with tools, schedulers, or legacy orchestrators that do not support OAuth flows.
- **Development and Testing** — Simplified authentication during development, debugging, or CI/CD pipelines.

## Relationship to Standard Ingestion

The standard [[ingestion-framework|Ingestion Framework]] typically relies on [[google-oauth|Google OAuth]] (or other SSO providers) for authentication through the UI. CLI Ingestion with Basic Auth bypasses the UI and uses a JWT token to authenticate the CLI session as the `ingestion‑bot`. This approach is an alternative for the same ingestion workflows, giving administrators the flexibility to choose the method that best fits their environment.

## Prerequisites

- OpenMetadata server running with Basic Auth enabled (default since v0.12.1).
- Access to the OpenMetadata UI with permissions to view Bots.

## Procedure

### 1. Obtain the JWT Token

1. Navigate to **Settings** (from the activity bar) in the OpenMetadata UI.
2. Click on **Bots** to see the list of bots.
3. Click on the **ingestion‑bot**.
4. On the ingestion‑bot details page, locate the JWT token and click the **Copy** button.

### 2. Configure the Pipeline YAML

Add the `securityConfig` block under `workflowConfig.openMetadataServerConfig` in your pipeline configuration file:

```yaml
workflowConfig:
  openMetadataServerConfig:
    hostPort: http://localhost:8585/api
    authProvider: openmetadata
    securityConfig:
      jwtToken: 'eyJraWQiO...'
```

**Important:** `authProvider` must be set to `openmetadata`.

### 3. Run the Pipeline

Execute the ingestion using the `metadata` CLI:

```bash
metadata ingest -c ./pipeline_name.yaml
```

## How It Works

The JWT token authenticates the CLI session as the `ingestion‑bot`, a pre‑configured system bot account. The OpenMetadata server validates the token and authorises the ingestion request based on the bot’s assigned roles and policies. This leverages the same [[bot-authentication|Bot Authentication]] mechanism used by the [[kubernetes-native-orchestrator|Kubernetes Native Orchestrator]].

## Comparison with Other Ingestion Methods

| Method                    | Trigger                        | Authentication                |
| ------------------------- | ------------------------------ | ----------------------------- |
| UI Workflow               | OpenMetadata UI                | User session (OAuth/SSO)      |
| K8s Native Orchestrator   | CronJob / OMJob Operator       | Bot JWT token                 |
| CLI with Basic Auth       | `metadata ingest` command      | Bot JWT token in YAML         |

## Administration

Configuring and managing Basic Auth credentials for CLI ingestion falls under the responsibilities of an [[openmetadata-administration|OpenMetadata Administrator]]. This includes safeguarding the JWT token and ensuring the ingestion‑bot has the necessary permissions.

## Open Questions

- Can bots other than `ingestion‑bot` be used for CLI ingestion, or is `ingestion‑bot` the only authorised bot?
- How does CLI ingestion interact with the Kubernetes native orchestrator? Does the pipeline execute locally or as a Kubernetes Job?

## See Also

- [[security-config|Security Config]] — Detailed breakdown of the `securityConfig` YAML block.
- [[metadata-cli|Metadata CLI]] — The `metadata` command‑line tool.
- [[metadata-ingestion-workflow|Metadata Ingestion Workflow]] — The canonical UI‑based ingestion workflow.
- [[ingestion-framework|Ingestion Framework]] — The broader ingestion system.
- [[openmetadata-administration|OpenMetadata Administration]] — Administering authentication and ingestion.
- [[google-oauth|Google OAuth]] — Default authentication for the UI.
- [[bot-authentication|Bot Authentication]] — Mechanism behind the JWT token.
- [[kubernetes-native-orchestrator|Kubernetes Native Orchestrator]] — Alternative triggering mechanism.