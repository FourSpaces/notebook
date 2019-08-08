## Hive 数据参仓库迁移计划



创建表结构

- 测试表选取

  ```
  # 无分区表
  hdfs dfs -du -h /hive/warehouse/mid.db/callback
  
  hdfs dfs -du -h /hive/warehouse/mid.db/zlg03041
  
  # 包含分区表
  hdfs dfs -du -h /hive/warehouse/dw.db/base_data_onlyid
  ```

  

- 获取表结构

  ```
  hive -e "use dw;show create table base_data_onlyid" >base_data_onlyid.txt
  
  CREATE TABLE `base_data_onlyid`(
    `kind` string,
    `appversionname` string,
    `channelid` string,
    `devicebrand` string,
    `systemversion` string,
    `islocklocation` string,
    `imei` string)
  PARTITIONED BY (
    `ymd` string)
  ROW FORMAT SERDE
    'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
  STORED AS INPUTFORMAT
    'org.apache.hadoop.mapred.TextInputFormat'
  OUTPUTFORMAT
    'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
  LOCATION
    'hdfs://myha01:8020/hive/warehouse/dw.db/base_data_onlyid'
  TBLPROPERTIES (
    'last_modified_by'='root',
    'last_modified_time'='1544173403',
    'transient_lastDdlTime'='1544173403')
    
    
    
    hive -e "use mid;show create table callback" >callback.txt
    
    CREATE TABLE `callback`(
    `ymd` string,
    `ipaddr` string,
    `name` string,
    `timestamp` string)
  ```

- 

复制数据到新的数据仓库

- 含有分区表的情况
- 不包含分区表的情况

把表给同步回去

```
hdfs dfs -mv /hive/warehouse/event_rday/* /新路径

# 分区修复命令进行修复
msck repair table dw.base_data_onlyid;
```





#### Disco 数据

```
hadoop distcp -Ddistcp.bytes.per.map=1073741824 -Dmapreduce.job.queuename=hive -Dmapreduce.job.name=cpdata /hive/warehouse/dw.db/base_data_onlyid  hdfs://hadoop35.bigdata.org/hive/warehouse/dw.db/base_data_onlyid


hadoop distcp -Ddistcp.bytes.per.map=1073741824 -Dmapreduce.job.queuename=hive -Dmapreduce.job.name=cpdata /hive/warehouse/mid.db/callback  hdfs://hadoop35.bigdata.org/hive/warehouse/mid.db/callback

```



```
python distcp_table.py --table_path=/hive/warehouse/bi.db/active_natural_week --aims_hostname=hadoop35.bigdata.org --is_partition=n

```



