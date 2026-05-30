---
type: concept
title: Airflow Storage Requirements
created: 2026-05-14
updated: 2026-05-14
tags: [airflow, kubernetes, storage, nfs, persistent-volumes]
related: [on-premises-kubernetes-deployment, nfs-subdir-external-provisioner, helm-charts, kubernetes-native-orchestrator]
sources: ["OMD - Kubernetes On Premises.md"]
---

# Airflow Storage Requirements

A specific infrastructure requirement that arises when deploying OpenMetadata with the Airflow-dependent Helm Chart on Kubernetes. Apache Airflow expects a PersistentVolume with ReadWriteMany (RWX) access mode, meaning the volume can be mounted as read-write by multiple nodes simultaneously.

## Why RWX Is Required

Airflow's architecture in a Kubernetes deployment involves multiple components (scheduler, workers, web server) that may run on different nodes. These components need shared access to DAG files, logs, and other runtime data. A ReadWriteMany volume ensures all pods can read and write to the same storage location regardless of which node they are scheduled on.

## The NFS Workaround

In on-premises Kubernetes environments, native RWX storage options (such as cloud-provided file storage) are typically unavailable. The documented workaround involves:

1. **Setting up an NFS server** with a shared path (e.g., `/airflow`) accessible from all Kubernetes nodes.
2. **Installing the `nfs-subdir-external-provisioner`** Helm Chart to create a StorageClass that dynamically provisions subdirectories on the NFS share as PersistentVolumes.
3. **Configuring the OpenMetadata Helm Chart** to use this StorageClass for Airflow's PersistentVolumeClaims.

## Alternative Approaches

The [[kubernetes-native-orchestrator]] eliminates the Airflow dependency entirely, which also removes the RWX storage requirement. For teams evaluating on-premises deployments, this is a significant architectural consideration.