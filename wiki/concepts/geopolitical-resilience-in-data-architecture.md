---
type: concept
title: Geopolitical Resilience in Data Architecture
created: 2026-04-29
updated: 2026-04-29
tags: [architecture, risk-management, cloud, multi-cloud]
related: [cloud-native-data-systems, designing-data-intensive-applications, data-lakehouse]
sources: ["Designing Data-intensive Applications with Martin Kleppmann.md"]
---
# Geopolitical Resilience in Data Architecture

Geopolitical resilience in data architecture refers to designing data systems to withstand geopolitical risks, such as the possibility of being locked out of cloud services due to international tensions or regulatory changes.

## The Risk

[[martin-kleppmann]] raised this concern in the context of European dependence on US cloud services (AWS, GCP, Azure). While he considers a complete lockout unlikely, he argues it is "no longer unthinkable" given recent geopolitical tensions. This is a business risk that architects should consider for critical workloads.

## Mitigation Strategies

- **Multi-cloud setup** — Running workloads across multiple cloud providers so that if one provider becomes unavailable (due to geopolitical or other reasons), the system can continue operating on another.
- **Multi-region deployment** — Deploying across multiple geographic regions within a single cloud provider to tolerate regional outages.
- **Hybrid cloud** — Combining on-premises infrastructure with cloud services to maintain fallback capacity.
- **Open standards** — Using open formats (Parquet, Iceberg) and portable abstractions to avoid vendor lock-in.

## Trade-offs

- **Cost** — Multi-cloud and multi-region setups are significantly more expensive to design, operate, and maintain.
- **Complexity** — Consistency models become more complex across regions and providers.
- **Human overhead** — Operating multiple cloud environments requires specialized skills and additional team capacity.

## Connection to Wiki

- [[cloud-native-data-systems]] — Cloud-native architectures enable multi-cloud and multi-region patterns.
- [[data-lakehouse]] — Lakehouse architectures with open formats (Iceberg) facilitate portability across clouds.
- [[designing-data-intensive-applications]] — DDIA's second edition adds coverage of multi-region and multi-cloud considerations.