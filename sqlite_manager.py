import sqlite3
from consts import *


class SQLiteManager:
    def __init__(self):
        self.db_connection = sqlite3.connect(DATABASE_FILE)
        self.cursor = self.db_connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(CREATE_DETECTION_DATA_TABLE)
        self.db_connection.commit()

    def insert_detection_data(self, vehicle_id, detection_time, object_type, object_value):
        self.cursor.execute(INSERT_DETECTION_DATA, (vehicle_id, detection_time, object_type, object_value))

    def close(self):
        self.db_connection.commit()
        self.db_connection.close()

    def sqlite_write(self, df):
        df.write.format(JDBC_FORMAT).options(
            url=JDBC_URL,
            driver=JDBC_DRIVER,
            dbtable=JDBC_DBTABLE
        ).mode('append').save()
