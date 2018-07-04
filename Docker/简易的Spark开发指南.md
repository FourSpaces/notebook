简易的Spark开发指南

Last modified [Mar 05, 2018](https://zaoshu.atlassian.net/wiki/pages/diffpagesbyversion.action?pageId=183959588&selectedPageVersions=6&selectedPageVersions=7)

特别备注

- spark-mongodb-connector建议使用2.1.1版本，之前在2.1.0上有默认分区导致的计算问题的bug，详细情况可以查阅mongodb的Jira

- - <https://jira.mongodb.org/browse/SPARK-151> 
  - --packages org.mongodb.spark:mongo-spark-connector_2.11:2.1.1

环境

- 开发环境为macOS High Sierra，运行环境为Ubuntu 16.04
- docker 17.09.1-ce
- docker-compose version 1.15.0, build e12f3b9
-  spark：

- - master：bde2020/spark-master:2.1.0-hadoop2.8-hive-java8
  - worker：bde2020/spark-worker:2.1.0-hadoop2.8-hive-java8

- MongoDB：

- - aashreys/mongo-auth:latest

- - - MongoDB shell version v3.4.5
    - image hash: d574225230be

Mac搭建开发环境步骤

搭建spark和MongoDB

- 参考用的docker-compose.yml，这里是完全本地使用的版本，比如说spark-master这个特有的名字，这里的spark-master出现过的地方都要完全一致，否则worker都会拒绝工作。。。。。

线上环境的执行方案是全部使用ip地址，方便使用容器工具提交任务，而不是进入容器内部提交任务。。。

安装JDK

- mac上就用oracle jdk 1.8好了，OpenJDK好像不好装
- 去oracle jdk网站下载，安装，结束，没啥要配置的
- 不准用jdk1.9，spark2.1不支持

安装SBT

- 目前是1.0.4
- 不建议使用IntelliJ IDEA的sbt，那样就只能在idea的sbt-shell执行sbt命令，然而sbt-shell似乎有点问题
- 如果提示要装xcode-shell，gcc啥的，都装上
- 配置国内aliyun加速源：

- - 在home目录下的.sbt目录下修改repositories文件，没有就新建一个，.sbt目录没有也新建

安装IntelliJ IDEA

- 装scala语言插件，重启idea

![image?mode=full-fit&client=3b6e509c-c992-4734-b6ce-6e79a035ddda&token=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIzYjZlNTA5Yy1jOTkyLTQ3MzQtYjZjZS02ZTc5YTAzNWRkZGEiLCJhY2Nlc3MiOnsidXJuOmZpbGVzdG9yZTpmaWxlOmViZDBjM2JhLTkyYmEtNDYzZS1iYTEwLTcxNjFiZTdiMjMyYyI6WyJyZWFkIl19LCJleHAiOjE1MjcxNDE4NDQsIm5iZiI6MTUyNzEzODQ4NH0.Hd25KAcv2yuOsgXj7Cfk2Irutd5hX32HIO1fkxCWCok](http://note.youdao.com/yws/res/4264/37E64E50E57A42529A6A29AFF5735A62)

创建Spark项目

- New Project-----Scala------sbt
- scala选2.11.12，或者2.11.x都行，spark不支持2.12.x
- sbt会自动扫描出来，按上面的装就是1.0.4了

![image?mode=full-fit&client=3b6e509c-c992-4734-b6ce-6e79a035ddda&token=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIzYjZlNTA5Yy1jOTkyLTQ3MzQtYjZjZS02ZTc5YTAzNWRkZGEiLCJhY2Nlc3MiOnsidXJuOmZpbGVzdG9yZTpmaWxlOjUxNWZkNGQyLTkzMTAtNDc2YS05ZGZhLWI5ZDdkMjRlOGFhNSI6WyJyZWFkIl19LCJleHAiOjE1MjcxNDE4NDQsIm5iZiI6MTUyNzEzODQ4NH0.tmd1YWRQqxqlrbIynEMHoV3w_PoKf4jw4a9zEl1ss-8](http://note.youdao.com/yws/res/4266/495345376FAC42BC8F876145D7BA7367)

配置sbt依赖

- 大概长这样，name和version随便来，剩下的严格和环境一致。右上角弹出的提示中点击Enable Auto-Import

新建scala object

![image?mode=full-fit&client=3b6e509c-c992-4734-b6ce-6e79a035ddda&token=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIzYjZlNTA5Yy1jOTkyLTQ3MzQtYjZjZS02ZTc5YTAzNWRkZGEiLCJhY2Nlc3MiOnsidXJuOmZpbGVzdG9yZTpmaWxlOmZlY2QyZmM2LTgyMmUtNDIyMC1hOTkxLTY2YjYyNGNlYzVlZiI6WyJyZWFkIl19LCJleHAiOjE1MjcxNDE4NDQsIm5iZiI6MTUyNzEzODQ4NH0.U2n7ZIvlQNPB3lD8JrYSRaweSYHZVL7Iw0Ij4vk94-k](http://note.youdao.com/yws/res/4269/B0C3E0F641B441A3AE7B11C7E832D0C4)

- 这里新建一个object，起个名字
- 然后样例代码如下：
- spark的连接地址和上面的docker-compose.yml有关，mongodb的连接地址也和上面的docker-compose.yml有关

编译、本地试验

- idea的terminal里面，输入sbt，输入package，然后就打包好了，一般4~5kb大的一个jar包

- - 不建议使用intellij的sbt-shell窗口，感觉贼慢贼蠢。。。

- 拷贝jar，改成自己项目的地址

- - docker cp /Users/iris/IdeaProjects/spark-mongo-1/target/scala-2.11/spark-mongo-1_2.11-0.1.jar [spark-master:/tmp/](http://spark-master/tmp/)

- 进入spark-master容器执行jar

- -  docker exec -it spark-master /bin/bash
  - cd /spark/bin
  - ./spark-submit --packages org.mongodb.spark:mongo-spark-connector_2.11:2.1.1  /tmp/spark-mongo-1_2.11-0.1.jar

- <http://localhost:8080/>   这个是spark-master的web ui，能看到些神奇的东西，不过好像也没啥用

CircleCI构建

- 调整过circleci配置文件后可以试试这一步，平常就没必要了
- spikerlabs/scala-sbt:scala-2.11.12-sbt-1.0.4

- - 如果用的scala和sbt版本不同，参考：<https://hub.docker.com/r/spikerlabs/scala-sbt/>

- 在项目下创建circleci配置

- - 最简单的版本，目前circleci本地不支持cache，emmmm.......下载依赖可能会比较慢

- 验证配置：circleci config validate
- 本地执行构建：circleci build
- 参考资料：<https://circleci.com/docs/2.0/local-jobs/>

参考项目

- <https://github.com/zaoshu/spark-example>

<https://zaoshu.atlassian.net/secure/Dashboard.jspa>