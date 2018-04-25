# Welcome to Spark Python API Docs!

Contents:

- pyspark package
  - [Subpackages](http://spark.apache.org/docs/latest/api/python/pyspark.html#subpackages) 
  - [Contents](http://spark.apache.org/docs/latest/api/python/pyspark.html#module-pyspark)
- pyspark.sql module
  - [Module Context](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#module-pyspark.sql)
  - [pyspark.sql.types module](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#module-pyspark.sql.types)
  - [pyspark.sql.functions module](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#module-pyspark.sql.functions)
  - [pyspark.sql.streaming module](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#module-pyspark.sql.streaming)
- pyspark.streaming module
  - [Module contents](http://spark.apache.org/docs/latest/api/python/pyspark.streaming.html#module-pyspark.streaming)
  - [pyspark.streaming.kafka module](http://spark.apache.org/docs/latest/api/python/pyspark.streaming.html#module-pyspark.streaming.kafka)
  - [pyspark.streaming.kinesis module](http://spark.apache.org/docs/latest/api/python/pyspark.streaming.html#module-pyspark.streaming.kinesis)
  - [pyspark.streaming.flume.module](http://spark.apache.org/docs/latest/api/python/pyspark.streaming.html#module-pyspark.streaming.flume)
- pyspark.ml package
  - [ML Pipeline APIs](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#module-pyspark.ml)
  - [pyspark.ml.param module](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#module-pyspark.ml.param)
  - [pyspark.ml.feature module](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#module-pyspark.ml.feature)
  - [pyspark.ml.classification module](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#module-pyspark.ml.classification)
  - [pyspark.ml.clustering module](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#module-pyspark.ml.clustering)
  - [pyspark.ml.linalg module](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#module-pyspark.ml.linalg)
  - [pyspark.ml.recommendation module](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#module-pyspark.ml.recommendation)
  - [pyspark.ml.regression module](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#module-pyspark.ml.regression)
  - [pyspark.ml.stat module](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#module-pyspark.ml.stat)
  - [pyspark.ml.tuning module](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#module-pyspark.ml.tuning)
  - [pyspark.ml.evaluation module](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#module-pyspark.ml.evaluation)
  - [pyspark.ml.fpm module](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#module-pyspark.ml.fpm)
  - [pyspark.ml.image module](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#module-pyspark.ml.image)
  - [pyspark.ml.util module](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#module-pyspark.ml.util)
- pyspark.mllib package
  - [pyspark.mllib.classification module](http://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#module-pyspark.mllib.classification)
  - [pyspark.mllib.clustering module](http://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#module-pyspark.mllib.clustering)
  - [pyspark.mllib.evaluation module](http://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#module-pyspark.mllib.evaluation)
  - [pyspark.mllib.feature module](http://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#module-pyspark.mllib.feature)
  - [pyspark.mllib.fpm module](http://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#module-pyspark.mllib.fpm)
  - [pyspark.mllib.linalg module](http://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#module-pyspark.mllib.linalg)
  - [pyspark.mllib.linalg.distributed module](http://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#module-pyspark.mllib.linalg.distributed)
  - [pyspark.mllib.random module](http://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#module-pyspark.mllib.random)
  - [pyspark.mllib.recommendation module](http://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#module-pyspark.mllib.recommendation)
  - [pyspark.mllib.regression module](http://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#module-pyspark.mllib.regression)
  - [pyspark.mllib.stat module](http://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#module-pyspark.mllib.stat)
  - [pyspark.mllib.tree module](http://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#module-pyspark.mllib.tree)
  - [pyspark.mllib.util module](http://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#module-pyspark.mllib.util)

## Core classes:

> [`pyspark.SparkContext`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext)
>
> <Spark功能的主要入口点>Main entry point for Spark functionality.
>
> 
>
> [`pyspark.RDD`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD)
>
> <弹性分布式数据集（RDD），Spark中的基本抽象。>A Resilient Distributed Dataset (RDD), the basic abstraction in Spark.
>
> [`pyspark.streaming.StreamingContext`](http://spark.apache.org/docs/latest/api/python/pyspark.streaming.html#pyspark.streaming.StreamingContext)
>
> <Spark Streaming功能的主要入口点> Main entry point for Spark Streaming functionality.
>
> [`pyspark.streaming.DStream`](http://spark.apache.org/docs/latest/api/python/pyspark.streaming.html#pyspark.streaming.DStream)
>
> <离散化流（DStream），Spark Streaming中的基本抽象>A Discretized Stream (DStream), the basic abstraction in Spark Streaming.
>
> [`pyspark.sql.SQLContext`](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.SQLContext)
>
> <DataFrame和SQL功能的主要入口点>Main entry point for DataFrame and SQL functionality.
>
> [`pyspark.sql.DataFrame`](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame)
>
> <分组到已命名列中的分布式数据集合>A distributed collection of data grouped into named columns.

# Indices and tables[¶](http://spark.apache.org/docs/latest/api/python/index.html#indices-and-tables)

- [Search Page](http://spark.apache.org/docs/latest/api/python/search.html)



-------------

# pyspark package

## Subpackages

- [pyspark.sql module](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html)
- [pyspark.streaming module](http://spark.apache.org/docs/latest/api/python/pyspark.streaming.html)
- [pyspark.ml package](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html)
- [pyspark.mllib package](http://spark.apache.org/docs/latest/api/python/pyspark.mllib.html)

## Contents

PySpark is the Python API for Spark.

Public classes:

> - - [`SparkContext`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext):
>
>     Main entry point for Spark functionality.
>
> - - [`RDD`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD):
>
>     A Resilient Distributed Dataset (RDD), the basic abstraction in Spark.
>
> - - [`Broadcast`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.Broadcast):
>
>     A broadcast variable that gets reused across tasks.
>
> - - [`Accumulator`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.Accumulator):
>
>     An “add-only” shared variable that tasks can only add values to.
>
> - - [`SparkConf`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkConf):
>
>     For configuring Spark.
>
> - - [`SparkFiles`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkFiles):
>
>     Access files shipped with jobs.
>
> - - [`StorageLevel`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.StorageLevel):
>
>     Finer-grained cache persistence levels.
>
> - - [`TaskContext`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.TaskContext):
>
>     Information about the current running task, available on the workers and experimental.

- *class* `pyspark.``SparkConf`(*loadDefaults=True*, *_jvm=None*, *_jconf=None*)[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/conf.html#SparkConf)

  Spark应用程序的配置。用于将各种Spark参数设置为键值对。

  大多数情况下，您将创建一个SparkConf对象[`SparkConf()`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkConf)，该对象 将从spark。* Java系统属性中加载值。在这种情况下，您直接在[`SparkConf`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkConf)对象上设置的任何参数都优先于系统属性。

  对于单元测试，您也可以调用`SparkConf(false)`跳过加载外部设置并获取相同的配置，而不管系统属性如何。

  这个类中的所有setter方法都支持链接。例如，您可以编写conf.setMaster（“local”）。setAppName（“My app”）。

  > 注意: 一旦将SparkConf对象传递给Spark，它就会被克隆，并且不能再由用户修改。

  - `contains`（*key* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/conf.html#SparkConf.contains)

    此配置是否包含给定的密钥？


  - `get`（*key*，*defaultValue = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/conf.html#SparkConf.get)

    获取某个键的配置值，否则返回默认值。


  - `getAll`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/conf.html#SparkConf.getAll)

    获取所有值作为键值对的列表。


  - `set`（*key*，*value* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/conf.html#SparkConf.set)

    设置配置属性。


  - `setAll`（*双*）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/conf.html#SparkConf.setAll)

    设置多个参数，作为键值对列表传递。参数：**对** - 要设置的键值**对**列表


  - `setAppName`（*价值*）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/conf.html#SparkConf.setAppName)

    设置应用程序名称


  - `setExecutorEnv`（*key = None*，*value = None*，*pairs = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/conf.html#SparkConf.setExecutorEnv)

    设置要传递给执行者的环境变量。


  - `setIfMissing`（*key*，*value* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/conf.html#SparkConf.setIfMissing)

    设置配置属性（如果尚未设置）。


  - `setMaster`（*价值*）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/conf.html#SparkConf.setMaster)

    设置要连接的主要URL。


  - `setSparkHome`（*价值*）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/conf.html#SparkConf.setSparkHome)

    设置工作站节点上安装Spark的路径。


  - `toDebugString`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/conf.html#SparkConf.toDebugString)

    以键=值对的列表形式返回配置的可打印版本，每行一个。


- *class* `pyspark.``SparkContext`(*master=None*, *appName=None*, *sparkHome=None*, *pyFiles=None*, *environment=None*, *batchSize=0*, *serializer=PickleSerializer()*, *conf=None*, *gateway=None*, *jsc=None*, *profiler_cls=<class 'pyspark.profiler.BasicProfiler'>*)[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext)

  Spark功能的主要入口点。SparkContext表示与Spark集群的连接，并可用于[`RDD`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD)在该集群上创建和广播变量。

  - `PACKAGE_EXTENSIONS`*=（'.zip'，'.egg'，'.jar'）*



  - `accumulator`（*value*，*accum_param = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.accumulator)

    创建一个[`Accumulator`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.Accumulator)给定的初始值，使用给定的 [`AccumulatorParam`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.AccumulatorParam)帮助对象来定义如何提供数据类型的值。如果您不提供一个，则默认AccumulatorParams用于整数和浮点数。对于其他类型，可以使用自定义的AccumulatorParam。


  - `addFile`（*path*，*recursive = False* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.addFile)

    在每个节点上使用此Spark作业添加要下载的文件。该`path`传递可以是本地文件，在HDFS（或其他Hadoop的支持的文件系统）的文件，或HTTP，HTTPS或FTP URI。要访问Spark作业中的文件，请使用文件名L {SparkFiles.get（fileName）<pyspark.files.SparkFiles.get>}来查找其下载位置。如果递归选项设置为True，则可以提供一个目录。当前目录仅支持Hadoop支持的文件系统。`>>> from  pyspark  import  SparkFiles >>> path  =  os 。路径。加入（tempdir ， “test.txt” ）>>> with  open （path ， “w” ） as  testFile ：...    _  =  testFile 。写（“100” ）>>> sc 。addFile （路径）>>> DEF  FUNC （迭代）： 。   与 开放式（SparkFiles 。获得（“的test.txt” ）） 为 TESTFILE ：...        fileVal  =  INT （TESTFILE 。的ReadLine （））...        返回 [ X  *  fileVal  为 X  在 迭代器] >>> SC 。并行化（[ 1 ， 2 ， 3 ， 4 ]） 。mapPartitions （func ）。搜集（）[100,200,300,400]`


  - `addPyFile`（*path* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.addPyFile)

    为将来在此SparkContext上执行的所有任务添加.py或.zip依赖项。该`path`传递可以是本地文件，在HDFS（或其他Hadoop的支持的文件系统）的文件，或HTTP，HTTPS或FTP URI。


  - `applicationId`

    Spark应用程序的唯一标识符。其格式取决于调度程序的实现。在本地火花应用程序的情况下，如“本地-1433865536131”在YARN的情况下，像'application_1433865536131_34483'`>>> sc 。applicationId'local   -...'`


  - `binaryFiles`（*path*，*minPartitions = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.binaryFiles)

    注意 试验从HDFS，本地文件系统（所有节点上都可用）或Hadoop支持的任何文件系统URI中读取二进制文件的目录作为字节数组。每个文件都被读取为单个记录并以键值对返回，其中键是每个文件的路径，该值是每个文件的内容。注意 小文件是首选，大文件也是允许的，但可能会导致性能不佳。


  - `binaryRecords`（*path*，*recordLength* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.binaryRecords)

    注意 试验如果每个记录都是一组具有指定数字格式的数字（请参阅ByteBuffer），并且每条记录的字节数是恒定的，则从平面二进制文件加载数据。参数：**路径** - 目录到输入数据文件**recordLength** - 分割记录的长度


  - `broadcast`（*价值*）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.broadcast)

    向群集广播一个只读变量，返回一个L {Broadcast <pyspark.broadcast.Broadcast>}对象以便在分布式函数中读取它。该变量只会发送到每个群集一次。


  - `cancelAllJobs`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.cancelAllJobs)

    取消所有已安排或正在运行的作业。


  - `cancelJobGroup`（*groupId* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.cancelJobGroup)

    取消指定组的活动作业。查看[`SparkContext.setJobGroup`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext.setJobGroup) 更多信息。


  - `defaultMinPartitions`

    当用户未给出Hadoop RDD的默认分区数时


  - `defaultParallelism`

    当用户没有给出默认的并行度水平时（例如，为了减少任务）


  - `dump_profiles`（*path* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.dump_profiles)

    将配置文件统计信息转储到目录路径中


  - `emptyRDD`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.emptyRDD)

    创建一个没有分区或元素的RDD。


  - `getConf`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.getConf)



  - `getLocalProperty`（*key* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.getLocalProperty)

    获取此线程中设置的本地属性，如果缺失则返回null。看到 [`setLocalProperty`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext.setLocalProperty)


  - *classmethod* `getOrCreate`（*conf = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.getOrCreate)

    获取或实例化SparkContext并将其注册为单例对象。参数：**conf** - SparkConf（可选）


  - `hadoopFile`（*path*，*inputFormatClass*，*keyClass*，*valueClass*，*keyConverter = None*，*valueConverter = None*，*conf = None*，*batchSize = 0* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.hadoopFile)

    使用HDFS中的任意键和值类，本地文件系统（所有节点上都可用）或任何Hadoop支持的文件系统URI读取“旧”Hadoop InputFormat。该机制与sc.sequenceFile相同。Hadoop配置可以作为Python字典传入。这将转换为Java中的配置。参数：**路径** - Hadoop文件的路径**inputFormatClass** - Hadoop InputFormat的完全限定类名（例如“org.apache.hadoop.mapred.TextInputFormat”）**keyClass** - 关键Writable类的完全限定类名（例如“org.apache.hadoop.io.Text”）**valueClass** - 值的完全限定类名可写类（例如“org.apache.hadoop.io.LongWritable”）**keyConverter** - （默认无）**valueConverter** - （默认无）**conf** - Hadoop配置，以字典形式传入（默认为无）**batchSize** - 表示为单个Java对象的Python对象的数量。（默认为0，自动选择batchSize）


  - `hadoopRDD`（*inputFormatClass*，*keyClass*，*valueClass*，*keyConverter = None*，*valueConverter = None*，*conf = None*，*batchSize = 0* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.hadoopRDD)

    从任意Hadoop配置中读取具有任意键和值类的“旧”Hadoop InputFormat，该配置以Python词典形式传入。这将转换为Java中的配置。该机制与sc.sequenceFile相同。参数：**inputFormatClass** - Hadoop InputFormat的完全限定类名（例如“org.apache.hadoop.mapred.TextInputFormat”）**keyClass** - 关键Writable类的完全限定类名（例如“org.apache.hadoop.io.Text”）**valueClass** - 值的完全限定类名可写类（例如“org.apache.hadoop.io.LongWritable”）**keyConverter** - （默认无）**valueConverter** - （默认无）**conf** - Hadoop配置，以字典形式传入（默认为无）**batchSize** - 表示为单个Java对象的Python对象的数量。（默认为0，自动选择batchSize）


  - `newAPIHadoopFile`（*path*，*inputFormatClass*，*keyClass*，*valueClass*，*keyConverter = None*，*valueConverter = None*，*conf = None*，*batchSize = 0* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.newAPIHadoopFile)

    使用HDFS中的任意键和值类，本地文件系统（所有节点都可用）或任何Hadoop支持的文件系统URI读取“新API”Hadoop InputFormat。该机制与sc.sequenceFile相同。Hadoop配置可以作为Python字典传入。这将转换为Java中的配置参数：**路径** - Hadoop文件的路径**inputFormatClass** - Hadoop InputFormat的完全限定类名（例如“org.apache.hadoop.mapreduce.lib.input.TextInputFormat”）**keyClass** - 关键Writable类的完全限定类名（例如“org.apache.hadoop.io.Text”）**valueClass** - 值的完全限定类名可写类（例如“org.apache.hadoop.io.LongWritable”）**keyConverter** - （默认无）**valueConverter** - （默认无）**conf** - Hadoop配置，以字典形式传入（默认为无）**batchSize** - 表示为单个Java对象的Python对象的数量。（默认为0，自动选择batchSize）


  - `newAPIHadoopRDD`（*inputFormatClass*，*keyClass*，*valueClass*，*keyConverter = None*，*valueConverter = None*，*conf = None*，*batchSize = 0* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.newAPIHadoopRDD)

    从任意Hadoop配置中读取具有任意键和值类的'新API'Hadoop InputFormat，该配置作为Python字典传入。这将转换为Java中的配置。该机制与sc.sequenceFile相同。参数：**inputFormatClass** - Hadoop InputFormat的完全限定类名（例如“org.apache.hadoop.mapreduce.lib.input.TextInputFormat”）**keyClass** - 关键Writable类的完全限定类名（例如“org.apache.hadoop.io.Text”）**valueClass** - 值的完全限定类名可写类（例如“org.apache.hadoop.io.LongWritable”）**keyConverter** - （默认无）**valueConverter** - （默认无）**conf** - Hadoop配置，以字典形式传入（默认为无）**batchSize** - 表示为单个Java对象的Python对象的数量。（默认为0，自动选择batchSize）


  - `parallelize`（*c*，*numSlices = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.parallelize)

    分发本地Python集合以形成RDD。如果输入表示性能范围，则建议使用xrange。`>>> sc 。并行化（[ 0 ， 2 ， 3 ， 4 ， 6 ]， 5 ）。glom （）。collect （）[[0]，[2]，[3]，[4]，[6]] >>> sc 。并行化（x范围（0 ， 6 ， 2 ）， 5 ）。glom （）。collect （）[[]，[0]，[]，[2]，[4]]`


  - `pickleFile`（*name*，*minPartitions = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.pickleFile)

    加载先前使用[`RDD.saveAsPickleFile`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD.saveAsPickleFile)方法保存的RDD 。`>>> tmpFile  =  NamedTemporaryFile （delete = True ）>>> tmpFile 。close （）>>> sc 。并行化（范围（10 ））。saveAsPickleFile （TMPFILE 。名， 5 ）>>> 排序（SC 。pickleFile （TMPFILE 。名称， 3 ）。收集（））[0，1，2，3，4，5，6，7，8，9]`


  - `range`（*start*，*end = None*，*step = 1*，*numSlices = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.range)

    创建一个包含从开始到结束 （独占）元素的int的新RDD，逐步增加每个元素。可以像python内置的range（）函数一样调用。如果使用单个参数调用，参数被解释为结束，并且start被设置为0。参数：**开始** - 起始值**结束** - 最终值（独占）**步** - 增量步（默认值：1）**numSlices** - 新RDD的分区数量返回：int的RDD`>>> sc 。范围（5 ）。collect （）[0，1，2，3，4] >>> sc 。范围（2 ， 4 ）。collect （）[2，3] >>> sc 。范围（1 ， 7 ， 2 ）。collect （）[1，3，5]`


  - `runJob`（*rdd*，*partitionFunc*，*partitions = None*，*allowLocal = False* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.runJob)

    在指定的一组分区上执行给定的partitionFunc，并将结果作为一组元素返回。如果未指定“分区”，则会在所有分区上运行。`>>> myRDD  =  sc 。并行化（范围（6 ）， 3 ）>>> sc 。runJob （myRDD ， 拉姆达 部分： [ X  *  X  为 X  在 部分]）[0,1，4，9，16，25]``>>> myRDD  =  sc 。并行化（范围（6 ）， 3 ）>>> sc 。runJob （myRDD ， 拉姆达 部分： [ X  *  X  为 X  在 部分]， [ 0 ， 2 ]， 真）[0,1，16，25]`


  - `sequenceFile`（*path*，*keyClass = None*，*valueClass = None*，*keyConverter = None*，*valueConverter = None*，*minSplits = None*，*batchSize = 0* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.sequenceFile)

    使用任意键和值读取Hadoop SequenceFile HDFS的可写类，本地文件系统（所有节点都可用）或任何Hadoop支持的文件系统URI。机制如下：Java RDD由SequenceFile或其他InputFormat以及键和值Writable类创建序列化试图通过Pyrolite酸洗如果失败，则回退是对每个键和值调用“toString”[`PickleSerializer`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.PickleSerializer) 用于反序列化Python端的pickle对象参数：**路径** - sequncefile的路径**keyClass** - 关键Writable类的完全限定类名（例如“org.apache.hadoop.io.Text”）**valueClass** - 值的完全限定类名可写类（例如“org.apache.hadoop.io.LongWritable”）**keyConverter** -**valueConverter** -**minSplits** - 数据集中的最小分割（默认min（2，sc.defaultParallelism））**batchSize** - 表示为单个Java对象的Python对象的数量。（默认为0，自动选择batchSize）


  - `setCheckpointDir`（*dirName* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.setCheckpointDir)

    设置RDD将被检查点的目录。如果在群集上运行，该目录必须是HDFS路径。


  - `setJobDescription`（*价值*）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.setJobDescription)

    设置当前作业的人类可读描述。


  - `setJobGroup`（*groupId*，*description*，*interruptOnCancel = False* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.setJobGroup)

    为此线程启动的所有作业分配一个组ID，直到组ID被设置为不同的值或清除。通常，应用程序中的执行单元由多个Spark操作或作业组成。应用程序员可以使用此方法将所有这些作业分组在一起并给出组描述。一旦设置，Spark Web UI将把这些作业与这个组关联起来。该应用程序可以[`SparkContext.cancelJobGroup`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext.cancelJobGroup)用来取消该组中的所有正在运行的作业。`>>> import  threading >>> from  time  import  sleep >>> result  =  “Not Set” >>> lock  =  线程。Lock （）>>> def  map_func （x ）：...     sleep （100 ）...     raise  Exception （“Task should be cancelled” ）>>> def  start_job （x ）：...     全局 结果...     尝试：        sc 。setJobGroup （“job_to_cancel” ， “some description” ）...         result  =  sc 。并行化（范围（x ））。地图（map_func ）。收集（）...     除 例外 为 ë ：...         结果 =  “取消” ...     锁。release （）>>> def  stop_job （）：...     sleep （5）...     sc 。cancelJobGroup （“job_to_cancel” ）>>> 剿 =  锁。acquire （）>>> supress  =  线程。线程（target = start_job ， args = （10 ，））。start （）>>> supress  =  线程。线程（target = stop_job ）。start （）>>> supress  = 锁定。acquire （）>>> print （result ）已取消`如果作业组的interruptOnCancel设置为true，则作业取消将导致Thread.interrupt（）在作业的执行程序线程上被调用。这有助于确保实时地停止任务，但由于HDFS-1208的原因，默认情况下会关闭，HDFS可能会通过将节点标记为无效来响应Thread.interrupt（）。


  - `setLocalProperty`（*key*，*value* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.setLocalProperty)

    设置影响从此线程提交的作业的本地属性，例如Spark Fair Scheduler池。


  - `setLogLevel`（*logLevel* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.setLogLevel)

    控制我们的logLevel。这会覆盖任何用户定义的日志设置。有效的日志级别包括：ALL，DEBUG，ERROR，FATAL，INFO，OFF，TRACE，WARN


  - *classmethod* `setSystemProperty`（*key*，*value* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.setSystemProperty)

    设置Java系统属性，如spark.executor.memory。这必须在实例化SparkContext之前调用。


  - `show_profiles`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.show_profiles)

    将配置文件统计信息打印到标准输出


  - `sparkUser`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.sparkUser)

    为运行SparkContext的用户获取SPARK_USER。


  - `startTime`

    Spark Context开始时返回纪元时间。


  - `statusTracker`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.statusTracker)

    返回[`StatusTracker`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.StatusTracker)对象


  - `stop`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.stop)

    关闭SparkContext。


  - `textFile`（*name*，*minPartitions = None*，*use_unicode = True* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.textFile)

    从HDFS读取文本文件，本地文件系统（所有节点都可用）或任何Hadoop支持的文件系统URI，并将其作为字符串的RDD返回。如果use_unicode为False，则字符串将保持为str（编码为utf-8），这比unicode更快更小。（在Spark 1.2中添加）`>>> path  =  os 。路径。加入（tempdir ， “sample-text.txt” ）>>> with  open （path ， “w” ） as  testFile ：...    _  =  testFile 。写（“Hello world！” ）>>> textFile  =  sc 。textFile （路径）>>> textFile 。collect （）['Hello world！']`


  - `uiWebUrl`

    返回由此SparkContext启动的SparkUI实例的URL


  - `union`（*rdds* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.union)

    建立RDD列表的联合。这支持具有不同序列化格式的RDD的联合（），尽管这迫使它们使用默认序列化器被重新串行化：`>>> path  =  os 。路径。加入（tempdir ， “union-text.txt” ）>>> with  open （path ， “w” ） as  testFile ：...    _  =  testFile 。写（“你好” ）>>> textFile  =  sc 。textFile （路径）>>> textFile 。collect （）['Hello'] >>>  sc 。并行（[ “世界！” ]）>>> 排序（SC 。工会（[ 文本文件， 并行]） 。收集（））[ '你好'， '世界！']`


  - `version`

    此应用程序正在运行的Spark版本。


  - `wholeTextFiles`（*path*，*minPartitions = None*，*use_unicode = True* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/context.html#SparkContext.wholeTextFiles)

    从HDFS，本地文件系统（所有节点上都可用）或任何Hadoop支持的文件系统URI中读取文本文件的目录。每个文件都被读取为单个记录并以键值对返回，其中键是每个文件的路径，该值是每个文件的内容。如果use_unicode为False，则字符串将保持为str（编码为utf-8），这比unicode更快更小。（在Spark 1.2中添加）例如，如果您有以下文件：`hdfs ：// a - hdfs - 路径/ 部分- 00000 hdfs ：// a - hdfs - 路径/ 部分- 00001 ... hdfs ：// a - hdfs - 路径/ 部分- nnnnn`做rdd = sparkContext.wholeTextFiles（“hdfs：// a-hdfs-path”），然后`rdd`包含：`（a - hdfs - path / part - 00000 ， 其 内容）（a - hdfs - path / part - 00001 ， 其 内容）... （a - hdfs - path / part - nnnnn ， 其 内容）`注意 小文件是首选，因为每个文件都将完全加载到内存中。`>>> dirPath  =  os 。路径。加入（tempdir ， “文件” ）>>> os 。MKDIR （dirPath ）>>> 与 开放（OS ，路径，加入（dirPath ， “1.txt的” ）， “W” ） 为 文件1 ：...    _  =  文件1 。写（“1” ）>>> 路径。加入（dirPath ， “2.txt” ）， “w” ） 作为 file2 ：...    _  =  file2 。写（“2” ）>>> textFiles  =  sc 。wholeTextFiles （dirPath ）>>> 排序（TEXTFILES 。收集（））[（ '... / 1.txt的'， '1'），（ '... / 2.txt'， '2'）]`


- *class* `pyspark.``SparkFiles`[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/files.html#SparkFiles)

  解析通过L {SparkContext.addFile（）<pyspark.context.SparkContext.addFile>}添加的文件的路径。

  SparkFiles仅包含类方法; 用户不应该创建SparkFiles实例。

  - *classmethod* `get`（*filename* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/files.html#SparkFiles.get)

    获取通过添加的文件的绝对路径[`SparkContext.addFile()`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext.addFile)。


  - *classmethod* `getRootDirectory`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/files.html#SparkFiles.getRootDirectory)

    获取包含通过添加文件的根目录 [`SparkContext.addFile()`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext.addFile)


- *class* `pyspark.``RDD`(*jrdd*, *ctx*, *jrdd_deserializer=AutoBatchedSerializer(PickleSerializer())*)[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD)

  弹性分布式数据集（RDD），Spark中的基本抽象。表示可以并行操作的不可变分区元素集合。

  - `aggregate`（*zeroValue*，*seqOp*，*combOp* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.aggregate)

    使用给定的组合函数和中性的“零值”合计每个分区的元素，然后聚合所有分区的结果。函数op（t1，t2）被允许修改`t1`并返回它的结果值以避免对象分配; 但是，它不应该修改`t2`。第一个函数（seqOp）可以返回与此RDD类型不同的结果类型U。因此，我们需要一个将T合并为U的操作，以及一个合并两个U的操作`>>> seqOp  =  （lambda  x ， y ： （x [ 0 ]  +  y ， x [ 1 ]  +  1 ））>>> combOp  =  （lambda  x ， y ： （x [ 0 ]  +  y [ 0 ]， x [ 1 ]  +  y [ 1 ]））>>> sc 。并行化（[ 1， 2 ， 3 ， 4 ]） 。骨料（（0 ， 0 ）， SEQOP ， combOp ）（10,4）>>> SC 。并行化（[]）。骨料（（0 ， 0 ）， SEQOP ， combOp ）（0,0）`


  - `aggregateByKey`（*zeroValue*，*seqFunc*，*combFunc*，*numPartitions = None*，*partitionFunc = <function portable_hash>* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.aggregateByKey)

    使用给定的组合函数和中性的“零值”合计每个键的值。此函数可以返回与此RDD中的值类型不同的结果类型U.因此，我们需要一个将V合并到U的操作，以及一个合并两个U的操作，前一个操作用于合并分区内的值，后者用于合并分区之间的值。为了避免内存分配，这两个函数都可以修改并返回它们的第一个参数，而不是创建一个新的U.


  - `cache`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.cache)

    使用默认存储级别（`MEMORY_ONLY`）坚持此RDD 。


  - `cartesian`（*other* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.cartesian)

    返回此RDD和另一个的笛卡尔乘积，即，所有对的元素的RDD （A，B）其中，`a`是在`self`与 `b`在`other`。`>>> rdd  =  sc 。并行化（[ 1 ， 2 ]）>>> 排序（RDD 。笛卡尔（RDD ）。收集（））[（1，1），（1,2），（2,1），（2,2）]`


  - `checkpoint`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.checkpoint)

    将此RDD标记为检查点。它将被保存到设置的检查点目录内的文件中，[`SparkContext.setCheckpointDir()`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext.setCheckpointDir)并且对其父RDD的所有引用都将被删除。在此RDD上执行任何作业之前，必须调用此函数。强烈建议将此RDD保存在内存中，否则将其保存在文件中将需要重新计算。


  - `coalesce`（*numPartitions*，*shuffle = False* ）[[源代码\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.coalesce)

    返回一个减少到numPartitions分区的新RDD 。`>>> sc 。并行化（[ 1 ， 2 ， 3 ， 4 ， 5 ]， 3 ）。glom （）。collect （）[[1]，[2,3]，[4，5]] >>> sc 。并行化（[ 1 ， 2 ， 3 ， 4 ， 5 ]， 3 ）。合并（1 ）。glom （）。collect （）[[1，2，3，4，5]]`


  - `cogroup`（*other*，*numPartitions = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.cogroup)

    对于`self`or中的每个关键字k `other`，返回一个包含一个元组的结果RDD `self`以及该关键字的值列表以及`other`。`>>> x  =  sc 。parallelize （[（“a” ， 1 ）， （“b” ， 4 ）]）>>> y  =  sc 。并行化（[（ “ 一” ， 2 ）]）>>> [（X ， 元组（地图（列表， ÿ ））） 为 X ， ÿ  在 排序（列表（X 。协同组（ÿ ）。collect （）））] [（'a'，（[1]，[2]）），（'b'，（[4]，[]））]`


  - `collect`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.collect)

    返回包含此RDD中所有元素的列表。注意 因为所有的数据都被加载到驱动程序的内存中，所以只有当结果数组很小时才应使用该方法。


  - `collectAsMap`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.collectAsMap)

    将此RDD中的键值对作为字典返回给主数据库。注意 因为所有的数据都加载到驱动程序的内存中，所以只有在结果数据很小时才应使用此方法。`>>> m  =  sc 。并行化（[（1 ， 2 ），  （3 ， 4 ）]） 。collectAsMap （）>>> m [ 1 ] 2 >>> m [ 3 ] 4`


  - `combineByKey`（*createCombiner*，*mergeValue*，*mergeCombiners*，*numPartitions = None*，*partitionFunc = <function portable_hash>* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.combineByKey)

    使用自定义集合函数集合每个键的元素的通用函数。对于“组合类型”C，将RDD [（K，V）]转换为RDD [（K，C）]类型的结果。用户提供三种功能：`createCombiner`，它将V变成C（例如，创建一个元素列表）`mergeValue`，将V合并到C中（例如，将其添加到列表的末尾）`mergeCombiners`，将两个C合并为一个C（例如合并列表）为了避免内存分配，mergeValue和mergeCombiners都允许修改并返回它们的第一个参数，而不是创建一个新的C.另外，用户可以控制输出RDD的分区。注意 V和C可以不同 - 例如，可以将类型（Int，Int）的RDD分组为类型（Int，List [Int]）的RDD。`>>> x  =  sc 。parallelize （[（“a” ， 1 ）， （“b” ， 1 ）， （“a” ， 2 ）]）>>> def  to_list （a ）：...     return  [ a ] ... >>> def  append （a ， b ）：...     a 。追加（b ）...     返回 一个... >>> def  extend（a ， b ）：...     a 。延伸（b ）...     返回 一个... >>> 排序（X 。combineByKey （to_list ， 追加， 延伸）。收集（））[（ 'A'，[1,2]），（ 'B'， [1]）]`


  - `context`

    该[`SparkContext`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext)RDD创建于此。


  - `count`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.count)

    返回此RDD中的元素数量。`>>> sc 。并行化（[ 2 ， 3 ， 4 ]） 。count （）3`


  - `countApprox`（*超时*，*置信度= 0.95* ）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.countApprox)

    注意 试验count（）的近似版本在超时内返回潜在的不完整结果，即使并非所有任务都已完成。`>>> rdd  =  sc 。并行化（范围（1000 ）， 10 ）>>> rdd 。countApprox （1000 ， 1.0 ）1000`


  - `countApproxDistinct`（*relativeSD = 0.05* ）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.countApproxDistinct)

    注意 试验返回RDD中不同元素的近似数量。所使用的算法基于streamlib实现的 [“HyperlogLog实践：一种先进的基数估计算法的算法工程”，可在此处找到](http://dx.doi.org/10.1145/2452376.2452456)。参数：**relativeSD** - 相对准确度。较小的值创建需要更多空间的计数器。它必须大于0.000017。`>>> n  =  sc 。并行化（范围（1000 ））。地图（str ）。countApproxDistinct （）>>> 900  <  n  <  1100 True >>> n  =  sc 。并行化（[ i  ％ 20  for  i  in  range （1000 ）]）。countApproxDistinct （）>>> 16  <  n  <  24 True`


  - `countByKey`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.countByKey)

    计算每个键的元素数量，并将结果作为字典返回给主数据。`>>> rdd  =  sc 。并行化（[（ “ 一” ， 1 ），  （“B” ， 1 ），  （“A” ， 1 ）]）>>> 排序（RDD 。countByKey （） 。项目（））[（ '一个'，2 ），（'b'，1）]`


  - `countByValue`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.countByValue)

    将此RDD中每个唯一值的计数返回为（值，计数）对的字典。`>>> 排序（SC 。并行（[ 1 ， 2 ， 1 ， 2 ， 2 ]， 2 ）。countByValue （） 。项目（））[（1，2），（2，3）]`


  - `distinct`（*numPartitions = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.distinct)

    返回包含此RDD中不同元素的新RDD。`>>> 排序（SC 。并行（[ 1 ， 1 ， 2 ， 3 ]） 。不同的（） 。收集（））[1，2，3]`


  - `filter`（*f* ）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.filter)

    返回仅包含满足谓词的元素的新RDD。`>>> rdd  =  sc 。并行化（[ 1 ， 2 ， 3 ， 4 ， 5 ]）>>> RDD 。过滤器（lambda  x ： x  ％ 2  ==  0 ）。collect （）[2，4]`


  - `first`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.first)

    返回此RDD中的第一个元素。`>>> sc 。并行化（[ 2 ， 3 ， 4 ]） 。first （）2 >>> sc 。并行化（[]）。first （）Traceback（最近一次调用最后一次）：    ... ValueError：RDD为空`


  - `flatMap`（*f*，*preservesPartitioning = False* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.flatMap)

    首先将函数应用于此RDD的所有元素，然后展平结果，以返回新的RDD。`>>> rdd  =  sc 。并行化（[ 2 ， 3 ， 4 ]）>>> 排序（RDD 。flatMap （拉姆达 X ： 范围（1 ， X ）） 。收集（））[1，1，1，2，2，3] >>> 排序（RDD 。flatMap （拉姆达 X ： [（X ， X ），  （X ， X ）]） 。collect （））[（2,2），（2,2），（3,3），（3,3），（4,4），（4,4）]`


  - `flatMapValues`（*f* ）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.flatMapValues)

    通过flatMap函数传递键值对RDD中的每个值，而不更改键; 这也保留了原始RDD的分区。`>>> x  =  sc 。parallelize （[（“a” ， [ “x” ， “y” ， “z” ]）， （“b” ， [ “p” ， “r” ]）] >>> def  f （x ）： return  x >>> x 。flatMapValues （f ）。collect （）[（'a'，'x'），（'a'，'y'），（'a'，'z'），（'b'，'p'），（'b'，' R'）]`


  - `fold`（*zeroValue*，*op* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.fold)

    使用给定的关联函数和中性的“零值”聚合每个分区的元素，然后聚合所有分区的结果。函数op（t1，t2）被允许修改`t1`并返回它的结果值以避免对象分配; 但是，它不应该修改`t2`。这与在Scala等函数语言中为非分布式集合实现的折叠操作有些不同。这种折叠操作可以单独应用于分区，然后将这些结果折叠到最终结果中，而不是按照某种定义的顺序对每个元素顺序应用折叠。对于不可交换的函数，结果可能与应用于非分布式集合的折叠结果不同。`>>> 从 运营商 导入 添加>>> sc 。并行化（[ 1 ， 2 ， 3 ， 4 ， 5 ]） 。折叠（0 ， 添加）15`


  - `foldByKey`（*zeroValue*，*func*，*numPartitions = None*，*partitionFunc = <function portable_hash>* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.foldByKey)

    使用关联函数“func”和中性“zeroValue”合并每个关键字的值，该关联函数可以添加到结果任意次数，并且不得更改结果（例如，0表示加法或1表示乘法。 ）。`>>> rdd  =  sc 。并行化（[（ “ 一” ， 1 ），  （“B” ， 1 ），  （“A” ， 1 ）]）>>> 从 操作者 进口 添加>>> 排序（RDD 。foldByKey （0 ， 添加）。收集（））[（'a'，2），（'b'，1）]`


  - `foreach`（*f* ）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.foreach)

    将此功能应用于此RDD的所有元素。`>>> def  f （x ）： print （x ）>>> sc 。并行化（[ 1 ， 2 ， 3 ， 4 ， 5 ]） 。的foreach （˚F ）`


  - `foreachPartition`（*f* ）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.foreachPartition)

    将此功能应用于此RDD的每个分区。`>>> 高清 ˚F （迭代器）：...     对于 X  在 迭代：...          打印（X ）>>> SC 。并行化（[ 1 ， 2 ， 3 ， 4 ， 5 ]） 。foreachPartition （f ）`


  - `fullOuterJoin`（*other*，*numPartitions = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.fullOuterJoin)

    执行右外连接的`self`和`other`。对于每个元素（k，v）in `self`，`other`如果没有元素`other`具有密钥k ，则所得到的RDD将包含w in 或所述对（k，（v，None））的所有对（k，（v，w））。类似地，对于每个元素（k，w）in `other`，`self`如果没有元素`self`具有v in ，或者对（k，（None，w）），则所得到的RDD将包含所有对（k，键k。散列 - 将生成的RDD分区到给定数量的分区中。`>>> x  =  sc 。parallelize （[（“a” ， 1 ）， （“b” ， 4 ）]）>>> y  =  sc 。并行化（[（ “ 一” ， 2 ），  （“C” ， 8 ）]）>>> 排序（X 。fullOuterJoin （Ý ）。收集（））[（ 'A'，（1，2）），（ 'b'，（4，None）），（'c'，（None，8））]`


  - `getCheckpointFile`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.getCheckpointFile)

    获取此RDD被检查点的文件的名称RDD在本地检查点时未定义。


  - `getNumPartitions`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.getNumPartitions)

    返回RDD中的分区数量`>>> rdd  =  sc 。并行化（[ 1 ， 2 ， 3 ， 4 ]， 2 ）>>> RDD 。getNumPartitions （）2`


  - `getStorageLevel`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.getStorageLevel)

    获取RDD的当前存储级别。`>>> rdd1  =  sc 。并行化（[ 1 ，2 ]）>>> RDD1集。getStorageLevel （）StorageLevel（FALSE，FALSE，FALSE，FALSE，1）>>> 打印（RDD1集。getStorageLevel （））序列化1X复制`


  - `glom`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.glom)

    通过将每个分区内的所有元素合并到一个列表中返回一个RDD。`>>> rdd  =  sc 。并行化（[ 1 ， 2 ， 3 ， 4 ]， 2 ）>>> 排序（RDD 。据为己有（） 。收集（）） [[1，2]，[3，4]]`


  - `groupBy`（*f*，*numPartitions = None*，*partitionFunc = <function portable_hash>* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.groupBy)

    返回分组项目的RDD。`>>> rdd  =  sc 。并行化（[ 1 ， 1 ， 2 ， 3 ， 5 ， 8 ]）>>> 结果 =  RDD 。groupBy （lambda  x ： x  ％ 2 ）。collect （）>>> sorted （[（x ， sorted （y ）） for  （x ， y ） in  result ]）[（0，[2,8]），（1，[1，3，5]）]`


  - `groupByKey`（*numPartitions = None*，*partitionFunc = <function portable_hash>* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.groupByKey)

    将RDD中每个键的值分组为单个序列。散列 - 将生成的RDD与numPartitions分区进行分区。注意 如果您正在分组以便对每个密钥执行聚合（例如总计或平均），则使用reduceByKey或aggregateByKey将提供更好的性能。`>>> rdd  =  sc 。并行化（[（ “ 一” ， 1 ），  （“B” ， 1 ），  （“A” ， 1 ）]）>>> 排序（RDD 。groupByKey （） 。mapValues （LEN ）。收集（））[（ 'A'，2），（ 'b'，1）] >>> 排序（RDD 。groupByKey （） 。mapValues （列表）。[（'a'，[1,1]），（'b'，[1]）]`


  - `groupWith`（*其他*，**其他*）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.groupWith)

    cogroup的别名，但支持多个RDD。`>>> w  =  sc 。parallelize （[（“a” ， 5 ）， （“b” ， 6 ）]）>>> x  =  sc 。parallelize （[（“a” ， 1 ）， （“b” ， 4 ）]）>>> y  =  sc 。parallelize （[（“a” ， 2 ）]）>>> z  =  sc 。并行化（[（“b” ， [（X ， 元组（地图（列表， ÿ ））） 为 X ， ÿ  在 排序（列表（瓦特。groupWith （X ， ÿ ， Ž ）。收集（）））] [（ 'A'，（[5] ，[1]，[2]，[]）），（'b'，（[6]，[4]，[]，[42]））]`


  - `histogram`（*桶*）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.histogram)

    使用提供的桶计算直方图。除了最后一个关闭之外，所有桶都向右开放。例如[1,10,20,50]表示桶是[1,10] [10,20] [20,50]，这意味着1 <= x <10,10 <= x <20,20 <= x <= 50。在1和50的输入上，我们将得到1,0,1的直方图。如果你的直方图是均匀间隔的（例如[0,10,20,30]），则可以从O（log n）inseration转换为每个元素O（1）（其中n是桶的数量）。桶必须进行排序，不包含任何重复项，并且至少有两个元素。如果存储区是数字，它将生成在RDD的最小值和最大值之间均匀分布的存储区。例如，如果最小值为0，最大值为100，则给定存储桶 为2，则结果存储桶将为[0,50）[50,100]。桶必须至少为1.如果RDD包含无穷大，则会引发异常。如果RDD中的元素不发生变化（max == min），则将使用一个桶。返回值是一个桶和直方图的元组。`>>> rdd  =  sc 。并行化（范围（51 ））>>> rdd 。直方图（2 ）（[ 0,25,50 ]，[25,26]）>>> rdd 。直方图（[ 0 ， 5 ， 25 ， 50 ]）（[0，5，25，50]，[5，20，26]）>>> RDD 。直方图（[ 0 ， 15 ， 30 ， 45 ， 60 ]）   ＃均匀间隔开的叶片（[0,15,30,45,60]，[ 15,15,15,6 ]）>>> rdd  =  sc 。并行化（[ “ab” ， “ac” ， “b” ， “bd” ， “ef” ]）>>> rdd 。直方图（（“a” ， “b” ， “c” ））（（'a'，'b'，'c'），[2,2]）`


  - `id`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.id)

    此RDD的唯一ID（在其SparkContext中）。


  - `intersection`（*other* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.intersection)

    返回此RDD与另一个RDD的交集。输出不会包含任何重复的元素，即使输入RDD也是如此。注意 此方法在内部执行洗牌。`>>> rdd1  =  sc 。并行化（[ 1 ， 10 ， 2 ， 3 ， 4 ， 5 ]）>>> RDD2  =  SC 。并行化（[ 1 ， 6 ， 2 ， 3 ， 7 ， 8 ]）>>> RDD1集。相交（rdd2 ）。collect （）[1，2，3]`


  - `isCheckpointed`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.isCheckpointed)

    返回此RDD是否已检查点和实现，可靠或本地。


  - `isEmpty`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.isEmpty)

    当且仅当RDD根本不包含任何元素时返回true。注意 RDD可能是空的，即使它至少有一个分区。`>>> sc 。并行化（[]）。isEmpty （）True >>> sc 。并行化（[ 1 ]）。isEmpty （）错误`


  - `isLocallyCheckpointed`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.isLocallyCheckpointed)

    返回此RDD是否标记为本地检查点。暴露于测试。


  - `join`（*other*，*numPartitions = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.join)

    返回一个RDD，其中包含in `self`和in中匹配键的所有元素对 `other`。每对元素将作为（k，（v1，v2））元组返回，其中（k，v1）处于`self`和（k，v2）处于中`other`。在群集中执行散列连接。`>>> x  =  sc 。parallelize （[（“a” ， 1 ）， （“b” ， 4 ）]）>>> y  =  sc 。并行化（[（ “ 一” ， 2 ），  （“A” ， 3 ）]）>>> 排序（X 。加入（Ý ）。收集（））[（ 'A'，（1，2）），（ 'a'，（1，3））]`


  - `keyBy`（*f* ）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.keyBy)

    通过应用在此RDD中创建元素的元组`f`。`>>> x  =  sc 。并行化（范围（0 ，3 ）） 。keyBy （lambda  x ： x * x ）>>> y  =  sc 。并行化（拉链（范围（0 ，5 ）， 范围（0 ，5 ）））>>> [（X ， 列表（地图（列表， ÿ ））） 对于 X ， ÿ  在 排序（X 。协同组（Ý ）。收集（））] [（0，[[0]，[0]]），（1，[1]，[1]]），（2 ，[[]，[2]]），（3，[[]，[3]]），（4，[[2]，[4]]）]`


  - `keys`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.keys)

    用每个元组的键返回一个RDD。`>>> m  =  sc 。并行化（[（1 ， 2 ），  （3 ， 4 ）]） 。keys （）>>> m 。collect （）[1，3]`


  - `leftOuterJoin`（*other*，*numPartitions = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.leftOuterJoin)

    执行左外连接的`self`和`other`。对于每个元素（k，v）in `self`，`other`如果没有元素`other`具有密钥k ，则所得到的RDD将包含w in 或所述对（k，（v，None））的所有对（k，（v，w））。散列 - 将生成的RDD分区到给定数量的分区中。`>>> x  =  sc 。parallelize （[（“a” ， 1 ）， （“b” ， 4 ）]）>>> y  =  sc 。并行化（[（ “ 一” ， 2 ）]）>>> 排序（X 。leftOuterJoin （Ý ）。收集（））[（ 'A'，（1，2）），（ 'B'，（4，无））]`


  - `localCheckpoint`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.localCheckpoint)

    使用Spark的现有缓存层将此RDD标记为本地点检查。此方法适用于希望截断RDD谱系的用户，同时跳过在可靠的分布式文件系统中复制物化数据的昂贵步骤。这对于需要定期截断的长谱系的RDD很有用（如GraphX）。本地检查点会牺牲性能的容错性。特别是，将检查点数据写入执行程序中的临时本地存储，而不是写入可靠的容错存储。结果是如果执行程序在计算过程中失败，检查点数据可能不再可访问，导致无法恢复的作业失败。这对使用动态分配并不安全，这会删除执行程序及其缓存块。如果您必须同时使用这两项功能，建议您设置`spark.dynamicAllocation.cachedExecutorIdleTimeout`较高的值。[`SparkContext.setCheckpointDir()`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext.setCheckpointDir)未使用设置的检查点目录。


  - `lookup`（*key* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.lookup)

    返回在RDD关键值列表键。如果RDD具有已知的分区程序，则只需搜索该键映射到的分区即可高效地执行此操作。`>>> l  =  范围（1000 ）>>> rdd  =  sc 。并行化（zip （l ， l ）， 10 ）>>> rdd 。查找（42 ）  ＃慢[42] >>> 排序 =  RDD 。sortByKey （）>>> sorted 。lookup （42 ）  ＃fast [42] >>> sorted 。查找（1024）[] >>> rdd2  =  sc 。parallelize （[（（'a' ， 'b' ）， 'c' ）]）。groupByKey （）>>> 列表（RDD2 。查找（（'A' ， 'B' ））[ 0 ]）[ 'C']`


  - `map`（*f*，*preservesPartitioning = False* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.map)

    通过对该RDD的每个元素应用一个函数来返回一个新的RDD。`>>> rdd  =  sc 。并行化（[ “b”的， “一” ， “C” ]）>>> 排序（RDD 。地图（拉姆达 X ： （X ， 1 ）） 。收集（））[（ 'A'，1），（” b'，1），（'c'，1）]`


  - `mapPartitions`（*f*，*preservesPartitioning = False* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.mapPartitions)

    通过将函数应用于此RDD的每个分区来返回新的RDD。`>>> rdd  =  sc 。并行化（[ 1 ， 2 ， 3 ， 4 ]， 2 ）>>> DEF  ˚F （迭代）： 产率 之和（迭代）>>> RDD 。mapPartitions （f ）。collect （）[3,7]`


  - `mapPartitionsWithIndex`（*f*，*preservesPartitioning = False* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.mapPartitionsWithIndex)

    通过将函数应用于此RDD的每个分区，同时跟踪原始分区的索引，返回新的RDD。`>>> rdd  =  sc 。并行化（[ 1 ， 2 ， 3 ， 4 ]， 4 ）>>> DEF  ˚F （splitIndex ， 迭代器）： 产率 splitIndex >>> RDD 。mapPartitionsWithIndex （f ）。sum （）6`


  - `mapPartitionsWithSplit`（*f*，*preservesPartitioning = False* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.mapPartitionsWithSplit)

    弃用：改为使用mapPartitionsWithIndex。通过将函数应用于此RDD的每个分区，同时跟踪原始分区的索引，返回新的RDD。`>>> rdd  =  sc 。并行化（[ 1 ， 2 ， 3 ， 4 ]， 4 ）>>> DEF  ˚F （splitIndex ， 迭代器）： 产率 splitIndex >>> RDD 。mapPartitionsWithSplit （f ）。sum （）6`


  - `mapValues`（*f* ）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.mapValues)

    通过map函数传递键值对RDD中的每个值，而不更改键; 这也保留了原始RDD的分区。`>>> x  =  sc 。parallelize （[（“a” ， [ “apple” ， “banana” ， “lemon” ]）， （“b” ， [ “grapes” ]）]）>>> def  f （x ）： return  len （x ）>>> x 。mapValues （f ）。collect （）[（'a'，3），（'b'，1）]`


  - `max`（*key = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.max)

    找到此RDD中的最大项目。参数：**键** - 用于生成比较**键**的函数`>>> rdd  =  sc 。并行化（[ 1.0 ， 5.0 ， 43.0 ， 10.0 ]）>>> RDD 。max （）43.0 >>> rdd 。max （key = str ）5.0`


  - `mean`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.mean)

    计算此RDD元素的平均值。`>>> sc 。并行化（[ 1 ， 2 ， 3 ]） 。平均（）2.0`


  - `meanApprox`（*超时*，*置信度= 0.95* ）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.meanApprox)

    注意 试验近似操作以在超时内返回平均值或满足置信度。`>>> rdd  =  sc 。并行化（范围（1000 ）， 10 ）>>> - [R  =  总和（范围（1000 ）） /  1000.0 >>> ABS （RDD 。meanApprox （1000 ） -  - [R ） /  [R  <  0.05 真`


  - `min`（*key = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.min)

    找到此RDD中的最小项目。参数：**键** - 用于生成比较**键**的函数`>>> rdd  =  sc 。并行化（[ 2.0 ， 5.0 ， 43.0 ， 10.0 ]）>>> RDD 。min （）2.0 >>> rdd 。min （key = str ）10.0`


  - `name`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.name)

    返回此RDD的名称。


  - `partitionBy`（*numPartitions*，*partitionFunc = <function portable_hash>* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.partitionBy)

    使用指定的分区程序返回分区的RDD副本。`>>> pairs  =  sc 。并行化（[ 1 ， 2 ， 3 ， 4 ， 2 ， 4 ， 1 ]） 。map （lambda  x ： （x ， x ））>>> sets  =  pairs 。partitionBy （2 ）。glom （）。collect （）>>> len （set （sets [ 0 ]）。相交（set （sets [ 1 ]）））0`


  - `persist`（*storageLevel = StorageLevel（False*，*True*，*False*，*False*，*1）*）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.persist)

    设置此RDD的存储级别以在第一次计算后在操作中保留其值。如果RDD尚未设置存储级别，则只能用于分配新的存储级别。如果未指定存储级别，则默认为（`MEMORY_ONLY`）。`>>> rdd  =  sc 。并行化（[ “b” ， “a” ， “c” ]）>>> rdd 。坚持（）。is_cached是真的`


  - `pipe`（*命令*，*env = None*，*checkCode = False* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.pipe)

    将由管道元素创建的RDD返回到分叉的外部进程。`>>> sc 。并行化（[ '1' ， '2' ， '' ， '3' ]）。管（'猫' ）。collect （）['1'，'2'，''，'3']`参数：**checkCode** - 是否检查shell命令的返回值。


  - `randomSplit`（*权重*，*种子=无*）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.randomSplit)

    随机分配此RDD与提供的权重。参数：**权重** - 分割的**权**重，如果不等于1，则将被归一化**种子** - 随机种子返回：将RDD分成列表`>>> rdd  =  sc 。并行化（范围（500 ）， 1 ）>>> rdd1 ， rdd2  =  rdd 。randomSplit （[ 2 ， 3 ]， 17 ）>>> LEN （RDD1集。收集（） +  RDD2 。收集（））500 >>> 150  <  RDD1集。count （） <  250 True >>> 250  < rdd2 。count （） <  350 True`


  - `reduce`（*f* ）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.reduce)

    使用指定的交换和关联二元运算符来减少此RDD的元素。目前本地减少分区。`>>> 从 运营商 导入 添加>>> sc 。并行化（[ 1 ， 2 ， 3 ， 4 ， 5 ]） 。减少（添加）15 >>> sc 。并行化（（2  for  _  in  range （10 ）））。地图（拉姆达 x ： 1 ）。缓存（）。减少（添加）10 >>> sc 。并行化（[]）。reduce （add ）Traceback（最近一次调用的最后一次）：    ... ValueError：不能减少（）空的RDD`


  - `reduceByKey`（*func*，*numPartitions = None*，*partitionFunc = <function portable_hash>* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.reduceByKey)

    使用关联和交换reduce函数合并每个键的值。在将结果发送到Reducer之前，这也将在每个映射器上进行本地合并，类似于MapReduce中的“合并器”。输出将使用分区进行`numPartitions`分区，或者`numPartitions`未指定缺省并行性级别if 。默认分区是散列分区。`>>> from  operator  import  add >>> rdd  =  sc 。并行化（[（ “ 一” ， 1 ），  （“B” ， 1 ），  （“A” ， 1 ）]）>>> 排序（RDD 。reduceByKey （添加）。收集（））[（ 'A'， 2），（'b'，1）]`


  - `reduceByKeyLocally`（*func* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.reduceByKeyLocally)

    使用关联和交换reduce函数合并每个键的值，但将结果立即作为字典返回给主。在将结果发送到Reducer之前，这也将在每个映射器上进行本地合并，类似于MapReduce中的“合并器”。`>>> from  operator  import  add >>> rdd  =  sc 。并行化（[（ “ 一” ， 1 ），  （“B” ， 1 ），  （“A” ， 1 ）]）>>> 排序（RDD 。reduceByKeyLocally （添加）。项（））[（ 'A'， 2），（'b'，1）]`


  - `repartition`（*numPartitions* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.repartition)

    返回具有完全numPartitions分区的新RDD。可以增加或减少此RDD中的并行性级别。在内部，这使用混洗重新分配数据。如果您要减少此RDD中的分区数量，请考虑使用coalesce，这可以避免执行混洗。`>>> rdd  =  sc 。并行化（[ 1 ，2 ，3 ，4 ，5 ，6 ，7 ]， 4 ）>>> 排序（RDD 。据为己有（） 。收集（）） [[1]，[2，3]，[4，5 ]，[6，7]] >>> LEN （RDD 。再分配（2 ）。据为己有（） 。收集（））2 >>> LEN （RDD。重新分配（10 ）。glom （）。收集（））10`


  - `repartitionAndSortWithinPartitions`（*numPartitions = None*，*partitionFunc = <function portable_hash>*，*ascending = True*，*keyfunc = <function RDD。<lambda >>* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.repartitionAndSortWithinPartitions)

    根据给定的分区器对RDD进行重新分区，并在每个生成的分区中按键分类记录。`>>> rdd  =  sc 。并行化（[（0 ， 5 ），  （3 ， 8 ），  （2 ， 6 ），  （0 ， 8 ），  （3 ， 8 ），  （1 ， 3 ）]）>>> RDD2  =  RDD 。repartitionAndSortWithinPartitions （2 ， lambda  x ： x  ％ 2 ， True ）>>>rdd2 。glom （）。collect （）[[（0,5），（0,8），（2,6）]，[（1,3），（3,8），（3,8）]]`


  - `rightOuterJoin`（*other*，*numPartitions = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.rightOuterJoin)

    执行右外连接的`self`和`other`。对于每个元素（k，w）in而言`other`，如果没有元素`self`具有密钥，则所得到的RDD将包含v中的所有对（k，（v，w）），或者该对（k，（None，w））ķ。散列 - 将生成的RDD分区到给定数量的分区中。`>>> x  =  sc 。parallelize （[（“a” ， 1 ）， （“b” ， 4 ）]）>>> y  =  sc 。并行化（[（ “ 一” ， 2 ）]）>>> 排序（Ý 。rightOuterJoin （X ）。收集（））[（ 'A'，（2，1）），（ 'B'，（无，4 ））]`


  - `sample`（*withReplacement*，*fraction*，*seed = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.sample)

    返回此RDD的采样子集。参数：**withReplacement** - 可以对元素进行多次采样（取样时取代）**分数** - 样本的预期大小，作为RDD大小的一部分，无需替换：选择每个元素的概率; 小数必须为[0，1]替换：每个元素被选择的预期次数; 分数必须> = 0**种子** -种子的随机数发生器注意 这不能保证准确地提供指定总数的分数`DataFrame`。`>>> rdd  =  sc 。并行化（范围（100 ）， 4 ）>>> 6  <=  rdd 。样品（假， 0.1 ， 81 ）。count （） <=  14 真`


  - `sampleByKey`（*withReplacement*，*fractions*，*seed = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.sampleByKey)

    返回按键采样的RDD子集（通过分层采样）。使用分数指定的不同密钥的可变采样率创建此RDD的样本，这是采样率图的关键。`>>> fractions  =  { “a” ： 0.2 ， “b” ： 0.1 } >>> rdd  =  sc 。并行化（级分。键（）） 。笛卡尔（SC 。并行（范围（0 ， 1000 ）））>>> 样品 =  字典（RDD 。sampleByKey （假， 级分， 2 ）。groupByKey （）。collect （））>>> 100  <  len （sample [ “a” ]） <  300  and  50  <  len （sample [ “b” ]） <  150 True >>> max （sample [ “a” ]） <=  999  和 min （sample [ “a” ]） > =  0 True >>> max （sample [ “ <=  999  和 min （样本[ “b” ]） > =  0 True`


  - `sampleStdev`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.sampleStdev)

    计算此RDD元素的样本标准偏差（通过除以N-1而不是N来估计标准偏差时校正偏差）。`>>> sc 。并行化（[ 1 ， 2 ， 3 ]） 。sampleStdev （）1.0`


  - `sampleVariance`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.sampleVariance)

    计算此RDD元素的样本方差（通过除以N-1而不是N来校正方差估计中的偏差）。`>>> sc 。并行化（[ 1 ， 2 ， 3 ]） 。sampleVariance （）1.0`


  - `saveAsHadoopDataset`（*conf*，*keyConverter = None*，*valueConverter = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.saveAsHadoopDataset)

    使用旧的Hadoop OutputFormat API（mapred包），将键值对（形式为RDD [（K，V）]的Python RDD输出到任何Hadoop文件系统。键/值将使用用户指定的转换器或默认情况下转换为输出 `org.apache.spark.api.python.JavaToWritableConverter`。参数：**conf** - Hadoop作业配置，作为字典传入**keyConverter** - （默认无）**valueConverter** - （默认无）


  - `saveAsHadoopFile`（*path*，*outputFormatClass*，*keyClass = None*，*valueClass = None*，*keyConverter = None*，*valueConverter = None*，*conf = None*，*compressionCodecClass = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.saveAsHadoopFile)

    使用旧的Hadoop OutputFormat API（mapred包），将键值对（形式为RDD [（K，V）]的Python RDD输出到任何Hadoop文件系统。如果未指定，则会推断键和值类型。使用用户指定的转换器或键，将键和值转换为输出`org.apache.spark.api.python.JavaToWritableConverter`。将 `conf`其应用于与此RDD的SparkContext关联的基本Hadoop conf之上，以创建用于保存数据的合并Hadoop MapReduce作业配置。参数：**路径** - Hadoop文件的路径**outputFormatClass** - Hadoop OutputFormat的完全限定类名（例如“org.apache.hadoop.mapred.SequenceFileOutputFormat”）**keyClass** - 密钥Writable类的完全限定类名（例如“org.apache.hadoop.io.IntWritable”，默认为None）**valueClass** - 值的完全限定类名可写类（例如“org.apache.hadoop.io.Text”，默认为None）**keyConverter** - （默认无）**valueConverter** - （默认无）**conf** - （默认没有）**compressionCodecClass** - （默认无）


  - `saveAsNewAPIHadoopDataset`（*conf*，*keyConverter = None*，*valueConverter = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.saveAsNewAPIHadoopDataset)

    使用新的Hadoop OutputFormat API（mapreduce包），将键值对（形式为RDD [（K，V）]的Python RDD输出到任何Hadoop文件系统。键/值将使用用户指定的转换器或默认情况下转换为输出 `org.apache.spark.api.python.JavaToWritableConverter`。参数：**conf** - Hadoop作业配置，作为字典传入**keyConverter** - （默认无）**valueConverter** - （默认无）


  - `saveAsNewAPIHadoopFile`（*path*，*outputFormatClass*，*keyClass = None*，*valueClass = None*，*keyConverter = None*，*valueConverter = None*，*conf = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.saveAsNewAPIHadoopFile)

    使用新的Hadoop OutputFormat API（mapreduce包），将键值对（形式为RDD [（K，V）]的Python RDD输出到任何Hadoop文件系统。如果未指定，则会推断键和值类型。使用用户指定的转换器或键，将键和值转换为输出`org.apache.spark.api.python.JavaToWritableConverter`。将 `conf`其应用于与此RDD的SparkContext关联的基本Hadoop conf之上，以创建用于保存数据的合并Hadoop MapReduce作业配置。参数：**路径** - Hadoop文件的路径**outputFormatClass** - Hadoop OutputFormat的完全限定类名（例如“org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat”）**keyClass** - 密钥Writable类的完全限定类名（例如“org.apache.hadoop.io.IntWritable”，默认为None）**valueClass** - 值的完全限定类名可写类（例如“org.apache.hadoop.io.Text”，默认为None）**keyConverter** - （默认无）**valueConverter** - （默认无）**conf** - Hadoop作业配置，以字典形式传入（默认为无）


  - `saveAsPickleFile`（*path*，*batchSize = 10* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.saveAsPickleFile)

    将此RDD保存为序列化对象的SequenceFile。使用的序列化程序是`pyspark.serializers.PickleSerializer`，默认批量大小为10。`>>> tmpFile  =  NamedTemporaryFile （delete = True ）>>> tmpFile 。close （）>>> sc 。并行化（[ 1 ， 2 ， '火花' ， 'RDD' ]） 。saveAsPickleFile （TMPFILE 。名称， 3 ）>>> 排序（SC 。pickleFile （TMPFILE 。名， 5 ）。图（str ）。collect （））['1'，'2'，'rdd'，'spark']`


  - `saveAsSequenceFile`（*path*，*compressionCodecClass = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.saveAsSequenceFile)

    使用我们从RDD的键和值类型转换的类型，将键值对（形式RDD [（K，V）]）的Python RDD输出到任何Hadoop文件系统`org.apache.hadoop.io.Writable`。机制如下：Pyrolite用于将pickled Python RDD转换为Java对象的RDD。此Java RDD的键和值将转换为可写并写出。参数：**路径** - 序列文件的路径**compressionCodecClass** - （默认无）


  - `saveAsTextFile`（*path*，*compressionCodecClass = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.saveAsTextFile)

    使用字符串表示元素将此RDD保存为文本文件。参数：**路径** - 文本文件的路径**compressionCodecClass** - （默认没有）字符串即“org.apache.hadoop.io.compress.GzipCodec”`>>> tempFile  =  NamedTemporaryFile （delete = True ）>>> tempFile 。close （）>>> sc 。并行化（范围（10 ））。saveAsTextFile （临时文件。名）>>> 从 的FileInput  进口 输入>>> 从 水珠 进口 水珠>>> “” 。连接（排序（输入（glob（临时文件。名 +  “/部分-0000 *” ））））'0 \ N1 \ N 2 \ N3 \ N4 \ N5 \ N6 \ N7 \ n8 \ N9 \ N'`保存到文本文件时可以容忍空行。`>>> tempFile2  =  NamedTemporaryFile （delete = True ）>>> tempFile2 。close （）>>> sc 。parallelize （[ '' ， 'foo' ， '' ， 'bar' ， '' ]）。saveAsTextFile （tempFile2 。名）>>> '' 。连接（排序（输入（glob （tempFile2 。  “/ part-0000 *” ））））'\ n \ n \ nbar \ nfoo \ n'`使用compressionCodecClass`>>> tempFile3  =  NamedTemporaryFile （delete = True ）>>> tempFile3 。close （）>>> codec  =  “org.apache.hadoop.io.compress.GzipCodec” >>> sc 。parallelize （[ 'foo' ， 'bar' ]）。saveAsTextFile （tempFile3 。名称， 编解码器）>>> 从 的FileInput  进口 输入， hook_compressed >>>  （输入（水珠（tempFile3 。名 +  “/part*.gz” ）， openhook = hook_compressed ））>>> b ' 。加入（结果）。解码（'utf-8' ）'bar \ nfoo \ n'`


  - `setName`（*名称*）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.setName)

    为此RDD指定一个名称。`>>> rdd1  =  sc 。并行化（[ 1 ， 2 ]）>>> RDD1集。setName （'RDD1' ）。name （）'RDD1'`


  - `sortBy`（*keyfunc*，*ascending = True*，*numPartitions = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.sortBy)

    按给定的keyfunc对此RDD进行排序`>>> tmp  =  [（'a' ， 1 ）， （'b' ， 2 ）， （'1' ， 3 ）， （'d' ， 4 ）， （'2' ， 5 ）] >>> sc 。并行（tmp ）。sortBy （lambda  x ： x [ 0 ]）。collect （）[（'1'，3），（'2'，5），（'a'，1），（'b'，2），（'d'，4）] >>> sc 。并行（tmp ）。sortBy （lambda  x ： x [ 1 ]）。collect （）[（'a'，1），（'b'，2），（'1'，3），（'d'，4），（'2'，5）]`


  - `sortByKey`（*ascending = True*，*numPartitions = None*，*keyfunc = <function RDD。<lambda >>* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.sortByKey)

    对此RDD进行排序，假定它由（键，值）对组成。`>>> tmp  =  [（'a' ， 1 ）， （'b' ， 2 ）， （'1' ， 3 ）， （'d' ， 4 ）， （'2' ， 5 ）] >>> sc 。并行（tmp ）。sortByKey （）。first （）（'1'，3）>>> sc 。并行（tmp ）。sortByKey （True ， ）。collect （）[（'1'，3），（'2'，5），（'a'，1），（'b'，2），（'d'，4）] >>> sc 。并行（tmp ）。sortByKey （True ， 2 ）。collect （）[（'1'，3），（'2'，5），（'a'，1），（'b'，2），（'d'，4）] >>> tmp2  =  [ （'玛丽' ， 1 ）， （'有' ， 2 ）， （'a' ， 3 ）， （'小' ，   5 ）] >>> tmp2 。extend （[（'which' ， 6 ）， （'fleece' ， 7 ）， （'was' ， 8 ）， （'white' ， 9 ）]）>>> sc 。并行化（tmp2 ）。sortByKey （真， 3 ， keyfunc = 拉姆达 ķ ： ķ 。下（）） 。collect （）[（'a'，3），（'fleece'，7），（'had'，2），（'lamb'，5），...（'white'，9），（'which'，6 ）]`


  - `stats`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.stats)

    `StatCounter`在一次操作中返回一个可捕获RDD元素的均值，方差和计数的对象。


  - `stdev`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.stdev)

    计算此RDD元素的标准偏差。`>>> sc 。并行化（[ 1 ， 2 ， 3 ]） 。stdev （）0.816 ...`


  - `subtract`（*other*，*numPartitions = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.subtract)

    返回`self`不包含的每个值`other`。`>>> x  =  sc 。parallelize （[（“a” ， 1 ）， （“b” ， 4 ）， （“b” ， 5 ）， （“a” ， 3 ）]）>>> y  =  sc 。并行化（[（ “ 一” ， 3 ），  （“C” ， 无）]）>>> 排序（X 。减去（Ý ）。收集（））[（'a'，1），（'b'，4），（'b'，5）]`


  - `subtractByKey`（*other*，*numPartitions = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.subtractByKey)

    返回`self`与匹配键无关的每个（键，值）对`other`。`>>> x  =  sc 。parallelize （[（“a” ， 1 ）， （“b” ， 4 ）， （“b” ， 5 ）， （“a” ， 2 ）]）>>> y  =  sc 。并行化（[（ “ 一” ， 3 ），  （“C” ， 无）]）>>> 排序（X 。subtractByKey （ÿ ）。[（'b'，4），（'b'，5）]`


  - `sum`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.sum)

    在此RDD中添加元素。`>>> sc 。并行化（[ 1.0 ， 2.0 ， 3.0 ]） 。sum （）6.0`


  - `sumApprox`（*超时*，*置信度= 0.95* ）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.sumApprox)

    注意 试验在超时范围内返回总和或满足信心的近似操作。`>>> rdd  =  sc 。并行化（范围（1000 ）， 10 ）>>> - [R  =  总和（范围（1000 ））>>> ABS （RDD 。sumApprox （1000 ） -  - [R ） /  [R  <  0.05 真`


  - `take`（*num* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.take)

    采取RDD的第一个数字元素。它通过首先扫描一个分区来工作，并使用该分区的结果来估计满足限制所需的额外分区数量。从RDD中的Scala实现转换＃take（）。注意 因为所有的数据都被加载到驱动程序的内存中，所以只有当结果数组很小时才应该使用该方法。`>>> sc 。并行化（[ 2 ， 3 ， 4 ， 5 ， 6 ]） 。缓存（）。采取（2 ）[2，3] >>> sc 。并行化（[ 2 ， 3 ， 4 ， 5 ， 6 ]） 。采取（10 ）[ 2,3,4,5,6 ] >>> sc 。并行化（范围（100 ）， 100）。过滤器（lambda  x ： x  >  90 ）。采取（3 ）[91，92，93]`


  - `takeOrdered`（*num*，*key = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.takeOrdered)

    从RDD中获取N个元素，按升序排列或按可选键功能指定。注意 因为所有的数据都被加载到驱动程序的内存中，所以只有当结果数组很小时才应该使用该方法。`>>> sc 。并行化（[ 10 ， 1 ， 2 ， 9 ， 3 ， 4 ， 5 ， 6 ， 7 ]） 。takeOrdered （6 ）[1，2，3，4，5，6] >>> sc 。并行化（[ 10 ， 1 ， 2 ， 9 ， 3 ， 4 ， 5 ， 6 ， 7 ]， 2 ）。takeOrdered（6 ， key = lambda  x ： - x ）[10，9，7，6，5，4]`


  - `takeSample`（*withReplacement*，*num*，*seed = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.takeSample)

    返回此RDD的固定大小的采样子集。注意 因为所有的数据都被加载到驱动程序的内存中，所以只有当结果数组很小时才应使用该方法。`>>> rdd  =  sc 。并行化（范围（0 ， 10 ））>>> LEN （RDD 。takeSample （真， 20 ， 1 ））20 >>> LEN （RDD 。takeSample （假， 5 ， 2 ））5 >>> LEN （RDD 。takeSample （假， 15 ， 3 ））10`


  - `toDebugString`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.toDebugString)

    此RDD的描述及其用于调试的递归依赖关系。


  - `toLocalIterator`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.toLocalIterator)

    返回包含此RDD中所有元素的迭代器。迭代器将消耗与此RDD中最大分区一样多的内存。`>>> rdd  =  sc 。并行化（范围（10 ））>>> [ X  为 X  在 RDD 。toLocalIterator （）] [0,1,2,3,4,5,6,7,8,9]`


  - `top`（*num*，*key = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.top)

    从RDD获取前N个元素。注意 因为所有的数据都被加载到驱动程序的内存中，所以只有当结果数组很小时才应使用该方法。注意 它返回按降序排列的列表。`>>> sc 。并行化（[ 10 ， 4 ， 2 ， 12 ， 3 ]） 。顶部（1 ）[12] >>> sc 。并行化（[ 2 ， 3 ， 4 ， 5 ， 6 ]， 2 ）。顶部（2 ）[ 6,5 ] >>> sc 。并行化（[ 10 ， 4 ， 2 ， 12， 3 ]）。顶部（3 ， key = str ）[ 4，3，2 ]`


  - `treeAggregate`（*zeroValue*，*seqOp*，*combOp*，*depth = 2* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.treeAggregate)

    以多级树形模式聚合此RDD的元素。参数：**深度** - 建议树的深度（默认值：2）`>>> add  =  lambda  x ， y ： x  +  y >>> rdd  =  sc 。并行化（[ - 5 ， - 4 ， - 3 ， - 2 ， - 1 ， 1 ， 2 ， 3 ， 4 ]， 10 ）>>> RDD 。treeAggregate （0 ， add ， add ）-5 >>> rdd。treeAggregate （0 ， add ， add ， 1 ）-5 >>> rdd 。treeAggregate （0 ， add ， add ， 2 ）-5 >>> rdd 。treeAggregate （0 ， add ， add ， 5 ）-5 >>> rdd 。treeAggregate （0 ， add ， add ， 10 ）-5`


  - `treeReduce`（*f*，*深度= 2* ）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.treeReduce)

    以多级树形模式减少此RDD的元素。参数：**深度** - 建议树的深度（默认值：2）`>>> add  =  lambda  x ， y ： x  +  y >>> rdd  =  sc 。并行化（[ - 5 ， - 4 ， - 3 ， - 2 ， - 1 ， 1 ， 2 ， 3 ， 4 ]， 10 ）>>> RDD 。treeReduce （add ）-5 >>> rdd 。treeReduce （添加， 1 ）-5 >>> rdd 。treeReduce （add ， 2 ）-5 >>> rdd 。treeReduce （add ， 5 ）-5 >>> rdd 。treeReduce （add ， 10 ）-5`


  - `union`（*other* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.union)

    返回此RDD和另一个的联合。`>>> rdd  =  sc 。并行化（[ 1 ， 1 ， 2 ， 3 ]）>>> RDD 。工会（rdd ）。collect （）[1，1，2，3，1，1，2，3]`


  - `unpersist`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.unpersist)

    将RDD标记为非持久性，并从内存和磁盘中删除所有块。


  - `values`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.values)

    用每个元组的值返回一个RDD。`>>> m  =  sc 。并行化（[（1 ， 2 ），  （3 ， 4 ）]） 。values （）>>> m 。collect （）[2，4]`


  - `variance`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.variance)

    计算RDD元素的方差。`>>> sc 。并行化（[ 1 ， 2 ， 3 ]） 。方差（）0.666 ...`


  - `zip`（*other* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.zip)

    拉链本RDD用另一个，返回键 - 值对与在每个RDD等各RDD第二元件的第一元件假设两个RDDS具有相同数目的分区和相同数量的每个分区中的元素（例如，一个是通过另一张地图制作的）。`>>> x  =  sc 。并行化（范围（0 ，5 ））>>> ý  =  SC 。并行化（范围（1000 ， 1005 ））>>> X 。zip （y ）。collect （）[（0,1000），（1，1001），（2，1002），（3，1003），（4，1004）]`


  - `zipWithIndex`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.zipWithIndex)

    将此RDD与其元素索引一起拉伸。排序首先基于分区索引，然后是每个分区内项目的排序。因此，第一个分区中的第一个项目获取索引0，最后一个分区中的最后一个项目接收最大的索引。当此RDD包含多个分区时，此方法需要触发Spark任务。`>>> sc 。并行化（[ “a” ， “b” ， “c” ， “d” ]， 3 ）。zipWithIndex （）。collect （）[（'a'，0），（'b'，1），（'c'，2），（'d'，3）]`


  - `zipWithUniqueId`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.zipWithUniqueId)

    使用生成的独特Long ID对此RDD进行压缩。第k个分区中的项目将获得ids k，n + k，2 * n + k，...，其中n是分区数。所以可能存在差距，但这种方法不会引发火花的工作，这是不同的[`zipWithIndex`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD.zipWithIndex)`>>> sc 。并行化（[ “a” ， “b” ， “c” ， “d” ， “e” ]， 3 ）。zipWithUniqueId （）。collect （）[（'a'，0），（'b'，1），（'c'，4），（'d'，2），（'e'，5）]`


