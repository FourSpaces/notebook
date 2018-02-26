## Kafka

Kafka 消息系统，作为多种类型的数据管道和消息系统使用。

是一种分布式的，基于发布/订阅的消息系统。



- 活动流数据：包括页面访问量，被查看内容方面的信息以及搜索情况内容。

  这种数据通常的处理方式是先把各种活动以日志的形式写入某种文件，然后周期性地对这些文件进行统计分析。

- 运营数据：服务器的性能数据（CPU、IO使用率、请求时间、服务日志等等数据)。



#### Kafka架构

- Broker

  Kafka集群包含一个或多个服务器，这种服务器被称为broker

- Topic

  每条发布到Kafka集群的消息都有一个类别，这个类别被称为Topic。（物理上不同Topic的消息分开存储，逻辑上一个Topic的消息虽然保存于一个或多个broker上但用户只需指定消息的Topic即可生产或消费数据而不必关心数据存于何处）

- Partition

  Parition是物理上的概念，每个Topic包含一个或多个Partition.

- Producer

  消息生产者，负责发布消息到Kafka broker

- Consumer

  消息消费者，向Kafka broker读取消息的客户端。

- Consumer Group

  每个Consumer属于一个特定的Consumer Group（可为每个Consumer指定group name，若不指定group name则属于默认的group）。

#### Kafka 拓扑结构

