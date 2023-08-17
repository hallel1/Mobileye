from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
import pyspark.sql.functions as F

import consts

import os

os.environ["PYSPARK_PYTHON"] = "C:\\Python310\\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = "C:\\Python310\\python.exe"
os.environ["SPARK_HOME"] = "C:\\spark\\spark-3.4.1-bin-hadoop3"


def main():
    conf = SparkConf().setAppName(consts.SPARK_APP_NAME)
    spark = SparkSession.builder.config(conf=conf).getOrCreate()
    df = spark.read.json(spark.sparkContext.parallelize([consts.data]))

    df_exploded = df.select(F.explode("objects_detection_events").alias("events"))

    df_detections = (df_exploded
    .select("events.vehicle_id", "events.detection_time",
            F.explode("events.detections").alias("detection"))
    .select(
        "vehicle_id",
        "detection_time",
        "detection.object_type",
        "detection.object_value"
    ))

    spark.stop()


if __name__ == "__main__":
    main()
