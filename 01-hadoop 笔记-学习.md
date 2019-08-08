## hadoop 笔记-学习



```
missing blocks The following files may be corrupted

1 检查文件缺失情况
hadoop fsck /user/hive/warehouse | grep parquet

2 删除缺失文件
hadoop fsck -delete  /user/hive/warehouse/mid_table/part-00000-2434bd33-8a21-4249-9c0c-17e0f4ba397b-c000.snappy.parquet 

```



### HDFS架构

1 Master(NameNode / NN)  带 N个SLaves(DataNode / DN)

HDFS/YARN/HBase  都使用同样的架构方式



1个文件会被拆分成多个Block

block size: 128M

130M  ==> 2个Block: 128M 和 2M



**NN**：

1）负责客户端请求的响应

2）负责元数据(文件的名称、副本系数、Block存放的DN位置) 的管理

3）记录文件的修改记录



**DN**：

1）存储用户的文件对应的数据块（Block）

2) 要定期向NN发送心跳信息，汇报本身及其所有的block 信息，健康状况

Ss

**生产部署**

Namenode + N 个datanode

建议：NN 和 DN 是部署在不同的节点上s

### HDFS副本机制

副本系数、副本因子

block replication（文件名, 块数量， 块的id ）

```
hadoop fs -setrep -R //修改备份文件数
hadoop fs -setrep -R 3 /jars
```



### Hadoop 环境安装

1)、安装JDK，配置安装目录到系统环境变量(~/.bash_profile)中

​	export JAVA_HOME=java的安装目录

​        Export PATH=$JAVA_HOME/bin:$PATH

2)、机器参数设置

​         设置机器名称：hosename, /etc/sysconfig/network

​         设置hostname 与 ip 的映射关系 ， /etc/hosts

​         设置ssh 免密登录（可以省略，但是重启hadoop进程的是你，需要手动输入密码）

3)、hadoop配置修改

​       hdfs-site.xml  core-site.xml,  hadoop-env.sh, yarn-site.xml



4)、**格式化HDFS** 

注意：这一步操作，只是在第一次启动时执行，如果每次启动都格式化的化，会导致HDFS上的数据被清空

```
hdfs namenode -format
```

5)、 **启动 HDFS **

```
srart-dfs.sh
```

验证是否启动成功：

```
命令行：jps
NameNode
DataNode

浏览器：http://hadoop主机名:50070
```

7)、**关闭 HDFS**

```
./stop-dfs.sh
```



**HDFS shell 常用命令**

- ls
- get
- mkdir
- rm
- put

**HDFS 优点**

- 高容错
- 适合批处理
- 适合大数据
- 构建中廉价的机器上

**HDFS 缺点**

- 低延迟的数据访问
- 小文件存储

### MapReduce

**特点**

- 易于编程
- 良好的扩张性
- 高容错性
- 海量数据的离线处理

不擅长

- 实时计算
- 流式计算
- DAG计算（作业流图）



**MapReduce 编程模型**

- input
- map & reduce
- output

### yarn 资源调度框架

MapReduce1.x 存在的问题

jobTracker 负责资源调度 和 任务调度，

taskTracker 负责干活

- 资源利用率 & 运维成本 & 多套集群
- jobTracker 太忙碌

YARN

- 基于资源配置，多种组件使用 调度，共享资源

**YARN 架构**

1 RM(ResourceManager) + N NM(NodeManager)

**ResourceManager的职责**： 一个集群active状态的RM 只有一个, 负责整个集群的资源管理和调度

1) 处理客户端的请求(启动/杀死任务)

2) 启动/监控 ApplicationMater(一个作业对应一个AM)

3) 监控NM

4) 系统的资源分配和调度



**NodeManager** 职责：整个集群中有N个， 负责单个节点的资源管理和使用以及task的运行情况

1) 定期向RM汇报本节点的资源使用情况 和 各个Container的运行状态

2) 接收并处理RM 的container 启动/停止的各种命令

3) 单个节点的资源管理和任务管理



**ApplicationMater** 职责：每个应用/作业对应一个，负责应用程序的管理

1)  数据切分

2) 为应用程序向RM申请资源( container), 并分配给内部任务ß

3) 与NM通信以启动/停止task, task 是运行在container中的

4) task 的监控和容错



**Container**

 对任务运行情况的描述：CPU、memory、环境变量



**YARN 执行流程**

1)  用户向YARN 提交作业

2) RM 为该作业分配一个container(AM)

