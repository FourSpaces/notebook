Hive 错误解决文档

--------------

org.apache.hadoop.hive.ql.exec.MoveTask

产生问题的原因：
hive的查询结果在在进行move操作时，需要进行文件权限的授权，多个文件的授权是并发进行的，hive中该源码是在一个线程池中
执行的，该操作在多线程时线程同步有问题的该异常，这是hive的一个bug，目前截止目前的最新版本Apache Hive 2.1.1还没有修复该问题；
可以通过关闭hive的文件权限继承 hive.warehouse.subdir.inherit.perms=false 来规避该问题。

解决方法：
hive.warehouse.subdir.inherit.perms



~~~~~~~~

----------------

```
org.apache.hadoop.hive.ql.metadata.HiveException(Failed to create Spark client for Spark session 
```



