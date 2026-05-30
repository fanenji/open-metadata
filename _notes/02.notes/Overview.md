

**OpenMetadata** is an open-source, cloud-native data metadata platform that serves as a centralized **data catalog** for modern data stacks. It automatically collects, organizes, and exposes metadata from databases, BI tools, data pipelines, cloud services, and more, making it easier for teams to discover, understand, govern, and trust their data.

### Core Capabilities
- **Automated Metadata Ingestion**: 100+ native connectors (Snowflake, BigQuery, Redshift, Kafka, dbt, Airflow, GCP/AWS/Azure services, etc.) that sync metadata, schemas, ownership, and usage stats.
- **Data Discovery & Search**: Intuitive UI + REST/GraphQL APIs for fast dataset search, filtering, and exploration.
- **End-to-End Data Lineage**: Visual, automated lineage tracking across ELT pipelines, transformations, and report dependencies.
- **Collaboration & Documentation**: Comments, tags, ratings, custom profiles, and team assignments to turn raw metadata into actionable context.
- **Data Governance & Compliance**: Classifications, privacy tags, policy hints, audit trails, and role-based access control to support regulatory needs.
- **Open Metadata Specification (OMS)**: A vendor-neutral schema that standardizes how metadata is defined, stored, and shared across tools.

### Technical Architecture
- **Backend**: Java (Spring Boot)
- **Frontend**: React
- **Storage**: PostgreSQL (metadata), OpenSearch (full-text & vector search)
- **Auth**: SSO/SAML/OAuth, LDAP, RBAC
- **Extensibility**: Plugin-based ingestion pipelines, custom workflows, and open APIs

###  Why Teams Use It
- Replaces fragmented metadata across dozens of tools
- Accelerates self-service analytics & data democratization
- Improves data trust, compliance, and lineage transparency
- Fully open-source (Apache 2.0) with a strong community & frequent releases

