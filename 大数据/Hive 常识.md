# Hive 常识



流程：

- 建表
- 载入数据





仓库目录：hive.metastore.warehouse.dir: 默认为：/usr/hive/warehouse/records

fs.default.name : 设置hive仓库的存储位置，

Hive --config /users/tom/dev/hive-conf 

可以设置HIVE_CONF_DIR 环境变量来指定配置文件目录



hive 优化配置

不同的执行时长使用不同的资源

- 超过1小时的使用中资源
- 超过3小时的使用大资源
- 超过7小时的使用超资源



常见语句：

```
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
```

托管表：hive将数据存在自己的仓库目录下

外部表：让hive 到数据仓库目录以外的位置访问数据

```plsql
-- 加载数据到托管表
CREATE TABLE managed_table(dummy STRING);
LOAD DATA INPATH '/udr'
```



导出数据

```
insert overwrite local directory '/home/carter/staging' row format delimited fields terminated by ',' select imei from userdb.user_package_list where ymd >= 20181005 group by imei;
```

虚表

```
select lx,count(*) from movie_message lateral view explode(leixing) leixing as lx group by lx;
```

解析json数组

```
explode(split(regexp_replace(regexp_replace('[{"website":"www.iteblog.com","name":"过往记忆"},{"website":"carbondata.iteblog.com","name":"carbondata 中文文档"}]', '\\}\\,\\{', '\\}\\;\\{'),'\\[|\\]',''),'\\;'))

explode(split(regexp_replace(regexp_replace('变量', '\\}\\,\\{', '\\}\\;\\{'),'\\[|\\]',''),'\\;'))
```

