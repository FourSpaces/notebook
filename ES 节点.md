//ES 节点

120，121，122，123，33，238，239，240，



各节点的配置文件

vim /etc/elasticsearch/elasticsearch.yml



目前集群存在的问题

```
master_nodes 应该在3台左右吧
discovery.zen.minimum_master_nodes: 1

```



不一致的地方

参考地址：<https://www.cnblogs.com/jstarseven/p/6803054.html>

```
bootstrap.memory_lock: true
```





```
cluster.name: es-cluster-5.3.1   配置集群名称 三台服务器保持一致

node.name: node-1                 配置单一节点名称，每个节点唯一标识

network.host: 0.0.0.0              设置绑定的ip地址

http.port: 9200                      端口

discovery.zen.ping.unicast.hosts: ["172.16.31.220", "172.16.31.221","172.16.31.224"]   集群节点ip或者主机

discovery.zen.minimum_master_nodes: 3    设置这个参数来保证集群中的节点可以知道其它N个有master资格的节点。默认为1，对于大的集群来说，可以设置大一点的值（2-4）

下面两行配置为haad插件配置，三台服务器一致。

http.cors.enabled: true
http.cors.allow-origin: "*"

ok，220服务器修改完毕。
```





查看系统中有哪些用户：

cut -d : -f 1 /etc/passwd

查看系统中有哪些组：

cut -d : -f 1 /etc/group



```
service elasticsearch status
service elasticsearch restart 
service elasticsearch status

cd /home/elasticsearch/
```





es 存在的问题

```
es 主节点被写挂
```



ES 写入量， 每秒45M







-   文档(document):索引和搜索时使用的主要数据载体，包含一个或多个存有数据的字段。 

-   字段(field):文档的一部分，包含名称和值两部分。 

-   词(term):一个搜索单元，表示文本中的一个词。 

-   标记(token):表示在字段文本中出现的词，由这个词的文本、开始和结束偏移量以及类 

  型组成。 





获取集群节点

```
http://172.16.16.120:9200/_cluster/state/nodes/
```



停止某个节点

```

```





========================================

###  配置文件位置[编辑](https://github.com/elastic/elasticsearch/edit/7.2/docs/reference/setup/configuration.asciidoc)

Elasticsearch有三个配置文件：

- `elasticsearch.yml` 用于配置Elasticsearch
- `jvm.options` 用于配置Elasticsearch JVM设置
- `log4j2.properties` 用于配置Elasticsearch日志记录



**最重要的系统配置**

获取配置方法

```
cat /proc/sys/vm/swappiness
ulimit -n
sysctl vm.max_map_count

```



设置

```
sysctl vm.swappiness=1
ulimit -n 65535
sysctl -w vm.max_map_count=262144

```



永久设置

 ```
echo "vm.swappiness=1" >> /etc/sysctl.conf
sysctl -p


vim /etc/security/limits.conf
* soft core    unlimited
* hard core    unlimited
* soft nofile  65535
* hard nofile  65535
 ```





设置`network.host` ， Elasticsearch 才会升级为生产

- 禁用交换



- 增加文件描述符



- 确保足够的虚拟内存



- 确保足够的线程



- JVM DNS 缓存设置



- 临时目录未安装 noexec



## ES 学习

> 索引

创建 索引的时候可以通过

修改 number_of_shards : 分片 

修改 number_of_replicas ：副本



#### 索引模版

创建好一个索引参数设置(settings) 和 映射(mapping)的模版，在创建新索引时指定模板名称就可以使用



index.shadow_replicas=true  索引是否应该使用副本，不在任何副本分片上重复文档操作

## ES  分析

批处理  6

![image-20190719104245406](/Users/weicheng/Library/Application Support/typora-user-images/image-20190719104245406.png)

批处理  18

![image-20190719104418029](/Users/weicheng/Library/Application Support/typora-user-images/image-20190719104418029.png)





```
sudo rpm --install elasticsearch-7.2.0-x86_64.rpm
```



```
###没有开始安装，请执行以下语句以配置elasticsearch服务以使用systemd自动启动
  sudo systemctl daemon-reload
  sudo systemctl enable elasticsearch.service
###您可以通过执行来启动elasticsearch服务
  sudo systemctl restart elasticsearch.service
在/ etc / elasticsearch中创建了elasticsearch keystore

```



