## Spark笔记

RDD 是分布式 内存的一 个抽 象概念，是一种高度受限的共享内存模型，即 RDD 是只读
的记录分区的栠合 ， 能横跨栠群所有节点并行计算，是一种基千工作集的应用抽象。



本质上 ，一个 RDD 在代码中相当千数据的 一个元数据结构( 一个 RDD
就是一组分区)，存储着数据分区及 Block、 Node 等的映射关系，以及其他元数据信息，存
储店 RDD 之前的依赖转换关系。分区是 一个逻辑概念， Transformation 前后的新旧分区在物
理上可能是同一块内存存储。



RDD 的写操作是粗粒度的，读操作既可以是粗粒度的，也可以是细粒度的。



在Spark中， 一个RDD就是一个分布式对象集合，每个 RDD 可分为多个片 (Partitions), 而分片可以在集群环境的不同节点上计算。

- 转换 Transformation操作： map、union 和 groubByKey
- 行动 Action 操作：



### RDD 五大特性 :

- 分区列表
- 每个分区都有一个计算函数
- 依赖于其他RDD的列表
- Key-value 数据类型的RDD分区器，控制分区策略和分区数。
- 每个分区都有一个优先位置列表



Spark RDD 是被分区的，每 一个分区都会被一个计算任务 (Task) 处理 ，分区数决定并行计算数嵌， RDD 的并行度默认从父 RDD 传给子 RDD。

RDD 之间的依赖有两种:窄依赖(Narrow Dependency)、宽依赖 (Wide Dependency) o RDD 是 Spark 的核心数据结构，通过RDD 的依赖关系形成调度关系。通过对 RDD 的操作形成整个 Spark程序。



#### DataSet 的定义与内部机制

DataSet是可以并行使用函数或关系操作转换特定域对象的强类型集合。

每个 DataSet有一个非类型化的 DataFrame。 

DataFrame 是 Dataset[Row]的别名。

DataSet 中可用的算子分为转换算子和行动算子。

转换莽子可以产生新的 DataSet; 

行动算子将触发计算和返回结果；

本质上， DataSet表示一个逻辑计划，它描述了生成数据所需的计算。



#### RDD弹性特征七个方面解析

1. 自动进行内存和磁盘数据存储的切换

2. 基千 Lineage (血统)的高效容错机制

3. Task如果失败，会自动进行特定次数的重试。（默认重试次数为4）

4. Stage 如果失败，会自动进行特定次数的重试。（默认重试次数为4）

   Stage 是 SparkJob 运行时具有相同逻辑功能和 并行计算任务的 一个基本单元。 

5. checkpoint和persist C检查点和持久化)，可主动或被动触发

   checkpoint是对 RDD 进行的标记，会产生一系列的文件，且所有父依赖都会被删除，是
   整个依赖 (Lineage) 的终点。 

6. 数据调度弹性， DAGScheduler、 TASKScheduler和资源管理无关

   Spark将执行模型抽象为通用的有向无环图计划 (DAG), 这可以将多 Stage 的任务串联
   或并行执行，从而不需要将 Stage 中间结果输出到 HDFS 中，当发生节点运行故障时，可有
   其他可用节点代替该故障节点运行。

7. 数据分片的高度弹性 (coalesce)

   Spark 进行数据分片时，默认将数据放在内存中，如果内存放不下， 一部分会放在磁盘上进行保存。

   把许多小的 Partition合并成一个较大的 Partition去处理，这样会提高效率。



#### RDD依赖关系

- 窄依赖 (Narrow Dependency) 

  窄依赖表示每个父 RDD 中的 Partition最多被子 RDD 的一个 Partition所使用。

​           1、一对一依赖 （OneToOneDepcndency），父 RDD 与子 RDD 的依赖关系是一对一的依赖关系。

​               如 map、 filter、 join with inputs co-partitioned;  

​               结果数据与开始数据个数一一对应

​	  2、范围依赖（RangeDependency）表示父 RDD 与子 RDD 的一对 一 的范围内依赖关系 

​		如 union

​                结果数据与开始数据范围（区，块）对应

