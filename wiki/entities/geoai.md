---
type: entity
title: GeoAI
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, ai, python, open-source, tool]
related: [opengeos, q-wu, geospatial-ai-overview, leafmap, maplibre, qgis, pytorch, transformers-hugging-face, pytorch-segmentation-models, torchange]
sources: ["GeoAI.md"]
---
# GeoAI

GeoAI is a comprehensive Python package for integrating artificial intelligence with geospatial data analysis and visualization. Developed by [[Q. Wu]] and the [[opengeos]] organization, it provides a unified framework for processing satellite imagery, aerial photographs, and vector data using deep learning models.

## Core Capabilities

1. **Search and Download**: Interactive and programmatic access to remote sensing imagery and geospatial data from providers like Sentinel, Landsat, and NAIP.
2. **Dataset Preparation**: Automated generation of training datasets with image chips and corresponding labels, including vector-to-raster and raster-to-vector conversion utilities.
3. **Model Training**: Support for classification, detection, and segmentation tasks with pre-trained models and transfer learning utilities.
4. **Inference Pipelines**: Apply trained models to new geospatial datasets.
5. **Interactive Visualization**: Integration with [[Leafmap]] and [[MapLibre]] for multi-layer visualization of vector and raster data.
6. **QGIS Plugin**: A dedicated plugin enabling AI-powered geospatial workflows directly within the [[QGIS]] desktop environment without coding.

## Technical Stack

GeoAI integrates with:
- [[PyTorch]] for deep learning
- [[Transformers (Hugging Face)]] for transformer-based models
- [[PyTorch Segmentation Models]] for segmentation tasks
- [[torchange]] for change detection

## Supported Data Formats

GeoTIFF, JPEG2000, GeoJSON, Shapefile, GeoPackage, GeoParquet

## Installation

Available via pip (`geoai-py`), conda, and mamba from conda-forge.

## Documentation and Resources

- Official site: [https://opengeoai.org](https://opengeoai.org/)
- Book: [https://book.opengeoai.org](https://book.opengeoai.org/)
- Video tutorials and workshops available on YouTube

## Funding

Supported by [[NASA]] (Grant No. 80NSSC22K1742) and [[AmericaView]]/[[USGS]] (Grant/Cooperative Agreement No. G23AP00683).

## Citations

- Wu, Q. (2026). GeoAI: A Python package for integrating artificial intelligence with geospatial data analysis and visualization. *Journal of Open Source Software*, 11(118), 9605.
- Wu, Q. (2026). *GeoAI with Python: A Practical Guide to Open-Source Geospatial AI*.
