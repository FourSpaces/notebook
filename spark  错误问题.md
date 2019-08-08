## spark  错误问题



------------

RECEIVED SIGNAL TERM

```

```







--------------------

Failing this attempt.Diagnostics: [2019-06-14 13:54:38.048]Container [pid=20225,containerID=container_1560395426252_0278_02_000001] is running 315781120B beyond the 'PHYSICAL' memory limit. Current usage: 2.8 GB of 2.5 GB physical memory used; 4.8 GB of 5.3 GB virtual memory used. Killing container.

Dump of the process-tree for container_1560395426252_0278_02_000001

```
调大执行内存e
```



---------------------------------

java.lang.IllegalArgumentException: Error while instantiating 'org.apache.spark.sql.hive.HiveSessionStateBuilder

```

```



--------------

Job aborted due to stage failure: Aborting TaskSet 4.0 because task 47 (partition 47) cannot run anywhere due to node and executor blacklist.  Blacklisting behavior can be configured via spark.blacklist.*.

```

```





-----------------

spark.sql.parquet.mergeSchema  设置为true 合并原数据



为spark DF 添加空列

```
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
val udf_null = udf((s: Any) => Map("k"->"v").get("l"))
val s = caseClassDS.withColumn("ymd", udf_null(col("name")).cast(IntegerType))
```





----------------------

Spark  GC 问题

java.lang.OutOfMemoryError: GC overhead limit exceeded

```

```





java.lang.OutOfMemoryError: Java heap space



---------------------

When creating a Hive table with Druid storage handler



```
ollection.mutable.ArrayBuffer.foldLeft(ArrayBuffer.scala:48)
	at org.apache.spark.sql.catalyst.rules.RuleExecutor$$anonfun$execute$1.apply(RuleExecutor.scala:82)
	at org.apache.spark.sql.catalyst.rules.RuleExecutor$$anonfun$execute$1.apply(RuleExecutor.scala:74)
```





-------------------

org.apache.spark.sql.AnalysisException: partition column ymd is not defined in table tests.currency_record







------------------------------

java.lang.StackOverflowError

<https://blog.csdn.net/u010936936/article/details/88363449>

```

```

