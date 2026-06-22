from pyspark.sql.functions import col

bronze_df = spark.read.table(
    "autoloader_catalog.retail_streaming.bronze_retail_sales"
)

silver_df = (
    bronze_df
    .withColumn(
        "revenue",
        col("quantity") * col("unit_price")
    )
)

silver_df.write.mode("overwrite").saveAsTable(
    "autoloader_catalog.retail_streaming.silver_retail_sales"
)

display(silver_df)
