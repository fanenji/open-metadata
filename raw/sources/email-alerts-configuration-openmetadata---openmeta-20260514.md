---
type: clip
title: "Email Alerts Configuration | OpenMetadata - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/alerts-notifications/email-alerts-configuration"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Email Alerts Configuration | OpenMetadata - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/alerts-notifications/email-alerts-configuration

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationAlerts & NotificationsEmail Alerts Configuration | OpenMetadataHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData Quality and ObservabilityOverviewData QualityData ProfilerAlerts & NotificationsOverviewData Observability AlertsSystem & Governance NotificationsEmail Alerts ConfigurationSlack Alerts ConfigurationMicrosoft Teams Alerts ConfigurationGoogle Chat Alerts ConfigurationGeneric Webhook Alert ConfigurationIncident ManagerOn this pageEmail Alerts ConfigurationConfiguring Email SMTP SettingsEmail Configuration FieldsUsernamePasswordSender EmailServer EndpointServer PortTransportation StrategyEmailing EntityEnable SMTP ServerSupport URLDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Email Alerts Configuration

OpenMetadata can send emails for various events such as sign-up confirmations, password resets, and alert notifications. To enable email alerts, you must first configure the SMTP server in the OpenMetadata platform.

​Configuring Email SMTP Settings

To configure email notifications in OpenMetadata, navigate to Settings > Preferences > Email.

​Email Configuration Fields

​Username

The username of your SMTP account used for authentication.

​Password

The password associated with the SMTP account username.

​Sender Email

The email address that will appear as the sender in emails. This can be the same as the username, but some services like Amazon SES may allow a different email address.

​Server Endpoint

The endpoint of your SMTP server. Examples:

smtp.gmail.com (for Gmail)

smtp.sendgrid.net (for SendGrid)

Your organization’s SMTP server address

​Server Port

The port number of the SMTP server. The port depends on the transportation strategy:

Transportation StrategyPortDescriptionSMTP25Standard unencrypted SMTPSMTPS465SMTP with implicit TLS encryptionSMTP_TLS587SMTP with explicit TLS encryption (recommended)

​Transportation Strategy

Select the appropriate transportation strategy based on your SMTP server configuration:

SMTP: For unencrypted connections (port 25)

SMTPS: For implicit TLS encryption (port 465)

SMTP_TLS: For explicit TLS encryption (port 587) - Recommended

​Emailing Entity

The name of the entity that appears in email subjects and content. By default, this is set to “OpenMetadata”.

For example, if you set this to “JohnDoe”, emails will show “JohnDoe” instead of “OpenMetadata” in the subject lines and email body.

​Enable SMTP Server

A toggle to enable or disable the SMTP configuration. Set to true to activate email notifications, or false to disable them.

​Support URL

A support URL link that will be included in emails for users to reach out in case of issues.

Default: https://slack.open-metadata.org

You can update this to point to your internal support channels or documentation.Was this page helpful?YesNoSuggest editsRaise issueSystem & Governance Notifications | OpenMetadataPreviousSlack Alerts Configuration | OpenMetadataNext⌘I
