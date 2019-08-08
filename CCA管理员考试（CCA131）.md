## CCA管理员考试（CCA131）

- 问题数量：  预配置Cloudera Enterprise集群上的8-12个基于性能（动手）任务。 

- 时间限制：  120分钟

- 传球得分：  70％

- 语言：  英语

- 价格：  295美元

  

  课程：https://ondemand.cloudera.com/courses

## 所需技能

### 安装

展示对Cloudera Manager，CDH和生态系统项目的安装过程的理解。

- 设置本地CDH存储库
- 执行Hadoop安装的操作系统级配置
- 安装Cloudera Manager服务器和代理
- 使用Cloudera Manager安装CDH
- 将新节点添加到现有群集
- 使用Cloudera Manager添加服务

### 配置

执行有效管理Hadoop集群所需的基本和高级配置

- 使用Cloudera Manager配置服务
- 创建HDFS用户的主目录
- 配置NameNode HA
- 配置ResourceManager HA
- 为Hiveserver2 / Impala配置代理

### 管理

维护和修改群集以支持企业中的日常操作

- 重新平衡群集
- 设置过多磁盘填充的警报
- 定义并安装机架拓扑脚本
- 在群集中安装新类型的I / O压缩库
- 根据用户反馈修改YARN资源分配
- 委托/退役节点

### 安全

启用相关服务并配置群集以满足安全策略定义的目标; 展示基本安全实践的知识

- 配置HDFS ACL
- 安装和配置Sentry
- 配置Hue用户授权和认证
- 启用/配置日志和查询编辑
- 在HDFS中创建加密区域

### 测试

对集群运营指标进行基准测试，测试系统配置以确保运营和效率

- 通过HTTPFS执行文件系统命令
- 有效地复制群集内/群集之间的数据
- 创建/恢复HDFS目录的快照
- 获取/设置文件或目录结构的ACL
- 对集群进行基准测试（I / O，CPU，网络）

### 疑难解答

展示查找问题根本原因，优化低效执行和解决资源争用情况的能力

- 解决Cloudera Manager中的错误/警告
- 解决集群操作中的性能问题/错误
- 确定应用程序失败的原因
- 配置公平计划程序以解决应用程序延迟



## CCA Spark和Hadoop开发人员考试（CCA175）

- 问题数量：  Cloudera Enterprise集群上8-12个基于性能（动手）的任务。请参阅下面的完整群集配置
- 时间限制：  120分钟
- 传球得分：  70％
- 语言：  英语
- 价格：  295美元



## 所需技能

### 数据摄取

在外部系统和集群之间传输数据的技能。这包括以下内容：

- 使用Sqoop将数据从MySQL数据库导入HDFS
- 使用Sqoop从HDFS导出数据到MySQL数据库
- 使用Sqoop在导入期间更改数据的分隔符和文件格式
- 将实时和近实时流数据摄取到HDFS中
- 在将数据加载到群集时处理流数据
- 使用Hadoop文件系统命令将数据加载到HDFS中和从HDFS加载数据

### 变换，舞台和存储

将存储在HDFS中的给定格式的一组数据值转换为新数据值或新数据格式，并将它们写入HDFS。

- 从HDFS加载RDD数据以用于Spark应用程序
- 使用Spark将RDD的结果写回HDFS
- 以各种文件格式读写文件
- 对数据执行标准提取，转换，加载（ETL）过程

### 数据分析

使用Spark SQL在应用程序中以编程方式与Metastore进行交互。通过对加载的数据使用查询来生成报告。

- 将Metastore表用作Spark应用程序的输入源或输出接收器
- 了解Spark中查询数据集的基础知识
- 使用Spark过滤数据
- 编写计算汇总统计信息的查询
- 使用Spark加入不同的数据集
- 生成排名或排序的数据

### 组态

这是一个实践考试，候选人应该熟悉生成结果的所有方面，而不仅仅是编写代码。

- 提供命令行选项以更改应用程序配置，例如增加可用内存

### Spark 1和Spark 2

您的考试群集运行Spark 1.6附带的CDH 5.15。已安装附加软件包以提供Spark 2.3。考生在参加考试前应该知道如何运行两个不同版本的Spark。有关说明，请访问：[https](https://www.cloudera.com/documentation/spark2/latest/topics/spark_running_apps.html)：  [//www.cloudera.com/documentation/spark2/latest/topics/spark_running_apps.html](https://www.cloudera.com/documentation/spark2/latest/topics/spark_running_apps.html)



## 课程大纲

Apache Hadoop和Hadoop生态系统简介 

- Apache Hadoop和Hadoop生态系统简介
- Apache Hadoop概述
- 数据摄取和存储
- 数据处理 
- 数据分析与探索
- 其他生态系统工具
- 动手练习简介

Apache Hadoop文件存储

- Apache Hadoop集群组件
- HDFS架构
- 使用HDFS 

Apache Hadoop集群上的分布式处理

- YARN建筑
- 与YARN合作

Apache Spark基础知识

- 什么是Apache Spark？
- 启动Spark Shell
- 使用Spark Shell 
- 数据集和数据框架入门
- DataFrame操作

使用DataFrames和Schema

- 从数据源创建DataFrame
- 将DataFrames保存到数据源
- DataFrame架构 
- 渴望和懒惰的执行

使用DataFrame查询分析数据

- 使用列表达式查询DataFrame
- 分组和聚合查询
- 加入DataFrames 

RDD概述

- RDD概述 
- RDD数据源
- 创建和保存RDD 
- RDD操作

使用RDD转换数据

- 编写和传递转换函数 
- 转型执行
- 在RDD和DataFrame之间转换 

使用配对RDD聚合数据

- 键值对RDD 
- 的map-reduce
- 其他配对RDD操作 

 

使用Apache Spark SQL查询表和视图

- 使用SQL查询Spark中的表 
- 查询文件和视图
- 目录API 
- 比较Spark SQL，Apache Impala和Apache Hive-on-Spark

 

在Scala中使用数据集

- 数据集和数据框架 
- 创建数据集
- 加载和保存数据集 
- 数据集操作

 

编写，配置和运行Apache Spark应用程序

- 编写Spark应用程序 
- 构建和运行应用程序
- 应用程序部署模式 
- Spark应用程序Web UI
- 配置应用属性 

分布式处理

- 回顾：群集上的Apache Spark 
- RDD分区
- 示例：在查询中进行分区 
- 阶段和任务
- 工作执行计划 
- 示例：Catalyst执行计划
- 示例：RDD执行计划 

分布式数据持久性

- DataFrame和数据集持久性 
- 持久性存储级别
- 查看持久的RDD 

Apache Spark数据处理中的常见模式

- 常见的Apache Spark用例 
- Apache Spark中的迭代算法
- 机器学习 
- 示例：k-means

Apache Spark Streaming：DStreams简介

- Apache Spark Streaming概述 
- 示例：流请求计数
- DStreams 
- 开发流媒体应用程序

Apache Spark Streaming：处理多个批次

- 多批次操作 
- 时间切片
- 国家行动 
- 滑动窗口操作
- 预览：结构化流媒体 

 

Apache Spark Streaming：数据源

- 流数据源概述 
- Apache Flume和Apache Kafka数据源
- 示例：使用Kafka直接数据源 