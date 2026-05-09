---
type: concept
title: Kubernetes Local Data Access
created: 2026-03-15
updated: 2026-03-15
tags: [kubernetes, local-development, data-access, storage, geospatial]
related: [kubernetes, orbstack, minikube, kind, k3d, rancher-desktop, geospatial-docker-base-images]
sources: ["Kubernetes Development on macOS Guide.md"]
---
# Kubernetes Local Data Access

Accessing local data files (Shapefiles, GeoTIFFs, CSVs) from containers running in a local Kubernetes cluster presents specific challenges because Pods run in an isolated environment separate from the macOS host filesystem.

## Challenge

Pods run within the isolated environment of the Kubernetes cluster, which may itself be inside a VM (Minikube, Docker Desktop) or a container (Kind, k3d). Direct mapping from the macOS host requires tool-specific support.

## Solutions

### Volume Mounting (Host Path)

Kubernetes supports `hostPath` volumes, but behavior varies by tool:

- **OrbStack**: Provides optimized file sharing (VirtioFS) and likely supports standard hostPath volumes mapping effectively to the macOS filesystem.
- **Rancher Desktop / Docker Desktop**: Typically allow hostPath volumes to map to the macOS host filesystem via their file-sharing mechanisms.
- **Minikube**: hostPath mounts map to paths inside the Minikube VM. Use `minikube mount <host-src>:<vm-dest>` to create a persistent mount from macOS into the VM.
- **Kind / k3d**: Nodes are Docker containers. Configure at cluster creation time: `extraMounts` in Kind config, `-v /host/path:/container/path` in k3d cluster create.

### kubectl cp

Manually copy data into/out of Pods. Suitable for small files or occasional transfers, but cumbersome for large datasets or frequent iteration.

### Local Object Storage (MinIO)

Deploy MinIO within the local K8s cluster (using its Helm chart or Operator). Upload data to MinIO buckets. Modify ETL scripts to read/write data using an S3-compatible library (boto3) pointed at the local MinIO service endpoint. This approach adds complexity but more closely mimics cloud-native workflows.

## Recommendation

For straightforward local development, investigate the host volume mounting capabilities of your chosen tool (OrbStack, Rancher Desktop). This is often the most direct way to work with local data files.