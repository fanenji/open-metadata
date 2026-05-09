---
type: source
title: "GeoAI: A Python Package for Integrating Artificial Intelligence with Geospatial Data Analysis and Visualization"
created: 2026-04-04
updated: 2026-04-29
tags: [geospatial, ai, python, open-source]
related: [geoai, geospatial-ai-overview, opengeos, q-wu]
sources: ["GeoAI.md"]
authors: [Q. Wu]
year: 2026
url: "https://opengeoai.org/"
venue: "Journal of Open Source Software, 11(118), 9605"
---
# GeoAI: A Python Package for Integrating Artificial Intelligence with Geospatial Data Analysis and Visualization

This source describes the GeoAI Python package, a comprehensive tool for integrating artificial intelligence with geospatial data analysis and visualization. Developed by [[Q. Wu]] and the [[opengeos]] organization, GeoAI provides a unified framework for processing satellite imagery, aerial photographs, and vector data using state-of-the-art deep learning models.

The package offers six core capabilities: (1) interactive and programmatic search and download of remote sensing imagery, (2) automated dataset preparation with image chips and label generation, (3) model training for classification, detection, and segmentation, (4) inference pipelines for applying models to new datasets, (5) interactive visualization via [[Leafmap]] and [[MapLibre]], and (6) a [[QGIS]] plugin for code-free AI workflows.

GeoAI integrates with [[PyTorch]], [[Transformers (Hugging Face)]], [[PyTorch Segmentation Models]], and [[torchange]]. It addresses a gap in the geospatial AI ecosystem by providing high-level APIs that abstract complex ML workflows while maintaining flexibility for advanced users. The package is funded by [[NASA]] and [[AmericaView]]/[[USGS]].

The source includes a statement of need arguing that existing solutions like [[TorchGeo]], [[TerraTorch]], and [[SRAI]] provide foundational tools but lack comprehensive, high-level interfaces for the broader geospatial community.
