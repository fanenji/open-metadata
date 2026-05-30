---
type: clip
title: "How to Create Glossary Terms | Official Documentation - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/glossary/create-terms"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# How to Create Glossary Terms | Official Documentation - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/glossary/create-terms

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationGlossaryHow to Create Glossary Terms | Official DocumentationHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData GovernanceOverviewGlossaryOverviewWhat is a Glossary TermHow to Setup a GlossaryHow to Create Glossary TermsHow to Bulk Import a GlossaryGlossary ExportGlossary Approval WorkflowImport-Export TroubleshootingGlossary StylingHow to Add Assets to Glossary TermsBest Practices for GlossaryClassificationDomains & Data ProductMetricsColumn Bulk OperationsOn this pageHow to Create Glossary TermsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​How to Create Glossary Terms

Once a glossary has been created, you can add multiple Glossary Terms and Child Terms in it.

Once in the Glossary, click on Add Term.

Enter the required information:

Name* - This contains the name of the glossary term, and is a required field.

Display Name - This contains the Display name of the glossary term.

Description* - A unique and clear definition to establish consistent usage and understanding of the term. This is a required field.

Tags - Classification tags can be added to glossary terms. When adding a glossary term to assets, it will also add the associated tags to that asset. This helps to further describe and categorize the data assets.

Synonyms - Other terms that are used for the same concept. For e.g., for a term ‘Customer’, the synonyms can be ‘Client’, ‘Shopper’, ‘Purchaser’.

Related Terms - These terms can build a network of concepts to capture an associative relationship. For e.g., for a term ‘Customer’, the related terms can be ‘Customer LTV (LifeTime Value)’, ‘Customer Acquisition Cost (CAC)’.

Mutually Exclusive - There are cases where only one term from a particular glossary is relevant for a data asset. For example, an asset can either be ‘PII-Sensitive’ or a ‘PII-NonSensitive’. It cannot be both. For such cases, a Glossary Term can be created where the child terms can be mutually exclusive. If this configuration is enabled, you won’t be able to assign multiple terms from the same Glossary Term to the same data asset.

References - Add links from the internet from where you inherited the term.

Owner - Either a Team or a User can be the Owner of a Glossary term.

Reviewers  - Multiple reviewers can be added.

Once a glossary term has been added, you can create Child Terms under it. The child terms help to build a conceptual hierarchy (Parent-Child relationship) to go from generic to specific concepts. For e.g., for a term ‘Customer’, the child terms can be ‘Loyal Customer’, ‘New Customer’, ‘Online Customer’.

Instead of creating a glossary manually, you can bulk upload glossary terms using a CSV file.

How to Bulk Import a GlossarySave time and effort by bulk uploading glossary terms using a CSV file.

How to Add Assets to Glossary TermsAssociate glossary terms to data assets making it easier for data discoveryWas this page helpful?YesNoSuggest editsRaise issueHow to Setup a Glossary | Official DocumentationPreviousHow to Bulk Import a GlossaryNext⌘I
