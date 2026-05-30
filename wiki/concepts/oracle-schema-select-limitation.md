---
type: concept
title: Oracle Schema-Level SELECT Limitation
created: 2026-05-14
updated: 2026-05-14
tags: [oracle, permissions, security, ingestion, data-quality]
related: [oracle-connector, data-profiling, data-quality]
sources: ["Oracle Connector  OpenMetadata Enterprise Database Guide.md"]
---
# Oracle Schema-Level SELECT Limitation

Oracle Database does not provide a native, out-of-the-box mechanism to grant `SELECT` privileges on all tables within a schema in a single statement. This is a platform limitation that affects OpenMetadata's [[data-profiling|Profiler]] and [[data-quality|Data Quality]] workflows when ingesting from Oracle sources.

## Impact on OpenMetadata

The base permissions for metadata ingestion — `CREATE SESSION` and `SELECT_CATALOG_ROLE` — are sufficient to read data dictionary views and extract structural metadata. However, Profiler and Data Quality workflows require actual `SELECT` access on the tables being analyzed. Because Oracle lacks a schema-level grant, administrators must choose between:

1. **`SELECT ANY TABLE`**: A system privilege that grants read access to all tables in the database. This is the simplest approach but may violate least-privilege security policies.
2. **Per-table grants**: Explicit `GRANT SELECT ON {schema}.{table}` statements for each table. This is more secure but requires ongoing maintenance as new tables are created.

## Comparison with Other Databases

| Database | Schema-Level SELECT Support |
|----------|----------------------------|
| PostgreSQL | `GRANT SELECT ON ALL TABLES IN SCHEMA {schema} TO {role}` |
| MySQL | `GRANT SELECT ON {database}.* TO {user}` |
| Oracle | No native equivalent; workarounds required |

## Workaround Scripts

Oracle DBAs often use PL/SQL scripts to iterate over `ALL_TABLES` and dynamically grant `SELECT` on each table. Example:

```sql
BEGIN
  FOR t IN (SELECT table_name FROM all_tables WHERE owner = 'TARGET_SCHEMA') LOOP
    EXECUTE IMMEDIATE 'GRANT SELECT ON TARGET_SCHEMA.' || t.table_name || ' TO my_role';
  END LOOP;
END;
```

This script must be re-run whenever new tables are added to the schema.

## See Also

- [[oracle-connector]] — Full Oracle connector documentation
- [[data-profiling]] — Profiler workflow requirements
- [[data-quality]] — Data quality test configuration