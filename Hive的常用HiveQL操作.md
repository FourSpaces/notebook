## Hive的常用HiveQL操作

1）Hive基本数据类型

首先，我们简单叙述一下HiveQL的基本数据类型。

Hive支持基本数据类型和复杂类型, 基本数据类型主要有数值类型(INT、FLOAT、DOUBLE ) 、布尔型和字符串, 复杂类型有三种:ARRAY、MAP 和 STRUCT。

a.基本数据类型

- TINYINT: 1个字节
- SMALLINT: 2个字节
- INT: 4个字节
- BIGINT: 8个字节
- BOOLEAN: TRUE/FALSE
- FLOAT: 4个字节，单精度浮点型
- DOUBLE: 8个字节，双精度浮点型STRING 字符串

b.复杂数据类型

- ARRAY: 有序字段
- MAP: 无序字段
- STRUCT: 一组命名的字段

2）常用的HiveQL操作命令

Hive常用的HiveQL操作命令主要包括：数据定义、数据操作。接下来详细介绍一下这些命令即用法（想要了解更多请参照《Hive编程指南》一书）。

a.数据定义：主要用于创建修改和删除数据库、表、视图、函数和索引。

**创建、修改和删除数据库**

```sql
create database if not exists hive;       #创建数据库show databases;                           #查看Hive中包含数据库show databases like 'h.*';                #查看Hive中以h开头数据库describe databases;                       #查看hive数据库位置等信息alter database hive set dbproperties;     #为hive设置键值对属性use hive;                                 #切换到hive数据库下drop database if exists hive;             #删除不含表的数据库drop database if exists hive cascade;     #删除数据库和它中的表
```

sql

注意，除 dbproperties属性外，数据库的元数据信息都是不可更改的，包括数据库名和数据库所在的目录位置，没有办法删除或重置数据库属性。

**创建、修改和删除表**

```sql
#创建内部表（管理表）create table if not exists hive.usr(      name string comment 'username',      pwd string comment 'password',      address struct<street:string,city:string,state:string,zip:int>,      comment  'home address',      identify map<int,tinyint> comment 'number,sex')       comment 'description of the table'       tblproperties('creator'='me','time'='2016.1.1'); #创建外部表create external table if not exists usr2(      name string,      pwd string,  address struct<street:string,city:string,state:string,zip:int>,      identify map<int,tinyint>)       row format delimited fields terminated by ','     location '/usr/local/hive/warehouse/hive.db/usr'; #创建分区表create table if not exists usr3(      name string,      pwd string,      address struct<street:string,city:string,state:string,zip:int>,      identify map<int,tinyint>)       partitioned by(city string,state string);    #复制usr表的表模式  create table if not exists hive.usr1 like hive.usr; show tables in hive;  show tables 'u.*';        #查看hive中以u开头的表describe hive.usr;        #查看usr表相关信息alter table usr rename to custom;      #重命名表 #为表增加一个分区alter table usr2 add if not exists      partition(city=”beijing”,state=”China”)      location '/usr/local/hive/warehouse/usr2/China/beijing'; #修改分区路径alter table usr2 partition(city=”beijing”,state=”China”)     set location '/usr/local/hive/warehouse/usr2/CH/beijing';#删除分区alter table usr2 drop if exists  partition(city=”beijing”,state=”China”)#修改列信息alter table usr change column pwd password string after address; alter table usr add columns(hobby string);                  #增加列alter table usr replace columns(uname string);              #删除替换列alter table usr set tblproperties('creator'='liming');      #修改表属性alter table usr2 partition(city=”beijing”,state=”China”)    #修改存储属性set fileformat sequencefile;             use hive;                                                   #切换到hive数据库下drop table if exists usr1;                                  #删除表drop database if exists hive cascade;                       #删除数据库和它中的表
```

sql

**视图和索引的创建、修改和删除**

主要语法如下，用户可自行实现。

```sql
create view view_name as....;                #创建视图alter view view_name set tblproperties(…);   #修改视图
```

sql

因为视图是只读的，所以 对于视图只允许改变元数据中的 tblproperties属性。

```sql
#删除视图drop view if exists view_name;#创建索引create index index_name on table table_name(partition_name/column_name)  as 'org.apache.hadoop.hive.ql.index.compact.CompactIndexHandler' with deferred rebuild....; 
```

sql

这里’org.apache.hadoop.hive.ql.index.compact.CompactIndexHandler’是一个索引处理器，即一个实现了索引接口的Java类，另外Hive还有其他的索引实现。

```sql
alter index index_name on table table_name partition(...)  rebulid;   #重建索引
```

sql

如果使用 deferred rebuild，那么新索引成空白状态，任何时候可以进行第一次索引创建或重建。

```sql
show formatted index on table_name;                       #显示索引drop index if exists index_name on table table_name;      #删除索引
```

sql

**用户自定义函数**

在新建用户自定义函数（UDF）方法前，先了解一下Hive自带的那些函数。`show functions;` 命令会显示Hive中所有的函数名称：

