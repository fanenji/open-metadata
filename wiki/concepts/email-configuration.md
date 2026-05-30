---
type: concept
title: Email Configuration (SMTP)
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, email, smtp, configuration, alerts, notifications]
related: [data-observability-alerts, openmetadata-administration, external-dependencies-configuration, system-notifications]
sources: ["email-alerts-configuration-openmetadata---openmeta-20260514.md"]
---

# Email Configuration (SMTP)

Email configuration in OpenMetadata is the process of setting up an SMTP server to enable the platform to send transactional and alert emails. This is a prerequisite for delivering [[data-observability-alerts]] and system notifications (sign-up confirmations, password resets) to users.

## Configuration Location

Navigate to **Settings > Preferences > Email** in the OpenMetadata UI.

## Configuration Fields

| Field | Description |
|-------|-------------|
| **Username** | SMTP account username for authentication. |
| **Password** | Password associated with the SMTP account username. |
| **Sender Email** | The email address that appears as the sender. Can differ from the username (e.g., Amazon SES). |
| **Server Endpoint** | SMTP server address (e.g., `smtp.gmail.com`, `smtp.sendgrid.net`, or your organization's SMTP). |
| **Server Port** | Port number determined by the transportation strategy (see below). |
| **Transportation Strategy** | Encryption mode for the SMTP connection (see below). |
| **Emailing Entity** | Customizable sender name appearing in email subjects and body; defaults to "OpenMetadata". |
| **Enable SMTP Server** | Toggle to activate or deactivate email notifications. |
| **Support URL** | Link included in emails for user support; defaults to `https://slack.open-metadata.org`. |

## Transportation Strategies

OpenMetadata supports three SMTP transportation strategies:

| Strategy | Port | Encryption | Recommendation |
|----------|------|------------|----------------|
| `SMTP` | 25 | None (unencrypted) | Not recommended for production |
| `SMTPS` | 465 | Implicit TLS | Acceptable for legacy systems |
| `SMTP_TLS` | 587 | Explicit TLS (STARTTLS) | **Recommended** |

## Dependency Chain

Email alerts require **both** of the following to be configured:

1. An [[data-observability-alerts|alert rule]] defining the trigger conditions and destination (email).
2. The SMTP configuration (this page) enabling the platform to send emails.

Without SMTP configuration, alert rules with email destinations will not deliver notifications.

## Best Practices

- Use `SMTP_TLS` (port 587) for secure, modern email delivery.
- Override the default Support URL with your organization's internal support channel or documentation.
- For services like Gmail, you may need an app-specific password rather than your regular account password.
- Test the configuration by triggering a test alert or password reset flow.

## Limitations & Open Questions

- The documentation only covers username/password authentication. Modern email services (Gmail, SendGrid) may require OAuth2, API keys, or app passwords — these are not explicitly documented.
- Rate limits or throttling considerations for high-volume alert environments are not addressed.
- Multiple recipient or distribution list support is not documented.