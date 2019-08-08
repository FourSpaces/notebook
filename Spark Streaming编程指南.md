# Spark Streaming编程指南

- [概观](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#overview)
- [一个简单的例子](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#a-quick-example)
- 基本概念
  - [链接](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#linking)
  - [初始化StreamingContext](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#initializing-streamingcontext)
  - [离散流（DStreams）](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#discretized-streams-dstreams)
  - [输入DStreams和Receivers](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#input-dstreams-and-receivers)
  - [DStreams的转换](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#transformations-on-dstreams)
  - [DStreams的输出操作](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#output-operations-on-dstreams)
  - [DataFrame和SQL操作](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#dataframe-and-sql-operations)
  - [MLlib运营](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#mllib-operations)
  - [缓存/持久性](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#caching--persistence)
  - [检查点](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#checkpointing)
  - [累加器，广播变量和检查点](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#accumulators-broadcast-variables-and-checkpoints)
  - [部署应用程序](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#deploying-applications)
  - [监控应用](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#monitoring-applications)
- 性能调优
  - [减少批处理时间](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#reducing-the-batch-processing-times)
  - [设置正确的批次间隔](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#setting-the-right-batch-interval)
  - [内存调整](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#memory-tuning)
- [容错语义](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#fault-tolerance-semantics)
- [从这往哪儿走](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#where-to-go-from-here)

# 概观

Spark Streaming是核心Spark API的扩展，可实现实时数据流的可扩展，高吞吐量，容错流处理。数据可以从许多来源（如Kafka，Flume，Kinesis或TCP套接字）中提取，并且可以使用以高级函数表示的复杂算法进行处理`map`，例如`reduce`，`join`和`window`。最后，处理后的数据可以推送到文件系统，数据库和实时仪表板。实际上，您可以在数据流上应用Spark的 [机器学习](https://spark.apache.org/docs/2.1.0/ml-guide.html)和 [图形处理](https://spark.apache.org/docs/2.1.0/graphx-programming-guide.html)算法。

![Spark Streaming](https://spark.apache.org/docs/2.1.0/img/streaming-arch.png)

在内部，它的工作原理如下。Spark Streaming接收实时输入数据流并将数据分成批处理，然后由Spark引擎处理以批量生成最终结果流。

![Spark Streaming](https://spark.apache.org/docs/2.1.0/img/streaming-flow.png)

Spark Streaming提供称为*离散流*或*DStream*的高级抽象，表示连续的数据流。DStream可以从来自Kafka，Flume和Kinesis等源的输入数据流创建，也可以通过在其他DStream上应用高级操作来创建。在内部，DStream表示为一系列 [RDD](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.rdd.RDD)。

本指南向您展示如何使用DStreams开始编写Spark Streaming程序。您可以使用Scala，Java或Python编写Spark Streaming程序（在Spark 1.2中引入），所有这些都在本指南中介绍。您可以在本指南中找到标签，让您在不同语言的代码段之间进行选择。

**注意：**有一些API在Python中不同或不可用。在本指南中，您将找到标记**Python API，**突出显示这些差异。

------

# 一个简单的例子

在我们详细介绍如何编写自己的Spark Streaming程序之前，让我们快速了解一下简单的Spark Streaming程序是什么样的。假设我们想要计算从TCP套接字上监听的数据服务器接收的文本数据中的字数。您需要做的就是如下。

- [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_0)
- [**Java的**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_java_0)
- [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_0)

首先，我们将Spark Streaming类的名称和StreamingContext中的一些隐式转换导入到我们的环境中，以便将有用的方法添加到我们需要的其他类（如DStream）。[StreamingContext](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.streaming.StreamingContext)是所有流功能的主要入口点。我们使用两个执行线程创建一个本地StreamingContext，批处理间隔为1秒。

```
import org.apache.spark._
import org.apache.spark.streaming._
import org.apache.spark.streaming.StreamingContext._ // not necessary since Spark 1.3

// Create a local StreamingContext with two working thread and batch interval of 1 second.
// The master requires 2 cores to prevent from a starvation scenario.

val conf = new SparkConf().setMaster("local[2]").setAppName("NetworkWordCount")
val ssc = new StreamingContext(conf, Seconds(1))
```

使用此上下文，我们可以创建一个DStream来表示来自TCP源的流数据，指定为主机名（例如`localhost`）和端口（例如`9999`）。

```
// Create a DStream that will connect to hostname:port, like localhost:9999
val lines = ssc.socketTextStream("localhost", 9999)
```

此`lines`DStream表示将从数据服务器接收的数据流。此DStream中的每条记录都是一行文本。接下来，我们希望将空格字符分割为单词。

```
// Split each line into words
val words = lines.flatMap(_.split(" "))
```

`flatMap`是一对多DStream操作，它通过从源DStream中的每个记录生成多个新记录来创建新的DStream。在这种情况下，每行将被分成多个单词，单词流表示为 `words`DStream。接下来，我们要计算这些单词。

```
import org.apache.spark.streaming.StreamingContext._ // 从Spark 1.3开始就没有必要了
// 计算每批中的每个单词
val pairs = words.map(word => (word, 1))
val wordCounts = pairs.reduceByKey(_ + _)

// 将此DStream中生成的每个RDD的前十个元素打印到控制台
wordCounts.print()
```

所述`words`DSTREAM被进一步映射（一到一个变换）到一个DSTREAM `(word, 1)`对，然后将其还原得到的单词的频率数据中的每一批。最后，`wordCounts.print()`将打印每秒生成的一些计数。

请注意，执行这些行时，Spark Streaming仅设置它在启动时将执行的计算，并且尚未启动实际处理。要在设置完所有转换后开始处理，我们最终调用

```
ssc.start()             // 开始计算
ssc.awaitTermination()  // 等待计算终止
```

完整的代码可以在Spark Streaming示例 [NetworkWordCount中找到](https://github.com/apache/spark/blob/v2.1.0/examples/src/main/scala/org/apache/spark/examples/streaming/NetworkWordCount.scala)。 

如果您已经[下载](https://spark.apache.org/docs/2.1.0/index.html#downloading)并[构建了](https://spark.apache.org/docs/2.1.0/index.html#building) Spark，则可以按如下方式运行此示例。您首先需要使用Netcat（在大多数类Unix系统中找到的小实用程序）作为数据服务器运行

```
$ nc -lk 9999
```

然后，在不同的终端中，您可以使用启动示例

- [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_1)
- [**Java的**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_java_1)
- [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_1)

```
$ ./bin/run-example streaming.NetworkWordCount localhost 9999
```

然后，在运行netcat服务器的终端中键入的任何行将被计数并每秒在屏幕上打印。它看起来像下面这样。

| `# TERMINAL 1: # Running Netcat  $ nc -lk 9999  hello world    ...` |      | [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_2)[**Java的**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_java_2)[**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_2)`# TERMINAL 2: RUNNING NetworkWordCount  $ ./bin/run-example streaming.NetworkWordCount localhost 9999 ... ------------------------------------------- Time: 1357008430000 ms ------------------------------------------- (hello,1) (world,1) ...` |
| ------------------------------------------------------------ | ---- | ------------------------------------------------------------ |
|                                                              |      |                                                              |

------

------

# 基本概念

接下来，我们将超越简单的示例，详细介绍Spark Streaming的基础知识。

## 链接

与Spark类似，Spark Streaming可通过Maven Central获得。要编写自己的Spark Streaming程序，必须将以下依赖项添加到SBT或Maven项目中。

- [**Maven的**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_Maven_3)
- [**SBT**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_SBT_3)

```
<dependency>
    <groupId>org.apache.spark</groupId>
    <artifactId>spark-streaming_2.11</artifactId>
    <version>2.1.0</version>
</dependency>
```

要从Kafka，Flume和Kinesis等源中提取Spark Streaming核心API中不存在的数据，您必须将相应的工件添加`spark-streaming-xyz_2.11`到依赖项中。例如，一些常见的如下。

| 资源     | 神器                                                |
| -------- | --------------------------------------------------- |
| 卡夫卡   | 火花流 - 卡夫卡0-8_2.11                             |
| 水槽     | 火花流，flume_2.11                                  |
| 室壁运动 | spark-streaming-kinesis-asl_2.11 [亚马逊软件许可证] |
|          |                                                     |

有关最新列表，请参阅 [Maven存储库](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22org.apache.spark%22%20AND%20v%3A%222.1.0%22) 以获取受支持的源和工件的完整列表。

------

## 初始化StreamingContext

要初始化Spark Streaming程序，必须创建一个**StreamingContext**对象，它是所有Spark Streaming功能的主要入口点。

- [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_4)
- [**Java的**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_java_4)
- [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_4)

甲[的StreamingContext](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.streaming.StreamingContext)对象可以从被创建[SparkConf](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.SparkConf)对象。

```
import org.apache.spark._
import org.apache.spark.streaming._

val conf = new SparkConf().setAppName(appName).setMaster(master)
val ssc = new StreamingContext(conf, Seconds(1))
```

该`appName`参数是应用程序在集群UI上显示的名称。 `master`是[Spark，Mesos或YARN群集URL](https://spark.apache.org/docs/2.1.0/submitting-applications.html#master-urls)，或在本地模式下运行的特殊**“local [\*]”**字符串。实际上，当在群集上运行时，您不希望`master`在程序中进行硬编码，而是[启动应用程序`spark-submit`](https://spark.apache.org/docs/2.1.0/submitting-applications.html)并在那里接收它。但是，对于本地测试和单元测试，您可以传递“local [*]”以在进程中运行Spark Streaming（检测本地系统中的核心数）。请注意，这会在内部创建一个[SparkContext](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.SparkContext)（所有Spark功能的起点），可以作为`ssc.sparkContext`。

必须根据应用程序的延迟要求和可用的群集资源设置批处理间隔。有关 更多详细信息，请参见[性能调整](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#setting-the-right-batch-interval)部分。

甲`StreamingContext`目的还可以从现有的创建的`SparkContext`对象。

```
import org.apache.spark.streaming._

val sc = ...                // existing SparkContext
val ssc = new StreamingContext(sc, Seconds(1))
```

定义上下文后，您必须执行以下操作。

1. 通过创建输入DStreams来定义输入源。
2. 通过将转换和输出操作应用于DStream来定义流式计算。
3. 开始接收数据并使用它进行处理`streamingContext.start()`。
4. 等待处理停止（手动或由于任何错误）使用`streamingContext.awaitTermination()`。
5. 可以使用手动停止处理`streamingContext.stop()`。

##### 要记住的要点：

- 一旦启动了上下文，就不能设置或添加新的流式计算。
- 上下文停止后，无法重新启动。
- 在JVM中只能同时激活一个StreamingContext。
- StreamingContext上的stop（）也会停止SparkContext。要仅停止StreamingContext，请将`stop()`called 的可选参数设置`stopSparkContext`为false。
- 只要在创建下一个StreamingContext之前停止前一个StreamingContext（不停止SparkContext），就可以重复使用SparkContext创建多个StreamingContexts。

------

## 离散流（DStreams）

**Discretized Stream**或**DStream**是Spark Streaming提供的基本抽象。它表示连续的数据流，可以是从源接收的输入数据流，也可以是通过转换输入流生成的已处理数据流。在内部，DStream由一系列连续的RDD表示，这是Spark对不可变分布式数据集的抽象（有关更多详细信息，请参阅[Spark编程指南](https://spark.apache.org/docs/2.1.0/programming-guide.html#resilient-distributed-datasets-rdds)）。DStream中的每个RDD都包含来自特定时间间隔的数据，如下图所示。

![Spark Streaming](https://spark.apache.org/docs/2.1.0/img/streaming-dstream.png)

应用于DStream的任何操作都转换为底层RDD上的操作。例如，在[先前](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#a-quick-example)将行流转换为单词的[示例](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#a-quick-example)中，`flatMap`操作应用于`lines`DStream中的每个RDD 以生成DStream的 `words`RDD。如下图所示。

![Spark Streaming](https://spark.apache.org/docs/2.1.0/img/streaming-dstream-ops.png)

这些底层RDD转换由Spark引擎计算。DStream操作隐藏了大部分细节，并为开发人员提供了更高级别的API以方便使用。这些操作将在后面的章节中详细讨论。

------

## 输入DStreams和Receivers

输入DStream是表示从流源接收的输入数据流的DStream。在[快速示例中](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#a-quick-example)，`lines`输入DStream是表示从netcat服务器接收的数据流。每个输入DStream（文件流除外，本节稍后讨论）都与**Receiver** （[Scala doc](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.streaming.receiver.Receiver)， [Java doc](https://spark.apache.org/docs/2.1.0/api/java/org/apache/spark/streaming/receiver/Receiver.html)）对象相关联，该对象从源接收数据并将其存储在Spark的内存中进行处理。

Spark Streaming提供两类内置流媒体源。

- *基本来源*：StreamingContext API中直接提供的*源*。示例：文件系统和套接字连接。
- *高级资源*：Kafka，Flume，Kinesis等资源可通过额外的实用程序类获得。这些需要链接额外的依赖关系，如 [链接](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#linking)部分所述。

我们将在本节后面讨论每个类别中的一些来源。

请注意，如果要在流应用程序中并行接收多个数据流，可以创建多个输入DStream（在“ [性能调整”](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#level-of-parallelism-in-data-receiving)部分中进一步讨论）。这将创建多个接收器，这些接收器将同时接收多个数据流。但请注意，Spark worker / executor是一个长期运行的任务，因此它占用了分配给Spark Streaming应用程序的其中一个核心。因此，重要的是要记住，Spark Streaming应用程序需要分配足够的内核（或线程，如果在本地运行）来处理接收的数据，以及运行接收器。

##### 要记住的要点

- 在本地运行Spark Streaming程序时，请勿使用“local”或“local [1]”作为主URL。这两种方法都意味着只有一个线程将用于本地运行任务。如果您正在使用基于接收器的输入DStream（例如套接字，Kafka，Flume等），那么将使用单个线程来运行接收器，而不留下用于处理接收数据的线程。因此，在本地运行时，始终使用“local [ *n* ]”作为主URL，其中*n* >要运行的接收器数量（有关如何设置主服务器的信息，请参阅[Spark属性](https://spark.apache.org/docs/2.1.0/configuration.html#spark-properties)）。
- 将逻辑扩展到在集群上运行时，分配给Spark Streaming应用程序的核心数必须大于接收器数。否则系统将接收数据，但无法处理数据。

### 基本来源

我们已经`ssc.socketTextStream(...)`在[快速示例](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#a-quick-example) 中查看了通过TCP套接字连接接收的文本数据创建DStream的[示例](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#a-quick-example)。除了套接字之外，StreamingContext API还提供了从文件创建DStream作为输入源的方法。

- **文件流：**用于从与HDFS API兼容的任何文件系统（即HDFS，S3，NFS等）上的文件读取数据，可以将DStream创建为：

  - [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_5)
  - [**Java的**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_java_5)
  - [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_5)

  ```
    streamingContext.fileStream[KeyClass, ValueClass, InputFormatClass](dataDirectory)
  ```

  Spark Streaming将监视目录`dataDirectory`并处理在该目录中创建的任何文件（不支持嵌套目录中写入的文件）。注意

  - 文件必须具有相同的数据格式。
  - 这些文件必须在创建`dataDirectory`通过原子*移动*或*重命名*他们到数据目录。
  - 移动后，不得更改文件。因此，如果连续追加文件，则不会读取新数据。

  对于简单的文本文件，有一种更简单的方法`streamingContext.textFileStream(dataDirectory)`。并且文件流不需要运行接收器，因此不需要分配核心。

  **Python API** `fileStream`中没有Python API，只有	`textFileStream`可用。

- **基于自定义接收器的流：**可以使用通过自定义接收器接收的数据流创建DStream。有关更多详细信息，请参阅[自定义接收器指南](https://spark.apache.org/docs/2.1.0/streaming-custom-receivers.html)

- **将RDD作为流队列：**为了使用测试数据测试Spark Streaming应用程序，还可以使用基于RDD队列创建DStream `streamingContext.queueStream(queueOfRDDs)`。推入队列的每个RDD将被视为DStream中的一批数据，并像流一样处理。

有关从套接字和文件流的详细信息，请参阅在相关函数的API单证 [的StreamingContext](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.streaming.StreamingContext)斯卡拉，[JavaStreamingContext](https://spark.apache.org/docs/2.1.0/api/java/index.html?org/apache/spark/streaming/api/java/JavaStreamingContext.html) 对Java和[的StreamingContext](https://spark.apache.org/docs/2.1.0/api/python/pyspark.streaming.html#pyspark.streaming.StreamingContext)为Python。

### 高级资源

**Python API**从Spark 2.1.0开始，在这些源代码中，Kafka，Kinesis和Flume在Python API中可用。

此类源需要与外部非Spark库连接，其中一些库具有复杂的依赖性（例如，Kafka和Flume）。因此，为了最大限度地减少与依赖项版本冲突相关的问题，从这些源创建DStream的功能已移至可在必要时显式[链接的](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#linking)单独库。

请注意，Spark shell中不提供这些高级源，因此无法在shell中测试基于这些高级源的应用程序。如果您真的想在Spark shell中使用它们，则必须下载相应的Maven工件JAR及其依赖项，并将其添加到类路径中。

其中一些先进的来源如下。

- **Kafka：** Spark Streaming 2.1.0与Kafka经纪人版本0.8.2.1或更高版本兼容。有关更多详细信息，请参阅[Kafka集成指南](https://spark.apache.org/docs/2.1.0/streaming-kafka-integration.html)。
- **Flume：** Spark Streaming 2.1.0与Flume 1.6.0兼容。有关详细信息，请参阅[Flume集成指南](https://spark.apache.org/docs/2.1.0/streaming-flume-integration.html)。
- **Kinesis：** Spark Streaming 2.1.0与Kinesis Client Library 1.2.1兼容。有关详细信息，请参阅[Kinesis集成指南](https://spark.apache.org/docs/2.1.0/streaming-kinesis-integration.html)。

### 自定义来源

**Python API Python**尚不支持此功能。

输入DStream也可以从自定义数据源创建。您所要做的就是实现一个用户定义的**接收器**（参见下一节以了解它是什么），它可以从自定义源接收数据并将其推送到Spark。有关详细信息，请参阅[自定义接收器指南](https://spark.apache.org/docs/2.1.0/streaming-custom-receivers.html)

### 接收器可靠性

根据其*可靠性，*可以有两种数据源。来源（如Kafka和Flume）允许传输数据得到确认。如果从这些*可靠*来源接收数据的系统正确地确认接收到的数据，则可以确保不会因任何类型的故障而丢失数据。这导致两种接收器：

1. *可靠的接收器* - *可靠的接收器*在接收到数据并将其存储在带复制的Spark中时，正确地将确认发送到可靠的源。
2. *不可靠的接收器* -一个*不可靠的接收器*并*没有*发送确认的资源等。这可以用于不支持确认的源，甚至可以用于不需要或需要进入确认复杂性的可靠源。

“ [自定义接收器指南”](https://spark.apache.org/docs/2.1.0/streaming-custom-receivers.html)中讨论了如何编写可靠接收器的详细信息 。

------

## DStreams的转换

与RDD类似，转换允许修改来自输入DStream的数据。DStreams支持普通Spark RDD上可用的许多转换。一些常见的如下。

| 转型                                       | 含义                                                         |
| ------------------------------------------ | ------------------------------------------------------------ |
| **map**（*功能*）                          | 通过将源DStream的每个元素传递给函数*func来*返回一个新的DStream 。 |
| **flatMap**（*func*）                      | 与map类似，但每个输入项可以映射到0个或更多输出项。           |
| **过滤器**（*功能*）                       | 通过仅选择*func*返回true 的源DStream的记录来返回新的DStream 。 |
| **重新分配**（*numPartitions*）            | 通过创建更多或更少的分区来更改此DStream中的并行度级别。      |
| **union**（*otherStream*）                 | 返回一个新的DStream，它包含源DStream和*otherDStream中*元素的并 *集*。 |
| **count**（）                              | 通过计算源DStream的每个RDD中的元素数量，返回单元素RDD的新DStream。 |
| **减少**（*功能*）                         | 通过使用函数*func*（它接受两个参数并返回一个）聚合源DStream的每个RDD中的元素，返回单元素RDD的新DStream 。该函数应该是关联的和可交换的，以便可以并行计算。 |
| **countByValue**（）                       | 当在类型为K的元素的DStream上调用时，返回（K，Long）对的新DStream，其中每个键的值是其在源DStream的每个RDD中的频率。 |
| **reduceByKey**（*func*，[*numTasks* ]）   | 当在（K，V）对的DStream上调用时，返回（K，V）对的新DStream，其中使用给定的reduce函数聚合每个键的值。**注意：**默认情况下，这使用Spark的默认并行任务数（本地模式为2，在群集模式下，数量由config属性确定`spark.default.parallelism`）进行分组。您可以传递可选`numTasks`参数来设置不同数量的任务。 |
| **join**（*otherStream*，[ *numTasks*]）   | 当在（K，V）和（K，W）对的两个DStream上调用时，返回（K，（V，W））对的新DStream与每个键的所有元素对。 |
| **协同组**（*otherStream*，[*numTasks* ]） | 当在（K，V）和（K，W）对的DStream上调用时，返回（K，Seq [V]，Seq [W]）元组的新DStream。 |
| **变换**（*功能*）                         | 通过将RDD-to-RDD函数应用于源DStream的每个RDD来返回新的DStream。这可以用于在DStream上执行任意RDD操作。 |
| **updateStateByKey**（*func*）             | 返回一个新的“状态”DStream，其中通过在键的先前状态和键的新值上应用给定函数来更新每个键的状态。这可用于维护每个密钥的任意状态数据。 |
|                                            |                                                              |

其中一些转换值得更详细地讨论。

#### UpdateStateByKey操作

该`updateStateByKey`操作允许您在使用新信息不断更新时保持任意状态。要使用它，您必须执行两个步骤。

1. 定义状态 - 状态可以是任意数据类型。
2. 定义状态更新功能 - 使用函数指定如何使用先前状态和输入流中的新值更新状态。

在每个批处理中，Spark都会对所有现有密钥应用状态更新功能，无论它们是否在批处理中都有新数据。如果更新函数返回，`None`则将删除键值对。

让我们举一个例子来说明这一点。假设您要维护文本数据流中看到的每个单词的运行计数。这里，运行计数是状态，它是一个整数。我们将更新功能定义为：

- [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_6)
- [**Java的**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_java_6)
- [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_6)

```
def updateFunction(newValues: Seq[Int], runningCount: Option[Int]): Option[Int] = {
    val newCount = ...  // add the new values with the previous running count to get the new count
    Some(newCount)
}
```

这适用于包含单词的DStream（例如，[前面示例中](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#a-quick-example)`pairs`包含DStream `(word, 1)`的[对象](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#a-quick-example)）。

```
val runningCounts = pairs.updateStateByKey[Int](updateFunction _)
```

将为每个单词调用更新函数，`newValues`其序列为1（来自`(word, 1)`成对）并`runningCount`具有前一个计数。

请注意，使用`updateStateByKey`需要配置检查点目录，这将在[检查点](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#checkpointing)部分中详细讨论。

#### 变换操作

该`transform`操作（及其变体`transformWith`）允许在DStream上应用任意RDD到RDD功能。它可用于应用未在DStream API中公开的任何RDD操作。例如，将数据流中的每个批次与另一个数据集连接的功能不会直接在DStream API中公开。但是，您可以轻松地使用它`transform`来执行此操作。这使得非常强大的可能性。例如，可以通过将输入数据流与预先计算的垃圾邮件信息（也可以使用Spark生成）连接，然后根据它进行过滤，来进行实时数据清理。

- [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_7)
- [**Java的**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_java_7)
- [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_7)

```
val spamInfoRDD = ssc.sparkContext.newAPIHadoopRDD(...) // RDD containing spam information

val cleanedDStream = wordCounts.transform { rdd =>
  rdd.join(spamInfoRDD).filter(...) // join data stream with spam information to do data cleaning
  ...
}
```

请注意，在每个批处理间隔中都会调用提供的函数。这允许您进行时变RDD操作，即RDD操作，分区数，广播变量等可以在批次之间进行更改。

#### 窗口操作

Spark Streaming还提供*窗口计算*，允许您在滑动数据窗口上应用转换。下图说明了此滑动窗口。

![Spark Streaming](https://spark.apache.org/docs/2.1.0/img/streaming-dstream-window.png)

如该图所示，每一个窗口时间*的幻灯片*在源DSTREAM，落入窗口内的源RDDS被组合及操作，以产生加窗DSTREAM的RDDS。在这种特定情况下，操作应用于最后3个时间单位的数据，并按2个时间单位滑动。这表明任何窗口操作都需要指定两个参数。

- *窗口长度* - *窗口*的持续时间（图中的3）。
- *滑动间隔* - 执行窗口操作的间隔（图中的2）。

这两个参数必须是源DStream的批处理间隔的倍数（图中的1）。

让我们用一个例子来说明窗口操作。比如说，您希望通过每隔10秒生成最后30秒数据的字数来扩展 [前面的示例](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#a-quick-example)。为此，我们必须在最后30秒的数据`reduceByKey`上对`pairs`DStream `(word, 1)`对应用操作。这是使用该操作完成的`reduceByKeyAndWindow`。

- [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_8)
- [**Java的**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_java_8)
- [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_8)

```
// Reduce last 30 seconds of data, every 10 seconds
val windowedWordCounts = pairs.reduceByKeyAndWindow((a:Int,b:Int) => (a + b), Seconds(30), Seconds(10))
```

一些常见的窗口操作如下。所有这些操作都采用上述两个参数 - *windowLength*和*slideInterval*。

| 转型                                                         | 含义                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **window**（*windowLength*，*slideInterval*）                | 返回一个新的DStream，它是根据源DStream的窗口批次计算的。     |
| **countByWindow**（*windowLength*，*slideInterval*）         | 返回流中元素的滑动窗口数。                                   |
| **reduceByWindow**（*func*，*windowLength*，*slideInterval*） | 返回一个新的单元素流，通过使用*func*在滑动间隔内聚合流中的元素而创建。该函数应该是关联的和可交换的，以便可以并行正确计算。 |
| **reduceByKeyAndWindow**（*func*，*windowLength*，*slideInterval*，[ *numTasks* ]） | 当在（K，V）对的DStream上调用时，返回（K，V）对的新DStream，其中使用给定的reduce函数*func* 在滑动窗口中的批次聚合每个键的值。**注意：**默认情况下，这使用Spark的默认并行任务数（本地模式为2，在群集模式下，数量由config属性确定`spark.default.parallelism`）进行分组。您可以传递可选 `numTasks`参数来设置不同数量的任务。 |
| **reduceByKeyAndWindow**（*func*，*invFunc*，*windowLength*，*slideInterval*，[ *numTasks* ]） | 上述更有效的版本，`reduceByKeyAndWindow()`其中使用前一窗口的reduce值逐步计算每个窗口的reduce值。这是通过减少进入滑动窗口的新数据和“反向减少”离开窗口的旧数据来完成的。一个例子是当窗口滑动时“添加”和“减去”键的计数。但是，它仅适用于“可逆减少函数”，即那些具有相应“反向减少”函数的减函数（作为参数*invFunc*）。同样`reduceByKeyAndWindow`，reduce任务的数量可通过可选参数进行配置。请注意，必须启用[检查点](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#checkpointing)才能使用此操作。 |
| **countByValueAndWindow**（*windowLength*， *slideInterval*，[*numTasks* ]） | 当在（K，V）对的DStream上调用时，返回（K，Long）对的新DStream，其中每个键的值是其在滑动窗口内的频率。同样 `reduceByKeyAndWindow`，reduce任务的数量可通过可选参数进行配置。 |
|                                                              |                                                              |

#### 加入运营

最后，值得强调的是，您可以轻松地在Spark Streaming中执行不同类型的连接。

##### 流连接

Streams可以很容易地与其他流连接。

- [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_9)
- [**Java的**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_java_9)
- [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_9)

```
val stream1: DStream[String, String] = ...
val stream2: DStream[String, String] = ...
val joinedStream = stream1.join(stream2)
```

这里，在每个批处理间隔中，生成的RDD `stream1`将与生成的RDD连接`stream2`。你也可以做`leftOuterJoin`，`rightOuterJoin`，`fullOuterJoin`。此外，在流的窗口上进行连接通常非常有用。这也很容易。

- [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_10)
- [**Java的**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_java_10)
- [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_10)

```
val windowedStream1 = stream1.window(Seconds(20))
val windowedStream2 = stream2.window(Minutes(1))
val joinedStream = windowedStream1.join(windowedStream2)
```

##### 流数据集连接

在解释`DStream.transform`操作时已经显示了这一点。这是将窗口流与数据集连接的另一个示例。

- [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_11)
- [**Java的**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_java_11)
- [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_11)

```
val dataset: RDD[String, String] = ...
val windowedStream = stream.window(Seconds(20))...
val joinedStream = windowedStream.transform { rdd => rdd.join(dataset) }
```

实际上，您还可以动态更改要加入的数据集。提供给的函数在`transform`每个批处理间隔进行评估，因此将使用`dataset`引用指向的当前数据集。

API文档中提供了完整的DStream转换列表。对于Scala API，请参阅[DStream](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.streaming.dstream.DStream) 和[PairDStreamFunctions](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.streaming.dstream.PairDStreamFunctions)。对于Java API，请参阅[JavaDStream](https://spark.apache.org/docs/2.1.0/api/java/index.html?org/apache/spark/streaming/api/java/JavaDStream.html) 和[JavaPairDStream](https://spark.apache.org/docs/2.1.0/api/java/index.html?org/apache/spark/streaming/api/java/JavaPairDStream.html)。对于Python API，请参阅[DStream](https://spark.apache.org/docs/2.1.0/api/python/pyspark.streaming.html#pyspark.streaming.DStream)。

------

## DStreams的输出操作

输出操作允许将DStream的数据推送到外部系统，如数据库或文件系统。由于输出操作实际上允许外部系统使用转换后的数据，因此它们会触发所有DStream转换的实际执行（类似于RDD的操作）。目前，定义了以下输出操作：

| 输出操作                                    | 含义                                                         |
| ------------------------------------------- | ------------------------------------------------------------ |
| **print**（）                               | 在运行流应用程序的驱动程序节点上打印DStream中每批数据的前十个元素。这对开发和调试很有用。  **Python API**这在**Python API**中称为 **pprint（）**。 |
| **saveAsTextFiles**（*前缀*，[ *后缀* ]）   | 将此DStream的内容保存为文本文件。每个批处理间隔的文件名基于*前缀*和*后缀*生成：*“prefix-TIME_IN_MS [.suffix]”*。 |
| **saveAsObjectFiles**（*前缀*，[ *后缀* ]） | 将此DStream的内容保存为`SequenceFiles`序列化Java对象。每个批处理间隔的文件名基于*前缀*和 *后缀*生成：*“prefix-TIME_IN_MS [.suffix]”*。  **Python API**这在Python API中不可用。 |
| **saveAsHadoopFiles**（*前缀*，[ *后缀* ]） | 将此DStream的内容保存为Hadoop文件。每个批处理间隔的文件名基于*前缀*和*后缀*生成：*“prefix-TIME_IN_MS [.suffix]”*。  **Python API**这在Python API中不可用。 |
| **foreachRDD**（*func*）                    | 最通用的输出运算符，它将函数*func*应用于从流生成的每个RDD。此函数应将每个RDD中的数据推送到外部系统，例如将RDD保存到文件，或通过网络将其写入数据库。请注意，函数*func*在运行流应用程序的驱动程序进程中执行，并且通常会在其中执行RDD操作，这将强制计算流式RDD。 |
|                                             |                                                              |

### 使用foreachRDD的设计模式

`dstream.foreachRDD`是一个功能强大的原语，允许将数据发送到外部系统。但是，了解如何正确有效地使用此原语非常重要。一些常见的错误要避免如下。

通常将数据写入外部系统需要创建连接对象（例如，与远程服务器的TCP连接）并使用它将数据发送到远程系统。为此，开发人员可能无意中尝试在Spark驱动程序中创建连接对象，然后尝试在Spark工作程序中使用它来保存RDD中的记录。例如（在Scala中），

- [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_12)
- [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_12)

```
dstream.foreachRDD { rdd =>
  val connection = createNewConnection()  // executed at the driver
  rdd.foreach { record =>
    connection.send(record) // executed at the worker
  }
}
```

这是不正确的，因为这需要连接对象被序列化并从驱动程序发送到worker。这种连接对象很少跨机器传输。此错误可能表现为序列化错误（连接对象不可序列化），初始化错误（需要在worker处初始化连接对象）等。正确的解决方案是在worker处创建连接对象。

但是，这可能会导致另一个常见错误 - 为每条记录创建一个新连接。例如，

- [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_13)
- [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_13)

```
dstream.foreachRDD { rdd =>
  rdd.foreach { record =>
    val connection = createNewConnection()
    connection.send(record)
    connection.close()
  }
}
```

通常，创建连接对象会产生时间和资源开销。因此，为每个记录创建和销毁连接对象可能会产生不必要的高开销，并且可能显着降低系统的总吞吐量。更好的解决方案是使用 **`rdd.foreachPartition`- 创建单个连接对象并使用该连接发送RDD分区中的所有记录。**

- [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_14)
- [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_14)

```
dstream.foreachRDD { rdd =>
  rdd.foreachPartition { partitionOfRecords =>
    val connection = createNewConnection()
    partitionOfRecords.foreach(record => connection.send(record))
    connection.close()
  }
}
```

这会分摊许多记录的连接创建开销。

最后，通过在多个RDD /批处理中重用连接对象，可以进一步优化这一点。由于多个批次的RDD被推送到外部系统，因此可以维护连接对象的静态池，而不是可以重用的连接对象，从而进一步减少了开销。

- [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_15)
- [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_15)

```
dstream.foreachRDD { rdd =>
  rdd.foreachPartition { partitionOfRecords =>
    // ConnectionPool is a static, lazily initialized pool of connections
    val connection = ConnectionPool.getConnection()
    partitionOfRecords.foreach(record => connection.send(record))
    ConnectionPool.returnConnection(connection)  // return to the pool for future reuse
  }
}
```

请注意，池中的连接应根据需要延迟创建，如果暂时不使用，则会超时。这实现了最有效的数据发送到外部系统。

##### 要记住的其他要点：

- DStreams由输出操作延迟执行，就像RDD由RDD操作延迟执行一样。具体而言，DStream输出操作中的RDD操作会强制处理接收到的数据。因此，如果您的应用程序没有任何输出操作，或者输出操作`dstream.foreachRDD()`没有任何RDD操作，那么就不会执行任何操作。系统将简单地接收数据并将其丢弃。
- 默认情况下，输出操作一次执行一次。它们按照应用程序中定义的顺序执行。

------

## DataFrame和SQL操作

您可以轻松地对流数据使用[DataFrames和SQL](https://spark.apache.org/docs/2.1.0/sql-programming-guide.html)操作。您必须使用StreamingContext正在使用的SparkContext创建SparkSession。此外，必须这样做，以便可以在驱动器故障时重新启动。这是通过创建一个延迟实例化的SparkSession单例实例来完成的。这在以下示例中显示。它修改了早期的[单词计数示例，](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#a-quick-example)以使用DataFrames和SQL生成单词计数。每个RDD都转换为DataFrame，注册为临时表，然后使用SQL进行查询。

- [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_16)
- [**Java的**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_java_16)
- [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_16)

```
/** DataFrame operations inside your streaming program */

val words: DStream[String] = ...

words.foreachRDD { rdd =>

  // Get the singleton instance of SparkSession
  val spark = SparkSession.builder.config(rdd.sparkContext.getConf).getOrCreate()
  import spark.implicits._

  // Convert RDD[String] to DataFrame
  val wordsDataFrame = rdd.toDF("word")

  // Create a temporary view
  wordsDataFrame.createOrReplaceTempView("words")

  // Do word count on DataFrame using SQL and print it
  val wordCountsDataFrame = 
    spark.sql("select word, count(*) as total from words group by word")
  wordCountsDataFrame.show()
}
```

查看完整的[源代码](https://github.com/apache/spark/blob/v2.1.0/examples/src/main/scala/org/apache/spark/examples/streaming/SqlNetworkWordCount.scala)。

您还可以对从不同线程（即，与正在运行的StreamingContext异步）的流数据上定义的表运行SQL查询。只需确保将StreamingContext设置为记住足够数量的流数据，以便查询可以运行。否则，不知道任何异步SQL查询的StreamingContext将在查询完成之前删除旧的流数据。例如，如果要查询最后一批，但查询可能需要5分钟才能运行，则调用`streamingContext.remember(Minutes(5))`（在Scala中，或在其他语言中等效）。

有关[DataFrame的](https://spark.apache.org/docs/2.1.0/sql-programming-guide.html)详细信息，请参阅[DataFrames和SQL](https://spark.apache.org/docs/2.1.0/sql-programming-guide.html)指南。

------

## MLlib运营

您还可以轻松使用[MLlib](https://spark.apache.org/docs/2.1.0/ml-guide.html)提供的机器学习算法。首先，有流媒体机器学习算法（例如[流媒体线性回归](https://spark.apache.org/docs/2.1.0/mllib-linear-methods.html#streaming-linear-regression)，[流媒体KMeans](https://spark.apache.org/docs/2.1.0/mllib-clustering.html#streaming-k-means)等），它们可以同时学习流数据以及将模型应用于流数据。除此之外，对于更大类的机器学习算法，您可以离线学习学习模型（即使用历史数据），然后在线将数据应用于流数据。有关详细信息，请参阅[MLlib](https://spark.apache.org/docs/2.1.0/ml-guide.html)指南。

------

## 缓存/持久性

与RDD类似，DStreams还允许开发人员将流的数据保存在内存中。也就是说，`persist()`在DStream上使用该方法会自动将该DStream的每个RDD保留在内存中。如果DStream中的数据将被多次计算（例如，对相同数据进行多次操作），这将非常有用。对于像`reduceByWindow`和这样的基于窗口的操作和 `reduceByKeyAndWindow`基于状态的操作`updateStateByKey`，这是隐含的。因此，基于窗口的操作生成的DStream会自动保留在内存中，而无需开发人员调用`persist()`。

对于通过网络接收数据的输入流（例如，Kafka，Flume，套接字等），默认持久性级别设置为将数据复制到两个节点以实现容错。

请注意，与RDD不同，DStreams的默认持久性级别会将数据序列化为内存。“ [性能调整”](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#memory-tuning)部分对此进行了进一步讨论。有关不同持久性级别的更多信息，请参阅“ [Spark编程指南”](https://spark.apache.org/docs/2.1.0/programming-guide.html#rdd-persistence)。

------

## 检查点

流应用程序必须全天候运行，因此必须能够适应与应用程序逻辑无关的故障（例如，系统故障，JVM崩溃等）。为了实现这一点，Spark Streaming需要将足够的信息*检查*到容错存储系统，以便它可以从故障中恢复。检查点有两种类型的数据。

- 元数据检查点

   \- 将定义流式计算的信息保存到容错存储（如HDFS）。这用于从运行流应用程序的驱动程序的节点的故障中恢复（稍后详细讨论）。元数据包括：

  - *配置* - 用于创建流应用程序的配置。
  - *DStream操作* - 定义流应用程序的DStream操作集。
  - *不完整的批次* - 其工作排队但尚未完成的批次。

- *数据检查点* - 将生成的RDD保存到可靠的存储。在一些跨多个批次组合数据的*有状态*转换中，这是必需的。在这种转换中，生成的RDD依赖于先前批次的RDD，这导致依赖关系链的长度随时间增加。为了避免恢复时间的这种无限增加（与依赖链成比例），有状态变换的中间RDD周期性地*检查点*到可靠存储（例如HDFS）以切断依赖链。

总而言之，元数据检查点主要用于从驱动程序故障中恢复，而如果使用状态转换，即使对于基本功能也需要数据或RDD检查点。

#### 何时启用检查点

必须为具有以下任何要求的应用程序启用检查点：

- *有状态转换的用法* - 如果在应用程序中使用了（`updateStateByKey`或`reduceByKeyAndWindow`使用反函数），则必须提供检查点目录以允许定期RDD检查点。
- *从运行应用程序的驱动程序的故障中恢复* - 元数据检查点用于使用进度信息进行恢复。

请注意，可以在不启用检查点的情况下运行没有上述有状态转换的简单流应用程序。在这种情况下，驱动程序故障的恢复也将是部分的（某些已接收但未处理的数据可能会丢失）。这通常是可以接受的，并且许多以这种方式运行Spark Streaming应用程序。预计对非Hadoop环境的支持将在未来得到改善。

#### 如何配置检查点

可以通过在容错，可靠的文件系统（例如，HDFS，S3等）中设置目录来启用检查点，检查点信息将保存到该文件系统中。这是通过使用完成的`streamingContext.checkpoint(checkpointDirectory)`。这将允许您使用上述有状态转换。此外，如果要使应用程序从驱动程序故障中恢复，则应重写流应用程序以使其具有以下行为。

- 当程序第一次启动时，它将创建一个新的StreamingContext，设置所有流然后调用start（）。
- 当程序在失败后重新启动时，它将从检查点目录中的检查点数据重新创建StreamingContext。

- [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_17)
- [**Java的**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_java_17)
- [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_17)

使用此行为变得简单`StreamingContext.getOrCreate`。其用法如下。

```
// Function to create and setup a new StreamingContext
def functionToCreateContext(): StreamingContext = {
  val ssc = new StreamingContext(...)   // new context
  val lines = ssc.socketTextStream(...) // create DStreams
  ...
  ssc.checkpoint(checkpointDirectory)   // set checkpoint directory
  ssc
}

// Get StreamingContext from checkpoint data or create a new one
val context = StreamingContext.getOrCreate(checkpointDirectory, functionToCreateContext _)

// Do additional setup on context that needs to be done,
// irrespective of whether it is being started or restarted
context. ...

// Start the context
context.start()
context.awaitTermination()
```

如果`checkpointDirectory`存在，则将从检查点数据重新创建上下文。如果目录不存在（即第一次运行），则将`functionToCreateContext`调用该函数以创建新上下文并设置DStream。请参阅Scala示例 [RecoverableNetworkWordCount](https://github.com/apache/spark/tree/master/examples/src/main/scala/org/apache/spark/examples/streaming/RecoverableNetworkWordCount.scala)。此示例将网络数据的字数附加到文件中。

除了使用之外`getOrCreate`还需要确保驱动程序进程在失败时自动重启。这只能通过用于运行应用程序的部署基础结构来完成。这在“ [部署”](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#deploying-applications)部分中进一步讨论 。

请注意，RDD的检查点会导致节省可靠存储的成本。这可能会导致RDD被检查点的那些批次的处理时间增加。因此，需要仔细设置检查点的间隔。在小批量（例如1秒）时，每批次的检查点可能会显着降低操作吞吐量。相反，检查点过于频繁会导致谱系和任务大小增长，这可能会产生不利影响。对于需要RDD检查点的有状态转换，默认间隔是批处理间隔的倍数，至少为10秒。它可以通过使用来设置`dstream.checkpoint(checkpointInterval)`。通常，DStream的5-10个滑动间隔的检查点间隔是一个很好的设置。

------

## 累加器，广播变量和检查点

无法从Spark Streaming中的检查点恢复[累加器](https://spark.apache.org/docs/2.1.0/programming-guide.html#accumulators)和[广播变量](https://spark.apache.org/docs/2.1.0/programming-guide.html#broadcast-variables)。如果启用了检查点并使用[累加器](https://spark.apache.org/docs/2.1.0/programming-guide.html#accumulators)或[广播变量](https://spark.apache.org/docs/2.1.0/programming-guide.html#broadcast-variables)，则必须为[累加器](https://spark.apache.org/docs/2.1.0/programming-guide.html#accumulators)和[广播变量](https://spark.apache.org/docs/2.1.0/programming-guide.html#broadcast-variables)创建延迟实例化的单例实例，以便在驱动程序重新启动失败后重新实例化它们。这在以下示例中显示。

- [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_18)
- [**Java的**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_java_18)
- [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_18)

```
object WordBlacklist {

  @volatile private var instance: Broadcast[Seq[String]] = null

  def getInstance(sc: SparkContext): Broadcast[Seq[String]] = {
    if (instance == null) {
      synchronized {
        if (instance == null) {
          val wordBlacklist = Seq("a", "b", "c")
          instance = sc.broadcast(wordBlacklist)
        }
      }
    }
    instance
  }
}

object DroppedWordsCounter {

  @volatile private var instance: LongAccumulator = null

  def getInstance(sc: SparkContext): LongAccumulator = {
    if (instance == null) {
      synchronized {
        if (instance == null) {
          instance = sc.longAccumulator("WordsInBlacklistCounter")
        }
      }
    }
    instance
  }
}

wordCounts.foreachRDD { (rdd: RDD[(String, Int)], time: Time) =>
  // Get or register the blacklist Broadcast
  val blacklist = WordBlacklist.getInstance(rdd.sparkContext)
  // Get or register the droppedWordsCounter Accumulator
  val droppedWordsCounter = DroppedWordsCounter.getInstance(rdd.sparkContext)
  // Use blacklist to drop words and use droppedWordsCounter to count them
  val counts = rdd.filter { case (word, count) =>
    if (blacklist.value.contains(word)) {
      droppedWordsCounter.add(count)
      false
    } else {
      true
    }
  }.collect().mkString("[", ", ", "]")
  val output = "Counts at time " + time + " " + counts
})
```

查看完整的[源代码](https://github.com/apache/spark/blob/v2.1.0/examples/src/main/scala/org/apache/spark/examples/streaming/RecoverableNetworkWordCount.scala)。

------

## 部署应用程序

本节讨论部署Spark Streaming应用程序的步骤。

### 要求

要运行Spark Streaming应用程序，您需要具备以下条件。

- *具有集群管理器的集群* - 这是任何Spark应用程序的一般要求，并在[部署指南](https://spark.apache.org/docs/2.1.0/cluster-overview.html)中进行了详细讨论。

- *打包应用程序JAR* - 您必须将流应用程序编译为JAR。如果您正在使用[`spark-submit`](https://spark.apache.org/docs/2.1.0/submitting-applications.html)启动应用程序，那么您将不需要在JAR中提供Spark和Spark Streaming。但是，如果您的应用程序使用[高级源](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#advanced-sources)（例如Kafka，Flume），则必须将它们链接的额外工件及其依赖项打包在用于部署应用程序的JAR中。例如，使用的应用程序`KafkaUtils` 必须包含`spark-streaming-kafka-0-8_2.11`应用程序JAR中的所有传递依赖项。

- *为执行程序配置足够的内存* - 由于接收的数据必须存储在内存中，因此必须为执行程序配置足够的内存来保存接收的数据。请注意，如果您正在进行10分钟的窗口操作，则系统必须至少将最后10分钟的数据保留在内存中。因此，应用程序的内存要求取决于其中使用的操作。

- *配置检查点* - 如果流应用程序需要它，则必须将Hadoop API兼容容错存储中的目录（例如HDFS，S3等）配置为检查点目录，并以检查点信息可以写入的方式编写流应用程序用于故障恢复。有关详细信息，请参阅[检查点](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#checkpointing)部分。

- 配置应用程序驱动程序的自动重新启动

   \- 要自动从驱动程序故障中恢复，用于运行流应用程序的部署基础结构必须监视驱动程序进程并在驱动程序失败时重新启动驱动程序。不同的

  集群管理器

   有不同的工具来实现这一点

  - *Spark Standalone* - 可以提交Spark应用程序驱动程序以在Spark Standalone集群中运行（请参阅 [集群部署模式](https://spark.apache.org/docs/2.1.0/spark-standalone.html#launching-spark-applications)），即应用程序驱动程序本身在其中一个工作节点上运行。此外，可以指示独立集群管理器*监督*驱动程序，如果驱动程序由于非零退出代码而失败，或者由于运行驱动程序的节点故障，则重新启动它。有关详细信息，请参阅[Spark Standalone指南](https://spark.apache.org/docs/2.1.0/spark-standalone.html)中的 *集群模式*和*监督*。
  - *YARN* - Yarn支持类似的机制来自动重启应用程序。有关更多详细信息，请参阅YARN文档。
  - *Mesos* - [Marathon](https://github.com/mesosphere/marathon)已被用于与Mesos实现这一目标。

- *配置*预*写日志* - 从Spark 1.2开始，我们引入了预*写日志*以实现强大的容错保证。如果启用，则从接收器接收的所有数据都将写入配置检查点目录中的预写日志。这可以防止驱动程序恢复时的数据丢失，从而确保零数据丢失（在[容错语义](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#fault-tolerance-semantics)部分中详细讨论 ）。这可以通过设置来启用[配置参数](https://spark.apache.org/docs/2.1.0/configuration.html#spark-streaming)`spark.streaming.receiver.writeAheadLog.enable`来`true`。然而，这些更强的语义可能以单个接收器的接收吞吐量为代价。这可以通过[并行](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#level-of-parallelism-in-data-receiving)运行[更多接收器](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#level-of-parallelism-in-data-receiving)来纠正 增加总吞吐量。此外，建议在启用预写日志时禁用Spark中接收数据的复制，因为日志已存储在复制存储系统中。这可以通过将输入流的存储级别设置为来完成`StorageLevel.MEMORY_AND_DISK_SER`。使用S3（或任何不支持刷新的文件系统）进行*预写日志时*，请记得启用 `spark.streaming.driver.writeAheadLog.closeFileAfterWrite`和 `spark.streaming.receiver.writeAheadLog.closeFileAfterWrite`。有关详细信息，请参阅 [Spark Streaming配置](https://spark.apache.org/docs/2.1.0/configuration.html#spark-streaming)。

- *设置最大接收速率* - 如果群集资源不足以使流应用程序以接收数据的速度处理数据，则可以通过设置记录/秒的最大速率限制来限制接收器。请参阅接收器和 Direct Kafka方法的[配置参数](https://spark.apache.org/docs/2.1.0/configuration.html#spark-streaming) 。在Spark 1.5中，我们引入了一项称为*背压*的功能，无需设置此速率限制，因为Spark Streaming会自动计算出速率限制，并在处理条件发生变化时动态调整它们。这个背压可以通过设置来启用[配置参数](https://spark.apache.org/docs/2.1.0/configuration.html#spark-streaming)来。`spark.streaming.receiver.maxRate``spark.streaming.kafka.maxRatePerPartition` `spark.streaming.backpressure.enabled``true`

### 升级应用程序代码

如果需要使用新的应用程序代码升级正在运行的Spark Streaming应用程序，则有两种可能的机制。

- 升级的Spark Streaming应用程序启动并与现有应用程序并行运行。一旦新的（接收与旧的数据相同的数据）已经预热并准备好黄金时间，旧的可以被放下。请注意，这可以用于支持将数据发送到两个目标（即早期和升级的应用程序）的数据源。
- 现有应用程序正常关闭（请参阅 [`StreamingContext.stop(...)`](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.streaming.StreamingContext) 或[`JavaStreamingContext.stop(...)`](https://spark.apache.org/docs/2.1.0/api/java/index.html?org/apache/spark/streaming/api/java/JavaStreamingContext.html) 用于正常关闭选项），确保在关闭之前完全处理已接收的数据。然后可以启动升级的应用程序，该应用程序将从早期应用程序停止的同一点开始处理。请注意，这只能通过支持源端缓冲的输入源（如Kafka和Flume）来完成，因为在前一个应用程序关闭且升级的应用程序尚未启动时需要缓冲数据。并且无法从早期检查点重新启动升级前代码的信息。检查点信息基本上包含序列化的Scala / Java / Python对象，并且尝试使用新的修改类反序列化对象可能会导致错误。在这种情况下，要么使用不同的检查点目录启动升级的应用程序，要么删除以前的检查点目录。

------

## 监控应用

除了Spark的[监控功能外](https://spark.apache.org/docs/2.1.0/monitoring.html)，还有Spark Streaming特有的其他功能。使用StreamingContext时， [Spark Web UI会](https://spark.apache.org/docs/2.1.0/monitoring.html#web-interfaces)显示一个附加`Streaming`选项卡，其中显示有关运行接收器的统计信息（接收器是否处于活动状态，接收的记录数，接收器错误等）和已完成的批处理（批处理时间，排队延迟等）。 ）。这可用于监视流应用程序的进度。

Web UI中的以下两个指标尤为重要：

- *处理时间* - 处理每批数据的时间。
- *计划延迟* - 批处理在队列中等待处理先前批处理完成的时间。

如果批处理时间始终大于批处理间隔和/或排队延迟不断增加，则表明系统无法以最快的速度处理批次并且落后。在这种情况下，请考虑 [减少](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#reducing-the-batch-processing-times)批处理时间。

还可以使用[StreamingListener](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.streaming.scheduler.StreamingListener)接口监视Spark Streaming程序的进度，该 接口允许您获取接收器状态和处理时间。请注意，这是一个开发人员API，未来可能会对其进行改进（即报告更多信息）。

------

------

# 性能调优

从群集上的Spark Streaming应用程序中获得最佳性能需要进行一些调整。本节介绍了许多可以调整以提高应用程序性能的参数和配置。在高层次上，您需要考虑两件事：

1. 通过有效使用群集资源减少每批数据的处理时间。
2. 设置正确的批量大小，以便可以像接收到的那样快速处理批量数据（即，数据处理与数据提取保持同步）。

## 减少批处理时间

可以在Spark中进行许多优化，以最大限度地缩短每个批处理的处理时间。这些已在“ [调整指南”](https://spark.apache.org/docs/2.1.0/tuning.html)中详细讨论过。本节重点介绍一些最重要的内容。

### 数据接收中的并行度

通过网络接收数据（如Kafka，Flume，socket等）需要将数据反序列化并存储在Spark中。如果数据接收成为系统中的瓶颈，则考虑并行化数据接收。请注意，每个输入DStream都会创建一个接收单个数据流的接收器（在工作机器上运行）。因此，可以通过创建多个输入DStream并将它们配置为从源接收数据流的不同分区来实现接收多个数据流。例如，接收两个数据主题的单个Kafka输入DStream可以分成两个Kafka输入流，每个输入流只接收一个主题。这将运行两个接收器，允许并行接收数据，从而提高整体吞吐量。这些多个DStream可以组合在一起以创建单个DStream。然后，可以在统一流上应用在单个输入DStream上应用的转换。这样做如下。

- [**斯卡拉**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_scala_19)
- [**Java的**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_java_19)
- [**蟒蛇**](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#tab_python_19)

```
val numStreams = 5
val kafkaStreams = (1 to numStreams).map { i => KafkaUtils.createStream(...) }
val unifiedStream = streamingContext.union(kafkaStreams)
unifiedStream.print()
```

应考虑的另一个参数是接收器的块间隔，它由[配置参数](https://spark.apache.org/docs/2.1.0/configuration.html#spark-streaming)决定 `spark.streaming.blockInterval`。对于大多数接收器，接收的数据在存储在Spark的内存中之前合并为数据块。每批中的块数决定了在类似地图的转换中用于处理接收数据的任务数。每批每个接收器的任务数量大约是（批处理间隔/块间隔）。例如，200 ms的块间隔将每2秒批次创建10个任务。如果任务数量太少（即，少于每台计算机的核心数），那么效率将会很低，因为所有可用的核心都不会用于处理数据。要增加给定批处理间隔的任务数，请减少块间隔。但是，建议的块间隔最小值约为50 ms，低于该值时，任务启动开销可能会出现问题。

使用多个输入流/接收器接收数据的替代方案是显式地重新分区输入数据流（使用`inputStream.repartition(<number of partitions>)`）。这会在进一步处理之前将收到的批量数据分布到群集中指定数量的计算机上。

### 数据处理中的并行度

如果在计算的任何阶段中使用的并行任务的数量不够高，则可能未充分利用群集资源。例如，对于像`reduceByKey` 和的分布式reduce操作`reduceByKeyAndWindow`，默认的并行任务数由`spark.default.parallelism` [配置属性](https://spark.apache.org/docs/2.1.0/configuration.html#spark-properties)控制。您可以将并行级别作为参数传递（请参阅[`PairDStreamFunctions`](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.streaming.dstream.PairDStreamFunctions) 文档），或者设置`spark.default.parallelism` [配置属性](https://spark.apache.org/docs/2.1.0/configuration.html#spark-properties)以更改默认值。

### 数据序列化

通过调整序列化格式可以减少数据序列化的开销。在流式传输的情况下，有两种类型的数据被序列化。

- **输入数据**：默认情况下，通过Receiver接收的输入数据通过[StorageLevel.MEMORY_AND_DISK_SER_2](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.storage.StorageLevel$)存储在执行程序的内存中。也就是说，数据被序列化为字节以减少GC开销，并且为了容忍执行器故障而被复制。此外，数据首先保存在内存中，并且仅在内存不足以保存流式计算所需的所有输入数据时才溢出到磁盘。这种序列化显然有开销 - 接收器必须反序列化接收的数据并使用Spark的序列化格式重新序列化。
- **流式传输操作生成的持久RDD**：流式计算生成的RDD可以保留在内存中。例如，窗口操作将数据保留在内存中，因为它们将被多次处理。但是，与[StorageLevel.MEMORY_ONLY](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.storage.StorageLevel$)的Spark Core默认值不同，流式计算生成的持久RDD 默认使用[StorageLevel.MEMORY_ONLY_SER](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.storage.StorageLevel$)（即序列化）保留，以最大限度地减少GC开销。

在这两种情况下，使用Kryo序列化可以减少CPU和内存开销。有关详细信息，请参阅[Spark Tuning Guide](https://spark.apache.org/docs/2.1.0/tuning.html#data-serialization)。对于Kryo，请考虑注册自定义类，并禁用对象引用跟踪（请参阅“ [配置指南”](https://spark.apache.org/docs/2.1.0/configuration.html#compression-and-serialization)中的Kryo相关配置）。

在需要为流应用程序保留的数据量不大的特定情况下，将数据（两种类型）保存为反序列化对象可能是可行的，而不会产生过多的GC开销。例如，如果您使用几秒钟的批处理间隔而没有窗口操作，则可以尝试通过相应地显式设置存储级别来禁用持久数据中的序列化。这将减少由于序列化导致的CPU开销，可能在没有太多GC开销的情况下提高性能。

### 任务启动开销

如果每秒启动的任务数量很高（例如，每秒50或更多），则向从属设备发送任务的开销可能很大，并且将难以实现亚秒级延迟。通过以下更改可以减少开销：

- **执行模式**：在独立模式或粗粒度Mesos模式**下**运行Spark可以获得比细粒度Mesos模式更好的任务启动时间。有关更多详细信息，请参阅[Running on Mesos指南](https://spark.apache.org/docs/2.1.0/running-on-mesos.html)。

这些更改可以将批处理时间减少100毫秒，从而允许亚秒级批量大小可行。

------

## 设置正确的批次间隔

要使群集上运行的Spark Streaming应用程序保持稳定，系统应该能够以接收数据的速度处理数据。换句话说，批处理数据应该在生成时尽快处理。通过[监视](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#monitoring-applications)流式Web UI中的处理时间可以找到是否适用于应用程序 ，其中批处理时间应小于批处理间隔。

根据流式计算的性质，所使用的批处理间隔可能对应用程序在固定的一组集群资源上可以维持的数据速率产生重大影响。例如，让我们考虑一下早期的WordCountNetwork示例。对于特定数据速率，系统可能能够每2秒（即，2秒的批处理间隔）跟上报告字数，但不是每500毫秒。因此需要设置批处理间隔，以便可以维持生产中的预期数据速率。

确定适合您的应用程序批量大小的好方法是使用保守的批处理间隔（例如，5-10秒）和低数据速率进行测试。要验证系统是否能够跟上数据速率，您可以检查每个已处理批处理所遇到的端到端延迟的值（在Spark驱动程序log4j日志中查找“总延迟”，或使用 [StreamingListener](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.streaming.scheduler.StreamingListener) 接口）。如果延迟保持与批量大小相当，则系统稳定。否则，如果延迟不断增加，则意味着系统无法跟上，因此不稳定。一旦了解了稳定的配置，就可以尝试提高数据速率和/或减小批量。注意，只要延迟减小到低值（即，小于批量大小），由于临时数据速率增加引起的延迟的瞬时增加可能是正常的。

------

## 内存调整

“调[优指南”中](https://spark.apache.org/docs/2.1.0/tuning.html#memory-tuning)详细讨论了[调整](https://spark.apache.org/docs/2.1.0/tuning.html#memory-tuning) Spark应用程序的内存使用情况和GC行为。强烈建议您阅读。在本节中，我们将特别在Spark Streaming应用程序的上下文中讨论一些调优参数。

Spark Streaming应用程序所需的集群内存量在很大程度上取决于所使用的转换类型。例如，如果要在最后10分钟的数据上使用窗口操作，那么您的群集应该有足够的内存来在内存中保存10分钟的数据。或者，如果您想使用`updateStateByKey`大量的键，那么必要的内存将很高。相反，如果你想做一个简单的map-filter-store操作，那么必要的内存就会很低。

通常，由于通过接收器接收的数据与StorageLevel.MEMORY_AND_DISK_SER_2一起存储，因此不适合内存的数据将溢出到磁盘。这可能会降低流应用程序的性能，因此建议您根据流应用程序的需要提供足够的内存。最好尝试小规模地查看内存使用情况并进行相应估算。

内存调整的另一个方面是垃圾收集。对于需要低延迟的流应用程序，不希望由JVM垃圾收集引起大的暂停。

有一些参数可以帮助您调整内存使用和GC开销：

- **DStream的持久性级别**：如前面[数据序列化](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#data-serialization)部分所述，输入数据和RDD默认持久化为序列化字节。与反序列化持久性相比，这减少了内存使用和GC开销。启用Kryo序列化可进一步减少序列化大小和内存使用量。通过压缩（参见Spark配置`spark.rdd.compress`）可以实现内存使用的进一步减少，但代价是CPU时间。
- **清除旧数据**：默认情况下，DStream转换生成的所有输入数据和持久RDD都会自动清除。Spark Streaming根据使用的转换决定何时清除数据。例如，如果您使用10分钟的窗口操作，那么Spark Streaming将保留最后10分钟的数据，并主动丢弃旧数据。通过设置，可以将数据保留更长的时间（例如，交互式查询旧数据）`streamingContext.remember`。
- **CMS垃圾收集器**：强烈建议使用并发标记和清除GC，以保持GC相关的暂停始终较低。尽管已知并发GC会降低系统的整体处理吞吐量，但仍建议使用它来实现更一致的批处理时间。确保在驱动程序（使用`--driver-java-options`输入`spark-submit`）和执行程序（使用[Spark配置](https://spark.apache.org/docs/2.1.0/configuration.html#runtime-environment)`spark.executor.extraJavaOptions`）上设置CMS GC 。
- **其他提示**：为了进一步降低GC开销，这里有一些尝试的提示。
  - 使用`OFF_HEAP`存储级别保留RDD 。请参阅[Spark编程指南](https://spark.apache.org/docs/2.1.0/programming-guide.html#rdd-persistence)中的更多详细信息。
  - 使用具有较小堆大小的更多执行程序。这将降低每个JVM堆中的GC压力。

------

##### 要记住的要点：

- DStream与单个接收器相关联。为了获得读取并行性，需要创建多个接收器，即多个DStream。接收器在执行器内运行。它占据一个核心。确保在预订接收器插槽后有足够的内核进行处理，即`spark.cores.max`应考虑接收器插槽。接收器以循环方式分配给执行器。
- 当从流源接收数据时，接收器创建数据块。每隔blockInterval毫秒生成一个新的数据块。在batchInterval期间创建N个数据块，其中N = batchInterval / blockInterval。这些块由当前执行程序的BlockManager分发给其他执行程序的块管理器。之后，将在驱动程序上运行的网络输入跟踪器通知块位置以进行进一步处理。
- 在驱动程序上为batchInterval期间创建的块创建RDD。batchInterval期间生成的块是RDD的分区。每个分区都是spark中的任务。blockInterval == batchinterval意味着创建了一个分区，并且可能在本地处理它。
- 块中的映射任务在执行器中处理（一个接收块，另一个块复制块），具有块而不管块间隔，除非非本地调度启动。具有更大的blockinterval意味着更大的块。较高的值会`spark.locality.wait`增加在本地节点上处理块的机会。需要在这两个参数之间找到平衡，以确保在本地处理更大的块。
- 您可以通过调用来定义分区数，而不是依赖于batchInterval和blockInterval `inputDstream.repartition(n)`。这会随机重新调整RDD中的数据以创建n个分区。是的，为了更大的并行性。虽然以洗牌为代价。RDD的处理由驾驶员的jobcheduler作为工作安排。在给定的时间点，只有一个作业处于活动状态。因此，如果一个作业正在执行，则其他作业将排队。
- 如果您有两个dstream，将形成两个RDD，并且将创建两个将一个接一个地安排的作业。为了避免这种情况，你可以结合两个dstreams。这将确保为dstream的两个RDD形成单个unionRDD。然后，此unionRDD被视为单个作业。但是，RDD的分区不会受到影响。
- 如果批处理时间超过批处理间隔，那么显然接收者的内存将开始填满并最终导致抛出异常（最可能是BlockNotFoundException）。目前没有办法暂停接收器。使用SparkConf配置`spark.streaming.receiver.maxRate`，可以限制接收器的速率。

------

------

# 容错语义

在本节中，我们将讨论Spark Streaming应用程序在发生故障时的行为。

## 背景

要理解Spark Streaming提供的语义，让我们记住Spark的RDD的基本容错语义。

1. RDD是一个不可变的，确定性可重新计算的分布式数据集。每个RDD都会记住在容错输入数据集上用于创建它的确定性操作的沿袭。
2. 如果由于工作节点故障导致RDD的任何分区丢失，则可以使用操作系列从原始容错数据集重新计算该分区。
3. 假设所有RDD转换都是确定性的，那么无论Spark集群中的故障如何，最终转换后的RDD中的数据总是相同的。

Spark对容错文件系统（如HDFS或S3）中的数据进行操作。因此，从容错数据生成的所有RDD也是容错的。但是，Spark Streaming不是这种情况，因为大多数情况下的数据是通过网络接收的（除非 `fileStream`使用时）。要为所有生成的RDD实现相同的容错属性，接收的数据将在群集中的工作节点中的多个Spark执行程序之间进行复制（默认复制因子为2）。这导致系统中需要在发生故障时恢复的两种数据：

1. *接收和复制的*数据 - 此数据在单个工作节点发生故障时仍然存在，因为其副本存在于其他节点之一上。
2. *接收到的数据但缓冲用于复制* - 由于未复制，因此恢复此数据的唯一方法是从源中再次获取数据。

此外，我们应该关注两种失败：

1. *工作节点失败* - 运行执行程序的任何工作节点都可能失败，并且这些节点上的所有内存数据都将丢失。如果任何接收器在故障节点上运行，则它们的缓冲数据将丢失。
2. *驱动程序节点失败* - 如果运行Spark Streaming应用程序的驱动程序节点出现故障，那么SparkContext显然会丢失，并且所有带有内存数据的执行程序都将丢失。

有了这些基础知识，让我们了解Spark Streaming的容错语义。

## 定义

流系统的语义通常根据系统处理每条记录的次数来捕获。系统可以在所有可能的操作条件下提供三种类型的保证（尽管出现故障等）

1. *最多一次*：每条记录将被处理一次或根本不处理。
2. *至少一次*：每条记录将被处理一次或多次。这比*最多一次*强*，*因为它确保不会丢失任何数据。但可能有重复。
3. *恰好一次*：每条记录只处理一次 - 不会丢失数据，也不会多次处理数据。这显然是三者的最强保证。

## 基本语义

在任何流处理系统中，从广义上讲，处理数据有三个步骤。

1. *接收数据*：使用接收器或其他方式从数据源接收数据。
2. *转换数据*：使用DStream和RDD转换转换接收的数据。
3. *推出数据*：最终转换的数据被推送到外部系统，如文件系统，数据库，仪表板等。

如果流应用程序必须实现端到端的一次性保证，那么每个步骤都必须提供一次性保证。也就是说，每个记录必须只接收一次，转换一次，然后推送到下游系统一次。让我们在Spark Streaming的上下文中理解这些步骤的语义。

1. *接收数据*：不同的输入源提供不同的保证。这将在下一小节中详细讨论。
2. *转换数据*：由于RDD提供的保证，所有已接收的数据将只处理*一次*。即使存在故障，只要接收到的输入数据可访问，最终转换的RDD将始终具有相同的内容。
3. *推出数据*：默认情况下输出操作*至少*确保*一次*语义，因为它取决于输出操作的类型（幂等或不是）和下游系统的语义（支持是否支持事务）。但是用户可以实现自己的事务机制来实现*一次性*语义。这将在本节后面详细讨论。

## 接收数据的语义

不同的输入源提供不同的保证，范围从*至少一次*到*恰好一次*。阅读更多详情。

### 使用文件

如果所有输入数据都已存在于HDFS等容错文件系统中，则Spark Streaming可以始终从任何故障中恢复并处理所有数据。这给出 *了一次性*语义，这意味着无论失败什么，所有数据都将被处理一次。

### 使用基于Receiver的源

对于基于接收器的输入源，容错语义取决于故障情形和接收器类型。正如我们前面讨论[过的](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#receiver-reliability)，有两种类型的接收器：

1. *可靠的接收器* - 这些接收器仅在确保已复制接收的数据后才确认可靠的源。如果此类接收器发生故障，则源将不会收到对缓冲（未复制）数据的确认。因此，如果重新启动接收器，源将重新发送数据，并且不会因失败而丢失数据。
2. *不可靠的接收器* - 此类接收器*不*发送确认，因此在由于工作人员或驱动程序故障而失败时*可能*会丢失数据。

根据使用的接收器类型，我们实现以下语义。如果工作节点发生故障，则可靠接收器不会丢失数据。对于不可靠的接收器，接收但未复制的数据可能会丢失。如果驱动程序节点出现故障，那么除了这些丢失之外，在内存中接收和复制的所有过去数据都将丢失。这将影响有状态转换的结果。

为了避免丢失过去收到的数据，Spark 1.2引入了预*写日志*，将接收到的数据保存到容错存储中。通过[启用](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#deploying-applications)预[写日志](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html#deploying-applications)和可靠的接收器，数据丢失为零。在语义方面，它提供至少一次保证。

下表总结了失败时的语义：

| 部署方案                                                     | 工人失败                                                     | 司机失败                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| *Spark 1.1或更早版本，*或 *Spark 1.2或更高版本，无需提前写入日志* | 使用不可靠的接收器丢失缓冲数据使用可靠的接收器实现 零数据丢失 至少一次语义 | 使用不可靠的接收器丢失缓冲数据 过去的数据在所有接收器中丢失 未定义的语义 |
| *Spark 1.2或更高版本，具有预写日志*                          | 使用可靠的接收器实现零数据丢失 至少一次语义                  | 使用可靠的接收器和文件实现零数据丢失 至少一次语义            |
|                                                              |                                                              |                                                              |

### 使用Kafka Direct API

在Spark 1.3中，我们引入了一个新的Kafka Direct API，它可以确保Spark Streaming只接收一次所有Kafka数据。除此之外，如果您实现一次性输出操作，您可以实现端到端的一次性保证。“ [卡夫卡集成指南”中](https://spark.apache.org/docs/2.1.0/streaming-kafka-integration.html)进一步讨论了这种方法。

## 输出操作的语义

输出操作（例如`foreachRDD`）*至少具有一次*语义，即，在工作者失败的情况下，转换的数据可能被多次写入外部实体。虽然这对于使用`saveAs***Files`操作保存到文件系统是可以接受的 （因为文件将被简单地用相同的数据覆盖），但是可能需要额外的努力来实现精确一次的语义。有两种方法。

- *幂等更新*：多次尝试始终写入相同的数据。例如，`saveAs***Files`始终将相同的数据写入生成的文件。

- *事务性更新*：所有更新都是以事务方式进行的，以便以原子方式完成更新。一种方法是做到这一点。

  - 使用批处理时间（可用`foreachRDD`）和RDD的分区索引来创建标识符。该标识符唯一地标识流应用程序中的blob数据。

  - 使用标识符以事务方式（即，一次，原子地）使用此blob更新外部系统。也就是说，如果标识符尚未提交，则以原子方式提交分区数据和标识符。否则，如果已经提交，请跳过更新。

    ```
    dstream.foreachRDD { (rdd, time) =>
      rdd.foreachPartition { partitionIterator =>
        val partitionId = TaskContext.get.partitionId()
        val uniqueId = generateUniqueId(time.milliseconds, partitionId)
        // use this uniqueId to transactionally commit the data in partitionIterator
      }
    }
    ```

------

------

# 从这往哪儿走

- 其他指南
  - [Kafka集成指南](https://spark.apache.org/docs/2.1.0/streaming-kafka-integration.html)
  - [Kinesis集成指南](https://spark.apache.org/docs/2.1.0/streaming-kinesis-integration.html)
  - [自定义接收器指南](https://spark.apache.org/docs/2.1.0/streaming-custom-receivers.html)
- 可以在[第三方项目中](http://spark.apache.org/third-party-projects.html)找到第三方DStream数据源
- API文档
  - Scala文档
    - [StreamingContext](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.streaming.StreamingContext)和 [DStream](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.streaming.dstream.DStream)
    - [KafkaUtils](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.streaming.kafka.KafkaUtils$)， [FlumeUtils](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.streaming.flume.FlumeUtils$)， [KinesisUtils](https://spark.apache.org/docs/2.1.0/api/scala/index.html#org.apache.spark.streaming.kinesis.KinesisUtils$)，
  - Java文档
    - [JavaStreamingContext](https://spark.apache.org/docs/2.1.0/api/java/index.html?org/apache/spark/streaming/api/java/JavaStreamingContext.html)， [JavaDStream](https://spark.apache.org/docs/2.1.0/api/java/index.html?org/apache/spark/streaming/api/java/JavaDStream.html)和 [JavaPairDStream](https://spark.apache.org/docs/2.1.0/api/java/index.html?org/apache/spark/streaming/api/java/JavaPairDStream.html)
    - [KafkaUtils](https://spark.apache.org/docs/2.1.0/api/java/index.html?org/apache/spark/streaming/kafka/KafkaUtils.html)， [FlumeUtils](https://spark.apache.org/docs/2.1.0/api/java/index.html?org/apache/spark/streaming/flume/FlumeUtils.html)， [KinesisUtils](https://spark.apache.org/docs/2.1.0/api/java/index.html?org/apache/spark/streaming/kinesis/KinesisUtils.html)
  - Python文档
    - [StreamingContext](https://spark.apache.org/docs/2.1.0/api/python/pyspark.streaming.html#pyspark.streaming.StreamingContext)和[DStream](https://spark.apache.org/docs/2.1.0/api/python/pyspark.streaming.html#pyspark.streaming.DStream)
    - [KafkaUtils](https://spark.apache.org/docs/2.1.0/api/python/pyspark.streaming.html#pyspark.streaming.kafka.KafkaUtils)
- [Scala](https://github.com/apache/spark/tree/master/examples/src/main/scala/org/apache/spark/examples/streaming) ，[Java](https://github.com/apache/spark/tree/master/examples/src/main/java/org/apache/spark/examples/streaming) 和[Python中的](https://github.com/apache/spark/tree/master/examples/src/main/python/streaming)更多示例
- 描述Spark Streaming的[论文](http://www.eecs.berkeley.edu/Pubs/TechRpts/2012/EECS-2012-259.pdf)和[视频](http://youtu.be/g171ndOHgJ0)。