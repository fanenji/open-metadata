---
type: concept
title: IAM Policy Separation
tags: [aws, iam, security, least-privilege, s3]
related: [dbt-artifact-storage-s3, dbt-artifact-storage, dbt-integration]
sources: ["dbt-artifact-storage---aws-s3-configuration-openme-20260514.md"]
created: 2026-05-14
updated: 2026-05-14
---

# IAM Policy Separation

IAM Policy Separation is a security best practice for the [[dbt-artifact-storage-s3|dbt Artifact Storage S3]] configuration. It involves creating two distinct IAM policies with minimal permissions: one for the dbt/Airflow environment (write access) and one for OpenMetadata (read access).

## Rationale

By separating the policies, OpenMetadata never receives write access to the S3 bucket. This follows the least-privilege principle and limits the blast radius if either set of credentials is compromised.

## Write Policy

The write policy grants `s3:PutObject` and `s3:PutObjectAcl` on the artifact prefix, plus `s3:ListBucket` on the bucket. This is attached to the Airflow/ECS task role.

## Read Policy

The read policy grants `s3:GetObject` and `s3:ListBucket` on the bucket and artifact prefix. This is attached to the OpenMetadata service role or used with access keys.

## Implementation

The policies are created using the AWS CLI and attached to the appropriate IAM roles. See [[dbt-artifact-storage-s3]] for the complete policy JSON and CLI commands.