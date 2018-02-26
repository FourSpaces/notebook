## 动态调试\分析链家APK - 获取请求校验方式

​         基础问题请自行百度／谷歌

​         对链家APK进行抓包，发现链家APK请求头中附带了请求校验信息Authorization，这里需要知道请求校验生成方式，从而模拟请求，获取链家房源信息数据。

目录：

- 1 、搭建动态调试环境 (androud studio + Android Device Monitor + android 虚拟机／真机)
- 2、反编译 链家APK ，获取APK的small 代码 , java 代码 (Apktool + jeb)
- 3、分析反编译后的代码、找到 生成Authorization的逻辑
- 4、动态调试small，获取生成Authorization的必备参数。
- 5、验证迭代、实现验证方式



#### 1、搭建动态调试环境

参考：[apk逆向 - smali动态调试](http://www.cnblogs.com/dliv3/p/5935957.html)

***工具：***

- **Android studio** ： 包含用于构建 Android 应用所需的所有工具，包括 Android Device Monitor
- **Smalidea** ：一款动态调试Smali的插件
- android 虚拟机／真机：root过的且开启了调试功能的测试机， 建议使用真机，虽然arm架构的虚拟机默认rooot ,并开启了调试功能，但是慢、卡。

***开启手机的调试功能***

根据android的官方文档，如果调试一个APK，必须满足以下两个条件中的任何一个：

​	1.**APK**的**AndroidManifest.xml**文件中的Application标签包含**android:debuggable="true"**

​	2.andorid系统中 /default.prop中的**ro.debuggable**的值为1

这里选择方式二，不对apk进行修改，就可调试，避免APK签名验证问题，满足调试、分析需求。

**修改方式**

修改ro.debuggable方式有很多，这里选择 mprop工具来临时修改内存， mprop 自行下载。

mprop的使用：

​	1）使用add 将mproppush到手机adb push .\你的存放路径\ mprop /data/local/tmp/

​	2）修改权限adb shell "chmod 755 /data/local/tmp/mprop"

​	3）运行使用root权限运行mprop，设置ro.debuggable=1， ./mprop ro.debuggable 1

​	4）重启 adb, 查看ro.debuggable 属性是否为1



#### 2、反编译 APK

***工具：***

​	**Apktool :** 逆向Android应用程序工具，可以将程序解码为原始形式 ，并在修改后重新构建为APK程序。这里主要使用它的逆向功能。

​	**jeb :**  著名APK反编译工具，第三方Java反编译器输出，支持java代码中函数跳转。可以提高效率减少分析时间。



- 使用Apktool 将链家APK反编译，备用，后面会使用它来调试

  ```shell
  apktool d Android_lianjia_pc.apk
  ```

  ​





