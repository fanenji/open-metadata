---
type: concept
title: Kubernetes Secrets Management
created: 2026-02-13
updated: 2026-05-07
tags: [kubernetes, security, secrets, configuration, best-practices, helm-for-data-platforms, kubernetes-probes, kubernetes-jobs-cronjobs]
related: [kubernetes-development-best-practices, kubernetes-geospatial-etl-deployment, kubernetes-fastapi-deployment, kubernetes-airflow-deployment-local, kubernetes-prefect-deployment-local, kubernetes, helm-for-data-platforms, kubernetes-probes, kubernetes-jobs-cronjobs]
sources: ["Kubernetes Dev Environment on MacBook_ .md", "Kubernetes Development on macOS Guide.md"]
---
# Kubernetes Secrets Management

Kubernetes Secrets are objects for storing sensitive data such as API keys, passwords, tokens, and certificates. They are a critical component of secure application deployment on Kubernetes.

## Core Principles

- **Never hardcode** credentials in application code, Dockerfiles, or ConfigMaps.
- **Use Kubernetes Secrets** to store sensitive data.
- **Apply the principle of least privilege** using RBAC to restrict access to Secrets.
- **Enable encryption at rest** for Secrets in etcd for production environments.
- **Rotate secrets regularly.**

## Creating Secrets

Secrets can be created imperatively or declaratively:

```bash
# Imperative (recommended for simplicity)
kubectl create secret generic oracle-db-secret \
  --from-literal=username=myuser \
  --from-literal=password=mypassword \
  --from-literal=dsn=myhost.example.com:1521/ORCLPDB1

# From files
kubectl create secret generic ssh-key-secret \
  --from-file=id_rsa=~/.ssh/id_rsa
```

For declarative management, define a YAML manifest with base64-encoded `data` values. Store such manifests in version control with encrypted values (e.g., using Sealed Secrets or External Secrets Operator).

## Mounting Secrets into Pods

### As Volume Mounts (Recommended)

Each key in the Secret's `data` field becomes a file under the mount path. The application reads credentials from these files.

```yaml
spec:
  containers:
  - name: my-app
    volumeMounts:
    - name: oracle-credentials
      mountPath: "/etc/secrets/oracle"
      readOnly: true
  volumes:
  - name: oracle-credentials
    secret:
      secretName: oracle-db-secret
```

Advantages:
- Secrets are updated automatically if the Secret object changes (application may need a reload mechanism).
- Setting `readOnly: true` minimizes the risk of accidental modification.
- Preferred over environment variables for multiple keys/files.

### As Environment Variables

```yaml
env:
- name: ORACLE_USER
  valueFrom:
    secretKeyRef:
      name: oracle-db-secret
      key: username
```

Or inject all keys from a secret:

```yaml
envFrom:
- secretRef:
    name: oracle-db-secret
```

**Note:** Environment variables do not update automatically if the Secret changes; a Pod restart is required.

## Best Practices

- **Restrict Secret access** to only the containers within a Pod that need it.
- **Avoid logging** sensitive data retrieved from Secrets.
- **Use separate Secrets** for different purposes (e.g., one for Oracle, one for PostGIS, one for API keys).
- **Prefer volume mounts** over environment variables for configuration that might change.
- **Store Secret manifests in version control** with values encrypted (e.g., using Sealed Secrets, External Secrets Operator) or using tools like Helm secrets.