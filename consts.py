CREATE_DETECTION_DATA_TABLE = '''
CREATE TABLE IF NOT EXISTS detection_data (
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