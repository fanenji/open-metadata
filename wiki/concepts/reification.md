---
type: concept
title: Reification
created: 2026-04-02
updated: 2026-04-02
tags: [rdf, ontology, pattern]
related: [property-graph-vs-rdf-owl]
sources: ["Property Graphs vs. Rigid Ontologies Choosing the Right Foundation for Enterprise AI Memory.md"]
---
# Reification

An RDF pattern required to attach properties to relationships. In RDF, relationships themselves cannot carry properties directly; instead, a new node must be created to represent the relationship, with the relationship properties attached to that node. This is awkward compared to property graphs, where relationships naturally carry their own properties (e.g., allocation percentage, escalation reason, severity).