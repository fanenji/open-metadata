---
type: source
title: "dbt Artifact Storage - Local Filesystem Configuration | OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, artifact-storage, local-filesystem, configuration, openmetadata]
related: [dbt-artifact-storage, dbt-artifact-storage-local, dbt-integration, dbt-artifacts, nfs-subdir-external-provisioner, kubernetes]
sources: ["dbt-artifact-storage---local-filesystem-configurat-20260514.md"]
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/storage-local-guide"
venue: OpenMetadata Documentation
---

# dbt Artifact Storage - Local Filesystem Configuration

This source is the official OpenMetadata v1.12.x documentation for configuring a local or shared filesystem as the artifact storage layer for the [[dbt]] Core + [[OpenMetadata]] integration. It covers four configuration options: same machine (development), Docker Compose with shared volume, Kubernetes with PersistentVolumeClaim, and NFS mounted shared storage. The guide emphasizes that local filesystem storage is ideal for development and single-server deployments but is not recommended for production distributed systems, where cloud storage (S3, GCS, Azure) should be used.

Key topics include the absolute path requirement for artifact file configuration, the ReadWriteMany access mode prerequisite for Kubernetes, artifact copy automation patterns, and troubleshooting common issues such as "File not found" and permission denied errors. The source provides concrete YAML examples, command snippets, and a verification procedure.

This source strengthens the existing [[dbt-artifact-storage]] concept page by adding detailed local filesystem configuration guidance alongside the previously documented S3, GCS, Azure, and HTTP storage backends. It also extends the [[nfs-subdir-external-provisioner]] entity page with a concrete NFS mount pattern for dbt artifacts.