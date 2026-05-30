---
type: concept
title: PostgreSQL IAM Authentication
created: 2026-05-14
updated: 2026-05-15
tags: [postgresql, iam, aws, rds, authentication, security]
related: [postgresql-connector, postgresql-ssl-modes, postgresql-connector-troubleshooting]
sources: ["PostgreSQL Connector  OpenMetadata Database Integration.md", "postgresql-connector-troubleshooting---openmetadat-20260514.md"]
---
# PostgreSQL IAM Authentication

IAM authentication for PostgreSQL allows connecting to AWS RDS PostgreSQL instances using AWS Identity and Access Management (IAM) credentials instead of a database password. OpenMetadata supports this authentication method for the [[postgresql-connector]] as an alternative to password-based authentication.

## Prerequisites

For IAM authentication to work, three conditions must be met:

1. **IAM DB Authentication Enabled on RDS** – The RDS instance must have IAM DB authentication enabled. This can be configured via the AWS Console by modifying the RDS instance.

2. **Database User with `rds_iam` Role** – Create a PostgreSQL user and grant the `rds_iam` role:
   ```sql
   CREATE USER iam_user WITH LOGIN;
   GRANT rds_iam TO iam_user;
   ```

3. **IAM Policy with `rds-db:connect` Permission** – The IAM role used for ingestion must have a policy that allows the `rds-db:connect` action on the specific resource ARN for the database user. Example:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [{
       "Effect": "Allow",
       "Action": ["rds-db:connect"],
       "Resource": ["arn:aws:rds-db:region:account:dbuser:resource-id/user"]
     }]
   }
   ```
   Replace `region`, `account`, `resource-id`, and `user` with the appropriate values for your environment.

If any of these prerequisites are missing, authentication will fail, typically with a “PAM authentication failed for user” error.

## Common Error

**Error message**: `PAM authentication failed for user "<user>"`

**Cause**: One or more of the IAM prerequisites are not satisfied.

**Resolution**: Verify each requirement in order:
1. Confirm that IAM DB authentication is enabled on the RDS instance.
2. Check that the database user has been granted the `rds_iam` role.
3. Ensure the AWS role used for authentication includes the `rds-db:connect` permission with the correct resource ARN.

## SSL Recommendation

When using IAM authentication, it is recommended to pair it with an appropriate [[postgresql-ssl-modes|SSL mode]], such as `allow`.