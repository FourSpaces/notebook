# Hadoop 错误解决方案

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



