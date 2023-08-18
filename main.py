import queue
import time

from pyspark import SparkConf
from pyspark.sql import SparkSession
from watchdog.observers import Observer

import consts
from handler_watcher import HandlerWatcher
from parser_files import parser_vehicle_status, parser_objects_detection_events
from spark_config import set_spark_config
from sqlite_manager import SQLiteManager
from utils import identifier_file, create_dataframe_from_json, read_file


def main():
    set_spark_config()
    conf = SparkConf().setAppName(consts.SPARK_APP_NAME)
    spark = SparkSession.builder.config(conf=conf).getOrCreate()
    sqLite = SQLiteManager()
    file_queue, observer = watcher_setting(spark)
    watcher_files(spark, file_queue, observer, sqLite)

    spark.stop()


def watcher_setting(spark):
    file_queue = queue.Queue()
    event_handler = HandlerWatcher(file_queue)
    event_handler.set_spark(spark)

    observer = Observer()
    observer.schedule(event_handler, consts.DIRECTORY_TO_WATCH, recursive=True)
    observer.start()
    return file_queue, observer


def watcher_files(spark, file_queue, observer, sqLite):
    try:
        while True:
            if not file_queue.empty():
                print("Identifier new file.")
                file_path = file_queue.get()
                run_new_file_process(spark, file_path, sqLite)
            else:
                time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Observer Stopped")
    except Exception as e:
        print(e)
        watcher_files(spark, file_queue, observer, sqLite)
    observer.join()


def run_new_file_process(spark, file_path, sqLite):
    functions_map = {
        "objects_detection": [parser_objects_detection_events, sqLite.insert_detection_objects],
        "vehicle_status": [parser_vehicle_status, sqLite.insert_detection_data],
    }
    data = read_file(file_path)
    raw_df = create_dataframe_from_json(spark, data)
    functions_array = identifier_file(file_path, functions_map)
    df = parser_file(functions_array, raw_df)
    insert_to_db(functions_array, df)


def parser_file(functions_array, raw_df):
    return functions_array[consts.PARSER_FILE](raw_df)


def insert_to_db(functions_array, df):
    rows = [list(row) for row in df.collect()]
    for row in rows:
        functions_array[consts.INSERT_TO_DB](*row)


if __name__ == "__main__":
    main()
