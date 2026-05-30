---
type: entity
title: "Cloudfront"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: entity
title: CloudFront
created: 2026-05-14
updated: 2026-05-14
tags: [aws, cdn, http-server, configuration, openmetadata]
related: [http-artifact-storage, dbt-artifact-storage, dbt-integration, s3]
sources: ["dbt-artifact-storage---http-server-configuration-o-20260514.md"]
---

# CloudFront

Amazon CloudFront is a content delivery network (CDN) service offered by AWS. In the context of OpenMetadata's [[dbt-integration]], CloudFront is the recommended HTTP server option for serving dbt JSON artifacts, combining S3 storage with CDN capabilities for HTTPS and global access.

## Configuration for dbt Artifacts

The recommended setup involves:
1. Creating an S3 bucket and uploading dbt artifacts (following the S3 configuration guide)
2. Creating a CloudFront distribution pointing to the S3 bucket as the origin
3. Configuring OpenMetadata with the CloudFront URL (e.g., `https://d123abc.cloudfront.net/dbt/`)

## Advantages

- **HTTPS**: Built-in SSL/TLS support
- **Global Access**: Edge locations for low-latency worldwide access
- **Managed Infrastructure**: No server maintenance required
- **Scalability**: Automatically handles traffic spikes

## Relationship

CloudFront is the recommended option within the [[http-artifact-storage]] pattern, preferred over self-managed Nginx or Apache servers for production deployments.