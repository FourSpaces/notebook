## 概念了解

**主从结构**：在一个集群中，会有部分节点充当主服务器的角色，其他服务器都是从服务器的角色，当前这种架构模式叫做主从结构。

主从结构分类：

1、一主多从

2、多主多从

Hadoop中的HDFS和YARN都是主从结构，主从结构中的主节点和从节点有多重概念方式：

1、主节点　　从节点

2、master　　slave

3、管理者　　工作者

4、leader　　follower

**Hadoop集群中各个角色的名称**：

| 服务 | 主节点          | 从节点      |
| ---- | --------------- | ----------- |
| HDFS | NameNode        | DataNode    |
| YARN | ResourceManager | NodeManager |



**高可用模式：**

​       表示整个集群中的主节点会有多个

　　注意区分：能够对外提供服务的主节点还是只有一个。其他的主节点全部处于一个热备的状态。

　　正在对外提供服务的主节点：active　　有且仅有一个

　　热备的主节点：standby　　可以有多个

　　工作模式：1、在任意时刻，只有一个主节点是active的，active的主节点对外提供服务

　　　　　　　2、在任意时刻，都应至少有一个standby的主节点，等待active的宕机来进行接替

　　架构模式：就是为了解决分布式集群中的通用问题SPOF

　　不管是分布式架构还是高可用架构，都存在一个问题：主从结构—从节点数量太多了。最直观的的问题：造成主节点的工作压力过载，主节点会宕机，当前的这种现象是一种死循环



## 集群服务器规划

使用4台CentOS-7.5服务器进行集群搭建, hadoop HA 集群的搭建依赖于 zookeeper，

所以选取三台当做 zookeeper 集群 ，总共准备了四台主机，分别是:

office-prod-bigdata-00，office-prod-bigdata-01，office-prod-bigdata-02，office-prod-bigdata-03 

其中 **office-prod-bigdata-00** 和 **office-prod-bigdata-01** 做 namenode 的主备切换，

而将 **office-prod-bigdata-02** 和 **office-prod-bigdata-03** 做 resourcemanager 的主备切换

| 主机名称/服务          | IP           | 用户 | HDFS                        | YARN                       | ZooKeeper     |
| ---------------------- | ------------ | ---- | --------------------------- | -------------------------- | ------------- |
| office-prod-bigdata-00 | 172.16.16.60 | root | NameNodeDataNodejournalnode | NodeManager                | Zookeeperzkfc |
| office-prod-bigdata-01 | 172.16.16.61 | root | NameNodeDataNodejournalnode | NodeManager                | Zookeeperzkfc |
| office-prod-bigdata-02 | 172.16.16.62 | root | DataNodejournalnode         | NodeManagerResourceManager | Zookeeper     |
| office-prod-bigdata-03 | 172.16.16.63 | root | DataNode                    | NodeManagerResourceManager |               |



## 软件安装步骤概述

1、获取安装包

2、解压缩和安装

3、修改配置文件

4、初始化，配置环境变量，启动，验证

## 安装 Zookeeper 集群