3) RM 会与对应的NM通信, 要求NM 在这个container上启动应用程序的AM

4) AM首先向RM 注册，然后AM将为各个任务申请资源，并监控运行情况

5) AM采用轮询的方式通过RPC协议向RM申请和领取资源

6) AM申请到资源后，便和相应的NM通信，要求NM启动任务

7) NM启动我们作业对应的task



**yarn 配置**

- mapred-site.xml
- Yarn-site.xml

yarn 启动/停止

```
start-yarn.sh
stop-yarn.sh
```

```
jps
ResourceManager
NodeManager

```



提交一个RM作业到yarn

```
hadoop jar mapred的作业程序的jar包 参数
```



### Hive

背景：

- MapReduce 编程的不便利性
- HDFS上文件缺失 Schema

**Hive是什么**

解决海量结构化的日志数据统计问题

构建在hadoop 上的数据仓库

hive定义了一种类SQL 查询语句:HQL

通常用于进行离线数据处理

底层支持多种底层执行引擎（MapReduce, Tez, Spark）

支持多种压缩格式 ( GZIP, LZO, Snappy, BZIP2)

存储格式（TextFile、SequenceFile、RCFile、ORC、Parquet）

UDF: 自定义函数

**为啥使用hive**

- 简单、容易上手(提供了 类似SQL查询语言HQL)
- 为超大数据集设计的计算/存储扩展能力(MR 计算, HDFS 存储)
- 统一的元数据管理(可与Presto/ Impala/ SparkSQL等共享数据)

**hive 基础使用**

创建表：

```
CREATE TABLE table_name
     [(col_name data_type [COMMENT col_comment])]
     
create table hive_wordcount(context string);
```

加载数据到hive

```
LOAD DATA LOCAL INPATH 'filepath' INTO TABLE tablename

load data local inpath '/home/dara/hello.text' into table hive_wordcount
```

查询语句

```
select word, count(1) from hive_wordcount lateral view explode(split(context, '\t')) wc as word group by word;
```

lateral view explode(): 是把每行记录按照指定分隔符进行拆解

Hive sql 提交执行以后会生成MR 作业，在yarn 上运行



### Spark

spark 分布式计算框架

- 速度快「执行、开发快」（基于内存、DAG执行引擎（数据流处理））
- 易用性（多种语言支持，大量类库支持）
- 通用的 （sql、streaming、 complex、 analytics ）
- 运行在更多的组件

**MapReduce 的局限性**

 代码繁琐、只能支持 map 和 reduce  方法、

 执行效率低下、不适合（迭代多次，交互式，流式的处理）

**框架多样化, 均可使用 spark完成**

1) 批处理(离线): MapReduce、Hive、Pig

2）流式处理(实时)：Storm、Jstorm

3)  交互式计算 : Impala



Hbase : 构建在HDFS上的列式数据库

BDAS：Berkeley  Data  Analytics Stack. (伯克利 数据) 

**Spark Standalone 部署**

Spark Standalone 模式的架构和 Hadoop HDFS/YARN很类似

1 master + n worker



spark-env.sh

```
SPARK_MASTER_HOME=hadoop001

SPARK_WORKER_CORES=2

SPARK_WORKER_MEMORY=2g

# 配置 节点数

SPARK_WORKER_INSTANCES=1

```



 ### Spark Sql

**Hive:** 类似于 SQL的Hive QL 语言， sql ==>mapreduce

​           特点：mapreduce

​           改进：hive on tez、hive on spark、hive on mapreduce

**Spark**:  hive on spark ==> shark(hive on spark)

​            Shark 推出：基于spark 基于内存的列式存储、与hive能够兼容

​           缺点：hive ql 的解析、逻辑执行计划生成、执行计划的优化是依赖hive的，

​                        仅仅只是将物理执行计划从 mr作业替换成 spark 作业

**shark终止后，产生啦2个分支**：

1）hive on spark

​           hive 社区，源码在Hive 中

2）Spark SQL

​           Spark社区，源码是在spark中

​           支持多种数据源，多种优化技术、扩展性好很多

**SQL on Hadoop**    

1) Hive [facebook]

​	sql ==> mapreduce

​	metastore : 元数据

​	sql : database、table、view

​	

2) impala [cloudera]

​	cdh (建议生产环境使用)、cm

​	sql:  自己的守护进程执行的，非mr

​        metastore

3) presto

​      Facebook、京东 都在使用

​      sql

