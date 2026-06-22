# Databricks Auto Loader Streaming Project

This project implements a retail data pipeline using Databricks Auto Loader, Delta Lake, and Medallion Architecture.

## Architecture

CSV Files → Auto Loader → Bronze Delta Table → Silver Curated Table → Gold Business Aggregations

## Project Objectives

- Implement incremental file ingestion using Databricks Auto Loader
- Build a Medallion Architecture (Bronze, Silver, Gold)
- Process streaming data using Structured Streaming
- Store data in Delta Lake tables
- Implement checkpointing for fault tolerance and exactly-once processing
- Automate pipeline execution using Databricks Workflows

## Technologies

- Databricks
- PySpark
- Auto Loader
- Structured Streaming
- Delta Lake
- GitHub
- GitHub Actions
- Databricks Workflows

## Project Implementation

This project implements an end-to-end Databricks Auto Loader pipeline using Medallion Architecture.

### Pipeline Flow

CSV files → Auto Loader → Bronze Delta Table → Silver Delta Table → Gold Delta Table

### Completed Features

- Created Unity Catalog: `autoloader_catalog`
- Created schema: `retail_streaming`
- Created managed volumes: `raw_data` and `checkpoints`
- Uploaded incremental CSV files: `retail_sales_01.csv` and `retail_sales_02.csv`
- Implemented Bronze Auto Loader ingestion
- Implemented checkpointing and schema tracking
- Created Silver transformation with revenue calculation
- Created Gold aggregation by category
- Orchestrated pipeline using Databricks Workflows
