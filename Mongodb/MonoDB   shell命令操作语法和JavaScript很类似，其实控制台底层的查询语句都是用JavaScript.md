#### 1. MongoDB的获取和安装

（1）获取地址 http://www.mongodb.org/downloads 根据自己需要选择相应的版本，linux下可以使用wget 命令。

（2）解压 mongodb-win32-i386-1.8.1

（3）创建数据存放文件夹，mongodb默认的数据目录 /data/db

C:/> mkdir /data

C:/> mkdir /data/db

（4）运行 MongoDB

mongod.exe - 数据库的服务器端，相当于mysql的 mysqld命令，启动服务器端

mongo.exe - 数据库的客户端,相当于mysql的mysql命令，打开管理控制台

启动服务

mongod.exe --dbpath F:/DataBase/MongoDB/db/

--dbpath 数据文件存放路径 

--port 数据服务端口

C:/> cd /my_mongo_dir/bin

C:/my_mongo_dir/bin > mongod //启动mongod 服务器，默认的数据库路径 /data/db，端口27071

启动客户端

mongo.exe cclove

cclove 所连接的数据库名称

C:/> cd /my_mongo_dir/bin

C:/my_mongo_dir/bin> mongo

#### 2. 熟悉MongoDB的数据操作语句，类sql

##### 数据库操作语法

mongo --path

db.AddUser(username,password) 添加用户

db.auth(usrename,password) 设置数据库连接验证

db.cloneDataBase(fromhost) 从目标服务器克隆一个数据库

db.commandHelp(name) returns the help for the command

db.copyDatabase(fromdb,todb,fromhost) 复制数据库fromdb---源数据库名称，todb---目标数据库名称，fromhost---源数据库服务器地址

db.createCollection(name,{size:3333,capped:333,max:88888}) 创建一个数据集，相当于一个表

db.currentOp() 取消当前库的当前操作

db.dropDataBase() 删除当前数据库

db.eval(func,args) run code server-side

db.getCollection(cname) 取得一个数据集合，同用法：db['cname'] or db.cname

db.getCollenctionNames() 取得所有数据集合的名称列表

db.getLastError() 返回最后一个错误的提示消息

db.getLastErrorObj() 返回最后一个错误的对象

db.getMongo() 取得当前服务器的连接对象get the server connection object

db.getMondo().setSlaveOk() allow this connection to read from then nonmaster membr of a replica pair

db.getName() 返回当操作数据库的名称

db.getPrevError() 返回上一个错误对象

db.getProfilingLevel() ?什么等级

db.getReplicationInfo() ?什么信息

db.getSisterDB(name) get the db at the same server as this onew

db.killOp() 停止（杀死）在当前库的当前操作

db.printCollectionStats() 返回当前库的数据集状态

db.printReplicationInfo()

db.printSlaveReplicationInfo()

db.printShardingStatus() 返回当前数据库是否为共享数据库

db.removeUser(username) 删除用户

db.repairDatabase() 修复当前数据库

db.resetError()

db.runCommand(cmdObj) run a database command. if cmdObj is a string, turns it into {cmdObj:1}

db.setProfilingLevel(level) 0=off,1=slow,2=all

db.shutdownServer() 关闭当前服务程序

db.version() 返回当前程序的版本信息

##### 数据集(表)操作语法

db.linlin.find({id:10}) 返回linlin数据集ID=10的数据集

db.linlin.find({id:10}).count() 返回linlin数据集ID=10的数据总数

db.linlin.find({id:10}).limit(2) 返回linlin数据集ID=10的数据集从第二条开始的数据集

db.linlin.find({id:10}).skip(8) 返回linlin数据集ID=10的数据集从0到第八条的数据集

db.linlin.find({id:10}).limit(2).skip(8) 返回linlin数据集ID=1=的数据集从第二条到第八条的数据

db.linlin.find({id:10}).sort() 返回linlin数据集ID=10的排序数据集

db.linlin.findOne([query]) 返回符合条件的一条数据

db.linlin.getDB() 返回此数据集所属的数据库名称

db.linlin.getIndexes() 返回些数据集的索引信息

db.linlin.group({key:...,initial:...,reduce:...[,cond:...]})

db.linlin.mapReduce(mayFunction,reduceFunction,<optional params>)

db.linlin.remove(query) 在数据集中删除一条数据

db.linlin.renameCollection(newName) 重命名些数据集名称

db.linlin.save(obj) 往数据集中插入一条数据

db.linlin.stats() 返回此数据集的状态

