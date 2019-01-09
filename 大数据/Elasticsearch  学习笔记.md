# Elasticsearch  学习笔记



### 计算集群中的文档数量

 ```
curl -XGET 'http://localhost:9200/_count?pretty' -d '{"query":{"match_all":{}}}'
 ```

​      或者

```
curl -XGET 'http://localhost:9200/_count?pretty=\\{"query":\\{"match_all":\\{\\}\\}\\}'
```



### 添加 记录/文档

 ```
curl -XPUT 'http://localhost:9200/megacorp/employee/1' -d '{"first_name": "John", "last_name": "Smith", "age": 25, "about": "I love to go rock climbing", "interests":["sports", "music"]}'


curl -XPUT 'http://localhost:9200/megacorp/employee/2' -d '{"first_name": "Jane", "last_name": "Smith", "age": 32, "about": "I love to collect rock albums", "interests":[ "music"]}'


curl -XPUT 'http://localhost:9200/megacorp/employee/3' -d '{"first_name": "Douglas", "last_name": "Fir", "age": 35, "about": "I like to build cabinets", "interests":["forestry"]}'
 ```



### 检索 记录/文档

```
curl -XGET 'http://localhost:9200/megacorp/employee/1'
```



### 删除 记录/文档

```
DELETE
```



### 简单搜索

- 获取前10个结果

 ```
curl -XGET 'http://localhost:9200/megacorp/employee/_search'
 ```

依然使用 megacorp 索引 和 employee 类型，但是我们在结尾使用关键字 _search 来取代原来的文档ID， 默认会返回前10个结果。

- 查询字符串( query string)搜索， 搜索姓氏中 包含"Smith" 的员工。

```
curl -XGET 'http://localhost:9200/megacorp/employee/_search?q=last_name:Smith'
```



### DSL 查询

- 查询 姓氏 为"Smith" 的员工

```
curl -XGET 'http://localhost:9200/megacorp/employee/_search' -d '{"query": {"match":{"last_name":"Smith"}}}'
```



- *filter* 过滤器,   查询姓氏为"Smith" 的员工，但是只想得倒年龄大于30岁。

```
curl -XGET 'http://localhost:9200/megacorp/employee/_search' -d '{"query": {
    	"bool": {
    		"filter": {
    			"range": {"age": {"gt": 30} }
    		},
    		"must": {
            	"match": {"last_name": "smith"}
    		}
    	}
    }
}'


curl -XGET 'http://localhost:9200/megacorp/employee/_search' -d '{"query": {"bool": {"filter": {"range": {"age": {"gt": 30} }},"must": {"match": {"last_name": "smith"}}}}}'

```

- 全文搜索

```
curl -XGET 'http://localhost:9200/megacorp/employee/_search' -d '{
    "query": {"match": {"about": "rock climbing"}}
}'


curl -XGET 'http://localhost:9200/megacorp/employee/_search' -d '{"query": {"match": {"about": "rock climbing"}}}'
```

​        阐明了 Elasticsearch 如何 *在* 全文属性上搜索并返回相关性最强的结果。

​        Elasticsearch中的 *相关性* 概念非常重要，也是完全区别于传统关系型数据库的一个概念，数据库中的一条记录要么匹配要么不匹配。

​	

- match_phrase 查询、短语搜索

  想要精确匹配一系列单词或者*短语* ,  执行这样一个查询，仅匹配同时包含 “rock” *和* “climbing” ，*并且* 二者以短语 “rock climbing” 的形式紧挨着的雇员记录。

```
curl -XGET 'http://localhost:9200/megacorp/employee/_search' -d '{
    "query": {"match_phrase": {"about": "rock climbing"}}
}'


curl -XGET 'http://localhost:9200/megacorp/employee/_search' -d '{"query": {"match_phrase": {"about": "rock climbing"}}}'
```

​	

- 高亮搜索  highlight

```
curl -XGET 'http://localhost:9200/megacorp/employee/_search' -d '{
    "query": {"match_phrase": {"about": "rock climbing"}},
    "highlight": {"fields": {"about": {}}}
}'


curl -XGET 'http://localhost:9200/megacorp/employee/_search' -d '{"query": {"match_phrase": {"about": "rock climbing"}}, "highlight": {"fields": {"about": {}}}}'

```

​	

-  aggregations  聚合 分析

  在聚合前做如下操作

```
PUT megacorp/_mapping/employee/
{
  "properties": {
    "interests": { 
      "type":     "text",
      "fielddata": true
    }
  }
}

curl -XPUT 'http://localhost:9200/megacorp/_mapping/employee' -d '{"properties": {"interests": { "type":"text","fielddata": true}}}'
```



```
curl -XGET 'http://localhost:9200/megacorp/employee/_search' -d '{"aggs":{"all_interests": {
"terms": { "field": "interests" }
}}}'


curl -XGET 'http://localhost:9200/megacorp/employee/_search' -d '{"aggs":{"all_interests": {"terms": { "field": "interests" }}}}'

```

​	

- 组合查询

```
GET /megacorp/employee/_search
{
  "query": {
    "match": {
      "last_name": "smith"
    }
  },
  "aggs": {
    "all_interests": {
      "terms": {
        "field": "interests"
      }
    }
  }
}


curl -XGET 'http://localhost:9200/megacorp/employee/_search' -d '{"aggs":{"all_interests": {"terms": { "field": "interests" }}}, "query": {"match": {"last_name": "smith"}}}'
```



- 分级汇总  查询特定兴趣爱好员工的平均年龄：

```
GET /megacorp/employee/_search
{
    "aggs" : {
        "all_interests" : {
            "terms" : { "field" : "interests" },
            "aggs" : {
                "avg_age" : {
                    "avg" : { "field" : "age" }
                }
            }
        }
    }
}



curl -XGET 'http://localhost:9200/megacorp/employee/_search' -d '{"aggs": {"all_interests": {"terms": {"field" : "interests"}, "aggs": {"avg_age": {"avg": {"field": "age"}}} } }}'
```





### 集群健康

```
GET /_cluster/health

curl -XGET 'http://localhost:9200/_cluster/health'

```





# Spark ES



spark ES 自定义文档ID

```
scala> val upcomingTrip = Trip("1",  "OTP", "SFO")
upcomingTrip: Trip = Trip(1,OTP,SFO)

scala> val lastWeekTrip = Trip("2", "MUC", "OTP")
lastWeekTrip: Trip = Trip(2,MUC,OTP)

scala> val rdd = sc.makeRDD(Seq(upcomingTrip, lastWeekTrip))
rdd: org.apache.spark.rdd.RDD[Trip] = ParallelCollectionRDD[3] at makeRDD at <console>:40

scala> import org.apache.spark.SparkContext
import org.apache.spark.SparkContext

scala> import org.elasticsearch.spark.rdd.EsSpark
import org.elasticsearch.spark.rdd.EsSpark

scala> EsSpark.saveToEs(rdd, "spark/docs")
                                                                                
scala> EsSpark.saveToEs(rdd, "spark/docs", Map("es.mapping.id" -> "id"))


```

