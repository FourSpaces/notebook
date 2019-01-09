# Centos7离线安装Cloudera Manager 5.14.1

# 简介

如果是新手，请严格按照步骤来做。当然还有其他安装方式，这里讲的方式比较适合测试使用。

| 内容             | 版本   |
| ---------------- | ------ |
| CentOS           | 7 64位 |
| JDK              | 1.7    |
| Cloudera Manager | 5.14.1 |

本次安装一共使用3台服务器，主要用户测试。

| 服务名  | 内网IP          | 用途       |
| ------- | --------------- | ---------- |
| master  | 192.168.254.130 | 主，按照CM |
| slave01 | 192.168.254.210 | 从         |
| slave02 | 192.168.254.211 | 从         |

> 可以搭建三台虚拟机，其中master内存在8G以上，slave内存在4G以上，每个虚机的硬盘空间100G+

# 下载软件包和数据包

我这里提供两种下载方式：

> 在下载的时候可以先把服务器基础环境准备好

## 百度云盘下载

推荐百度云超级VIP账号的用户，里面包含所有的安装包和数据包

```
链接: https://pan.baidu.com/s/1JC-vpYH7SWBwju9C8DkVPw 密码: 26v8
```

## 官方下载

这是一个漫长的过程，试过才知道爽。

### 下载CM和jdk软件包

访问：<http://archive.cloudera.com/cm5/redhat/7/x86_64/cm/5.14.1/RPMS/x86_64/>

把上面的所有rpm包都下载回来本地，下载速度慢可以使用`axel`多线程下载，如果没有装`axel`，也可以使用 `wget -b`后台下载

我的相关下载都放在 `/data/soft`下，我的Cloudera Manager 5.14.1的下载放在 `/data/soft/cm5.14.1`，所以新建目录并进入目录:

```
mkdir -p /data/soft/cm5.14.1/cm-and-jdk

cd /data/soft/cm5.14.1/cm-and-jdk
```

```
wget -b http://archive.cloudera.com/cm5/redhat/7/x86_64/cm/5.14.1/RPMS/x86_64/cloudera-manager-agent-5.14.1-1.cm5141.p0.1.el7.x86_64.rpm

wget -b  http://archive.cloudera.com/cm5/redhat/7/x86_64/cm/5.14.1/RPMS/x86_64/cloudera-manager-daemons-5.14.1-1.cm5141.p0.1.el7.x86_64.rpm

wget -b http://archive.cloudera.com/cm5/redhat/7/x86_64/cm/5.14.1/RPMS/x86_64/cloudera-manager-server-5.14.1-1.cm5141.p0.1.el7.x86_64.rpm

wget -b http://archive.cloudera.com/cm5/redhat/7/x86_64/cm/5.14.1/RPMS/x86_64/cloudera-manager-server-db-2-5.14.1-1.cm5141.p0.1.el7.x86_64.rpm

wget -b http://archive.cloudera.com/cm5/redhat/7/x86_64/cm/5.14.1/RPMS/x86_64/enterprise-debuginfo-5.14.1-1.cm5141.p0.1.el7.x86_64.rpm

wget -b http://archive.cloudera.com/cm5/redhat/7/x86_64/cm/5.14.1/RPMS/x86_64/jdk-6u31-linux-amd64.rpm

wget -b http://archive.cloudera.com/cm5/redhat/7/x86_64/cm/5.14.1/RPMS/x86_64/oracle-j2sdk1.7-1.7.0+update67-1.x86_64.rpm
```

### 下载cloudera-manager安装文件

访问：<http://archive.cloudera.com/cm5/installer/5.14.1/>

下载cloudera-manager-installer.bin

```
cd /data/soft/cm5.14.1/

wget http://archive.cloudera.com/cm5/redhat/7/x86_64/cm/cloudera-manager.repo
```

### 下载rpm仓库文件

```
wget http://archive.cloudera.com/cm5/redhat/7/x86_64/cm/cloudera-manager.repo
```

### 下载parcel

这个比较大，放下服务器慢慢下吧

```
mkdir -p /data/soft/cm5.14.1/parcel

cd /data/soft/cm5.14.1/parcel
```

```
wget -b http://archive.cloudera.com/cdh5/parcels/5.14.0.24/CDH-5.14.0-1.cdh5.14.0.p0.24-el7.parcel

wget -b http://archive.cloudera.com/cdh5/parcels/5.14.0.24/CDH-5.14.0-1.cdh5.14.0.p0.24-el7.parcel.sha1
```

