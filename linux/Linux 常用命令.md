Linux 常用命令

1.停止进程

```
 ctrl + c
```

2.清屏

```
  ctrl + l
```

3.搜索历史命令

```
 ctrl + r
```

4.文件名自动补全

```
 Tab键
```

5.进入目录

```
  cd path
```

6.进入用户家目录

```
  cd ~
```

7.进入最近上一次访问的目录

```
 cd -
```

8.返回上一级目录

```
  cd ..
```

9.查看目录文件列表

```
ls：查看目录下文件列表（不显示隐藏文件）

ls -a：查看目录下所有文件列表（显示隐藏文件）

ls -l：查看目录下所有文件的详细信息列表，该命令等价于ll

ls -la：查看目录下所有文件详细信息列表（显示隐藏文件）
```

10.查看文件行数

```
wc -l filename
```

​    ![img](http://www.chinahadoop.cn/files/course/2018/07-13/154218a3e334997131.png)

11.查看文件中字符个数

```
 wc -w filename
```

​    ![img](http://www.chinahadoop.cn/files/course/2018/07-13/154255f73bd9511093.png)

12.复制文件

```
cp filename ./newfilename

cp filename /otherdir

cp hello*.txt /otherdir 复制hello开头的txt文件到其他指定路径
```

13.重命名文件

```
 mv filename newfilename
```

14.查看历史命令

```
 history | grep rm 在历史命令中查找执行rm的操作
```

15.软链接

​    Linux下的软链接类似于windows下的快捷方式

```
ln -s targetfile linkfile 为targetfile文件创建软链接linkfile

rm -rf linkfile  删除软链接linkfile
```

16.查找文件

​    1）按文件名称查找，可以使用通配符*

​      在/datadir路径下查找hello开头的文件，并列出详细信息

```
find /datadir -name “hello*” -ls
```

​      ![img](http://www.chinahadoop.cn/files/course/2018/07-13/154553140cbe371663.png)

​    2）按照文件所属用户查找

​      在/home/hadoop路径下查找属于用户hadoop的文件

```
find /home/hadoop  -user hadoop -ls
```

### 文件管理

1.创建文件

​    touch filename

2.删除文件

​    rm filename（会有提示是否删除）

​    rm –f filename（强制删除）

3.创建文件夹

​    mkdir dirname

​    mkdir -p dir1/dir2/dir3（递归创建文件夹）

​    mkdir dir/{dir1,dir2}在dir在已存在的dir文件夹下同时创建dir1和dir2两个文件夹

4.删除文件夹及所有子文件夹

​    rm -r dirname（会有提示是否删除文件夹）

​    rm -rf dirname（强制删除文件夹，没有提示）

### 文件内容管理

1.将文件内容全部输出到控制台

​    cat filename

2.将文件内容分页显示，按空格下翻页，按b字母键上翻页，按q字母键退出

​    more filename

3.将文件内容分页显示，按空格下翻页，按b字母键上翻页，按上箭头（↑）上翻一行，按下箭头（↓）下翻一行。

​    less filename

5.Linux中每一个文件有一个inode，文件名修改inode编号不变，当文件
修改名称后tail -f 继续跟踪原inode编号文件；不支持文件滚动。

​    tail -f filename 

6.按照文件名称跟踪文件，文件修改名称后，有新的文件如果使用原文件名称，则继续跟踪该名称文件；支持文件滚动。

​    tail -F filename

7.查看文件末尾num行

​    tail -num filename

​    ![img](http://www.chinahadoop.cn/files/course/2018/07-13/153835b04c04818500.jpg)

8.查看文件头部num行

​    head -num filename

​    ![img](http://www.chinahadoop.cn/files/course/2018/07-13/154115bd8d11669846.png)





### 文件权限操作

1.文件或文件夹权限

​    文件夹或者文件名称前用四种字母和符号表示的一串字符串表示的文件或者文件夹类型和权限。
   ![img](http://www.chinahadoop.cn/files/course/2018/07-18/100205dca61b720808.jpg)

​    -：表示文件类型为文件
    d：表示文件类型为文件夹
    l：小写的L表示符号链接
    r：可读
    w：可写
    x：可执行

2.drwxrwxr-x文件夹权限举例：

​    第一组rwx：表示这个文件夹的拥有者对文件夹的权限：可读可写可执行
    第二组rwx：表示这个文件夹的所属组对文件夹的权限：可读可写可执行
    第三组r-x：表示这个文件夹的其他用户对文件夹的权限：可读，不可写，可执行

3.修改文件权限 

​    chmod u/g/o +/- r/w/x 表示给文件的用户/组/其他添加或者取消读写执行权限
    chmod u+x filename表示为文件/文件夹所属用户添加可执行权限
    chmod u-x filename 表示为文件/文件夹所属用户删除可执行权限
    chmod g-rw filename表示将文件/文件夹对所属组的rw权限取消
    chmod o-rw filename表示将文件/文件夹对其他人的rw权限取消

4.文件权限的每一组可以用三位二进制数表示

​    rwxrwxr-x对应的二进制111111101每组换算成十进制数字775
    如果想取消其他用户的执行权限rwxrwxr--换成二进制111111100换算成十进制数字774
    执行赋权命令：chmod 774 finame

5.如果要将一个文件夹的所有内容权限统一修改，则可以使用-R参数

​    chmod -R 777 dirname/

6.注意：目录没有执行权限的时候普通用户不能进入，属主也不可以

​    当文件具有读写权限时，虽然没有执行权限，如果该文件父文件夹具有写权限普通用户可以在文件夹中删除该文件，这样的删除操作属于对父级文件夹的修改。如果父文件夹没有写权限普通用户是不能再文件夹中删除文件的。



### vim 的使用

1.vim test

​    首先会进入“一般模式”，此模式只接受各种快捷键，不能编辑文件内容；

​    **i**  从一般模式进入编辑模式，此模式下可以输入内容；

​    **o**  从一般模式进入编辑模式并且是光标所在行的下一行开始输入内容；

​    **u**  撤销到上一步操作，多次撤销按多次u；

​    **Esc**  退出编辑模式，回到一般模式；

​    **：**  进入“底行命令模式”，输入wq命令，回车即可保存退出；

2.常用快捷键（在一般模式下使用）

​    **a**  在光标后一位开始插入

​    **A**  在该行的最后插入

​    **I**  在该行的最前面插入

​    **gg** 直接跳到文件的首行

​    **G**  直接跳到文件的末行

​    **dd** 删除行，输入2dd，则一次性删除光标所在行一下的2行

​    **yy** 复制当前行,复制多行“num+yy”，如复制三行3yy，则复制当前行和后2行

​    **p**  粘贴

​    **v**  进入字符选择模式，选择完成后，按y复制，按p粘贴

​    **ctrl+v**  进入块选择模式，选择完成后，按y复制，按p粘贴

​    **shift+v**  进入行选择模式，选择完成后，按y复制，按p粘贴

3.查找并替换

​    在一般模式下按:冒号进入命令模式操作，输入 **%s/被替换的内容/新替换的内容**，如下：

​    **%s/hello/hi** 查找文件中所有hello，替换为hi

4.查找

​    在一般模式下输入“**/查找的内容**”，如下：

​    /hi查找文件中出现的hi，并定位到第一个找到的地方，按n可以定位到下一个匹配位置（按N定位到上一个）



### 常用压缩与解压缩

1.zip压缩/解压缩，压缩文件后缀名.zip

​    zip tes.zip test.txt

​    压缩文件夹

​    zip -r dirtest.zip dirtest

​    解压缩文件/文件夹

​    unzip tes.zip/dirtest.zip

2.gzip压缩/解压缩，压缩文件后缀名.gz

​    gzip test.txt

​    解压gz文件：

​    gzip -d test.gz

3.bzip2压缩/解压缩，压缩文件后缀名.bz2

​    bzip2 test1

​    解压bz2文件

​    bzip2 -d test1.bz2

4.打包/解包，打包文件后缀名.tar

​    打包：tar -cvf barball.tar ball/

​    可以将多个文件打在一个包里

​    tar –cvf files.tar file1 file2 file3

​    解包：tar -xvf barball.tar

5.一次性完成打包和gzip压缩的操作，文件后缀名.tar.gz

​    打压缩包：tar -zcvf tarball.tar.gz ball/

​    解压缩包：tar -zxvf tarball.tar.gz

​    解压缩到指定路径下

​    tar -zxvf tarball.tar.gz -C ./tardir

6.一次性完成打包和bzip2压缩的操作，文件后缀名.tar.bz2

​    tar -jcvf bz2dir.tar.bz2 bz2dir/

​    将bz2dir.tar.bz2解压到/usr目录下面

​    tar -jxvf bz2dir.tar.bz2

### yum 的使用

1.yum介绍

​    yum是基于RMP包管理，能够从指定的服务器自动下载安装RPM包，并且自动处理依赖关系，方便快捷。

2.常用命令

​    查看yum提供的rpm列表

​    yum list

​    使用管道查找yum提供的java软件包

​    yum list | grep java

​    使用yum安装lrzsz

​    yum install -y lrzsz.x86_64

​    使用yum移除jdk

​    yum remove -y java-1.6.0-openjdk-1.6.0.35-1.13.7.1.el6_6.x86_64