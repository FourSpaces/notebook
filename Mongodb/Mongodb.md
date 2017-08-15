mongod.exe --bind_ip yourIPadress --logpath "C:\data\dbConf\mongodb.log" --logappend --dbpath "C:\data\db" --port yourPortNumber --serviceName "YourServiceName" --serviceDisplayName "YourServiceName" --install



mongod --dbpath /data/mongodb/db --logpath /data/mongodb/log/mongodb.log --logappend

all output going to: /data/mongodb/log/mongodb.log


mongod --dbpath /data/mongodb/db --logpath /data/mongodb/log/mongodb.log --logappend 


# 教程链接地址：http://blog.csdn.net/flyfish111222/article/details/51886787
-------------------------------------------------------------
SQL术语/概念| 	MongoDB术语/概念     解释/说明
database    |	database 	|   数据库
table       |   collection 	|   数据库表/集合
row 	    |   document 	|   数据记录行/文档
column      |   field 	        |   数据字段/域
index 	    |   index 	        |   索引
table joins |	表连接,MongoDB不支持
primary key |	primary key 	|   主键,MongoDB自动将_id字段设置为主键
--------------------------------------------------------------



常见命令：
创建数据库：use DATABASE_NAME
[如果数据库不存在，则创建数据库，否则切换到指定数据库]

查看所有数据库：show dbs
[创建的数据库中 没有数据的时候，不显示数据库名]
复制数据库
数据表的复制 db.runCommand({cloneCollection:"commit.daxue",from:"198.61.104.31:27017"});
数据库的复制  db.copyDatabase("user","user","198.61.104.31:27017");

向数据库[runoob]中插入数据：db.runoob.insert({"name":"xiaoming"})

删除数据库，切换到对应的库，执行：db.dropDatabase() 
删除集合，切换到对应的库，执行：db.collection.drop() 
[collection 为对应的集合]





# MongoDB 工具

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
  $ mongo  #运行mongo启动shell
  ```

-  连接数据库🔗

   ```

   ```

   ​

-  查看数据库列表

   ```
   show dbs
   ```

-  切换到数据库

   ```

   ```

   ​

-  ​

-  查看数据库中的集合列表

   ```
   show tables
   ```

   ​



# pymongo 安装

