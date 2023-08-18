import consts
from json_parser import parse_json_file


def read_file(file_path):
    return parse_json_file(file_path)


def create_dataframe_from_json(spark, data):
    return spark.read.json(spark.sparkContext.parallelize([data]))


def identifier_file(file_path, function_map):
    for file_type, functions_array in function_map.items():
        if file_type in file_path:
            return functions_array
    raise Exception("Invalid file name.")