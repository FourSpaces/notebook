# Azkaban 重启

```
cd /usr/local/webserver/azkaban-3.60/azkaban-exec-server/
./bin/shutdown-exec.sh
rm -rf *.out
./bin/start-exec.sh 
jps
exit
```





 删除组件连接

```
rm -rf  /bin/avro-tools 
rm -rf  /bin/beeline 
rm -rf  /bin/bigtop-detect-javahome 
rm -rf  /bin/catalogd 
rm -rf  /bin/cli_mt 
rm -rf  /bin/cli_st 
rm -rf  /bin/flume-ng 
rm -rf  /bin/hadoop 
rm -rf  /bin/hadoop-0.20 
rm -rf  /bin/hadoop-fuse-dfs 
rm -rf  /bin/hbase 
rm -rf  /bin/hbase-indexer 
rm -rf  /bin/hbase-indexer-sentry 
rm -rf  /bin/hcat 
rm -rf  /bin/hdfs
rm -rf  /bin/hive
rm -rf  /bin/hiveserver2
rm -rf  /bin/impalad 
rm -rf  /bin/impala-shell 
rm -rf  /bin/kite-dataset 
rm -rf  /bin/kudu 
rm -rf  /bin/llama 
rm -rf  /bin/llamaadmin 
rm -rf  /bin/load_gen 
rm -rf  /bin/mahout 
rm -rf  /bin/mapred 
rm -rf  /bin/oozie 
rm -rf  /bin/parquet-tools 
rm -rf  /bin/pig 
rm -rf  /bin/sentry 
rm -rf  /bin/solrctl 
rm -rf  /bin/sqoop 
rm -rf  /bin/sqoop2 
rm -rf  /bin/sqoop-codegen 
rm -rf  /bin/sqoop-create-hive-table 
rm -rf  /bin/sqoop-eval 
rm -rf  /bin/sqoop-export 
rm -rf  /bin/sqoop-help 
rm -rf  /bin/sqoop-import 
rm -rf  /bin/sqoop-import-all-tables 
rm -rf  /bin/sqoop-job 
rm -rf  /bin/sqoop-list-databases 
rm -rf  /bin/sqoop-list-tables 
rm -rf  /bin/sqoop-merge 
rm -rf  /bin/sqoop-metastore 
rm -rf  /bin/sqoop-version 
rm -rf  /bin/statestored 
rm -rf  /bin/spark*
rm -rf  /bin/whirr 
rm -rf  /bin/yarn 
rm -rf  /bin/zookeeper-client 
rm -rf  /bin/zookeeper-server 
rm -rf  /bin/zookeeper-server-cleanup 
rm -rf  /bin/impala-collect-minidumps 
rm -rf  /bin/spark-executor
rm -rf  /bin/pyspark
rm -rf  /bin/spark-shell
rm -rf  /bin/spark-submit
ll | grep alternatives
source ~/.bash_profile
exit
```





添加组件连接

```
cd /bin
ln -s /etc/alternatives/avro-tools
ln -s /etc/alternatives/beeline
ln -s /etc/alternatives/bigtop-detect-javahome
ln -s /etc/alternatives/catalogd
ln -s /etc/alternatives/cli_mt
ln -s /etc/alternatives/cli_st
ln -s /etc/alternatives/flume-ng
ln -s /etc/alternatives/hadoop
ln -s /etc/alternatives/hadoop-0.20
ln -s /etc/alternatives/hadoop-fuse-dfs
ln -s /etc/alternatives/hbase
ln -s /etc/alternatives/hbase-indexer
ln -s /etc/alternatives/hbase-indexer-sentry
ln -s /etc/alternatives/hcat
ln -s /etc/alternatives/hdfs
ln -s /etc/alternatives/hive
ln -s /etc/alternatives/hiveserver2
ln -s /etc/alternatives/impalad
ln -s /etc/alternatives/impala-shell
ln -s /etc/alternatives/kafka-acls
ln -s /etc/alternatives/kafka-broker-api-versions
ln -s /etc/alternatives/kafka-configs
ln -s /etc/alternatives/kafka-console-consumer
ln -s /etc/alternatives/kafka-console-producer
ln -s /etc/alternatives/kafka-consumer-groups
ln -s /etc/alternatives/kafka-consumer-perf-test
ln -s /etc/alternatives/kafka-delete-records
ln -s /etc/alternatives/kafka-log-dirs
ln -s /etc/alternatives/kafka-mirror-maker
ln -s /etc/alternatives/kafka-preferred-replica-election
ln -s /etc/alternatives/kafka-reassign-partitions
ln -s /etc/alternatives/kafka-replica-verification
ln -s /etc/alternatives/kafka-run-class
ln -s /etc/alternatives/kafka-sentry
ln -s /etc/alternatives/kafka-topics
ln -s /etc/alternatives/kafka-verifiable-consumer
ln -s /etc/alternatives/kafka-verifiable-producer
ln -s /etc/alternatives/kite-dataset
ln -s /etc/alternatives/kudu
ln -s /etc/alternatives/kudu-master
ln -s /etc/alternatives/kudu-tserver
ln -s /etc/alternatives/ld
ln -s /etc/alternatives/load_gen
ln -s /etc/alternatives/print-lp
ln -s /etc/alternatives/print-lpq
ln -s /etc/alternatives/print
ln -s /etc/alternatives/print-lprm
ln -s /etc/alternatives/print-lpstat
ln -s /etc/alternatives/mta-mailq
ln -s /etc/alternatives/mapred
ln -s /etc/alternatives/mta-newaliases
ln -s /etc/alternatives/oozie
ln -s /etc/alternatives/parquet-tools
ln -s /etc/alternatives/pax
ln -s /etc/alternatives/pig
ln -s /etc/alternatives/pyspark
ln -s /etc/alternatives/mta-rmail
ln -s /etc/alternatives/sentry
ln -s /etc/alternatives/solrctl
ln -s /etc/alternatives/spark-executor
ln -s /etc/alternatives/spark-shell
ln -s /etc/alternatives/spark-sql
ln -s /etc/alternatives/spark-submit
ln -s /etc/alternatives/sqoop
ln -s /etc/alternatives/sqoop-codegen
ln -s /etc/alternatives/sqoop-create-hive-table
ln -s /etc/alternatives/sqoop-eval
ln -s /etc/alternatives/sqoop-export
ln -s /etc/alternatives/sqoop-help
ln -s /etc/alternatives/sqoop-import
ln -s /etc/alternatives/sqoop-import-all-tables
ln -s /etc/alternatives/sqoop-job
ln -s /etc/alternatives/sqoop-list-databases
ln -s /etc/alternatives/sqoop-list-tables
ln -s /etc/alternatives/sqoop-merge
ln -s /etc/alternatives/sqoop-metastore
ln -s /etc/alternatives/sqoop-version
ln -s /etc/alternatives/statestored
ln -s /etc/alternatives/yarn
ln -s /etc/alternatives/zookeeper-client
ln -s /etc/alternatives/zookeeper-server
ln -s /etc/alternatives/zookeeper-server-cleanup
ln -s /etc/alternatives/zookeeper-server-initialize
exit
```





```
hdfs -> /etc/alternatives/hdfs
```

