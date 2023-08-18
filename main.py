import time

import pyspark.sql.functions as F
from pyspark import SparkConf
from pyspark.sql import SparkSession
from watchdog.observers import Observer

import consts
from spark_config import set_spark_config
from handler_watcher import HandlerWatcher
import queue


def main():
    set_spark_config()
    conf = SparkConf().setAppName(consts.SPARK_APP_NAME)
    spark = SparkSession.builder.config(conf=conf).getOrCreate()

    watcher(spark)
    spark.stop()


def watcher(spark):
    file_queue = queue.Queue()
    observer = Observer()
    event_handler = HandlerWatcher(file_queue)
    event_handler.set_spark(spark)
    observer.schedule(event_handler, consts.DIRECTORY_TO_WATCH, recursive=True)
    observer.start()
    try:
        while True:
            if not file_queue.empty():
                file_path = file_queue.get()
                identifier_file(file_path)
            else:
                time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
        print("Observer Stopped")
    observer.join()


def identifier_file(file_path):


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
