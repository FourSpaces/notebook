## 常识

#### MapReduce

MapReduce 是一种可用于数据处理的编程模式，MapReduce 本质上是并行的

MapReduce 任务过程分为两个处理阶段：

- map 阶段，[数据准备阶段]

- reduce 阶段，[数据处理阶段]

每个阶段都以兼职对作为输入和输出。程序员主需要写两个函数：map 函数 和 reduce 函数。

![image-20190226190656324](/Users/weicheng/Library/Application Support/typora-user-images/image-20190226190656324.png)

集群上的可用贷款限制了MapReduce作业的数量，应尽量避免map 和reduce 任务之间的数据传输。

#### job

MapReduce作业(job) 是客户端需要执行的一个工作单元，包括

- 输入数据

- MapReduce 程序

- 配置信息



#### task

Hadoop 将作业分成若干个任务(task)来执行，主要包括两类：

- map 任务
- reduce 任务

通过 YARN进行调度，如果一个任务失败，它将在另一个不同的节点上重新调度运行

#### input split

Hadoop 将MapReduce的输入数据划分成等长的小数据块，成为输入分片(input split).

Hadoop 为每个分片构建一个map  任务，并由该任务来运行用户自定义的map函数从而处理分片中的记录

分片太大，意味处理每个分片所花的时间会增大。

分片太小，管理分片的总时间和构建map任务的总时间，决定作业的整个执行时间。

合理的分片，趋向于HDFS的一个块的大小，默认是128M

数据本地优化：Hadoop 在存储有输入数据的节点上运行map任务，可以获得最佳性能。[无需只有带宽]

最佳分片大小与块大小相同，如果分片跨越两个数据块，就会造成分片中的数据需要通过网络传输到任务节点。

Map 任务将输出结果写入本地硬盘，而非HDFS的原因？

map输出是中间结果，中间结果，经过 reduce 任务处理后，才产生最终输出结果，作业完成中间结果也就没有了用途，会被删掉。

Reduce 任务并不具备数据本地化的优势，

单个reduce 任务的熟人通常来自于所有mapper的输出，因此将结果输出到HDFS 实现可靠存储。



分区可以由用户定义的分区函数控制，但通常用默认的partitioner 通过哈希函数来分区，高效



#### shuffle(混洗)

map任务和reduce任务之间的数据流，被称为 shuffle。

每个 reduce任务的输入来自许多map  任务，调整混洗参数对作业总执行时间的影响非常大。

数据处理完全可以安全并行（无需混洗时），可能会出现无reduce任务的情况。



#### combiner 函数

Hadoop 允许用户针对map 任务的输出指定一个combiner（像mapper 和reducer 一样），combiner函数的输出作为reduce 函数的输入。

由于combiner 属于优化方案，不管Hadoop 调用combiner 多少次，reducer 的输出结果都是一样的。

例子：

计算最高气温的例子，1950年的读数由两个map 任务处理(因为它们在不同的分片中)，

第一个map的输出如下：

(1950, 0)

(1950, 20)

(1950, 10)

第二个 map 的输出如下：

(1950, 25)

(1950, 15)

reduce函数被调用时，输入如下：

(1950, [0, 20, 10, 25, 15])

因为25为该列数据中最大的，所以它的输出为：(1950, 50)

我们可以像使用reduce 函数那样，使用combiner找出每个map 任务输出结果中的最高气温，这样reduce函数调用时，将被传入以下数据：

(1950, [20, 25])

reduce输出结果和以前一样， combiner 函数能够减少mapper和reducer之间的数据传输量。



#### Streaming 

Hadoop Streaming使用 Unix  标准流作为 hadoop和应用程序之间的接口。

Streaming天生适合用于文本处理。map的输入数据通过标准输入流传递给map函数，并且是一行一行的传输，最后将结果行写入到标准输出



#### partition

partition 分区 

### Hadoop 分布式文件系统

#### HDFS

HDFS的构建思路: 一次写入，多次读取，是最高效的访问模式。

低时间延迟的数据访问，不适合在HDFS上运行，HDFS是为高数据吞吐量应用优化的，所以会以提高时间延迟为代价

namenode 将文件系统的元数据存储在内存中，因此该文件系统所能存储的文件总数受限于 namenode的内存容量。

