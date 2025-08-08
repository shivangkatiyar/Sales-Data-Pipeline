import os

os.environ["HADOOP_HOME"] = "C:\\Hadoop"

import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from src.main.utility.logging_config import *

def spark_session():
    spark = SparkSession.builder.master("local[*]") \
        .appName("spark_project")\
        .config("spark.driver.extraClassPath", "C:\\my_sql_jar\\mysql-connector-java-8.0.26\\mysql-connector-java-8.0.26.jar") \
        .getOrCreate()
    logger.info("spark session %s",spark)
    return spark

# .config("spark.hadoop.hadoop.native.lib", "false") \
# .config("spark.hadoop.io.native.lib.available", "false") \


# from pyspark.sql import SparkSession
#
# spark = SparkSession.builder \
#     .appName("Test Write") \
#     .getOrCreate()
#
# df = spark.range(1, 10)
#
# df.write.mode("overwrite").parquet("output_test")







