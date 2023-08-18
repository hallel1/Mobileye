import queue
import time

from pyspark import SparkConf
from pyspark.sql import SparkSession
from watchdog.observers import Observer

import consts
from handler_watcher import HandlerWatcher
from spark_config import set_spark_config
from utils import identifier_file, create_dataframe_from_json, read_file


def main():
    set_spark_config()
    conf = SparkConf().setAppName(consts.SPARK_APP_NAME)
    spark = SparkSession.builder.config(conf=conf).getOrCreate()

    watcher_files(spark)

    spark.stop()


def watcher_files(spark):
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
                data = read_file(file_path)
                raw_df = create_dataframe_from_json(spark, data)
                df = identifier_file(file_path, raw_df)
                df.printSchema()
            else:
                time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Observer Stopped")
    except Exception as e:
        print(e)
    observer.join()


if __name__ == "__main__":
    main()
