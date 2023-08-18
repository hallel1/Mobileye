import sqlite3
import consts


class SQLiteManager:
    def __init__(self):
        self.db_connection = sqlite3.connect(consts.DATABASE_FILE)
        self.cursor = self.db_connection.cursor()
        self.create_tables()

    def create_tables(self):
        for table in consts.SQLITE_TABLES:
            self.cursor.execute(table)
            self.db_connection.commit()

    def insert_detection_objects(self, vehicle_id, detection_time, object_type, object_value):
        self.cursor.execute(consts.INSERT_DETECTION_DATA, (vehicle_id, detection_time, object_type, object_value))
        print("inserted")
    def insert_detection_data(self, vehicle_id, report_time, status):
        self.cursor.execute(consts.INSERT_VEHICLE_STATUS, (vehicle_id, report_time, status))

    def close(self):
        self.db_connection.commit()
        self.db_connection.close()

    def sqlite_write(self, df):
        df.write.format(consts.JDBC_FORMAT).options(
            url=consts.JDBC_URL,
            driver=consts.JDBC_DRIVER,
            dbtable=consts.JDBC_DBTABLE
        ).mode('append').save()
