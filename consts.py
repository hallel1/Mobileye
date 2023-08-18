from parser_files import read_vehicle_status, read_objects_detection_events
from sqlite_manager import SQLiteManager
CREATE TABLE IF NOT EXISTS detection_data (
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
INSERT INTO detection_data (vehicle_id, detection_time, object_type, object_value)
VALUES (?, ?, ?, ?)
'''

CREATE_VEHICLE_STATUS_TABLE = '''
CREATE TABLE IF NOT EXISTS vehicle_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id TEXT NOT NULL,
    report_time TEXT NOT NULL,
    status TEXT NOT NULL
);
'''

INSERT_VEHICLE_STATUS = '''
INSERT INTO vehicle_status (vehicle_id, report_time, status) VALUES (?, ?, ?);
'''
SPARK_APP_NAME = "JSONtoSQLite"
JDBC_FORMAT = 'jdbc'
JDBC_URL = 'jdbc:sqlite:/path/to/your/sqlite.db'
JDBC_DRIVER = 'org.sqlite.JDBC'
JDBC_DBTABLE = 'detection_data'

data = """{
  "objects_detection_events": [
    {
      "vehicle_id": "ebab5f787798416fb2b8afc1340d7a4e",
      "detection_time": "2022-06-05T21:02:34.546Z",

FUNCTIONS_MAP = {
    "objects_detection": read_objects_detection_events,
    "vehicle_status": read_vehicle_status,
}