见我的另一篇博客 [ZooKeeper 的集群搭建](https://my.oschina.net/2devil/blog/3001137)

## 安装 Hadoop 集群

### 1、规划

规划安装用户：root, （这里目前使用 root, 后面会逐渐规范起来, 使用 hadoop）

规划安装目录：/usr/local/webserver/hadoop-2.9.1

规划数据目录：/hadoop/data/

注：安装目录和数据目录需要自己单独创建

### 2、上传解压缩

这里使用 hadoop2.9.1 作为安装版本，去官网下载后， 解压在 /usr/local/webserver/ 目录下

### 3、修改配置文件

cd 到配置文件目录：/usr/local/webserver/hadoop-2.9.1/etc/

```
cd /usr/local/webserver/hadoop-2.9.1/etc/
```

#### hadoop-env.sh

修改 JAVA_HOME 为 JDK的安装路径 : /usr/local/webserver/jdk1.8

![](https://raw.githubusercontent.com/FourSpaces/RepositoryResources/master/image/blog/image.png)

**core-site.xml**

```
<configuration>
  <property>
        <name>fs.defaultFS</name>
        <value>hdfs://myha01</value>
        <description> 指定hdfs的nameservice为myha01 </description>
   </property>

   <property>
        <name>hadoop.tmp.dir</name>
        <value>/hadoop/data/hadoop/tmp</value>
        <description> hadoop临时文件目录 </description>
    </property>

   <property>
        <name>ha.zookeeper.quorum</name>
        <value>office-prod-bigdata-00:2181,office-prod-bigdata-01:2181,office-prod-bigdata-02:2181</value>
   		<description> 指定zookeeper地址 </description>
	</property>
</configuration>
```



**hdfs-site.xml**

```
<configuration>

    <!-- 指定副本数 -->
    <property>
        <name>dfs.replication</name>
        <value>2</value>
    </property>

    <!-- 配置namenode和datanode的工作目录-数据存储目录 -->
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>/hadoop/data/hadoopdata/dfs/name</value>
    </property>

    <property>
        <name>dfs.datanode.data.dir</name>
        <value>/hadoop/data/hadoopdata/dfs/data</value>
    </property>

    <!-- 启用webhdfs -->
    <property>
        <name>dfs.webhdfs.enabled</name>
        <value>true</value>
    </property>

    <!--指定hdfs的nameservice为myha01，需要和core-site.xml中的保持一致 
        dfs.ha.namenodes.[nameservice id]为在nameservice中的每一个NameNode设置唯一标示符。 
        配置一个逗号分隔的NameNode ID列表。这将是被DataNode识别为所有的NameNode。 
        例如，如果使用"myha01"作为nameservice ID，并且使用"nn1"和"nn2"作为NameNodes标示符 
    -->

    <property>
        <name>dfs.nameservices</name>
        <value>myha01</value>
    </property>

    <!-- myha01下面有两个NameNode，分别是nn1，nn2 -->
    <property>
        <name>dfs.ha.namenodes.myha01</name>
        <value>nn1,nn2</value>
    </property>


    <!-- nn1的RPC通信地址 -->
    <property>
        <name>dfs.namenode.rpc-address.myha01.nn1</name>
        <value>office-prod-bigdata-00:9000</value>
    </property>

    <!-- nn1的http通信地址 -->
    <property>
        <name>dfs.namenode.http-address.myha01.nn1</name>
        <value>office-prod-bigdata-00:50070</value>
    </property>

    <!-- nn2的RPC通信地址 -->
    <property>
        <name>dfs.namenode.rpc-address.myha01.nn2</name>
        <value>office-prod-bigdata-01:9000</value>
    </property>

    <!-- nn2的http通信地址 -->
    <property>
        <name>dfs.namenode.http-address.myha01.nn2</name>
        <value>office-prod-bigdata-01:50070</value>
    </property>

    <!-- 指定NameNode的edits元数据的共享存储位置。也就是JournalNode列表 
         该url的配置格式：qjournal://host1:port1;host2:port2;host3:port3/journalId 
         journalId推荐使用nameservice，默认端口号是：8485 -->

    <property>
        <name>dfs.namenode.shared.edits.dir</name>
        <value>qjournal://office-prod-bigdata-00:8485;office-prod-bigdata-01:8485;office-prod-bigdata-02:8485/myha01</value>
    </property>

    <!-- 指定JournalNode在本地磁盘存放数据的位置 -->
    <property>
        <name>dfs.journalnode.edits.dir</name>
        <value>/hadoop/data/journaldata</value>
    </property>

    <!-- 开启NameNode失败自动切换 -->
    <property>
        <name>dfs.ha.automatic-failover.enabled</name>
        <value>true</value>
    </property>

    <!-- 配置失败自动切换实现方式 -->
    <property>
        <name>dfs.client.failover.proxy.provider.myha01</name>
        <value>org.apache.hadoop.hdfs.server.namenode.ha.ConfiguredFailoverProxyProvider</value>
    </property>

    <!-- 配置隔离机制方法，多个机制用换行分割，即每个机制暂用一行 -->
    <property>
        <name>dfs.ha.fencing.methods</name>
        <value>
            sshfence
            shell(/bin/true)
        </value>
    </property>

    <!-- 使用sshfence隔离机制时需要ssh免登陆 -->
    <property>
        <name>dfs.ha.fencing.ssh.private-key-files</name>
        <value>/root/.ssh/id_rsa</value>
    </property>

    <!-- 配置sshfence隔离机制超时时间 -->
    <property>
        <name>dfs.ha.fencing.ssh.connect-timeout</name>
        <value>30000</value>
    </property>

    <property>
        <name>ha.failover-controller.cli-check.rpc-timeout.ms</name>
        <value>60000</value>
    </property>

</configuration>

```



**mapred-site.xml**

```
<configuration>

    <!-- 指定mr框架为yarn方式 -->
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>

    <!-- 指定mapreduce jobhistory地址 -->
    <property>
        <name>mapreduce.jobhistory.address</name>
        <value>office-prod-bigdata-00:10020</value>
    </property>

    <!-- 任务历史服务器的web地址 -->
    <property>
        <name>mapreduce.jobhistory.webapp.address</name>
        <value>office-prod-bigdata-00:19888</value>
    </property>
    <property>
    	<name>mapreduce.application.classpath</name>
    	<value>$HADOOP_MAPRED_HOME/*,$HADOOP_MAPRED_HOME/lib/*,$MR2_CLASSPATH</value>
    	<value>/usr/local/webserver/hadoop-2.9.1/share/hadoop/mapreduce/*, /usr/local/webserver/hadoop-2.9.1/share/hadoop/mapreduce/lib/*</value>
  	</property>


</configuration>
```



yarn-site.xml

```
<configuration>

    <!-- 开启RM高可用 -->
    <property>
        <name>yarn.resourcemanager.ha.enabled</name>
        <value>true</value>
    </property>

    <!-- 指定RM的cluster id -->
    <property>
        <name>yarn.resourcemanager.cluster-id</name>
        <value>yrc</value>
    </property>

    <!-- 指定RM的名字 -->
    <property>
        <name>yarn.resourcemanager.ha.rm-ids</name>
        <value>rm1,rm2</value>
    </property>

    <!-- 分别指定RM的地址 -->
    <property>
        <name>yarn.resourcemanager.hostname.rm1</name>
        <value>office-prod-bigdata-02</value>
    </property>

    <property>
        <name>yarn.resourcemanager.hostname.rm2</name>
        <value>office-prod-bigdata-03</value>
    </property>

    <property>
         <name>yarn.resourcemanager.webapp.address.rm1</name>
         <value>office-prod-bigdata-02:8088</value>
    </property>

    <property>
         <name>yarn.resourcemanager.webapp.address.rm2</name>
         <value>office-prod-bigdata-03:8088</value>
    </property>

    <!-- 指定zk集群地址 -->
    <property>
        <name>yarn.resourcemanager.zk-address</name>
        <value>office-prod-bigdata-00:2181,office-prod-bigdata-01:2181,office-prod-bigdata-02:2181</value>
    </property>

    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>

    <property>
         <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
         <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>

    <property>
         <name>mapreduce.shuffle.port</name>
         <value>23080</value>
    </property>

    <property>
        <name>yarn.log-aggregation-enable</name>
        <value>true</value>
    </property>

    <property>
        <name>yarn.log-aggregation.retain-seconds</name>
        <value>86400</value>
    </property>

    <!-- 启用自动恢复 -->
    <property>
        <name>yarn.resourcemanager.recovery.enabled</name>
        <value>true</value>
    </property>

	<!-- 制定resourcemanager的状态信息存储在zookeeper集群上 -->
    <property>
        <name>yarn.resourcemanager.store.class</name>
        <value>org.apache.hadoop.yarn.server.resourcemanager.recovery.ZKRMStateStore</value>
    </property>

    <property>
        <name>yarn.nodemanager.resource.memory-mb</name>
        <value>61440</value>
        <description>NodeManager 此节点可用物理内存,注意，该参数是不可修改的，一旦设置，整个运行过程中不 可动态修改。</description>
    </property>

    <property>
        <name>yarn.scheduler.maximum-allocation-mb</name>
        <value>12288</value>
        <discription>单个任务可申请的最多物理内存量,单位MB,默认8182MB</discription>
    </property>

    <property>
        <name>yarn.nodemanager.resource.cpu-vcores</name>
        <value>22</value>
        <description>NodeManager总的可用虚拟CPU个数</description>
    </property>

    <property>
        <name>yarn.scheduler.maximum-allocation-vcores</name>
        <value>8</value>
        <description>单个任务可申请的CPU个数</description>
    </property>

    <property>
        <name>yarn.scheduler.minimum-allocation-mb</name>
        <value>2048</value>
        <discription>单个任务可申请的最少物理内存量,单位MB</discription>
    </property>

    <property>
        <name>yarn.nodemanager.vmem-pmem-ratio</name>
        <value>2.1</value>
    </property>

    <property>
         <name>yarn.resourcemanager.scheduler.class</name>
         <value>org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairScheduler</value>
         <description> 配置yarn 调度器为 FairScheduler </description>
    </property>

    <property>
        <name>yarn.scheduler.fair.allocation.file</name>
        <value>/usr/local/webserver/hadoop-2.9.1/etc/hadoop/fair-scheduler.xml</value>
   </property>

   <property>
         <name>yarn.scheduler.fair.preemption</name>
         <value>true</value>
         <description>是否启用抢占机制，默认值是false</description>
   </property>

   <property>
         <name>yarn.scheduler.fair.user-as-default-queue</name>
         <value>true</value>
         <description>default is True</description>
   </property>

   <property>
         <name>yarn.scheduler.fair.allow-undeclared-pools</name>
         <value>false</value>
         <description>default is True</description>
   </property>

   <property>
         <name>yarn.scheduler.fair.max.assign</name>
         <value>1</value>
         <description>default is -1 </description>
   </property>

</configuration>
```



slaves

```
office-prod-bigdata-00
office-prod-bigdata-01
office-prod-bigdata-02
office-prod-bigdata-03
```



fair-scheduler.xml, 根据自身实际去修改配置

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<allocations>

    <defaultQueueSchedulingPolicy>fair</defaultQueueSchedulingPolicy>
    <queue name="root">
        <queue name="default">
            <aclAdministerApps>root,hive,spark,hadoop</aclAdministerApps>
            <aclSubmitApps>*</aclSubmitApps>
            <maxRunningApps>12</maxRunningApps>
            <maxResources>225280 mb,80 vcores</maxResources>
            <minResources>2048 mb,1 vcores</minResources>
            <minSharePreemptionTimeout>1000</minSharePreemptionTimeout>
            <schedulingPolicy>fair</schedulingPolicy>
            <maxAMShare>1</maxAMShare>
            <weight>1</weight>
        </queue>

    </queue>

    <queuePlacementPolicy>
        <rule create="false" name="specified"/>
        <rule create="true" name="default"/>
    </queuePlacementPolicy>

</allocations>
```



### 4、把安装包分别分发给其他的节点

重点强调： 每台服务器中的hadoop安装包的目录必须一致， 安装包的配置信息还必须保持一致

```
[root@office-prod-bigdata-00 webserver]$ scp -r /usr/local/webserver/hadoop-2.9.1 office-prod-bigdata-01:/usr/local/webserver/
[root@office-prod-bigdata-00 webserver]$ scp -r /usr/local/webserver/hadoop-2.9.1 office-prod-bigdata-02:/usr/local/webserver/
[root@office-prod-bigdata-00 webserver]$ scp -r /usr/local/webserver/hadoop-2.9.1 office-prod-bigdata-03:/usr/local/webserver/
```



### 5、配置Hadoop环境变量

千万注意：

1、如果你使用root用户进行安装。 vi /etc/profile 即可 系统变量

2、如果你使用普通用户进行安装。 vi ~/.bashrc 用户变量

```
export HADOOP_HOME=/usr/local/webserver/hadoop-2.9.1
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_YARN_HOME=$HADOOP_HOME
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:
export HADOOP_CLASSPATH=$HADOOP_HOME/etc/hadoop:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mpreduce/*:$HADOOP_HOME/contrib/capacity-scheduler/*.jar
```



### 6、查看hadoop版本

验证是否安装成功,， 输入以下命令 查看输出是否 为 Hadoop 2.9.1

```
hadoop version
```

### 7、Hadoop HA 初始化

**重点强调：一定要按照以下步骤逐步进行操作**

### 1)、启动ZooKeeper

 启动各节点的 ZooKeeper 服务

### 2)、在你配置的各个journalnode节点启动该进程

需要在 office-prod-bigdata-00，office-prod-bigdata-01，office-prod-bigdata-02 三天机器上启动 journalnode

```
[root@office-prod-bigdata-00 sbin]$ hadoop-daemon.sh start journalnode
starting journalnode, logging to /usr/local/webserver/hadoop-2.9.1/logs/hadoop-hadoop-journalnode-hadoop1.out
[hadoop@hadoop1 sbin]$ jps
2739 JournalNode
2788 Jps
2647 QuorumPeerMain
[hadoop@hadoop1 conf]$ 
```



### 3)、格式化namenode

先选取一个namenode（office-prod-bigdata-00）节点进行格式化



```
[root@office-prod-bigdata-00 hadoop-2.9.1]# hadoop namenode -format
```


下图是我网上找的
![格式化](https://raw.githubusercontent.com/FourSpaces/RepositoryResources/master/image/blog/image2018-10-26_15-19-8.png)

### 4)、要把在hadoop1节点上生成的元数据 给复制到 另一个namenode（office-prod-bigdata-01）节点上

```
[root@office-prod-bigdata-00 hadoop-2.9.1]# cd data/
[root@office-prod-bigdata-00 data]# ls
hadoop  hadoopdata  journaldata
[root@office-prod-bigdata-00 data]# 
[root@office-prod-bigdata-00 data]# scp -r hadoopdata/ root@office-prod-bigdata-01:$PWD
VERSION 100% 206 0.2KB/s 00:00 
fsimage_0000000000000000000.md5 100% 62 0.1KB/s 00:00 
fsimage_0000000000000000000 100% 323 0.3KB/s 00:00 
seen_txid 100% 2 0.0KB/s 00:00 
```

### 5)、格式化zkfc

**重点强调：只能在nameonde节点进行**

```
hdfs zkfc -formatZK
```
下图是我网上找的
![格式化zkfc](https://raw.githubusercontent.com/FourSpaces/RepositoryResources/master/image/blog/image2018-10-26_17-23-16.png)

### 8、启动

- #### **启动HDFS**

在 /usr/local/webserver/hadoop-2.9.1/sbin 目录下，运行 **start-dfs.sh**，运行 jps 命令，查看启动情况, 



- #### **启动YARN**

在主备 resourcemanager 中随便选择一台进行启动, 这里挑选  office-prod-bigdata-03

在 /usr/local/webserver/hadoop-2.9.1/sbin 目录下，运行 **start-yarn.sh,**运行 jps 命令，查看启动情况

- **启动备用节点的 YARN**
  备用节点为  office-prod-bigdata-02
  在 /usr/local/webserver/hadoop-2.9.1/sbin 目录下，运行 
  ```
  yarn-daemon.sh start resourcemanager, 
  ```
  运行 jps 命令，查看是否 启动 ResourceManager



- #### 启动 mapreduce 任务历史服务器

  cd到节点 office-prod-bigdata-00上 /usr/local/webserver/hadoop-2.9.1/sbin 目录下，运行 

  ```
  mr-jobhistory-daemon.sh start historyserver
  ```


### **9、查看各节点的状态**

**HDFS**

```
[root@office-prod-bigdata-00 data]# hdfs haadmin -getServiceState nn1

active


[root@office-prod-bigdata-00 data]# hdfs haadmin -getServiceState nn2

standby
```



**YARN**

```
[root@office-prod-bigdata-00 data]# yarn rmadmin -getServiceState rm1

standby
 
[root@office-prod-bigdata-00 data]# yarn rmadmin -getServiceState rm2

action
```


## Hadoop HA 重启
Hadoop HA 集群挂掉后，重启方案：

一、检查 

1) 检查是 Hadoop 的组件挂掉，还是zookeeper 挂掉。

       jps:
       QuorumPeerMain 
    
       QuorumPeerMain 不在就是zookeeper 挂掉了

2) 检查： NameNode 节点是否已经挂掉
   jps  查看 office-prod-bigdata-00， office-prod-bigdata-01 节点上是否有NameNode 节点，如果没有，则启动NameNode 节点


二、启动 

1)  zookeeper启动3台机器（office-prod-bigdata-00，office-prod-bigdata-01， office-prod-bigdata-02）       
```
zkServer.sh start
```
2)  启动namenode
```
cd $HADOOP_HOME/sbin

./hadoop-daemon.sh start namenode
```

3)  启动HDFS
在 $HADOOP_HOME/sbin 目录下，运行 start-dfs.sh，运行 jps 命令，查看启动情况, 
```
cd $HADOOP_HOME/sbin
./start-dfs.sh
```

4)  启动YARN 
在主备 resourcemanager 中随便选择一台进行启动, 这里挑选 office-prod-bigdata-02
在 $HADOOP_HOME/sbin 目录下，运行 start-yarn.sh,运行 jps 命令，查看启动情况
```
cd $HADOOP_HOME/sbin
./start-yarn.sh
```

启动备用节点的 YARN ( hadoop13 )
备用节点为  office-prod-bigdata-03
在 $HADOOP_HOME/sbin 目录下，运行 yarn-daemon.sh start resourcemanager, 运行 jps 命令，查看是否 启动 ResourceManager
```
cd $HADOOP_HOME/sbin
./yarn-daemon.sh start resourcemanager
```

4) 启动 mapreduce 任务历史服务器
启动 mapreduce 任务历史服务器
在 $HADOOP_HOME/sbin 目录下，运行 mr-jobhistory-daemon.sh start historyserver
```
cd $HADOOP_HOME/sbin
./mr-jobhistory-daemon.sh start historyserver

```

5) 启动  datanode
```
cd $HADOOP_HOME/sbin
./hadoop-daemon.sh start datanode
```
6) 启动  nodemanager
```
cd $HADOOP_HOME/sbin
./yarn-daemon.sh start  nodemanager
```

三、查看各节点的状态 (office-prod-bigdata-00，office-prod-bigdata-01， office-prod-bigdata-02)任意一个节点上

**HDFS** 
```
[root@office-prod-bigdata-00 data]# hdfs haadmin -getServiceState nn1
 
active
 
 
[root@office-prod-bigdata-00 data]# hdfs haadmin -getServiceState nn2
 
standby
```

**YARN**
```
[root@office-prod-bigdata-00 data]# yarn rmadmin -getServiceState rm1


standby
 
[root@office-prod-bigdata-00 data]# yarn rmadmin -getServiceState rm2


action
```

四、其他操作

1) ha 有问题时候，不能进行故障转移，需要手动进行

手动故障转移
```
cd $HADOOP_HOME
./bin/hdfs haadmin -transitionToActive --forcemanual nn2
```

2) 建好集群后，修改了zk服务器名字，导致zk存储的名字与实际不符，需要重置zkfc 的HA 名字空间
```
cd $HADOOP_HOME
./bin/hdfs zkfc -formatZK
```
