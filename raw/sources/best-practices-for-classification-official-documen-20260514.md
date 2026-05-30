---
type: clip
title: "Best Practices for Classification | Official Documentation - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/best-practices"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Best Practices for Classification | Official Documentation - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/best-practices

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationClassificationBest Practices for Classification | Official DocumentationHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData GovernanceOverviewGlossaryClassificationOverviewOverview of ClassificationHow to Classify Data AssetsHow to Request for Classification TagsSample Data Handling Using PII TagsAuto-Classification WorkflowWhat are TiersBest Practices for ClassificationDomains & Data ProductMetricsColumn Bulk OperationsOn this pageBest Practices for Classification1. Add Classification Tags to Glossary Terms2. Make Use of Tier Classification3. Use Classifications to Simplify Policies4. Use Display Name to Improve Names5. Don’t Delete Classification Tags;  Rename them6. Group Similar Concepts TogetherDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Best Practices for Classification

A controlled vocabulary is an organized arrangement of words and phrases to define terminology to organize and retrieve information. Glossary and Classification are both controlled vocabulary.

Here are the Best Practices around Classification:

​1. Add Classification Tags to Glossary Terms

Classification tags can be added to a glossary term. This helps to define both the semantic meaning and type of data in a single step. Instead of adding classification tags manually, a glossary term can be added to define the meaning of the data, and classification tags like PII-sensitive can be added to the term to define the type of data. This helps to auto-assign PII tags.

Organizations have data producers who create tables, and build data models. Team members who understand regulatory compliance requirements are good at classifying data. Among them, those who understand the data as well as the regulatory requirements, can help organizations scale by adding glossary terms along with the classification and tags.

​2. Make Use of Tier Classification

Tiering helps define the importance of data to an organization. By focusing on Tier 1 data, organizations can create the highest impact. Identifying Tier 5 can help declutter the existing data. Learn more about Tiers.

​3. Use Classifications to Simplify Policies

Along with ownership and team membership, tags are a powerful way to group data assets. A single policy can be created at the Resource level instead of managing multiple policies for various resources.

Resources can be grouped using classification tags like sensitive data, restrictive data, external data, raw data, public data, internal data, etc. Further, Policies can be created based on Tags to simplify data governance.

Instead of creating policies for separate tables with sensitive data, the ‘Sensitive’ tag can be attached to various data assets; and a policy can be created to match based on the Sensitive tag, which will take care of all the resources marked accordingly.

​4. Use Display Name to Improve Names

When classification tags are inherited from source systems, the names may not communicate the concept well. For example, dep-prod instead of Product Department. Users are more likely to search using common terms like Product or Department, and this helps in better discovery.

In cases where abbreviations or acronyms are used, a better display name helps in data discovery. For example, c_id can be changed to Customer ID, and CAC can be changed to Customer Acquisition Cost

​5. Don’t Delete Classification Tags;  Rename them

When classification tags have typos, users tend to delete the term. All the effort spent in tagging the data assets is lost when terms are deleted. OpenMetadata supports renaming Classification tags. Simply rename them.

​6. Group Similar Concepts Together

When adding terms, building a semantic relationship helps to understand data through concepts. For example, grouping related terms helps in understanding the various terms and their overall relationship.

Was this page helpful?YesNoSuggest editsRaise issueWhat are Tiers | OpenMetadata Classification Tiers GuidePreviousDomains & Data Products | Official DocumentationNext⌘I
