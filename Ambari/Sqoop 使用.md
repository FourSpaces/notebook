# Sqoop 使用


sqoop 的help
```
usage: sqoop COMMAND [ARGS]

Available commands:
  codegen            生成与数据库记录交互的代码
  create-hive-table  将表定义导入Hive
  eval               执行SQL语句并显示结果
  export             将HDFS目录导出到数据库表
  help               列出可用命令
  import             将表从数据库导入到HDFS
  import-all-tables  将表从数据库导入到HDFS
  import-mainframe   将数据集从大型机服务器导入到HDFS
  job                使用保存的作业
  list-databases     列出服务器上的可用数据库
  list-tables        列出数据库中的可用表
  merge              合并增量导入的结果
  metastore          运行独立的sqoop元存储
  version            显示版本信息
```

## 例子：
### 导入数据
- Mysql  To HDFS
```
## 全部倒入
sqoop import \
-connect jdbc:mysql://172.16.16.21:3306/appdata \
--username appdata \
--password KVdawj08kna- \
--table app_yyb \
--target-dir /user/app_yyb \
--fields-terminated-by "\t" \
--m 1

## 查询控制导入


```

- 使用sqoop将：mysql中的数据导入到HIVE中
```
sqoop import \
-connect jdbc:mysql://172.16.16.21:3306/appdata \
--username appdata \
--password KVdawj08kna- \
--table app_yyb \
--fields-terminated-by "\t" \
--hive-table userdb.app_yyb \
--hive-import \
--m 1


sqoop create-hive-table \
-connect jdbc:mysql://172.16.16.21:3306/appdata \
--username appdata \
--password KVdawj08kna- \
--table app_yyb \
--hive-table userdb.app_yyb
```