## spark 实战电影点 评系统应用



功能：

1、统计某特定电影观看者巾男性和女性不同年龄的人数

2、计算所有电影中平均得分最高(口碑最好)的电影 TopN

3、计算最流行电影(即所有电影中粉丝或者观看人数最多)的电影 TopN

4、实现所有电影中最受男性 、 女性喜爱的电影 TopN、

5、实现所有电影中 QQ 或者微信核心目标用户最喜爱电影 TopN 分析

6、实现所有电影中淘宝核心目标用户最喜爱电影TopN 分析

7、电影点评系统实现 Java和 Scala版本的二次排序系统等



#### 电影点评系统用户行为分析统计

基于 MovieLens 数据集中 ratings.dat、 users.dat、 movies.dat、 occupations.dat文件进行用户行为实战分析。 

用户行为分析统计的数据处理: 

1、-个基本的技巧是，先使用传统的 SQL去实现一个数据处理的业务逻辑(自已可以手动模拟一些数据);

2、在 Spark2.x 的时候，再一次推荐使用 DataSet去实现业务功能，尤其是统计分析功能; 

3、如果想成为专家级别的顶级 Spark人才，请使用 RDD 实现业务功能



使用 Parquet的文件格式



大数据电影点评系统用户行为分析统计的数据源格式 :

```
"ratings.dat": UserId, MovieID, Rating, Timestamp
"users.dat": UserId, Gender, Age, OccupationId, zip-code
"movies.dat": MovieID, title, Genres
"occupations.dat": OccupationID, OccupationName
```



使用数据冗余来实现代码复用或者更高效地运行，这是企业级项目的一个非常厘要 的技巧! 