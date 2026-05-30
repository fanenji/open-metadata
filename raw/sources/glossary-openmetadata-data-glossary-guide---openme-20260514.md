---
type: clip
title: "Glossary | OpenMetadata Data Glossary Guide - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/glossary"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Glossary | OpenMetadata Data Glossary Guide - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/glossary

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationGlossaryGlossary | OpenMetadata Data Glossary GuideHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData GovernanceOverviewGlossaryOverviewWhat is a Glossary TermHow to Setup a GlossaryHow to Create Glossary TermsHow to Bulk Import a GlossaryGlossary ExportGlossary Approval WorkflowImport-Export TroubleshootingGlossary StylingHow to Add Assets to Glossary TermsBest Practices for GlossaryClassificationDomains & Data ProductMetricsColumn Bulk OperationsOn this pageGlossaryGlossary in OpenMetadataGlossary APIsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Glossary

A Glossary is a Controlled Vocabulary to describe important concepts and terminologies within your organization to foster a common and consistent understanding of data. A controlled vocabulary is an organized arrangement of words and phrases to define terminology to organize and retrieve information.

Glossary adds semantics or meaning to data by defining the business terminologies. It defines concepts related to a specific domain. For example, Business Glossary or Bank Glossary. A well-defined business glossary helps foster team collaboration with the use of standard terms. The terms from the glossary can be used for labeling or tagging as additional metadata of data assets for describing and categorizing things. Glossaries are important for data discovery, retrieval, and exploration through conceptual terms, and facilitates Data Governance.

​Glossary in OpenMetadata

OpenMetadata models a Glossary as a Thesauri that organizes terms with hierarchical, equivalent, and associative relationships within a domain. The Glossary in OpenMetadata can be accessed from Govern >>  Glossary. All the Glossaries are displayed in the left nav bar. Clicking on a specific glossary will display the expanded view to show the entire hierarchy of the glossary terms (parent-child terms).

Tip: A well-defined and centralized glossary makes it easy to onboard new team members and help them get familiar with the organizational terminology.

Watch the Webinar on Glossaries and Classifications in OpenMetadata

​Glossary APIs

OpenMetadata has extensive Glossary APIs. The main entities are Glossary and Glossary Term. These entities are identified by a Unique ID. Glossary terms have a fully qualified name in the form of glossary.parentTerm.childTerm

You can create, delete, modify, and update using APIs. Refer to the Glossary API documentation.

Glossary TermLearn about the hierarchically arranged glossary terms.Setup a GlossaryLearn how to set up a glossary manually in OpenMetadata.Create Glossary TermsSetup glossary terms to define the terminology. Add tags, synonyms, related terms, links, etc.Bulk Import a GlossarySave time and effort by bulk uploading glossary terms using a CSV file.Glossary ExportQuickly export a glossary as a CSV file.Glossary Approval WorkflowSet up a review and approval process for glossary terms.Glossary StylingStylize your glossary terms with color-coding and icons.Add Assets to Glossary TermsAssociate glossary terms to data assets making it easier for data discoveryBest Practices for GlossaryHere are the Top 8 Best Practices around Terminologies.Was this page helpful?YesNoSuggest editsRaise issueData Governance | OpenMetadata Governance GuidePreviousWhat is a Glossary Term | Official DocumentationNext⌘I
