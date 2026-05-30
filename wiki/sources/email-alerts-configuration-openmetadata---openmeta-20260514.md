---
type: source
title: Email Alerts Configuration | OpenMetadata - OpenMetadata Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, email, smtp, alerts, notifications, configuration]
related: [email-configuration, data-observability-alerts, openmetadata-administration, external-dependencies-configuration]
sources: ["email-alerts-configuration-openmetadata---openmeta-20260514.md"]
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/alerts-notifications/email-alerts-configuration"
venue: "OpenMetadata Documentation"
---

# Email Alerts Configuration | OpenMetadata - OpenMetadata Documentation

This source is the official OpenMetadata v1.12.x documentation page for configuring email alerts via SMTP. It provides a step-by-step guide for setting up the SMTP server in OpenMetadata (Settings > Preferences > Email), covering all configuration fields: Username, Password, Sender Email, Server Endpoint, Server Port, Transportation Strategy, Emailing Entity, Enable SMTP Server toggle, and Support URL.

The page documents three transportation strategies — `SMTP` (unencrypted, port 25), `SMTPS` (implicit TLS, port 465), and `SMTP_TLS` (explicit TLS, port 587, recommended) — and explains that email alerts are required for delivering notifications for sign-up confirmations, password resets, and alert notifications. The default Support URL points to the OpenMetadata Slack community (`https://slack.open-metadata.org`).

This source fills a critical gap in the alert notification pipeline: while [[data-observability-alerts]] describes alert rules and destinations, this page provides the prerequisite SMTP configuration needed to actually deliver email notifications. It is a dependency for any organization that wants email-based alerting.