# hive on spark 性能优化



性能测试方案：

- 对hive 进行聚合查询操作
- 查询700W数据

```
select packagename from dw.meta_play_game group by packagename;

[56s, 50, 86]

select packagename, max(appname) as appname, count(*) as counts from dw.meta_play_game group by packagename order by counts desc;
[120, 102, 91,    173, 150, 128.468, 120, 120]



```

现状：

​	开始一段命令的等待时间：40s,  40秒后开始执行。

​	3个实例

优化项：

```
spark.executor.cores=4
spark.executor.memory=9G
spark.yarn.executor.memoryOverhead=2g
spark.driver.memory=6g
spark.yarn.driver.memoryOverhead=1G
spark.executor.instances=
```

hive配置修改：

```
set spark.master=yarn-cluster;
set spark.executor.instances=5;
set spark.executor.cores=4;
set spark.executor.memory=8g;
set spark.yarn.executor.memoryOverhead=2g;
set spark.driver.memory=2g;
set spark.yarn.driver.memoryOverhead=1g;
set hive.prewarm.enabled=true;



------------------------------------------
hive client连接spark driver超时. 增加 hive.spark.client.future.timeout .

在hive 任务提交的时候指定队列
set mapred.job.queue.name=QueueA;
```





### 性能与配置



```
Status: Running (Hive on Spark job[0])
--------------------------------------------------------------------------------------
          STAGES   ATTEMPT        STATUS  TOTAL  COMPLETED  RUNNING  PENDING  FAILED  
--------------------------------------------------------------------------------------
Stage-0 ........         0      FINISHED     11         11        0        0       0  
Stage-1 ........         0      FINISHED     22         22        0        0       0  
--------------------------------------------------------------------------------------
STAGES: 02/02    [==========================>>] 100%  ELAPSED TIME: 56.27 s    
--------------------------------------------------------------------------------------
```





更多YARN的优化文档请查看[Tuning YARN](http://www.cloudera.com/documentation/enterprise/latest/topics/cdh_ig_yarn_tuning.html#concept_vbk_m43_fr)

### [Spark 配置](http://bihell.com/2016/04/18/hadoop-performance-management/#Spark-%E9%85%8D%E7%BD%AE)

分配好YARN的资源以后你需要对Spark的executor和driver的内存，并行数量等进行配置。



设置executor内存的时候考虑以下因素:

- executor的内存越多，查询的map join就越快，不过这样会导致内存回收压力增加。
- 在executor内核 分配过多的情况下有可能导致HDFS客户端并发写入性能下降

Cloudera建议把*spark.executor.cores* 设置为 4,5或6 这取决于你分配给了YARN多少内核。为使最小化未使用内核,



一个executor可使用的总内存为*spark.executor.memory*和*spark.yarn.executor.memoryOverhead*之和

Cloudera建议设置*spark.yarn.executor.memoryOverhead*为总内存的15-20% . 按照本例来说*spark.executor.memoryOverhead=2* G *spark.executor.memory=12* G.



**注意:确保spark.executor.memoryOverhead和spark.executor.memory总数小于yarn.scheduler.maximum-allocation-mb**



#### [配置Driver内存](http://bihell.com/2016/04/18/hadoop-performance-management/#%E9%85%8D%E7%BD%AEDriver%E5%86%85%E5%AD%98)

可以根据以下*yarn.nodemanager.resource.memory-mb的值来计算.

- 超过50G设置为12G
- 12G至50G之间设置为4G
- 1G至12G之间设置为1G
- 少于1G设置为256M

同样的*spark.yarn.driver.memoryOverhead*也应该是总数的10-15% .这个例子中*yarn.nodemanager.resource.memory-mb=100*GB, 所以总内存可以设置为12GB .也就是说 *spark.driver.memory=10.5* GB *spark.yarn.driver.memoryOverhead=1.5* GB