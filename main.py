import pyspark.sql.functions as F
from pyspark import SparkConf
from pyspark.sql import SparkSession

import consts
from spark_config import set_spark_config


def main():
    set_spark_config()
    conf = SparkConf().setAppName(consts.SPARK_APP_NAME)
    spark = SparkSession.builder.config(conf=conf).getOrCreate()
    df = spark.read.json(spark.sparkContext.parallelize([consts.data]))


def read_objects_detection_events(df):
    df_exploded = df.select(F.explode("objects_detection_events").alias("events"))

    df_detections = df_exploded \
        .select("events.vehicle_id", "events.detection_time",
                F.explode("events.detections").alias("detection")) \
        .select("vehicle_id",
                "detection_time",
                "detection.object_type",
                "detection.object_value")

    return df_detections


def read_vehicle_status(df):
    df_exploded = df.select(F.explode("vehicle_status").alias("vehicle_status"))

    df_detections = df_exploded \
        .select("vehicle_status.vehicle_id",
                "vehicle_status.report_time",
                "vehicle_status.status")

    return df_detections


if __name__ == "__main__":
    main()
