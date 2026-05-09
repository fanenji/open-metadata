---
type: entity
title: Martin Kleppmann
created: 2026-04-29
updated: 2026-05-07
tags: [author, researcher, distributed-systems, formal-verification, local-first-software]
related: [ddia-book, distributed-systems-fundamentals, formal-verification, local-first-software, cloud-native-architecture-paradigm, designing-data-intensive-applications, chris-riccomini, kafka, rapportive, linkedin, go-test-it, y-combinator, jay-kreps, cloud-native-data-systems, distributed-systems-failure-modes]
sources: ["Designing Data-intensive Applications with Martin Kleppmann-SUMMARY.md", "Designing Data-intensive Applications with Martin Kleppmann.md"]
---

# Martin Kleppmann

Martin Kleppmann is a researcher and professor at the University of Cambridge, author of *Designing Data-Intensive Applications* (DDIA)—one of the most influential books on modern distributed systems—and creator of the [[local-first-software]] Automerge library. He transitioned from industry to academia after contributing to stream processing at LinkedIn.

## Career

- **Go Test It (2008)**: A cross-browser automated testing service based on Selenium. Bootstrapped, did not achieve significant traction.
- **Rapportive (2010–2012)**: A Gmail extension that provided social CRM features by embedding social media profiles inside the email client. Y Combinator alum. Acquired by LinkedIn in 2012.
- **LinkedIn (2012–2014)**: Joined after the Rapportive acquisition. Worked on LinkedIn Intro (shut down) before joining the stream processing team, where he contributed to Apache [[Kafka]] and co-developed Samza, a stream processing framework on Kafka. During this time he began writing *Designing Data-Intensive Applications* with 50% time support.
- **University of Cambridge (2014–present)**: Left LinkedIn to focus on writing DDIA full-time and joined Cambridge as a researcher. Continued writing and published the first edition in 2017. After the first edition, he fully transitioned to academic research. He is now a professor and lecturer, conducting research on [[local-first-software]], CRDTs, formal verification, and cryptography for supply chain provenance.

## Key Contributions

- **Author of *Designing Data-Intensive Applications*** (1st ed. 2017; 2nd ed. 2026 with co-author [[chris-riccomini]]). The book is widely considered the definitive practitioner-focused guide to data systems.
- **Co-developed Samza**, a stream processing framework built on [[Kafka]], and contributed to the stream processing ecosystem at LinkedIn.
- **Creator of Automerge**, a CRDT library for [[local-first-software]] that enables conflict-free merging in distributed applications.
- **Leading researcher** in local-first software, CRDTs, formal verification, and cryptography for supply chain provenance.
- **Advocate for formal verification** (model checking with TLA+, proof assistants). He believes that AI will make formal verification more practical for data systems, especially in the age of AI-generated code.

## Philosophy

- **Understanding fundamentals**: While higher-level abstractions and managed cloud services are convenient, understanding the internals of distributed systems remains a "superpower" for debugging, diagnosing performance issues, and making informed trade-offs. His book aims to provide that foundational understanding without requiring readers to build systems from scratch.
- **Ethics is part of engineering**: Engineers have a strong voice in defining trade-offs, and ethical considerations should be integrated into technical decisions.
- **Hybrid career path**: The hybrid path of moving between industry and academia (or vice versa) produces the strongest practitioners.