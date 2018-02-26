## 动态调试Android 篇

当Dalvik 虚拟机从Android应用程序框架中启动时，系统属性ro.debuggable 为1 ，可使用 adb shell getprop ro.debuggable 来检查，所有程序都开启调试支持，若为0，则判断程序 androidManifest.xml



在上一篇中讲到了关于Android so的动态调试，没看的可以点这里：[点击打开链接](http://blog.csdn.net/feibabeibei_beibei/article/details/52740212)；

我自认为写的还是挺全的，在上文中我们说到关于最后一步jdb附加调试时，很多时候都会出现附加不上的问题，使人很闹心。。。于是这一篇就是专门关于这个问题进行展开的。解决这个问题方法有很多，我是按照自己认为的优良答案顺序展开的，都是借鉴网上的各路大神而总结的。

**解决篇：**

根据android的官方文档，如果调试一个APK，必须满足以下两个条件中的任何一个：

1.APK的AndroidManifest.xml文件中的Application标签包含android:debuggable="true";

2./default.prop中的ro.debuggable的值为1；

**方法一：**

在已经root的手机安装Xposed框架和xinstaller插件

目的：就是利用Xposed的HOOK插件xinstaller开启系统中所有应用的调试功能。

使用方法：

第一步：下载Xposed框架，并激活，再下载xinstaller插件安装；

第二步：开启模块，点击xinstall插件设置专家模式，进入其他设置，开启调试应用，最后在xposed中激活重启，OK！！

关于框架和xinstaller插件会放在附件中。





## mprop 临时修改内存篇

我们没有谷歌的亲儿子，但是我们有神器的小工具。

首先我们看到如图所示ro.debuggable=0；

![img](http://img.blog.csdn.net/20161006172020388?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

init进程会解析这个default.prop文件，然后把这些属性信息解析到内存中，给所有app进行访问使用，所以在init进程的内存块中是存在这些属性值的，那么这时候我们可以利用进程注入技术，我们可以使用ptrace注入到init进程，然后修改内存中的这些属性值，只要init进程不重启的话，那么这些属性值就会起效。当然这个工具已经写好，我会放在后main附件中。

解决方法：

第一步：拷贝mprop 到/data/目录下；
第二步：./mprop ro.debuggable 1；
第三步：getprop ro.debuggable;（查看此时ro.debuggable在内存中的值）
第四步：stop;start(重启adbd进程)；



1、兼容Android 4.x-7.x

2、修改ro.debuggable属性

3、mprop的使用：

​	1）将mproppush到手机adb push .\你的存放路径\ mprop /data/local/tmp/

​	2）修改权限adb shell "chmod 755 /data/local/tmp/mprop"

​	3）运行使用root权限运行mprop，设置ro.debuggable=1，查看ro.debuggable 属性是否为1

