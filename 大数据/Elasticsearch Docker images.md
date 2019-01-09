Elasticsearch Docker images

Elasticsearch是一个功能强大的开源搜索和分析引擎，可以轻松探索数据。



```
 docker pull elasticsearch:5.6-alpine
```



Elasticsearch是一个分布式RESTful搜索和分析引擎，能够解决越来越多的用例。作为Elastic Stack的核心，它集中存储您的数据，以便您可以发现预期并发现意外情况。



## 在开发模式下运行

创建用户定义的网络（用于连接到连接到同一网络的其他服务（例如Kibana））：

```
$ docker network create somenetwork
```

运行Elasticsearch：

```
$ docker run -d --name elasticsearch --net somenetwork -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:5.6-alpine
```

## 在生产模式下运行

请参阅[使用Docker安装Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/6.x/docker.html)