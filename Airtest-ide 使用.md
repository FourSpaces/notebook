## Airtest-ide 使用



### 安装

- 下载 Airtest-IDE

  1、打开 airtest http://airtest.netease.com/ 官方网站

  2、选择 适合自己系统的版本下载，这里以windows为例, 下载版本为 v1.2.0

  

  ![image-20190321144706084](/Users/weicheng/Library/Application Support/typora-user-images/image-20190321144706084.png)


​         3、点击下载链接后，出现用户协议页面，直接翻到最下面，点击 "Agree and download" 按钮，开始下载

  ![image-20190321145447788](/Users/weicheng/Library/Application Support/typora-user-images/image-20190321145447788.png)

​	下面为 撰文时 最新的 下载地址，

​	Download  [v1.2.0]

 		**Windows64**: [AirtestIDE_2019-01-15_py3_win64.zip](http://airtest.netease.com/download.html?download=AirtestIDE_2019-01-15_py3_win64.zip)
 		**Windows32**: [AirtestIDE_2019-01-15_py3_win32.zip](http://airtest.netease.com/download.html?download=AirtestIDE_2019-01-15_py3_win32.zip)
 		**Mac**: [AirtestIDE_2019-01-15_py3_Mac10-12.dmg](http://airtest.netease.com/download.html?download=AirtestIDE_2019-01-15_py3_Mac10-12.dmg)
 		**Ubuntu**: [AirtestIDE_2019-01-15_py3_ubuntu16-04.deb](http://airtest.netease.com/download.html?download=AirtestIDE_2019-01-15_py3_ubuntu16-04.deb)

​	

- 安装 Airtest-IDE

  1、将下载来的zip 压缩包提取到 指定的目录，

  2、打开 解压缩后的目录， 找到 AirtestIDE ，右击 "选择" "发送到" "桌面快捷方式"

  ![image-20190321151426864](/Users/weicheng/Library/Application Support/typora-user-images/image-20190321151426864.png) 

  3、 在桌面点击 AirtestIDE 快捷方式打开 AirtestIDE

  4、弹出登录按钮，可以选择登录，或者注册账号，这里不再赘述。

- 打开 AirtestIDE 界面

  ![image-20190321152058154](/Users/weicheng/Library/Application Support/typora-user-images/image-20190321152058154.png)

  - 创建项目
  - 打开项目
  - 保存项目
  - 另存为
  - 运行用例
  - 停止运行
  - 查看测试报告



- 连接设备

  AirtestIDE 目前支持测试 Android，Windows和iOS上的应用。

  #### 连接Android手机

  通过ADB连接你的电脑和Android手机，即可开始调试Android应用。 [ADB](https://developer.android.com/studio/command-line/adb.html) 是Google官方提供的Android调试工具。AirtestIDE依赖ADB与安卓设备进行通信。

  打开AirtestIDE，按照以下步骤进行连接：

  1. 打开手机 `设置-开发者选项-USB调试`开关，参考 [安卓官方文档](https://developer.android.com/studio/debug/dev-options.html#debugging)
  2. 在AirtestIDE设备面板中点击 `Refresh ADB` 按钮，查看连接上的设备
  3. 如果没有显示出设备，试试 `Restart ADB`，如果还不行，参考 [FAQ](http://airtest.netease.com/docs/cn/2_device_connection/2_android_faq.html)
  4. 点击对应设备的 `Connect` 按钮，进行初始化

  手机连接成功后，你即可在AirtestIDE中看到手机屏幕的镜像显示，并进行实时操作。

  ![è¿æ¥å®åææº](http://airtest.netease.com/tutorial/gif/android_connection.gif)

  



### 录制自动化脚本

现在我们可以开始录制自动化测试脚本了。

#### 模拟输入

先从最常用的模拟点击开始。

##### 基于图像识别

点击Airtest辅助窗上的 `录制` 按钮（摄像头图标），然后随着你在设备窗口上操作手机，代码会自动生成在代码窗口中。

![录制GIF](http://airtest.netease.com/tutorial/gif/airtest_auto_record.gif)

马上来验证一下，点击 `运行` 按钮运行你的第一个自动化脚本吧！

如果你觉得自动录制的图标不够精确，还可以点击Airtest辅助窗上的 `touch` 按钮，然后在设备窗口上框选精确的图标， 也可以自动生成 `touch` 语句。

![框选录制GIF](http://airtest.netease.com/tutorial/gif/airtest_manual_record.gif)

类似的模拟输入操作还有滑动：点击 `swipe` 按钮，在设备窗口上框选精确的图标作为滑动起点， 然后点击滑动终点位置，即会自动生成一个 `swipe` 语句。

其他模拟输入的API包括：

- text: 文字输入
- keyevent: 按键输入，包括(HOME/BACK/MENU等)
- sleep: 等待
- snapshot: 截屏

##### 基于UI控件

如果你发现图像识别不够精确，可以使用基于UI控件搜索的方式进行自动化测试。

目前AirtestIDE直接支持Unity3d、Cocos2d两种游戏引擎和Android源生App。 由于游戏引擎使用OpenGL等图形接口直接渲染，而没有使用Android源生的UI系统， 我们需要与游戏的Runtime进行通信获取整个UI结构。 Unity3d和Cocos2d-js我们提供了非常方便的SDK接入方 法 [点这里](http://poco-chinese.readthedocs.io/zh_CN/latest/source/doc/integration.html)。

其他游戏引擎和UI系统我们提供了SDK可自行扩展。

> 实际上在网易游戏内部我们就是用这种方式支持了Messiah/NeoX/梦幻等多个自研引擎。

- Android源生App：直接开始！

接入完成后我们即可开始。手机启动游戏，在Poco辅助窗中切换模式至对应引擎类型，即可看到整个UI结构。

![切换POCO模式.GIF](http://airtest.netease.com/tutorial/gif/poco_switch_app.gif)

点击录制按钮，然后随着你的操作，会自动生成Poco语句。

![POCO自动录制.GIF](http://airtest.netease.com/tutorial/gif/poco_auto_record.gif)

同样，你也可以通过UI树形结构更精确的检视UI控件， 双击自动生成Poco语句， 或者自行选择更好的写法。更好的属性选择，通常会增强整个自动化脚本的健壮性和可读性， 这是门 [学问](http://poco-chinese.readthedocs.io/zh_CN/latest/source/README.html#working-with-poco-objects) 。

![POCO自行选择.GIF](http://airtest.netease.com/tutorial/gif/poco_manual_record.gif)

录制完脚本后记得运行试试效果。

由于Android源生App应用的UI结构可以通过 `Accessibility` 获取，我们直接开始使用。 将Poco辅助窗的模式切换至 `Android`能看到整个UI树形结构。

![Android Poco.GIF](http://airtest.netease.com/tutorial/gif/android-poco.gif)

实际上，上述两种方式分别是基于两个框架：

- 基于图像识别的 [Airtest](https://github.com/AirtestProject/Airtest) 框架，适用于所有Android和Windows游戏
- 基于UI控件搜索的 [Poco](https://github.com/AirtestProject/Poco) 框架，适用于Unity3d，Cocos2d与Android App

这两个框架都是由网易团队开发，在实际项目使用经验中，我们发现两者互相配合会得到最好的效果。