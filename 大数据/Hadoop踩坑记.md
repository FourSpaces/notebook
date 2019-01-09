# Hadoop踩坑记

最近在学习Hadoop，由于我搭建的环境比较特殊（在5台不同的供应商的云服务器上搭建）以及我学习的教程版本偏旧，学习的过程中遇到异常多坑，将自己遇到的难以解决的坑以及解决方案记录下来，希望对大家有帮助。

1.HA机制下mapreduce程序无法执行 
无论是将本地运行正常的程序或是示例程序PI，在集群上跑，都无法执行，还未开始执行就退出了。 
在yarn的管理界面上查看mapreduce的日志发现

```
2018-06-04 16:00:58,564 ERROR [main] org.apache.hadoop.mapreduce.v2.app.client.MRClientService: Webapps failed to start. Ignoring for now:
java.lang.NullPointerException
at org.apache.hadoop.util.StringUtils.join(StringUtils.java:930)
at org.apache.hadoop.yarn.server.webproxy.amfilter.AmFilterInitializer.initFilter(AmFilterInitializer.java:75)
at org.apache.hadoop.http.HttpServer2.initializeWebServer(HttpServer2.java:466)
at org.apache.hadoop.http.HttpServer2.<init>(HttpServer2.java:412)
at org.apache.hadoop.http.HttpServer2.<init>(HttpServer2.java:115)
at org.apache.hadoop.http.HttpServer2$Builder.build(HttpServer2.java:336)
at org.apache.hadoop.yarn.webapp.WebApps$Builder.build(WebApps.java:315)
at org.apache.hadoop.yarn.webapp.WebApps$Builder.start(WebApps.java:401)
at org.apache.hadoop.yarn.webapp.WebApps$Builder.start(WebApps.java:397)
at org.apache.hadoop.mapreduce.v2.app.client.MRClientService.serviceStart(MRClientService.java:143)
at org.apache.hadoop.service.AbstractService.start(AbstractService.java:194)
at org.apache.hadoop.mapreduce.v2.app.MRAppMaster.serviceStart(MRAppMaster.java:1269)1234567891011121314
```

我根据异常跟踪源码，问题大概就是MRClientService的WebApp创建过程出错，导致WebApp对象为null，后边调用了WebApp的getHttpPort()方法，导致空指针，而具体为什么会创建出错，百度上也找不到答案，后来经过不懈努力后才找到答案： 
HA机制下yarn-site.xml需要加入以下配置:

```
<property> 
    <name>yarn.resourcemanager.webapp.address.rm1</name>  
    <value>xxx1:8088</value> 
</property>  

<property> 
    <name>yarn.resourcemanager.webapp.address.rm2</name>  
    <value>xxx2:8088</value> 
</property>123456789
```

其中xxx1和xxx2需要替换成你的ResourceManager的主机名，比较坑的的就是即使你不配置，一样可以访问到管理界面，但是运行就会报错，我学的教程可能是旧版本的Hadoop，并没有提到这一点。 
增加了这一个配置以后，mapreduce程序就可以正常运行了。

2.Hbase的RegionServer无法启动 
先说一下，Hbase需要Hadoop支持，但并不是所有版本的Hbase与所有版本的Hadoop都兼容，两者版本需要匹配才能工作，具体对照可以参考<http://hbase.apache.org/book.html#configuration>。一开始我是用的Hadoop2.9发现Hbase任何版本下都是X，于是赶紧换回了2.8才能工作。 
我遇到的问题是，在Master主机上执行start-hbase.sh，HMaster启动成功了，RegionServer没有启动成功（准确的说应该是启动一下后就关闭了，用jps可以看到进程存在过），查看RegionServer的logs下的日志发现:

```
2018-06-10 17:06:23,528 ERROR [main] regionserver.HRegionServerCommandLine: Region server exiting
java.lang.RuntimeException: Failed construction of Regionserver: class org.apache.hadoop.hbase.regionserver.HRegionServer
    at org.apache.hadoop.hbase.regionserver.HRegionServer.constructRegionServer(HRegionServer.java:2682)
    at org.apache.hadoop.hbase.regionserver.HRegionServerCommandLine.start(HRegionServerCommandLine.java:64)
    at org.apache.hadoop.hbase.regionserver.HRegionServerCommandLine.run(HRegionServerCommandLine.java:87)
    at org.apache.hadoop.util.ToolRunner.run(ToolRunner.java:70)
    at org.apache.hadoop.hbase.util.ServerCommandLine.doMain(ServerCommandLine.java:126)
    at org.apache.hadoop.hbase.regionserver.HRegionServer.main(HRegionServer.java:2697)
Caused by: java.lang.reflect.InvocationTargetException
    at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
    at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)
    at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
    at java.lang.reflect.Constructor.newInstance(Constructor.java:423)
    at org.apache.hadoop.hbase.regionserver.HRegionServer.constructRegionServer(HRegionServer.java:2680)
    ... 5 more
Caused by: java.io.IOException: Problem binding to hadoop-remote-01/115.159.153.135:16020 : Cannot assign requested address. To switch ports use the 'hbase.regionserver.port' configuration property.
    at org.apache.hadoop.hbase.regionserver.RSRpcServices.<init>(RSRpcServices.java:938)
    at org.apache.hadoop.hbase.regionserver.HRegionServer.createRpcServices(HRegionServer.java:647)
    at org.apache.hadoop.hbase.regionserver.HRegionServer.<init>(HRegionServer.java:531)
    ... 10 more
Caused by: java.net.BindException: Cannot assign requested address
    at sun.nio.ch.Net.bind0(Native Method)
    at sun.nio.ch.Net.bind(Net.java:433)
    at sun.nio.ch.Net.bind(Net.java:425)
    at sun.nio.ch.ServerSocketChannelImpl.bind(ServerSocketChannelImpl.java:223)
    at sun.nio.ch.ServerSocketAdaptor.bind(ServerSocketAdaptor.java:74)
    at org.apache.hadoop.hbase.ipc.RpcServer.bind(RpcServer.java:2592)
    at org.apache.hadoop.hbase.ipc.RpcServer$Listener.<init>(RpcServer.java:585)
    at org.apache.hadoop.hbase.ipc.RpcServer.<init>(RpcServer.java:2045)
    at org.apache.hadoop.hbase.regionserver.RSRpcServices.<init>(RSRpcServices.java:930)
    ... 12 more12345678910111213141516171819202122232425262728293031
```