每个文件、目录和数据块的存储信息大约占150个字节，如果有100W个文件，每个文件一个数据块，至少会占据300M的内存。

HDFS中的文件写入只支持单个写入者，而且写操作总是以"只添加"方式在文件末尾写数据。不支持多个写入者的操作，也不支持在文件的任意位置进行修改。



**数据块**：

df 和 fsck 可以用来维护文件系统，对系统中的块进行操作。

HDFS中也有块(block)的概念，默认为128M. HDFS 上的文件被划分为块大小的多个分块。

HDFS中小于一个块大小的文件不会占据整个块的空间。

HDFS中的块比磁盘的块大，目的是为了最小化寻址开销。如果块足够大，从磁盘传输数据的时间会明显大于定位这个块开始位置所需的时间。



**对于分布式系统中的块进行抽象的好处：**

- 一个文件的大小可以大于网络中的任意一个磁盘的容量。
- 使用抽象块作为存储单元，大大简化了存储子系统的设计。
- 适合用于数据备份，提供数据容错能力，提高可用性。

```
# HDFS 中的 fsck指令可以显示块信息
## 列出文件系统中各文件由哪些块构成
hdfs fsck / -files -blocks
```



**namenode 和 datanode**

HDFS 集群由两类节点  以管理节点-工作节点模式运行，即一个namenode(管理节点) 和 多个 datanode（工作节点）。

- Namenode 管理文件系统的命名空间，维护文件系统数和整颗数内所有文件和目录，并用两个文件形式永久保存在本地磁盘上，分别是[ 命名空间镜像文件 和 编辑日志文件]。

  Namenode 也记录了每个文件中各个块坐在的数据节点信，并步永久保存块的位置信息，因为这些信息会在系统启动时根据数据节点信息重建

  **客户端(client)** 代表用户通过与namenode 和datanode 交互来访问整个文件系统。



- Datanode 是文件系统的工作节点，它们根据需要存储并检索数据块（受客户端或namenode 调度），并定期向namenode   发送它们所存储的块的列表



如果没有namenode,  文件系统将无法使用。因此对namenode 实现容错非常重要，hadoop提供了两种机制。

- 第一种机制是备份那些组成文件系统元数据持久状态的文件，通过配置使namenode在多个文件系统上保存元数据的持久状态。一般的配置是 将持久状态写入本地磁盘的同时，写入一个远程挂载的网络文件系统（NFS）
- 另一种可行的方法是运行一个辅助namenode, 这个辅助namenode 的重要作用是定期合并编辑日志与命名空间镜像，以防止编辑日志过大。它会保存合并后的命名空间镜像的副本，并在namenode发生故障时启用。



#### 块缓存

Datanode 从磁盘中读取块，对于访问频繁的文件，其对应的块可能被显示的缓存在 datanode的内存中，以堆外块缓存(off-heap block cache)的形式存在。默认情况下，一个块仅缓存在一个datanode的内存中。作业调度器通过在缓存块的datanode 上运行任务，可以利用块的优势提高读操作的性能。

例如，连接(join)操作中使用的一个小的查询表就是块缓存的一个很好的候选。

用户或者应用通过在等**缓存池(cache pool)**中增加一个 cache directive 来告诉 namenode 需要缓存哪些文件及存多久。缓存池是一个用于管理缓存权限和资源使用的管理性分组。



#### 联邦HDFS

Namenode 在内存中保存文件系统中每个文件 和 美国数据块的引用关系，意味着对于一个拥有大量文件的超大集群来说，内存将成为限制系统横向扩展的瓶颈。在2.x 发行版本系列中引入的联邦HDFS允许系统通过添加namenode 实现扩张，其中每个nemenode管理文件系统命名空间中的一部分。例如一个namenode可能管理/user 目录下的所有文件，另一个namenode可能管理/share  目录下的所有文件。

每个namenode维护一个命名空间卷，由命名空间的元数据和一个数据块池组成，数据块池包含该命名空间下文件的所有数据块。



#### HDFS HA 高可用

配置一对活动-备用(active-standby) namenode，当活动 namenode失败，备用namenode  就会接管它的任务，并开始服务于来自客户端的请求。

