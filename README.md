# Distributed-Spark-Apriori
### Usage on NYU Shanghai HPC
(Steps on NYU Dumbo are similar)

```bash
module purge
module load spark
module load python/gnu/3.7.3

spark-submit ./src/apriori.py
```


### Credit
https://github.com/zhang943/Spark-Apriori
https://github.com/tracy-talent/curriculum/blob/master/MapReduce/Apriori/src/distributed/Apiori1.scala
https://github.com/apache/spark/pull/2847
https://github.com/Cheng-Lin-Li/Spark