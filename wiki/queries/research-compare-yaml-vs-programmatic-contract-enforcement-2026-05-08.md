---
type: query
title: "Research: Compare YAML vs Programmatic Contract Enforcement"
created: 2026-05-08
origin: deep-research
tags: [research]
---

# Research: Compare YAML vs Programmatic Contract Enforcement

```wiki
---
title: YAML vs Programmatic Contract Enforcement
created: 2026-05-12
updated: 2026-05-12
type: comparison
tags: [data-contracts, data-quality, dbt, yaml, programmatic-enforcement]
related: [[dbt-data-contract-implementation]], [[YAML-data-contract-format]], [[great-expectations-for-data-contracts]], [[dbt-macros]], [[data-contract-platform]], [[dbt-testing-patterns]], [[engineering-led-data-quality]], [[data-contract-observability]]
sources: ["JSON vs YAML: When to Use Which - DEV Community.md", "API Contract: Enforcement of Compliance with a Style Guide - SAP Community.md", "Why is YAML the best language for data contracts - Tom Baeyens LinkedIn.md", "YAML Policy as Code (PaC) - Monokle.md", "Data Contracts Explained: Key Aspects, Tools, Setup in 2026 - Atlan.md"]
---

# YAML vs Programmatic Contract Enforcement

Data contract enforcement is the mechanism by which agreements between data producers and consumers are validated, monitored, and guaranteed. There are two dominant strategies for implementing this enforcement: **YAML-based (declarative) contracts** and **programmatic (code-driven) contracts**. This page compares the two approaches, drawing on existing wiki knowledge and the latest community discussions.

## 1. YAML-Based Contract Enforcement

**Definition**: Contract rules are expressed in a structured, human-readable YAML (or JSON) file that is treated as a configuration artifact. Enforcement is delegated to tools that parse the YAML and execute the prescribed checks, often as part of a [[CI-CD-for-data-pipelines|CI/CD pipeline]] or data platform.

### 1.1 Key Characteristics

- **Human-centric syntax**: YAML's indentation-based structure, comments, and lack of mandatory quotes make it easier for data engineers, analysts, and even domain experts to write and review [3].  
- **Git‑friendly**: YAML files are plain text; changes appear as line‑by‑line diffs in pull requests, enabling peer review, approval workflows, and complete audit trails [3][4].  
- **Tool‑neutral specification**: The contract defines *what* to enforce (field types, nullability, allowed values, SLA, ownership), while the enforcement engine (dbt, Soda, Great Expectations via YAML configs, OPA) handles *how* to enforce it.  
- **Policy as Code (PaC)**: YAML contracts can be treated as machine‑readable policies that are automatically validated at CI/CD gates, ensuring that no data product enters production without meeting its declared contract [4].  
- **Examples in the wild**:  
  - [[dbt-data-contract-implementation|dbt contracts]]: `{{ config(contract = {…}) }}` blocks or separate YAML files for models [see dbt‑contract‑artifact‑integration].  
  - Soda.io checks in `checks.yml` files [5].  
  - OpenAPI / AsyncAPI style guides, linted by tools like Spectral or Monokle [2].  
  - Data governance policies (access masking, role‑based permissions) expressed in YAML [5].

### 1.2 Enforcement Mechanisms

YAML contracts don’t enforce themselves; they rely on an execution layer that reads the YAML and runs:

- **Linters & policy engines** (e.g., Spectral, Monokle, Open Policy Agent with Rego) that validate YAML structure and custom rules [2][4].  
- **dbt tests** (singular, generic, or from packages like [[dbt-expectations]]) that are triggered during `dbt test` or `dbt build`.  
- **CI/CD pipelines** that invoke these linters/test runners and block merges on failure [4].  
- **Data quality platforms** (Soda, Great Expectations, Monte Carlo) that schedule regular scans and surface contract violations via dashboards or alerts.

This separation of *specification* and *execution* is often cited as the main advantage of YAML‑based contracts: the contract is a living document that can be understood without reading the validation code.

## 2. Programmatic Contract Enforcement

**Definition**: Enforcement logic is written directly in a general‑purpose or domain‑specific programming language (Python, SQL, dbt Jinja macros) as test functions, procedures, or custom scripts. The contract is embedded in the *execution logic* rather than in a separate configuration file.

### 2.1 Key Characteristics

- **Maximum flexibility**: Code can express arbitrarily complex rules—multi‑table joins, API calls, statistical models (e.g., anomaly detection), and custom notification logic—that are difficult or impossible to represent in static YAML schemas.  
- **Deep pipeline integration**: Programmatic tests can be injected directly into ETL/ELT transformations (e.g., dbt macros, Python tasks in Airflow/Kestra), eliminating the need for a separate validation step.  
- **Rich testing libraries**: Frameworks like Great Expectations, [[dbt-expectations]], or plain pytest allow data engineers to leverage mature software testing patterns (mocking, parameterization, fixtures) for data validation.  
- **Examples**:  
  - **dbt macros**: Reusable Jinja‑SQL tests that perform complex comparisons, reference environment variables, or call external services [see [[dbt-macros]]].  
  - **Great Expectations suites**: Python objects that define expectations and can be run interactively or in a pipeline; they can also be serialised to YAML for portability, but the native interface is Python.  
  - **Custom SQL checks** run via [[on-run-end-hook|dbt on‑run‑end hooks]] or Airflow operators.  
  - **Data validation libraries** like Pandera (pandas) or Deequ (Spark).

### 2.2 Enforcement Mechanisms

Programmatic enforcement typically happens:

- **At runtime**, during data transformation (e.g., inside a dbt model’s Jinja code).  
- **As standalone test suites** executed by CI/CD, orchestrated by Airflow/Dagster, or triggered by webhooks.  
- **Through “shift‑left” hooks** (pre‑commit, pre‑merge) that run scripts to validate incoming changes.

Because the logic is code, it is version‑controlled and can be reviewed, but the *intent* of the contract may be harder to extract for non‑technical stakeholders.

## 3. Comparative Analysis

| Criterion                  | YAML‑Based Enforcement                                          | Programmatic Enforcement                                         |
|----------------------------|-----------------------------------------------------------------|------------------------------------------------------------------|
| **Readability**            | High – easily read by analysts, managers, and tools [3]         | Low‑medium – requires programming knowledge; intent may be obscured by implementation details |
| **Version Control**        | Native – clean diffs, PR‑friendly [3]                           | Native, but diffs often contain implementation noise (e.g., loops, error handling) |
| **Flexibility**            | Limited – constrained by schema and linter rules; complex logic often requires custom tool extensions | Unlimited – any computation can be performed; suitable for statistical, multi‑source, or API‑driven checks |
| **Tool Support**           | Growing – dbt, Soda, Spectral, Monokle, and OPA offer YAML‑based interfaces [2][4][5] | Mature – Great Expectations, dbt macros, SQL test frameworks, general‑purpose programming libraries |
| **Setup Complexity**       | Low for simple rules – a few YAML lines; higher when writing custom linter plugins or DSLs | Medium – requires writing and maintaining code, but reuses existing engineering skills |
| **CI/CD Integration**      | Straightforward – run a linter/validator, check exit code [4]   | Straightforward – run a script, check exit code; test frameworks provide reporters |
| **Separation of Concerns** | Clear – contract spec is isolated from enforcement code [3]     | Blurred – enforcement is the contract; risk of “contract drift” if not carefully documented |
| **Stakeholder Alignment**  | Easier – YAML becomes a shared artifact between producers and consumers, replacing lengthy email threads [3] | More difficult – requires translation from business requirements to code; test descriptions can serve as documentation |
| **Performance Overhead**   | Typically negligible – linting/validation runs quickly           | Depends on the tests; complex SQL or API calls may be slower     |

## 4. Hybrid Approaches

In practice, many teams blend the two paradigms:

- **YAML spec + programmatic engine**: A YAML file defines the expected schema and simple constraints; a Python or dbt macro reads the YAML and generates the actual tests. This is the pattern behind [[dbt-data-contract-implementation|dbt’s contract feature]] and many Great Expectations configurations.  
- **Programmatic tests with YAML export**: Great Expectations suites can be exported to YAML, making the contract portable while retaining the ability to define intricate logic in Python.  
- **Layered validation**: Coarse‑grained YAML contracts are checked at CI/pre‑commit (fast feedback), while deeper, programmatic integrity checks run nightly or as part of a [[data-contract-observability|full observability stack]].

## 5. Existing Wiki Coverage & Gaps

The wiki already contains detailed material on:

- [[dbt-data-contract-implementation]] – dbt’s YAML contract syntax, preflight validation, and artifact integration.  
- [[great-expectations-for-data-contracts]] – using Great Expectations as a programmatic enforcement engine.  
- [[dbt-testing-patterns]] – categorisation of tests, including [[dbt-expectations]].  
- [[data-contract-platform]] – general concept of a platform that enforces contracts.

This page fills the gap of a direct, criteria‑based comparison between the two styles.

## 6. Contradictions & Open Questions

- The claim that “YAML is best for data contracts” [3] is not universally accepted. Some practitioners argue that complex contracts quickly outgrow YAML’s expressiveness, leading to “YAML spaghetti” that is as hard to read as the code it replaces.  
- The line between “YAML‑based” and “programmatic” is fuzzy: dbt tests expressed as YAML selectors are ultimately compiled to SQL and run programmatically. The distinction is more about the *authoring* experience and the *primary* artifact used to communicate the contract.  
- YAML schema validation standards (like JSON Schema for YAML) are less mature than their JSON counterparts [1]; however, the data contracts domain often uses custom tool‑specific schemas (e.g., dbt’s contract structure) rather than a universal YAML schema language.

## 7. Suggested Additional Sources Worth Finding

- Andrew Jones’ original “Data Contracts” articles at GoCardless ([[andrew-jones]], [[GoCardless]]).  
- dbt Labs’ official guidance on “When to use dbt contracts vs. custom tests” ([[dbt-data-contract-implementation]] already linked).  
- Soda’s documentation on “programmatic checks” vs. “SodaCL” (YAML).  
- The “Policy as Code” movement beyond data (Open Policy Agent, HashiCorp Sentinel) to understand how YAML/Rego trade‑offs apply in adjacent fields.

## 8. Conclusion

Neither YAML‑based nor programmatic enforcement is universally superior. YAML shines when the primary goal is **clarity, collaboration, and governance**—providing a shared, version‑controlled specification that non‑engineers can understand. Programmatic enforcement excels in **complex, dynamic, or high‑performance environments** where flexibility and reusability of software engineering practices are paramount. The mature data engineering team will often combine both, using YAML as the “contract surface” and code as the “contract engine,” aligning with the broader trend toward [[engineering-led-data-quality]] and [[shift-left-data-quality]].

```

## References

1. [JSON vs YAML: When to Use Which (Complete Developer Guide) - DEV Community](https://dev.to/_d7eb1c1703182e3ce1782/json-vs-yaml-when-to-use-which-complete-developer-guide-1ijn) — dev.to
2. [API Contract: Enforcement of Compliance with a Sty... - SAP Community](https://community.sap.com/t5/technology-blog-posts-by-members/api-contract-enforcement-of-compliance-with-a-style-guide/ba-p/13545442) — community.sap.com
3. [Why is YAML the best language for data contracts? A data contract is a formal specification of a dataset. It defines field names, data types, allowed values, nullability, and constraints. These… | Tom Baeyens](https://www.linkedin.com/posts/tombaeyens_why-is-yaml-the-best-language-for-data-contracts-activity-7413893545901711361-EHCb) — linkedin.com
4. [YAML Policy as Code (PaC) | Monokle](https://monokle.io/learn/what-is-policy-as-code-the-best-way-to-streamline-kubernetes-environments) — monokle.io
5. [Data Contracts Explained: Key Aspects, Tools, Setup in 2026](https://atlan.com/data-contracts/) — atlan.com