# 服务器环境准备

## 修改hostname及hosts

> 针对所有节点操作

为了便于安装过程中对各个服务器的访问更易区分、更便捷，我们需要分别对各个服务器修改hostname及hosts

```
hostnamectl --static set-hostname master
```

```
hostnamectl --static set-hostname slave01
```

```
hostnamectl --static set-hostname slave02
```

修改hosts：

```
vim /etc/hosts
```

根据自己的3台服务器IP地址，在最后面增加：

```
192.168.254.130 master
192.168.254.210 slave01
192.168.254.211 slave02
```

重启机器

```
reboot
```

## 关闭防火墙和selinux

> 针对所有节点操作

关闭防火墙

```
systemctl stop firewalld.service #停止firewall
systemctl disable firewalld.service #禁止firewall开机启动
firewall-cmd --state #查看默认防火墙状态（关闭后显示notrunning，开启后显示running）
```

关闭selinux：

```
vim /etc/selinux/config
```

找到SELINUX改为：

```
SELINUX=disabled
```

## ssh无密码登录

> 针对所有节点操作

先在master上执行：

```
ssh-keygen -t rsa   #一路回车到完成

ssh-copy-id -i ~/.ssh/id_rsa.pub root@master   #将公钥拷贝到本机的authorized_keys上
```

再在其他节点分别执行以下命令：

```
ssh-keygen -t rsa   #一路回车到完成

ssh-copy-id -i ~/.ssh/id_rsa.pub root@master  

#注意此处不变，将公钥拷贝到master的authorized_keys上
```

在master上，将authorized_keys分发到其他节点服务器：

```
scp ~/.ssh/authorized_keys root@slave01:~/.ssh/

scp ~/.ssh/authorized_keys root@slave02:~/.ssh/
```

## 安装ntp时间同步软件

所有节点时间一致非常重要，要不然启动Cloudera Manager服务后，后台会报错。

所有节点执行：

```
yum install ntp -y
```

安装完成后，阿里云的服务器会自动使用阿里云的ntp服务器进行同步，故可不再进行下面的配置，直接进入2.6节，若其他没有统一ntp服务器进行同步的，则还需要以下设置：

### 将master设置为主服务器（在master节点操作）：

```
vim /etc/ntp.conf
```

内容如下：

```
driftfile /var/lib/ntp/ntp.drift #草稿文件
# 允许内网其他机器同步时间
restrict 192.168.137.0 mask 255.255.255.0 nomodify notrap
 
# Use public servers from the pool.ntp.org project.
# 中国这边最活跃的时间服务器 : [http://www.pool.ntp.org/zone/cn](http://www.pool.ntp.org/zone/cn)
server 210.72.145.44 perfer   # 中国国家受时中心
server 202.112.10.36             # 1.cn.pool.ntp.org
server 59.124.196.83             # 0.asia.pool.ntp.org
 
# allow update time by the upper server 
# 允许上层时间服务器主动修改本机时间
restrict 210.72.145.44 nomodify notrap noquery
restrict 202.112.10.36 nomodify notrap noquery
restrict 59.124.196.83 nomodify notrap noquery
 
# 外部时间服务器不可用时，以本地时间作为时间服务
server  127.127.1.0     # local clock
fudge   127.127.1.0 stratum 10
```

重启ntpd服务：

```
systemctl ntpd restart
```

查看同步状态：

```
netstat -tlunp | grep ntp
```

所有子节点ntp加入开机启动：

```
systemctl enable ntpd
```

### 设置slave到master 的同步（在slave节点操作）：

```
vim /etc/ntp.conf
```

内容如下：

```
driftfile /var/lib/ntp/ntp.drift # 草稿文件

statsdir /var/log/ntpstats/
statistics loopstats peerstats clockstats
filegen loopstats file loopstats type day enable
filegen peerstats file peerstats type day enable
filegen clockstats file clockstats type day enable

# 让NTP Server为内网的ntp服务器
server 192.168.137.110
fudge 192.168.137.110 stratum 5

# 不允许来自公网上ipv4和ipv6客户端的访问
restrict -4 default kod notrap nomodify nopeer noquery 
restrict -6 default kod notrap nomodify nopeer noquery

# Local users may interrogate the ntp server more closely.
restrict 127.0.0.1
restrict ::1
```

