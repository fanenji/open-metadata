---
type: clip
title: "How to Bulk Import a Glossary - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/glossary/import"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# How to Bulk Import a Glossary - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/glossary/import

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationGlossaryHow to Bulk Import a GlossaryHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData GovernanceOverviewGlossaryOverviewWhat is a Glossary TermHow to Setup a GlossaryHow to Create Glossary TermsHow to Bulk Import a GlossaryGlossary ExportGlossary Approval WorkflowImport-Export TroubleshootingGlossary StylingHow to Add Assets to Glossary TermsBest Practices for GlossaryClassificationDomains & Data ProductMetricsColumn Bulk OperationsOn this pageHow to Bulk Import a GlossaryMutually ExclusiveAdd Owners and Reviewers to a GlossaryDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​How to Bulk Import a Glossary

OpenMetadata supports Glossary Bulk Upload to save time and effort by uploading a CSV with thousands of terms in one go. You can create or update multiple glossary terms simultaneously. When bulk uploading, Owners and Reviewers can be defined, who will be further propagated to every glossary term.

To import a glossary into OpenMetadata:

Navigate to Govern > Glossary

Click on Add a new glossary. Eg. Banking Glossary

You can also bulk upload terms to an existing glossary.

Add the Name*, Display Name, Description*, Tags, Owner, and Reviewer details for the glossary. The * marked fields are required fields.

Click on the ⋮ icon and Export the glossary file. If you have glossary terms in your Glossary, the same will be exported as a CSV file. If you have If there are no terms in the Glossary, then a blank CSV template will be downloaded.

Once you have the template, you can fill in the following details:

parent - The parent column helps to define the hierarchy of the glossary terms. If you leave this field blank, the Term will be created at the root level. If you want to create a hierarchy of Glossary Terms, the parent details must be entered as per the hierarchy. For example, from the Glossary level, Banking.Account.Savings Account

name* - This contains the name of the glossary term, and is a required field.

displayName - This contains the Display name of the glossary term.

description* - This contains the description or details of the glossary term and is a required field.

synonyms - Include words that have the same meaning as the glossary term. For e.g., for a term ‘Customer’, the synonyms can be ‘Client’, ‘Shopper’, ‘Purchaser’. In the CSV file, the synonyms must be separated by a semicolon (;) as in Client;Shopper;Purchaser

relatedTerms - A term which has a related concept as the glossary term. This term must be available in OpenMetadata. For e.g., for a term ‘Customer’, the related terms can be ‘Customer LTV (LifeTime Value)’, ‘Customer Acquisition Cost (CAC)’. In the CSV file, the relatedTerms must contain the hierarchy, which is separated by a full stop (.). Multiple terms must be separated by a semicolon (;) as in Banking.Account.Savings account;Banking.Debit card

references - Add links from the internet from where you inherited the term. In the CSV file, the references must be in the format (name;url;name;url) IBM;https://www.ibm.com/;World Bank;https://www.worldbank.org/

tags - Add the tags which are already existing in OpenMetadata. In the CSV file, the tags must be in the format PII.Sensitive;PersonalData.Personal

​Mutually Exclusive

You can also mark the Glossary as Mutually Exclusive if you want only one of the terms from the glossary to be applicable to the data assets. There are cases where only one glossary term from a Glossary is relevant for a data asset. For example, an asset can either be PII Sensitive or PII Non-Sensitive. It cannot be both. For such cases, a Glossary can be created where the terms can be mutually exclusive. If this configuration is enabled, you won’t be able to assign multiple tags from the same Glossary to the same data asset.

​Add Owners and Reviewers to a Glossary

If the Owner details are added while creating the glossary, the same will be inherited for the glossary terms. Either a Team or a User can be the Owner of a Glossary. Multiple users can be Reviewers. These can be changed later. The glossary Owner and Reviewers are inherited for all the glossary terms.

Once the CSV file is ready, click on the ⋮ icon and select the Import button.

Drag and drop the CSV file, or upload it by clicking on the Browse button.

The import utility will validate the file and a Preview of the elements that will be imported to OpenMetadata is displayed.

After previewing the uploaded terms, click on Import.

The glossary terms will be scanned and imported. After which a Success or Failure message will be displayed.

Once a part of the terms or all terms are created successfully, the Import button will be displayed. Click on Import to create the glossary terms from the CSV file in OpenMetadata.

Next you can View the imported glossary. You can Expand All the terms to view the nested terms. Glossary terms can be dragged and dropped as required to rearrange the glossary.

The glossary Owner is inherited for all the glossary terms.

Both importing and exporting the Glossary from OpenMetadata is quick and easy!

Glossary ExportQuickly export a glossary as a CSV file.

Glossary Approval WorkflowSet up a review and approval process for glossary termsWas this page helpful?YesNoSuggest editsRaise issueHow to Create Glossary Terms | Official DocumentationPreviousGlossary Export | OpenMetadata Export GuideNext⌘I
