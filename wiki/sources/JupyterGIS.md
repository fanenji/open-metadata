---
type: source
title: JupyterGIS
created: 2026-04-29
updated: 2026-04-29
tags: [jupyter, gis, collaborative-editing, geospatial, open-source]
related: [jupytergis, yjs-framework, sylvain-corlay, quantstack, simula-research-lab, jupytercad]
sources: ["JupyterGIS.md"]
authors: [Sylvain Corlay, Anne Fouilloux, Monika Weissschnur]
year: 2024
url: "https://blog.jupyter.org/jupytergis-d63b7adf9d0c"
venue: "Jupyter Blog"
---
# JupyterGIS

This blog post announces the European Space Agency (ESA) funding of a project to build JupyterGIS, the first open-source GIS tool with built-in collaborative editing. The consortium is led by [[QuantStack]] and [[Simula Research Lab]].

The project aims to create a web-based GIS user interface as a JupyterLab extension, enabling collaborative editing of QGIS project files using the [[Yjs framework]] (CRDT-based). It will also integrate GIS capabilities inline in Jupyter notebooks via the display system. The project plans to explore integration with the Copernicus Data Space Ecosystem (CDSE) and the European Open Science Cloud (EOSC).

JupyterGIS builds on three years of prior work on collaborative editing in JupyterLab core. The sibling project [[JupyterCAD]] shares the same architectural approach. Real-world applications include emergency management, where collaborative GIS can improve coordination among response teams.

Partners include the LIVE-Env project (Harvard), Berkeley Institute for Data Sciences (BIDS), Schmidt Center for Data Science and Environment (DSE), and 2i2c.