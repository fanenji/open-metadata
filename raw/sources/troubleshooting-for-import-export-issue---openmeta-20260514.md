---
type: clip
title: "Troubleshooting for Import-Export issue - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-discovery/troubleshooting"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Troubleshooting for Import-Export issue - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-discovery/troubleshooting

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationData DiscoveryTroubleshooting for Import-Export issueHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData DiscoveryOverviewHow to Discover Assets of InterestSteps for Searching Using HierarchyGet a Quick Glance of the Data AssetsDetailed View of the Data AssetsAdd Complex Queries using Advanced SearchBulk Upload Data AssetsHow to Bulk Import Data AssetHow to Export Data AssetImport-Export TroubleshootingTable ConstraintOn this pageTroubleshooting Export IssueTroubleshooting StepsStep 1: Check for Load Balancer or ProxyStep 2: Verify WebSocket ConnectivityStep 3: Adjust WebSocket Settings in Your ProxyStep 4: Restart Services and VerifyDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Troubleshooting Export Issue

When attempting to export a CSV file for a Glossary, the process gets stuck on the message “Export initiated successfully.” and never completes. The file is not downloaded, and the export button remains disabled.

This issue may occur if WebSockets are blocked in your network setup due to a proxy or load balancer configuration. OpenMetadata relies on WebSockets for real-time communication, and if they are blocked, the export process cannot complete.

​Troubleshooting Steps

​Step 1: Check for Load Balancer or Proxy

If your setup includes a load balancer or proxy, verify whether WebSockets are being blocked.

Run the following API request to check the export status:

curl -X GET "https://<your-openmetadata-instance>/api/v1/glossaries/name/<Glossary_Name>/exportAsync"

If the response does not return a file and remains in an active state indefinitely, WebSockets might be blocked.

​Step 2: Verify WebSocket Connectivity

Open the Developer Tools in your browser (F12 or Ctrl + Shift + I in Chrome).

Navigate to the Network tab.

Filter requests by WebSockets (WS).

Check if WebSocket requests to OpenMetadata (wss://<your-openmetadata-instance>) are blocked, failing, or not established.

​Step 3: Adjust WebSocket Settings in Your Proxy

If WebSockets are blocked, update your proxy configuration to allow WebSocket traffic.

​Step 4: Restart Services and Verify

Restart your proxy or load balancer after making the configuration changes.

Clear browser cache and cookies.

Retry the CSV export in OpenMetadata.

Once WebSockets are enabled in the proxy settings, the glossary export should complete successfully, and the CSV file should be available for download.Was this page helpful?YesNoSuggest editsRaise issueBulk Export Data Assets via CSV in OpenMetadataPreviousManaging and Editing Table Constraint in OpenMetadataNext⌘I
