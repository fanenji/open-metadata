type: concept
title: AI and ML Blueprint
created: 2026-04-29
updated: 2026-04-29
tags: [architecture, blueprint, machine-learning, artificial-intelligence, mlops]
related: [unified-data-infrastructure-architecture, data-lifecycle-stages, modern-business-intelligence-blueprint, multimodal-data-processing-blueprint, feature-store-architecture, data-lakehouse]
sources: ["Data-Report-Martin-Inline-Graphics-R8-1.pdf"]
---
# AI and ML Blueprint

Blueprint #3 of the [[unified-data-infrastructure-architecture]], representing the architecture for the full ML lifecycle including feature engineering, model training, experiment tracking, model registry, and inference serving. This blueprint addresses the unique infrastructure requirements of machine learning workloads.

## Architecture

The blueprint is organized into three main phases:

### Data Transformation
- **Data Sources**: Data lake + data warehouse + streaming engine
- **Data Labeling**: Labelbox, Snorkel, Scale, SageMaker
- **Dataflow Automation**: Airflow, Pachyderm, Prefect, Tecton, Kubeflow
- **Feature Store**: Tecton (feature management and serving)
- **Query Engines**: Presto, Hive

### Model Training and Development
- **Data Science Platform**: Jupyter, Databricks, Domino, SageMaker, DataRobot, H2O, Colab, Deepnote
- **Data Science Libraries**: Spark, Pandas, NumPy, Dask
- **ML Frameworks**: Scikit-learn, XGBoost, MLlib
- **DL Frameworks**: TensorFlow, Keras, PyTorch, H2O, Hugging Face
- **Experiment Tracking**: Weights and Biases, Comet, MLflow
- **Model Registry**: Algorithmia, MLflow, SageMaker
- **Model Tuning**: Sigopt, Hyperopt, Ray Tune
- **Distributed Processing**: Spark, Ray, Dask, Distributed TF, Kubeflow, Horovod
- **RL Libraries**: Gym, Dopamine, RLlib, Coach
- **Visualization**: Tensorboard, Fiddler

### Model Inference
- **Batch Predictor**: Spark
- **Online Model Server**: TF Serving, Ray Serve, Seldon
- **Model Monitoring**: Fiddler, Arthur, Arize

## Key Characteristics

- Supports the full ML lifecycle from data preparation to production inference
- Feature store as a critical infrastructure component for feature management and serving
- Experiment tracking and model registry for reproducibility and governance
- Separate batch and online inference paths
- Higher complexity and specialized skill requirements than other blueprints

## Relationship to Other Blueprints

This blueprint builds on the storage and processing infrastructure of [[modern-business-intelligence-blueprint]] and [[multimodal-data-processing-blueprint]], adding ML-specific components. The [[feature-store-architecture]] concept in the wiki connects directly to the feature store component of this blueprint.