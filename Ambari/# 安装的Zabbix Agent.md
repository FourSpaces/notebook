```
service zabbix-server start
```

## # 安装的Zabbix Agent



## 第1步 - 添加必需库

```
CentOS/RHEL 7:
# rpm -Uvh http://repo.zabbix.com/zabbix/3.0/rhel/7/x86_64/zabbix-release-3.0-1.el7.noarch.rpm

```

## 第2步 - 安装Zabbix Agent

```
# yum install -y zabbix-agent
```

## 第3步 - 编辑Zabbix Agent配置

Zabbix Agent /etc/zabbix/zabbix_agentd.conf

```
#Server=[zabbix server ip]
#Hostname=[ Hostname of client system ]

Server=192.168.1.11
Hostname=Server1
```

## 第4步 - 重新启动Zabbix Agent

在配置文件中添加ZABBIX服务器的IP后，现在使用下面的命令重新启动代理服务。

```
service zabbix-agent restart
```

要启动和停止Zabbix Agent服务，使用以下命令。

```
service zabbix-agent restart
service zabbix-agent status
service zabbix-agent stop
```



```
rpm -Uvh http://repo.zabbix.com/zabbix/3.0/rhel/7/x86_64/zabbix-release-3.0-1.el7.noarch.rpm

yum install -y zabbix-agent

sed -i "s/ServerActive=127.0.0.1/ServerActive=172.16.17.131/g" /etc/zabbix/zabbix_agentd.conf
sed -i "s/Server=127.0.0.1/Server=172.16.17.131/g" /etc/zabbix/zabbix_agentd.conf
sed -i "s/Hostname=Zabbix server/Hostname=${HOSTNAME}/g" /etc/zabbix/zabbix_agentd.conf

service zabbix-agent restart
service zabbix-agent status
```



