# Apache 工具组集合作用



## Apache Knox

我们主要用Knox来保护Spark UI、HDFS UI、Yarn UI，以及thrift server。当然，Knox也不只是服务于Hadoop、Spark，对于Web化的应用，基本上都可以使用Knox做保护，例如用Knox做Tomcat代理，主要是定义service.xml和rewrite.xml，即处理哪些url、如何处理。

Knox也支持Kerberos保护的集群。不过我这里使用了未启动Kerberos的集群，先忽略
Knox还可以保护HDFS NN UI、Yarn UI等，具体参考

Knox以类似防火墙的形式挡在Spark集群之前，接管所有用户请求（如WEB UI访问、HDFS内容查看、Hive/HBase数据操作等）。从拓扑上来说这种做法更清爽（相对Kerberos），但对内部集群的保护要求很高，因为一旦攻破了Knox层，不管资源还是数据都是光着屁股的

**Apache Knox提供如下功能**：

- Authentication (LDAP and Active Directory Authentication Provider)
- Federation/SSO (HTTP Header Based Identity Federation)
- Authorization (Service Level Authorization)
- Auditing

![](http://knox.apache.org/images/knox-overview.gif)

参考：https://ieevee.com/tech/2016/06/17/knox.html


## Apache Ranger
Apache Ranger提供一个集中式安全管理框架, 并解决授权和审计。它可以对Hadoop生态的组件如HDFS、Yarn、Hive、Hbase等进行细粒度的数据访问控制。通过操作Ranger控制台,管理员可以轻松的通过配置策略来控制用户访问权限。

参考：https://www.jianshu.com/p/d9941b8687b7
