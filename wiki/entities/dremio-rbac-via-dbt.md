type: entity
title: Dremio RBAC via dbt
created: 2026-05-07
updated: 2026-05-07
tags: [dremio, rbac, security, dbt, governance]
related: [dremio, dremio-semantic-layer-ci-cd, dbt-dremio-adapter]
sources: ["semantic-layer-ci-cd-with-dremio-and-dbt.pdf"]
---
# Dremio RBAC via dbt

Dremio's Role-Based Access Control (RBAC) can be managed through dbt using SQL grants and UDF-based row/column-level security policies.

## RBAC Grants

While dbt's built-in `grants` functionality supports view/table-level privileges, the recommended approach is to set access controls at the folder or space level for better manageability. This is done using the `on-run-end` hook in `dbt_project.yml`:

```yaml
on-run-end:
  - "GRANT SELECT ON SPACE dbt_demo_space TO ROLE dremio_user"
```

## Row/Column-Level Security via UDFs

Dremio-native row-access and column-masking policies can be applied using UDFs via dbt's `post-hook` functionality:

1. **Define the UDF** in a dbt macro:
```sql
CREATE OR REPLACE FUNCTION {{ folder_path }}.rls_udf (passenger_count INTEGER)
RETURNS BOOLEAN
RETURN SELECT is_member('ADMIN') OR passenger_count > 1
```

2. **Apply the policy** in a model's post-hook:
```sql
{{ config(
    post_hook='ALTER VIEW {{ this }} ADD ROW ACCESS POLICY
               "dremio_space".rls_udf(passenger_count)'
) }}
```

## Best Practices

- Manage users and roles through a central enterprise identity provider (Azure AD, Okta, LDAP), not via dbt
- Grant privileges at the folder/space level rather than individual views/tables
- Use `on-run-start` for UDF creation and `on-run-end` for RBAC grants
- Ensure UDFs are created before the views that reference them (use DAG ordering)
