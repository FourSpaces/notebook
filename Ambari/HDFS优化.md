# HDFS优化

## 优化Linux文件系统

**noatime和nodiratime属性** 
Linux文件系统会记录文件创建、修改和访问操作的时间信息，这在读写操作频繁的应用中将带来不小的性能损失。在挂载文件系统时设置noatime和nodiratime可禁止文件系统记录文件和目录的访问时间，这对HDFS这种读取操作频繁的系统来说，可以节约一笔可观的开销。可以修改/etc/fstab文件来实现这个设置。

```
$ vim /etc/fstab
如对/mnt/disk1使用noatime属性，可以做如下修改:
/ ext4 defaults 1 1
/mnt/disk1 ext4 defaults,noatime 1 2
/mnt/disk2 ext4 defaults 1 2
/mnt/disk3 ext4 defaults 1 2
/mnt/disk4 ext4 defaults 1 2
/mnt/disk5 ext4 defaults 1 2
/mnt/temp ext4 defaults 1 2
swap swap defaults 0 0
tmpfs /dev/shm tmpfs defaults 0 0
devpts /dev/pts devpts gid=5,mode=620 0 0
sysfs /sys sysfs defaults 0 0
proc /proc proc defaults 0 0
修改完成后，运行下述命令使之生效：
$ mount –o remount /mnt/disk1
```



**预读缓冲**
预读技术可以有效的减少磁盘寻道次数和应用的I/O等待时间，增加Linux文件系统预读缓冲区的大小(默认为256 sectors，128KB)，可以明显提高顺序文件的读性能，建议调整到1024或2048 sectors。预读缓冲区的设置可以通过blockdev命令来完成。下面的命令将/dev/sda的预读缓冲区大小设置为2048 sectors。
$ blockdev –setra 2048 /dev/sda

注意：**预读缓冲区并不是越大越好，多大的设置将导致载入太多无关数据，造成资源浪费，过小的设置则对性能提升没有太多帮助。**


**不使用RAID** 
应避免在TaskTracker和DataNode所在的节点上进行RAID。RAID为保证数据可靠性，根据类型的不同会做一些额外的操作，HDFS有自己的备份机制，无需使用RAID来保证数据的高可用性。
**不使用LVM**
LVM是建立在磁盘和分区之上的逻辑层，将Linux文件系统建立在LVM之上，可实现灵活的磁盘分区管理能力。DataNode上的数据主要用于批量的读写，不需要这种特性，建议将每个磁盘单独分区，分别挂载到不同的存储目录下，从而使得数据跨磁盘分布，不同数据块的读操作可并行执行，有助于提升读性能。
**JBOD**
JBOD是在一个底板上安装的带有多个磁盘驱动器的存储设备，JBOD没有使用前端逻辑来管理磁盘数据，每个磁盘可实现独立并行的寻址。将DataNode部署在配置JBOD设备的服务器上可提高DataNode性能。



## 优化HDFS配置

HDFS提供了十分丰富的配置选项，几乎每个HDFS配置项都具有默认值，一些涉及性能的配置项的默认值一般都偏于保守。根据业务需求和服务器配置合理设置这些选项可以有效提高HDFS的性能。表3-7列出了可优化的配置选项及参考值。
表3-7HDFS可优化配置项参考

## hdfs-site.xml

| 配置项                     | 优化原理                                                     | 推荐值                           |
| -------------------------- | ------------------------------------------------------------ | -------------------------------- |
| dfs.namenode.handler.count | NameNode中用于处理RPC调用的线程数，默认为10。对于较大的集群和配置较好的服务器，可适当增加这个数值来提升NameNode RPC服务的并发度。 | 64                               |
| dfs.datanode.handler.count | DataNode中用于处理RPC调用的线程数，默认为3。可适当增加这个数值来提升DataNode RPC服务的并发度。  **线程数的提高将增加DataNode的内存需求，因此，不宜过度调整这个数值。* | 10                               |
| dfs.replication            | 数据块的备份数。默认值为3，对于一些热点数据，可适当增加备份数。 | 3                                |
| dfs.block.size             | HDFS数据块的大小，默认为64M。数据库设置太小会增加NameNode的压力。数据块设置过大会增加定位数据的时间。 | 128                              |
| dfs.datanode.data.dir      | HDFS数据存储目录。如3.3.1所述，将数据存储分布在各个磁盘上可充分利用节点的I/O读写性能。 | 设置多个磁盘目录                 |
| hadoop.tmp.dir             | Hadoop临时目录，默认为系统目录/tmp。在每个磁盘上都建立一个临时目录，可提高HDFS和MapReduce的I/O效率。 | 设置多个磁盘目录                 |



core-site.xml
| 配置项                     | 优化原理                                                     | 推荐值                           |
| -------------------------- | ------------------------------------------------------------ | -------------------------------- |
| io.file.buffer.size        | HDFS文件缓冲区大小，默认为4096(即4K)。                       | 131072(128K)                     |
| fs.trash.interval          | HDFS清理回收站的时间周期，单位为分钟。默认为0，表示不使用回收站特性。 | 为防止重要文件误删，可启用该特性 |
| dfs.datanode.du.reserved   | DataNode保留空间大小，单位为字节。默认情况下，DataNode会占用全部可用的磁盘空间，该配置项可以使DataNode保留部分磁盘空间工其他应用程序使用。 | 视具体应用而定                   |
| 机架感应                   | 对于较大的集群，建议启用HDFS的机架感应功能。启用机架感应功能可以使HDFS优化数据块备份的分布，增强HDFS的性能和可靠性。 | -                                |





硬件环境配置

- **CPU**

  为了提高性能，CPU必须处于Performance模式，而不是PowerSave。另外还需要检查/proc/cpuinfo中的CPU主频，保证即使CPU空闲，主频也为2.XGHz.

- **网络**

  网络必须能够全速运行。可以用网络工具来检测网路速度。

- **磁盘**

  必须保证足够多的磁盘，如果磁盘吞吐量不够，磁盘IO将是整个测试过程的瓶颈。