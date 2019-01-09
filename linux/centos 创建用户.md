创建新用户
[root@VM ~]# adduser it 
为这个用户初始化密码，linux会判断密码复杂度，不过可以强行忽略： 
[root@VM_~]# passwd it 
Changing password for user it. 
New password: 
BAD PASSWORD: it is based on a dictionary word 
BAD PASSWORD: is too simple 
Retype new password: 
passwd: all authentication tokens updated successfully.

授权
个人用户的权限只可以在本home下有完整权限，其他目录要看别人授权。而经常需要root用户的权限，这时候sudo可以化身为root来操作 
sudo命令的授权管理是在sudoers文件里的。可以看看sudoers： 
[root@VM_ ~]# whereis sudoers 
sudoers: /etc/sudoers.d /etc/sudoers /usr/libexec/sudoers.so /usr/share/man/man5/sudoers.5.gz 
找到这个文件位置之后再查看权限： 
[root@VM_ ~]# ls -l /etc/sudoers 
-r–r—– 1 root root 3729 Dec 8 2015 /etc/sudoers 
是的，只有只读的权限，如果想要修改的话，需要先添加w权限： 
[root@VM_ ~]# chmod -v u+w /etc/sudoers 
mode of /etc/sudoers changed to 0640 (rw-r—–) 
然后就可以添加内容了，在下面的一行下追加新增的用户： 
[root@VM_ ~]# vim /etc/sudoers



wq保存退出，这时候要记得将写权限收回：

[root@VM_ ~]# chmod -v u-w /etc/sudoers

mode of `/etc/sudoers’ changed to 0440 (r–r—–)
--------------------- 
