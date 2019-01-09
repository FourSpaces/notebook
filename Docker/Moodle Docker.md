# Moodle Docker



Moodle是一个非常受欢迎的开源学习管理解决方案（LMS），用于提供电子教学课程和计划。 它不仅被大学使用，而且还被世界各地数百家为员工提供电子学习教育的公司使用。 Moodle具有简单的界面，拖放功能，基于角色的权限，深度报告，许多语言翻译，记录良好的API等等。 随着一些最大的大学和组织已经在使用它，Moodle已经准备好满足几乎任何规模的组织的需求。



## Docker Compose

```
$ curl -sSL https://raw.githubusercontent.com/bitnami/bitnami-docker-moodle/master/docker-compose.yml > docker-compose.yml

$ docker-compose up -d
```

# Why use Bitnami Images?



- Bitnami密切跟踪上游源变化，并使用我们的自动化系统及时发布此图像的新版本。
- 使用Bitnami图像，可以尽快获得最新的错误修复和功能。
  Bitnami容器，虚拟机和云映像使用相同的组件和配置方法 - 可以根据您的项目需求轻松切换格式。
- 我们所有的图像都基于minideb一个简单的基于Debian的容器图像，它为您提供了一个小的基本容器图像和熟悉的领先的Linux发行版。
- Bitnami容器图像每天发布，提供最新的分发包。



## 如何在Kubernetes中部署Moodle？

将Bitnami应用程序部署为Helm Charts是开始使用Kubernetes上的应用程序的最简单方法。 在Bitnami Moodle Chart GitHub存储库中阅读有关安装的更多信息。

Bitnami容器可与Kubeapps一起使用，以便在群集中部署和管理Helm Charts。



要运行此应用程序，您需要Docker Engine 1.10.0。建议使用版本1.6.0或更高版本的Docker Compose。



## 如何使用此镜像

使用数据库容器运行Moodle

建议使用数据库服务器运行Moodle。您可以使用docker-compose或手动运行容器。

```
version: '2'

services:
  mariadb:
    image: 'bitnami/mariadb:latest'
    environment:
      - MARIADB_USER=bn_moodle
      - MARIADB_DATABASE=bitnami_moodle
      - ALLOW_EMPTY_PASSWORD=yes
    volumes:
      - 'mariadb_data:/bitnami'
  moodle:
    image: 'bitnami/moodle:latest'
    environment:
      - MARIADB_HOST=mariadb
      - MARIADB_PORT_NUMBER=3306
      - MOODLE_DATABASE_USER=bn_moodle
      - MOODLE_DATABASE_NAME=bitnami_moodle
      - ALLOW_EMPTY_PASSWORD=yes
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - 'moodle_data:/bitnami'
    depends_on:
      - mariadb

volumes:
  mariadb_data:
    driver: local
  moodle_data:
    driver: local
```

手动运行应用程序

如果要手动运行应用程序而不是使用docker-compose，则这些是运行所需的基本步骤：

1, 为应用程序和数据库创建新网络：

```
$ docker network create moodle-tier
```

2, 为MariaDB持久性创建卷并创建MariaDB容器

```
$ docker volume create --name mariadb_data
$ docker run -d --name mariadb \
 -e ALLOW_EMPTY_PASSWORD=yes \
 -e MARIADB_USER=bn_moodle \
 -e MARIADB_DATABASE=bitnami_moodle \
 --net moodle-tier \
 --volume mariadb_data:/bitnami \
 bitnami/mariadb:latest
```

注意：您需要为容器命名，以便Moodle解析主机

3, 为Moodle持久性创建卷并启动容器

```
$ docker volume create --name moodle_data
$ docker run -d --name moodle -p 80:80 -p 443:443 \
 -e ALLOW_EMPTY_PASSWORD=yes \
 -e MOODLE_DATABASE_USER=bn_moodle \
 -e MOODLE_DATABASE_NAME=bitnami_moodle \
 --net moodle-tier \
 --volume moodle_data:/bitnami \
 bitnami/moodle:latest
```

然后，您可以通过 http://your-ip//访问您的应用程序





如果删除容器，则所有数据和配置都将丢失，下次运行映像时，数据库将重新初始化。 为避免这种数据丢失，您应该安装一个即使在删除容器后也会保留的卷。

