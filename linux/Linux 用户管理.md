Linux 用户管理



1.添加新组

​    groupadd groupname

2.添加新用户

​    useradd username

3.设置用户密码

​    passwd username

4.给用户添加组

​    usermod -g groupname username

5.添加新用户同时添加组

​    useradd -g groupname username

6.查看用户组

​    groups username

7.删除用户

​    userdel username

8.删除组

​    groupdel groupname

9.将用户从组中删除

​    gpasswd -d groupname username

10.切换用户

​    su username