- 宽依赖 (Shuffle Dependency) ，一种会导致计算时产生 Shuffle操作的RDD操作。

  宽依赖表示一个父 RDD 的 Partition都会被多个子 RDD 的 Partition所使用。

​          Spark 中常见的宽依赖关系的操作：GroupByKey



#### Spark  中的DAG逻辑视图

- DAG图：有一个有向图无法从任意顶点出发经过若干条边回到该点，则这个图是一个有向无环图

- Spark 中DAG的体现：Spark中，计算过程会有先后顺序，受制于某些任务必须比另一些任务早执行的限制，我们必须对任务进行排队，形成一个队列的任务集合，这个任务集合就是DAG图。
- Spark 中 DAG 生成过程的重点是对 Stage 的划分，其划分的依据是 ROD 的依赖关系，
  对千不同的依赖关系 ， 高层调度器会进行不同的处理。
- 对于窄依赖， RDD 之间的数据不需要进行 Shuffle, 多个数据处理可以在同 一 台机器的内存中完成，所以窄依赖在 Spark 中被划分为同一个 Stage; 
- 对于宽依赖，由千 Shuffle的存在，必须等到父 RDD 的 Shuffle处理完成后，才能开始接下来的计算，所以会在此处进行 Stage 的切分 。
- 在 Spark 中， DAG 生成的流程关键在千回溯，在程序提交后 ，高层调度器将所有的 RDD 看成是一个 Stage, 然后对此 Stage进行从后往前的回溯，遇到 Shuffle 就断开，遇到窄依赖， 则归并到同一个 Stage。等到所有的步骤回溯完成，便生成一个 DAG 图。 

**DAG逻辑视图解析** 【DAG具体的生成流程和关系】

 ```
val conf = new SparkConf()  // 创建SparkConf
conf.setAppName("Wow, My First Spark App")  // 设置应用名称
conf.setMaster("local")  // 在本地运行
val sc = new SparkContext(conf)
val lines = sc.textFile("C://data//SparkText.txt", 1)

// 操作1， flatMap 由lines 通过flatMap 操作形成新的MapPartitionRDD
val words = lines.flatMap(lines=>lines.split(" "))

// 操作2， map由word通过Map操作形成新的MapOartitionRDD
val pairs = words.map( word => (word, 1))

// 操作3， reduceByKey (包含2步 reduce)
// 此步骤生成 MapPartitionRDD 和 ShuffleRDD
val WordCounts = pairs.reduceByKey(_+_)
Wordcounts.collect.foreach(println)

// 关闭
sc.stop()
 ```

- 开始运行前，DAG调度器会将整个流程设定为一个Stage, 

​	此Stage 包含3个操作，5个RDD,  分别是 MapPartitionRDD（读取文件数据时）、MapPartitionRDD(flatMap操作)、MapPartitionRDD(map操作)、MapPartitionRDD(reduceByKey 的local段的操作)、ShuffleRDD(reduceByKeyshuffle 操作)

- 1 、回溯整个流程，在 shuffleRDD 与 MapPartitionRDD(reduceByKey的local段的操作) 中存在 shuffle 操作，整个RDD先在此切开，形成两个Stage.
- 2、继续向前回溯，MapPartitionRDD ( reduceByKey 的local段的操作) 与MapPartitionRDD(map 操作) 中间不存在 Shuffle (即 两个RDD的依赖关系为窄依赖)，归为同一个Stage.
- 3、继续回溯，发现往前的所有的RDD之间都不存在 Shuffle, 应归为同一个 Stage.
- 4、回溯完成，形成DAG，由两个Stage
  - 第一个 Stage 由MapPartitionRDD(读取文件数据时)、MapPartitionRDD(flatMap操作)、MapPartitionRDD(map 操作)、MapPartitionRDD( reduceByKey的local段的操作)构成。
  - 第二个 Stage  由 ShuffleRDD (reduceByKey Shuffle 操作)构成。





​     



#### 常规容错