对于持久性，您应该在/ bitnami路径上安装卷。 此外，您应该装载一个卷以持久存储MariaDB数据。

上面的示例定义了docker卷，即mariadb_data和moodle_data。 只要不删除这些卷，Moodle应用程序状态就会持续存在。

为避免无意中删除这些卷，您可以将主机目录装载为数据卷。 或者，您可以使用卷插件来托管卷数据。



### 使用docker-compose在主机中挂载永久文件夹

这需要从之前显示的模板中进行修改：

```
version: '2'

services:
  mariadb:
    image: 'bitnami/mariadb:latest'
    environment:
      - ALLOW_EMPTY_PASSWORD=yes
      - MARIADB_USER=bn_moodle
      - MARIADB_DATABASE=bitnami_moodle
    volumes:
      - '/path/to/mariadb-persistence:/bitnami'
  moodle:
    image: 'bitnami/moodle:latest'
    environment:
      - MOODLE_DATABASE_USER=bn_moodle
      - MOODLE_DATABASE_NAME=bitnami_moodle
      - ALLOW_EMPTY_PASSWORD=yes
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - '/path/to/moodle-persistence:/bitnami'
    depends_on:
      - mariadb
```

### 手动挂载持久文件夹

在这种情况下，您需要在run命令中指定要挂载的目录。该过程与先前显示的过程相同：



1,如果您之前没有这样做，请为应用程序和数据库创建一个新网络：

```
$ docker network create moodle-tier
```

2,在以前的网络中启动MariaDB数据库：

```
$ docker run -d --name mariadb \
 -e ALLOW_EMPTY_PASSWORD=yes \
 -e MARIADB_USER=bn_moodle \
 -e MARIADB_DATABASE=bitnami_moodle \
 -v /path/to/mariadb-persistence:/bitnami \
 --net moodle-tier \
 bitnami/mariadb:latest

```

注意：您需要为容器命名，以便Moodle解析主机

3, 运行Moodle容器：

```
$ docker run -d -p 80:80 -p 443:443 --name moodle \
 -e ALLOW_EMPTY_PASSWORD=yes \
 -e MOODLE_DATABASE_USER=bn_moodle \
 -e MOODLE_DATABASE_NAME=bitnami_moodle \
 --net moodle-tier \
 --volume /path/to/moodle-persistence:/bitnami \
 bitnami/moodle:latest
```

4,升级此应用程序

注意：从Moodle 3.4.0-r1开始，应该在官方文档之后在docker容器内手动完成应用程序升级。

作为替代方案，您可以尝试使用更新的docker镜像进行升级，但是Moodle容器中的任何数据都将丢失，您必须重新安装手动添加的所有插件和主题。

Bitnami提供最新版本的MariaDB和Moodle，包括安全补丁，在它们上游后不久。 我们建议您按照以下步骤升级容器。 我们将在这里介绍Moodle容器的升级。 对于MariaDB升级，请参阅https://github.com/bitnami/bitnami-docker-mariadb/blob/master/README.md#upgrade-this-image



1, 获取更新的图像

```
$ docker pull bitnami/moodle:latest
```

2, 停止你的容器

对于docker-compose：

```
$ docker-compose stop moodle
```

用于手动执行:

```
$ docker stop moodle
```

3, 拍摄应用程序状态的快照

```
$ rsync -a /path/to/moodle-persistence /path/to/moodle-persistence.bkp.$(date +%Y%m%d-%H.%M.%S)
```

另外，快照MariaDB数据

如果升级失败，您可以使用这些快照来还原应用程序状态。

1, 删除当前正在运行的容器

$ docker-compose rm -v moodle

或

$ docker rm -v moodle



2，删除持久数据。从3.4.0-r1开始需要这样做，因为整个安装是持久的，否则新的docker镜像将使用旧的应用程序代码。

获取包含持久数据的卷

```bash
$ docker volume ls
```

删除volume

```bash
$ docker volume rm YOUR_VOLUME
```

3， 运行新的镜像

对于docker-compose`$ docker-compose up moodle`

对于手动执行（如果需要，安装目录）：

docker run --name moodle bitnami/moodle:latest



## 构造

### 环境变量

启动moodle映像时，可以通过在docker-compose文件或docker run命令行上传递一个或多个环境变量来调整实例的配置。

