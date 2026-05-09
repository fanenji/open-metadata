---
type: concept
title: Local-First Software
created: 2026-04-29
updated: 2026-04-29
tags: [local-first, crdt, collaborative-apps, decentralized-systems]
related: [martin-kleppmann, distributed-systems-fundamentals, formal-verification]
sources: ["Designing Data-intensive Applications with Martin Kleppmann-SUMMARY.md"]
---
# Local-First Software

[[Martin Kleppmann]]'s main research area for the last ~10 years. Collaborative applications (like Google Docs, Figma) that do not depend on a single cloud provider — the user controls their data.

## Engineering Challenges

Much harder than centralized versions:

- **Access control in decentralized systems**: In a centralized system, the server decides "does the revocation arrive before the edit?" In a distributed/peer-to-peer system, different nodes may see events in different orders → permanent inconsistency. Solving this *without consensus* (to preserve high availability and offline operation) is an open research problem, close to a solution in **Automerge**.
- **Unreliable timestamps**: In a decentralized context, a user with revoked access can forge timestamps to backdate an edit and bypass access control. Clocks cannot be used as arbiters.

## Automerge

A CRDT (Conflict-free Replicated Data Type) library by Kleppmann that enables conflict-free merging in distributed systems. Foundation of local-first software.

## Relevance to Data Platform

While local-first software is primarily about collaborative applications, the underlying CRDT research and decentralized access control challenges have potential synergies with [[data-contract-platform]] and [[data-mesh]] architectures, where multiple domains need to coordinate without a central authority.