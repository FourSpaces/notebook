Amber  服务启动配置

启动顺序：

- Zookeeper

- HDFS

- YARN

- MapReduces2

- Hive

- Spark2




```
hdfs-site.xml 
<property>
  <name>dfs.namenode.datanode.registration.ip-hostname-check</name>
  <value>false</value>
</property>
```

