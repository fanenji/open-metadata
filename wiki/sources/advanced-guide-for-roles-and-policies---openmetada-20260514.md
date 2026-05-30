---
type: source
title: "Advanced Guide for Roles and Policies - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [roles, policies, authorization, rbac, abac, access-control, authentication, bots]
related: [roles-and-policies, viewbasic-viewall-operations, bot-authentication, hybrid-rbac-abac-model, teams-and-users, google-oauth, openmetadata-administration]
sources: ["advanced-guide-for-roles-and-policies---openmetada-20260514.md"]
authors: ["OpenMetadata"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/roles-policies"
venue: "OpenMetadata Official Documentation v1.12.x"
---
# Advanced Guide for Roles and Policies - OpenMetadata Documentation

This source is the official OpenMetadata v1.12.x advanced guide covering the platform's access control design. It details the hybrid RBAC-ABAC authorization model, the authentication flow for both human users (SSO) and bots (JWT via SSL certificates), and the three-factor authorization framework (user identity, resource attributes, requested operation). A critical section distinguishes between the `ViewBasic` and `ViewAll` operations, defining exactly which metadata fields each grants access to. The document also reiterates the hierarchical team structure as the foundation for access control, emphasizing that only `Group` teams can own data assets. The content ends with navigation links to subsequent pages on "Building Blocks of Authorization" and "Use Cases," indicating the guide is part of a multi-page series.