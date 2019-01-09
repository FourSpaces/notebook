# Hadoop 常见操作



```
root@5c868d31ca5f:/usr/local/hadoop-2.7.6/bin# ./hdfs -h
Usage: hdfs [--config confdir] [--loglevel loglevel] COMMAND
       where COMMAND is one of:
  dfs                  在Hadoop支持的文件系统上运行文件系统命令.
  classpath            打印类路径
  namenode -format     格式化DFS文件系统
  secondarynamenode    运行DFS辅助名称节点
  namenode             运行DFS名称节点
  journalnode          运行DFS日志节点
  zkfc                 运行ZK故障转移控制器守护程序
  datanode             运行DFS数据节点
  dfsadmin             运行DFS管理客户端
  haadmin              运行DFS HA管理客户端
  fsck                 运行DFS文件系统检查实用程序
  balancer             运行集群平衡实用程序
  jmxget               从NameNode或DataNode获取JMX导出的值。
  mover                运行一个实用程序来移动块副本
                       storage types
  oiv                  将离线fsimage查看器应用于fsimage
  oiv_legacy           将离线fsimage查看器应用于传统fsimage
  oev                  apply the offline edits viewer to an edits file
  fetchdt              fetch a delegation token from the NameNode
  getconf              get config values from configuration
  groups               get the groups which users belong to
  snapshotDiff         diff two snapshots of a directory or diff the
                       current directory contents with a snapshot
  lsSnapshottableDir   list all snapshottable dirs owned by the current user
						Use -help to see options
  portmap              run a portmap service
  nfs3                 run an NFS version 3 gateway
  cacheadmin           configure the HDFS cache
  crypto               configure HDFS encryption zones
  storagepolicies      list/get/set block storage policies
  version              print the version
```

# 常用命令

## *一、     hadoop fs （hdfs dfs）  文件操作*

### 1)    ls 显示目录下的所有文件或者文件夹

使用方法： hadoop fs -ls [uri形式目录]

示例: hadoop fs –ls /    显示根目录下的所有文件和目录

显示目录下的所有文件可以加 -R 选项

示例: hadoop fs -ls -R /

### 2)    cat 查看文件内容

使用方法：hadoop fs -cat URI [URI …]

示例： hadoop fs -cat /in/test2.txt

### 3)    mkdir 创建目录

使用方法：hadoop fs -mkdir [uri形式目录] 

示例: hadoop fs –mkdir /test

创建多级目录 加上 –p 

示例: hadoop fs –mkdir -p /a/b/c

### 4)    rm 删除目录或者文件

使用方法:hadoop fs -rm [文件路径]   删除文件夹加上 -r

示例: hadoop fs -rm /test1.txt

 

删除文件夹加上 -r，

示例:hadoop fs -rm -r /test

 

 

### 5)    put 复制文件

将文件复制到hdfs系统中，也可以是从标准输入中读取文件，此时的dst是一个文件

​    使用方法: hadoop fs -put <localsrc> ... <dst>

示例：

Hadoop fs -put /usr/wisedu/temp/test1.txt /

从标准输入中读取文件：hadoop fs -put -/in/myword

### 6)    cp 复制系统内文件

​    使用方法：hadoopfs -cp URI [URI …] <dest>

将文件从源路径复制到目标路径。这个命令允许有多个源路径，此时目标路径必须是一个目录。 
    示例：

hadoop fs -cp /in/myword/word

 

### 7)    copyFromLocal 复制本地文件到hdfs

使用方法：hadoop fs-copyFromLocal <localsrc> URI

