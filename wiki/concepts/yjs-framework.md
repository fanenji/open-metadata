---
type: concept
title: Yjs Framework
created: 2026-04-29
updated: 2026-04-29
tags: [collaborative-editing, crdt, javascript, framework]
related: [jupytergis, jupytercad, jupyterlab]
sources: ["JupyterGIS.md"]
---
# Yjs Framework

Yjs is a JavaScript framework implementing CRDT (Conflict-free Replicated Data Type) data structures for real-time collaborative editing. It is the foundation of the collaborative editing features in [[JupyterLab]] core and is used by both [[JupyterGIS]] and [[JupyterCAD]].

## Relevance to Data Platform

While Yjs is a frontend technology, its use in JupyterGIS enables collaborative geospatial authoring workflows that could complement the data platform's backend processing pipeline. If the platform requires multi-user GIS editing capabilities, Yjs provides the underlying synchronization mechanism.