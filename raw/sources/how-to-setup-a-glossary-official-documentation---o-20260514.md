---
type: clip
title: "How to Setup a Glossary | Official Documentation - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/glossary/setup"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# How to Setup a Glossary | Official Documentation - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/glossary/setup

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationGlossaryHow to Setup a Glossary | Official DocumentationHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData GovernanceOverviewGlossaryOverviewWhat is a Glossary TermHow to Setup a GlossaryHow to Create Glossary TermsHow to Bulk Import a GlossaryGlossary ExportGlossary Approval WorkflowImport-Export TroubleshootingGlossary StylingHow to Add Assets to Glossary TermsBest Practices for GlossaryClassificationDomains & Data ProductMetricsColumn Bulk OperationsOn this pageHow to Setup a GlossaryAdd a Owner and Reviewers to a GlossaryDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​How to Setup a Glossary

To create a glossary manually in OpenMetadata:

Navigate to Govern > Glossary

Click on + Add to add a new glossary

Enter the details to configure the glossary.

Name* - This is a required field.

Display Name

Description* - Describe the context or domain of the glossary. This is a required field.

Tags - Classification tags can be added to a glossary.

Mutually Exclusive - There are cases where only one term from a particular glossary is relevant for a data asset. For example, an asset can either be ‘PII-Sensitive’ or a ‘PII-NonSensitive’. It cannot be both. For such cases, a Glossary can be created where the glossary terms can be mutually exclusive. If this configuration is enabled, you won’t be able to assign multiple terms from the same Glossary to the same data asset.

Owner - Either a Team or a  User can be the Owner of a Glossary.

Reviewers  - Multiple reviewers can be added.

​Add a Owner and Reviewers to a Glossary

When creating a glossary, you can add the glossary owner. Either a Team or a User can be a Owner of the Glossary. Simply click on the option for Owner to select the user or team.

Multiple users can be added as Reviewers by clicking on the pencil icon. If the Reviewer details exist for a glossary, then the same details are reflected when adding a new term manually as well.

If the Owner and Reviewer details are added while creating the glossary, and the glossary terms are bulk uploaded using a CSV file, then the glossary Owner and Reviewers are inherited for all the glossary terms. These details can be changed later.

How to Create Glossary TermsSetup Glossary Terms to define the terminology. Add tags, synonyms, related terms, links, etc.

How to Bulk Import a GlossarySave time and effort by bulk uploading glossary terms using a CSV file.

How to Add Assets to Glossary TermsAssociate glossary terms to data assets making it easier for data discoveryWas this page helpful?YesNoSuggest editsRaise issueWhat is a Glossary Term | Official DocumentationPreviousHow to Create Glossary Terms | Official DocumentationNext⌘I
