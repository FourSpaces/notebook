# Scala 程序 创建并打包

今天来到公司，感慨，既然 sbt是scala的御用打包管理工具，就用sbt，虽然比较抵触，但是不学是不可能的，sbt按道理也是比较简单的。后来在使用中 确实不是 很难

在使用IDEA  创建基于sbt 的scala项目中，确实遇到里一些小的问题，但是如果处理好了，这些都是非常简单，迅速进入到开发中。

中间 遇到的问题 ，

1.sbt首次时候 ，下载 解压  配置环境 变量，首次创建sbt项目，sbt会下载很多依赖，大概需要二十分钟左右，再下次创建sbt 会非常快

![img](//upload-images.jianshu.io/upload_images/182433-843fb05ecba1cc0a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

默认情况下 jdk  sbt  scala sdk 都会被统统引入进来，

![img](//upload-images.jianshu.io/upload_images/182433-2b24c3ddeaacc697.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

假如 没有正确引入，可以在菜单栏，【File】-【Project Structure】设置 【Global Libraries】和【Modeles】【Libraries】从新引入对应的sdk

![img](//upload-images.jianshu.io/upload_images/182433-0e2ec3d5480c7302.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

![img](//upload-images.jianshu.io/upload_images/182433-2bfeb4f0dc8cc858.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

![img](//upload-images.jianshu.io/upload_images/182433-962f4f98e029c779.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

![img](//upload-images.jianshu.io/upload_images/182433-a2e8e23102b3748d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

![img](//upload-images.jianshu.io/upload_images/182433-a85698017221644a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

2.引入依赖，下载失败，在引入一些 springframework的jar包，在build.sbt,填写了依赖项，但是并没有开始自动下载相关jar 包，后来在sbt的命令行交互环境compile中发现，springframework 5 版本下载失败，但是springwork 4的版本是可以下载，这种情况要么修改 sbt 仓库地址，要么就是选择可以下载的内容。另外为了 方便 sbt的 编译 打包  自动下载依赖，建议 开启 sbt view  ，在 菜单栏的 view 中选择 tool window 选择  sbt，即可开启。并且自动同步 下载依赖会比较方便

![img](//upload-images.jianshu.io/upload_images/182433-4dbca294b2fa7581.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/488)

另外 开启 配置   sbt  Task ，设置 编译 compile ，IDEA右上角部分 ，选择 Edit Configurations,在弹层中的左上角 点击 绿色的加号，选择 SBT Task,Tasks：对应sbt命令，编译就选择填写 【compile】 ，【working directory】 选择对应的 scala的类文件，其他如果没有额外配置可以不动，选择 Apply，即可使用。

![img](//upload-images.jianshu.io/upload_images/182433-aa112149db4e74d8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

如何运行一个Scala的文件，有时候会错误的选择 scala console 或者scala script，但是都不对，应该是选择Application ，这个可以在 Edit Configurations 中选择【Application】，配置 【Main class】对应的类文件，和【working directory】，【use classpath of module】，apply 即可启用，

![img](//upload-images.jianshu.io/upload_images/182433-fad3ee94b3d378d0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

另外简单的就是 在项目文件目录中，右击对应的类文件，选择【run  **.scala】,切记 不要选择有 美元$ 符号的，否则便是java编译，会出现需要static method。

正常的基于sbt 的scala 项目 的文件目录结构：

![img](//upload-images.jianshu.io/upload_images/182433-ab4d3e6d980d7107.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

另外是 代码层次的 

比如 继承   比如引入其他jar包

子类快速实现 父类的方法，在子类 类名红线处 ，alt + enter回车即可  快速实现，

父類

![img](//upload-images.jianshu.io/upload_images/182433-db154765e674a002.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/421)

父類

子類

![img](//upload-images.jianshu.io/upload_images/182433-bd91b110e3e5823a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/428)

有時 import 的 類的類路徑  import 語句是置灰的，說明引入時是有問題，需要 加引號或者其他大括號之類的

![img](//upload-images.jianshu.io/upload_images/182433-e6bb49c23e0ecde2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/549)

另外 是調試  Debug 狀態，項目文件目錄  類文件  右鍵  Debug 即可

F8 往下走，F7進入方法內部

另外熟練常用的IDEA的一些快捷鍵非常有幫助

在新建的scala 項目中 嘗試 了  for循環遍歷，if 判斷， 一些 函數式 lamabda 表達式。

代碼只有長寫才有可能熟練

碰见 jvm不能运行，应该是sbt 的jvm 的路径错了， Terminal中 which java 找到 java 的全路径，一般就是sbt的jvm路径默认错了，少一个文件夹

idea  Cannot run program "/Library/Java/JavaVirtualMachines/jdk1.8.0_51.jdk/bin/java" (in directory

![img](//upload-images.jianshu.io/upload_images/182433-9c1ced3067b51a58.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

![img](//upload-images.jianshu.io/upload_images/182433-1c8f1b124e214a87.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/572)

小礼物走一走，来简书关注我

赞赏支持

 

 

 

 

 