mongod.exe --bind_ip yourIPadress --logpath "C:\data\dbConf\mongodb.log" --logappend --dbpath "C:\data\db" --port yourPortNumber --serviceName "YourServiceName" --serviceDisplayName "YourServiceName" --install



mongod --dbpath /data/mongodb/db --logpath /data/mongodb/log/mongodb.log --logappend

all output going to: /data/mongodb/log/mongodb.log


mongod --dbpath /data/mongodb/db --logpath /data/mongodb/log/mongodb.log --logappend 


# 教程链接地址：http://blog.csdn.net/flyfish111222/article/details/51886787
-------------------------------------------------------------


SQL术语/概念    | 	MongoDB术语/概念  |   解释/说明

—|—|—

database  |	database 	|   数据库
table       |   collection 	|   数据库表/集合
row 	    |   document 	|   数据记录行/文档
column      |   field 	        |   数据字段/域
index 	    |   index 	        |   索引
table joins |	表连接,MongoDB | 不支持

primary key |	primary key 	|   主键,MongoDB自动将_id字段设置为主键
--------------------------------------------------------------



## MongoDB 工具

MongoDB 在 bin 目录下提供了一系列有用的工具，这些工具提供了 MongoDB 在运维管理上 的方便。

| 工具                                       | 描述                                       |
| ---------------------------------------- | ---------------------------------------- |
| [mongosniff](http://www.mongodb.org.cn/manual/201.html) | mongodb监测工具，作用类似于 tcpdump                |
| [mongotop](http://www.mongodb.org.cn/manual/200.html) | 跟踪一个MongoDB的实例，查看哪些大量的时间花费在读取和写入数据       |
| [mongostat](http://www.mongodb.org.cn/manual/199.html) | mongodb自带的状态检测工具                         |
| [mongoexport](http://www.mongodb.org.cn/manual/198.html) | Mongodb数据导出工具                            |
| [mongod.exe](http://www.mongodb.org.cn/manual/188.html) | MongoDB服务启动工具                            |
| [mongos](http://www.mongodb.org.cn/manual/189.html) | 分片路由，如果使用了 sharding 功能，则应用程序连接的是 mongos 而不是 mongod |
| [mongo](http://www.mongodb.org.cn/manual/190.html) | 客户端命令行工具，其实也是一个 js 解释器，支持 js 语法          |
| [mongodump](http://www.mongodb.org.cn/manual/193.html) | MongoDB数据备份工具                            |
| [mongorestore](http://www.mongodb.org.cn/manual/194.html) | MongoDB数据恢复工具                            |
| [bsondump](http://www.mongodb.org.cn/manual/195.html) | 将 bson 格式的文件转储为 json 格式的数据              |
| [mongooplog](http://www.mongodb.org.cn/manual/196.html) |                                          |
| [mongoimport](http://www.mongodb.org.cn/manual/197.html) | Mongodb数据导入工具                            |
| [mongoperf](http://www.mongodb.org.cn/manual/202.html) |                                          |
| [mongofiles](http://www.mongodb.org.cn/manual/203.html) | GridFS 管理工具，可实现二制文件的存取                   |



# Run MongoDB

- 创建数据存放目录, 并确保对该目录有写权限

  ```
  sudo mkdir -p /data/db/
  ```


- 可以使用service 来启动mongo数据库

  ```
  sudo service mongodb start/stop
  ```

  service的默认权限是mongodb用户，一般不是root用户

- 不用参数启动, 可以使用

  ```
  sudo mongod
  ```

- 运行后，出现等待连接为成功 

  ```
  waiting for connections on port 27017
  ```

   启动 成功后，mongo 会运行一个http服务器，能够获取 数据库 的信息

  ```
  http://localhost:28017
  ```







## 常见命令

-  启动shell

  ```
  $ mongo  
  #运行mongo启动mongo shell
  ```

- 连接数据库🔗

   ```

   ```

   ​

- 查看数据库列表

   ```
   show dbs
   ```

- 切换到数据库

   ```
   use 
   ```

   ​

- ​

- 查看数据库中的集合列表

   ```
   show tables
   ```

- 显示当前使用的数据库

   ```
   db
   #默认数据库为test
   ```

- 切换数据库

   ```
   use <db>
   use test
   ```

- 列出可用数据库

   ```
   show dbs
   ```

- 插入数据

   ```
   # 语法格式
   db.COLLECTION_NAME.insert(document)

   >db.col.insert({title: 'MongoDB 教程', 
       by: '菜鸟教程',
       url: 'http://www.runoob.com',
       likes: 100
   })

   将文档插入到名为col的集合中。如果col集合当前不存在，操作将创建集合,并插入数据
   ```

- 查询数据

   ```
   # 语法格式
   db.collection.find(query, projection)
   # query : 可选，使用查询操作符指定查询条件
   # projection : 可选，使用投影操作符指定返回的键，默认查询时返回文档中所有键值，默认省略

   >db.col.find().pretty()
   # pretty() 方法用来格式化数据
   ```

-  删除数据库

-  删除集合

   ```
   db.collection.drop()
   ```

   ​










   ```

-  - 查询集合中数据总量

   ```
     db.barber_comment_infos.find({}).count();
     ```
    
     ​


##  

Query 条件

### MongoDB 与 RDBMS Where 语句比较

如果你熟悉常规的 SQL 数据，通过下表可以更好的理解 MongoDB 的条件语句查询：

| 操作    | 格式                       | RDBMS中的类似语句         | 范例                                       |
| ----- | ------------------------ | ------------------- | ---------------------------------------- |
| 等于    | `{<key>:<value>`}        | `where by = '菜鸟教程'` | `db.col.find({"by":"菜鸟教程"}).pretty()`    |
| 小于    | `{<key>:{$lt:<value>}}`  | `where likes < 50`  | `db.col.find({"likes":{$lt:50}}).pretty()` |
| 小于或等于 | `{<key>:{$lte:<value>}}` | `where likes <= 50` | `db.col.find({"likes":{$lte:50}}).pretty()` |
| 大于    | `{<key>:{$gt:<value>}}`  | `where likes > 50`  | `db.col.find({"likes":{$gt:50}}).pretty()` |
| 大于或等于 | `{<key>:{$gte:<value>}}` | `where likes >= 50` | `db.col.find({"likes":{$gte:50}}).pretty()` |
| 不等于   | `{<key>:{$ne:<value>}}`  | `where likes != 50` | `db.col.find({"likes":{$ne:50}}).pretty()` |

------

MongoDB OR 条件语句使用了关键字 **$or**,语法格式如下：

```
>db.col.find(
   {
      $or: [
	     {key1: value1}, {key2:value2}
      ]
   }
).pretty()
```

# pymongo 安装





## 包组件 mongoexport

`mongoexport` 是一个实用程序，可以生成一个JSON或CSV导出存储在MongoDB实例中的数据。

`mongoexport`从系统命令行运行，而不是[`mongo`](https://docs.mongodb.com/manual/reference/program/mongo/#bin.mongo)shell。