4) drill

​	sql

​	访问：hdfs、rdbms、json、hbase、mangodb、s3、hive

5) Spark SQL

​	sql

​	dataframe/dataset api

​	metastore

​	访问：hdfs、rdbms、json、hbase、mangodb、s3、hive  ==> 外部数据源	

Spark sql 小节：

1）Spark Sql 的应用并不局限于SQL

2) 访问hive、josn、parquet等文件的数据；

3）sql 只是 Spark SQL 的一个功能而已



![image-20190306124650929](/Users/weicheng/Library/Application Support/typora-user-images/image-20190306124650929.png)



### 从Hive 平滑过渡到spark



**提交Spark程序**

```
./bin/spark-submit \
  --class <main-class> \
  --master <master-url> \
  --deploy-mode <deploy-mode> \
  --conf <key>=<value> \
  ... # other options
  <application-jar> \
  [application-arguments]
```

sqlContext(1.x)

```
val sc: SparkContext
val sqlContext = new org.apache.spark.sql.SQLContext(sc)
```



hiveContext

```
val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)
```



SparkSession(2.x)

```
val spark = SparkSession
.builder()
.appName("Spark SQL basic example")
.config("spark.some.config.option", "some-value")
.getOrCreate()
```



在spark sql 中使用hive

- 将 hive-site.xml 传入 spark的conf 文件夹中，为了将hive的配置信息载入到spark中

- 将mysql 的包倒入spark 的lib文件夹中， 或者通过 --jars 将驱动传入过去
- 使用spark-sql 或者spark-shell 访问hive 数据 

查看 SparkSql 执行计划

- 查看物理执行计划

```
create table t (key string, value string);
explain select * from t a join t b on a.key = b.key and a.key > 3;
```

```
== Physical Plan ==
*SortMergeJoin [key#37], [key#39], Inner
:- *Sort [key#37 ASC], false, 0
:  +- Exchange hashpartitioning(key#37, 200)
:     +- *Filter (isnotnull(key#37) && (cast(key#37 as double) > 3.0))
:        +- HiveTableScan [key#37, value#38], MetastoreRelation userdb, t, a
+- *Sort [key#39 ASC], false, 0
   +- Exchange hashpartitioning(key#39, 200)
      +- *Filter ((cast(key#39 as double) > 3.0) && isnotnull(key#39))
         +- HiveTableScan [key#39, value#40], MetastoreRelation userdb, t, b
Time taken: 0.205 seconds, Fetched 1 row(s)
19/03/07 10:07:07 INFO CliDriver: Time taken: 0.205 seconds, Fetched 1 row(s)
```

----------

```
explain select a.key * (2+3), b.value from t a join t b on a.key = b.key and a.key > 3;

```

```
== Physical Plan ==
*Project [(cast(key#44 as double) * 5.0) AS (CAST(key AS DOUBLE) * CAST((2 + 3) AS DOUBLE))#48, value#47]
+- *SortMergeJoin [key#44], [key#46], Inner
   :- *Sort [key#44 ASC], false, 0
   :  +- Exchange hashpartitioning(key#44, 200)
   :     +- *Filter (isnotnull(key#44) && (cast(key#44 as double) > 3.0))
   :        +- HiveTableScan [key#44], MetastoreRelation userdb, t, a
   +- *Sort [key#46 ASC], false, 0
      +- Exchange hashpartitioning(key#46, 200)
         +- *Filter ((cast(key#46 as double) > 3.0) && isnotnull(key#46))
            +- HiveTableScan [key#46, value#47], MetastoreRelation userdb, t, b
Time taken: 0.296 seconds, Fetched 1 row(s)
```

- 查看详细的执行计划

```
explain extended select a.key * (2+3), b.value from t a join t b on a.key = b.key and a.key > 3;
```

```
# 解析的逻辑计划
== Parsed Logical Plan ==
'Project [unresolvedalias(('a.key * (2 + 3)), None), 'b.value]
+- 'Join Inner, (('a.key = 'b.key) && ('a.key > 3))
   :- 'UnresolvedRelation `t`, a
   +- 'UnresolvedRelation `t`, b

# 分析逻辑计划
== Analyzed Logical Plan ==
org.apache.spark.sql.AnalysisException: Table or view not found: t; line 1 pos 52
org.apache.spark.sql.AnalysisException: Table or view not found: t; line 1 pos 52

# 优化的逻辑计划
== Optimized Logical Plan ==
org.apache.spark.sql.AnalysisException: Table or view not found: t; line 1 pos 52

# 物理计划
== Physical Plan ==
org.apache.spark.sql.AnalysisException: Table or view not found: t; line 1 pos 52
Time taken: 4.346 seconds, Fetched 1 row(s)


```

  