```
sudo rpm --install kibana-7.2.0-x86_64.rpm
```

```
sudo -i service kibana start
sudo -i service kibana stop
```



ES 学习



```
// ES 的一些下划线字段
_id
_index
_score
_type
```



```
// 插入一个文档
PUT /get-together/group/1?pretty
{
  "name": "Elasticsearch Denver",
  "organizer": "lee"
}

// 创建一个索引
PUT /new-index
{
  "acknowledged": true
}

// 查看当前映射
GET /get-together/_mapping/group?pretty


// 获取自动生成的映射

//// 索引一篇新文档
PUT /get-together/new-events/1
{
    "name": "Late Night with Elasticsearch",
    "date": "2013-10-25T19:00"
}

//// 获取自动生成的映射
GET /get-together/_mapping/new-events?pretty

//// 定义新的映射
PUT /get-together/_mapping/new-events
{
    "new-events": {
        "properties": {
            "host": {
                "type": "string"
            }
        }
    }
}
```





映射是随着新文档自动创建的





> 概念理解

每篇文档属于一种类型

每种类型属于一个索引

索引认为是数据库

类型是数据库中的表

类型包含了映射中每个字段的定义

映射包括了该类型的文档中可能出现的所有字段，并告诉ES 如何索引一篇文档的多个字段。



预先定义自己的映射，在生产环境中





> 分段与合并

分段是建立索引的时候所创建的一块Lucene索引， 也称为分片。



![image-20190731173232204](/Users/weicheng/Library/Application Support/typora-user-images/image-20190731173232204.png)



在索引创建时增加分析器



### 增加索引的性能

```
临时减少集群中副本分片的数量

lucene 分段， 刷新、冲刷、合并策略 如何影响索引和搜索性能的。
```



#### 分段

ES接到发生的文档，会将其索引到内存中，分段（倒排索引）

刷新(refresh) ：会让ES重新打开索引，让新建的文档可以被搜索

冲刷(flush): 将索引的数据从内存写入磁盘，比较耗费资源

​	冲刷操作的触发条件：

 - 内存缓冲区已满
 - 自从上次冲刷后超过了一定的时间
 - 事物日志达到了一定的阀值



合并(Lucene) :随着索引的数据变多，小分段被合并为大分段，设置分段合并时间，分段合并大小

存储 和存储限流：ES调节每秒写入的字节数



```
// 获取索引设置
GET /get-together/_settings?pretty

// 手动刷新
GET /get-together/_refresh

// 设置刷新时间
"index.refresh_interval": "5s"


//// 控制冲刷频率
内存缓冲区大小 在 elasticsearch.yml中定义，
indices.memory.index_buffer_size=10% 或者 100MB 

具体索引设置
index.translog: {
    "flush_threshold_size": "500mb",
    "flush_threshold_period": "10m"
}

```



分段是不变的一组文件，用来存储索引数据，容易被缓存

一、将分段的总数据量保持在受控的范围内

二、真正的删除文档



合并发生在索引、更新、删除文档的时候。想要快速索引，就需要少合并，牺牲一些查询性能

![image-20190731203834008](/Users/weicheng/Library/Application Support/typora-user-images/image-20190731203834008.png)

```
基于具体的索引上的设置
PUT /get-together/_settings
{
    "index.merge": {
        "policy": {
            "segments_per_tier": 5,
            "max_merge_at_once": 5,
            "max_merged_segment": "1gb"
        },
     "scheduler.max_thread_count": 1
    }
}
```



更新索引 和 更新文档是一回事么？



垃圾回收（GC）太多的回收调优技巧

- 减小索引缓冲区大小
- 减少过滤器缓存和分片查询缓存的大小
- 减少搜索和聚集请求中size  参数的值(对于聚集，还需要考虑到 shard_size)
- 处理大规模的数据，需要增加一些非数据节点和非主节点来扮演客户端的角色，他们负责聚合每个分片的搜索结果，以及聚集操作



### 索引模版

创建新的索引 和 相关映射

模版定义位于Elasticsearch 配置所在的地方，位于一个模板目录下，该路径在配置文件 elasticsearch.yml  中被定义为 path.conf

/usr/share/elasticsearch/bin/elasticsearch



定义模版



