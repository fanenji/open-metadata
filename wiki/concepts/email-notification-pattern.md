---
type: concept
title: Email Notification Pattern
created: 2026-05-07
updated: 2026-05-07
tags: [email, notification, smtp, etl, monitoring]
related: [geoscript-rest-api-architecture, celery-integration-pattern, fastapi-background-tasks-pattern]
sources: ["GEOSCRIPTS - REST API.md"]
---
# Email Notification Pattern

The email notification pattern sends email messages after background script execution, providing operational feedback on success or failure. This pattern is used in the geoscript REST API to notify operators of ETL job completion.

## Configuration

Email configuration is stored in a `.env` file:
- `SMTP_MAIL_SERVER`: SMTP server address
- `FROM_ADDRESS`: Sender email address
- `ERROR_TO_ADDRESS`: Default recipient for error notifications
- `OK_TO_ADDRESS`: Default recipient for success notifications

## Recipient Selection

1. If an `email` parameter is provided in the API request, it is used as the recipient
2. If no `email` parameter is provided, `ERROR_TO_ADDRESS` is used for failures and `OK_TO_ADDRESS` for successes

## Related Pages

- [[geoscript-rest-api-architecture]] — Overall architecture context
- [[celery-integration-pattern]] — Celery tasks that trigger email notifications
- [[fastapi-background-tasks-pattern]] — Background tasks that trigger email notifications