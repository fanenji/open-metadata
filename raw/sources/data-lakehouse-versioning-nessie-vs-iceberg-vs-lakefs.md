---
source_url: "https://www.dremio.com/blog/data-lakehouse-versioning-comparison-nessie-apache-iceberg-lakefs/"
fetched: "2026-04-22"
title: "Data Lakehouse Versioning: Nessie vs Iceberg vs LakeFS"
author: "- "Alex Merced""
published: "2024-03-05"
clipped_from: obsidian-web-clipper
---
[DataOps, a collaborative data management practice](https://www.dremio.com/blog/what-is-dataops-automating-data-management-on-the-apache-iceberg-lakehouse/) focused on improving the communication, integration, and automation of data flows between data managers and data consumers across an organization, has emerged as a focal point for data-driven cultures.

At the core of effective DataOps is versioning — creating, managing, and tracking different versions of data sets. Versioning is fundamental for several reasons. First, it allows for isolating changes, enabling teams to work on datasets in parallel without interference. Second, it supports the creation of zero-copy environments where users can experiment and analyze without affecting the original data. Furthermore, versioning facilitates tagging for reproducibility, ensuring that analyses can be traced back to the exact data version used, which is critical for audits and regulatory compliance. Lastly, it enables multi-table transactions, allowing for complex changes across multiple datasets to be treated as a single atomic operation.

These capabilities are not just beneficial; they are essential in today's fast-paced data environments, where data integrity, reliability, and reproducibility are paramount.

## The Essence of Versioning in Data Lakehouses

[Data lakehouses, which combine the best features](https://www.dremio.com/blog/why-lakehouse-why-now-what-is-a-data-lakehouse-and-how-to-get-started/) of data lakes and data warehouses, have become increasingly popular for managing big data. They offer the scalability and flexibility of data lakes with the governance and performance optimizations of data warehouses. In this context, versioning is pivotal in addressing some of the most pressing data management challenges.

Versioning in data lakehouses allows for better data governance by tracking changes and maintaining a history of data transformations. This historical insight is invaluable for debugging and understanding data lineage. It also supports dynamic data environments, where changes are frequent and data schemas evolve. By enabling safe, isolated changes, versioning ensures that the data lakehouse remains a reliable source of truth for the organization.

Moreover, versioning opens up new possibilities for data experimentation and innovation. Data scientists and analysts can branch out datasets to test hypotheses or build models without risking the integrity of production data. This freedom to experiment, coupled with the ability to quickly revert changes or merge successful experiments into the main data repository, accelerates innovation.

As we delve into the various versioning solutions available in the data lakehouse ecosystem, it's clear that the choice of versioning strategy—be it file versioning with LakeFS, table versioning with Apache Iceberg, or catalog versioning with Nessie—can significantly impact the efficiency, flexibility, and robustness of data operations.

## Try Dremio’s Interactive Demo

Explore this interactive demo and see how Dremio's Intelligent Lakehouse enables Agentic AI

## Catalog Versioning with Nessie

[Nessie](https://www.dremio.com/blog/what-is-nessie-catalog-versioning-and-git-for-data/) revolutionizes [data lake management](https://www.dremio.com/blog/what-is-lakehouse-management-git-for-data-automated-apache-iceberg-table-maintenance-and-more/) by introducing a version control model akin to Git for source code repositories. Its design focuses on providing a consistently updated view of data across all datasets within a data lake, ensuring that any changes, such as those from batch jobs, are isolated until they're complete. This approach ensures users only see their data's final, consistent state, akin to committing changes in a version control system.

### How Nessie Works

Nessie's architecture is designed to significantly simplify data lake management. It records changes to the data lake as commits at the catalog level, but without duplicating the actual data. A Nessie commit tracks versions of metadata attached to a namespace representing objects in your lakehouse, like tables, namespaces, and views. This strategy allows for adding meaning to changes, ensuring an always-consistent view of data, and isolating sets of changes for experiments or distributed jobs through branches. With Nessie, it's possible to have known, fixed versions of data, enabling easy tagging for reference and automatic removal of unused data files, simplifying garbage collection.

### Key Features of Nessie

**Commits and Branches:** Changes in the data lake are recorded as commits, allowing users to manage data changes precisely. Branches offer isolated environments for changes, ensuring that failed experiments or jobs do not impact the main data set.

**Tags:** Known versions of data can be tagged, similar to Git, allowing easy reference to specific data states for reporting or analysis.

**Automatic Data Management:** Nessie automates the tedious process of tracking which data files are in use and which can be safely deleted, significantly simplifying data lake management.

### Use Cases for Nessie

Nessie's approach to data lake versioning supports various data engineering and data science workflows:

**Isolated Experimentation:** Data scientists and engineers can use branches to experiment with data changes without risking the integrity of production datasets.

**Auditing and Compliance:** By tagging specific commits, organizations can maintain easily accessible historical records of their data for compliance and auditing purposes.

**Simplified Data Ops:** Nessie simplifies the operations associated with managing large data lakes, including schema changes, data file management, and cleanup.

### Pros and Cons of Using Nessie

#### Pros

- **Consistent Data View:** Nessie ensures that all users have a consistent view of data, even across complex, multi-table transactions and changes.
- **Simplified Data Management:** By handling the tracking of data files and automating garbage collection, [Nessie's GC cleaner](https://projectnessie.org/features/gc/) reduces the manual overhead of managing a data lake.
- **Supports Multiple Environments:** With Nessie, production, staging, and development environments can share the same data lake without risking data consistency, supporting CI/CD for data.
- **Immutable Data Files:** Nessie's model works well with the immutable nature of data files in a data lake, referencing existing data without necessitating copies.

#### Cons

- **Learning Curve:** Users unfamiliar with version control concepts may face a learning curve in adopting Nessie, though its benefits to data management are substantial. Fortunately, Nessie, in practice, works via SQL, making it one of the most accessible versioning solutions for the least technical users.
- **Integration Effort:** Integrating Nessie with existing data lakes and workflows may require initial setup and configuration efforts. This is made a lot easier when using Dremio as your [Data Lakehouse Platform](https://www.dremio.com/blog/what-is-a-data-lakehouse-platform/) as [Dremio's integrated catalog is powered by Nessie](https://www.dremio.com/blog/managing-data-as-code-with-dremio-arctic-easily-ensure-data-quality-in-your-data-lakehouse/) and managed by Dremio.

Nessie offers a powerful model for managing data lakes with version control principles. It provides data teams with tools to manage changes, ensure consistency, and support complex data operations with ease. Its approach to versioning and the ability to isolate experiments and manage data files efficiently make it an invaluable tool for modern data lakes.

### Example of Using Nessie with Dremio

```
xxxxxxxxxx
```

```
-- Creating a new branch for data integration
```
```
CREATE BRANCH dataIntegration_010224;
```
```
​
```
```
-- Switching to the dataIntegration branch
```
```
USE BRANCH dataIntegration_010224;
```
```
​
```
```
-- Merging staging data into the SalesData table on the dataIntegration branch
```
```
MERGE INTO DACSalesData AS target
```
```
USING DACStagingSalesData AS source
```
```
ON target.id = source.id
```
```
WHEN MATCHED THEN
```
```
UPDATE SET productId = source.productId, saleAmount = source.saleAmount, saleDate = source.saleDate
```
```
WHEN NOT MATCHED THEN
```
```
INSERT (id, productId, saleAmount, saleDate) VALUES (source.id, source.productId, source.saleAmount, source.saleDate);
```
```
​
```
```
-- Performing data quality checks on the dataIntegration branch
```
```
-- Check for non-negative sale amounts
```
```
SELECT COUNT(*) AS InvalidAmountCount
```
```
FROM DACSalesData
```
```
WHERE saleAmount < 0;
```
```
​
```
```
-- Check for valid sale dates (not in the future)
```
```
SELECT COUNT(*) AS InvalidDateCount
```
```
FROM DACSalesData
```
```
WHERE saleDate > CURRENT_DATE;
```
```
​
```
```
-- QUERY MAIN BRANCH
```
```
SELECT * FROM DACSalesData AT BRANCH main;
```
```
​
```
```
-- QUERY INGESTION BRANCH
```
```
SELECT * FROM DACSalesData AT BRANCH dataIntegration_010224;
```
```
​
```
```
-- Assuming checks have passed, switch back to the main branch and merge changes from dataIntegration
```
```
-- This step should be executed after confirming that the checks have passed
```
```
USE BRANCH main;
```
```
MERGE BRANCH dataIntegration_010224 INTO main;
```
```
​
```
```
-- QUERY MAIN BRANCH
```
```
SELECT * FROM DACSalesData AT BRANCH main;
```
```
​
```
```
-- QUERY INGESTION BRANCH
```
```
SELECT * FROM DACSalesData AT BRANCH dataIntegration_010224;
```

## Table Versioning with Apache Iceberg

Apache Iceberg introduces an innovative approach to versioning in data lakes by utilizing table metadata to maintain a snapshot log. This log is crucial for enabling powerful features like reader isolation and time travel queries, making Iceberg a standout choice for managing data at scale.

### Understanding Branching and Tagging in Iceberg

Iceberg's snapshot log represents the historical changes applied to a table, where each snapshot captures a particular state.

### Branches and Tags

Iceberg supports branches and tags for more nuanced snapshot management, with named references to snapshots that follow their own independent lifecycle. Branch and tag-level retention policies control this, enabling distinct lineages of snapshots (branches) or marking significant snapshots for retention (tags).

Branches are akin to branches in version control systems, providing independent lines of snapshot history. Each branch points to the "head" snapshot of its lineage, allowing for parallel development and experimentation.

Tags are used to mark specific snapshots for special purposes, such as compliance or historical reference, without the overhead of maintaining a separate branch.

Retention properties govern these mechanisms that specify how long to keep branches, tags, and their referenced snapshots.

### Use Cases for Iceberg's Versioning

The flexibility of branching and tagging in Iceberg facilitates various data management strategies, including compliance with GDPR requirements, historical data retention for auditing, and supporting experimental workflows.

#### Historical Tags

Tags enable the retention of critical snapshots for auditing purposes, following specific retention policies:

Weekly snapshots for a month, monthly snapshots for six months, and annual snapshots indefinitely. These snapshots can be tagged and retained according to a defined policy, ensuring that important states of the table are preserved for future reference or compliance needs.

#### Temporary Testing Branches

Experimental branches, such as a "test-branch," can be created for short-term testing, with policies to retain the branch and its snapshots for a limited period. This allows for safe testing of changes without impacting the main dataset.

#### Audit Branches

An audit branch can be used to validate write workflows independently from the main table history. By directing write operations to an audit branch and performing validations, it's possible to ensure data quality before integrating changes into the main dataset. This branch can then be fast-forwarded to update the main table state, seamlessly integrating validated changes.

### Pros

- **Catalog Agnostic:** Works seamlessly across all Iceberg catalogs, offering a universal solution for Iceberg tables.
- **No Additional Service Required:** Unlike systems that require running a separate service for versioning, Iceberg's built-in capabilities simplify infrastructure requirements.
- **Cloud and Storage Agnostic:** Iceberg's versioning is independent of the underlying storage or cloud provider, offering flexibility in deployment environments.
- **Support for Complex Transactions:** With properties like write.wap.enabled, Iceberg supports complex, multi-table transactions within the constraints of its versioning system.

### Cons

- **Single Table Focus:** Branching and tagging mechanisms are limited to individual tables, which may complicate scenarios requiring coordinated versioning across multiple tables.
- **Specific to Iceberg:** The versioning features are exclusive to Iceberg, limiting their applicability to datasets not managed by this format.

Apache Iceberg's approach to table versioning, particularly its branching and tagging capabilities, provides a robust framework for managing the data lifecycle in a lakehouse architecture. By enabling sophisticated version control directly within table metadata, Iceberg facilitates a wide range of data engineering and governance practices, enhancing the flexibility and reliability of data management strategies.

### Example of Using Native Iceberg Table Branching in SparkSQL

```
xxxxxxxxxx
```

```
-- Step 1: Create Tags for Snapshot Retention
```
```
-- Tag for end of week snapshot, retained for 7 days
```
```
ALTER TABLE prod.db.table CREATE TAG \`EOW-01\` AS OF VERSION 7 RETAIN 7 DAYS;
```
```
​
```
```
-- Tag for end of month snapshot, retained for 6 months
```
```
ALTER TABLE prod.db.table CREATE TAG \`EOM-01\` AS OF VERSION 30 RETAIN 180 DAYS;
```
```
​
```
```
-- Tag for end of year snapshot, retained forever
```
```
ALTER TABLE prod.db.table CREATE TAG \`EOY-2023\` AS OF VERSION 365;
```
```
​
```
```
-- Step 2: Creating a Temporary Test Branch
```
```
-- This branch is for testing or development, with a 7 day retention and the latest 2 snapshots kept
```
```
ALTER TABLE prod.db.table CREATE BRANCH \`test-branch\` RETAIN 7 DAYS WITH SNAPSHOT RETENTION 2 SNAPSHOTS;
```
```
​
```
```
-- Step 3: Setting up an Audit Branch for Write Workflow Validation
```
```
-- Enable write-audit-publish (WAP) feature for the table
```
```
ALTER TABLE prod.db.table SET TBLPROPERTIES ('write.wap.enabled'='true');
```
```
​
```
```
-- Create an audit branch starting from snapshot 3, retained for 1 week
```
```
ALTER TABLE prod.db.table CREATE BRANCH \`audit-branch\` AS OF VERSION 3 RETAIN 7 DAYS;
```
```
​
```
```
-- Perform write operations on the audit branch
```
```
-- Assuming setting the branch to write to is done outside SQL, e.g., via Spark session configuration
```
```
-- Here, INSERT is just illustrative; actual SQL might vary based on the data schema
```
```
SET spark.wap.branch = 'audit-branch';
```
```
INSERT INTO prod.db.table VALUES (3, 'c');
```
```
​
```
```
-- After validation, fast forward the main branch to the head of the audit branch to update the main table state
```
```
CALL catalog_name.system.fast_forward('prod.db.table', 'main', 'audit-branch');
```
```
​
```
```
-- Note: The branch reference \`audit-branch\` will be removed when \`expireSnapshots\` is run 1 week later as per its retention policy
```

## File Versioning with LakeFS

[LakeFS offers a versioning system for data lakes](https://docs.lakefs.io/integrations/dremio.html) by implementing a git-like interface for file-level versioning. Let's delve into how LakeFS achieves this, focusing on its architecture and components.

The architecture of LakeFS is built around several key components:

**Object Storage:** LakeFS leverages object storage as its primary data storage solution. It supports many object stores, including AWS S3, Google Cloud Storage, Azure Blob Storage, MinIO, and Ceph.

**Metadata Storage:** In addition to object storage, LakeFS uses key-value storage to manage metadata. Supported databases for metadata storage include PostgreSQL, DynamoDB, and CosmosDB, providing a robust foundation for tracking changes, managing versions, and supporting complex operations like branching and merging.

### Pros

- **Comprehensive Versioning System:** LakeFS provides a system for managing file-level versions in data lakes by encapsulating versioning logic and operations within a distributed architecture.
- **Cloud and Storage Agnostic:** The support for multiple object and metadata storage systems ensures that LakeFS can operate across different cloud environments and integrate with existing data storage solutions.
- **Multi-Session, Multi-File Transactions:** Supports complex data operations across multiple files and sessions, enabling effective data management practices like branching, committing, and merging changes.

### Cons

- **Requires S3-Compatible Storage Layer:** While LakeFS's compatibility with a range of object storage solutions is a significant advantage, it necessitates an S3-compatible layer, which might limit options for organizations with specialized storage needs.
- **Disconnected from Table Concepts:** As LakeFS operates at the file level, it's somewhat removed from higher-level abstractions like tables. This means it might not directly support tasks like table optimization and cleanup, which are handled by other systems integrated with LakeFS, such as Dremio with Nessie for Apache Iceberg tables.
- **Less Accessible for Non-Technical Users:** Without a SQL interface and the primarily a CLI interface, LakeFS can be trickier for non-technical users to benefit from.

### Example of Using LakeFS with Python

```
xxxxxxxxxx
```

```
# Create a new branch from the main branch for the dataset modifications
```
```
repo_name = "quickstart"
```
```
source_branch = "main"
```
```
new_branch_name = "denmark-lakes"
```
```
​
```
```
# Using the lakeFS repository object to manage branches
```
```
repo = lakefs.Repository(repo_name, client=client)
```
```
new_branch = repo.branch(new_branch_name).create(source_reference_id=source_branch)
```
```
print(f"Created new branch: {new_branch_name}")
```
```
​
```
```
# Assuming you have already manipulated the data
```
```
# Here we just simulate the process of uploading the modified data back to lakeFS
```
```
​
```
```
# Write the modified data back to the new branch
```
```
# Note: Replace this part with your actual data manipulation and export process
```
```
data_path = "lakes.parquet"
```
```
modified_data_content = b"modified data representing lakes in Denmark"
```
```
new_branch.object(path=data_path).upload(data=modified_data_content, pre_sign=True)
```
```
print(f"Data written to {data_path} in branch {new_branch_name}")
```
```
​
```
```
# Commit the changes to the new branch
```
```
commit_message = "Create a dataset of just the lakes in Denmark"
```
```
commit_ref = new_branch.commit(message=commit_message)
```
```
print(f"Committed changes: {commit_ref.get_commit().id}")
```
```
​
```
```
# Merge the new branch back into the main branch
```
```
main_branch = repo.branch(source_branch)
```
```
merge_result = new_branch.merge_into(main_branch)
```
```
print(f"Merged branch {new_branch_name} into {source_branch}: {merge_result}")
```
```
​
```
```
# Verify merged data - This is more of a conceptual step, as verification would
```
```
# depend on how you access and verify data in your lakeFS setup.
```
```
# You could re-import the data into DuckDB or use another tool to ensure the merge was successful.
```

## Conclusion

In the era of big data, where the volume, velocity, and variety of data continue to challenge traditional data management practices, adopting a versioning system that aligns with your data strategy is more than a convenience—it's a necessity. By leveraging the strengths of LakeFS, Apache Iceberg, and Nessie, organizations can balance operational efficiency, data governance, and innovation, ensuring that their data lakehouse remains a robust foundation for data-driven decision-making.

[Build a Nessie/Iceberg/Dremio Lakehouse on Your Laptop with this Tutorial](https://www.dremio.com/blog/intro-to-dremio-nessie-and-apache-iceberg-on-your-laptop/)