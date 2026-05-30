---
type: concept
title: "External Secrets Manager Setup"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: External Secrets Manager Setup
created: 2026-05-14
updated: 2026-05-14
tags: [secrets, security, configuration, aws, azure, gcp]
related: [sdk-configuration, test-runner, data-quality-as-code, bot-authentication]
sources: ["testrunner---running-table-level-tests---openmetad-20260514.md"]
---

# External Secrets Manager Setup

When an OpenMetadata instance uses an external secrets manager for credential storage (rather than the default database-stored credentials), the Python SDK must be explicitly configured to access and decrypt those credentials. This is required for all SDK operations, including [[test-runner|TestRunner]] and ingestion pipelines.

## Why It's Required

The SDK needs to:
1. Retrieve the service connection configuration from OpenMetadata
2. Decrypt the credentials stored in the external secrets manager
3. Establish a connection to the data source
4. Execute the operation (test or ingestion)

Without proper secrets manager configuration, the SDK cannot decrypt credentials and will fail with "Cannot decrypt service connection" errors.

## General Setup Steps

1. Contact your OpenMetadata administrator to obtain:
   - The secrets manager type (AWS, Azure, GCP, etc.)
   - The secrets manager loader configuration
   - Required environment variables or configuration files
   - Any additional setup (IAM roles, service principals, etc.)

2. Install required dependencies for your secrets manager provider

3. Configure environment variables with access credentials

4. Initialize the `SecretsManagerFactory` **before** calling `configure()` or creating a TestRunner

## Provider-Specific Configuration

### AWS and AWS Parameters Store

**Dependencies:** `pip install "openmetadata-ingestion[aws]"`

**SecretsManagerProvider options:**
- `SecretsManagerProvider.aws`
- `SecretsManagerProvider.managed_aws`
- `SecretsManagerProvider.aws_ssm`
- `SecretsManagerProvider.managed_aws_ssm`

**Environment variables:**
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`

### Azure Key Vault

**Dependencies:** `pip install "openmetadata-ingestion[azure]"`

**SecretsManagerProvider options:**
- `SecretsManagerProvider.azure_kv`
- `SecretsManagerProvider.managed_azure_kv`

**Environment variables:**
- `AZURE_CLIENT_ID`
- `AZURE_CLIENT_SECRET`
- `AZURE_TENANT_ID`
- `AZURE_KEY_VAULT_NAME`

### Google Cloud Secret Manager

**Dependencies:** `pip install "openmetadata-ingestion[gcp]"`

**SecretsManagerProvider:** `SecretsManagerProvider.gcp`

**Environment variables:**
- `GOOGLE_APPLICATION_CREDENTIALS` — path to the credentials JSON file
- `GCP_PROJECT_ID`

## Example: AWS Secrets Manager

```python
import os
from metadata.generated.schema.security.secrets.secretsManagerClientLoader import SecretsManagerClientLoader
from metadata.generated.schema.security.secrets.secretsManagerProvider import SecretsManagerProvider
from metadata.sdk import configure
from metadata.utils.secrets.secrets_manager_factory import SecretsManagerFactory

os.environ["AWS_ACCESS_KEY_ID"] = "your-access-key-id"
os.environ["AWS_SECRET_ACCESS_KEY"] = "your-secret-access-key"
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

SecretsManagerFactory(
    secrets_manager_provider=SecretsManagerProvider.managed_aws,
    secrets_manager_loader=SecretsManagerClientLoader.env,
)

configure(host="https://your-openmetadata-instance.com/api", jwt_token="your-jwt-token")
```

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Cannot decrypt service connection" | Secrets manager not initialized or misconfigured | Ensure `SecretsManagerFactory` is initialized before `configure()` |
| "Access Denied" or "Unauthorized" | Insufficient permissions | Verify IAM role/service principal permissions; check credentials are valid |
| "Module not found" | Missing dependencies | Install the required extras package for your provider |
| Tests fail with connection errors | Credentials not properly decrypted | Verify provider matches backend; test credential access independently; enable debug logging |

## Related

- [[sdk-configuration]] — General SDK setup pattern
- [[test-runner]] — Uses this setup for data quality testing
- [[data-quality-as-code]] — Programmatic testing paradigm
- [[bot-authentication]] — JWT token authentication