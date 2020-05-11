from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import time

if __name__ == "__main__":
    # list of datasets
    testFiles = ["T10I2D100K", "T10I4D100K", "T20I2D100K", "T20I4D100K", "T20I6D100K"]
    # list of support value
    support = [0.004, 0.006, 0.008]

    sc = SparkContext(appName="Spark Apriori")
    spark = SparkSession(sc)
    schema = StructType([
        StructField("algorithm", StringType(), False),
        StructField("datasets", StringType(), False),
        StructField("support", FloatType(), False)
    ])
    for i in range(5):
        schema.add("test{}".format(i+1), FloatType(), True)
    experiments = []

    for f in testFiles:
        for s in support:
            times = []
            for i in range(5):
                start = time.time()
                apriori(sc, "./data/{}.data".format(f), "./result/{}{}{}".format(f, s, i+1), s)
                end = time.time()
                times.append(end - start)
            experiments.append(["Apriori", f, s] + times)
        df = spark.createDataFrame(experiments, schema)
        df.coalesce(1).write.mode("overwrite").csv("./experiments/runtime{}".format(f))
        experiments = []
    sc.stop()