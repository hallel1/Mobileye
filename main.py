from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext

import consts

import os

os.environ["PYSPARK_PYTHON"] = "C:\\Python310\\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = "C:\\Python310\\python.exe"
os.environ["SPARK_HOME"] = "C:\\spark\\spark-3.4.1-bin-hadoop3"


def main():
    conf = SparkConf().setAppName(consts.SPARK_APP_NAME)
    spark = SparkSession.builder.config(conf=conf).getOrCreate()

    spark.stop()


if __name__ == "__main__":
    main()
