# [spark系统实现yarn资源的自动调度](https://www.cnblogs.com/charlesblc/p/7075134.html)



参考：

<http://blog.csdn.net/dandykang/article/details/48160953>

 

​    对于Spark应用来说，资源是影响Spark应用执行效率的一个重要因素。当一个长期运行 的服务（比如Thrift Server），若分配给它多个Executor，可是却没有任何任务分配给它，而此时有其他的应用却资源张，这就造成了很大的资源浪费和资源不合理的调度。 

​    动态资源调度就是为了解决这种场景，根据当前应用任务的负载情况，实时的增减 Executor个数，从而实现动态分配资源，使整个Spark系统更加健康。

 

配置步骤：

 

​    \1. 需要先配置External shuffle service。参见**spark on yarn（External shuffle service）**配置

​    \2. 在“spark-defaults.conf”中必须添加配置项“spark.dynamicAllocation.enabled”，并将该参数的值设置为“true”，表示开启动态资源调度功能。默认情况下关闭此功能。

​    \3. 根据情况配置一些可选参数

 

以下是基本配置参考

> spark.shuffle.service.enabled                true   配置External shuffle Service服务（一定要配置启用）
>
> spark.shuffle.service.port                       7337
>
> spark.dynamicAllocation.enabled         true   启用动态资源调度
>
> spark.dynamicAllocation.minExecutors    3    每个应用中最少executor的个数
>
> spark.dynamicAllocation.maxExecutors    8    每个应用中最多executor的个数
>
>  
>
>  

可选参数说明：

 

配置项                                                                                    说明                                                                默认值

spark.dynamicAllocation.minExecutors                             最小Executor个数。                                        0 

spark.dynamicAllocation.initialExecutors                          初始Executor个数。                                        spark.dynamicAllocation.minExecutors

spark.dynamicAllocation.maxExecutors                             最大executor个数。                                        Integer.MAX_VALUE

spark.dynamicAllocation.schedulerBacklogTimeout         调度第一次超时时间。                                 1(s)

spark.dynamicAllocation.sustainedSchedulerBacklogTimeout 调度第二次及之后超时时间。      spark.dynamicAllocation.schedulerBacklogTimeout

spark.dynamicAllocation.executorIdleTimeout                  普通Executor空闲超时时间。                          60(s)

spark.dynamicAllocation.cachedExecutorIdleTimeout      含有cached blocks的Executor空闲超时时间。spark.dynamicAllocation.executorIdleTimeout的2倍

 

说明

\1. 使用动态资源调度功能，必须配置External Shuffle Service。如果没有使用External Shuffle Service，Executor被杀时会丢失shuffle文件。 

\2. 配置了动态资源调度功能，就不能再单独配置Executor的个数，否则会报错退出。

\3. 使用动态资源调度功能，能保证最少的executor的个数（spark.dynamicAllocation.minExecutors）