**模版结构**

```
{
  "order": 0,                // 模板优先级
  "template": "logstash_*",  // 模板匹配的方式
  "settings": {...},         // 索引设置
  "mappings": {...},         // 索引中各字段的映射定义
  "aliases": {...}           // 索引的别名
}

```



**通用索引模版**

```json
{
  "order": 0,
  "template": "*",
  "settings": {
    "index": {
      "refresh_interval": "5s",
      "number_of_shards": "3",
      "max_result_window": 10000,
      "translog": {
        "flush_threshold_size": "500mb",
        "sync_interval": "30s",
        "durability": "async"
      },
      "merge": {
        "scheduler": {
          "max_merge_count": "100",
          "max_thread_count": "1"
        }
      },
      "analysis": {
        "analyzer": {
          "hanlp_array": {
            "type": "pattern",
            "pattern": "[,;。？?！!，、；：:“”‘’《》【】（）~〈〉「」『』…/\\[\\]<>\"\\`\\^*+]+",
            "lowercase": "true"
          }
        }
      },
      "number_of_replicas": "0",
      "unassigned": {
        "node_left": {
          "delayed_timeout": "2m"
        }
      }
    }
  },
  "mappings": {
    "doc": {
      "dynamic_date_formats": ["yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||yyyy-MM||yyyy/MM/dd||yyyy/MM||strict_date_optional_time||epoch_millis"],
      "_all": {
        "enabled": false
      },
      "properties": {
        "html": {
          "index": "false",
          "doc_values": "false",
          "norms": "false",
          "fielddata": "false",
          "store": "false",
          "type": "text"
        }
      },
      "dynamic_templates": [
        {
          "id_field": {
            "mapping": {
              "type": "keyword",
              "store": "true"
            },
            "match": "*id"
          }
        },
        {
          "no_field": {
            "mapping": {
              "type": "keyword",
              "store": "true"
            },
            "match": "*no"
          }
        },
        {
          "code_field": {
            "mapping": {
              "type": "keyword",
              "store": "true"
            },
            "match": "*code"
          }
        },
        {
          "geo_field": {
            "mapping": {
              "type": "geo_point",
              "store": "true"
            },
            "match": "*_geo"
          }
        },
        {
          "ip_field": {
            "mapping": {
              "type": "ip",
              "store": "true"
            },
            "match": "*_ip"
          }
        },
        {
          "len_field": {
            "mapping": {
              "type": "integer",
              "store": "true"
            },
            "match": "*_len"
          }
        },
        {
          "num_field": {
            "mapping": {
              "type": "integer",
              "store": "true"
            },
            "match": "*_num"
          }
        },
        {
          "long_field": {
            "mapping": {
              "type": "long",
              "store": "true"
            },
            "match": "*_long"
          }
        },
        {
          "ft_field": {
            "mapping": {
              "type": "float",
              "store": "true"
            },
            "match": "*_ft"
          }
        },
        {
          "db_field": {
            "mapping": {
              "type": "double",
              "store": "true"
            },
            "match": "*_db"
          }
        },
        {
          "typ_field": {
            "mapping": {
              "type": "keyword",
              "store": "true"
            },
            "match": "*_typ*"
          }
        },
        {
          "sta_field": {
            "mapping": {
              "type": "keyword",
              "store": "true"
            },
            "match": "*_sta"
          }
        },
        {
          "lvl_field": {
            "mapping": {
              "type": "keyword",
              "store": "true"
            },
            "match": "*_lvl"
          }
        },
        {
          "flg_field": {
            "mapping": {
              "type": "keyword",
              "store": "true"
            },
            "match": "*_flg"
          }
        },
        {
          "dtm_field": {
            "mapping": {
              "type": "date",
              "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||yyyy-MM||yyyy||yyyy/MM/dd||yyyy/MM||strict_date_optional_time||epoch_millis",
              "store": "true"
            },
            "match": "*_dtm"
          }
        },
        {
          "ns_field": {
            "mapping": {
              "index": "false",
              "doc_values": "false",
              "norms": "false",
              "fielddata": "false",
              "store": "false"
            },
            "match": "*_ns"
          }
        },
        {
          "bin_field": {
            "mapping": {
              "type": "binary",
              "doc_values": "false",
              "norms": "false",
              "fielddata": "false",
              "store": "false"
            },
            "match": "*_bin"
          }
        },
        {
          "raw_field": {
            "mapping": {
              "type": "binary",
              "doc_values": "false",
              "norms": "false",
              "fielddata": "false",
              "store": "false"
            },
            "match": "*_raw"
          }
        },
        {
          "std_field": {
            "mapping": {
              "store": "true",
              "analyzer": "standard",
              "type": "text"
            },
            "match": "*_std"
          }
        },
        {
          "url_field": {
            "mapping": {
              "store": "true",
              "type": "keyword",
              "doc_values": "false",
              "norms": "false",
              "fielddata": "false"
            },
            "match": "*_url"
          }
        },
        {
          "tag_field": {
            "mapping": {
              "store": "true",
              "type": "text",
              "analyzer": "ik_max_word",
              "search_analyzer": "ik_max_word",
              "search_quote_analyzer": "ik_max_word",
              "fields": {
                "orginal": {
                  "type": "keyword"
                },
                "array": {
                  "analyzer": "hanlp_array",
                  "search_analyzer": "ik_max_word",
                  "type": "text",
                  "fielddata": "true"
                }
              }
            },
            "match": "*tag"
          }
        },
        {
          "file_field": {
            "mapping": {
              "type": "attachment",
              "fields": {
                "content": {
                  "store": "false",
                  "type": "text"
                },
                "author": {
                  "store": "true",
                  "type": "text"
                },
                "title": {
                  "store": "true",
                  "type": "text"
                },
                "keywords": {
                  "store": "true",
                  "type": "text"
                },
                "content_length": {
                  "store": "true"
                },
                "language": {
                  "store": "true"
                },
                "date": {
                  "store": "true",
                  "type": "date"
                },
                "content_type": {
                  "store": "true"
                }
              }
            },
            "match": "*_file"
          }
        },
        {
          "path_field": {
            "mapping": {
              "store": "true",
              "analyzer": "hanlp_array",
              "search_analyzer": "ik_max_word",
              "type": "text",
              "fielddata": "true",
              "fields": {
                "normal": {
                  "type": "text",
                  "analyzer": "ik_max_word",
                  "search_analyzer": "ik_max_word",
                  "search_quote_analyzer": "ik_max_word"
                },
                "orginal": {
                  "type": "keyword"
                }
              }
            },
            "match": "*_path"
          }
        },
        {
          "arr_field": {
            "mapping": {
              "store": "true",
              "analyzer": "hanlp_array",
              "search_analyzer": "ik_max_word",
              "type": "text",
              "fielddata": "true",
              "fields": {
                "normal": {
                  "type": "text",
                  "analyzer": "ik_max_word",
                  "search_analyzer": "ik_max_word",
                  "search_quote_analyzer": "ik_max_word"
                }
              }
            },
            "match": "*_arr"
          }
        },
        {
          "string_field": {
            "mapping": {
              "type": "text",
              "analyzer": "ik_max_word",
              "search_analyzer": "ik_max_word",
              "search_quote_analyzer": "ik_max_word",
              "term_vector": "with_positions_offsets",
              "fields": {
                "orginal": {
                  "type": "keyword",
                  "ignore_above": "36"
                }
              }
            },
            "match_mapping_type": "string"
          }
        }
      ]
    }
  }
}

```



设置默认模版为：

```
PUT /_template/default_template
{
  "template": "*", 
  "order":    1, 
  "settings": {
    "index": {
      "refresh_interval": "5s",
      "number_of_shards": "3",
      "max_result_window": 10000,
      "translog": {
        "flush_threshold_size": "500mb",
        "sync_interval": "30s",
        "durability": "async"
      },
      "merge": {
        "scheduler": {
          "max_merge_count": "100",
          "max_thread_count": "1"
        }
      },
      "analysis": {
        "analyzer": {
          "hanlp_array": {
            "type": "pattern",
            "pattern": "[,;。？?！!，、；：:“”‘’《》【】（）~〈〉「」『』…/\\[\\]<>\"\\`\\^*+]+",
            "lowercase": "true"
          }
        }
      },
      "number_of_replicas": "0",
      "unassigned": {
        "node_left": {
          "delayed_timeout": "2m"
        }
      }
    }
  }
}
```

