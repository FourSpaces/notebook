

### spark 软件栈

![image-20190316174645606](/Users/weicheng/Library/Application Support/typora-user-images/image-20190316174645606.png)



#### Spark Core

Spark Core 实现了 Spark 的基本功能，包含任务调度、内存管理、错误恢复、与存储系统交互等模块。Spark Core 中还包含了对弹性分布式数据集(resilient distributed dataset，简称 RDD)的 API 定义。RDD 表示分布在多个计算节点上可以并行操作的元素集合，是Spark 主要的编程抽象。Spark Core 提供了创建和操作这些集合的多个 API。



#### Spark SQL

Spark SQL 是 Spark 用来操作结构化数据的程序包。

支持多种数据源，比如 Hive 表、Parquet 以及 JSON 等

Spark SQL 还支持开发者将 SQL 和传统的 RDD 编程的数据操作方式相结合



#### Spark Streaming

Spark Streaming 是 Spark 提供的对实时数据进行流式计算的组件。



#### MLlib

MLlib 提供了很多种机器学习算法，包括分类、回归、聚类、协同过滤等，还提供了模型评估、数据导入等额外的支持功能



#### GraphX

用来操作图(比如社交网络的朋友关系图)的程序库，可以进行并行的图计算.



数据科学应用和数据处理应用