db.linlin.storageSize() 返回此数据集的存储大小

db.linlin.totalIndexSize() 返回此数据集的索引文件大小

db.linlin.totalSize() 返回些数据集的总大小

db.linlin.update(query,object[,upsert_bool]) 在此数据集中更新一条数据

db.linlin.validate() 验证此数据集

db.linlin.getShardVersion() 返回数据集共享版本号

db.linlin.find({'name':'foobar'}) select * from linlin where name='foobar'

db.linlin.find() select * from linlin

db.linlin.find({'ID':10}).count() select count(*) from linlin where ID=10

db.linlin.find().skip(10).limit(20) 从查询结果的第十条开始读20条数据 select * from linlin limit 10,20 ----------mysql

db.linlin.find({'ID':{$in:[25,35,45]}}) select * from linlin where ID in (25,35,45)

db.linlin.find().sort({'ID':-1}) select * from linlin order by ID desc

db.linlin.distinct('name',{'ID':{$lt:20}}) select distinct(name) from linlin where ID<20

db.linlin.group({key:{'name':true},cond:{'name':'foo'},reduce:function(obj,prev){prev.msum+=obj.marks;},initial:{msum:0}})

select name,sum(marks) from linlin group by name

db.linlin.find('this.ID<20',{name:1}) select name from linlin where ID<20

db.linlin.insert({'name':'foobar','age':25}) insert into linlin ('name','age') values('foobar',25)

db.linlin.insert({'name':'foobar','age':25,'email':'cclove2@163.com'})

db.linlin.remove({}) delete * from linlin

db.linlin.remove({'age':20}) delete linlin where age=20

db.linlin.remove({'age':{$lt:20}}) delete linlin where age<20

db.linlin.remove({'age':{$lte:20}}) delete linlin where age<=20

db.linlin.remove({'age':{$gt:20}}) delete linlin where age>20

db.linlin.remove({'age':{$gte:20}}) delete linlin where age>=20

db.linlin.remove({'age':{$ne:20}}) delete linlin where age!=20

db.linlin.update({'name':'foobar'},{$set:{'age':36}}) update linlin set age=36 where name='foobar'

db.linlin.update({'name':'foobar'},{$inc:{'age':3}}) update linlin set age=age+3 where name='foobar'

#### 官方提供的操作语句对照表：

上行：SQL 操作语句

下行：Mongo 操作语句

CREATE TABLE USERS (a Number, b Number)

db.createCollection("mycoll")

INSERT INTO USERS VALUES(1,1)

db.users.insert({a:1,b:1})

SELECT a,b FROM users

db.users.find({}, {a:1,b:1})

SELECT * FROM users

db.users.find()

SELECT * FROM users WHERE age=33

db.users.find({age:33})

SELECT a,b FROM users WHERE age=33

db.users.find({age:33}, {a:1,b:1})

SELECT * FROM users WHERE age=33 ORDER BY name

db.users.find({age:33}).sort({name:1})

SELECT * FROM users WHERE age>33

db.users.find({'age':{$gt:33}})})

SELECT * FROM users WHERE age<33

db.users.find({'age':{$lt:33}})})

SELECT * FROM users WHERE name LIKE "%Joe%"

db.users.find({name:/Joe/})

SELECT * FROM users WHERE name LIKE "Joe%"

db.users.find({name:/^Joe/})

SELECT * FROM users WHERE age>33 AND age<=40

db.users.find({'age':{$gt:33,$lte:40}})})

SELECT * FROM users ORDER BY name DESC

db.users.find().sort({name:-1})

SELECT * FROM users WHERE a=1 and b='q'

db.users.find({a:1,b:'q'})

SELECT * FROM users LIMIT 10 SKIP 20

db.users.find().limit(10).skip(20)

SELECT * FROM users WHERE a=1 or b=2

db.users.find( { $or : [ { a : 1 } , { b : 2 } ] } )

SELECT * FROM users LIMIT 1

db.users.findOne()

SELECT DISTINCT last_name FROM users

db.users.distinct('last_name')

SELECT COUNT(*y) FROM users

db.users.count()

SELECT COUNT(*y) FROM users where AGE > 30

db.users.find({age: {'$gt': 30}}).count()

SELECT COUNT(AGE) from users

db.users.find({age: {'$exists': true}}).count()

CREATE INDEX myindexname ON users(name)

db.users.ensureIndex({name:1})

CREATE INDEX myindexname ON users(name,ts DESC)

db.users.ensureIndex({name:1,ts:-1})