常规容错有两种方式:一个是数据检杏点;另 一个是记录数据的更新。数
据梒查点的基本工作方式，就是通过数据中心的网络链接不同的机器，然后每次操作的时候
都要复制数据集，就相当于每次都有一个复制，复制是要通过网络传输的，网络带宽就 是分
布式的瓶颈，对存储资源也是很大的消耗。记录数据更新就是每次数据变化了就记录一下，
这种方式不需要重新复制 一份数据，但是比较复杂，消耗性能。 



Spark 的 RDD 通过记录数据更新的方式为何很高效?

因为  RDD 是不叫变的且 Lazy; 

 RDD 的写操作是粗粒度的 。
但是， ROD 读操作既可以是粗粒度的，也可以是细粒度的。



#### RDD内部的计算机制

RDD的多个Partition 分别由不同的Task 处理。

Task 分为两类： shuffleMapTask、resultTask



Task 解析

Task 是计算运行在奂群上的基本计算单位。一个 Task 负责处理 RDD 的一个 Partition, 

一个 RDD 的多个 Partition会分别由不同的 Task去处理 



RDD 的窄依赖中，子 ROD 中 Partition 的个数基本都大千等千父 RDD
中 Partition 的个数，所以 Spark 计算中对千每一个 Stage 分配的 Task 的数目是基于该 Stage
中最后一个 RDD 的 Partition的个数来决定的。最后一个 RDD 如果有 100个 Partition,则 Spark
对这个 Stage 分配 100 个 Task。



Task运行千 Executor上，而 Executor位千 CoarseGrainedExecutorBackend (NM 进程)中。

第一类为
shuftleMapTask, 指 Task所处的 Stage不是最后一个 Stage, 也就是 Stage 的计算结果还没有
输出，而是通过 Shuffie交给下一个 Stage使用;



第二类为 resultTask, 指 Task所处 Stage是
DAG 中最后一个 Stage, 也就是 Stage 计算结果需要进行输出等操作，计算到此已经结束;



**计算过程深度解析**



ROD 在进行计算前， Driver给其他 Executor 发送消息，让 Executor 启动 Task, 在 Executor 

启动 Task成功后，通过消息机制汇报启动成功信息给 Driver。 



#### Spark RDD 容错原理及四大核心要点

RDD的依赖关系（宽依赖，窄依赖）

Spark框架层面的三大层面（调度层，RDD血统层， Checkpoint层）

**RDD的不同依赖关系的不同容错处理机制**

- 宽依赖，数据出错，无法达到效果，需要重新计算全部
- 窄依赖，数据出错，只需要重新出错部分即可



**四大核心要点**

1、 调度层（包含DAG生成和Task 重算两大核心）

​       从调度层面来将，错误主要出现在两个方面，在Stage 输出时出错 和 在Task计算时出错

​       1> Stage 输出失败， 上层调度器DAGScheduler 会进行重试

​       2> Spark 计算过程中，计算内部某个Task 任务出现失败，底层调度器会对此Task 进行若干次重试（4次）



2、RDD Lineage 血统层容错

3、checkpoint 层容错

​	Spark checkpoint通过将 RDD 写入 Disk作检查点，是 Sparklineage容错的辅助， lineage
​	过长会造成容错成本过高，这时在中间阶段做检查点容错，如果之后有节点出现问题而丢失
​	分区， 从做检 查点 的 RDD 开始重做 Lineage, 就会减少开销。

​	checkpoint主要适用千以下两种情况 :

​		DAG中的Lineage 过长，如果重算，开销太大，如 PageRank、ALS 等。

​                适合在宽依赖上做checkpoint , 这个时候就可以避免为lineage  重新计算而带来的冗余计算。



#### Spark RDD 中的 Runtime 流程解析

Spark 的 Runtime 架构图

(I) 从 SparkRuntime 的角度讲，包括五大核心对象: Master、 Worker、 Executor、 Driver、CoarseGrainedExecutorBackend。

(2) Spark 在做分布式集群系统设计 的时候:最大化功能独立 、模块化封装具体独立的 对象、强 内聚松耦合 。 Spark 运行架构图如图 3-7 所示。

![image-20190214113238600](/Users/weicheng/Library/Application Support/typora-user-images/image-20190214113238600.png)

