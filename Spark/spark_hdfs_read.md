


SPARK CODE :

#### Code to read a file from hdfs in Spark

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext

sparkSession = SparkSession.builder.appName("example-pyspark-read-and-write").getOrCreate()
df_load = sparkSession.read.csv("hdfs://localhost:54310/hdfs/demolarge4.csv")

df_load.show()


#### Code to read a file from remote hdfs in Spark

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext

sparkSession = SparkSession.builder.appName("example-pyspark-read-and-write").getOrCreate()
df_load = sparkSession.read.csv("hdfs://172.17.2.175:54310/hdfs/demolarge4.csv")
df_load.show()


APACHE-DRILL:

#### Query to get a data from hdfs

select * from dfs.`demo/demolarge4.csv` limit 10;


STORAGE PLUGIN FOR REMOTE HDFS FILE ACCCESS :
{
  
...
  
"connection": "hdfs://172.17.2.175:54310/"

...


STORAGE PLUGIN FOR REMOTE HDFS FILE ACCCESS :

...
  
"connection": "hdfs://localhost:54310/"

...

  




