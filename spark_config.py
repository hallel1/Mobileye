import os


def spark_config():
    os.environ["PYSPARK_PYTHON"] = "C:\\Python310\\python.exe"
    os.environ["PYSPARK_DRIVER_PYTHON"] = "C:\\Python310\\python.exe"
    os.environ["SPARK_HOME"] = "C:\\spark\\spark-3.4.1-bin-hadoop3"
    os.environ["HADOOP_HOME"] = "C:\\hadoop\\hadoopvhadoop-3.3.6-src"
