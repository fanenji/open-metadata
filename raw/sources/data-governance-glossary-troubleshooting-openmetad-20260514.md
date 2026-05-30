---
type: clip
title: "Data Governance Glossary Troubleshooting | OpenMetadata Guide - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/glossary/troubleshooting"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Data Governance Glossary Troubleshooting | OpenMetadata Guide - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/glossary/troubleshooting

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationGlossaryData Governance Glossary Troubleshooting | OpenMetadata GuideHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData GovernanceOverviewGlossaryOverviewWhat is a Glossary TermHow to Setup a GlossaryHow to Create Glossary TermsHow to Bulk Import a GlossaryGlossary ExportGlossary Approval WorkflowImport-Export TroubleshootingGlossary StylingHow to Add Assets to Glossary TermsBest Practices for GlossaryClassificationDomains & Data ProductMetricsColumn Bulk OperationsOn this pageTroubleshootingGlossary Import/Export Stuck When Using NGINXDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Troubleshooting

​Glossary Import/Export Stuck When Using NGINX

Issue:

When running OpenMetadata behind NGINX with SSL (HTTPS proxy to port 8585), glossary bulk import and export operations may remain stuck in the “Import is in progress” state.

Cause:

The glossary import/export functionality relies on WebSocket communication. If NGINX is not configured to support WebSocket upgrades, the WebSocket handshake will fail, resulting in the UI hanging on the import/export process.

Solution:

Update your NGINX configuration to support WebSocket upgrades by modifying the location / block as follows:

location / {

proxy_pass http://127.0.0.1:8585;

# Enable WebSocket support

proxy_set_header Upgrade $http_upgrade;

proxy_set_header Connection 'upgrade';

proxy_http_version 1.1;

}

Was this page helpful?YesNoSuggest editsRaise issueGlossary Approval Workflow | Official DocumentationPreviousGlossary Styling | OpenMetadata Glossary CustomizationNext⌘I
