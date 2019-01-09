# [基于【CentOS-7+ Ambari 2.7.0 + HDP 3.0】搭建HAWQ数据仓库01 —— 准备环境，搭建本地仓库，安装ambari](https://www.cnblogs.com/dajianshi/p/9455980.html)



一、集群软硬件环境准备：

操作系统：  centos 7 x86_64.1804

Ambari版本：2.7.0

HDP版本：3.0.0

HAWQ版本：2.3.0
5台PC作为工作站：

| ep-bd01 | ep-bd02 | ep-bd03 | ep-bd04 | ep-bd05 |
| ------- | ------- | ------- | ------- | ------- |
|         |         |         |         |         |

  其中ep-bd01作为主节点，用于安装ambari-server。

二、配置操作系统，安装必备软件

1，安装CentOS 7操作系统：[环境配置，安装必备软件。](https://www.cnblogs.com/dajianshi/p/9474398.html)

2，安装配置NTP服务，保证集群时间保持同步，以防止由于时间不同而造成掉线故障。

详细看随笔：[基于【CentOS-7+ Ambari 2.7.0 + HDP 3.0】搭建HAWQ数据仓库之——安装配置NTP服务，保证集群时间保持同步](https://www.cnblogs.com/dajianshi/p/9473951.html)
见《安装配置NTP服务》

3，安装MariaDB Server用于Ambari server以及Hue和Hive

详细过程，参见：[基于【CentOS-7+ Ambari 2.7.0 + HDP 3.0】搭建HAWQ数据仓库之一 —— MariaDB 安装配置](https://www.cnblogs.com/dajianshi/p/9473650.html)

 4，安装yum priorities plugin

```
yum install yum-plugin-priorities -y
```

 

三、搭建本地仓库：

1，下载软件包：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
cd /root
mkdir downloads
cd downloads
wget http://public-repo-1.hortonworks.com/HDP-GPL/centos7/3.x/updates/3.0.0.0/HDP-GPL-3.0.0.0-centos7-gpl.tar.gz
wget http://public-repo-1.hortonworks.com/HDP/centos7/3.x/updates/3.0.0.0/hdp.repo
wget http://public-repo-1.hortonworks.com/HDP/centos7/3.x/updates/3.0.0.0/HDP-3.0.0.0-1634.xml
wget http://public-repo-1.hortonworks.com/ambari/centos7/2.x/updates/2.7.0.0/ambari.repo
wget http://public-repo-1.hortonworks.com/HDP-UTILS-1.1.0.22/repos/centos7/HDP-UTILS-1.1.0.22-centos7.tar.gz
wget http://public-repo-1.hortonworks.com/HDP/centos7/3.x/updates/3.0.0.0/HDP-3.0.0.0-centos7-rpm.tar.gz
wget http://public-repo-1.hortonworks.com/ambari/centos7/2.x/updates/2.7.0.0/ambari-2.7.0.0-centos7.tar.gz
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

2、搭建本地仓库：

安装并开启Apache HTTP服务

![img](https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif) 安装HTTPD服务

确保/var/www/html目录存在，没有的话创建。

```
mkdir -p /var/www/html
```

 创建HDP，HDF子目录

```
cd /var/www/html
mkdir hdp  hdf
```

解开下载的软件包：

```
cd /var/www/html
tar -zxvf  /root/downloads/ambari-2.7.0.0-centos7.tar.gz    -C .
tar -zxvf  /root/downloads/HDP-3.0.0.0-centos7-rpm.tar.gz   -C ./hdp
tar -zxvf  /root/downloads/HDP-GPL-3.0.0.0-centos7-gpl.tar.gz  -C ./hdp
tar -zxvf  /root/downloads/HDP-UTILS-1.1.0.22-centos7.tar.gz   -C ./hdp
```

 修改下载的ambari.repo，

```
vim ambari.repo
安装如下内容修改，[注意版本号，需要根据具体下载的版本不同修改，解压后自己查看一下]：
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
#VERSION_NUMBER=2.7.0.0-897
```

[ambari-2.7.0.0]
\#json.url = http://public-repo-1.hortonworks.com/HDP/hdp_urlinfo.json
name=ambari Version - ambari-2.7.0.0
baseurl=http://ep-bd01/ambari/centos7/2.7.0.0-897
gpgcheck=1
gpgkey=http://ep-bd01/ambari/centos7/2.7.0.0-897/RPM-GPG-KEY/RPM-GPG-KEY-Jenkins
enabled=1
priority=1

```
 
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

复制到/etc/yum.repos.d

```
cp ambari.repo   /etc/yum.repos.d/ambari.repo
```

修改下载的hdp.repo，

```
vim hdp.repo
安装如下内容修改，[注意版本号，需要根据具体下载的版本不同修改，解压后自己查看一下]：
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

\#VERSION_NUMBER=3.0.0.0-1634
[HDP-3.0]
name=HDP Version - HDP-3.0.0.0
baseurl=http://ep-bd01/hdp/HDP/centos7/3.0.0.0-1634
gpgcheck=1
gpgkey=http://ep-bd01/hdp/HDP/centos7/3.0.0.0-1634/RPM-GPG-KEY/RPM-GPG-KEY-Jenkins
enabled=1
priority=1

[HDP-3.0-GPL]
name=HDP GPL Version - HDP-GPL-3.0.0.0
baseurl=http://ep-bd01/hdp/HDP-GPL/centos7/3.0.0.0-1634
gpgcheck=1
gpgkey=http://ep-bd01/hdp/HDP-GPL/centos7/3.0.0.0-1634/RPM-GPG-KEY/RPM-GPG-KEY-Jenkins
enabled=1
priority=1

[HDP-UTILS-1.1.0.22]
name=HDP-UTILS Version - HDP-UTILS-1.1.0.22
baseurl=http://ep-bd01/hdp/HDP-UTILS/centos7/1.1.0.22
gpgcheck=1
gpgkey=http://ep-bd01/hdp/HDP-UTILS/centos7/1.1.0.22/RPM-GPG-KEY/RPM-GPG-KEY-Jenkins
enabled=1
priority=1

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

保存退出，复制到/etc/yum.repos.d/

```
cp  hdp.repo  /etc/yum.repos.d/hdp.repo
```

四、主节点安装ambari server

1，使用刚才配置好的本地仓库，直接yum命令安装。

```
yum install ambari-server -y
```

2，查看ambari server 状态

```
 systemctl status ambari-server 

● ambari-server.service - LSB: ambari-server daemon
   Loaded: loaded (/etc/rc.d/init.d/ambari-server; bad; vendor preset: disabled)
   Active: inactive (dead)
     Docs: man:systemd-sysv-generator(8)
```

看到ambari server已成功安装了。

3，配置mariadb，建立用户和数据库供ambari使用

建立数据库用户ambari

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
mysql -uroot -p
```

MariaDB [(none)]> use mysql;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [mysql]> grant all privileges on *.* to 'ambari'@'%' identified by 'ambari';
Query OK, 0 rows affected (0.06 sec)

MariaDB [mysql]> flush privileges;
Query OK, 0 rows affected (0.00 sec)

MariaDB [mysql]>

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

建立数据库ambari，并运行ambari数据库建表sql命令文件。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
MariaDB [mysql]> create database ambari;
Query OK, 1 row affected (0.01 sec)

MariaDB [mysql]> use ambari;
Database changed
MariaDB [ambari]> source /var/lib/ambari-server/resources/Ambari-DDL-MySQL-CREATE.sql;
Query OK, 0 rows affected (0.01 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.06 sec)

Query OK, 0 rows affected (0.00 sec)
Statement prepared
... ...
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

4，配置ambari server

执行命令

```
ambari-server setup
```

回答选择项，其中JDK选择“”Custom“”，给出系统安装目录，数据库一定要选择高级配置，指定mariadb数据库和用户，本人系统中详细过程如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
Using python  /usr/bin/python
Setup ambari-server
Checking SELinux...
SELinux status is 'disabled'
Customize user account for ambari-server daemon [y/n] (n)? n
Adjusting ambari-server permissions and ownership...
Checking firewall status...
Checking JDK...
[1] Oracle JDK 1.8 + Java Cryptography Extension (JCE) Policy Files 8
[2] Custom JDK
==============================================================================
Enter choice (1): 1
To download the Oracle JDK and the Java Cryptography Extension (JCE) Policy Files you must accept the license terms found at http://www.oracle.com/technetwork/java/javase/terms/license/index.html and not accepting will cancel the Ambari Server setup and you must install the JDK and JCE files manually.
Do you accept the Oracle Binary Code License Agreement [y/n] (y)? ^C
Aborting ... Keyboard Interrupt.
[root@ep-bd01 downloads]# ambari-server setup
Using python  /usr/bin/python
Setup ambari-server
Checking SELinux...
SELinux status is 'disabled'
Customize user account for ambari-server daemon [y/n] (n)? n
Adjusting ambari-server permissions and ownership...
Checking firewall status...
Checking JDK...
[1] Oracle JDK 1.8 + Java Cryptography Extension (JCE) Policy Files 8
[2] Custom JDK
==============================================================================
Enter choice (1): 2
WARNING: JDK must be installed on all hosts and JAVA_HOME must be valid on all hosts.
WARNING: JCE Policy files are required for configuring Kerberos security. If you plan to use Kerberos,please make sure JCE Unlimited Strength Jurisdiction Policy Files are valid on all hosts.
Path to JAVA_HOME: ^C
Aborting ... Keyboard Interrupt.
[root@ep-bd01 downloads]# echo $JAVA_HOME
/usr/java/jdk1.8.0_181-amd64
[root@ep-bd01 downloads]# $JAVA_HOME/bin/java -version
java version "1.8.0_181"
Java(TM) SE Runtime Environment (build 1.8.0_181-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.181-b13, mixed mode)
[root@ep-bd01 downloads]# ambari-server setup         
Using python  /usr/bin/python
Setup ambari-server
Checking SELinux...
SELinux status is 'disabled'
Customize user account for ambari-server daemon [y/n] (n)? n
Adjusting ambari-server permissions and ownership...
Checking firewall status...
Checking JDK...
[1] Oracle JDK 1.8 + Java Cryptography Extension (JCE) Policy Files 8
[2] Custom JDK
==============================================================================
Enter choice (1): 2
WARNING: JDK must be installed on all hosts and JAVA_HOME must be valid on all hosts.
WARNING: JCE Policy files are required for configuring Kerberos security. If you plan to use Kerberos,please make sure JCE Unlimited Strength Jurisdiction Policy Files are valid on all hosts.
Path to JAVA_HOME: ^C
Aborting ... Keyboard Interrupt.
[root@ep-bd01 downloads]# ambari-server setup
Using python  /usr/bin/python
Setup ambari-server
Checking SELinux...
SELinux status is 'disabled'
Customize user account for ambari-server daemon [y/n] (n)? n   
Adjusting ambari-server permissions and ownership...
Checking firewall status...
Checking JDK...
[1] Oracle JDK 1.8 + Java Cryptography Extension (JCE) Policy Files 8
[2] Custom JDK
==============================================================================
Enter choice (1): 1
To download the Oracle JDK and the Java Cryptography Extension (JCE) Policy Files you must accept the license terms found at http://www.oracle.com/technetwork/java/javase/terms/license/index.html and not accepting will cancel the Ambari Server setup and you must install the JDK and JCE files manually.
Do you accept the Oracle Binary Code License Agreement [y/n] (y)? y
Downloading JDK from http://public-repo-1.hortonworks.com/ARTIFACTS/jdk-8u112-linux-x64.tar.gz to /var/lib/ambari-server/resources/jdk-8u112-linux-x64.tar.gz
ERROR: Exiting with exit code 1. 
REASON: Downloading or installing JDK failed: 'Fatal exception:  Failed to download JDK: <urlopen error [Errno -2] Name or service not known>. Please check that the JDK is available at http://public-repo-1.hortonworks.com/ARTIFACTS/jdk-8u112-linux-x64.tar.gz. Also you may specify JDK file location in local filesystem using --jdk-location command line argument., exit code 1'. Exiting.
[root@ep-bd01 downloads]# ambari-server setup
Using python  /usr/bin/python
Setup ambari-server
Checking SELinux...
SELinux status is 'disabled'
Customize user account for ambari-server daemon [y/n] (n)? n
Adjusting ambari-server permissions and ownership...
Checking firewall status...
Checking JDK...
[1] Oracle JDK 1.8 + Java Cryptography Extension (JCE) Policy Files 8
[2] Custom JDK
==============================================================================
Enter choice (1): 2
WARNING: JDK must be installed on all hosts and JAVA_HOME must be valid on all hosts.
WARNING: JCE Policy files are required for configuring Kerberos security. If you plan to use Kerberos,please make sure JCE Unlimited Strength Jurisdiction Policy Files are valid on all hosts.
Path to JAVA_HOME: /usr/java/jdk1.8.0_181-amd64
Validating JDK on Ambari Server...done.
Check JDK version for Ambari Server...
JDK version found: 8
Minimum JDK version is 8 for Ambari. Skipping to setup different JDK for Ambari Server.
Checking GPL software agreement...
GPL License for LZO: https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html
Enable Ambari Server to download and install GPL Licensed LZO packages [y/n] (n)? n
Completing setup...
Configuring database...
Enter advanced database configuration [y/n] (n)? y
Configuring database...
==============================================================================
Choose one of the following options:
[1] - PostgreSQL (Embedded)
[2] - Oracle
[3] - MySQL / MariaDB
[4] - PostgreSQL
[5] - Microsoft SQL Server (Tech Preview)
[6] - SQL Anywhere
[7] - BDB
==============================================================================
Enter choice (1): 3
Hostname (localhost): ep-bd01
Port (3306): 
Database name (ambari): ambari
Username (ambari): ambari
Enter Database Password (bigdata): 
Re-enter password: 
Configuring ambari database...
Should ambari use existing default jdbc /usr/share/java/mysql-connector-java.jar [y/n] (y)? y
Configuring remote database connection properties...
WARNING: Before starting Ambari Server, you must run the following DDL against the database to create the schema: /var/lib/ambari-server/resources/Ambari-DDL-MySQL-CREATE.sql
Proceed with configuring remote database connection properties [y/n] (y)? y
Extracting system views...
ambari-admin-2.7.0.0.897.jar
....
Ambari repo file doesn't contain latest json url, skipping repoinfos modification
Adjusting ambari-server permissions and ownership...
Ambari Server 'setup' completed successfully.
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

5，命令行方式设置mysql数据库连接库，用于oozie和ranger连接mariadb时使用（上面设置后不起作用，必须如下操作）：

```
ambari-server setup --jdbc-db=mysql --jdbc-driver=/usr/share/java/mysql-connector-java.jar
```

 

6，配置ambari-server自启动，启动ambari-server

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
[root@ep-bd01 downloads]# systemctl enable ambari-server
[root@ep-bd01 downloads]# systemctl start ambari-server
[root@ep-bd01 downloads]# systemctl status ambari-server
● ambari-server.service - LSB: ambari-server daemon
   Loaded: loaded (/etc/rc.d/init.d/ambari-server; bad; vendor preset: disabled)
   Active: active (running) since Tue 2018-08-14 11:06:16 CST; 2min 36s ago
     Docs: man:systemd-sysv-generator(8)
  Process: 323056 ExecStart=/etc/rc.d/init.d/ambari-server start (code=exited, status=0/SUCCESS)
   CGroup: /system.slice/ambari-server.service
           └─323080 /usr/java/jdk1.8.0_181-amd64/bin/java -server -XX:NewRatio=3 -XX:+UseConcMarkSweepGC -XX:-UseGCOverheadLimit -XX:CMSInitiatingOccupancyFraction=60 -XX:+CMSClassUnloadingEnabled -Dsun.zip.disableMemoryMapping=true -...

Aug 14 11:05:58 ep-bd01 ambari-server[323056]: Organizing resource files at /var/lib/ambari-server/resources...
Aug 14 11:05:58 ep-bd01 ambari-server[323056]: Ambari database consistency check started...
Aug 14 11:05:58 ep-bd01 ambari-server[323056]: Server PID at: /var/run/ambari-server/ambari-server.pid
Aug 14 11:05:58 ep-bd01 ambari-server[323056]: Server out at: /var/log/ambari-server/ambari-server.out
Aug 14 11:05:58 ep-bd01 ambari-server[323056]: Server log at: /var/log/ambari-server/ambari-server.log
Aug 14 11:06:16 ep-bd01 ambari-server[323056]: Waiting for server start.....................
Aug 14 11:06:16 ep-bd01 ambari-server[323056]: Server started listening on 8080
Aug 14 11:06:16 ep-bd01 ambari-server[323056]: DB configs consistency check: no errors and warnings were found.
Aug 14 11:06:16 ep-bd01 ambari-server[323056]: Ambari Server 'start' completed successfully.
Aug 14 11:06:16 ep-bd01 systemd[1]: Started LSB: ambari-server daemon.systemctl status ambari-server
● ambari-server.service - LSB: ambari-server daemon
   Loaded: loaded (/etc/rc.d/init.d/ambari-server; bad; vendor preset: disabled)
   Active: active (running) since Tue 2018-08-14 11:06:16 CST; 2min 36s ago
     Docs: man:systemd-sysv-generator(8)
  Process: 323056 ExecStart=/etc/rc.d/init.d/ambari-server start (code=exited, status=0/SUCCESS)
   CGroup: /system.slice/ambari-server.service
           └─323080 /usr/java/jdk1.8.0_181-amd64/bin/java -server -XX:NewRatio=3 -XX:+UseConcMarkSweepGC -XX:-UseGCOverheadLimit -XX:CMSInitiatingOccupancyFraction=60 -XX:+CMSClassUnloadingEnabled -Dsun.zip.disableMemoryMapping=true -...

Aug 14 11:05:58 ep-bd01 ambari-server[323056]: Organizing resource files at /var/lib/ambari-server/resources...
Aug 14 11:05:58 ep-bd01 ambari-server[323056]: Ambari database consistency check started...
Aug 14 11:05:58 ep-bd01 ambari-server[323056]: Server PID at: /var/run/ambari-server/ambari-server.pid
Aug 14 11:05:58 ep-bd01 ambari-server[323056]: Server out at: /var/log/ambari-server/ambari-server.out
Aug 14 11:05:58 ep-bd01 ambari-server[323056]: Server log at: /var/log/ambari-server/ambari-server.log
Aug 14 11:06:16 ep-bd01 ambari-server[323056]: Waiting for server start.....................
Aug 14 11:06:16 ep-bd01 ambari-server[323056]: Server started listening on 8080
Aug 14 11:06:16 ep-bd01 ambari-server[323056]: DB configs consistency check: no errors and warnings were found.
Aug 14 11:06:16 ep-bd01 ambari-server[323056]: Ambari Server 'start' completed successfully.
Aug 14 11:06:16 ep-bd01 systemd[1]: Started LSB: ambari-server daemon.
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

ok，Ambari-server安装完成。浏览器访问ambari-server服务：

```
http://ep-bd01:8080
```

默认用户名/密码为：admin/admin，登陆后界面如下：

![ambari-server安装后](https://images2018.cnblogs.com/blog/2249/201808/2249-20180814112941049-1498994606.png)

 五、所有主机节点，安装ambari-agent，并配置自启动

```
yum install ambari-agent -y 
systemctl enable ambari-agent 
systemctl restart ambari-agent && systemctl status ambari-agent
```



# 自我总结

一、安装配置NTP服务

1、所有节点上使用yum安装配置NTP服务

```
yum install ntp -y
```

2、选定一台节点作为NTP server, 192.168.58.11
修改/etc/ntp.conf

```
vim  /etc/ntp.conf
```

1>，注释掉restrict 127.0.0.1 ，修改为：

```
restrict 192.168.58.11 mask 255.255.0.0 nomodify notrap
```

2>，使本地时钟可作为时钟源，添加如下两行：

```
server 127.127.1.0
fudge 127.127.1.0 stratum 10
```

3，屏蔽默认服务器设置，添加国内节点

```
# server in China
server 202.112.10.36 prefer
server 1.cn.pool.ntp.org
server 2.cn.pool.ntp.org
server 3.cn.pool.ntp.org
server 0.cn.pool.ntp.org
```

4， 启用ntpd服务

设置ntpd为自启动

```
systemctl enable ntpd
```

启动ntpd服务

```
systemctl start ntpd
```

三、配置其他节点作为客户端（每个节点都执行）

1，修改/etc/ntp.conf

添加主节点，屏蔽默认服务器设置：

```
server  192.168.58.11
```

 保存退出，复制到其他客户端节点或者在每个节点执行上述编辑。

例如在ep-bd02上编辑完成后，从ep-bd02通过scp复制到其他三个主机：

```
scp /etc/ntp.conf ep-bd03:/etc/.
scp /etc/ntp.conf ep-bd04:/etc/.
scp /etc/ntp.conf ep-bd05:/etc/.

```

2，【每个节点】执行：

从主节点同步时间：

```
ntpdate ep-bd01
```

设置自动启动，然后启动ntpd

```
systemctl enable ntpd
systemctl start ntpd
```

四、注意事项

1，当server与client之间的时间误差过大时（可能是1000秒），处于对修改时间可能对系统和应用带来不可预知的问题，NTP将停止时间同步！
所以如果发现NTP启动之后时间并不进行同步时，应该考虑到可能是时间差过大引起的，此时需要先手动进行时间同步！

手动同步命令

```
ntpdate  ep-bd01
```

2，“”the NTP socket is in use, exiting“”【错误解决】 

**the NTP socket is in use, exiting的解决办法
the NTP socket is in use, exiting
这个错误的原因是存在已经启动的ntpdate服务，重复启动导致的。
使用下面的命令查看进程：“lsof -i:123” 这里的123是端口号，例如我的机器运行结果是：

```
[root@ep-bd03]# lsof -i:123
```

命令输出如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME

ntpd 30016 ntp 16u IPv4 389632 0t0 UDP *:ntp 
ntpd 30016 ntp 17u IPv6 389633 0t0 UDP *:ntp 
ntpd 30016 ntp 18u IPv4 389638 0t0 UDP localhost:ntp 
ntpd 30016 ntp 19u IPv4 389639 0t0 UDP ep-bd03:ntp 
ntpd 30016 ntp 20u IPv4 389640 0t0 UDP ep-bd03:ntp 
ntpd 30016 ntp 21u IPv6 389641 0t0 UDP localhost:ntp 
ntpd 30016 ntp 22u IPv6 389642 0t0 UDP ep-bd03:ntp
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

杀kill掉这个进程后，重新运行ntpdate 校时服务

```
[root@ep-bd03 ]# kil -9 30016
```

 