(3) 当 Driver 中的 SparkContext初始化时 会提交程序给 Master, Master如果接受该程序 在 Spark 中运行，就会为 当前的程序分配 AppID, 同时会分配具体的计算资源。需要特别 注 意的是， Master 是根据当前提交程序的配世信息来给栠群中的 Worker 发指令分配具体的计 算资源，但是 ， Master发出指令后并不关心具体的资源是否已经分配，换 言之 ， Master 是发 指令后就记录了分配的资源 ，以后客户端再次提交其他的程序，就不能使用该资源了 。



- 其中， StandaloneSchedulerBackend 负责集群计算资源的管理和调度，这是从作业的
  角度来考虑的，注册给 Master 的时候， Master给我们分配资源，资源从 Executor本身转过来向 StandaloneSchedulerBackend注册，这是从作业调度的角度来考虑的，不 是从整个栠群来考虑，整个集群是 Master来管理计算资源的。
- DAGScheduler 负责 高层调度(如 Job 中 Stage 的划分、数据本地性等内容) 。
- TaskSchedulerlmple 负责具体 Stage 内部的底层调度(如具体每个 Task 的调度、 Task
  的容错等)。
- MapOutputTrackerMaster负 责 Shuffle 中数据输出和读取的管理 。 Shuffie 的时候将数 据写到本地，下一个 Stage 要使用上一个 Stage 的数据，因此写数据的时候要告诉 Driver中的 MapOutputTrackerMaster具体写到哪里，下一个 Stage读取数据的时候也 要访问 Driver的 MapOutputTrackerMaster获取数据的具体位置。



![image-20190214115853514](/Users/weicheng/Library/Application Support/typora-user-images/image-20190214115853514.png)



![image-20190214115905954](/Users/weicheng/Library/Application Support/typora-user-images/image-20190214115905954.png)

Shuffle 她 Spark甚至整个分布式系统的性能瓶颈，



Shuffle产生 ShuffieRDD, ShuffledRDD就变成另一个 Stage, 为什么是变成另外一个 Stage?
因为要网络传输，网络传输不能在内存中进行迭代 。



#### DataSet 的代码 如何转化为RDD 

DataSet 的代码转化成为 RDD 的内部流程如下 。 

Parse SQL(DataSet)-Analyze Logical Plan-Optimize Logical Plan一 Generate Physical Plan-Prepareed Spark Plan-Execute SQL--Generate RDD 

基于 DataSet 的代码一步步转化成为 RDD: 最终调用 execute()生成 RDD。 



### Spark Driver 

SparkContext是通往 Spark栠群的唯一入口，可以用来在 Spatk集群中创建 RDDs、累加
器 (Accumulators) 和广播变炽 (BroadcastVariables) 。



