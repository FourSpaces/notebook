# APP 反编译



工具介绍：

**apktool**  

​     **作用：资源文件获取，能够提取出图片文件和布局文件进行使用查看**

**dex2jar**

​     **作用：将apk反编译成java源代码（classes.dex转化成jar文件）**

**jd-gui**

​     **作用：查看APK中classes.dex转化成出的jar文件，即源代码文件**



**反编译流程：**

**一、apk反编译得到程序的源码、图片、XML配置、语言资源等文件**

下载上述工具中的apktool，解压得到3个文件：aapt.exe，apktool.bat。apktool.jar 。将须要反编译的APK文件放到该文件夹下，

**打开命令行界面（执行-CMD）** ，定位到apktool目录。输入下面命令：**apktool.sh d -f  test.apk  test**    

**![img](http://img.blog.csdn.net/20140311215117218?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdmlwemp5bm8x/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)**

（命令中test.apk指的是要反编译的APK文件全名，test为反编译后资源文件存放的文件夹名称，即为：apktool.bat   d  -f    [apk文件 ][输出目录]）	



在命令行下定位到dex2jar.bat所在文件夹，输入dex2jar.bat   classes.dex。效果例如以下：