重启ntpd服务：

```
systemctl ntpd restart
```

手动同步：

```
ntpdate -u master
```

所有节点重启服务器：

```
reboot
```

## 分配安装文件

主节点和子节点分别需要的文件整理如下：

主节点master，所需文件：

```
cloudera-manager-agent-5.14.1-1.cm5141.p0.2.el7.x86_64.rpm
cloudera-manager-daemons-5.14.1-1.cm5141.p0.2.el7.x86_64.rpm
cloudera-manager-server-5.14.1-1.cm5141.p0.2.el7.x86_64.rpm
cloudera-manager-server-db-2-5.14.1-1.cm5141.p0.2.el7.x86_64.rpm
enterprise-debuginfo-5.14.1-1.cm5141.p0.2.el7.x86_64.rpm
cloudera-manager-installer.bin
cloudera-manager.repo
CDH-5.14.1-1.cdh5.14.1.p0.2-el7.parcel
CDH-5.14.1-1.cdh5.14.1.p0.2-el7.parcel.sha1
```

从节点slave01、slave02，所需文件：

```
cloudera-manager-agent-5.14.1-1.cm5141.p0.2.el7.x86_64.rpm
cloudera-manager-daemons-5.14.1-1.cm5141.p0.2.el7.x86_64.rpm
cloudera-manager.repo
```

使用`scp`命令分配所需要的安装文件

# 安装Cloudera Manager

至此，所有设置完成。开始Cloudera Manager安装吧！

## 安装 cm-and-jdk

> 针对所有节点操作

修改仓库文件cloudera-manager.repo，把版本号加上

```
[cloudera-manager]
name = Cloudera Manager
baseurl = https://archive.cloudera.com/cm5/redhat/7/x86_64/cm/5.14.1/  #主要改这里的版本号
gpgkey = https://archive.cloudera.com/redhat/cdh/RPM-GPG-KEY-cloudera
gpgcheck = 1
```

### 验证repo文件是否起效

yum list | grep cloudera #如果列出的不是待安装的版本，执行下面命令重试

```
yum clean allyum list | grep cloudera
```

### 切换到cm-and-jdk目录下，执行

```
yum localinstall --nogpgcheck *.rpm
```

### 设置java路径：

```
vi /etc/profile
```

在该文件末尾添加以下行

```
JAVA_HOME=/usr/java/jdk1.7.0_67-cloudera
PATH=$JAVA_HOME/bin:$PATH
export JAVA_HOME PATH
```

### 检查安装：

```
java -version
```

> 下面针对master节点操作

进入cloudera-manager-installer.bin文件目录，给bin文件赋予可执行权限：

```
chmod +x ./cloudera-manager-installer.bin
```

运行：

```
./cloudera-manager-installer.bin --skip_repo_package=1
```

如果提示需要删除配置文件，则删除该文件

```
rm -rf /etc/cloudera-scm-server/db.properties
```

相同配置下顺利安装时间在1分钟内即可完成。
然后我们在web浏览器访问 http://192.168.254.130:7180/，看是否能打开页面即可，先不要进行登录操作。

注意：chd server服务器启动需要一些时间，等1分钟左右。

如果能访问，那证明 cloudera manager安装正常。

## 安装CDH

### 制作本地parcel

前面完成cloudera manager安装之后master会在/opt目录下生成cloudera文件夹，将之前下载好的CDH-*文件移动到parcel-repo文件夹中

```
cp CDH-5.14.0-1.cdh5.14.0.p0.24-el7.parcel /opt/cloudera/parcel-repo/
cp CDH-5.14.0-1.cdh5.14.0.p0.24-el7.parcel.sha1 /opt/cloudera/parcel-repo/CDH-5.14.0-1.cdh5.14.0.p0.24-el7.parcel.sha  #注意这里有重命名
```

将cloudera manager的用户授权给/opt和日志目录：

```
chown -R cloudera-scm.cloudera-scm /var/lib/cloudera-scm-server
chown cloudera-scm.cloudera-scm  /opt  -R
chown cloudera-scm.cloudera-scm  /var/log/cloudera-scm-agent -R
```

重启cloudera-scm-server（重要）

```
/etc/init.d/cloudera-scm-server restart
```