EXPLAIN SELECT * FROM users WHERE z=3

db.users.find({z:3}).explain()

UPDATE users SET a=1 WHERE b='q'

db.users.update({b:'q'}, {$set:{a:1}}, false, true)

UPDATE users SET a=a+2 WHERE b='q'

db.users.update({b:'q'}, {$inc:{a:2}}, false, true)

DELETE FROM users WHERE z="abc"

db.users.remove({z:'abc'});

#### Mongodb启动命令mongod参数说明

| --quiet                | # 安静输出                                   |
| ---------------------- | ---------------------------------------- |
| --port arg             | # 指定服务端口号，默认端口27017                      |
| --bind_ip arg          | # 绑定服务IP，若绑定127.0.0.1，则只能本机访问，不指定默认本地所有IP |
| --logpath arg          | # 指定MongoDB日志文件，注意是指定文件不是目录              |
| --logappend            | # 使用追加的方式写日志                             |
| --pidfilepath arg      | # PID File 的完整路径，如果没有设置，则没有PID文件         |
| --keyFile arg          | # 集群的私钥的完整路径，只对于Replica Set 架构有效         |
| --unixSocketPrefix arg | # UNIX域套接字替代目录,(默认为 /tmp)                |
| --fork                 | # 以守护进程的方式运行MongoDB，创建服务器进程              |
| --auth                 | # 启用验证                                   |
| --cpu                  | # 定期显示CPU的CPU利用率和iowait                  |
| --dbpath arg           | # 指定数据库路径                                |
| --diaglog arg          | # diaglog选项 0=off 1=W 2=R 3=both 7=W+some reads |
| --directoryperdb       | # 设置每个数据库将被保存在一个单独的目录                    |
| --journal              | # 启用日志选项，MongoDB的数据操作将会写入到journal文件夹的文件里 |
| --journalOptions arg   | # 启用日志诊断选项                               |
| --ipv6                 | # 启用IPv6选项                               |
| --jsonp                | # 允许JSONP形式通过HTTP访问（有安全影响）               |
| --maxConns arg         | # 最大同时连接数 默认2000                         |
| --noauth               | # 不启用验证                                  |
| --nohttpinterface      | # 关闭http接口，默认关闭27018端口访问                 |
| --noprealloc           | # 禁用数据文件预分配(往往影响性能)                      |
| --noscripting          | # 禁用脚本引擎                                 |
| --notablescan          | # 不允许表扫描                                 |
| --nounixsocket         | # 禁用Unix套接字监听                            |
| --nssize arg (=16)     | # 设置信数据库.ns文件大小(MB)                      |
| --objcheck             | # 在收到客户数据,检查的有效性，                        |
| --profile arg          | # 档案参数 0=off 1=slow, 2=all               |
| --quota                | # 限制每个数据库的文件数，设置默认为8                     |
| --quotaFiles arg       | # number of files allower per db, requires --quota |
| --rest                 | # 开启简单的rest API                          |
| --repair               | # 修复所有数据库run repair on all dbs           |
| --repairpath arg       | # 修复库生成的文件的目录,默认为目录名称dbpath              |
| --slowms arg (=100)    | # value of slow for profile and console log |
| --smallfiles           | # 使用较小的默认文件                              |
| --syncdelay arg (=60)  | # 数据写入磁盘的时间秒数(0=never,不推荐)               |
| --sysinfo              | # 打印一些诊断系统信息                             |
| --upgrade              | # 如果需要升级数据库                              |

#### * Replicaton 参数

| --fastsync      | # 从一个dbpath里启用从库复制服务，该dbpath的数据库是主库的快照，可用于快速启用同步 |
| --------------- | ---------------------------------------- |
| --autoresync    | # 如果从库与主库同步数据差得多，自动重新同步，                 |
| --oplogSize arg | # 设置oplog的大小(MB)                         |

#### * 主/从参数

| --master         | # 主库模式          |
| ---------------- | --------------- |
| --slave          | # 从库模式          |
| --source arg     | # 从库 端口号        |
| --only arg       | # 指定单一的数据库复制    |
| --slavedelay arg | # 设置从库同步主库的延迟时间 |

#### * Replica set(副本集)选项：

| --replSet arg | # 设置副本集名称 |
| ------------- | --------- |
|               |           |

\* Sharding(分片)选项

| --configsvr      | # 声明这是一个集群的config服务,默认端口27019，默认目录/data/configdb |
| ---------------- | ---------------------------------------- |
| --shardsvr       | # 声明这是一个集群的分片,默认端口27018                  |
| --noMoveParanoia | # 关闭偏执为moveChunk数据保存                     |

