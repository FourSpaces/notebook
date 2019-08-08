## yarn

Yarn 是Hadoop的集群资源管理系统。提供了请求和使用集群资源的API。

#### yarn 应用运行机制

yarn的两类长期运行的守护进程为自己提供核心服务

- 资源管理器(resource manager): 管理集群上资源的使用
- 节点管理器(node manager): 运行在集群中所有节点上且能够启动和监控容器(container)

容器用于执行特定应用程序的进程，每个都有资源限制（内存、CPU）,

一个容器可以是 一个 Unix进程， 也可以是一个Linux cgroup, 取决于yarn 的配置

![image-20190228200828538](/Users/weicheng/Library/Application Support/typora-user-images/image-20190228200828538.png)

1、客户端联系资源管理器，要求它运行一个 application master 进程。

2、 资源管理器找到一个能够在容器中启动 application master 的节点管理器

3、 应用运行，有可能将结果返回给客户端，或者向资源管理器请求更多的容器。

4、将更多的容器用于进行分布式计算



#### 资源请求

可以指定每个容器需要的计算机资源数量，还可以指定对容器的本地限制要求。

yarn 允许一个应用为所申请的容器指定本地限制，可以申请位于指定节点、机架、集群中的任何位置。

yarn 应用可以在运行中的任意时刻提出资源申请，最开始可以提出所有的请求，或者更为动态的方式在需要更多资源的时候提出请求。



#### 应用生命期模型

**单个用户作业对应一个应用**：MapReduce采取的方式

**作业的每个工作流或每个用户对话对应一个应用**：容器直接可以在作业间重用，并可能缓存作业之间的中间数据，spark采用的就是这种模型。

**多个用户共享一个长期运行的应用**：可以让用户获得非常低延迟的查询响应。



#### yarn 的优点

- 可扩展性（Scalability）可以扩展到10000个节点 和 100000个任务。
- 可用性（Availability）yarn 在资源管理器和application master之间进行了职责划分，为资源管理器提供了高可用性
- 利用率（Utilization）yarn的资源是精细话管理的，这样的应用能够按需请求资源，充分利用资源。
- 多租户（Multitenancy）



#### yarn 中的调度

**YARN 中的调度器：**

- FIFO 调度器(FIFO Scheduler)

- 容量调度器(Capacity Scheduler)

- 公平调度器(Fair Scheduler)

  

FIFO 调度器将应用放置在一个队列中，按提交顺序运行应用，第一个应用的请求被满足后再依次为队列中的下一个应用服务。

![image-20190228204522875](/Users/weicheng/Library/Application Support/typora-user-images/image-20190228204522875.png)



使用FIFO调度器时候，小作业一直被阻塞，直到大作业完成。

使用容量调度时，可以分成多个队列来运行作业

使用公平调度器时，不需要预留资源，因为调度器会在所有运行的作业直接动态平衡资源。



#### 容量调度器



假设的capacity 队列结构

```
root
 |---- prod
 |---- dev
 		|---- eng
 		|---- science
```

配置文件

文件名为：capacity-scheduler.xml, 在root 队列下定义两个队列：prod 和 dev, 分别占 40% 与 60%的容量。

注意：对特定队列进行配置时，是通过以下形式的配置属性 yarn.scheduler.capacity.<queue-path>.<sub-property> 进行设置的，其中 <queue-path> 表示队列的参差路径，例如 root.prod

```
<?xml version="1.0"?>
<configuration>
	<property>
		<name>yarn.scheduler.capacity.root.queues</name>
		<vlaue>prod,dev</value>
	</property>
	<property>
		<name>yarn.scheduler.capacity.root.dev.queues</name>
		<value>eng,science</value>
	</property>
	<property>
		<name>yarn.scheduler.capacity.root.prod.capacity</name>
		<value>40</value>
	</property>
	<property>
		<name>yarn.scheduler.capacity.root.dev.capacity</name>
		<value>60</value>
	</property>
	<property>
		<name>yarn.sheduler.capacity.root.dev.maximum-capacity</name>
		<value>75</value>
	</property>
	<property>
		<name>yarn.sheduler.capacity.root.dev.eng.capacity</name>
		<value>50</value>
	</property>
	<property>
		<name>yarn.sheduler.capacity.root.dev.science.capacity</name>
		<value>50</value>
	</property>
</configuration>
```

