import json


def parse_json_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