#### # 上述参数都可以写入 mongod.conf 配置文档里例如：

dbpath = /data/mongodb

logpath = /data/mongodb/mongodb.log

logappend = true

port = 27017

fork = true

auth = true

e.g：./mongod -shardsvr -replSet shard1 -port 16161 -dbpath /data/mongodb/data/shard1a -oplogSize 100 -logpath /data/mongodb/logs/shard1a.log -logappend -fork -rest

\----------------------------------------------------------------------------------

### MonoDB   shell命令操作语法和JavaScript很类似，其实控制台底层的查询语句都是用JavaScript脚本完成操作的。

Ø 数据库

1、Help查看命令提示

```
help
```

```
db.help();
```

```
db.yourColl.help();
```

```
db.youColl.find().help();
```

```
rs.help();
```

2、切换/创建数据库

```
>use yourDB;
```

```
当创建一个集合(table)的时候会自动创建当前数据库
```

```
3、查询所有数据库
```

```
show dbs;
```

```
4、删除当前使用数据库
```

```
db.dropDatabase();
```

```
5、从指定主机上克隆数据库
```

```
db.cloneDatabase(“127.0.0.1”);
```

```
将指定机器上的数据库的数据克隆到当前数据库
```

```
6、从指定的机器上复制指定数据库数据到某个数据库
```

```
db.copyDatabase("mydb", "temp", "127.0.0.1");
```

```
将本机的mydb的数据复制到temp数据库中
```

```
7、修复当前数据库
```

```
db.repairDatabase();
```

```
8、查看当前使用的数据库
```

```
db.getName();
```

```
db;
```

```
db和getName方法是一样的效果，都可以查询当前使用的数据库
```

```
9、显示当前db状态
```

```
db.stats();
```

```
10、当前db版本
```

```
db.version();
```

```
11、查看当前db的链接机器地址
```

```
db.getMongo();
```

Ø Collection聚集集合

```
1、创建一个聚集集合（table）
```

```
db.createCollection(“collName”, {size: 20, capped: 5, max: 100});
```

```
2、得到指定名称的聚集集合（table）
```

```
db.getCollection("account");
```

```
3、得到当前db的所有聚集集合
```

```
db.getCollectionNames();
```

```
4、显示当前db所有聚集索引的状态
```

```
db.printCollectionStats();
```

Ø 用户相关

```
1、添加一个用户
```

```
db.addUser("name");
```

```
db.addUser("userName", "pwd123", true);
```

```
添加用户、设置密码、是否只读
```

```
2、数据库认证、安全模式
```

```
db.auth("userName", "123123");
```

```
3、显示当前所有用户
```

```
show users;
```

```
4、删除用户
```

```
db.removeUser("userName");
```

Ø 其他

```
1、查询之前的错误信息
```

```
db.getPrevError();
```

```
2、清除错误记录
```

```
db.resetError();
```

###### 三、Collection聚集集合操作

Ø 查看聚集集合基本信息

```
1、查看帮助
```

```
db.yourColl.help();
```

```
2、查询当前集合的数据条数
```

```
db.yourColl.count();
```

```
3、查看数据空间大小
```

```
db.userInfo.dataSize();
```

```
4、得到当前聚集集合所在的db
```

```
db.userInfo.getDB();
```

```
5、得到当前聚集的状态
```

```
db.userInfo.stats();
```

```
6、得到聚集集合总大小
```

```
db.userInfo.totalSize();
```

```
7、聚集集合储存空间大小
```

```
db.userInfo.storageSize();
```

```
8、Shard版本信息
```

```
db.userInfo.getShardVersion()
```

```
9、聚集集合重命名
```

```
db.userInfo.renameCollection("users");
```

```
将userInfo重命名为users
```

```
10、删除当前聚集集合
```

```
db.userInfo.drop();
```

Ø 聚集集合查询

```
1、查询所有记录
```

```
db.userInfo.find();
```

```
相当于：select * from userInfo;
```

```
默认每页显示20条记录，当显示不下的情况下，可以用it迭代命令查询下一页数据。注意：键入it命令不能带“；”
```

```
但是你可以设置每页显示数据的大小，用DBQuery.shellBatchSize = 50;这样每页就显示50条记录了。
```

```
2、查询去掉后的当前聚集集合中的某列的重复数据
```

```
db.userInfo.distinct("name");
```

```
会过滤掉name中的相同数据
```

