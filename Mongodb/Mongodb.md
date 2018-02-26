mongod.exe --bind_ip yourIPadress --logpath "C:\data\dbConf\mongodb.log" --logappend --dbpath "C:\data\db" --port yourPortNumber --serviceName "YourServiceName" --serviceDisplayName "YourServiceName" --install



mongod --dbpath /data/mongodb/db --logpath /data/mongodb/log/mongodb.log --logappend

all output going to: /data/mongodb/log/mongodb.log


mongod --dbpath /data/mongodb/db --logpath /data/mongodb/log/mongodb.log --logappend 


# 教程链接地址：http://blog.csdn.net/flyfish111222/article/details/51886787
-------------------------------------------------------------


## MongoDB 基础

SQL术语/概念    | 	MongoDB术语/概念  |   解释/说明

—|—|—

database  |	database 	|   数据库
table       |   collection 	|   数据库表/集合（一组文档）
row 	    |   document 	|   数据记录行/文档
column      |   field 	        |   数据字段/域
index 	    |   index 	        |   索引
table joins |	表连接,MongoDB | 不支持

primary key |	primary key 	|   主键,MongoDB自动将_id字段设置为主键
--------------------------------------------------------------

- 特殊意义的字符

  ```
  . 
  $
  ```

- MondoDB 会对字段重新排序

-  ——————
  集合的动态模式是指 集合中的文档可以是各种各样的。

  子集合：
  GridFS:一种用于存储大文件的协议，使用子集合存储文件的元数据，这样就可以与集合中的其他文件块内容隔离开来

- 保留的数据库名：
  admin：root数据库，从身份验证角度来说。
  local： 一台服务器上的所有本地集合都可以存储在这个数据库中。不可以复制
  config： 分片信息会存储在config数据库中。




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

- 查看数据库列表

    ```
    show dbs
    ```

- 切换到数据库

    ```
    use <db>
    use test
    ```

- 查看数据库中的集合列表

    ```
    show tables
    ```

- 显示当前使用的数据库

    ```
    db
    #默认数据库为test
    ```


#### 创建、更新 和删除文档

- 插入数据(单次插入／批量插入)

    ```
    # 单次插入 语法格式
    db.COLLECTION_NAME.insert(document)

    /> db.col.insert({title: 'MongoDB 教程', 
       by: '菜鸟教程',
       url: 'http://www.runoob.com',
       likes: 100
      })
    将文档插入到名为col的集合中。如果col集合当前不存在，操作将创建集合,并插入数据

    # 批量插入
    db.COLLECTION_NAME.batchInsert(document)
    /> db.col.batchInsert([{'name':'dawei'},{'name':'kevin'},{'name':'suse'}])
    在Mongodb 中能接受的最大消息的长度是有限制的。

    ## 插入数据后，Mongodb 会检查插入文档的大小。

    ```

