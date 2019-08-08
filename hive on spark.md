hive on spark

1、安装hive

2、安装spark

Spark上的Hive文档提到您需要安装不包含Hive的Spark构建。从Spark 2.0.0开始，此限制不再适用。如果您的Spark构建包含Hive，您可以按照以下步骤操作



```
a.将<SPARK_HOME> / jars下的所有JAR上传到HDFS文件夹，不包括以下（与Hive相关的文件夹）：

hive-beeline
hive-cli
hive-exec
hive-jdbc
hive-metastore
spark-hive-thriftserver
spark-hive
spark-sql

```

```
将spark.yarn.archive设置为指向HDFS文件夹
```

```
设置spark.master = yarn和spark.submit.deployMode = cluster。
```