```
相当于：select distict name from userInfo;
```

```
3、查询age = 22的记录
```

```
db.userInfo.find({"age": 22});
```

```
相当于： select * from userInfo where age = 22;
```

```
4、查询age > 22的记录
```

```
db.userInfo.find({age: {$gt: 22}});
```

```
相当于：select * from userInfo where age > 22;
```

```
5、查询age < 22的记录
```

```
db.userInfo.find({age: {$lt: 22}});
```

```
相当于：select * from userInfo where age < 22;
```

```
6、查询age >= 25的记录
```

```
db.userInfo.find({age: {$gte: 25}});
```

```
相当于：select * from userInfo where age >= 25;
```

```
7、查询age <= 25的记录
```

```
db.userInfo.find({age: {$lte: 25}});
```

```
8、查询age >= 23 并且 age <= 26
```

```
db.userInfo.find({age: {$gte: 23, $lte: 26}});
```

```
9、查询name中包含 mongo的数据
```

```
db.userInfo.find({name: /mongo/});
```

```
//相当于%%
```

```
select * from userInfo where name like ‘%mongo%’;
```

```
10、查询name中以mongo开头的
```

```
db.userInfo.find({name: /^mongo/});
```

```
select * from userInfo where name like ‘mongo%’;
```

```
11、查询指定列name、age数据
```

```
db.userInfo.find({}, {name: 1, age: 1});
```

```
相当于：select name, age from userInfo;
```

```
当然name也可以用true或false,当用ture的情况下河name:1效果一样，如果用false就是排除name，显示name以外的列信息。
```

```
12、查询指定列name、age数据, age > 25
```

```
db.userInfo.find({age: {$gt: 25}}, {name: 1, age: 1});
```

```
相当于：select name, age from userInfo where age > 25;
```

```
13、按照年龄排序
```

```
升序：db.userInfo.find().sort({age: 1});
```

```
降序：db.userInfo.find().sort({age: -1});
```

```
14、查询name = zhangsan, age = 22的数据
```

```
db.userInfo.find({name: 'zhangsan', age: 22});
```

```
相当于：select * from userInfo where name = ‘zhangsan’ and age = ‘22’;
```

```
15、查询前5条数据
```

```
db.userInfo.find().limit(5);
```

```
相当于：select top 5 * from userInfo;
```

```
16、查询10条以后的数据
```

```
db.userInfo.find().skip(10);
```

```
相当于：select * from userInfo where id not in (
```

```
select top 10 * from userInfo
```

```
);
```

```
17、查询在5-10之间的数据
```

```
db.userInfo.find().limit(10).skip(5);
```

```
可用于分页，limit是pageSize，skip是第几页*pageSize
```

```
18、or与 查询
```

```
db.userInfo.find({$or: [{age: 22}, {age: 25}]});
```

```
相当于：select * from userInfo where age = 22 or age = 25;
```

```
19、查询第一条数据
```

```
db.userInfo.findOne();
```

```
相当于：select top 1 * from userInfo;
```

```
db.userInfo.find().limit(1);
```

```
20、查询某个结果集的记录条数
```

```
db.userInfo.find({age: {$gte: 25}}).count();
```

```
相当于：select count(*) from userInfo where age >= 20;
```

```
21、按照某列进行排序
```

```
db.userInfo.find({sex: {$exists: true}}).count();
```

```
相当于：select count(sex) from userInfo;
```

Ø 索引

```
1、创建索引
```

```
db.userInfo.ensureIndex({name: 1});
```

```
db.userInfo.ensureIndex({name: 1, ts: -1});
```

```
2、查询当前聚集集合所有索引
```

```
db.userInfo.getIndexes();
```

```
3、查看总索引记录大小
```

```
db.userInfo.totalIndexSize();
```

```
4、读取当前集合的所有index信息
```

```
db.users.reIndex();
```

```
5、删除指定索引
```

```
db.users.dropIndex("name_1");
```

```
6、删除所有索引索引
```

```
db.users.dropIndexes();
```

Ø 修改、添加、删除集合数据

```
1、添加
```

```
db.users.save({name: ‘zhangsan’, age: 25, sex: true});
```

```
添加的数据的数据列，没有固定，根据添加的数据为准
```

```
2、修改
```

```
db.users.update({age: 25}, {$set: {name: 'changeName'}}, false, true);
```

```
相当于：update users set name = ‘changeName’ where age = 25;
```

```
db.users.update({name: 'Lisi'}, {$inc: {age: 50}}, false, true);
```