除了限定源路径是一个本地文件外，和[**put**](http://hadoop.apache.org/docs/r1.0.4/cn/hdfs_shell.html#putlink)命令相似

### 8)    get 复制文件到本地系统

使用方法：hadoop fs -get[-ignorecrc] [-crc] <src> <localdst> 

复制文件到本地文件系统。可用-ignorecrc选项复制CRC校验失败的文件。使用-crc选项复制文件以及CRC信息。

示例：hadoop fs -get/word /usr/wisedu/temp/word.txt

### 9)    copyToLocal 复制 文件到本地系统

使用方法：hadoop fs-copyToLocal [-ignorecrc] [-crc] URI <localdst>

除了限定目标路径是一个本地文件外，和[get](http://hadoop.apache.org/docs/r1.0.4/cn/hdfs_shell.html#getlink)命令类似。

示例：hadoop fs - copyToLocal/word /usr/wisedu/temp/word.txt

### 10)           mv

将文件从源路径移动到目标路径。这个命令允许有多个源路径，此时目标路径必须是一个目录。不允许在不同的文件系统间移动文件。

使用方法：hadoop fs -mv URI [URI …] <dest>

示例：hadoop fs -mv /in/test2.txt /test2.txt

 

### 11)           du 显示文件大小

显示目录中所有文件的大小。

使用方法：hadoop fs -du URI [URI …]

示例: hadoop fs -du /

​       显示当前目录或者文件夹的大小可加选项 -s

​        示例: hadoop fs -du -s /

 

 

### 12)           touchz  创建空文件

  使用方法：hadoop fs -touchz URI [URI …] 

创建一个0字节的空文件

示例:hadoop fs -touchz /empty.txt

### 13)           chmod 改变文件权限

使用方法：hadoop fs -chmod[-R] <MODE[,MODE]... | OCTALMODE> URI [URI …]

与Linux平台下chmod命令相似，改变文件的权限。使用-R将使改变在目录结构下递归进行。命令的使用者必须是文件的所有者或者超级用户。

示例：先创建一个普通用户test:sudo useradd -m test

​      再用wisedu用户在hdfs系统目录/a下创建hello.txt文件，此时test具有读取/a/hello.txt文件的权限，如下图：

​     

​      在切换回wisedu用户修改文件的权限，让/a目录下的文件对于其他用户都不可读，命令: hadoop fs -chmod -R o-r /a  如下图所示，再切换回test用户查看/a/hello.txt文件时提示没有权限:

 

### 14)           chown 改变文件所有者

使用方法：hadoop fs -chown [-R] [OWNER][:[GROUP]] URI [URI]

改变文件的拥有者。使用-R将使改变在目录结构下递归进行。命令的使用者必须是超级用户。

示例:hadoop fs -chown -R test /a  如下图：

 

### 15)           chgrp 改变文件所在组

使用方法：hadoop fs -chgrp [-R] GROUP URI [URI …]

改变文件所属的组。使用-R将使改变在目录结构下递归进行。命令的使用者必须是文件的所有者或者超级用户。

示例：hadoop fs -chgrp -R test /a  如下图:

## *二、     hdfs dfsadmin 管理命令*

### 1)    -report

查看文件系统的基本信息和统计信息。

示例：hdfs dfsadmin -report

### 2)    -safemode

enter | leave | get | wait：安全模式命令。安全模式是NameNode的一种状态，在这种状态下，NameNode不接受对名字空间的更改（只读）；不复制或删除块。NameNode在启动时自动进入安全模式，当配置块的最小百分数满足最小副本数的条件时，会自动离开安全模式。enter是进入，leave是离开。

示例:hdfs dfsadmin -safemode get

​     hdfsdfsadmin -safemode enter

### 3)    -refreshNodes

重新读取hosts和exclude文件，使新的节点或需要退出集群的节点能够被NameNode重新识别。这个命令在新增节点或注销节点时用到。

示例：hdfs dfsadmin -refreshNodes

### 4)    -finalizeUpgrade

终结HDFS的升级操作。DataNode删除前一个版本的工作目录，之后NameNode也这样做。

### 5)    -upgradeProgress

​    status| details | force：请求当前系统的升级状态 | 升级状态的细节| 强制升级操作

### 6)    -metasave filename

 保存NameNode的主要数据结构到hadoop.log.dir属性指定的目录下的<filename>文件中。

### 7)    -setQuota<quota><dirname>……<dirname>

 为每个目录<dirname>设定配额<quota>。目录配额是一个长整形整数，强制设定目录树下的名字个数。

### 8)    -clrQuota<dirname>……<dirname>

为每个目录<dirname>清除配额设定。

### 9)    -help

​    显示帮助信息

 hdfs常用命令：

第一部分：hdfs文件系统命令

第一类：文件路径增删改查系列：

hdfs dfs -mkdir dir  创建文件夹

hdfs dfs -rmr dir  删除文件夹dir

hdfs dfs -ls  查看目录文件信息

hdfs dfs -lsr  递归查看文件目录信息

hdfs dfs -stat path 返回指定路径的信息

 

第二类：空间大小查看系列命令：

hdfs dfs -du -h dir 按照适合阅读的形式人性化显示文件大小

hdfs dfs -dus uri  递归显示目标文件的大小

hdfs dfs -du path/file显示目标文件file的大小

 

第三类:权限管理类：

hdfs dfs -chgrp  group path  改变文件所属组

hdfs dfs -chgrp -R /dir  递归更改dir目录的所属组

hdfs dfs -chmod [-R] 权限 -path  改变文件的权限

hdfs dfs -chown owner[-group] /dir 改变文件的所有者

hdfs dfs -chown -R  owner[-group] /dir  递归更改dir目录的所属用户

 

第四类：文件操作（上传下载复制）系列：

hdfs dfs -touchz a.txt 创建长度为0的空文件a.txt

hdfs dfs -rm file   删除文件file

hdfs dfs -put file dir  向dir文件上传file文件

hdfs dfs -put filea dir/fileb 向dir上传文件filea并且把filea改名为fileb

hdfs dfs -get file dir  下载file到本地文件夹

hdfs dfs -getmerge hdfs://Master:9000/data/SogouResult.txt CombinedResult  把hdfs里面的多个文件合并成一个文件，合并后文件位于本地系统

hdfs dfs -cat file   查看文件file

hdfs fs -text /dir/a.txt  如果文件是文本格式，相当于cat，如果文件是压缩格式，则会先解压，再查看

hdfs fs -tail /dir/a.txt查看dir目录下面a.txt文件的最后1000字节

hdfs dfs -copyFromLocal localsrc path 从本地复制文件

hdfs dfs -copyToLocal /hdfs/a.txt /local/a.txt  从hdfs拷贝到本地

hdfs dfs -copyFromLocal /dir/source /dir/target  把文件从原路径拷贝到目标路径

hdfs dfs -mv /path/a.txt /path/b.txt 把文件从a目录移动到b目录，可用于回收站恢复文件

 

第五类：判断系列：

hdfs fs -test -e /dir/a.txt 判断文件是否存在，正0负1

hdfs fs -test -d /dir  判断dir是否为目录，正0负1

hdfs fs -test -z /dir/a.txt  判断文件是否为空，正0负1

 

第六类：系统功能管理类：

hdfs dfs -expunge 清空回收站

hdfs dfsadmin -safemode enter 进入安全模式

hdfs dfsadmin -sfaemode leave 离开安全模式

hdfs dfsadmin -decommission datanodename 关闭某个datanode节点

hdfs dfsadmin -finalizeUpgrade 终结升级操作

hdfs dfsadmin -upgradeProcess status 查看升级操作状态

hdfs version 查看hdfs版本

hdfs daemonlog -getlevel <host:port> <name>  打印运行在<host:port>的守护进程的日志级别

hdfs daemonlog -setlevel <host:port> <name> <level>  设置运行在<host:port>的守护进程的日志级别

hdfs dfs -setrep -w 副本数 -R path 设置文件的副本数

 

第二部分：运维命令

start-dfs.sh   启动namenode，datanode，启动文件系统

stop-dfs.sh   关闭文件系统

start-yarn.sh  启动resourcemanager,nodemanager

stop-yarn.sh  关闭resourcemanager,nodemanager

start-all.sh    启动hdfs，yarn

stop-all.sh    关闭hdfs，yarn

hdfs-daemon.sh start datanode  单独启动datanode

start-balancer.sh -t 10% 启动负载均衡，尽量不要在namenode节点使用

hdfs namenode -format  格式化文件系统

hdfs namenode -upgrade  分发新的hdfs版本之后，namenode应以upgrade选项启动

hdfs namenode -rollback  将namenode回滚到前一版本，这个选项要在停止集群，分发老的hdfs版本之后执行

hdfs namenode -finalize  finalize会删除文件系统的前一状态。最近的升级会被持久化，rollback选项将再不可用，升级终结操作之后，它会停掉namenode，分发老的hdfs版本后使用

hdfs namenode importCheckpoint 从检查点目录装载镜像并保存到当前检查点目录，检查点目录由fs.checkpoint.dir指定

 

第三部分：mapreduce命令

hdfs jar file.jar 执行jar包程序

hdfs job -kill job_201005310937_0053  杀死正在执行的jar包程序

hdfs job -submit <job-file>  提交作业

hdfs job -status <job-id>   打印map和reduce完成百分比和所有计数器。

hdfs job -counter <job-id> <group-name> <counter-name>  打印计数器的值。

hdfs job -kill <job-id>  杀死指定作业。

hdfs job -events <job-id> <from-event-#> <#-of-events> 打印给定范围内jobtracker接收到的事件细节。

hdfs job -history [all] <jobOutputDir>     

hdfs job -history <jobOutputDir> 打印作业的细节、失败及被杀死原因的细节。更多的关于一个作业的细节比如成功的任务，做过的任务尝试等信息可以通过指定[all]选项查看。

hdfs job -list [all]  显示所有作业。-list只显示将要完成的作业。

hdfs job -kill -task <task-id>   杀死任务。被杀死的任务不会不利于失败尝试。

hdfs job -fail -task <task-id>   使任务失败。被失败的任务会对失败尝试不利。

 

第四部分：hdfs系统检查工具fsck

hdfs fsck <path> -move    移动受损文件到/lost+found

hdfs fsck <path> -delete   删除受损文件。

hdfs fsck <path> -openforwrite   打印出写打开的文件。

hdfs fsck <path> -files     打印出正被检查的文件。

hdfs fsck <path> -blocks     打印出块信息报告。

hdfs fsck <path> -locations     打印出每个块的位置信息。

hdfs fsck <path> -racks    打印出data-node的网络拓扑结构。

 

第五部分：运行pipies作业

hdfs pipes -conf <path> 作业的配置

hdfs pipes -jobconf <key=value>, <key=value>, ...  增加/覆盖作业的配置项

hdfs pipes -input <path>  输入目录

hdfs pipes -output <path> 输出目录

hdfs pipes -jar <jar file> Jar文件名

hdfs pipes -inputformat <class> InputFormat类

hdfs pipes -map <class> Java Map类

hdfs pipes -partitioner <class> Java Partitioner

hdfs pipes -reduce <class> Java Reduce类

hdfs pipes -writer <class> Java RecordWriter

hdfs pipes -program <executable> 可执行程序的URI

hdfs pipes -reduces <num> reduce个数