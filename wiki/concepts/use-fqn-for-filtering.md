---
type: concept
title: useFqnForFiltering
created: 2026-05-14
updated: 2026-05-14
tags: [auto-classification, ingestion-framework, filtering, configuration]
related: [auto-classification-external-workflow, filter-patterns, auto-classification]
sources: ["external-auto-classification-workflow---openmetada-20260514.md"]
---
# useFqnForFiltering

`useFqnForFiltering` is a boolean configuration parameter in the Auto Classification workflow that determines how filter patterns are matched against database objects.

## Behavior

- **`false` (default)**: Filter patterns are applied to raw object names. For example, a table filter pattern `includes: [abc]` matches any table named `abc`, regardless of which database or schema it belongs to.

- **`true`**: Filter patterns are applied to the Fully Qualified Name (FQN) of objects. The FQN format is `service_name.database_name.schema_name.table_name`. A pattern `includes: [my_service.my_db.*.abc]` would match table `abc` only in the specified service and database, across all schemas.

## Use Cases

- **Use `false`** when you want broad, name-based filtering across all databases and schemas.
- **Use `true`** when you need precise, scoped filtering — for example, when the same table name exists in multiple databases or schemas and you only want to classify one of them.

## Configuration

```yaml
sourceConfig:
  config:
    type: AutoClassification
    useFqnForFiltering: true
    databaseFilterPattern:
      includes:
        - my_database
    schemaFilterPattern:
      includes:
        - public
    tableFilterPattern:
      includes:
        - users
```

With `useFqnForFiltering: true`, the above configuration would only match tables with FQN matching `*.my_database.public.users`.