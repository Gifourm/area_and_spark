from pyspark.sql import SparkSession, DataFrame

spark = SparkSession.builder.getOrCreate()
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")


def get_all_products(products_table: DataFrame, categories_table: DataFrame, links_table: DataFrame) -> DataFrame:
    query = products_table.join(links_table, "productId", "left") \
                        .join(categories_table, "categoryId", "left") \
                        .select("productName", "categoryName")
    query.show()
    return query