- Namenode  之间需要通过高可用共享存储实现编辑日志的共享。　
- Datanode 需要同时向两个namenode  发送数据块处理报告，因为数据块的映射信息存储在 namenode 的内存中，而非磁盘
- 客户端需要使用特定的机制来处理namenode的实效问题。
- 辅助namenode的角色被备用namenode 所包含，备用namenode 为活动的namenode命名空间设置周期性检查点。

有两种高可用性共享存储，NFS过滤器或群体日志管理器(QJM)

QJM是一个专用的HDFS实现，为提供一个高可用的编辑日志而设计，以一组日志节点(journalnode)的形式运行，每次编辑必须写入多数日志节点。有三个jourbal节点，所以可以忍受其中任何一个的丢失。

但是QJM的实现并没有使用Zookeeper, HDFS HA 在选取活动的namenode的确实使用了Zookeeper技术。



#### 故障切换与规避

故障转移控制器，管理着将活动namenode转移为备用namenode 的转换过程。每个namenode 运行着一个轻量级的故障转移控制器，其工作就是监视宿主 namenode是否失效,并在namenode失效时进行故障切换。

在网速慢或者网络被分割的情况下，也可能会激发故障转移。

同一时间 QJM仅仅允许一个 namenode 向编辑日志中写入数据。

使用NFS过滤器实现共享编辑日志时，由于不可能同一时间只允许一个namenode写入数据(这也是为啥推荐QJM的原因)，因此需要更有力的规避的方法。

HDFS URI使用一个逻辑主机名，该主机名映射到一对namenode地址，客户端类库会访问每一个 namenode地址直至处理完成。



#### HDFS常用接口

fs.defaultFS：设置为 hdfs://localhost/， 用于设置Hadoop 的默认文件系统，客户端，将通过该属性得知namenode 在哪里运行，进而连接到它

dfs.replication: HDFS 的文件系统块数

![image-20190228122911399](/Users/weicheng/Library/Application Support/typora-user-images/image-20190228122911399.png)

第1列显示的是文件模式，

第2列是这个文件的备份数

第3列和第4列显示文件的所属用户和组别

第5列是文件的大小，以字节为单位

第6列和第7列为文件的最后修改日期和时间

第8列是文件或目录的名称

**权限**

只读(r), 写入(w),可执行(x)

读取文件或列出目录内容时需要只读权限

写入一个文件或是在一个目录上新建及删除文件或者目录，需要写入权限。

可执行权限，在访问一个目录的子项时需要该权限



每个文件和目录都有所属用户(owner)，所属组别(group)及模式(mode).

 这个模式由所属用户的权限、组成成员的权限及其他用户的权限组成的。

安全模式：启用安全模式

启用权限控制，参加 dfs.permissions.enabled属性，会检查所属用户权限，以确认客户端的用户名与所属用户是否匹配

super-user( 超级用户)，namenode进程的标识，对于超级用户，系统不会执行任何权限检查。

#### 接口

通过 HTTP 来访问HDFS 有两种方法：

- 直接访问

  文件元数据操作由namenode 管理，文件读(写)操作首先发往 namenode,由 namenode发送一个HTTPc重定向至某个客户端，指示以流方式传输文件数据的目的 或 源 datanode

- 通过代理访问



#### 文件操作

**文件读取**

![image-20190228125602620](/Users/weicheng/Library/Application Support/typora-user-images/image-20190228125602620.png)

**文件写入**

![image-20190228130411350](/Users/weicheng/Library/Application Support/typora-user-images/image-20190228130411350.png)

#### 网络拓扑

Hadoop 无法自动发现你的网络拓扑结构，如果网络只有一层，或者所以节点都在同一数据中心的同一机架上，不需要配置



#### 一致模型

文件系统的一致模型描述了文件读/写的数据可见性，HDFS  为性能牺牲了一些 POSIX的要求。

- 新建文件后，它在文件系统的命名空间立刻可见。
- 写入文件的内入不保证能立即可见，即使数据流已经刷新并存储，所以文件长度显示为0.
- 当写入的数据超过一个块后，第一个数据块对新的reader就是可见的，当前正在写入的块对其他reader 不可见。

hflush() 可以将数据刷新，写入管道。但不保证datanode已经将数据写到磁盘上，仅保证数据在 datanode 的内存中，

