from pyspark.sql import SparkSession

import consts


def main():
    spark = SparkSession.builder.appName(consts.SPARK_APP_NAME).getOrCreate()

    spark.stop()


if __name__ == "__main__":
    main()
