---
type: concept
title: dbt Developer Experience (DevEx)
created: 2026-04-29
updated: 2026-05-07
tags: ["dbt", "devex", "analytics-engineering", "data-engineering", "team-empowerment", "developer-experience", "onboarding", "tooling", "blablacar", "dbt-power-user-extension", "dbt-dry-run", "individual-datasets"]
related: ["dbt-project-organization-strategies", "dbt-project-scaffolding", "dbt-cloud-environments", "dbt-git-branching-strategies", "blablacar", "dbt-migration-strategy", "dbt-power-user-extension", "dbt-dry-run", "individual-datasets"]
sources: ["How to manage and schedule dbt.md", "One Thousands and One dbt Models How BlaBlaCar Moved to dbt in 12 months.md"]
---
# dbt Developer Experience (DevEx)

The practice of designing dbt workflows, tooling, and environments to empower analytics teams and maximize their productivity. DevEx is a key responsibility of data engineers in the dbt ecosystem. [[BlaBlaCar]] invested heavily in DevEx to enable over 50 data professionals to work effectively with dbt, serving as a reference implementation.

## User Personas

- **Data Engineers**: Work on foundational layers (sources, staging tables). Build the platform and infrastructure.
- **Analytics Engineers**: Work across all modeling layers (staging, core, intermediate, mart). Bridge between data engineering and analysis.
- **Data Analysts / Business Analysts / Web Analysts**: Use final mart models, need to understand column definitions, make small changes, store analyses. Often come from BI tool backgrounds.
- **Management (Head of Data, VP Tech)**: Need high-level view of modeling. dbt docs serve as an entry point.
- **Stakeholders**: Generally not dbt users — dbt is too technical.

## DevEx Levers

### Git Workflow
- Clear branching strategy, code review process, and merge policies.
- *BlaBlaCar insight*: Users may be unfamiliar with git; provide onboarding materials like cheat sheets to bridge the gap. The first cheat sheet provided at BlaBlaCar was on git, not dbt.

### CI/CD Pipeline
- Fast feedback on changes, automated testing, deployment automation.
- *BlaBlaCar implementation*: CI/CD pipeline on Jenkins with manifest generation. They use [[dbt-dry-run]], an open-source package that leverages BigQuery's dry run API to catch SQL errors before deployment.

### Documentation
- Well-maintained dbt docs, clear column descriptions, lineage visualization.
- *BlaBlaCar approach*: Documentation serves multiple purposes—how-to guides, reference pages, and discovery tips. They also provide cheat sheets for common tasks.

### Environment Management
- Dev, staging, production environments with appropriate data subsets.
- *BlaBlaCar practice*: Each developer gets a personal BigQuery dataset ([[individual-datasets]]) for safe dbt run testing without affecting production.

### Tooling
- IDE integration, CLI shortcuts, custom macros for common patterns.
- *BlaBlaCar enhancements*:
  - VS Code + [[dbt-power-user-extension]] replaced BigQuery UI as the primary SQL development tool.
  - A lightweight CLI setup tool creates standardized dbt projects and profiles with minimal input, reducing setup time for 50+ users.

### Training and Onboarding
- Onboarding materials, pair programming, knowledge sharing sessions.
- *BlaBlaCar program*:
  - Basic dbt onboarding (models, projects, run commands)
  - Framework onboarding (DAG generator, CLI tool)
  - Cheat sheets (first was on git)
  - Ongoing documentation with multiple types.

## Data Engineer's Role

The primary mission of a data engineer in the dbt context is to empower analytics teams through data tools. This includes:
- Identifying when analytics teams are under-equipped or working inefficiently.
- Providing a neat developer experience for every dbt user.
- Building foundational layers while giving analytics teams ownership of their domain models.
- Ensuring dbt projects are independent from other tools (e.g., not in the Airflow repo).

In the BlaBlaCar context, data engineers built the CLI setup tool, dry-run integration, and personal datasets to reduce friction for analytics engineers and analysts.

## Challenges in DevEx

- Balancing abstraction (easy onboarding) with flexibility (power users wanting custom dbt commands).
- Discovery problem: users don't know what tools can do for them (e.g., VS Code features).
- Version control learning curve for non-engineering users.

## Recommendations

- Analytics teams should own dbt repos.
- Data engineers should focus on DevEx and foundational layers.
- Provide clear documentation and training for analytics team members.
- Automate repetitive tasks through macros and CI/CD.
- Invest in developer tooling (IDE extensions, dry-run checks, standardized project setup) to reduce friction and onboarding time.