#### thriftserver/beeline的使用

- 启动thriftserver
- 通过beeline 连接到thriftserver

```
thriftserver/beeline的使用
1) 启动thriftserver: 默认端口是10000, 可以修改
2）启动beeline
beeline -u jdbc:hive2://localhost:10000 -n hadoop

修改thriftserver启动占用的默认端口号
./start-thriftserver.sh \
--master local[2] \
--jars ~/software/mysql-connector-java-5.1.27-bin.jar \
--hiveconf hive.server2.thrift.port=14000

beeline -u jdbc:hive2://localhost:14000 -n hadoop

```

thriftserver和普通的spark-shell/spark-sql有啥区别

-  Spark-shell、spark-sql都是一个spark application
- thriftserver, 不管你启动多少客户端(beeline/code), 永远都是一个spark application ，解决了数据共享问题，多个客户端可以共享数据。



#### jdbc方式编程访问

- Maven 添加依赖：org.spark-project.hive#hive-jdbc
- 开发代码访问thriftserver



#### DataFrame 和 DataSet

Dataset 分布式的数据集

DataFrame, 以列(列名， 类型， 值)的形式构成的分布式数据集，按照列赋予不同的名称。可以理解为一张表。



#### DataFrame 和 RDD

RDD :

​	java/scala ==> jvm

​        Python ==> python runtime



DataFrame:

​	java/scala/python ==> logic plan(执行计划)

RDD的各种语言编写程序 性能会与语言有关 与 DataFrame 的各种语言的程序，性能之间没有差异

![image-20190310161312984](/Users/weicheng/Library/Application Support/typora-user-images/image-20190310161312984.png)



#### DataFrame 和 RDD 的互操作

- 通过反射的方式进行【case class 前提：事先需要知道 字段、字段类型】

![image-20190310162420442](/Users/weicheng/Library/Application Support/typora-user-images/image-20190310162420442.png)

1、创建 case class.

2、读取RDD，将RDD 数据分开，new 成 case class 对象，

3、倒入隐式转换类。 import spark.implicits._

4、使用toDF() 转换为 DF 对象



- 通过编程的方式进行转换【Row  事先不知道列的情况下，使用】

![image-20190310163503978](/Users/weicheng/Library/Application Support/typora-user-images/image-20190310163503978.png)

1、创建RDD

2、创建schema, 使用StructType

3、使用 SparkSession的createDataFrame创建一个DF，将 RDD, schema 作为参数



#### DataFrame 和 Dataset 的互操作



#### External data 

用户:

​	方便快速从不同的数据源（json、parquet、rdbms），经过混合处理（json、join parquet）,

​        再将处理结果以特定的格式 (json、parquet) 写回到指定的系统 (HDFS、S3) 上去

外部数据源的目的

1）开发人员：是否需要将代码合并到spark中？

​      weibo

​      --jars

2) 用户：

​	读：spark.read.format(format)

​			format

​				build-in: json parquet jdbc csv

​	people.write.format("parquet").save("path")



**操作Parquet文件**

```
spark.read.format("parquet").load(path)
df.write.format("parquet").save(path)
```

spark.sql.parquet 模块 默认处理数据源为。parquet

使用spark-sql 处理parquet

```
CREATE TEMPORARY VIEW parquetTable
USING org.apache.spark.sql.parquet
OPTIONS (
  path "examples/path/people.parquet"
)

SELECT * FROM parquetTable
```



**操作hive 数据**

```
// 读取数据
spark.table(tableName)
// 写保存数据
df.write.saveAsTable(tableName)

// 设置 spark shuffle 分区数, spark.sql.shuffle.partitions 默认为200
spark.sqlContext.setConf("spark.sql.shuffle.partitions", "10")

// 生产环境中注意设置 spark.sql.shuffle.partitions, 能够提升计算速度
```



操作Mysql 数据库[关系型数据库都相似]

```
// 读取数据
spark.read.format("jdbc").options( Map("url" -> 
"jdbc:mysql://localhost:3306/hive?user=root&password=root",
"dbtable" -> "TBLS", "driver" ->
"com.mysql.jdbc.Driver")).load()
```



