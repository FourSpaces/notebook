### sbt  打包指南



将依赖一起打入 jar 包

```
sbt clean compile assembly
```



不打包依赖

```
sbt package
```





### Man 打包

将依赖一起打入 jar 包

```

```



不打包依赖

```
mvn clean package -DskipTests
```

Mavn 错误信息

------------

[**ERROR**] Failed to execute goal org.apache.maven.plugins:maven-assembly-plugin:2.2-beta-5:assembly **(default-cli)** on project nsq_streamsets: **Error reading assemblies: No assembly descriptors found.** -> **[Help 1]**

<https://blog.csdn.net/znsqingfeng/article/details/51302033>

```
只需把描述文件配置中的configuration移到plugin下即可:
```

