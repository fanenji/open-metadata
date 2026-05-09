---
type: concept
title: Collaborative Editing (CRDT-based)
created: 2026-04-29
updated: 2026-04-29
tags: [collaborative-editing, crdt, real-time, geospatial]
related: [jupytergis, yjs-framework, jupytercad]
sources: ["JupyterGIS.md"]
---
# Collaborative Editing (CRDT-based)

Collaborative editing using Conflict-free Replicated Data Types (CRDTs) enables multiple users to edit the same document simultaneously without conflicts. The [[Yjs framework]] implements CRDT data structures and is used in [[JupyterLab]] core.

## Application to GIS

[[JupyterGIS]] will be the first open-source GIS tool to provide collaborative editing features. This is particularly valuable for geoscience workflows involving large teams (climate modeling, agriculture, ecology, urban planning, emergency management) where coordination across diverse expertise is essential.

## Design Principle

The JupyterGIS team emphasizes that collaborative editing must be designed into the data model from inception, as retrofitting it into an existing application is considerably more difficult. This is why JupyterGIS is being built from the ground up with CRDT-based collaboration.