SparkContext 的核心作用是初始化 Spark 应用程序运行所需要的核心组件，包括高层调
度器 (DAGScheduler入底层调度器 (TaskScheduler)和调度器的通信终端 (SchedulerBackend),
同时还会负责 Spark程序向 Master注册程序等。



在 Application 的 main方法中 ， 最开始几行编写的代码一般是这样的:首先，创建 SparkConf实例，设置 SparkConf
实例的属性，以便覆盖 Spark默认配置文件 spark-env.sh,spark-default.sh和 log4j.properties中
的参数;然后， SparkConf 实例作为 SparkContext 类的唯一构造参数来实例化 SparkContext
实例对象。 SparkContext 在实例 化的过程中 会初始化 DAGScheduler、 TaskScheduler 和
SchedulerBackend, 而当RDD的action触发了作业(Job)后，SparkContext会调用DAGScheduler
将整个 Job 划分成几个小的阶段 (Stage), TaskScheduler会调度每个 Stage 的任务 (Task) 进
行处理。还有， SchedulerBackend管理整个集群中为这个当前的 Application分配的计算资源，
即 Executor。



- Spark程序在运行时分为 Driver和 Executor两部分: Spark程序编写是基千 SparkContext 的，具体包含两方面。

- Spark 编程的核心基础 RDD 是由 SparkContext 蛟初创建的(第 一个 RDD 一定是由 SparkContext 创建的)。
- Spark 程序的调度优化也是基于 SparkContext, 首先进行调度优化。
- Spark 程序的注册是通过 SparkContext 实例化时 生 产的对象来完成的 (其实是
  ScheduJerBackend 来注册程序)。
- Spark 程序在运行时要通过 ClusterManager 获取具体的计算资源， 计算资源获取也
  是通过 SparkContext产生的对象来申诸的(其实是 SchedulerBackend 来获取计算资
  源的)。
- SparkContext 崩溃或者结束的时候，整个 Spark程序也结束 。



SparkContext 包含四大核心对象 : DAGScheduler、TaskScheduler、 SchedulerBackend、 MapOutputTrackerMaster。

StandaloneSchedulerBackend 有 三大核心功能 : 负贞与 Master 连接，注册当前程序 RegisterWithMaster; 接收集群中为当前应川程序分配的计算资源 Executor 的注册并耸理 Executors: 负责发送 Task 到 具体的 Executor 执行。







其中各个术语及相关术语的描 述如下 。 

( 1) Driver Program: 运行 Application 的 main 函数并新建 SparkContext实例的程序，称 为驱动程序 (DriverProgram)。通常可以使用 SparkContext代表驱动程序。 

(2) Cluster Manager: 集群管理器 (ClusterManager) 是集群资源管理的外部服务。 Spark 上现在主要有 Standalone、 YARN、 Mesos 3 种集群资源管理器。 Spark 自带的 Standalone 模 式能够满足绝大部分纯粹的 Spark计算环境中对栠群资源管理的需求，基本上只有在集群中 运行多套计算框架的时候才建议考虑 YARN 和 Mesos。 

9.
 \10. i Master 组件对应的类 

已 

石 

第 5 章 Spark集群启动原理和源码详解 

(3) Worker Node: 栠群中可以运行 Application 代码的 工作节点 (Worker Node), 相当 于 Hadoop 的 Slave 节点。 

(4) Executor: 在 Worker Node 上为 Application 启动的一个工作进程，在进程中负责任 务 (Task) 的运行，并且负责将数据存放在内存或磁盘上，在 Executor 内部通过多线程的方 式( 即线程池)并发处理应用程序的具体任务。 

每个 Application都有各自独立的 Executors, 因此应用程序之间是相互隔离的。 

(5) Task: 任务 (Task) 是指被 Driver送到 Executor上的工作单元。通常， 一个任务会 处理一个 Partition的数据，每个 Partition一般是一个 HDFS 的 Block块的大小。 

(6) Application: 是创建了 SparkContext 实例对象的 Spark 用 户程序，包含了一个 Driver program和集群中多个 Worker上的 Executor。 

(7 ) .Job: 和 Spark 的 action 对应，每个 action, 如 count、 savaAsTextFile 等都会对应一 个 Job 实例，每个 Job会拆分成多个 Stages, 一个 Stage 中包含一个任务栠 (TaskSet) , 任务 集中的各个任务通过一定的调度机制发送到工作单位 (Executor) 上并行执行。 

Spark Standalone栠群的部署采用典型的 Master/Slave 架构 c 其中， Master节点负责整个 集群的资源管理与调度， Worker 节点(也可以称 Slave 节点)在 Master 节点的调度下启动 Executor, 负责执行具体工作(包括应用程序以及应用程序提交的任务)。 



#### Shuffle原理

由千Shuffle涉及磁盘的读写和网络1/0

 MapReduce 框架中， Shuflle 阶段是连接 Map 和 Reduce 之间的桥梁， Map 阶段通过 Shuflle过程将数据输出到Reduce阶段中 。由千Shuffle涉及磁盘的读写和网络1/0,因此Shuffle 性能的高低直接影响整个程序的性能。 Spark 本质上 也是一种 MapReduce 框架，因此也会有
自己的 Shuffle过程实现。



![image-20190214150828311](/Users/weicheng/Library/Application Support/typora-user-images/image-20190214150828311.png)



![image-20190214151203905](/Users/weicheng/Library/Application Support/typora-user-images/image-20190214151203905.png)