问题在Cannot assign requested address上，更改配置中的端口设置是没用的，查看资料有人说在/etc/hosts下加上127.0.0.1 localhost这一句，加上后确实能够启动进程了，但是启动进程并没什么用，因为加上这句导致无法与Master通信，在Master中找不到这几台RegionServer，在日志中出现一下错误

```
2018-06-10 17:20:03,746 WARN  [regionserver/hadoop-remote-01/127.0.0.1:16020] regionserver.HRegionServer: error telling master we are up
com.google.protobuf.ServiceException: java.net.SocketException: Invalid argument
    at org.apache.hadoop.hbase.ipc.AbstractRpcClient.callBlockingMethod(AbstractRpcClient.java:240)
    at org.apache.hadoop.hbase.ipc.AbstractRpcClient$BlockingRpcChannelImplementation.callBlockingMethod(AbstractRpcClient.java:336)
    at org.apache.hadoop.hbase.protobuf.generated.RegionServerStatusProtos$RegionServerStatusService$BlockingStub.regionServerStartup(RegionServerStatusProtos.java:8982)
    at org.apache.hadoop.hbase.regionserver.HRegionServer.reportForDuty(HRegionServer.java:2316)
    at org.apache.hadoop.hbase.regionserver.HRegionServer.run(HRegionServer.java:907)
    at java.lang.Thread.run(Thread.java:748)
Caused by: java.net.SocketException: Invalid argument
    at sun.nio.ch.Net.connect0(Native Method)
    at sun.nio.ch.Net.connect(Net.java:454)
    at sun.nio.ch.Net.connect(Net.java:446)
    at sun.nio.ch.SocketChannelImpl.connect(SocketChannelImpl.java:648)
    at org.apache.hadoop.net.SocketIOWithTimeout.connect(SocketIOWithTimeout.java:192)
    at org.apache.hadoop.net.NetUtils.connect(NetUtils.java:529)
    at org.apache.hadoop.net.NetUtils.connect(NetUtils.java:493)
    at org.apache.hadoop.hbase.ipc.RpcClientImpl$Connection.setupConnection(RpcClientImpl.java:416)
    at org.apache.hadoop.hbase.ipc.RpcClientImpl$Connection.setupIOstreams(RpcClientImpl.java:722)
    at org.apache.hadoop.hbase.ipc.RpcClientImpl$Connection.writeRequest(RpcClientImpl.java:906)
    at org.apache.hadoop.hbase.ipc.RpcClientImpl$Connection.tracedWriteRequest(RpcClientImpl.java:873)
    at org.apache.hadoop.hbase.ipc.RpcClientImpl.call(RpcClientImpl.java:1241)
    at org.apache.hadoop.hbase.ipc.AbstractRpcClient.callBlockingMethod(AbstractRpcClient.java:227)
    ... 5 more1234567891011121314151617181920212223
```

同时还会导致Hadoop出现问题，最后我在/etc/hosts下添加 
xx.xx.xx.xx localhost 
xx.xx.xx.xx为我的内网IP，通过ifconfig查看得到，问题解决

3.Storm和Kafka整合 
由于我跟着学习的视频版本比较老，版本变化有点大了。Storm和Kafka整合旧版本是在strom的external下有整合的jar包，新版本需要通过maven来添加整合jar包的依赖，否则KafkaSpout相关类没法使用，所以通过Maven添加相关的依赖即可。 
Maven配置可以参考<https://github.com/apache/storm> 中的example配置。 
有些类在新版本中过时了，可以参考<http://storm.apache.org/releases/1.2.2/storm-kafka-client.html> 进行开发。 
编写完成后提交到集群运行会报NoClassDefFoundError的错误，类似这个：

```
Exception in thread "main" java.lang.NoClassDefFoundError: org/apache/kafka/common/errors/InterruptException
    at storm.Topo.main(Topo.java:37)
Caused by: java.lang.ClassNotFoundException: org.apache.kafka.common.errors.InterruptException
    at java.net.URLClassLoader.findClass(URLClassLoader.java:381)
    at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
    at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:349)
    at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
    ... 1 more12345678
```

不仅仅只有这一个类找不到，可能会有很多类找不到，但问题根源都是一样的。这个错误一般都是在编译时能找到类，而运行时找不到类导致的，也就是我们集群环境缺少这个类，而这些类所属的jar包的路径应该要在$STORM_HOME/lib下，总共需要以下jar包： 
![这里写图片描述](https://img-blog.csdn.net/20180627145423871?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4MzM3ODIz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
其中非红底的jar包都是我添加进去的，如果你的$STORM_HOME/lib目录下缺少哪些jar包，你就从你的maven目录中找到对应jar包并复制进去，再重新运行即可执行了。



3、 多用户管理问题，资源配置问题

https://blog.csdn.net/mlljava1111/article/details/52043489

注意是否 单独启动了 yarn,  