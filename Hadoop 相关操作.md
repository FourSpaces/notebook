## Hadoop 相关操作

#### 进入和离开安全模式

查看namenode 是否处于安全模式

```
hdfs dfsadmin -safemode get

[root@hadoop10 current]# hdfs dfsadmin -safemode get
Safe mode is OFF in hadoop10.bigdata.org/172.16.16.60:9000
Safe mode is OFF in hadoop11.bigdata.org/172.16.16.61:9000
```

