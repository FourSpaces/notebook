Linux 系统管理命令



1.查看本地时间

​     date

2.查看主机名

​    hostname

3.修改主机名(重启后永久生效)

​    vim /etc/sysconfig/network

​    ![img](http://www.chinahadoop.cn/files/course/2018/07-13/155058290116930113.png)

4.修改IP(重启后永久生效)

​    vim /etc/sysconfig/network-scripts/ifcfg-eth0

5.修改/设置IP和主机名映射

​    vim /etc/hosts

​    ![img](http://www.chinahadoop.cn/files/course/2018/07-13/155248096720417709.png)

6.统计文件或文件夹的大小

​    du -sh  filepath

​    ![img](http://www.chinahadoop.cn/files/course/2018/07-18/09384448d32f867015.png)

7.查看磁盘的空间

​    df -h

8.关机

​    halt

9.重启

​    reboot

10.查看命令帮助

   command --help

11.echo使用

​    在显示器上显示文字

​        echo helloworld

​    将显示内容输出到文件中（覆盖）

​    ![img](http://www.chinahadoop.cn/files/course/2018/07-13/15592910b572075363.png)

   执行echo helloworld > testfile后：

​    ![img](http://www.chinahadoop.cn/files/course/2018/07-13/155907b7e6b1832231.png)

​    将显示内容追加输出到文件的末尾

​    ![img](http://www.chinahadoop.cn/files/course/2018/07-13/1601200e5656194330.png)

​     执行echo hellohaha >>testfile后：

​    ![img](http://www.chinahadoop.cn/files/course/2018/07-13/160324c16b52913057.png)

12.service后台服务管理

​    service --status-all 查看系统中所有后台服务

​    以网络服务为例：
    service network status 查看指定服务的状态
    service network stop 停止指定服务
    service network start 启动指定服务
    service netework restart 重启指定服务

13.查看自动启动服务

​    chkconfig

​    ![img](http://www.chinahadoop.cn/files/course/2018/07-13/16040333596c037532.png)

 

​    以防火墙服务为例：
    chkconfig iptables --list查看指定服务的自动启动状态
    chkconfig iptables off 关闭指定服务的自动启动
    chkconfig iptables on  启动指定服务的自动启动

14.vim /etc/inittab

​    ![img](http://www.chinahadoop.cn/files/course/2018/07-13/1605244c364d375195.png)

 

​    0：关闭所有进程并终止系统。（不要设置）
    1：单用户模式，只能系统管理员进入，在该模式下处理在有登录用户时不能进行更改的文件。
    2：多用户的模式，但并不支持文件共享，这种模式很少应用。
    3：最常用的运行模式，主要用来提供真正的多用户模式，也是多数服务器的缺省模式。
    4：一般不被系统使用。
    5：桌面启动模式，如果关闭将不启动桌面程序。
    6：关闭所有运行的进程并重新启动系统。（不要设置）