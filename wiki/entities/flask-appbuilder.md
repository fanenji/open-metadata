---
type: entity
title: Flask AppBuilder
created: 2026-05-07
updated: 2026-05-07
tags: [authentication, authorization, framework, python]
related: [apache-airflow, reverse-proxy-authentication-pattern]
sources: ["Orchestrazione Data Platform - Analisi Comparativa.md"]
---
# Flask AppBuilder

Flask AppBuilder (FAB) is the authentication and RBAC framework used by Apache Airflow. It provides a mature, integrated security layer for Flask-based web applications.

## Capabilities

- **Authentication**: Supports database-based auth, LDAP, OAuth/OIDC, and SAML (via custom security managers)
- **Authorization**: Provides a complete RBAC system with predefined roles (Admin, User, Viewer, Op, Public) and the ability to create custom roles with granular permissions, including DAG-level access control
- **Fernet Key Encryption**: Used by Airflow to encrypt sensitive data in the metadata database

## Relevance

FAB is the reason Airflow has the most mature native auth among OSS orchestrators. Its capabilities enable Airflow to support enterprise authentication requirements without external components, though configuration complexity remains.

## Related Pages

- [[apache-airflow]] — Primary user of Flask AppBuilder
- [[reverse-proxy-authentication-pattern]] — Alternative approach for tools without FAB