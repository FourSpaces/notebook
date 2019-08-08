

密钥分发

```
# 在主节点生成密钥匙

hostnamectl set-hostname hadoop7.bigdata.org
ssh-keygen -t rsa

# 生成 秘钥后分发

cd .ssh
id_rsa

    ssh-copy-id -i ~/.ssh/id_rsa.pub root@172.16.16.35

#
/root/.ssh/id_rsa.pub

# 这样主节点 就可以免密访问所有节点
## 所有节点之间能够相互访问，
##  1、在每个节点上 向主节点分发秘钥。
	2、在主节点 将 authorized_keys 分发给所有节点，完成节点之间的免密登录
	3、known_hosts 分发效果会更好。
```



机器配置

```

#关闭防火墙
[root@hadoop9 ~]# systemctl stop firewalld.service
#设置防火墙开机自动关闭
[root@hadoop9 ~]# systemctl disable firewalld.service
#查看防火墙状态
[root@hadoop9 ~]# firewall-cmd --state 


## 关闭Selinux
#临时关闭命令
[root@master soft]# setenforce 0
#修改配置文件(重启生效)
[root@master soft]# vim /etc/selinux/config
SELINUX=disabled

##修改swappiness
#临时修改
[root@master cloudera]# sysctl -w vm.swappiness=0
#永久修改
[root@master cloudera]# echo "vm.swappiness=0" >> /etc/sysctl.conf


#临时关闭透明大页面
echo never > /sys/kernel/mm/transparent_hugepage/defrag
echo never > /sys/kernel/mm/transparent_hugepage/enabled
[root@master cloudera]# echo never > /sys/kernel/mm/transparent_hugepage/defrag
[root@master cloudera]# echo never > /sys/kernel/mm/transparent_hugepage/enabled
#永久关闭透明大页面
root@master cloudera]# echo '            ' >> /etc/rc.local
[root@master cloudera]# echo '# 关闭大透明页面' >> /etc/rc.local 
[root@master cloudera]# echo 'echo never > /sys/kernel/mm/redhat_transparent_hugepage/defrag' >> /etc/rc.local
[root@master cloudera]# echo 'echo never > /sys/kernel/mm/redhat_transparent_hugepage/enabled' >> /etc/rc.local
#查看是否关闭透明大页面
[root@master cloudera]# cat /sys/kernel/mm/redhat_transparent_hugepage/defrag
[root@master cloudera]# cat /sys/kernel/mm/redhat_transparent_hugepage/enabled

# 修改最大进程数

# 关闭ipv6
# https://www.jianshu.com/p/225d040d0b66
# echo 1 > /proc/sys/net/ipv6/conf/eth0/disable_ipv6
vi /etc/sysctl.conf
i
net.ipv6.conf.all.disable_ipv6 =1
net.ipv6.conf.default.disable_ipv6 =1
sysctl -p

echo 1>/proc/sys/net/ipv6/conf/all/disable_ipv6
echo 1>/proc/sys/net/ipv6/conf/default/disable_ipv6
exit
```



CDH 客户端安装

```
yum --disablerepo=* --enablerepo=cloudera* list installed cloudera-manager-agent
```





## CDH5数据库配置

关闭mysql 

```
sudo systemctl stop mysqld
```



对 /var/lib/mysql 下的ib_logfile0, ib_logfile1 进行备份

```

```



创建mysql 库

```
CREATE DATABASE <database> DEFAULT CHARACTER SET <character set> DEFAULT COLLATE utf8_general_ci;

GRANT ALL ON <database>.* TO '<user>'@'%' IDENTIFIED BY '<password>';

```



