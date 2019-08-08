## spark 大数据分析读书笔记

```
withColumn("user", lit(userId))
// 添加或替换列，这里 lit 不知道啥意思s
```

-

### Spark 调优

#### 运行环境 jar 包管理及数据本地性调优

Spark中的数据本地性有以下 5种

- PROCESS _LOCAL: 进程本地化。代码和数据在同一个进程中 ， 也就是在同 一个Executor 中;计算数据的 Task 由 Executor 执行，数据在 Executor 的 BlockManager中;性能最好。

- NODE_LOCAL: 节点本地化:代码和数据在同一个节点中，数据作为一个 HDFS block 块，就在节点上，而 Task 在节点上某个 Executor 中运行;或者是数据和 Task 在一 个节点上的不同 Executor 中;数据需要在进程间进行传输。也就是说，数据虽然在 同- Worker 中， 但不是同一 NM 中。这隐含巷进程间移动数据的 开销。 
- NO_PREF: 数据没有局部性首选位置它能从任何位臂同等访问。对千 Task 来说， 数据从哪里获取都一样，无好坏之分。 
- RACK—LOCAL: 机架本地化。数据在不同的服务器上，但在相同的机架。数据衙要 通过网络在节点之间进行传输。 
- ANY: 数据在不同的服务器及机架上面。这种方式性能最差。 

Spark 应用程序本身包含代码和数据两部分， 通常，读取数据要尽量使数据以 PROCESS_LOCAL 或 NODE_LOCAL 方式读取。其中， PROCESS_LOCAL 还和 Cache有关，如果 RDD 经常用，应将该 RDD Cache 到内存中。注意， 由千 Cache 是 Lazy 级别的，所以必须通过一个 Action 的触发，才能真正地将该 RDD Cache 到内存中。 

#### 调优实践

1、配置 spark.yarn.jars, 设置 yarn的缓存清理间隔

```

spark-default.conf中配置spark.yarn.jars指向hdfs上的spark需要的jar包。如果不配置该参数，每次启动spark程序将会将driver端的SPARK_HOME打包上传分发到各个节点。

缓存清理间隔在yarn-site.xml通过yarn.nodemanager.localizer.cache.cleanup.interval-ms配置
默认为 600000


```



2、 调整Task 本地化级别

```

```



#### Spark on YARN 两种不同的调度模式以及优化

 Sparkon YARN 的两种不同类型模型 (YARN-Client模式、YARN-Cluster模式 )

```

```



#### YARN 队列资源不足引起的Spark 应用程序失败的原因及调优

```

```



#### Spark on YARN 模式下Executor经常被杀死的原因及调优方案

```

```







Spark.Executor.memory 来配置每个 Executor使用的内存总型



Task通过 Shuffle过程拉取了上一个 Stage的 Task的输出后，默认也占 Executor 总内存的 20%;

用 Spark.Shuffle.memoryFraction 可配笠比例 。

第三块是让 RDD Cache 使用，默认占 Executor 总内存的 60%; 用 Spark.storage.memoryFraction可配比例，

如果频繁发生Full GC,, 可以考虑降低这个比值，

如果频繁发生Minor GC,, 可以考虑降低这个比值



Spark.YARN.Executor.memoryOverhcad



```
spark.shuffle.file=32kb
spark.shuffle.io.maxRetries =30 
spark.shuffle.io.retryWait =30s
```



Shuftle 的过程中会产生大量的磁盘 I/0、网络 I/0, 以及压缩、解压缩、序列化和反序列化的操作，这一系列操作对性能都是一个很大的 负担。