可以看出， dev 队列被划分成了两个容量相等的队列eng  和 science.

dev队列的最大容量被设置为75%，因此即使prod 队列空闲，dev也不会将整个集群的资源用完。

prod队列则可能会占用全集群的资源。dev的两个子队列可能会占满集群的75%的资源



除了配置队列层次和容量，还可以控制单个用户或应用能被分配到的最大资源数量、同时运行的任务数量。

队列的ACL认证。



将队列放置在哪个队列中，取决于应用本身，不指定队列，会使用默认default队列

- MapReduce中：设置属性mapreduce.job.queuename来指定队列。
- spark中：



#### 公平调度器

为所有运行的应用公平分配资源。

1、启用公平调度器

​     需要 yarn-site.xml 文件中的 yarn.resourcemanager.scheduler.class 设置为公平调度器的完全限定名：org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairScheduler

​     需要 yarn-site.xml 文件中的 yarn.scheduler.fair.allocation.file 设置为    FairScheduler队列的配置文件路径，这里为：/usr/local/webserver/hadoop-2.9.1/etc/hadoop/fair-scheduler.xml

2、队列配置

```
<?xml version="1.0"?>
<allocations>
	<defaultQueueSchedulingPolicy>fair</defaultQueueSchedulingPolicy>
	<queue name="prod">
		<weight>40</weight>
		<schedulingPolicy>fifo</schedulingPolicy>
	</queue>
	<queue name="dev">
		<weight>60</weight>
		<queue name="eng" />
		<queue name="science" />
	</queue>
	<!-- 队列放置规则设置 -->
	<queuePlacenebtPolicy>
		<!-- specified 表示将应用放入指明的队列中，如果指明队列不存在，尝试下一个规则 -->
		<!-- primaryGroup 表示将应用放入以用户的主Unix组名命名的队列中 -->
		<!-- default 是一个兜底规则，当前述规则不匹配时，将启用该条规则 -->
		<rule name="specified" create="fales" />
		<rule name="primaryGroup" create="fales" />
		<rule name="default" queue="dev.eng" />
	</queuePlacenebtPolicy>
</allocations>
```

队列的默认调度策略可以通过顶层元素defaultQueueSchedulingPolicy设置，省略会采用公平策略。公平调度器也支持队列级别的FIFO(fifo) 策略，以及drf策略。

队列的调度策略可以被该队列的schedulingPolicy元素指定的策略覆盖。

**抢占**

允许调度器终止那些占用资源超过了其公平共享份额的队列的容器，这些容器资源释放后可以分配给资源数量低于应得份额的队列。抢占会降低整个集群的效率，因为被终止的containers需要重新执行。

将yarn.scheduler.fair.preemption 设置为 true，可全面启用抢占功能。有两个相关的抢占超时设置：

- 最小共享(minimum share preemption timeout)
- 公平共享(fair share preemption timeout)

两者设定时间均为秒级，默认两个超时参数都不设置，为来允许抢占容器，至少设置一个。



#### 延迟调度

当调度请求来临时，等待一小段时间后，可以增加在所请求节点上分配到容器的机会，提高集群效率。

对于容量调度器，可以通过设置 yarn.sheduler.capacity.node-locality-delay来配置延迟调度，设置为正整数，表示调度器准备错过的调度机会，

公平调度器，使用调度机会的数量来决定延迟时间，不过使用集群规模的比例来表示这个值。例如将yarn.scheduler.fair.locality.threshold.node设置为0.5 表示调度器在接受同一机架中的其他节点之间，将一直等待直到集群中的一半节点都给过调度机会。



#### 主导资源公平性（DRF）

当有多种资源类型需要度量时，就会比较复杂。例如一个用户的应用对CPU的需求量大，但是对内存的需求量少。而另一个用户需要很少的CPU，但对内存需求量很大，那么如何比较两个应用。

yarn 中调度器解决这个问题的思路是：观察每个用户的主导资源，并将其作为对集群资源使用的一个度量。

![image-20190301102233328](/Users/weicheng/Library/Application Support/typora-user-images/image-20190301102233328.png)



