操作 MySql 与 Hive 综合操作

```
// 使用外部数据源综合查询hive 与 mysql 的数据
// 读取 hive 中的一个表，
// 读取 mysql 中的一个表
// 组合 join 进行查询
```







#### Spark核心概念

1. driver program (驱动器程序, 发起集群上的各种并行操作)
   1. 通过一个SparkCountext对象来访问 Spark,  这个对象代表了对计算集群的一个连接，可以创建RDD 
   2. 管理多个执行器 (executor) 节点。



#### RDD 基础

弹性分布式数据集(RDD), 代表分布在集群中多台机器上的对象集合。

支持的类型操作：

- 转化操作 (由一个RDD 生成一个新的RDD)
- 活动操作 ( 对RDD 计算出一个结果，将结果存储到外部存储系统，或者返回给驱动器程序)

转化函数的返回值类型是RDD，行动操作返回的是其他的数据类型

Spark 使用谱系图来计算每个RDD. 依靠谱系图在持久化的RDD丢失部分数据时恢复丢失数据。

RDD的一些行动操作会以普通集合或者值的形式将RDD的的部分或结果返回到驱动器程序中



**Spark 程序或shell 会话工作方式**

1）从外部数据创建出输入RDD 

2) 使用诸如filter()这样的转化操作对RDD进行转化，以定义新的RDD

3) 告诉Spark对需要被重用的中间结果RDD执行persist() 操作。

4）使用行动操作 来触发一次并行计算，spark引擎优化后再执行



```
// 创建 RDD
// 在驱动器程序中对一个集合进行并行化
val lines = sc.parallelize(List("pandas", "i like pandas"))
// 读取外部数据集
val lines = sc.textFile("/path/to/README.md")

// 转化操作
val inputRDD = sc.textFile("log.txt")
val errorsRDD = inputRDD.filter(line => line.contains("error"))

// 行动操作对错误进行计数
println("Input had" + badLinesRDD.count() + " concerning lines" )
println("Here are 10 examples:")
badlinesRDD.take(10).foreach(println)

// 每个输入对应一个输出元素
// 计算RDD中各值的平方,
val input = sc.parallelize(List(1, 2, 3, 4))
val result = input.map(x => x * x)
println(result.collect().mkString(","))

// 每个输入元素生成多个输出元素
val lines = sc.parallelize(List("hello world", "hi"))
val words = lines.flatMap(line => line.split(" "))
words.first()

// union(other) 返回一个包含两个RDD中所有元素的RDD，包含重复数据
// intersection(other) 返回两个RDD中都有的元素，去掉重复元素。需要通过网络混洗数据来发现共有元素
// subtract(other) 返回只存在第一个RDD中，不存在第二个RDD中的RDD
// cartesian(other) 返回所有可能的(a, b)对，笛卡尔积

// aggregate(other) 计算RDD的平均值
// takeSample(withReplacement, num, seed) 从数据中获取一个采样

// collect() 将整个RDD中的内容返回驱动器程序中

// 持久化(缓存)
val result = input.map(x => x * x)
result.persist(StorageLevel.DISK_ONLY)
println(result.count())
println(result.collect().mkString(","))
```

![image-20190320205547213](/Users/weicheng/Library/Application Support/typora-user-images/image-20190320205547213.png)

使用隐式转换

```
import org.apache.spark.SparkContext._
```



#### 键值对操作

pari RDD 

- reduceByKey() 可以分别规约每个健对应的数据
- join() 将两个RDD中键相同的元素组合到一起，合并为一个RDD

```
// 对第二个元素进行筛选
pairs.filter{case (key, value) => value.length < 20}

// 使用reduceByKey() 和 mapValues()计算每个键对应的平均值
rdd.mapValues(x => (x, 1)).reduceByKey((x, y) => (x._1 + y._1, x._2 + y._2))

// 并行度
val data = Seq(("a", 3), ("b", 4), ("a", 1)) 
sc.parallelize(data).reduceByKey((x, y) => x + y) // 默认并行度 sc.parallelize(data).reduceByKey((x, y) => x + y, 10) // 自定义并行度

// 数据分组
// groupByKey() 对数据进行分组，返回一个 [k, Iterable[V]]
// rdd.reduceByKey(func) 与 rdd.groupByKey().mapValues(value => value.reduce(func))等价


```



**并行度调优 **

每个RDD都有固定数目的分区，分区数 决定了在RDD上执行操作时的并行度。



数据分组





 	 	