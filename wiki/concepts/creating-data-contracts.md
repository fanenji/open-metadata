---
type: concept
title: Creating Data Contracts
created: 2026-05-14
updated: 2026-05-14
tags: [data-contracts, how-to-guide, workflow]
related: [data-contracts, data-quality, data-asset-ownership, classification-tags, tiers, glossary-terms, snowflake]
sources: ["creating-data-contracts-openmetadata-data-contract-20260514.md"]
---

# Creating Data Contracts

This page documents the 6-step UI workflow for creating a [[data-contracts|Data Contract]] for a table in OpenMetadata v1.12.x. The workflow is a structured wizard that guides users through defining contract details, schema, semantics, and quality tests.

## Prerequisites

- A table must be ingested into OpenMetadata.
- The user must have appropriate permissions to create contracts on the table.

## Step-by-Step Workflow

### Step 1: Navigate to Contract Tab
Go to the Table's page, select the **Contract** tab, then click **+ Add Contract**.

### Step 2: Contract Details
Provide a name for the data contract. Optionally, assign Owners and provide a description. Click **Schema** to proceed.

### Step 3: Schema
Select the columns to include in the contract. Use the checkbox at the top right to select all columns. Click **Semantics** to proceed.

### Step 4: Semantics
Define business rules for the contract. For OpenMetadata Tables, rules can be created for:
- Service
- Owners
- Display Name
- Name
- Description
- Tags
- Domain
- Data Product
- Tier

Use **+ Add New Rule** to create multiple rules. Click **Quality** to proceed.

### Step 5: Quality
Click **+ Add Test** to attach Data Quality Tests to the contract. Click **Save** to finalize.

### Step 6: Run
Once created, execute the contract on demand by clicking **> Run now**.

## Example

The official documentation uses a Snowflake table (`DEMO_STAGE.JAFFLE_SHOP.CUSTOMERS`) as a concrete example.

## Related Pages

- [[data-contracts]] — Core concept page.
- [[data-quality]] — Quality tests are a core component.
- [[data-asset-ownership]] — Owners defined in Semantics.
- [[classification-tags]] — Tags defined in Semantics.
- [[tiers]] — Tier defined in Semantics.
- [[glossary-terms]] — Related via Tags and Domain.