![img](http://dblab.xmu.edu.cn/blog/wp-content/uploads/2016/01/5.png)

若想要查看具体函数使用方法可使用describe function 函数名：

![img](http://dblab.xmu.edu.cn/blog/wp-content/uploads/2016/01/6.png)

首先编写自己的UDF前需要继承UDF类并实现evaluate()函数，或是继承GenericUDF类实现initialize()函数、evaluate()函数和getDisplayString()函数，还有其他的实现方法，感兴趣的用户可以自行学习。

另外，如果用户想在Hive中使用该UDF需要将我们编写的Java代码进行编译，然后将编译后的UDF二进制类文件(.class文件)打包成一个JAR文件，然后在Hive会话中将这个JAR文件加入到类路径下，在通过create function语句定义好使用这个Java类的函数。

```sql
add jar <jar文件的绝对路径>;                        #创建函数create temporary function function_name;drop temporary function if exists function_name;    #删除函数
```

sql

3）数据操作

主要实现的是将数据装载到表中（或是从表中导出），并进行相应查询操作，对熟悉SQL语言的用户应该不会陌生。

**向表中装载数据**

这里我们以只有两个属性的简单表为例来介绍。首先创建表stu和course，stu有两个属性id与name，course有两个属性cid与sid。

```sql
create table if not exists hive.stu(id int,name string) row format delimited fields terminated by '\t';create table if not exists hive.course(cid int,sid int) row format delimited fields terminated by '\t';
```

sql

向表中装载数据有两种方法：从文件中导入和通过查询语句插入。

a.从文件中导入

假如这个表中的记录存储于文件stu.txt中，该文件的存储路径为/usr/local/hadoop/examples/stu.txt，内容如下。

stu.txt：

```
1 xiapi 
2 xiaoxue 
3 qingqing
```

下面我们把这个文件中的数据装载到表stu中，操作如下：

```sql
load data local inpath '/usr/local/hadoop/examples/stu.txt' overwrite into table stu;
```

sql

如果stu.txt文件存储在HDFS 上，则不需要 local 关键字。

b.通过查询语句插入

使用如下命令，创建stu1表，它和stu表属性相同，我们要把从stu表中查询得到的数据插入到stu1中：

```sql
create table stu1 as select id,name from stu;
```

sql

上面是创建表，并直接向新表插入数据；若表已经存在，向表中插入数据需执行以下命令：

```sql
insert overwrite table stu1 select id,name from stu where（条件）;
```

sql

这里关键字overwrite的作用是替换掉表（或分区）中原有数据，换成into关键字，直接追加到原有内容后。

**从表中导出数据**

a.可以简单拷贝文件或文件夹

命令如下：

```shell
hadoop  fs -cp source_path target_path;
```

Shell

b.写入临时文件

命令如下：

```sql
insert overwrite local directory '/usr/local/hadoop/tmp/stu'  select id,name from stu;
```

sql

**查询操作**

和SQL的查询完全一样，这里不再赘述。主要使用select…from…where…等语句，再结合关键字group by、having、like、rlike等操作。这里我们简单介绍一下SQL中没有的case…when…then…句式、join操作和子查询操作。

case…when…then…句式和if条件语句类似，用于处理单个列的查询结果，语句如下：

```sql
select id,name,  case   when id=1 then 'first'   when id=2 then 'second'  else 'third'
```

sql

结果如下：

![img](http://dblab.xmu.edu.cn/blog/wp-content/uploads/2016/01/7.png)

**连接**
连接（join）是将两个表中在共同数据项上相互匹配的那些行合并起来, HiveQL 的连接分为内连接、左向外连接、右向外连接、全外连接和半连接 5 种。

a. 内连接(等值连接)
内连接使用比较运算符根据每个表共有的列的值匹配两个表中的行。

首先，我们先把以下内容插入到course表中（自行完成）。

```
1 3
2 1
3 1
```

下面, 查询stu和course表中学号相同的所有行，命令如下：

```sql
select stu.*, course.* from stu join course on(stu .id=course .sid);
```

sql

执行结果如下：

![img](http://dblab.xmu.edu.cn/blog/wp-content/uploads/2016/01/9.png)

b. 左连接
左连接的结果集包括“LEFT OUTER”子句中指定的左表的所有行, 而不仅仅是连接列所匹配的行。如果左表的某行在右表中没有匹配行, 则在相关联的结果集中右表的所有选择列均为空值，命令如下：

```sql
select stu.*, course.* from stu left outer join course on(stu .id=course .sid); 
```

sql

执行结果如下：

![img](http://dblab.xmu.edu.cn/blog/wp-content/uploads/2016/01/10.png)

c. 右连接
右连接是左向外连接的反向连接,将返回右表的所有行。如果右表的某行在左表中没有匹配行,则将为左表返回空值。命令如下：

```sql
select stu.*, course.* from stu right outer join course on(stu .id=course .sid); 
```

sql

执行结果如下：

![img](http://dblab.xmu.edu.cn/blog/wp-content/uploads/2016/01/11.png)

d. 全连接
全连接返回左表和右表中的所有行。当某行在另一表中没有匹配行时,则另一个表的选择列表包含空值。如果表之间有匹配行,则整个结果集包含基表的数据值。命令如下：

```sql
select stu.*, course.* from stu full outer join course on(stu .id=course .sid); 
```

sql

执行结果如下：

![img](http://dblab.xmu.edu.cn/blog/wp-content/uploads/2016/01/12.png)

e. 半连接
半连接是 Hive 所特有的, Hive 不支持 in 操作,但是拥有替代的方案; left semi join, 称为半连接, 需要注意的是连接的表不能在查询的列中,只能出现在 on 子句中。命令如下：

```sql
select stu.* from stu left semi join course on(stu .id=course .sid); 
```

sql

执行结果如下：

![img](http://dblab.xmu.edu.cn/blog/wp-content/uploads/2016/01/13.png)

**子查询**
标准 SQL 的子查询支持嵌套的 select 子句,HiveQL 对子查询的支持很有限,只能在from 引导的子句中出现子查询。

**注意，在定义或是操作表时，不要忘记指定所需数据库。**