```
相当于：update users set age = age + 50 where name = ‘Lisi’;
```

```
db.users.update({name: 'Lisi'}, {$inc: {age: 50}, $set: {name: 'hoho'}}, false, true);
```

```
相当于：update users set age = age + 50, name = ‘hoho’ where name = ‘Lisi’;
```

```
3、删除
```

```
db.users.remove({age: 132});
```

```
4、查询修改删除
```

```
db.users.findAndModify({
```

```
    query: {age: {$gte: 25}}, 
```

```
    sort: {age: -1}, 
```

```
    update: {$set: {name: 'a2'}, $inc: {age: 2}},
```

```
    remove: true
```

```
});
```

```
db.runCommand({ findandmodify : "users", 
```

```
    query: {age: {$gte: 25}}, 
```

```
    sort: {age: -1}, 
```

```
    update: {$set: {name: 'a2'}, $inc: {age: 2}},
```

```
    remove: true
```

```
});
```

*update* 或 *remove* 其中一个是必须的参数; 其他参数可选。

**参数**

**详解**

**默认值**

*query*

查询过滤条件

{}

*sort*

如果多个文档符合查询过滤条件，将以该参数指定的排列方式选择出排在首位的对象，该对象将被操作

{}

*remove*

若为true，被选中对象将在返回前被删除

N/A

*update*

一个 [修改器对象](http://www.mongodb.org/display/DOCS/Updating)

N/A

*new*

若为true，将返回修改后的对象而不是原始对象。在删除操作中，该参数被忽略。

false

*fields*

参见[Retrieving a Subset of Fields](http://www.mongodb.org/display/DOCS/Retrieving+a+Subset+of+Fields) (1.5.0+)

All fields

*upsert*

创建新对象若查询结果为空。 [示例](http://github.com/mongodb/mongo/blob/master/jstests/find_and_modify4.js) (1.5.4+)

false

Ø 语句块操作

```
1、简单Hello World
```

```
print("Hello World!");
```

```
这种写法调用了print函数，和直接写入"Hello World!"的效果是一样的；
```

```
2、将一个对象转换成json
```

```
tojson(new Object());
```

```
tojson(new Object('a'));
```

```
3、循环添加数据
```

```
> for (var i = 0; i < 30; i++) {
```

```
... db.users.save({name: "u_" + i, age: 22 + i, sex: i % 2});
```

```
... };
```

```
这样就循环添加了30条数据，同样也可以省略括号的写法
```

```
> for (var i = 0; i < 30; i++) db.users.save({name: "u_" + i, age: 22 + i, sex: i % 2});
```

```
也是可以的，当你用db.users.find()查询的时候，显示多条数据而无法一页显示的情况下，可以用it查看下一页的信息；
```

```
4、find 游标查询
```

```
>var cursor = db.users.find();
```

```
> while (cursor.hasNext()) { 
```

```
    printjson(cursor.next()); 
```

```
}
```

```
这样就查询所有的users信息，同样可以这样写
```

```
var cursor = db.users.find();
```

```
while (cursor.hasNext()) { printjson(cursor.next); }
```

```
同样可以省略{}号
```

```
5、forEach迭代循环
```

```
db.users.find().forEach(printjson);
```

```
forEach中必须传递一个函数来处理每条迭代的数据信息
```

```
6、将find游标当数组处理
```

```
var cursor = db.users.find();
```

```
cursor[4];
```

```
取得下标索引为4的那条数据
```

```
既然可以当做数组处理，那么就可以获得它的长度：cursor.length();或者cursor.count();
```

```
那样我们也可以用循环显示数据
```

```
for (var i = 0, len = c.length(); i < len; i++) printjson(c[i]);
```

```
7、将find游标转换成数组
```

```
> var arr = db.users.find().toArray();
```

```
> printjson(arr[2]);
```

```
用toArray方法将其转换为数组
```

```
8、定制我们自己的查询结果
```

```
只显示age <= 28的并且只显示age这列数据
```

```
db.users.find({age: {$lte: 28}}, {age: 1}).forEach(printjson);
```

```
db.users.find({age: {$lte: 28}}, {age: true}).forEach(printjson);
```

```
排除age的列
```

```
db.users.find({age: {$lte: 28}}, {age: false}).forEach(printjson);
```

```
9、forEach传递函数显示信息
db.things.find({x:4}).forEach(function(x) {print(tojson(x));});
上面介绍过forEach需要传递一个函数，函数会接受一个参数，就是当前循环的对象，然后在函数体
```