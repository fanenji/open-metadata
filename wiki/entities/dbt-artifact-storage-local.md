---
type: entity
title: dbt Artifact Storage - Local Filesystem
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, artifact-storage, local-filesystem, configuration]
related: [dbt-artifact-storage, dbt-artifacts, dbt-integration, nfs-subdir-external-provisioner, kubernetes]
sources: ["dbt-artifact-storage---local-filesystem-configurat-20260514.md"]
---

# dbt Artifact Storage - Local Filesystem

The local/shared filesystem configuration for [[dbt]] artifact storage is a deployment pattern where dbt Core-generated JSON artifacts (manifest.json, catalog.json, run_results.json) are stored on a filesystem accessible by both dbt and [[OpenMetadata]]. This is the simplest setup for development and single-server deployments but is not recommended for production distributed systems.

## Configuration Options

Four configuration options are documented:

1. **Same Machine (Development)** — dbt and OpenMetadata run on the same machine; artifacts are read directly from the dbt project's `target/` directory using absolute paths.
2. **Docker Compose with Shared Volume** — A named Docker volume (`dbt-artifacts`) is shared between the dbt and OpenMetadata containers; dbt copies artifacts to the shared volume after generation.
3. **Kubernetes with PersistentVolumeClaim** — A PVC with `ReadWriteMany` access mode is created and mounted into both the dbt CronJob pod and the OpenMetadata deployment pod.
4. **NFS Mounted Shared Storage** — An NFS export is mounted on both the dbt server and the OpenMetadata server; dbt copies artifacts to the NFS mount point.

## Key Requirements

- **Absolute Paths**: OpenMetadata requires absolute filesystem paths for artifact file configuration. Relative paths cause "File not found" errors.
- **Read Permissions**: Artifact files must be readable by the OpenMetadata process (`chmod 644`).
- **ReadWriteMany (RWX)**: For Kubernetes deployments, the PVC must use `ReadWriteMany` access mode. Works with NFS, EFS, Azure Files, and GlusterFS. Does not work with EBS (ReadWriteOnce only).
- **Artifact Copy Automation**: dbt-generated artifacts must be copied from the `target/` directory to the shared location. This is typically automated via a wrapper script or post-generation command.

## Limitations

- No built-in versioning or backup for artifact files.
- File locking issues are possible with concurrent access.
- Requires shared filesystem infrastructure.
- Not recommended for production distributed systems.

## Verification

```bash
# Verify artifacts exist and are readable
ls -la /dbt-artifacts/
cat /dbt-artifacts/manifest.json | jq '.metadata.dbt_version'

# Check from OpenMetadata's perspective (if in Docker)
docker exec collate-container ls -la /dbt-artifacts/
docker exec collate-container cat /dbt-artifacts/manifest.json | jq '.'
```

## Troubleshooting

| Issue | Symptom | Solution |
|-------|---------|----------|
| File not found | "No such file or directory" | Verify absolute path is correct and accessible from OpenMetadata |
| Permission denied | "Permission denied" | Run `chmod 644 /dbt-artifacts/*.json` |
| Stale data | Old metadata showing | Ensure dbt writes artifacts before OpenMetadata reads |
| Mount issue | "Transport endpoint not connected" | Check NFS mount: `mount \| grep dbt-artifacts` |
| Volume not shared | Works for dbt, not OpenMetadata | Verify both containers/pods mount the same volume |

## Related Pages

- [[dbt-artifact-storage]] — Overview of all dbt artifact storage backends
- [[dbt-artifacts]] — Reference for manifest.json, catalog.json, and run_results.json
- [[dbt-integration]] — Overview of the dbt-OpenMetadata integration
- [[nfs-subdir-external-provisioner]] — Kubernetes external provisioner for dynamic NFS PVCs