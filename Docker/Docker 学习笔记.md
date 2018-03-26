## Docker 学习笔记

s

### Docker环境安装

启动终端后，通过命令可以检查安装后的 Docker 版本。

```shell
$ docker --version
Docker version 1.12.3, build 6b644ec
$ docker-compose --version
docker-compose version 1.8.1, build 878cff1
$ docker-machine --version
docker-machine version 0.8.2, build e18a919
```

如果 `docker version`、`docker info` 都正常的话，可以运行一个 [Nginx 服务器](https://hub.docker.com/_/nginx/)：

```
$ docker run -d -p 80:80 --name webserver nginx
```

服务运行后，可以访问 [http://localhost](http://localhost/)，如果看到了 "Welcome to nginx!"，就说明 Docker for Mac 安装成功了。

要停止 Nginx 服务器并删除执行下面的命令：

```
$ docker stop webserver
$ docker rm webserver
```
### Docker  加速器

- 检查加速器是否生效

Linux系统下配置完加速器需要检查是否生效，在命令行执行 ps -ef | grep dockerd，如果从结果中看到了配置的 --registry-mirror 参数说明配置成功。

```
$ sudo ps -ef | grep dockerd
root      5346     1  0 19:03 ?        00:00:00 /usr/bin/dockerd --registry-mirror=https://jxus37ad.mirror.aliyuncs.com

```
### 获取镜像

从 Docker Registry 获取镜像的命令是 `docker pull`。其命令格式为：

```
docker pull [选项] [Docker Registry地址]<仓库名>:<标签>

```

具体的选项可以通过 `docker pull --help` 命令看到，这里我们说一下镜像名称的格式。

- Docker Registry地址：地址的格式一般是 `<域名/IP>[:端口号]`。默认地址是 Docker Hub。
- 仓库名：如之前所说，这里的仓库名是两段式名称，既 `<用户名>/<软件名>`。对于 Docker Hub，如果不给出用户名，则默认为 `library`，也就是官方镜像。

比如：

```
bogon:~ kevin$ docker pull ubuntu:16.04
16.04: Pulling from library/ubuntu
e0a742c2abfd: Pull complete 
486cb8339a27: Pull complete 
dc6f0d824617: Pull complete 
4f7a5649a30e: Pull complete 
672363445ad2: Pull complete 
Digest: sha256:84c334414e2bfdcae99509a6add166bbb4fa4041dc3fa6af08046a66fed3005f
Status: Downloaded newer image for ubuntu:16.04
```

查看系统版本的命令

```
cat /etc/os-releases
```
### 镜像定制

我们修改了容器的文件，也就是改动了容器的存储层。我们可以通过 `docker diff` 命令看到具体的改动

```
$ docker diff webserver
```

#### docker commit 命令

可以将容器的存储层保存下来成为镜像。换句话说，就是在原有镜像的基础上，再叠加上容器的存储层，并构成新的镜像。

`docker commit` 的语法格式为：

```
docker commit [选项] <容器ID或容器名> [<仓库名>[:<标签>]]
```

#### docker build 命令

这里我们使用了 `docker build` 命令进行镜像构建。其格式为：

```
docker build [选项] <上下文路径/URL/->
```

在一个空白目录中，建立一个文本文件，并命名为 `Dockerfile`：

```
$ mkdir mynginx
$ cd mynginx
$ touch Dockerfile

$ docker build -t nginx:v3 .
```
#### Dockerfile 指令详解

- **COPY :  复制文件**

  格式：

  - `COPY <源路径>... <目标路径>`
  - `COPY ["<源路径1>",... "<目标路径>"]`

  和 `RUN` 指令一样，也有两种格式，一种类似于命令行，一种类似于函数调用。

  `COPY` 指令将从构建上下文目录中 `<源路径>` 的文件/目录复制到新的一层的镜像内的 `<目标路径>` 位置。比如：

  ```
  COPY package.json /usr/src/app/
  ```

  `<源路径>` 可以是多个，甚至可以是通配符，其通配符规则要满足 Go 的 [`filepath.Match`](https://golang.org/pkg/path/filepath/#Match) 规则，如：

  ```
  COPY hom* /mydir/
  COPY hom?.txt /mydir/
  ```

  `<目标路径>` 可以是容器内的绝对路径，也可以是相对于工作目录的相对路径（工作目录可以用 `WORKDIR`指令来指定）。目标路径不需要事先创建，如果目录不存在会在复制文件前先行创建缺失目录。

  此外，还需要注意一点，使用 `COPY` 指令，源文件的各种元数据都会保留。比如读、写、执行权限、文件变更时间等。这个特性对于镜像定制很有用。特别是构建相关文件都在使用 Git 进行管理的时候

- **CMD :  容器启动命令**

  CMD 容器启动命令

  `CMD` 指令的格式和 `RUN` 相似，也是两种格式：

  - `shell` 格式：`CMD <命令>`
  - `exec` 格式：`CMD ["可执行文件", "参数1", "参数2"...]`
  - 参数列表格式：`CMD ["参数1", "参数2"...]`。在指定了 `ENTRYPOINT` 指令后，用 `CMD` 指定具体的参数。

  之前介绍容器的时候曾经说过，Docker 不是虚拟机，容器就是进程。既然是进程，那么在启动容器的时候，需要指定所运行的程序及参数。`CMD` 指令就是用于指定默认的容器主进程的启动命令的。

  在运行时可以指定新的命令来替代镜像设置中的这个默认命令，比如，`ubuntu` 镜像默认的 `CMD` 是 `/bin/bash`，如果我们直接 `docker run -it ubuntu` 的话，会直接进入 `bash`。我们也可以在运行时指定运行别的命令，如 `docker run -it ubuntu cat /etc/os-release`。这就是用 `cat /etc/os-release` 命令替换了默认的 `/bin/bash` 命令了，输出了系统版本信息。

  在指令格式上，一般推荐使用 `exec` 格式，这类格式在解析时会被解析为 JSON 数组，因此一定要使用双引号 `"`，而不要使用单引号。

  如果使用 `shell` 格式的话，实际的命令会被包装为 `sh -c` 的参数的形式进行执行。比如：

  ```
  CMD echo $HOME

  ```

  在实际执行中，会将其变更为：

  ```
  CMD [ "sh", "-c", "echo $HOME" ]

  ```

  这就是为什么我们可以使用环境变量的原因，因为这些环境变量会被 shell 进行解析处理。

  提到 `CMD` 就不得不提容器中应用在前台执行和后台执行的问题。这是初学者常出现的一个混淆。

  Docker 不是虚拟机，容器中的应用都应该以前台执行，而不是像虚拟机、物理机里面那样，用 upstart/systemd 去启动后台服务，容器内没有后台服务的概念。

  一些初学者将 `CMD` 写为：

  ```
  CMD service nginx start

  ```

  然后发现容器执行后就立即退出了。甚至在容器内去使用 `systemctl` 命令结果却发现根本执行不了。这就是因为没有搞明白前台、后台的概念，没有区分容器和虚拟机的差异，依旧在以传统虚拟机的角度去理解容器。

  对于容器而言，其启动程序就是容器应用进程，容器就是为了主进程而存在的，主进程退出，容器就失去了存在的意义，从而退出，其它辅助进程不是它需要关心的东西。

  而使用 `service nginx start` 命令，则是希望 upstart 来以后台守护进程形式启动 `nginx` 服务。而刚才说了 `CMD service nginx start` 会被理解为 `CMD [ "sh", "-c", "service nginx start"]`，因此主进程实际上是 `sh`。那么当 `service nginx start` 命令结束后，`sh` 也就结束了，`sh` 作为主进程退出了，自然就会令容器退出。

  正确的做法是直接执行 `nginx` 可执行文件，并且要求以前台形式运行。比如：

  ```
  CMD ["nginx", "-g", "daemon off;"]
  ```



- **ENV :  设置环境变量**

  ​	ENV 设置环境变量

  ​	格式有两种：

  ​	-  `ENV <key> <value>`

  ​	-  `ENV <key1>=<value1> <key2>=<value2>...`

  这个指令很简单，就是设置环境变量而已，无论是后面的其它指令，如 `RUN`，还是运行时的应用，都可以直接使用这里定义的环境变量。





# 使用卷来管理数据

卷是一个或者多个容器内被选定的目录，为Docker 提供持久数据或者共享数据。卷可以在容器间共享，容器停止卷里面的内容依旧存在。

Docker 文档地址 

https://yeasy.gitbooks.io/docker_practice/content/underly/network.html



# Docker 基础命令

## 基本操作

- 镜像搜索

  ```
  $ docker search [镜像名]
  --automated :只列出 automated build类型的镜像；
  --no-trunc :显示完整的镜像描述；
  -s :列出收藏数不小于指定值的镜像。
  ```

- 获得镜像Pull

  ```
  $ docker pull [镜像名：标签名]
  ```

- 查看镜像列表

  ```
  $ docker images 
  ```

- 运行镜像

  ```
  $ docker run -i -t ubuntu:16.04 /bin/bash --name python3.5
  ```

  - docker run - 运行一个容器
  - -t - 分配一个（伪）tty (link is external)
  - -i - 交互模式 (so we can interact with it)
  - ubuntu:14.04 - 使用 ubuntu 基础镜像 14.04
  - /bin/bash - 运行命令 bash shell

    注: ubuntu 会有多个版本，通过指定 tag 来启动特定的版本 [image]:[tag]

- 查看Docker 容器运行列表。

  ```
  docker ps  # 查看当前运行的容器, ps -a 列出当前系统所有的容器
  ```

- 相关快捷键

  - 退出：Ctrl-Dorexit
  - detach：Ctrl-P + Ctrl-Q
  - attach:docker attach CONTAINER-ID 

- 删除一个或多个镜像

  ```
  Usage: docker rmi IMAGE [IMAGE...] Remove one or more images

    -f, --force=false Force removal of the image # 强制移除镜像不管是否有容器使用该镜像 --no-prune=false Do not delete untagged parents # 不要删除未标记的父镜像 
  ```

  ​

- 删除所有停止的容器

  ```
  docker rm $(docker ps -a -q)
  ```

- 删除所有 none 的镜像

  ```
  docker rmi $(docker images | grep "^<none>" | awk "{print $3}")

  docker rmi $(docker images -f "dangling=true" -q)
  ```

- 进入容器中 docker exec

  ```
  [root@localhost temp]# docker exec -it bb2 /bin/bash
  ```

  使用-it时，则和我们平常操作console界面类似。而且也不会像attach方式因为退出，导致 
  整个容器退出。 
  这种方式可以替代ssh或者nsenter、nsinit方式，在容器内进行操作。

  如果只使用-t参数，则可以看到一个console窗口，但是执行命令会发现由于没有获得stdin 
  的输出，无法看到命令执行情况。


# 容器相关命令

- 创建守护容器

  守护式容器没有交互模式，适合运行应用程序和服务。

  ```
  $ docker run --name daemon_dave -d ubuntu /bin/bash -c "while true; do echo hello world ; sleep 1; done"
  20479f4a9dfbfc205039e1e68f8f0f65de33722133f7ae269c15dd466bd21b10
  ```

  -d 参数 ：将容器放到后台运行

  while 循环 会一直打印 hello world ，直到容器或其进程停止运行。


- docker run 运行中的参数选项

  ```
  -v 允许将宿主机的目录作为卷，挂载到容器里
  ```

- 删除本地镜像

  如果要删除本地的镜像，可以使用 `docker rmi` 命令，其格式为：

  ```
  docker rmi [选项] <镜像1> [<镜像2> ...]
  ```

  注意  docker rm 命令是删除容器，不要混淆。


-------
- Docker 容器中常用功能
```
Management Commands:
  checkpoint  <管理检查点> Manage checkpoints 
  config      <管理Docker配置> Manage Docker configs
  container   <管理容器> Manage containers
  image       <管理镜像> Manage images
  network     <管理网络> Manage networks
  node        <管理Swarm节点> Manage Swarm nodes
  plugin      <管理插件> Manage plugins
  secret      <管理Docker的秘密> Manage Docker secrets
  service     <管理服务> Manage services
  stack       <管理Docker堆栈> Manage Docker stacks
  swarm       <管理群> Manage Swarm
  system      <管理Docker> Manage Docker
  volume      <管理卷> Manage volumes

Commands:
  attach      <将本地标准输入，输出和错误流附加到正在运行的容器> 
              Attach local standard input, output, and error streams to a running container
  build       <从Dockerfile构建映像> 
              Build an image from a Dockerfile
  commit      <从容器的更改创建一个新的图像>
              Create a new image from a container's changes
  cp          <复制容器和本地文件系统之间的文件/文件夹> 
              Copy files/folders between a container and the local filesystem
  create      <创建一个新的容器>
              Create a new container
  deploy      <部署新堆栈或更新现有堆栈> 
              Deploy a new stack or update an existing stack
  diff        <检查对容器文件系统上文件或目录的更改> 
              Inspect changes to files or directories on a container's filesystem
  events      <从服务器获取实时事件>
              Get real time events from the server
  exec        <在运行容器中运行命令> 
              Run a command in a running container
  export      <将容器的文件系统导出为tar存档> 
              Export a container's filesystem as a tar archive
              
  history     <显示图片/快照的历史> 
              Show the history of an image
  images      <列出镜像> 
              List images
  import      <从tarball导入内容以创建文件系统映像> 
              Import the contents from a tarball to create a filesystem image
  info        <显示系统范围的信息>
              Display system-wide information
  inspect     <返回关于Docker对象的低级信息> 
              Return low-level information on Docker objects
  kill        <杀死一个或多个运行容器> 
              Kill one or more running containers
  load        <从tar存档或STDIN加载映像> 
              Load an image from a tar archive or STDIN
  login       <登录Docker> 
              Log in to a Docker registry
  logout      <从Docker注销> 
              Log out from a Docker registry
  logs        <获取容器的日志> 
              Fetch the logs of a container
  pause       <暂停一个或多个容器内的所有进程> 
              Pause all processes within one or more containers
  port        <列表端口映射或容器的特定映射> 
              List port mappings or a specific mapping for the container
  ps          <列出容器> 
              List containers
  pull        <从Docker仓库中拉一个图像或存储库>
              Pull an image or a repository from a registry
  push        <将图像或存储库推送到docker存储库>
              Push an image or a repository to a registry
  rename      <重命名容器> 
              Rename a container
  restart     <重新启动一个或多个容器> 
              Restart one or more containers
  rm          <删除一个或多个容器> 
              Remove one or more containers
  rmi         <删除一个或多个镜像> 
              Remove one or more images
  run         <在新容器中运行命令>
              Run a command in a new container
  save        <将一个或多个图像保存到tar存档（默认情况下流式传输到STDOUT）> 
              Save one or more images to a tar archive (streamed to STDOUT by default)
  search      <搜索Docker Hub图像> 
              Search the Docker Hub for images
  start       <启动一个或多个停止的容器> 
              Start one or more stopped containers
  stats       <显示容器的实时流资源使用统计信息> 
              Display a live stream of container(s) resource usage statistics
  stop        <停止一个或多个运行容器>
              Stop one or more running containers
  tag         <创建引用SOURCE_IMAGE的标签TARGET_IMAGE>
              Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         <显示容器的正在运行的进程>
              Display the running processes of a container
  unpause     <取消暂停一个或多个容器内的所有进程> 
              Unpause all processes within one or more containers
  update      <更新一个或多个容器的配置> 
              Update configuration of one or more containers
  version     <显示Docker版本信息> 
              Show the Docker version information
  wait        <阻止直到一个或多个容器停止，然后打印他们的退出代码>
              Block until one or more containers stop, then print their exit codes

有关命令的更多信息，请运行'docker COMMAND --help'。

```

### 镜像改名

```
docker tag IMAGEID(镜像id) REPOSITORY:TAG（仓库：标签）

#例子
docker tag ca1b6b825289 registry.cn-hangzhou.aliyuncs.com/xxxxxxx:v1.0
```





##  常用docker 启动命令

mysql 

 ```
## mysql 服务端
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 -d mysql:latest

## 在docker  中链接
docker run -it --link some-mysql:mysql --rm mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'

## 
 ```



## 常用docker 命令

以下是此页面上的基本 Docker 命令列表，以及一些相关命令（如果您要在继续之前进行进一步探索）。

```
docker build -t friendlyname .# 使用此目录的 Dockerfile 创建镜像
docker run -p 4000:80 friendlyname  # 运行端口 4000 到 90 的“友好名称”映射
docker run -d -p 4000:80 friendlyname         # 内容相同，但在分离模式下
docker ps                                 # 查看所有正在运行的容器的列表
docker stop <hash>                     # 平稳地停止指定的容器
docker ps -a           # 查看所有容器的列表，甚至包含未运行的容器
docker kill <hash>                   # 强制关闭指定的容器
docker rm <hash>              # 从此机器中删除指定的容器
docker rm $(docker ps -a -q)           # 从此机器中删除所有容器
docker images -a                               # 显示此机器上的所有镜像
docker rmi <imagename>            # 从此机器中删除指定的镜像
docker rmi $(docker images -q)             # 从此机器中删除所有镜像
docker login             # 使用您的 Docker 凭证登录此 CLI 会话
docker tag <image> username/repository:tag  # 标记 <image> 以上传到镜像库
docker push username/repository:tag            # 将已标记的镜像上传到镜像库
docker run username/repository:tag                   # 运行镜像库中的镜像
```



```Shell
kevins-MBP:~ weicheng$ docker -help
unknown shorthand flag: 'e' in -elp
See 'docker --help'.

Usage:	docker COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default "/Users/weicheng/.docker")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default "/Users/weicheng/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/Users/weicheng/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/Users/weicheng/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  checkpoint  Manage checkpoints
  config      Manage Docker configs
  container   Manage containers
  image       Manage images
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images (experimental)
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container # 容器
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  deploy      Deploy a new stack or update an existing stack
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker COMMAND --help' for more information on a command.
```

