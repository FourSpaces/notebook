## parcel 文件的编写





> CDH  parcel 文件

Cloudera Manager支持向Cloudera Manager添加新类型的服务（称为附加服务），允许此类服务利用Cloudera Manager分发，配置，监视，资源管理和生命周期管理功能。



## 自定义服务描述符文件

集成附加服务需要自定义服务描述符（CSD）文件。CSD文件包含描述和管理新服务所需的所有配置。CSD以JAR文件的形式提供。

根据服务，CSD和相关软件可由Cloudera或ISV提供。集成过程假定已经安装了附加服务软件（parcel或package）并且它存在于集群中。建议的方法是让ISV将软件作为包裹提供，但安装软件的实际机制取决于ISV。在该指令[中安装一个附加服务](https://www.cloudera.com/documentation/enterprise/6/6.3/topics/cm_mc_addon_services.html#concept_kpt_spj_bn)假设你已经从Cloudera的仓库或从ISV获得的CSD文件。它还假定您已经获得了服务软件，理想情况下是一个包裹，并且在安装CSD之前或作为CSD安装过程的一部分，已经或将要在集群上安装它。



### 配置自定义服务描述符文件的位置

CSD文件的默认位置是 /opt/cloudera/csd  您可以在Cloudera Manager Admin Console中更改位置，如下所示：

1. 选择**管理** > **设置**。
2. 单击“ **自定义服务描述符”**类别。
3. 编辑“ **本地描述符存储库路径”**属性。
4. 输入**更改原因**，然后单击“ **保存更改”**以提交更改。
5. 重新启动Cloudera Manager Server：

```
sudo systemctl restart cloudera-scm-server
```



## 安装附加服务

ISV可以以包裹的形式提供其软件，或者他们可能具有不同的安装软件的方式。如果他们的软件不是作为包裹提供的，那么您必须*在*添加CSD文件*之前*安装他们的软件。按照ISV的说明安装软件。如果ISV已将其软件作为包裹提供，他们也可能已将其包裹存储库的位置包括在他们提供的CSD中。在这种情况下，首先安装CSD然后安装包裹。



### 安装自定义服务描述符文件

1. 从Cloudera或ISV获取CSD文件。

2. 登录到Cloudera Manager Server主机，并将CSD文件放在为CSD文件[配置](https://www.cloudera.com/documentation/enterprise/6/6.3/topics/cm_mc_addon_services.html#concept_qbv_3jk_bn__section_xvc_yqj_bn)的[位置](https://www.cloudera.com/documentation/enterprise/6/6.3/topics/cm_mc_addon_services.html#concept_qbv_3jk_bn__section_xvc_yqj_bn)下。

3. 将文件所有权设置为 Cloudera的-SCM：Cloudera的供应链管理 经许可644。

4. 重新启动Cloudera Manager Server：

   ```
   service cloudera-scm-server restart
   ```

5. 登录Cloudera Manager Admin Console并重新启动Cloudera Management Service。

   1. 执行以下操作之一：
      - 1. 选择**Clusters** > **Cloudera Management Service**。
        2. 选择**操作** > **重启**。
      - 在**Home** > **Status**选项卡上，单击**Cloudera Management Service**![img](https://www.cloudera.com/documentation/enterprise/6/6.3/images/down_arrow.png)右侧的，然后选择**Restart**。
   2. 单击**重启**以确认。“ **命令详细信息”**窗口显示停止然后启动角色的进度。
   3. 当**命令使用n / n成功的子命令完成时**，任务完成。单击**关闭**。

   





cloudera-integration/csd/

<https://github.com/streamsets/datacollector/tree/4ae2839958b4a6cbe0a2d1c955deac4918060c68/cloudera-integration>

![image-20190806114657629](/Users/weicheng/Library/Application Support/typora-user-images/image-20190806114657629.png)

