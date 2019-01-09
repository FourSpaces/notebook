安装 Zabbix Agent



1、首先配置ZABBIXYum库按您需要的版本和操作系统

```
rpm -Uvh http://repo.zabbix.com/zabbix/3.0/rhel/7/x86_64/zabbix-release-3.0-1.el7.noarch.rpm
```

2、在Linux系统上安装Zabbix Agent。

```
yum install zabbix zabbix-agent
```

3、编辑配置文件

```
vim  /etc/zabbix/zabbix_agentd.conf

Server=172.16.17.131 //ip为zabbix服务端的ip地址（被动模式）                    
ServerActive=172.16.17.131 //ip为zabbix-server的ip地址（主动模式）
Hostname=Zabbix server修改为Hostname=zabbix-shu            //指定服务器主机名称，这个是在web设置步骤3时候设置的；



```

4、重新启动Zabbix Agent

```
systemctl start zabbix-agent                                //开启zabbix-agent服务
systemctl enable zabbix-agent                            //设置开机启动

ps aux|grep zabbix                                                //查看服务是否启动

ps aux|grep zabbix 
netstat -lntp |grep zabbix  
```