```

CREATE DATABASE scm DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
GRANT ALL ON scm.* TO 'scm'@'%' IDENTIFIED BY 'K7kl32da4o2d-';

CREATE DATABASE amon DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
GRANT ALL ON amon.* TO 'amon'@'%' IDENTIFIED BY 'K7kl32da4o2d-';

CREATE DATABASE rman DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
GRANT ALL ON rman.* TO 'rman'@'%' IDENTIFIED BY 'K7kl32da4o2d-';

CREATE DATABASE hue DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
GRANT ALL ON hue.* TO 'hue'@'%' IDENTIFIED BY 'K7kl32da4o2d-';

CREATE DATABASE metastore DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
GRANT ALL ON metastore.* TO 'hive'@'%' IDENTIFIED BY 'K7kl32da4o2d-';

CREATE DATABASE sentry DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
GRANT ALL ON sentry.* TO 'sentry'@'%' IDENTIFIED BY 'K7kl32da4o2d-';

CREATE DATABASE nav DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
GRANT ALL ON nav.* TO 'nav'@'%' IDENTIFIED BY 'K7kl32da4o2d-';

CREATE DATABASE navms DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
GRANT ALL ON navms.* TO 'navms'@'%' IDENTIFIED BY 'K7kl32da4o2d-';

CREATE DATABASE oozie DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
GRANT ALL ON oozie.* TO 'oozie'@'%' IDENTIFIED BY 'K7kl32da4o2d-';


CREATE DATABASE azkabans DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
GRANT ALL ON azkabans.* TO 'azkabans'@'%' IDENTIFIED BY 'K7kl32da4o2d-';


CREATE DATABASE task_run_status DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
GRANT ALL ON task_run_status.* TO 'trs'@'%' IDENTIFIED BY 'K7kl32da4o2d=';

刷新权限
sflush privileges;

```





---------

## 报错信息



1 报错信息如下

+======================================================================+
| Error: JAVA_HOME is not set and Java could not be found |
+----------------------------------------------------------------------+
| Please download the latest Oracle JDK from the Oracle Java web site |
| > http://www.oracle.com/technetwork/java/javase/index.html < |
| |
| Cloudera Manager requires Java 1.6 or later. |
| NOTE: This script will find Oracle Java whether you install using |
| the binary or the RPM based installer. |
+======================================================================+

2 但是自己设置了JAVA_HOME啊

