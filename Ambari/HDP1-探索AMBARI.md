## 探索AMBARI

- Ambari Dashboard在端口上运行**：8080**。例如，[http：//sandbox-hdp.hortonworks.com：8080](http://sandbox-hdp.hortonworks.com:8080/)
- 以**管理员**身份登录，请参阅[管理密码重置](https://zh.hortonworks.com/tutorial/learning-the-ropes-of-the-hortonworks-sandbox/#admin-password-reset)
- 选择**管理Ambari**

[![管理-ambari](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/manage-ambari-3.jpg)](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/manage-ambari-3.jpg)

将显示以下屏幕：

[![Lab0_3](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/ambari-welcome-learning-the-ropes-sandbox-2-800x350.jpg)](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/ambari-welcome-learning-the-ropes-sandbox-2.jpg)

1. “ **仪表板** ”将带您进入Ambari仪表板，这是Hadoop操作员的主要UI
2. “ **群集管理** ”允许您向Ambari用户和组授予权限
3. “ **用户管理** ”允许您添加和删除Ambari用户和组
4. “ **Ambari用户视图** ”列出了属于群集的Ambari用户视图集

- 点击**Go to Dashboard**，你会看到一个类似的屏幕：

[![Lab0_4](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/Lab0-4-2-800x612.jpg)](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/Lab0-4-2.jpg)

资源管理器点击：

\1. **度量**，**比赛地图**和**配置历史**

然后：

\2. **后台操作**，**警报**，**管理员**和用户**视图**，图标（由3×3矩阵表示），以熟悉您可用的Ambari资源。

## 进一步阅读

- [Hadoop教程 - HDP入门](https://zh.hortonworks.com/tutorial/hadoop-tutorial-getting-started-with-hdp/)
- [HDP文档](https://docs.hortonworks.com/HDPDocuments/HDP3/HDP-3.0.1/index.html)
- [Hortonworks文档](http://docs.hortonworks.com/)

## 附录A：参考表

### 登录信息：

| 用户       | 密码                                                         |
| ---------- | ------------------------------------------------------------ |
| admin      | 请参阅[管理员密码重置](https://zh.hortonworks.com/tutorial/learning-the-ropes-of-the-hortonworks-sandbox/#admin-password-reset) |
| maria_dev  | maria_dev                                                    |
| raj_ops    | raj_ops                                                      |
| holger_gov | holger_gov                                                   |
| amy_ds     | amy_ds                                                       |

**admin** - 系统管理员

**maria_dev** - 负责准备并从数据中获取洞察力。她喜欢探索不同的HDP组件，如Hive，Pig，HBase。

**raj_ops** - 负责基础设施建设，研究和开发活动，如设计，安装，配置和管理。他是复杂操作系统系统管理领域的技术专家。

 **holger_gov** - 主要用于管理数据元素，包括内容和元数据。他的专业职位包括管理组织的全部数据的流程，政策，指南和责任，以遵守政策和/或监管义务。

 **amy_ds** - 使用Hive，Spark和Zeppelin进行探索性数据分析，数据清理和转换作为分析准备的数据科学家。

下面提到了Sandbox中这些用户之间的一些显着差异：

| 名称ID（S）         | 角色                                        | 服务                                                         |
| ------------------- | ------------------------------------------- | ------------------------------------------------------------ |
| Sam Admin           | Ambari Admin                                | Ambari                                                       |
| Raj (raj_ops)       | Hadoop Warehouse Operator(hadoop仓库管理员) | Hive/Tez, Ranger, Falcon, Knox, Sqoop, Oozie, Flume, Zookeeper |
| Maria (maria_dev)   | Spark and SQL Developer                     | Hive, Zeppelin, MapReduce/Tez/Spark, Pig, Solr, HBase/Phoenix, Sqoop, NiFi, Storm, Kafka, Flume |
| Amy (amy_ds)）      | Data Scientist（数据科学家）                | Spark, Hive, R, Python, Scala                                |
| Holger (holger_gov) | 数据专员                                    | Atlas(舆图)                                                  |



> Access: 权限
>
> Cluster：集群

操作系统级别授权**

| 名称ID（S）         | HDFS授权                                                     | AMBARI授权            | RANGER授权         |
| ------------------- | ------------------------------------------------------------ | --------------------- | ------------------ |
| Sam Admin           | Max Ops（行动）                                              | Ambari Admin          | Admin access       |
| Raj (raj_ops)       | 访问 Hive, Hbase, Atlas, Falcon, Ranger, Knox, Sqoop, Oozie, Flume, Operations | Cluster Administrator | Admin Access       |
| Maria (maria_dev)   | 访问Hive，Hbase，Falcon，Oozie和Spark                        | Service Operator      | Normal User Access |
| Amy (amy_ds)        | 访问Hive，Spark和Zeppelin                                    | Service Operator      | Normal User Access |
| Holger (holger_gov) | 访问Atlas                                                    | Service Administrator | Normal User Access |

**其他差异**

| 名称ID（S）         | SANDBOX角色           | 查看配置 | 启动/停止/重启服务 | 修改配置 | 添加/删除服务 | 安装组件 | 管理用户/组 | 管理AMBARI视图 | ATLAS UI ACCESS | [Sample Ranger Policy Access](https://zh.hortonworks.com/tutorial/tag-based-policies-with-apache-ranger-and-apache-atlas/#sample-ranger-policy) |
| ------------------- | --------------------- | -------- | ------------------ | -------- | ------------- | -------- | ----------- | -------------- | --------------- | ------------------------------------------------------------ |
| Sam Admin           | Ambari Admin          | 含       | 含                 | 含       | 含            | 含       | 含          | 含             | 含              | NA                                                           |
| Raj (raj_ops)       | Cluster Administrator | 含       | 含                 | 含       | 含            | 含       | 否          | 否             | 否              | 全部                                                         |
| Maria (maria_dev)   | Service Operator      | 含       | 含                 | 否       | 否            | 否       | 否          | 否             | 否              | 选择                                                         |
| Amy (amy_ds)        | Service Operator      | 含       | 含                 | 否       | 否            | 否       | 否          | 否             | 否              | 选择                                                         |
| Holger (holger_gov) | Service Administrator | 含       | 含                 | 含       | 否            | 否       | 否          | 否             | 含              | SELECT，CREATE，DROP                                         |

### 打开端口以供自定义使用

有关可自定义使用的端口，请参阅“ [沙箱指南”](https://github.com/hortonworks/data-tutorials/blob/master/tutorials/hdp/hortonworks-sandbox-guide/tutorial-3.md)。

在此示例中，我们将使用虚构端口**1234**，请注意此端口不可用于自定义用途。

**SSH到Sandbox主机上**

如果您正在运行VirtualBox VM：

```
＃上的VirtualBox虚拟机SSH 
SSH根@沙箱-HDP。霍顿工程。com-p2200
```

或者，如果您使用的是VMWare：

```
＃到VMware虚拟机SSH 
SSH根@沙箱-HDP。霍顿工程。com-p22
```

> 注意：默认密码为**hadoop**。

将目录更改为 `/sandbox/deploy-scripts/assets/`

```
cd / sandbox / deploy - 脚本/ 资产/ 
```

> 注意：在Sandbox的docker版本上，可以找到脚本 `deploy-scripts/assets/generate-proxy-deploy-script.sh`

在assets目录下，您将找到一个名为，编辑它的文件：`generate-proxy-deploy-script.sh`

```
我们生成- proxy - deploy - script 。SH
```

搜索`tcpPortsHDP`阵列并输入您要转发的端口：

[![新的端口](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/new-port-2.jpg)](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/new-port-2.jpg)

保存并退出按**esc**并输入`:x`

执行更改重新运行脚本：

```
cd / sandbox / deploy - 脚本
资产/ 生成- 代理- 部署- 脚本。SH 
```

并使用您的更改部署反向代理：

```
/sandbox/proxy/proxy-deploy.sh
```

最后，在虚拟环境中向前添加端口

设置 - >网络 - >高级 - >端口转发 - >添加新

现在重新启动虚拟机并享受您的新端口。

### 沙箱版本

当您遇到问题时，有人会问的第一件事就是“ *您使用的沙箱版本是什么* ”？要获取此信息：

使用[shell Web客户端](http://sandbox-hdp.hortonworks.com:4200/)登录并执行：。输出应该类似于：`sandbox-version`

[![沙盒版](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/sandbox-version-3.jpg)](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/sandbox-version-3.jpg)

> 注意：请参阅[登录凭据](https://zh.hortonworks.com/tutorial/learning-the-ropes-of-the-hortonworks-sandbox/#login-credentials)

### 管理员密码重置

由于密码容易被黑客攻击，我们建议
您将Ambari管理员密码更改为唯一。

1. 打开[Shell Web客户端](http://sandbox-hdp.hortonworks.com:4200/)（又名Shell-in-a-Box）：
2. 使用凭据登录：**root** / **hadoop**
3. 输入以下命令： `ambari-admin-password-reset`

> 重要提示：首次以**root用户**身份登录时，可能需要更改密码 - 请记住！

## 附录B：故障排除

- [Hortonworks社区连接](https://zh.hortonworks.com/community/forums/)（HCC）是一个很好的资源，可以找到您在Hadoop旅程中可能遇到的问题的答案。
- **挂起** / **长时间运行的进程**

有时您可能会遇到一个似乎永远无法运行但未完成的作业，查询或请求。可能是因为它处于**ACCEPTED**状态。开始查找的好地方是在[ResourceManager中](http://sandbox-hdp.hortonworks.com:8088/)。如果你知道一份工作已经完成，但是资源管理器仍然认为它正在运行 - 杀了它！

[![RM-杀](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/rm-kill-2-800x407.jpg)](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/rm-kill-2.jpg)

## 附录C：确定VIRTUALBOX SANDBOX的网络适配器

安装Sandbox VM后，它会附加到虚拟网络。有8种不同的网络模式，但您的沙箱将附加到的默认网络是NAT。我们将介绍我们的教程用例的相关网络：NAT和桥接适配器。

**网络地址转换（NAT）**

默认情况下，VM连接到网络地址转换（NAT）网络模式。默认情况下，guest虚拟机的IP地址会转换为主机的IP地址。NAT允许来宾系统连接到外部网络上的外部设备，但外部设备无法访问来宾系统。或者，VirtualBox可以通过端口转发在客户端上访问所选服务。VirtualBox侦听主机上的某些端口，然后将到达这些端口的数据包重新发送到同一端口或不同端口上的guest虚拟机。

我们如何将来自特定主机接口的所有传入流量转发到沙箱中的guest虚拟机，方法是指定该主机的IP，如下所示：

```
VBoxManage modifyvm “ Hortonworks Sandbox HDP 3.0.1 ” - natpf1 “ Sandbox Splash Page，tcp，127.0.0.1,1080 ,, 1080 ”。。。VBoxManage modifyvm “ Hortonworks Sandbox HDP 3.0.1 ” - natpf1 “ Sandbox Host SSH，tcp，127.0.0.1,2122，，22 ” 



 
```

您可以通过打开VM **设置**找到设置的网络，然后选择**网络**选项卡。

**桥接网络**

在此模式下，guest虚拟机可以直接访问主机已连接的网络。路由器为guest虚拟机分配IP地址。在该网络上，现在客户端IP地址可见，而不是仅显示主机IP地址。因此，外部设备（例如在Raspberry Pi上运行的MiNiFi）能够通过其IP地址连接到访客。

你什么时候需要这种模式？连接数据架构（CDA）需要它。要配置此模式，请首先关闭guest虚拟机虚拟机，单击设置，切换到网络选项卡，然后将**连接到**网络更改为**桥接适配器**。

[![桥接适配器](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/rm-kill-2-800x407.jpg)](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/rm-kill-2.jpg)

> 警告：首先确保您的计算机已连接到路由器，否则此功能将无法工作，因为没有路由器为guest虚拟机vm分配IP地址。

如果您使用的是**VirtualBox**或**VMWare**，则可以通过等待安装完成来确认IP地址，确认屏幕将告诉您沙盒解析的IP地址。例如：

[![沙箱环境的主机地址](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/guest-vm-NAT-mode-2.jpg)](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/guest-vm-NAT-mode-2.jpg)

> > **注意：** NAT沙箱的访客VM欢迎窗口 - >

[![沙箱环境的主机地址](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/guest-vm-bridged-mode-welcome-screen-2.jpg)](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/guest-vm-bridged-mode-welcome-screen-2.jpg)

> > **注意：** BRIDGED沙箱的访客VM欢迎窗口 - >

#### 教程问答和报告问题

如果您需要帮助或对本教程有疑问，请查看HCC以获取有关本教程的现有问题的答案。您可以使用下面的“提问”按钮发布新的HCC问题。