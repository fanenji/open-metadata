---
type: concept
title: Custom Property Types
created: 2026-05-14
updated: 2026-05-14
tags: [custom-properties, metadata-extension, data-types]
related: [custom-properties, custom-property-naming-conventions, schema-first-approach]
sources: ["how-to-create-a-custom-property-for-a-data-asset---20260514.md"]
---

# Custom Property Types

OpenMetadata supports 18 data types for custom properties, enabling organizations to extend metadata models with fields ranging from simple strings to complex entity references.

## Supported Types

| Type | Description | Use Case |
|------|-------------|----------|
| Date | Calendar date | Expiration date, review date |
| DateTime | Date and time | Last reviewed timestamp |
| Duration | Time duration | Data retention period |
| Email | Email address | Contact email for data steward |
| Entity Reference | Reference to another entity | Link to a related Glossary Term |
| Entity Reference List | List of entity references | Multiple related data assets |
| Enum | Enumeration of allowed values | Data sensitivity level (Low/Medium/High) |
| Integer | Whole number | Row count threshold |
| Markdown | Rich text with Markdown formatting | Detailed usage notes |
| Number | Numeric value | Cost per query |
| SQL Query | SQL query text | Sample query for the asset |
| String | Text string | Business description |
| Table | Reference to a table entity | Source table for a dashboard |
| Time | Time of day | Scheduled refresh time |
| Time Interval | Time range | Active data window |
| Timestamp | Unix timestamp | Last modified timestamp |

## Usage Notes

- Complex types like Entity Reference, Entity Reference List, and Table enable rich metadata modeling by linking assets together.
- The SQL Query type allows embedding example queries directly in metadata.
- Enum types require defining allowed values during property creation.

## Related

- [[custom-properties]] — The overall mechanism for extending data models.
- [[custom-property-naming-conventions]] — Rules for naming custom properties.
- [[schema-first-approach]] — The architectural principle enabling custom properties.