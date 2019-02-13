#### Code to read a file from hdfs in Spark

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext

sparkSession = SparkSession.builder.appName("example-pyspark-read-and-write").getOrCreate()
df_load = sparkSession.read.csv("hdfs://localhost:54310/hdfs/demolarge4.csv")

df_load.show()
