---
type: concept
title: Formal Verification
created: 2026-04-29
updated: 2026-05-07
tags: [formal-verification, model-checking, proof-assistant, tla-plus, ai, formal-methods, verification, code-quality]
related: [distributed-systems-fundamentals, martin-kleppmann, ddia-book, distributed-systems-failure-modes]
sources: ["Designing Data-intensive Applications with Martin Kleppmann-SUMMARY.md", "Designing Data-intensive Applications with Martin Kleppmann.md"]
---
# Formal Verification

**Formal verification** is the mathematical proof that a system satisfies a specification. Martin Kleppmann argues that formal verification will become increasingly important as AI-generated code becomes more prevalent. The techniques range from model checking to full proof assistants, forming a spectrum of assurance.

## Techniques

- **Model checking** (e.g., TLA+, FSBy): An automated approach that explores a finite or bounded state space to check properties. It is more accessible and a good starting point for verification.
- **Proof assistants** (e.g., Isabelle, Rocq/Coq, Lean): These allow constructing full mathematical proofs over all possible states. They are more powerful but require significant manual effort.

## Difference from Testing

Traditional testing verifies correctness for a set of input instances. Formal verification, in contrast, reasons over entire state spaces — "for every possible i and j, the length of the concatenated list is i+j." It proves the absence of certain classes of bugs rather than just detecting their presence.

## When to Use Formal Verification

Formal verification is most valuable for high-risk algorithms where bugs can cause data corruption or security vulnerabilities. It is not economical for routine industry work; [[Martin Kleppmann]] notes that he has only applied it in academia where months can be invested in a single algorithm. However, it is particularly relevant for distributed systems, where the state space is large and bugs are hard to reproduce with conventional testing.

### Relevance to the Data Platform

As the Data Platform incorporates more AI-generated code and complex distributed systems, formal verification techniques may become increasingly important for ensuring correctness and reliability.

## Why It Will Become More Important with AI

Formal verification is poised to become more critical as AI tooling advances:

1. **LLMs are becoming good at writing formal proofs**, reducing the human cost of verification.
2. **Vibe coding generates large amounts of code that humans cannot manually review**; automated verification becomes essential to guarantee correctness.
3. **Traditional tests are insufficient** for the scale and complexity of AI-generated code; formal proofs can guarantee the complete absence of certain bug types.
4. **Complement to testing**: Formal verification complements traditional testing by proving correctness, not just detecting bugs.

## Getting Started

Begin with model checking (TLA+, FSBy), which is much more approachable than proof assistants. Learning resources for proof assistants are scarce; [[Martin Kleppmann]] recommends learning in pairs with experienced colleagues.