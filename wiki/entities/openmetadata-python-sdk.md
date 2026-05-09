---
type: entity
title: OpenMetadata Python SDK
created: 2026-04-05
updated: 2026-04-05
tags: [openmetadata, python, sdk, automation, api]
related: [openmetadata, openmetadata-ingestion-framework, openmetadata-lineage, custom-connector-openmetadata]
sources: ["OpenMetadata - The Complete Guide Every Data Engineer Needs to Read.md"]
---
# OpenMetadata Python SDK

The Python SDK enables programmatic automation of all OpenMetadata operations.

## Installation

```bash
pip install openmetadata-ingestion
```

## Connect and Authenticate

```python
from metadata.ingestion.ometa.ometa_api import OpenMetadata
from metadata.generated.schema.entity.services.connections.metadata.openMetadataConnection import (
    OpenMetadataConnection,
)
from metadata.generated.schema.security.client.openMetadataJWTClientConfig import (
    OpenMetadataJWTClientConfig,
)

config = OpenMetadataConnection(
    hostPort="http://localhost:8585/api",
    authProvider="openmetadata",
    securityConfig=OpenMetadataJWTClientConfig(
        jwtToken="your-jwt-token"
    ),
)
metadata = OpenMetadata(config)
```

## Search and Retrieve Assets

```python
from metadata.generated.schema.entity.data.table import Table

table = metadata.get_by_name(
    entity=Table,
    fqn="snowflake_service.analytics_db.public.orders"
)
print(table.name, table.description, table.owner)

tables = metadata.list_entities(entity=Table)
for t in tables.entities:
    print(t.fullyQualifiedName.__root__)
```

## Update Descriptions

```python
from metadata.generated.schema.type.basic import Markdown

metadata.patch_description(
    entity=Table,
    source=table,
    description="This table contains all confirmed orders from the production system."
)
```

## Add Custom Tags

```python
from metadata.generated.schema.type.tagLabel import TagLabel, TagSource, LabelType, State

tag_label = TagLabel(
    tagFQN="Classification.PII.Email",
    source=TagSource.Classification,
    labelType=LabelType.Automated,
    state=State.Confirmed
)
metadata.patch_tag(entity=Table, source=table, tag_label=tag_label)
```

## Create a Database Service

```python
from metadata.generated.schema.api.services.createDatabaseService import (
    CreateDatabaseServiceRequest,
)
from metadata.generated.schema.entity.services.databaseService import (
    DatabaseServiceType,
    DatabaseConnection,
)
from metadata.generated.schema.entity.services.connections.database.snowflakeConnection import (
    SnowflakeConnection,
)

create_service = CreateDatabaseServiceRequest(
    name="prod-snowflake",
    serviceType=DatabaseServiceType.Snowflake,
    connection=DatabaseConnection(
        config=SnowflakeConnection(
            username="data_engineer",
            password="secret",
            account="xy12345.snowflakecomputing.com",
            warehouse="COMPUTE_WH",
            database="ANALYTICS",
        )
    ),
)
service = metadata.create_or_update(create_service)
```