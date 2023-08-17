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

data = """{
  "objects_detection_events": [
    {
      "vehicle_id": "ebab5f787798416fb2b8afc1340d7a4e",
      "detection_time": "2022-06-05T21:02:34.546Z",
      "detections": [
        {
          "object_type": "pedestrians",
          "object_value": 3
        },
        {
          "object_type": "cars",
          "object_value": 2
        },
        {
          "object_type": "signs",
          "object_value": 3
        }
      ]
    },
    {
      "vehicle_id": "ebab5f787798416fb2b8afc1340d7a4e",
      "detection_time": "2022-06-05T21:05:20.590Z",
      "detections": [
        {
          "object_type": "cars",
          "object_value": 4
        }
      ]
    },
    {
      "vehicle_id": "ebab5f787798416fb2b8afc1340d7a4e",
      "detection_time": "2022-06-05T21:11:35.567Z",
      "detections": [
        {
          "object_type": "trucks",
          "object_value": 5
        },
        {
          "object_type": "obstacles",
          "object_value": 2
        }
      ]
    }
  ]
}"""
