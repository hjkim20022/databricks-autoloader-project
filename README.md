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
