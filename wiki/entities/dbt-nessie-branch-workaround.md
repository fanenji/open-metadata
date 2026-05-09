---
type: entity
title: dbt Nessie Branch Workaround
created: 2026-02-17
updated: 2026-02-17
tags: [dbt, nessie, dremio, macro-override, branch-versioning]
related: [nessie-catalog-versioning, dremio-mcp-server, data-lakehouse-versioning-strategies, dbt-dispatch-pattern]
sources: ["DBT - NOTE.md"]
---
# dbt Nessie Branch Workaround

A practical workaround for the dbt-dremio adapter's lack of native Nessie branch support. The technique overrides adapter macros to inject `AT BRANCH <name>` into SQL statements.

## Implementation

1. **Override `create_table_as` macro** — Custom macro that adds `AT BRANCH {{ var("branch") }}` to the `CREATE TABLE` statement.
2. **Override `relation` macro** — Custom macro that adds branch awareness to relation references.
3. **Configure dispatch** — In `dbt_project.yml`, set the dispatch search order to route macro calls to the custom project before falling back to the adapter:
   ```yaml
   dispatch:
     - macro_namespace: dbt_dremio
       search_order: ['test_nessie_branch', 'dbt_dremio']
   ```
4. **Inject branch variable** — Pass the branch name via `--vars`, `dbt_project.yml`, or environment variable:
   ```bash
   dbt run --select raw --vars '{"branch": "test_nessie_branch"}' --debug
   ```
5. **Create branch** — A `pre_hook` on raw models creates the branch if it does not exist:
   ```sql
   CREATE BRANCH IF NOT EXISTS test_dbt_create_branch IN Nessie;
   ```

## Limitations

- The `pre_hook` approach is acknowledged as a TODO — it should be refactored into an ad-hoc macro.
- The pattern has been tested with table materializations; compatibility with incremental materializations is unverified.
- Stability across dbt-dremio adapter version upgrades is unknown.

## References

- Original Dremio community discussion: [How work with branch using dbt-dremio-nessie](https://community.dremio.com/t/how-work-with-branch-using-dbt-dremio-nessie/11792/4)
- Original adapter macros: [dbt-dremio create_table_as](https://github.com/dremio/dbt-dremio/blob/main/dbt/include/dremio/macros/materializations/table/create_table_as.sql), [dbt-dremio relation](https://github.com/dremio/dbt-dremio/blob/main/dbt/include/dremio/macros/adapters/relation.sql)