from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MyApp").getOrCreate()
df = spark.createDataFrame([(1, "hello"), (2, "world")], ["id", "word"])
df.show()
spark.stop()
