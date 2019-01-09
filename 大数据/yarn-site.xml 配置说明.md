# yarn-site.xml 配置说明

 注意，配置这些参数前，应充分理解这几个参数的含义，以防止误配给集群带来的隐患。另外，这些参数均需要在yarn-site.xml中配置。*

1. ResourceManager相关配置参数

- （1） `yarn.resourcemanager.address`
  参数解释：ResourceManager 对客户端暴露的地址。客户端通过该地址向RM提交应用程序，杀死应用程序等。
  默认值：${yarn.resourcemanager.hostname}:8032
- （2） `yarn.resourcemanager.scheduler.address`
  参数解释：ResourceManager 对ApplicationMaster暴露的访问地址。ApplicationMaster通过该地址向RM申请资源、释放资源等。
  默认值：${yarn.resourcemanager.hostname}:8030
- （3） `yarn.resourcemanager.resource-tracker.address`
  参数解释：ResourceManager 对NodeManager暴露的地址.。NodeManager通过该地址向RM汇报心跳，领取任务等。
  默认值：${yarn.resourcemanager.hostname}:8031
- （4） `yarn.resourcemanager.admin.address`
  参数解释：ResourceManager 对管理员暴露的访问地址。管理员通过该地址向RM发送管理命令等。
  默认值：${yarn.resourcemanager.hostname}:8033
- （5） `yarn.resourcemanager.webapp.address`
  参数解释：ResourceManager对外web ui地址。用户可通过该地址在浏览器中查看集群各类信息。
  默认值：${yarn.resourcemanager.hostname}:8088
- （6） `yarn.resourcemanager.scheduler.class`
  参数解释：启用的资源调度器主类。目前可用的有FIFO、Capacity Scheduler和Fair Scheduler。
  默认值：
  org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacityScheduler
- （7） `yarn.resourcemanager.resource-tracker.client.thread-count`
  参数解释：处理来自NodeManager的RPC请求的Handler数目。
  默认值：50
- （8） `yarn.resourcemanager.scheduler.client.thread-count`
  参数解释：处理来自ApplicationMaster的RPC请求的Handler数目。
  默认值：50
- （9） `yarn.scheduler.minimum-allocation-mb/ yarn.scheduler.maximum-allocation-mb`
  参数解释：单个可申请的最小/最大内存资源量。比如设置为1024和3072，则运行MapRedce作业时，每个Task最少可申请1024MB内存，最多可申请3072MB内存。
  默认值：1024/8192
- （10） `yarn.scheduler.minimum-allocation-vcores / yarn.scheduler.maximum-allocation-vcores`
  参数解释：单个可申请的最小/最大虚拟CPU个数。比如设置为1和4，则运行MapRedce作业时，每个Task最少可申请1个虚拟CPU，最多可申请4个虚拟CPU。什么是虚拟CPU，可阅读我的这篇文章：“YARN 资源调度器剖析”。
  默认值：1/32
- （11） `yarn.resourcemanager.nodes.include-path /yarn.resourcemanager.nodes.exclude-path`
  参数解释：NodeManager黑白名单。如果发现若干个NodeManager存在问题，比如故障率很高，任务运行失败率高，则可以将之加入黑名单中。注意，这两个配置参数可以动态生效。（调用一个refresh命令即可）
  默认值：“”
- （12） `yarn.resourcemanager.nodemanagers.heartbeat-interval-ms`
  参数解释：NodeManager心跳间隔
  默认值：1000（毫秒）

1. NodeManager相关配置参数

- （1） `yarn.nodemanager.resource.memory-mb`
  参数解释：NodeManager总的可用物理内存。注意，该参数是不可修改的，一旦设置，整个运行过程中不可动态修改。另外，该参数的默认值是8192MB，即使你的机器内存不够8192MB，YARN也会按照这些内存来使用（傻不傻？），因此，这个值通过一定要配置。不过，Apache已经正在尝试将该参数做成可动态修改的。
  默认值：8192
- （2） `yarn.nodemanager.vmem-pmem-ratio`
  参数解释：每使用1MB物理内存，最多可用的虚拟内存数。
  默认值：2.1
- （3） `yarn.nodemanager.resource.cpu-vcores`
  参数解释：NodeManager总的可用虚拟CPU个数。
  默认值：8
- （4） `yarn.nodemanager.local-dirs`
  参数解释：中间结果存放位置，类似于1.0中的mapred.local.dir。注意，这个参数通常会配置多个目录，已分摊磁盘IO负载。
  默认值：${hadoop.tmp.dir}/nm-local-dir
- （5） `yarn.nodemanager.log-dirs`
  参数解释：日志存放地址（可配置多个目录）。
  默认值：${yarn.log.dir}/userlogs
- （6） `yarn.nodemanager.log.retain-seconds`
  参数解释：NodeManager上日志最多存放时间（不启用日志聚集功能时有效）。
  默认值：10800（3小时）
- （7） `yarn.nodemanager.aux-services`
  参数解释：NodeManager上运行的附属服务。需配置成mapreduce_shuffle，才可运行MapReduce程序
  默认值：“”

 