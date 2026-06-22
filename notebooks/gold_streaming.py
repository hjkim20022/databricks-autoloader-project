from pyspark.sql.functions import sum

silver_df = spark.read.table(
    "autoloader_catalog.retail_streaming.silver_retail_sales"
)

gold_df = (
    silver_df
    .groupBy("category")
    .agg(
        sum("revenue").alias("total_revenue")
    )
)


gold_df.write.mode("overwrite").saveAsTable(
    "autoloader_catalog.retail_streaming.gold_retail_sales"
)

display(gold_df)
