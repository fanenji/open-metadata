---
type: clip
title: "Customizable Landing Page with Pluggable Panels - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/persona-landing-page-customization/customizable-landing-page"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Customizable Landing Page with Pluggable Panels - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/persona-landing-page-customization/customizable-landing-page

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationPersona and Landing Page CustomizationCustomizable Landing Page with Pluggable PanelsHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsAdmin GuideOverviewHow to Ingest MetadataHow to Delete a Service ConnectionManage Teams and UsersAdvanced Guide for Roles and PoliciesCLI Ingestion with Basic AuthHow to Add Custom LogoReindexing SearchData InsightsPermission DebuggerPersona and Landing Page CustomizationOverviewHow to Customize a Landing PageHow to Define PersonasAudit LogsOn this pageCustomizable Landing Page with Pluggable PanelsHow to Customize a Landing Page:Example Use Case:Future Enhancements:Switching Between PersonasSetting a Default Persona:Use Case Examples:1. Data Engineer2. Data StewardFuture Customizations:1. Entity Pages Customization:2. Knowledge Panel Expansion:Documentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Customizable Landing Page with Pluggable Panels

OpenMetadata’s customizable landing page allows admins to tailor the layout based on the user’s persona, providing a more relevant and enriched experience. The landing page is built using pluggable panels, which can be added, removed, or rearranged to meet the unique needs of different personas, such as data scientists, data engineers, or data stewards.

​How to Customize a Landing Page:

Set Up Personas:

After defining personas, navigate to Settings > Persona.

Select a Persona:

Customize a landing page for a specific persona (e.g., data steward) and then select homepage to customize it.

Click on Add widget

Pluggable Panels:

Configure panels based on the needs of each persona by adding widgets as required and then click on apply. Panels can include:

Activity Feed

Key Performance Indicators (KPIs)

Recent Announcements

Tasks

Recently Viewed and more

Rearrange and Save:

Adjust the layout based on user preferences and save the configuration.

​Example Use Case:

For a data scientist, the KPI panel may be removed, while prioritizing recent announcements and recent views.

A data engineer might add a Pipeline Status panel, while a data steward might include panels focused on data governance.

​Future Enhancements:

Additional panels, such as Data Quality Status or Knowledge Articles, can be added to further personalize and enhance the user experience. By leveraging pluggable panels, the customizable landing page can be tailored to enrich each user’s experience, making the platform more relevant and effective for different personas.

​Switching Between Personas

Users can switch between different personas without logging out or reconfiguring the platform. Upon switching, the application’s landing page and configuration adjust automatically to reflect the new role.

​Setting a Default Persona:

Users can set a default persona, so the system displays the layout and settings relevant to that role every time they log in.

​Use Case Examples:

​1. Data Engineer

Needs: Data pipeline monitoring, data quality, and task management.

Customized Landing Page: Includes panels for pipeline status, data quality metrics, and recent tasks related to pipeline execution. Announcements and Insights KPIs might be deprioritized.

Persona-Specific Panels: Add a Pipeline Status panel for real-time updates on data workflows.

​2. Data Steward

Needs: Access to recent data views, performance indicators, and analysis tools.

Customized Landing Page: Prioritizes recent data views and KPI dashboards, while removing unnecessary panels such as pipeline status.

Persona-Specific Panels: Data stewards might add panels related to KPIs or recently viewed data assets.

​Future Customizations:

OpenMetadata plans to expand persona-based customization beyond landing pages to entity pages as well. For example:

​1. Entity Pages Customization:

Users can add panels that display specific metadata, such as product-related knowledge articles or glossary terms associated with an entity.

​2. Knowledge Panel Expansion:

Additional panels like Product Knowledge Articles or Service Status will allow deeper insights based on the user’s role.Was this page helpful?YesNoSuggest editsRaise issuePersona and Landing Page Customization in OpenMetadataPreviousHow to Define Personas in OpenMetadataNext⌘I