- *class* `pyspark.``StorageLevel`(*useDisk*, *useMemory*, *useOffHeap*, *deserialized*, *replication=1*)[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/storagelevel.html#StorageLevel)

  用于控制RDD存储的标志。每个StorageLevel记录是否使用内存，是否将RDD丢弃到内存不足，是否将数据保存在特定于JAVA的序列化格式的内存中，以及是否在多个节点上复制RDD分区。还包含一些常用存储级别MEMORY_ONLY的静态常量。由于数据总是在Python端序列化，所有常量都使用序列化格式。

  - `DISK_ONLY`*= StorageLevel（True，False，False，False，1）*



  - `DISK_ONLY_2`*= StorageLevel（True，False，False，False，2）*



  - `MEMORY_AND_DISK`*= StorageLevel（True，True，False，False，1）*



  - `MEMORY_AND_DISK_2`*= StorageLevel（True，True，False，False，2）*



  - `MEMORY_AND_DISK_SER`*= StorageLevel（True，True，False，False，1）*



  - `MEMORY_AND_DISK_SER_2`*= StorageLevel（True，True，False，False，2）*



  - `MEMORY_ONLY`*= StorageLevel（False，True，False，False，1）*



  - `MEMORY_ONLY_2`*= StorageLevel（False，True，False，False，2）*



  - `MEMORY_ONLY_SER`*= StorageLevel（False，True，False，False，1）*



  - `MEMORY_ONLY_SER_2`*= StorageLevel（False，True，False，False，2）*



  - `OFF_HEAP`*= StorageLevel（True，True，True，False，1）*[¶](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.StorageLevel.OFF_HEAP)


- *class* `pyspark.``Broadcast`(*sc=None*, *value=None*, *pickle_registry=None*, *path=None*)[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/broadcast.html#Broadcast)

  使用创建的广播变量[`SparkContext.broadcast()`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext.broadcast)。通过访问它的价值`value`。

  例子：

  ```
  >>> from  pyspark.context  import  SparkContext 
  >>> sc  =  SparkContext （'local' ， 'test' ）
  >>> b  =  sc 。广播（[ 1 ， 2 ， 3 ， 4 ， 5 ]）
  >>> b 。值
  [1，2，3，4，5] 
  >>> sc 。并行化（[ 0 ， 0 ]） 。flatMap （lambda  x ： b。值）。collect （）
  [1，2，3，4，5，1，2，3，4，5] 
  >>> b 。unpersist （）
  ```

  ```
  >>> large_broadcast  =  sc 。广播（范围（10000 ））
  ```

  - `destroy`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/broadcast.html#Broadcast.destroy)

    销毁与此广播变量相关的所有数据和元数据。谨慎使用这个; 一旦广播变量被销毁，它不能再被使用。此方法阻止直到销毁完成。


  - `dump`（*value*，*f* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/broadcast.html#Broadcast.dump)



  - `load`（*path* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/broadcast.html#Broadcast.load



  - `unpersist`（*blocking = False* ）[[源代码\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/broadcast.html#Broadcast.unpersist)

    在执行者上删除此广播的缓存副本。如果广播在调用之后被使用，它将需要被重新发送给每个执行者。参数：**阻止** - 是否阻止，直到未完成


  - `value`

    返回广播的值


- *class* `pyspark.``Accumulator`(*aid*, *value*, *accum_param*)[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/accumulators.html#Accumulator)

  可以累积的共享变量，即具有可交换和关联的“添加”操作。Spark集群上的工作器任务可以使用+ = 运算符将值添加到累加器，但只有驱动程序可以使用访问其值[`value`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.Accumulator.value)。工人的更新会自动传播到驱动程序。

  虽然[`SparkContext`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext)载体对累加器基本数据类型，如`int`和 `float`，用户还可以通过提供一种定制定义的自定义类型累加器 [`AccumulatorParam`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.AccumulatorParam)对象。举例来说，参考这个模块的doctest。

  - `add`（*term* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/accumulators.html#Accumulator.add)

    为此累加器的值添加一个术语


  - `value`

    获取累加器的值; 只能在驱动程序中使用


- *class* `pyspark.``AccumulatorParam`[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/accumulators.html#AccumulatorParam)

  Helper对象，用于定义如何累积给定类型的值。

  - `addInPlace`（*value1*，*value2* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/accumulators.html#AccumulatorParam.addInPlace)

    添加累加器数据类型的两个值，返回一个新值; 为了效率，也可以更新`value1`并返回它。


  - `zero`（*价值*）[[来源\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/accumulators.html#AccumulatorParam.zero)

    为该类型提供“零值”，与所提供的尺寸兼容`value`（例如，零向量）


- *class* `pyspark.``MarshalSerializer`[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/serializers.html#MarshalSerializer)

  使用Python的Marshal序列化器序列化对象：

  > <http://docs.python.org/2/library/marshal.html>

  该序列化程序比PickleSerializer更快，但支持更少的数据类型。

  - `dumps`（*obj* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/serializers.html#MarshalSerializer.dumps)



  - `loads`（*obj* ）


- *class* `pyspark.``PickleSerializer`[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/serializers.html#PickleSerializer)

  使用Python的pickle序列化器序列化对象：

  > <http://docs.python.org/2/library/pickle.html>

  这个序列化程序几乎支持任何Python对象，但可能不如更专用的序列化程序那么快。

  - `dumps`（*obj* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/serializers.html#PickleSerializer.dumps)



  - `loads`（*obj*，*encoding ='bytes'* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/serializers.html#PickleSerializer.loads)[ ¶](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.PickleSerializer.loads)


- *class* `pyspark.``StatusTracker`(*jtracker*)[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/status.html#StatusTracker)

  用于监控作业和阶段进度的低级状态报告API。

  这些API有意提供非常弱的一致性语义; 这些API的使用者应该准备好处理空的/丢失的信息。例如，作业的阶段ID可知道，但状态API可能没有关于这些阶段的细节的任何信息，所以 getStageInfo可能会返回无一个有效的关卡ID。

  为了限制内存使用量，这些API仅提供有关最近作业/阶段的信息。这些API将为最后的spark.ui.retainedStages阶段和spark.ui.retainedJobs作业提供信息 。

  - `getActiveJobsIds`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/status.html#StatusTracker.getActiveJobsIds)

    返回包含所有活动作业的ID的数组。


  - `getActiveStageIds`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/status.html#StatusTracker.getActiveStageIds)

    返回包含所有活动阶段的ID的数组。


  - `getJobIdsForGroup`（*jobGroup = None* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/status.html#StatusTracker.getJobIdsForGroup)

    返回特定作业组中所有已知作业的列表。如果 jobGroup为None，则返回所有未与作业组关联的已知作业。返回的列表可能包含正在运行的，失败的和已完成的作业，并且可能因该方法的调用而有所不同。此方法不保证结果中元素的顺序。


  - `getJobInfo`（*jobId* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/status.html#StatusTracker.getJobInfo)

    返回一个[`SparkJobInfo`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkJobInfo)对象，如果作业信息找不到或被垃圾收集，则返回None。


  - `getStageInfo`（*stageId* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/status.html#StatusTracker.getStageInfo)

    返回一个[`SparkStageInfo`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkStageInfo)对象，如果无法找到舞台信息或收集垃圾，则返回None。


- *class* `pyspark.``SparkJobInfo`[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/status.html#SparkJobInfo)

  公开有关Spark作业的信息。


- *class* `pyspark.``SparkStageInfo`[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/status.html#SparkStageInfo)

  公开有关Spark Stages的信息。


- *class* `pyspark.``Profiler`(*ctx*)[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/profiler.html#Profiler)

  注意

   

  DeveloperApi类

  PySpark支持自定义分析器，这是为了允许使用不同的分析器以及输出到不同于BasicProfiler中提供的格式。

  - 自定义分析器必须定义或继承以下方法：

    配置文件 - 将生成某种系统配置文件。统计信息 - 返回收集的统计信息。转储 - 将配置文件转储到路径添加 - 将配置文件添加到现有的累积配置文件

  在创建SparkContext时选择profiler类

  ```
  >>> from  pyspark  import  SparkConf ， SparkContext 
  >>> from  pyspark  import  BasicProfiler 
  >>> class  MyCustomProfiler （BasicProfiler ）：
  ...     def  show （self ， id ）：
  ...         print （“我的RDD自定义配置文件：％s “  ％ id ）
  ... 
  >>> conf  =  SparkConf （）。设置（“spark.python.profile” ， “true”）
  >>> sc  =  SparkContext （'local' ， 'test' ， conf = conf ， profiler_cls = MyCustomProfiler ）
  >>> sc 。并行化（范围（1000 ））。地图（拉姆达 x ： 2  *  x ）。取（10 ）
  [ 
  0,2,4,6,8,10,12,14,16,18 ] >>> sc 。并行化（范围（1000））。count （）
  1000 
  >>> sc 。show_profiles （）
  我的RDD自定义配置文件：1 
  我的RDD自定义配置文件：3 
  >>> sc 。停止（）
  ```

  - `dump`（*id*，*path* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/profiler.html#Profiler.dump)

    将配置文件转储到路径中，id是RDD标识


  - `profile`（*func* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/profiler.html#Profiler.profile)

    分析功能func


  - `show`（*id* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/profiler.html#Profiler.show)

    将配置文件统计信息打印到标准输出，id是RDD标识


  - `stats`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/profiler.html#Profiler.stats)

    返回收集的性能分析统计信息（pstats.Stats）


- *class* `pyspark.``BasicProfiler`(*ctx*)[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/profiler.html#BasicProfiler)

  BasicProfiler是默认的分析器，它是基于cProfile和Accumulator实现的

  - `profile`（*func* ）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/profiler.html#BasicProfiler.profile)

    运行并分析传入的方法to_profile。返回配置文件对象。


  - `stats`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/profiler.html#BasicProfiler.stats)[](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.BasicProfiler.stats)


- *class* `pyspark.``TaskContext`[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/taskcontext.html#TaskContext)

  > 注意 试验 

  关于可在执行期间读取或变更的任务的上下文信息。要访问正在运行的任务的TaskContext，请使用： [`TaskContext.get()`](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.TaskContext.get)。

  - `attemptNumber`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/taskcontext.html#TaskContext.attemptNumber)

    “这个任务尝试了多少次。第一个任务尝试将被分配attemptNumber = 0，并且随后的尝试将具有增加的尝试次数。


  - *classmethod* `get`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/taskcontext.html#TaskContext.get)

    返回当前活动的TaskContext。这可以在用户函数内部调用，以访问关于正在运行的任务的上下文信息。注意 必须向工人而不是司机打电话。如果未初始化，则返回None。


  - `partitionId`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/taskcontext.html#TaskContext.partitionId)

    此任务计算的RDD分区的ID。


  - `stageId`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/taskcontext.html#TaskContext.stageId)

    此任务所属阶段的ID。


  - `taskAttemptId`（）[[source\]](http://spark.apache.org/docs/latest/api/python/_modules/pyspark/taskcontext.html#TaskContext.taskAttemptId)

    对于此任务尝试唯一的标识（在同一个SparkContext中，没有两个任务尝试将共享相同的尝试标识）。这大致相当于Hadoop的TaskAttemptID。