# 适用于Android的Appium Docker

### 为什么首先需要这种方法？

- 帮助您快速轻松地设置appium + android的自动化环境
- 如果没有这种方法，您需要手动执行每个自动设置步骤; 这可能很慢并且容易出错
- 有关更多详细信息，请参阅[Selenium Conference Youtube视频](https://www.youtube.com/watch?v=jGW6ycW_tTQ&list=PLRdSclUtJDYXFVU37NEqh4KkT78BLqjcG&index=7)

### 图像包括：

- appium / appium - Docker图像在真实的android设备上运行appium测试。
- 要在android模拟器中执行，请访问[docker-android](https://github.com/butomo1989/docker-appium.git)

### 如何构建：

```
$ docker build -t "appium/appium:local" -f Appium/Dockerfile Appium
```

以下`--build-arg`是可用的：

- ANDROID_BUILD_TOOLS_VERSION
- ANDROID_PLATFORM_VERSION
- APPIUM_VERSION
- SDK_VERSION

## 在Docker macOSX上设置Android真实设备测试

1. 确保你在mac上安装了最新的docker。

   ```
   $ docker-machine --version
   $ docker-machine version 0.10.0, build 76ed2a6
   ```

2. 按照以下步骤创建码头机

   ```
   $ docker-machine create --driver virtualbox appium-test-machine
   ```

3. 在创建的码头机中启用USB

   ```
   $ docker-machine stop appium-test-machine
   $ vboxmanage modifyvm appium-test-machine --usb on --usbehci on
   $ docker-machine start appium-test-machine
   ```

   **\*注意：*** 您需要安装[ Extension Pack](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)取决于您的virtualbox版本，以防出现错误“未找到USB 2.0控制器的实施”

4. 打开虚拟框，移至创建的appium-test-machine，选择USB并添加Android设备和主控制器。

   [![alt标签](https://github.com/appium/appium-docker-android/raw/master/images/virtualbox.png)](https://github.com/appium/appium-docker-android/blob/master/images/virtualbox.png)

5. SSH创建到Docker机器中

   ```
   $ docker-machine ssh appium-test-machine
   ```

6. 通过Android设备删除您的主机的所有权

   ```
   adb kill-server
   ```

7. 运行泊坞窗图像

   ```
   $ docker run --privileged -d -p 4723:4723  -v /dev/bus/usb:/dev/bus/usb --name container-appium appium/appium
   ```

8. 运行以下命令来验证adb设备是否可以检测到连接的Android设备。

   ```
   $ docker exec -it container-appium adb devices
   ```

9. 使用以下测试配置运行UI测试

   ```
   Push the apk file into the container
   $ docker cp /Users/loacl-macosx-path-to-apk/app-debug.apk container-appium:/opt
   
   Desired Capabilities:
   
   private void androidSetup() throws MalformedURLException {
           caps.setCapability("deviceName", "Android");
           caps.setCapability("app", "/opt/app-debug.apk");
           //Get the IP Address of boot2docker
           //docker inspect $(docker ps -q) | grep IPA
           driver = new AndroidDriver<MobileElement>(new URL("http://192.168.99.100:32769/wd/hub"), caps);
   }
   ```

### 分享Android识别码

每次，您将（重新）创建容器，连接到容器设备将在首次连接后要求授权。为了防止这种情况，您可以通过创建的所有容器共享一个身份。要做到这一点，您应该：

- 将所有设备连接到Docker物理机器
- 跑 `adb devices`
- 授权所有设备（不要忘记检查**始终允许此计算机**）

[![始终允许此计算机屏幕截图](https://github.com/appium/appium-docker-android/raw/master/images/authorization.png)](https://github.com/appium/appium-docker-android/blob/master/images/authorization.png)

- 用参数运行你的容器 `-v ~/.android:/root/.android`

例如：

```
$ docker run --privileged -d -p 4723:4723 -v ~/.android:/root/.android -v /dev/bus/usb:/dev/bus/usb --name container-appium appium/appium
```

## 将每个设备连接到单独的容器

在某些使用情况下，您可能希望为每个设备运行一个Appium-Docker-Android容器。要达到此目的，您必须运行`adb kill-server`并提供以下`--device`选项`docker run`：

```
$ docker run -d -p 4723:4723 --device /dev/bus/usb/XXX/YYY:/dev/bus/usb/XXX/YYY -v ~/.android:/root/.android --name device1 appium/appium
$ docker run -d -p 4724:4723 --device /dev/bus/usb/XXX/ZZZ:/dev/bus/usb/XXX/ZZZ -v ~/.android:/root/.android --name device2 appium/appium
```

## 通过Air连接到Android设备

Appium-Docker-Android可以通过Air与Android设备连接。

要做到这一点，你需要配置Android设备，根据[官方手册](https://developer.android.com/studio/command-line/adb.html#wireless)

然后用以下参数运行docker容器：

- REMOTE_ADB =真
- ANDROID_DEVICES = <android_device_host>：<android_device_port> [，<android_device_host>：<android_device_port>]
- REMOTE_ADB_POLLING_SEC = 60（默认值：5，轮询连接设备列表以便连接到丢失的远程设备之间的间隔）

```
$ docker run -d -p 4723:4723 -e REMOTE_ADB=true -e ANDROID_DEVICES=192.168.0.5:5555,192.168.0.6:5555 -e REMOTE_ADB_POLLING_SEC=60
```

## 连接到Selenium网格

Appium-Docker-Android可以通过传递以下参数与硒网格连接：

- CONNECT_TO_GRID =真
- APPIUM_HOST = <ip_address_of_appium_server>
- APPIUM_PORT = <port_of_appium_server>
- SELENIUM_HOST = <ip_address_of_selenium_hub>
- SELENIUM_PORT = <port_of_selenium_hub>

```
$ docker run --privileged -d -p 4723:4723 -e CONNECT_TO_GRID=true -e APPIUM_HOST="127.0.0.1" -e APPIUM_PORT=4723 -e SELENIUM_HOST="172.17.0.1" -e SELENIUM_PORT=4444 -v /dev/bus/usb:/dev/bus/usb --name container-appium appium/appium
```

### 自定义节点配置

该图像会生成节点配置文件，如果您想提供自己的配置，请传递以下参数：

- CONNECT_TO_GRID =真
- CUSTOM_NODE_CONFIG =真
- -v <path_to_config>：/ root / nodeconfig.json

### 轻松的安全

传递环境变量RELAXED_SECURITY = true以禁用其他安全检查以使用某些高级功能。

### Docker撰写

有[一个组合文件的例子](https://github.com/appium/appium-docker-android/blob/master/examples/docker-compose.yml)来模拟Docker解决方案中连接的设备与Selenium Hub和Appium服务器之间的连接。

```
$ docker-compose up -d
```

 