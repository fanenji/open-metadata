---
type: entity
title: nfs-subdir-external-provisioner
created: 2026-05-14
updated: 2026-05-14
tags: [kubernetes, storage, nfs, provisioner, helm]
related: [helm-charts, airflow-storage-requirements, on-premises-kubernetes-deployment]
sources: ["OMD - Kubernetes On Premises.md"]
---

# nfs-subdir-external-provisioner

An external provisioner for Kubernetes that dynamically creates PersistentVolumes (PVs) from an existing NFS share. It is deployed via a Helm Chart and creates a StorageClass that can satisfy ReadWriteMany (RWX) access mode requirements.

## Role in OpenMetadata On-Premises Deployments

The OpenMetadata Helm Chart depends on Apache Airflow, which requires a PersistentVolume with ReadWriteMany access. In on-premises environments without cloud-native RWX storage, the `nfs-subdir-external-provisioner` provides a workaround by provisioning subdirectories on a pre-existing NFS server as individual PersistentVolumes.

## Installation

```bash
helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner

helm install nfs-subdir-external-provisioner nfs-subdir-external-provisioner/nfs-subdir-external-provisioner \
  --create-namespace \
  --namespace nfs-provisioner \
  --set nfs.server=<NFS_HOSTNAME_OR_IP> \
  --set nfs.path=/airflow
```

This creates a StorageClass named `nfs-subdir-external-provisioner` that can be used by PersistentVolumeClaims requiring RWX access.