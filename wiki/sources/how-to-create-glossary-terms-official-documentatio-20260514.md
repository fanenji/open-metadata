---
type: source
title: "Source: how-to-create-glossary-terms-official-documentatio-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["how-to-create-glossary-terms-official-documentatio-20260514.md"]
tags: []
related: []
---

# Source: how-to-create-glossary-terms-official-documentatio-20260514.md

## Key Entities

- **Glossary Term** — Central entity; a business metadata classification object that can be applied to data assets. Already exists in the wiki ([[glossary-terms]]).
- **Glossary** — Container for terms; prerequisite for creating terms. Not yet a dedicated wiki page.
- **Child Term** — Sub-term within a glossary term's hierarchy; enables parent-child relationships for conceptual specificity. Not yet a dedicated wiki page.
- **Owner** — Team or User responsible for a glossary term. Already exists in the wiki ([[data-asset-ownership]]).
- **Reviewers** — Multiple users can be assigned to review glossary terms. Not yet a dedicated wiki page.
- **Tags** — Classification tags that can be associated with glossary terms; propagate to assets when the term is applied. Already exists in the wiki ([[classification-tags]], [[glossary-tags]]).

## Key Concepts

- **Mutually Exclusive** — Configuration flag preventing assignment of multiple child terms from the same glossary term to a single data asset. Not yet in the wiki.
- **Synonyms** — Alternative terms for the same concept (e.g., Customer = Client, Shopper). Not yet in the wiki.
- **Related Terms** — Network of associative relationships between glossary terms (e.g., Customer → Customer LTV). Not yet in the wiki.
- **Conceptual Hierarchy** — Parent-child relationship structure allowing terms to go from generic to specific (e.g., Customer → Loyal Customer). Not yet in the wiki.
- **Tag Propagation** — When a glossary term with associated tags is applied to an asset, the tags are automatically applied as well. Already partially covered in [[glossary-terms]].

## Main Arguments & Findings

- **Core claim:** Glossary terms are created via a simple UI form with required fields (Name, Description) and optional fields (Display Name, Tags, Synonyms, Related Terms, Mutually Exclusive, References, Owner, Reviewers).
- **Evidence:** Step-by-step procedural documentation from the official OpenMetadata v1.12.x guide.
- **Strength:** High — this is official documentation, not opinion or analysis.

## Connections to Existing Wiki

- **Strengthens:** [[glossary-terms]] — provides detailed creation procedure and field definitions.
- **Extends:** [[classification-tags]] — clarifies the relationship between glossary terms and tags (tags are associated with terms, not the other way around).
- **Extends:** [[data-asset-ownership]] — confirms that glossary terms can have Owners (Team or User).
- **Related to:** [[how-to-add-glossary-terms]] — this source covers term *creation*, while the existing page covers term *application* to assets.

## Contradictions & Tensions

- **No contradictions** with existing wiki content.
- **Minor tension:** The existing [[glossary-terms]] page mentions "tag propagation where associated tags are automatically applied" but does not detail the Mutually Exclusive feature or the Synonyms/Related Terms fields. This source fills those gaps.

## Recommendations

### Pages to Create
- **