重启速度较慢，约1分钟后访问 http://192.168.254.130:7180/ 登陆，账号密码 admin
选择免费版本，一路next开始安装。

基本默认就行

在为CDH集群安装指定主机的时候写

```
master
slave01
slave02
```

![img](https://upload-images.jianshu.io/upload_images/432952-b763b24fa61a112b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

在为CDH集群安装指定主机

这里需要填写我们集群定义的ip或者服务器名称（包括安装CM的主机本身），点击搜索，即可加载出所有主机。全选所有主机，并继续。

![img](https://upload-images.jianshu.io/upload_images/432952-0bce9d2b9b6cab66.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/751/format/webp)

CDH版本

这里会出现我们之前cp过去的CDH版本，选择并继续。

![img](https://upload-images.jianshu.io/upload_images/432952-163bdf933c499835.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/826/format/webp)

JDK安装选项

![img](https://upload-images.jianshu.io/upload_images/432952-4d91458d4c20a0f9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/834/format/webp)

集群安装单用户模式

如果之前的操作没有问题，这里将会很快完成

![img](https://upload-images.jianshu.io/upload_images/432952-ef0c4cb4defd0e6b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/830/format/webp)

正在安装选定Parcel

在选择安装的服务组合的时候，选择自己需要的，如果不知道，全部安装就行

![img](https://upload-images.jianshu.io/upload_images/432952-4829fd3b73760253.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

安装成功

这里是最激动人心的时候

随便找台机器测试一下spark:

```
spark-shell
```

![img](https://upload-images.jianshu.io/upload_images/432952-43c99c6eeea63074.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

spark-shell

激动的敲了一个：

![img](https://upload-images.jianshu.io/upload_images/432952-ab6aeceb7362de25.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/696/format/webp)

Hello World



```
sudo mkdir -p /var/lib/cloudera-service-monitor
sudo mkdir -p /var/lib/cloudera-host-monitor
sudo mkdir -p /var/lib/cloudera-scm-eventserver
sudo mkdir -p /var/lib/cloudera-scm-navigator
sudo mkdir -p /var/lib/cloudera-scm-headlamp
sudo mkdir -p /var/lib/cloudera-scm-firehose
sudo mkdir -p /var/lib/cloudera-scm-alertpublisher
sudo mkdir -p /var/log/cloudera-service-monitor
sudo mkdir -p /var/log/cloudera-host-monitor
sudo mkdir -p /var/log/cloudera-scm-eventserver
sudo mkdir -p /var/log/cloudera-scm-navigator
sudo mkdir -p /var/log/cloudera-scm-headlamp
sudo mkdir -p /var/log/cloudera-scm-firehose
sudo mkdir -p /var/log/cloudera-scm-alertpublisher

sudo chown cloudera-scm:cloudera-scm /var/lib/cloudera-service-monitor
sudo chown cloudera-scm:cloudera-scm /var/lib/cloudera-host-monitor
sudo chown cloudera-scm:cloudera-scm /var/lib/cloudera-scm-eventserver
sudo chown cloudera-scm:cloudera-scm /var/lib/cloudera-scm-navigator
sudo chown cloudera-scm:cloudera-scm /var/lib/cloudera-scm-headlamp
sudo chown cloudera-scm:cloudera-scm /var/lib/cloudera-scm-firehose
sudo chown cloudera-scm:cloudera-scm /var/lib/cloudera-scm-alertpublisher
sudo chown cloudera-scm:cloudera-scm /var/log/cloudera-service-monitor
sudo chown cloudera-scm:cloudera-scm /var/log/cloudera-host-monitor
sudo chown cloudera-scm:cloudera-scm /var/log/cloudera-scm-eventserver
sudo chown cloudera-scm:cloudera-scm /var/log/cloudera-scm-navigator
sudo chown cloudera-scm:cloudera-scm /var/log/cloudera-scm-headlamp
sudo chown cloudera-scm:cloudera-scm /var/log/cloudera-scm-firehose
sudo chown cloudera-scm:cloudera-scm /var/log/cloudera-scm-alertpublisher

```





# CDH启动与关闭

CM Portal 地址：

<http://master:7180/cmf/home>

关闭步骤：

在CM portal上关闭 cluster

在所有节点关闭CM agent：

```
service cloudera-scm-agent stop
```

在master节点关闭CM server：

```
service cloudera-scm-server stop
```

启动步骤：

在所有节点启动CM agent：

```
service cloudera-scm-agent start
```

在master节点启动CM server：

```
service cloudera-scm-server start
```

在CM portal上启动 cluster

查看启动日志：

```
/var/log/cloudera-scm-server/cloudera-scm-server.log
```

如果是3台机器一般会出现错误：

在CM console中将副本设为2：

```
dfs.replication=2
```

在所有的节点命令行执行：

```
hadoop fs -setrep 2 /
```

# 安装要点：

- 仔细，认真，严格按照步骤
- 常见问题：网络，防火墙等主机设置
- 碰到问题：查看日志&官网&百度

```
cloudera JDBC Driver com.mysql.jdbc.Driver not found.
```

将oracle的mysql的jar包放置到/usr/share/java/mysql-connector-java.jar路径下即可，注意修改jar包名称；

切记除了要下载parcel文件之外，还有manifest.json文件，否则在选择安装版本界面，cloudera无法识别parcel的版本。

还有需要对于sha1文件进行改名：*.parcel.sha1 -> *.parcel.sha

为什么CDH的安装页面显示无法发现CDH ?

之前一直怀疑是流程步骤有问题，其实流程本身没有问题，问题发生在流程的实施节点上：cdh文件损坏了；本来1.5G的大小，当时只有50M，我不记得原因了，但是太坑了。

我想到了权限问题；但是忽略了文件损坏问题：sha就是干这个用的，当时应该考虑到使用sha来校验一下文件。

如果cloudera发现能够正常发现parcel，在server启动后将会打出一条日志：

```
SearchRepositoryManager-0:com.cloudera.server.web.cmf.search.components.SearchRepositoryManager: Finished constructing repo:2017-09-27T16:19:00.763Z
```

安装CDH在拷贝parcel的时候发生异常：`Exhausted available authentication methods`；

后来发现原来是因为ssh的root用户被我设置为禁止远程登录；而CDH页面向导中我还配置的用root用户登录

之后发现拷贝异常，总是联网去下载agent包，但是agent都已经在各个节点了；后来发现agent的启动是失败的（在开始的步骤中能够被自动发现的都不需要装agent，需要通过手动输入IP来进行发现的需要装agent，怎么装？联网），报错显示：`ProtocolError: <ProtocolError for 127.0.0.1/RPC2: 401 Unauthorized>`；在网上搜索了一下，如下处理：

```
sudo ps -ef | grep supervisord

kill -9 PID

sudo ./cloudera-scm-agent restart
```

未完，重启后发现：

```
Error, CM server guid updated, expected d6c22714-0175-4a40-ace6-db92b7417a40, received 613b2c09-88f6-41fe-9424-41601be40310
```

原来还需要将`cm/lib/cloudera-scm-agent/`下面的`cm_guid`进行清除；这一点让我想到了cloudera数据迁移的时候需要做的事情，需要将同目录下的uuid进行删除；

在安装的过程中还有一个问题一直困扰我，就是僵尸agent，在agent经历如上的问题后，在自动发现的列表中有一些僵尸agent，会看到同hostname的多台机器，有一个是正常通信，有的则是Unkonwn，无法删掉，因为不勾选，那么正常通信的也不会勾选上。反正后来我改了一下hosts文件，莫名其妙的在勾选列表中消失了，但是遗憾的是正常通信的也没了。安装成功后，在Hosts页面才看到这些僵尸agent，此时再delete可以正常删除。

```
Skipping start command because all roles are started or decommissioned or on decommissioned host.
```

cloudera的server停止后要稍等一会在启动，因为释放内存需要一段时间；如果停止后立即就启动将会发生一种情况，内存没有释放完，JVM的内存大量释放和JVM的大量使用将会导致JVM频繁的进行回收和释放，导致JVM Pause以及World Stop

```
JAVA_HOME is not set and Java could not be found
```

具体原因不太清楚，最小化安装了一个centos7，发现没有jdk，不解。

在clouderea中添加了一个host，然后添加了一个spark nodemanager的角色，然后就悲剧了，总是抱JAVA_HOME is not set and Java could not be found的异常；即使手动拷贝了一个jdk1.8到上面，profile也配置了，仍然不好用。不解。

再看日志的时候，发现安装程序（cloudera的安装程序）将会到几个固定的地方查找，选一个，然后将jdk拷贝到该目录下，问题解决