![img](https://img2018.cnblogs.com/blog/567850/201902/567850-20190225213952137-14600871.png)

 

3在CDH的cloudera-scm-server启动脚本中添加JAVA_HOME环境变量

 find / -name 'cloudera-scm-server'

![img](https://img2018.cnblogs.com/blog/567850/201902/567850-20190225214101687-876607912.png)

vim /etc/rc.d/init.d/cloudera-scm-server

 

```
`export JAVA_HOME=/mnt/software/jdk1.``8``.0_201    <br>`
```

 



=====

com.cloudera.cmon.MgmtServiceLocatorException: Could not find a HOST_MONITORING nozzle from SCM.



## 集群目前存在的问题

```
已启用透明大页面压缩，可能会导致重大性能问题。请运行“echo never > /sys/kernel/mm/transparent_hugepage/defrag”和“echo never > /sys/kernel/mm/transparent_hugepage/enabled”以禁用此设置，然后将同一命令添加到 /etc/rc.local 等初始化脚本中，以便在系统重启时予以设置。以下主机将受到影响: 
 查看详细信息
hadoop[33-34, 36-38].bigdata.org

命令：

cat << EOF >> /etc/rc.local
echo never > /sys/kernel/mm/transparent_hugepage/defrag
echo never > /sys/kernel/mm/transparent_hugepage/enabled
EOF

echo never > /sys/kernel/mm/transparent_hugepage/defrag
echo never > /sys/kernel/mm/transparent_hugepage/enabled
```



## 新增一台主机后

```
hostnamectl set-hostname hadoop7.bigdata.org
    ssh-keygen -t rsa

# 生成 秘钥后分发

cd .ssh
id_rsa

    ssh-copy-id -i ~/.ssh/id_rsa.pub root@172.16.16.35

#
/root/.ssh/id_rsa.pub
```



```
systemctl stop firewalld.service #停止firewall
systemctl disable firewalld.service #禁止firewall开机启动

# 关闭SElinux
vi /etc/sysconfig/selinux
SELINUX=disabled

# 关闭 交换内存

# 设置文件句柄
# 查看用户级的文件数
ulimit -n


vi /etc/security/limits.conf

# 获取 最高能支持的句柄数 （19617222）
cat /proc/sys/fs/file-max

echo "* soft core    unlimited" >> /etc/security/limits.conf
echo "* hard core    unlimited" >> /etc/security/limits.conf
echo "* soft nofile  65535" >> /etc/security/limits.conf
echo "* hard nofile  65535" >> /etc/security/limits.conf

ulimit -n
ulimit -n 65535
ulimit -n

# socket句柄数限制, 会不会对集群有影响
too many open files
```



CDH主机都要执行的

- 设置权限

```
chmod 777 /data
```



- 重启 cloudera-scm-agent

```
sudo service cloudera-scm-agent next_stop_hard
sudo service cloudera-scm-agent stop
sudo systemctl start cloudera-scm-agent

sudo systemctl start cloudera-scm-agent

sudo systemctl restart cloudera-scm-agent
systemctl status cloudera-scm-agent
```



- 添加mysql jar包到  sqoop, spark

 ```
mkdir -p /usr/share/java/
scp hadoop35.bigdata.org:/usr/share/java/mysql-connector-java.jar /usr/share/java/mysql-connector-java.jar

scp hadoop35.bigdata.org:/opt/cloudera/parcels/CDH/lib/sqoop/lib/java-json-schema.jar /opt/cloudera/parcels/CDH/lib/sqoop/lib/java-json-schema.jar

ln -s /usr/share/java/mysql-connector-java.jar /opt/cloudera/parcels/CDH/lib/sqoop/lib/mysql-connector-java.jar

ln -s /usr/share/java/mysql-connector-java.jar /opt/cloudera/parcels/CDH/lib/spark/jars/mysql-connector-java.jar

java-json-schema.jar 

3UYCvHdQxD0NroCz7bHYQ1T8Idjq3zOs

ll /opt/cloudera/parcels/CDH/lib/sqoop/lib/ | grep  mysql

ll /opt/cloudera/parcels/CDH/lib/spark/jars/ | grep mysql
 ```

- 安装 pip 以及python 相关模块

```

scp hadoop30.bigdata.org:~/get-pip.py .
python get-pip.py -i https://pypi.doubanio.com/simple
pip --version
pip install -U pip -i https://pypi.doubanio.com/simple
pip install requests -i https://pypi.doubanio.com/simple
```



- 添加mysql

```
yum install wget -y
wget http://repo.mysql.com/mysql57-community-release-el7-9.noarch.rpm
rpm -ivh mysql57-community-release-el7-9.noarch.rpm 
rpm -ivh mysql-community-release-el7-11.noarch.rpm
---------------------

yum install wget -y
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
yum clean all
yum makecache

scp hadoop35.bigdata.org:/etc/yum.repos.d/mysql-community.repo  /etc/yum.repos.d/mysql-community.repo
scp  hadoop35.bigdata.org:/etc/pki/rpm-gpg/RPM-GPG-KEY-mysql /etc/pki/rpm-gpg/
yum update
yum install mysql -y
```



```
# 启动本地spark
spark-shell --master yarn --deploy-mode client

pyspark --master yarn --deploy-mode client
```



python 配置

```
mkdir /home/tool/
wget http://hadoop35.bigdata.org:9870/webhdfs/v1/test/ius-release-el7.rpm?op=OPEN
mv ius-release-el7.rpm?op=OPEN ius-release-el7.rpm
yum install -y ius-release-el7.rpm
yum install -y python36u
ln -s /bin/python3.6 /bin/python3
python3 -V


yum install -y python36u-pip
ln -s /bin/pip3.6 /bin/pip3
pip3 install --upgrade pip -i http://pypi.douban.com/simple --trusted-host pypi.douban.com


cd /usr/bin
python3 -m venv py3spark
source py3spark/bin/activate
pip3 install --upgrade pip -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
pip3 install numpy -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

python -V
deactivate

# 配置集群
export PYSPARK_PYTHON=/usr/bin/py3spark/bin/python
export PYSPARK_PYTHON=/usr/bin/python3
```



# CDH管理

### 查看图表

监控堆内存使用情况

```
# NameNode
select jvm_max_memory_mb, jvm_heap_used_mb where roleType="NameNode"
```



### 配置短路读取

```

dfs.client.read.shortcircuit = true
```



### HDFS Trash

删除文件会被移动到 /user/<username>/.Trash/Current

fs.trash.interval 等待时间

```


```





## 新集群替代旧集群

新集群经过周六的测试后，已经解决了测试过程中显现的所有问题：

新集群接替旧集群的计划如下：

1、周四开始在新集群上做数据计算的准备:

- 将数据更新到新集群中，大部分数据已经迁移，只需要更新部分数据，每天的量在300G左右。
- 将日志写入新集群中，这个应该在周三凌晨进行，周三的日志应该在新集群中。
- 配置旧集群的机器，连接到新集群中，这个应该在周三前完成。

2、周三的计划

- 旧集群数据计算完成后，应该是下午，需要趁这段时间。
- 将计算结果 更新到新集群，将旧集群关掉，将机器添加到新集群
- 测试新集群的问题

3、周四计算出现问题时，解决方案：

- 尽量解决问题。

- 如果在中午2点还未解决问题，将重启旧集群，保证可以当天计算完成。

  

#### 新集群启用的功能：

- 配置了本地文件快速读取，加快读完文件速度
- 开启了HDFS 垃圾桶，删除文件会被移动到 /user/<username>/.Trash/Current，误删文件后，可以及时回退。垃圾桶保留时间为1天。
- yarn资源动态配置。



设置调优：

vm.swappiness

```
cat /proc/sys/vm/swappiness
sudo sysctl -w vm.swappiness=1
```



linux

```
# 修改预读缓冲区
blockdev --getra /dev/mapper/centos-home
blockdev --setra 1024 /dev/mapper/centos-home
blockdev --getra /dev/mapper/centos-home


echo "vm.swappiness=1" >> /etc/sysctl.conf
```





HDFS

```
dfs.datanode.max.transfer.threads = 8192
dfs.namenode.handler.count = 128
dfs.datanode.handler.count = 8
dfs.namenode.replication.max-streams=30
dfs.namenode.replication.max-streams-hard-limit=60
dfs.datanode.du.reserved=50G
```



YARN

```
dfs.datanode.max.xcievers=
```

动态资源配置

```
spark.dynamicAllocation.schedulerBacklogTimeout=10
spark.dynamicAllocation.initialExecutors=1
```


HIVE
```
hive.limit.pushdown.memory.usage=0.4
hive.fetch.task.conversion=more
hive.fetch.task.conversion.threshold=1073741824

hive.optimize.ppd=true
hive.stats.autogather=true
```


Hive on spark

调优要解决的问题：

- 判断 shuffle过程 是否比较多，内存是否够用
- 判断 task执行用户代码内存是否够用
- 持久化内存是否够用
- 判断 task执行速度，跟CPU 有关

对Executor的内存理解（Executor的内存主要分为三块）：

- 第一块是让task执行我们自己编写的代码时使用，默认是占Executor总内存的20%；
- 第二块是让task通过shuffle过程拉取了上一个stage的task的输出后，进行聚合等操作时使用，默认也是占Executor总内存的20%；
- 第三块是让RDD持久化时使用，默认占Executor总内存的60%；



```
executor-memory: Executor内存的大小,决定了Spark作业的性能，而且跟常见的JVM OOM异常，也有直接的关联。
spark.shuffle.memoryFraction:设置shuffle过程中, 进行聚合操作时能够使用的Executor内存的比例，默认是0.2。

spark.storage.memoryFraction:该参数用于设置RDD持久化数据在Executor内存中能占的比例，默认是0.6。

```



```
如果发现作业由于频繁的gc导致运行缓慢（通过spark web ui可以观察到作业的gc耗时），意味着task执行用户代码的内存不够用，那么同样建议调低这个参数的值 spark.shuffle.memoryFraction
```

#### 网络检测想法
检测每台机器到所有机器的时间，预测网络链路问题。


### 日志分析想法
需要分析项目：
- task 数量
- 并行度， spark.default.parallelism
- 判断日志中是否 PROCESS_LOCAL， 好多的级别都是NODE_LOCAL、ANY，调整本地化等待时间。


常见的词语
- OOM 内存溢出
- GC 垃圾回收器，GC的时候，一定是会导致工作线程停止，频繁GC对Spark作业的速度影响很大

### 数据迁移方案

### sqoop 出现的问题

```
tool.ImportTool: Import failed: java.io.IOException: Generating splits for a textual index column allowed only in case of "-Dorg.apache.sqoop.splitter.allow_text_splitter=true" property passed as a parameter



ERROR ql.Driver: FAILED: IllegalStateException Unexpected Exception thrown: Unable to fetch table user_order. Invalid method name: 'get_table_req'
```

hive 出现问题时
```
hive on spark 报错


    hive --hiveconf hive.root.logger=DEBUG,console  -e "use userdb;select count(*) from app_yyb;"
```
hdfs 报错
java.io.IOException: Got error, status=ERROR, status message
一般是防火墙的问题，查看是否未关闭防火墙，关闭防火墙即可

**问题**：使用hive 进行 group by   分区字段 会造成 最后阶段的任务只有一个

**查询1**:  ymd 为分区字段，最后一个阶段只产生一个任务，并且不一定可以跑完

select uuid,ymd from dw.meta_play_game t where ymd <='20190610' and ymd >='20190511' group by uuid,ymd;

![image-20190611215250685](/Users/weicheng/Library/Application Support/typora-user-images/image-20190611215250685.png)



查询2:  kind 为表内字段，最后一个阶段产生了多个任务

select uuid,kind from dw.meta_play_game t where ymd <='20190610' and ymd >='20190511' group by uuid,kind;

![image-20190611215231213](/Users/weicheng/Library/Application Support/typora-user-images/image-20190611215231213.png)



查询3: report.sumwei_20190610 为 meta_play_game 符合条件的合集表，包含 ymd 字段，没有分区。

select uuid,onlyid,appname,ymd from report.sumwei_20190610 group by uuid,onlyid,appname,ymd;

![image-20190612101038025](/Users/weicheng/Library/Application Support/typora-user-images/image-20190612101038025.png)



```
mkdir /data1
mkdir /data2
mkfs.xfs -f /dev/sdb
mkfs.xfs -f /dev/sdc
mount /dev/sdb /data1
mount /dev/sdc /data2



mount /dev/sd1 /data1
mount /dev/sd2 /data2
```



进行时间同步

参考URL：<https://www.cnblogs.com/kevingrace/p/5821499.html>

```
yum -y install ntp ntpdate
/sbin/chkconfig --level=2345 ntpd on
ntpdate ntp2.aliyun.com

ntpdate 172.16.16.35
crontab -l
crontab -e
0 * * * *  /usr/sbin/ntpdate ntp1.aliyun.com; /sbin/hwclock -w

yum -y install ntpdate
service ntpd stop
chkconfig ntpd off
ntpdate 172.16.16.35
crontab -e
i
0 1 * * *  /usr/sbin/ntpdate 172.16.16.35; /sbin/hwclock -w
```



#### 性能测试

- 服务器性能测试

```
CPU、内存、网络、i/O
FGG, 死锁，(load average),
线程池最大链接数
```



```
top
vmstat
jsatack(堆日志)
jstat-gcutil（E， S0, S1）
free
fdisk
```





- 集群基准测试

  

**TestDFSIO  HDFS IO 读写**

集群写入

```
hadoop jar /root/cw/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.1.2-tests.jar TestDFSIO -write -nrFiles 200 -size 4GB
```



集群读出

```
hadoop jar /root/cw/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.1.2-tests.jar TestDFSIO -read -nrFiles 200 -size 4GB
```



安装htop
```
yum install epel-release -y
yum install htop -y
```



// 同时向一台机器传数据时候，两台机器使用带宽 相加并不等于 目标机器带宽，因为集群本身也在传输东西。

![image-20190711203519457](/Users/weicheng/Library/Application Support/typora-user-images/image-20190711203519457.png)



![image-20190711203737247](/Users/weicheng/Library/Application Support/typora-user-images/image-20190711203737247.png)



集群节点负载过高问题

