# Spark 运行

```
# 检查ssh服务开启状态
ps -s | grep ssh
# 先开启ssh 服务
service ssh start
/etc/init.d/ssh start

# 启动hadoop HDFS文件系统
start-dfs.sh
# 启动spark
cd /usr/local/spark-2.3.0
./sbin/start-all.sh
```

