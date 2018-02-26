# 安装Python 3.6 在Ubuntu 16.04 LTS 版本

在ubuntu 16.04版本中，系统默认安装 了python 2.7和3.5版本，因为系统本身用到python的程序，删除默认的版本又担心系统有问题，那有没有办法同时在安装和使用python 3.6版本呢？下文将一起安装python 3.6并修改原系统的python3命令以使用新安装的版本。

1、配置软件仓库，因为python 3.6 新版没有发布到ubuntu的正式仓库中，咱们通过第3方仓库来做。在命令行中输入：

```
sudo add-apt-repository ppa:jonathonf/python-3.61
```

*系统会提示输入密码*

2、检查系统软件包并安装 python 3.6

```
sudo apt-get update
sudo apt-get install python3.6
```

3、查看python版本信息（现在在你的系统中已经有3个python版本了） 
![这里写图片描述](http://img.blog.csdn.net/20170819170116817?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbHp6eW9r/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

4、通过上图我们看到，新安装的3.6版本需要输入 python3.6才能使用，那能不能配置我只输入python3时就默认使用3.6版本呢，当然可以，执行以下命令

```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2

sudo update-alternatives --config python3
```

5、最后，咱们确认一下

```
python3 -V
```