hsync()为确保数据写到磁盘上，我们可以在数据流同步后看到文件内容。



 #### distcp 并行复制数据

 distcp 可以并行从 Hadoop 文件系统中复制大量数据，也可以将大量数据复制到hadoop 中。

Distcp 的另一种用法是替代Hadoop fs -cp

```
# 将file1 复制为 file2
hadoop distcp file1 file2

# 将dir1 目录 复制到 dir2
hadoop distcp dir1 dir2

# 如果dir2 不存在，则新建dir2,目录dir1 的内容全部复制到dir2下，可以指定多个源路径，所有源路径下的内容都将被复制到目标路径下。

# 如果dir2 已经存在，那么目录dir1 将被复制到dir2下，形成目录结构 dir2/dir1,
使用 -overwrite 选项，在保持同样的目录结构的同时强制覆盖原有文件。
使用 -update 选型， 仅更新发生变化的文件。 
```

distcp 用于复制大文件。

```
[root@hadoop12 ~]# hadoop distcp
usage: distcp OPTIONS [source_path...] <target_path>
              OPTIONS
 -append                       重用目标文件中的现有数据，并在可能的情况下向其添加新数据
 -async                        应该阻止distcp执行
 -atomic                       提交所有更改或不提交
 -bandwidth <arg>              以MB为单位指定每个map的带宽
 -blocksperchunk <arg>         如果设置为正值，则具有多于此值的块的文件将被拆分为
 							<blocksperchunk>块的块，以便并行传输，并在目标上重新组装。
                            默认情况下， <blocksperchunk>为0，文件将完整传输而不进行
                            拆分。 此开关仅在源文件系统实现getBlockLocations方法且
                            目标文件系统实现concat方法时适用
 -copybuffersize <arg>         要使用的复制缓冲区的大小。 
 							默认情况下<copybuffersize> 是 8192B.
 -delete                       从目标中删除，源中缺少文件。 删除仅适用于更新或覆盖选项
 -diff <arg>                   使用快照差异报告来识别源和目标之间的差异
 -f <arg>                      需要复制的文件列表
 -filelimit <arg>              （已弃用！）限制复制到<= n的文件数
 -filters <arg>                包含要从副本中排除的路径的字符串列表的文件的路径。
 -i                            复制期间忽略失败
 -log <arg>                    DFS上保存distcp执行日志的文件夹
 -m <arg>                      要用于复制的最大并发数
 -mapredSslConf <arg>          配置ssl配置文件，与hftps://.配合使用。 必须在类路径中。
 -numListstatusThreads <arg>   用于构建文件列表的线程数（最多40个）。
 -overwrite                    覆盖目标文件，强制的，即使它们存在。
                               
 -p <arg>                      保留状态（rbugpcaxt）（复制，块大小，用户，组，
 							权限，校验和类型，ACL，XATTR，时间戳
 							   preserve status (rbugpcaxt)(replication,
                               block-size, user, group, permission,
                               checksum-type, ACL, XATTR, timestamps). If
                               -p is specified with no <arg>, then
                               preserves replication, block size, user,
                               group, permission, checksum type and
                               timestamps. raw.* xattrs are preserved when
                               both the source and destination paths are
                               in the /.reserved/raw hierarchy (HDFS
                               only). raw.* xattrpreservation is
                               independent of the -p flag. Refer to the
                               DistCp documentation for more details.
 -rdiff <arg>                  使用目标快照差异报告来标识对目标所做的更改
 -skipcrccheck                 是否跳过源路径和目标路径之间的CRC校验。
 -strategy <arg>               复制策略使用。 默认是根据文件大小划分工作
 -tmp <arg>                    用于原子提交的中间工作路径
 -update                       更新目标，仅复制missingfiles或目录
 -v                            在SKIP / COPY日志中记录其他信息（路径，大小）
```



在两个HDFS 集群直接传送数据，例如，以下命令在第二个集群上为第一个集群/foo目录创建了一个备份

```
hadoop distcp -update -delete -p hdfs://namenode1/foo hdfs://namenode2/foo
```

-delete 选项使distcp可以删除目标路径中任意没在源路径中出现的文件或目录

-p 意味着文件状态属性 权限、块大小 和复本数被保留



#### 保持HDFS集群均衡

balancer 均衡器工具