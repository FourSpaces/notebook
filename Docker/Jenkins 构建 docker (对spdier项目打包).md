# Jenkins 构建 docker (对spdier项目打包)



使用jenkins 镜像来构建

先给指定目录赋予 权限

```
cd /var/run
sudo chown -R 1000 docker.sock

cd /usr/local/bin/
sudo chown -R 1000 docker
 
```



```
# linux 
docker run --name=jenkins-docker -p 8080:8080 -p 50000:50000 -d  -v /Users/weicheng/jenkins-home-docker:/var/jenkins_home  -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker --group-add=$(stat -c %g /var/run/docker.sock) jenkins/jenkins:lts

# mac 
docker run --name=jenkins-docker -p 8080:8080 -p 50000:50000 -d  -v /Users/weicheng/jenkins-home-docker:/var/jenkins_home  -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker --group-add=$(stat -f %g /var/run/docker.sock)  jenkins/jenkins:lts

docker run --name=jenkins-docker -p 8080:8080 -p 50000:50000 -d  -v /Users/weicheng/jenkins-home-docker:/var/jenkins_home  -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker --privileged=true jenkins/jenkins:lts

docker run --name=jenkins-docker -p 8080:8080 -p 50000:50000 -d  -v /Users/weicheng/jenkins-home-docker:/var/jenkins_home  -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker --privileged=true jenkins-docker:tag

```





### shell 脚本构建

以下变量可用于shell脚本

- BRANCH_NAME

  对于multibranch项目，这将设置为正在构建的分支的名称，例如，如果您希望部署到生产`master`而不是从功能分支部署; 如果对应某种变更请求，名称通常是任意的（参考`CHANGE_ID`和`CHANGE_TARGET`）。

- CHANGE_ID

  对于与某种更改请求相对应的多分支项目，将设置为更改ID，例如拉取请求编号（如果支持）; 别的没有。

- CHANGE_URL

  对于与某种变更请求相对应的多分支项目，如果支持，将设置为更改URL; 别的没有。

- CHANGE_TITLE

  对于与某种变更请求相对应的多分支项目，如果支持，则将其设置为变更的标题; 别的没有。

- CHANGE_AUTHOR

  对于与某种变更请求相对应的多分支项目，如果支持，则将其设置为建议变更的作者的用户名; 别的没有。

- CHANGE_AUTHOR_DISPLAY_NAME

  对于与某种变更请求相对应的多分支项目，如果支持，则将其设置为作者的人名; 别的没有。

- CHANGE_AUTHOR_EMAIL

  对于与某种变更请求相对应的多分支项目，如果支持，则将其设置为作者的电子邮件地址; 别的没有。

- CHANGE_TARGET

  对于与某种更改请求相对应的多分支项目，如果支持，将将其设置为可以合并更改的目标或基本分支; 别的没有。

- BUILD_NUMBER

  当前的内部版本号，例如“153”

- BUILD_ID

  当前构建ID，对于在1.597+中创建的构建，与BUILD_NUMBER相同，但对于较旧构建，则为YYYY-MM-DD_hh-mm-ss时间戳

- BUILD_DISPLAY_NAME

  当前版本的显示名称，默认为“＃153”。

- JOB_NAME

  此构建的项目名称，例如“foo”或“foo / bar”。

- JOB_BASE_NAME

  此构建的项目的短名称剥离文件夹路径，例如“bar / foo”的“foo”。

- BUILD_TAG

  “jenkins- *$ {JOB_NAME}* - *$ {BUILD_NUMBER}* ” 字符串。JOB_NAME中的所有正斜杠（“/”）都用短划线（“ - ”）替换。方便放入资源文件，jar文件等，以便于识别。

- EXECUTOR_NUMBER

  标识正在执行此构建的当前执行程序（在同一计算机的执行程序之间）的唯一编号。这是您在“构建执行程序状态”中看到的数字，但该数字从0开始，而不是1。

- NODE_NAME

  构建在代理上的代理名称，如果在主服务器上运行则为“master”

- NODE_LABELS

  分配节点的以空格分隔的标签列表。

- WORKSPACE

  分配给构建作为工作空间的目录的绝对路径。

- JENKINS_HOME

  在主节点上为Jenkins存储数据的目录的绝对路径。

- JENKINS_URL

  Jenkins的完整URL，例如`http：// server：port / jenkins /`（注意：仅在系统配置中设置*Jenkins URL*时才可用）

- BUILD_URL

  此构建的完整URL，如`http：// server：port / jenkins / job / foo / 15 /`（必须设置*Jenkins URL*）

- JOB_URL

  此作业的完整URL，如`http：// server：port / jenkins / job / foo /`（必须设置*Jenkins URL*）

- GIT_COMMIT

  正在检出提交哈希。

- GIT_PREVIOUS_COMMIT

  最后在此分支上构建的提交的哈希值（如果有）。

- GIT_PREVIOUS_SUCCESSFUL_COMMIT

  最后在此分支上成功构建的提交哈希（如果有）。

- GIT_BRANCH

  远程分支名称（如果有）。

- GIT_LOCAL_BRANCH

  正在检出的本地分支名称（如果适用）。

- GIT_URL

  远程URL。如果有多个，会`GIT_URL_1`，`GIT_URL_2`等等。

- GIT_COMMITTER_NAME

  配置的Git提交者名称（如果有）。

- GIT_AUTHOR_NAME

  配置的Git作者姓名（如果有）。

- GIT_COMMITTER_EMAIL

  已配置的Git提交者电子邮件（如果有）。

- GIT_AUTHOR_EMAIL

  已配置的Git作者电子邮件（如果有）。

- SVN_REVISION

  当前检出到工作区的Subversion修订号，例如“12345”

- SVN_URL

  当前已签出到工作区的Subversion URL。





```
设置存储仓库
- 运维人员配置存储仓库


自动构建：
- 将项目打包到docker 中，
- 将打包好的项目重命名 传到服务器上

自动部署：
- 添加环境变量
- 部署镜像到远程服务器
- 完成部署发邮件

```



```
echo "build statr"
# Configuring environment variables
# docker registry config 
export ZXZL_DOCKER_REGISTRY_HOST="registry.cn-hangzhou.aliyuncs.com"
export ZXZL_DOCKER_REGISTRY_USERNAME="1614638361@qq.com"
export ZXZL_DOCKER_REGISTRY_PASSWORD="anying007"

# spider environment variables
# mongodb
# redis

echo "build docker image"
bash -x .tools/build_image.sh
```

