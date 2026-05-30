---
type: concept
title: Local/Shared Filesystem Artifact Storage
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, artifact-storage, local-filesystem, configuration, kubernetes]
related: [dbt-artifact-storage, dbt-artifact-storage-local, dbt-artifacts, dbt-integration, readwritemany, nfs-subdir-external-provisioner]
sources: ["dbt-artifact-storage---local-filesystem-configurat-20260514.md"]
---

# Local/Shared Filesystem Artifact Storage

Local/shared filesystem artifact storage is a configuration pattern for the [[dbt]]-[[OpenMetadata]] integration where dbt Core-generated JSON artifacts (manifest.json, catalog.json, run_results.json) are stored on a filesystem accessible by both dbt and OpenMetadata. This is the simplest storage backend to set up but carries significant production limitations.

## When to Use

- **Development environments** — Quick setup for testing the dbt-OpenMetadata integration.
- **Single-server deployments** — dbt and OpenMetadata run on the same machine or VM.
- **Proof-of-concept projects** — Before migrating to cloud storage for production.

## When to Avoid

- **Production distributed systems** — Not recommended due to lack of versioning, backup, and potential file locking issues.
- **Multi-server deployments** — Requires shared filesystem infrastructure (NFS, EFS) which adds complexity.
- **High-concurrency scenarios** — Concurrent artifact reads from multiple ingestion pipelines may cause file locking problems.

## Key Constraints

- **Absolute Path Requirement**: OpenMetadata requires absolute filesystem paths for artifact file configuration. Relative paths cause "File not found" errors.
- **ReadWriteMany (RWX)**: For Kubernetes deployments, the PVC must use `ReadWriteMany` access mode. Works with NFS, EFS, Azure Files, and GlusterFS. Does not work with EBS (ReadWriteOnce only).
- **Artifact Copy Automation**: dbt-generated artifacts must be copied from the `target/` directory to the shared location. This is typically automated via a wrapper script or post-generation command.

## Relationship to Other Storage Backends

The local/shared filesystem is one of five documented storage backends for dbt artifacts. The others are [[dbt-artifact-storage|S3, GCS, Azure, and HTTP]]. For production deployments, cloud storage is strongly recommended over local filesystem.

## Related Pages

- [[dbt-artifact-storage]] — Overview of all dbt artifact storage backends
- [[dbt-artifact-storage-local]] — Entity page for local filesystem configuration
- [[dbt-artifacts]] — Reference for manifest.json, catalog.json, and run_results.json
- [[dbt-integration]] — Overview of the dbt-OpenMetadata integration
- [[nfs-subdir-external-provisioner]] — Kubernetes external provisioner for dynamic NFS PVCs