- 查询数据
    ```
    # 语法格式
    db.collection.find(query, projection)
    db.collection.findOne(query, projection)
    # query : 可选，使用查询操作符指定查询条件
    # projection : 可选，使用投影操作符指定返回的键，默认查询时返回文档中所有键值，默认省略
    ```


    db.col.find().pretty()
    # pretty() 方法用来格式化数据
    
    ​```

- 更新数据
    ```
    db.collection.drop()
    ```

- 删除数据
    ```
    # 删除所有文档
    db.col.remove()

    # 删除指定条件的文档
    db.col.remove({'name':'kevin'})

    # 删除指定集合
    db.col.drop()
    ```


- 备份数据库

   ```
   mongodump -h dbhost -d dbname -o dbdirectory
   ```


   - -h：

     MongDB所在服务器地址，例如：127.0.0.1，当然也可以指定端口号：127.0.0.1:27017

   - -d：

     需要备份的数据库实例，例如：test

   - -o：

     备份的数据存放位置，例如：c:\data\dump，当然该目录需要提前建立，在备份完成后，系统自动在dump目录下建立一个test目录，这个目录里面存放该数据库实例的备份数据。



- 还原数据库

   ```
   mongorestore -h <hostname><:port> -d dbname <path>
   ```


   - --host <:port>, -h <:port>：

     MongoDB所在服务器地址，默认为： localhost:27017

   - --db , -d ：

     需要恢复的数据库实例，例如：test，当然这个名称也可以和备份时候的不一样，比如test2

   - --drop：

     恢复的时候，先删除当前数据，然后恢复备份的数据。就是说，恢复后，备份后添加修改的数据都会被删除，慎用哦！

   - <path>：

     mongorestore 最后的一个参数，设置备份数据所在位置，例如：c:\data\dump\test。

     你不能同时指定 <path> 和 --dir 选项，--dir也可以设置备份目录。

   - --dir：

     指定备份的目录

     你不能同时指定 <path> 和 --dir 选项。



- 倒入数据到数据库

  - 导入json  数据到数据库中 

    ```
    # 将当前路径下的meituan-shops.json 倒入到meituantest库中的ll 文档中
    mongoimport --db meituantest --collection ll --file meituan-shops.json  --jsonArray
    ​```
    ```

  - 导入csv  数据到数据库中
    ···
    mongoimport --db network1 --collection networkmanagement --type csv --headerline --ignoreBlanks --file /home/erik/Documents/networkmanagement-1.csv
    ···

- 导出数据到数据库
  - 导出数据到 csv 文件中
    ``` mongodb
    mongoexport  --csv -f district,district_url,floor,housr_area,house_name,house_url,house_direction,house_status,house_structure,lease_cycle,leasing_method,payment_method,regional_location,rental_price,subway,usage,lng,lat -d lianjiazufang -c guangdong -o  ./test.csv
    ```
    district,district_url,floor,housr_area,house_name,house_url,house_direction,house_status,house_structure,lease_cycle,leasing_method,payment_method,regional_location,rental_price,subway,usage,lng,lat

- 查询集合中数据总量

   ```
     db.barber_comment_infos.find({}).count();
   ```


- 获取数据库的大小, 字节b 作为大小衡量单位

   ```
   /> use databasename
   /> db.stats(); 
   { 
     "db" : "test",        //当前数据库 
     "collections" : 3,      //当前数据库多少表 
     "objects" : 4,        //当前数据库所有表多少条数据 
     "avgObjSize" : 51,      //每条数据的平均大小 
     "dataSize" : 204,      //所有数据的总大小 
     "storageSize" : 16384,    //所有数据占的磁盘大小 
     "numExtents" : 3, 
     "indexes" : 1,        //索引数 
     "indexSize" : 8176,     //索引大小 
     "fileSize" : 201326592,   //预分配给数据库的文件大小 
     "nsSizeMB" : 16, 
     "dataFileVersion" : { 
       "major" : 4, 
       "minor" : 5 
     }, 
     "ok" : 1 
   } 
   ```

   ​

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



## Mongodb 的常用查询操作

- 查询在某个范围内的数据。

  ```
  # 查询 type 为 1， 且 x 在11 到 21的范围内的数据
  db.collection.find({'type':1, 'x':{'$gt':11,'$lt':21}})
  ```

- 对查询的数据做排序

  ```
  # 对数据按time字段进行排序，
  # 第二个参数为1时从小到大排 顺序，为-1时从大到小排 逆序
  db.collection.find().sort('time',-1)
  ```

- 查询包含某字段的数据
  ```
  # 查询 拥有real_id字段的数据，
  # $exists 参数为 False时，查询不包含 拥有real_id字段的数据
  db.collection.find({"real_id":{'$exists':True}})
  ```






# pymongo 安装





## 包组件 mongoexport

`mongoexport` 是一个实用程序，可以生成一个JSON或CSV导出存储在MongoDB实例中的数据。

`mongoexport`从系统命令行运行，而不是[`mongo`](https://docs.mongodb.com/manual/reference/program/mongo/#bin.mongo)shell。

导入数据库 CSV
mongoimport --db erhoufang3 --collection clean_room1 --type csv --headerline --ignoreBlanks --file /Users/weicheng/docker/clean_room_p.csv

