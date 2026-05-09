---
source_url: "https://www.google.com/search?q=nessie+branch+best+practice&sourceid=chrome&ie=UTF-8&udm=50&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIemkjk18Cn72Gp24fGkjjh6wQFVCbKXb4P6swJy4x5wjmp_jXuQmh9XuontG_OYbw3ut6HXMfY8rgP3YiBp673QTTvw4jXocMzgd0hzcq6Zf_P--HWm4eH-23XmXDAUy56hBeVnuYa9qp9597Jm5LyWRVPRwc&ved=2ahUKEwipoY2n0-yQAxUT_7sIHeJPEp8Q0NsOegQIBBAB&aep=10&ntc=1&mstk=AUtExfBSTneL-yL_S3XpxeTlS_tmqhR8O1g92uvI9VAspMrQ3IVghiisHvM-iaduIE26DLJ2K8EGB4_RFpVkVRB6sPxelRoSG2FOUW_XzAKDMxwOIhmqhfqvzeidagdwBGOpY9Yf1s00egBqdPiRrBgU37avllIdc6JfJYXzpsvaaWpynvEksGpTb3F99g0IlbWlrrOXhjVBdZC2_eYgQRqlBzIN16cCV6ToxnqiM5wGuoDky9yH2TY_JZpVe9cHFAVovjUrXmOS9WnL6zmIk0pdF_p76S_hpSAk198HfTdqJQII5rCaEjMwsoO2OcHkYVrfchvG-Z3z4W0cYg&csuir=1&mtid=q4IUaYSzO9a79u8P6f2DsQM"
fetched: "2026-04-22"
title: "nessie branch best practice - Google Search"
author: "published:"
published: "created: 2026-04-22"
clipped_from: obsidian-web-clipper
---
## Search Results

Project Nessie, a transactional catalog for data lakes with Git-like semantics, allows the application of standard software development branching best practices to data management.

Core Principles

- **Isolation**: Create branches for all development or data transformation tasks to isolate changes and prevent disruption to production workloads running on the `main` branch.
- **Atomic Merges**: Use branches to group multiple, cross-table changes into a single, atomic transaction that can be merged back into the main branch. This guarantees that data consumers see a consistent view of the data at all times.
- **Review Process**: Implement a review process for changes made in a development branch before merging them back to the main branch, similar to code reviews.
- **Reproducibility and Rollbacks**: Tag specific commits to maintain historical records for auditing or to reproduce models and analyses. If issues are discovered, the entire branch or recent merges can be rolled back or deleted instantly.

Branching Strategies

While Nessie supports various Git-like workflows, common strategies can be adapted:

- **Feature Branches**: For new data pipelines, experiments, or schema changes, create a dedicated feature branch. All modifications (ingestion, transformation, quality checks) occur within this branch. The branch is merged to `main` only after validation passes.
- **Main/Develop Branches**: A structure similar to GitFlow can be used, with a `main` branch containing production-ready data and a `develop` branch for ongoing, integrated development (though simple GitHub Flow with just `main` and feature branches is often sufficient for data workflows).
- **Short-lived branches**: For agile data operations, branches should ideally be short-lived, used for a specific task, validated, and merged quickly.

Commit Best Practices

- **Meaningful Messages**: Provide meaningful commit summaries and messages (e.g., `aggregate-financial-stuff 2020/12/24`) so that users can understand the purpose and content of the changes when reviewing the history.
- **Atomic Commits**: Keep commits logically atomic, representing a single, complete set of related changes.

Operational Practices

- **Data Validation**: Run data quality checks and verification processes on the development branch to ensure data correctness before merging into `main`.
- **No Disruption**: Ensure that ETL/ELT processes operate exclusively on feature/development branches to avoid affecting production queries on the `main` branch.
- **Leverage Tags**: Use tags to mark important, stable versions of your data lake (e.g., end-of-quarter data for reporting) for easy future reference and time travel.

- Best Practices - Project Nessie: Transactional Catalog for Data...
	Commit Messages. Give Nessie commits a meaningful commit summary and message, like aggregate-financial-stuff 2020/12/24, so peopl...
	Project Nessie