![Kafka 拓扑结构](http://cdn1.infoqstatic.com/statics_s1_20170816-0412/resource/articles/kafka-analysis-part-1/zh/resources/0310020.png)



#### Kafka

- **Topics/logs**

一个Topics 可以认为是一类消息，每个topic将被分成多个partition(区)。

每个partition 在存储层中表现为 append log  文件，发布到此partition的消息被追加到log 文件的尾部。

每条消息在文件中的位置称为offset(偏移量)，offset是一个long型数字，唯一标记一条消息，kafka中几乎不允许对消息进行随机读写

![Topics](http://www.aboutyun.com/data/attachment/forum/201409/28/143553t3nhnsbri6s6nfh5.png?_=3999538)



- **Kafka 中的消息文件清除机制：**

​       日志文件会根据broker 中的配置要求，保留一定时间后删除。并不管消息是否消费。

​        kafka通过这种简单的手段,来释放磁盘空间,以及减少消息消费之后对文件内容改动的磁盘IO开支.

-  **consumer**

  consumer 控制消费消息的offset的保存和使用。

  当consumer 正常消费消息时，offset 将会“线性”的向前驱动，消息将被顺序消费。

  它只需要将offset重置为任意值，即可实现任意顺序消费消息。

  ​

- Partitions

  通过分区(Partition),可以将日志内容分散到多个[server](http://cpro.baidu.com/cpro/ui/uijs.php?rs=1&u=http%3A%2F%2Fwww%2Eaboutyun%2Ecom%2Fthread%2D9341%2D1%2D1%2Ehtml&p=baidu&c=news&n=10&t=tpclicked3_hc&q=92051019_cpr&k=server&k0=java&kdi0=8&k1=%B1%E0%B3%CC&kdi1=8&k2=%BF%CD%BB%A7%B6%CB&kdi2=8&k3=%C9%E8%BC%C6&kdi3=8&k4=server&kdi4=1&sid=4ebca4a25f27e407&ch=0&tu=u1692056&jk=fb2f0911808fa875&cf=29&fv=14&stid=9&urlid=0&luki=5&seller_id=1&di=128)上,来避免文件尺寸达到单机磁盘的上限,每个partiton都会被当前server(kafka实例)保存; 

  此外越多的partitions意味着可以容纳更多的consumer,有效提升并发消费的能力.(具体原理参见下文).

  ​

- **zookeeper**

  ​        kafka集群几乎不需要维护任何consumer和producer状态信息,这些信息有zookeeper保存;因此producer和consumer的[客户端](http://cpro.baidu.com/cpro/ui/uijs.php?rs=1&u=http%3A%2F%2Fwww%2Eaboutyun%2Ecom%2Fthread%2D9341%2D1%2D1%2Ehtml&p=baidu&c=news&n=10&t=tpclicked3_hc&q=92051019_cpr&k=%BF%CD%BB%A7%B6%CB&k0=java&kdi0=8&k1=%B1%E0%B3%CC&kdi1=8&k2=%BF%CD%BB%A7%B6%CB&kdi2=8&k3=%C9%E8%BC%C6&kdi3=8&k4=server&kdi4=1&sid=4ebca4a25f27e407&ch=0&tu=u1692056&jk=fb2f0911808fa875&cf=29&fv=14&stid=9&urlid=0&luki=3&seller_id=1&di=128)实现非常轻量级,它们可以随意离开,而不会对集群造成额外的影响.

- Distribution

  一个Topic的多个partitions,被分布在kafka集群中的多个server上;

  每个server(kafka实例)负责partitions中消息的读写操作;

  此外kafka还可以配置partitions需要备份的个数(replicas),每个partition将会被备份到多台机器上,以提高可用性.

  ​

- Producers

  ​       Producer将消息发布到指定的Topic中,同时Producer也能决定将此消息归属于哪个partition;

  ​	比如基于"round-robin"方式或者通过其他的一些算法等.

- Consumers

  ​	每个consumer属于一个consumer group，一个group可以有多个consumer.

  ​	发送到Topic的消息,只会被订阅此Topic的每个group中的一个consumer消费.

   	kafka的[设计](http://cpro.baidu.com/cpro/ui/uijs.php?rs=1&u=http%3A%2F%2Fwww%2Eaboutyun%2Ecom%2Fthread%2D9341%2D1%2D1%2Ehtml&p=baidu&c=news&n=10&t=tpclicked3_hc&q=92051019_cpr&k=%C9%E8%BC%C6&k0=java&kdi0=8&k1=%B1%E0%B3%CC&kdi1=8&k2=%BF%CD%BB%A7%B6%CB&kdi2=8&k3=%C9%E8%BC%C6&kdi3=8&k4=server&kdi4=1&sid=4ebca4a25f27e407&ch=0&tu=u1692056&jk=fb2f0911808fa875&cf=29&fv=14&stid=9&urlid=0&luki=4&seller_id=1&di=128)原理决定,对于一个topic,同一个group中不能有多于partitions个数的consumer同时消费,否则将意味着某些consumer将无法得到消息.

- Guarantees

​    1) 发送到partitions中的消息将会按照它接收的顺序追加到日志中

​    2) 对于消费者而言,它们消费消息的顺序和日志中消息顺序一致.

​    3) 如果Topic的"replicationfactor"为N,那么允许N-1个kafka实例失效.



#### 使用场景

​    1、Messaging   

​	对于一些常规的消息系统,kafka是个不错的选择;partitons/replication和容错,可以使kafka具有良好的扩展性和性能优势.不过到目前为止,我们应该很清楚认识到,

​	kafka并没有提供JMS中的"事务性""消息传输担保(消息确认机制)""消息分组"等企业级特性;kafka只能使用作为"常规"的消息系统,

​	在一定程度上,尚未确保消息的发送与接收绝对可靠(比如,消息重发,消息发送丢失等)

​    2、Websit activity tracking

​    	kafka可以作为"网站活性跟踪"的最佳工具;可以将网页/用户操作等信息发送到kafka中.并实时监控,或者离线统计分析等

​    3、Log Aggregation

​    	kafka的特性决定它非常适合作为"日志收集中心";

​	application可以将操作日志"批量""异步"的发送到kafka集群中,而不是保存在本地或者DB中;kafka可以批量提交消息/压缩消息等,这对producer端而言,几乎感觉不到性能的开支.此时consumer端可以使hadoop等其他系统化的存储和分析系统.



####消息传送机制

​    对于JMS实现,消息传输担保非常直接:有且只有一次(exactly once).在kafka中稍有不同:

​    1) at most once: 最多一次,这个和JMS中"非持久化"消息类似.发送一次,无论成败,将不会重发.

​    2) at least once: 消息至少发送一次,如果消息未能接受成功,可能会重发,直到接收成功.

​    3) exactly once: 消息只会发送一次.

​    at most once: 消费者fetch消息,然后保存offset,然后处理消息;当client保存offset之后,但是在消息处理过程中出现了异常,导致部分消息未能继续处理.那么此后"未处理"的消息将不能被fetch到,这就是"at most once".

​    at least once: 消费者fetch消息,然后处理消息,然后保存offset.如果消息处理成功之后,但是在保存offset阶段zookeeper异常导致保存操作未能执行成功,这就导致接下来再次fetch时可能获得上次已经处理过的消息,这就是"at least once"，原因offset没有及时的提交给zookeeper，zookeeper恢复正常还是之前offset状态.

​    exactly once: kafka中并没有严格的去实现(基于2阶段提交,事务),我们认为这种策略在kafka中是没有必要的.

​    通常情况下"at-least-once"是我们搜选.(相比at most once而言,重复接收数据总比丢失数据要好).