用户和站点配置

- `MOODLE_USERNAME`: Moodle application username. Default: **user**
- `MOODLE_PASSWORD`: Moodle application password. Default: **bitnami**
- `MOODLE_EMAIL`: Moodle application email. Default: **user@example.com**

使用现有数据库

- `MARIADB_HOST`: Hostname for MariaDB server. Default: **mariadb**
- `MARIADB_PORT_NUMBER`: Port used by MariaDB server. Default: **3306**
- `MOODLE_DATABASE_NAME`: Database name that Moodle will use to connect with the database. Default: **bitnami_moodle**
- `MOODLE_DATABASE_USER`: Database user that Moodle will use to connect with the database. Default: **bn_moodle**
- `MOODLE_DATABASE_PASSWORD`: Database password that Moodle will use to connect with the database. No defaults.
- `ALLOW_EMPTY_PASSWORD`: It can be used to allow blank passwords. Default: **no**

使用mysql-client为Moodle创建数据库

- `MARIADB_HOST`: Hostname for MariaDB server. Default: **mariadb**
- `MARIADB_PORT_NUMBER`: Port used by MariaDB server. Default: **3306**
- `MARIADB_ROOT_USER`: Database admin user. Default: **root**
- `MARIADB_ROOT_PASSWORD`: Database password for the `MARIADB_ROOT_USER` user. No defaults.
- `MYSQL_CLIENT_CREATE_DATABASE_NAME`: New database to be created by the mysql client module. No defaults.
- `MYSQL_CLIENT_CREATE_DATABASE_USER`: New database user to be created by the mysql client module. No defaults.
- `MYSQL_CLIENT_CREATE_DATABASE_PASSWORD`: Database password for the `MYSQL_CLIENT_CREATE_DATABASE_USER` user. No defaults.
- `ALLOW_EMPTY_PASSWORD`: It can be used to allow blank passwords. Default: **no**



如果要添加新的环境变量：

- 对于docker-compose，在应用程序部分下添加变量名称和值：

  ```
  moodle:
    image: bitnami/moodle:latest
    ports:
      - 80:80
      - 443:443
    environment:
      - MOODLE_PASSWORD=my_password
  ```





- 对于手动执行，为每个变量和值添加-e选项：

```
$ docker run -d  -p 80:80 -p 443:443 --name moodle
  -e MOODLE_PASSWORD=my_password \
  --net moodle-tier \
  --volume /path/to/moodle-persistence:/bitnami \
  bitnami/moodle:latest
```



### SMTP配置

要将Moodle配置为使用SMTP发送电子邮件，您可以设置以下环境变量：

- `SMTP_HOST`: SMTP host.
- `SMTP_PORT`: SMTP port.
- `SMTP_USER`: SMTP account user.
- `SMTP_PASSWORD`: SMTP account password.
- `SMTP_PROTOCOL`: SMTP protocol.

这将是使用GMail帐户进行SMTP配置的示例

- docker-compose:

```
moodle:
 image: bitnami/moodle:latest
 ports:
   - 80:80
   - 443:443
 environment:
   - MARIADB_HOST=mariadb
   - MARIADB_PORT_NUMBER=3306
   - MOODLE_DATABASE_USER=bn_moodle
   - MOODLE_DATABASE_NAME=bitnami_moodle
   - SMTP_HOST=smtp.gmail.com
   - SMTP_PORT=587
   - SMTP_USER=your_email@gmail.com
   - SMTP_PASSWORD=your_password
   - SMTP_PROTOCOL=tls
```

- 手动执行：

```
$ docker run -d  -p 80:80 -p 443:443 --name moodle
  -e MARIADB_HOST=mariadb \
  -e MARIADB_PORT_NUMBER=3306 \
  -e MOODLE_DATABASE_USER=bn_moodle \
  -e MOODLE_DATABASE_NAME=bitnami_moodle \
  -e SMTP_HOST=smtp.gmail.com \
  -e SMTP_PORT=587 \
  -e SMTP_USER=your_email@gmail.com \
  -e SMTP_PASSWORD=your_password \
  --net moodle-tier \
  --volume /path/to/moodle-persistence:/bitnami \
  bitnami/moodle:latest

```

