

# HIVE数据迁移



### 使用Hive提供的export/import进行数据的迁移

### **备份前需要关注的信息查询**

目的是查看需要备份数据的大概大小，保证在导入和导出时有足够的空间。便于指定迁移计划和步骤（空间不够时可能某些步骤需要拆分，分批次执行）

```
# 1 查看HDFS集群使用情况
hadoop dfsadmin -report

2 查看本地空间使用情况
df -lh

3 查找Hive在HDFS上仓库的位置
hadoop fs -find / -name warehouse

4 查看Hive仓库中各个库占用的大小
hadoop fs -du -h /hive/warehouse

4 查看Hive中的库和表

# 查询Hive库有，
show databases;
 
# 使用某个库
use 库名
 
# 查询某个库下的表，便于后期查看导出的数据表文件个数和表的个数是否能对应上
show tables;
 
 
# 如果这条命令报权限问题，那么需要先解决权限认证的问题，可查看下面的第三点解决
SELECT * FROM 表名 LIMIT 条数;

```



导出数据

```
# 创建保存目录
hadoop fs -mkdir /tmp/userdb

# 生成保存脚本
hive -e "show tables " | awk '{printf "export table %s to |/tmp/userdb/%s|;\n",$1,$1}' | sed "s/|/'/g" > ~/export.hql

# 执行脚本
# 导出数据到HDFS
hive -f ~/export.hql

```

```

hive -e "use mid; show tables " | awk '{printf "export table %s to |/tmp/mid/%s|;\n",$1,$1}' | sed "s/|/'/g" > ~/export.mid.hql


export table crash_rday to 'hdfs://172.16.16.13:8020/tmp/mid/crash_rday';


hive -e "use mid; show tables " | awk '{printf "export table mid.%s to |hdfs://172.16.16.13:8020/tmp/mid/%s|;\n",$1,$1}' | sed "s/|/'/g" > ~/export.mid.hql



cp export.mid.hql import.mid.hql
sed -i 's/export table/import table/g' import.mid.hql
sed -i 's/ to / from /g' import.mid.hql
```

导出数据库结构的脚本

```
#!/bin/bash
rm -rf databases.txt
hive -e " show databases; exit ;" > databases
#sleep(2)
rm -rf ./tables
rm -rf ./desc_table
mkdir -p ./tables
mkdir -p ./desc_table
for database in `cat databases`
do
  {
  # 获取数据库信息
  hive -e " use $database ;  show tables ; exit ;" > ./tables/$database
  for table in `cat ./tables/$database`
  do
     hive -e "use $database ; show create table $table ;" > ./desc_table/$database
  done
  }&
done
wait

```

导入数据库结构到hive 中

```

```

