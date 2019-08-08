Amber 接管线上Hadoop

一、zookeeper 接管

1、使用ambari 安装 zookeeper, (安装三个客户端。服务端)

2、停止所有的zookeeper, 在ambari 启动 zookeeper

3、在nameonde节点 格式化zkfc

```
hdfs zkfc -formatZK
```



二、Hadoop 接管

#### HDFS 接管

**Namenode 接管**

- 将配置文件修改为线上hadoop的配置信息[core-site.xml, hdfs-site.xml]

- 更新 从Namenode 节点的配置信息

- 打开集群安全模式。退出从Namenode

- 在 amber  Hosts中开启从Namenode 节点的namenode

- 等待启动成功。会遇到权限问题，需要将HDFS 加入之前配置的用户组中，设置文件组内访问

- Standby namenode节点 稳定输出后，将活动节点转移到 Standby 节点上。等待稳定输出

- 使用同样的模式, 将原先 active 的节点进行替换。

- 稳定后，完成HDFS Namenode 接管

  

  ```
  # 查看 namenode 状态
  hdfs dfsadmin -safemode get
  # 开启安全模式
  hdfs dfsadmin -safemode enter
  # 退出安全模式
  hdfs dfsadmin -safemode leave
  hdfs dfsadmin -safemode wait
  		
  ```

修补权限信息，是得ambari 和 和原有系统可以无缝衔接
```
groups 查看当前用户所在的组 
HDFS默认使用supergroup组

在所有机器上添加组
groupadd supergroup

将root hdfs 用户添加到 supergroup
usermod -a -G root hdfs

给datanode,nomenode,等 HDFS配置文件中相关路径，给775权限
chmod -R 775 data

chmod -R 775 /usr/local/webserver;chmod -R 775 /data/server/data;groupadd supergroup;usermod -a -G supergroup root;usermod -a -G supergroup hdfs

# 同步系统的权限信息到HDFS，在 所有的Namenode节点上进行 更新组信息操作
hdfs dfsadmin -refreshUserToGroupsMappings

```

```
usermod -a -G root hdfs
chmod -R 775 /usr/local/webserver
chmod -R 775 /data/server/data

ambari-agent start
```



或者使用滚动升级的方式进行操作

Namenode 相关操作

```
# 获取nn1状态
hdfs haadmin -getServiceState nn1

# 获取nn2状态
hdfs haadmin -getServiceState nn2



```







Datanode 接管

- 打开集群安全模式
- 关闭一个节点，ambari 上开启一个节点
- 完成Datanode 的接管

遇到的问题

----------------------



```
java.io.FileNotFoundException: /data/server/data/hadoopdata/dfs/name/current/VERSION (Permission den
```

更改目录权限，或者将yarn 、hdfs 用户加入root组中

```
java.io.IOException: Gap in transactions. Expected to be able to read up until at least txid 95325 but unable to find any edit logs containing txid 1
```



--------------

关闭安全模式

```
hdfs dfsadmin -safemode leav
```

-------------

```
org.apache.hadoop.hdfs.qjournal.client.QuorumException: Got too many exceptions to achieve quorum size 2/3. 3 exceptions thrown:
172.16.17.142:8485: Unknown protocol: org.apache.hadoop.hdfs.qjournal.protocol.QJournalProtocol
```

./hadoop-daemon.sh start journalnode

-----------

