# Distributed-Spark-Apriori
### Usage on NYU Shanghai HPC

```bash
module purge
module load spark
module load java
module load python/gnu/3.7.3

cd src
spark-submit apriori.py
```

Steps on NYU Dumbo are similar


### Reference
https://github.com/apache/spark/pull/2847
https://github.com/tracy-talent/curriculum/blob/master/MapReduce/Apriori/src/distributed/Apiori1.scala
https://github.com/zhang943/Spark-Apriori
https://github.com/Cheng-Lin-Li/Spark