# Bronze Auto Loader Streaming

raw_path = "/Volumes/autoloader_catalog/retail_streaming/raw_data/"

checkpoint_path = (
    "/Volumes/autoloader_catalog/"
    "retail_streaming/checkpoints/bronze_retail_sales"
)

schema_path = (
    "/Volumes/autoloader_catalog/"
    "retail_streaming/checkpoints/bronze_retail_sales_schema"
)

bronze_table = (
    "autoloader_catalog.retail_streaming.bronze_retail_sales"
)

bronze_df = (
    spark.readStream
         .format("cloudFiles")
         .option("cloudFiles.format", "csv")
         .option("header", "true")
         .option("cloudFiles.inferColumnTypes", "true")
         .option("cloudFiles.schemaLocation", schema_path)
         .load(raw_path)
)

(
    bronze_df.writeStream
             .format("delta")
             .option("checkpointLocation", checkpoint_path)
             .outputMode("append")
             .trigger(availableNow=True)
             .toTable(bronze_table)
)