- Nessie: Git for Data Lakes | Blog Post - Dremio
	With Nessie such processes are easy to implement and automate through the use of branches and commits. The ETL job begins by creat...![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFEAAABSCAMAAAAbxciqAAAAw1BMVEX/9/X//Pn/+fb///v///379/acrbf59PLp5+iyvcXt6+vKz9OQnqr57+0A3uAA1NZgeo1yiJmnsruUprFngJLg4OIAPWC7w8oAOF3X2t3S1NiClqTDzNJSdYtQcIU6YXra4uLI2Nlmt7myzM1aurxBuLmmyctvwMJwsrY+zM6JwsQXv8I8l5sAyMmn7/DN+vvh8/Srq6xP4+WE7e+JqKxq4OPDtbg5f4Scs7WHtbkAp6oAJVEhTmwqWHQASGhKZn4AAD72+OJQAAADbElEQVRYhe2Xa3ejNhCGmcFCV8dIIBMQoGSbdLvbZrvp/WLh/v9fVUGcxun2Q0M4PW0P7wcZhHn0SjNHGpJk1X9GuL1aCgXJdguwvX7z2VLE65vb28/l25srXASH2y92F7vd7t377TLAZARe3H25+2opIF7fXVx8+Ppjc0+XASbJ+903m28/NPdLWUyStxcftzffWViKFz1+/8OPVbKYwbiO9bs3d82CwKif7m6XtDjq51+2ywJR3C8YllWrVq36/wjH3RH+vIvj/G0dmwqQGvqcADzDuWcFZL9KIJcCkUajSKM5oACyRaAEPjX/d4gHT8meUn3UgrpjzojuNTUm5cdegpIvRkKmi3Kzp04Jp9oguDSeZFYV1l81gc4jpqEahO/zY8l8n1E79CZVhQllfrCzZq03dtjTY0sZo8yWmgh7NEXBcyLqZEZ9BUWeQvYbrQZ1MHJfhKy6zA7SORq09hDMi49eZDZGVyap5XUKY5PWxqYszreKeVWLl5uc0g7HTD9vxgyfrmcAPxng9RCYcpuyx2xuzqOBhODjSp6N9VdXT8DW+95C25GWjdPUvsbp3WnixntvcLpB28AJi649/QN4AQk+H83uK5ENVDQiFDTeDlW02VBkTIoElBaNN0BjT+J6AUza8aWuinCwkqUx+WIUhWRPFpXewKZFmbdD1yCafSl0nmt0PrcIyqVp66kuSy36wG1wPtqbiGCOzgvjmG/t0fVPRJ1tpHZM9tCPAyeDqAMhvnEqHcdzKdqDaKw8CKM30Yt28EBEW9vQmK7nqVbCPPPIqsta9mQkYiTyPN2U3I25PRJBHoUuXRiJsnf9IxGyzh0aPgQJfenc0zrW+5a2A45EgxPRDowFq09EWntTe1pHj3mqC3ATkVNBh4ZGj7oKcY+B5izWVTj4BhoNPLQREpffhJCB4nCKdYZU+zIXLLg6dPkYXBe7WxO6vuZqE0fNvT9PHyLG2JO43Y6ZSGKPoJAQMj2d8hFRjM8JBSrw1B37BSUPORtL72dbysJfCqtWrVq16p/TVC89lArJqXbC1xU/VrCa1kwwZlkdiz8R64ukmVPlnUTjWdtxpx4apnJnnSumk3Au0elYeaii81ypWNJ3rna8y7L586aKV6YtjCm4MYpwxTMeoeY1K4l//JxKOCQzPhFW/Vv1O46XQkS3aK4YAAAAAElFTkSuQmCC)
	Dremio
- Data Lakehouse Versioning: Nessie vs Iceberg vs LakeFS - Dremio
	Use Cases for Nessie Nessie's approach to data lake versioning supports various data engineering and data science workflows: Isola...![](data:image/jpeg;base64,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)
	Dremio

Show all

Google apps

Google Account

stefano parodi

fanenji@gmail.com