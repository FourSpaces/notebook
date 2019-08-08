# Hadoop 错误解决方案

---------------------



问题：

Application application_1536569935994_0036 failed 2 times due to AM Container for appattempt_1536569935994_0036_000002 exited with exitCode: 1

```
2018-09-11 14:08:21,702 INFO [Ping Checker] org.apache.hadoop.yarn.util.AbstractLivelinessMonitor: TaskAttemptFinishingMonitor thread interrupted
2018-09-11 14:08:21,702 FATAL [main] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: Error starting MRAppMaster
org.apache.hadoop.yarn.exceptions.YarnRuntimeException: java.lang.NullPointerException
	at org.apache.hadoop.mapreduce.v2.app.rm.RMCommunicator.register(RMCommunicator.java:177)
	at org.apache.hadoop.mapreduce.v2.app.rm.RMCommunicator.serviceStart(RMCommunicator.java:121)
	at org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator.serviceStart(RMContainerAllocator.java:274)
	at org.apache.hadoop.service.AbstractService.start(AbstractService.java:194)
	at org.apache.hadoop.mapreduce.v2.app.MRAppMaster$ContainerAllocatorRouter.serviceStart(MRAppMaster.java:959)
	at org.apache.hadoop.service.AbstractService.start(AbstractService.java:194)
	at org.apache.hadoop.service.CompositeService.serviceStart(CompositeService.java:121)
	at org.apache.hadoop.mapreduce.v2.app.MRAppMaster.serviceStart(MRAppMaster.java:1272)
	at org.apache.hadoop.service.AbstractService.start(AbstractService.java:194)
	at org.apache.hadoop.mapreduce.v2.app.MRAppMaster$5.run(MRAppMaster.java:1723)
	at java.security.AccessController.doPrivileged(Native Method)
	at javax.security.auth.Subject.doAs(Subject.java:422)
	at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1889)
	at org.apache.hadoop.mapreduce.v2.app.MRAppMaster.initAndStartAppMaster(MRAppMaster.java:1719)
	at org.apache.hadoop.mapreduce.v2.app.MRAppMaster.main(MRAppMaster.java:1650)
Caused by: java.lang.NullPointerException
	at org.apache.hadoop.mapreduce.v2.app.client.MRClientService.getHttpPort(MRClientService.java:177)
	at org.apache.hadoop.mapreduce.v2.app.rm.RMCommunicator.register(RMCommunicator.java:156)
	... 14 more
2018-09-11 14:08:21,704 INFO [main] org.apache.hadoop.util.ExitUtil: Exiting with status 1: org.apache.hadoop.yarn.exceptions.YarnRuntimeException: java.lang.NullPointerException
```

解决方案

```

```



---------------

问题：

```

User class threw exception: org.apache.spark.SparkException: Job aborted due to stage failure: Task 3206 in stage 1.0 failed 4 times, most recent failure: Lost task 3206.3 in stage 1.0 (TID 2826, hadoop4.bigdata.org): java.io.IOException: Cannot obtain block length for LocatedBlock{BP-589224685-172.16.16.60-1538189619928:blk_1151161069_77866578; 

或者

Connecting to namenode via http://hadoop10.bigdata.org:50070/fsck?ugi=root&openforwrite=1&path=%2Ftmp%2Fout%2Ftran
recoverLease got exception: DIR* NameSystem.internalReleaseLease: Failed to release lease for file /tmp/out/tran/20190423T160829.20190423.session_info.log. Committed blocks are waiting to be minimally replicated. Try again later.
```

解决方案

```
1、找到有问题的文件
hadoop fsck /tmp/out/tran -openforwrite | egrep -v '^\.+$' | egrep "MISSING|OPENFORWRITE" | grep -o "/[^ ]*" | sed -e "s/:$//" | xargs -i hdfs debug recoverLease -path {}

2、移除有问题的文件
```



------------------------

org.apache.hadoop.hdfs.protocol.AlreadyBeingCreatedException

```
2019-05-15 19:56:49,375 WARN org.apache.hadoop.hdfs.server.namenode.LeaseManager: Cannot release the path /hive/warehouse/log.db/ceshi/20190514/metaapp.0.2019-05-14.210400.log in the lease [Lease.  Holder: go-hdfs-VHvRwUdgVzekpwaY, pending creates: 1]. It will be retried.
org.apache.hadoop.hdfs.protocol.AlreadyBeingCreatedException: DIR* NameSystem.internalReleaseLease: Failed to release lease for file /hive/warehouse/log.db/ceshi/20190514/metaapp.0.2019-05-14.210400.log. Committed blocks are waiting to be minimally replicated. Try again later.
        at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.internalReleaseLease(FSNamesystem.java:3213)
        at org.apache.hadoop.hdfs.server.namenode.LeaseManager.checkLeases(LeaseManager.java:573)
        at org.apache.hadoop.hdfs.server.namenode.LeaseManager$Monitor.run(LeaseManager.java:509)
        at java.lang.Thread.run(Thread.java:745)
```

```
结论： 试图创建一个已存在的文件有可能会导致抛出AlreadyBeingCreatedException这个异常，由于namenode的server一直刷回收lease的日志，有可能是lease回收失败导致. 解决办法： 将代码： FSDataOutputStream fsdout = fs.create(tmpPath); 改成： if (fs.exists(tmpPath)) {      fs.delete(tmpPath, false);     } FSDataOutputStream fsdout = fs.create(tmpPath);
```