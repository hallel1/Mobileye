import consts
from json_parser import parse_json_file


def read_file(file_path):
    return parse_json_file(file_path)


def create_dataframe_from_json(spark, data):
    return spark.read.json(spark.sparkContext.parallelize([data]))


def identifier_file(file_path, data):
    for s, func in consts.FUNCTIONS_MAP.items():
        if s in file_path:
            return func(data)
    raise Exception("Invalid file name.")