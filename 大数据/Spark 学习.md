# Spark 学习



单词部分：

```
# hadoop 常用数据格式
Apache Avro
Apache Parquet

# NoSQL 数据库
Apache Hbase
Apache Cassandra

# 流式处理组件
Apache Flume
Apache Kafka

# sql 库
sparkSQL
Apache Hive

estimator 评估器
transformer 转换器

```





Apache Cassandra



## Spark 核心概念简介



每个Spark 应用都由一个驱动器程序( **driver program** ) 来发起集群上的各种并行操作，驱动器程序包含应用的 main 函数，并且定义了集群上的分布式数据集，还对这 些分布式数据集应用了相关操作。 

驱动器程序通过一个 **SparkContext** 对象来访问 Spark。这个对象代表对计算集群的一个连接，一旦有了 **SparkContext**，你就可以用它来创建 **RDD**。 

驱动器程序一般要管理多个执行器(**executor**)节点。比如，如果我们在 集群上运行 count() 操作，那么不同的节点会统计文件的不同部分的行数。 



 Spark 引擎可以执行更通用的有向无环图（DAG）算子。意味者在MapReduce 中需要将中间结果写入分布式系统时，Spark 能将中间结果直接传到流水作业线的下一步



#### Spark-shell

sc 是 SparkContext 的一个引用

spark是 sparkSession  对象， sparkSession 是 SparkContext对象的一个封装

sc.[\t]  显示 sc 对象的方法列表



















