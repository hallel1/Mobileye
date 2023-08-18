from parser_files import parser_vehicle_status, parser_objects_detection_events
from sqlite_manager import SQLiteManager
SPARK_APP_NAME = "JSONtoSQLite"
DIRECTORY_TO_WATCH = "./data"

# File Paths
JSON_FILE = 'input.json'
DATABASE_FILE = 'detections.db'

# SQL Statements
CREATE_OBJECT_DETECTION_TABLE = '''
CREATE TABLE IF NOT EXISTS object_detection (
    detection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id TEXT NOT NULL,
    detection_time TEXT NOT NULL,
    object_type TEXT NOT NULL,
    object_value INTEGER NOT NULL
)
'''

INSERT_DETECTION_DATA = '''
INSERT INTO object_detection (vehicle_id, detection_time, object_type, object_value)
VALUES (?, ?, ?, ?)
'''

CREATE_VEHICLE_STATUS_TABLE = '''
CREATE TABLE IF NOT EXISTS vehicle_status (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id TEXT NOT NULL,
    report_time TEXT NOT NULL,
    status TEXT NOT NULL
);
'''

INSERT_VEHICLE_STATUS = '''
INSERT INTO vehicle_status (vehicle_id, report_time, status) VALUES (?, ?, ?);
'''

SQLITE_TABLES = [CREATE_OBJECT_DETECTION_TABLE, CREATE_VEHICLE_STATUS_TABLE]

# JDBC settings
JDBC_FORMAT = 'jdbc'
JDBC_URL = 'jdbc:sqlite:/path/to/your/sqlite.db'
JDBC_DRIVER = 'org.sqlite.JDBC'
JDBC_DBTABLE = 'detection_data'


PARSER_FILE = 0
INSERT_TO_DB = 1
