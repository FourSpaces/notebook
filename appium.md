### 一般能力

这些功能涵盖多个驱动程序。

| 能力                           | 描述                                                         | 值                                                           |
| ------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `automationName`               | 使用哪种自动化引擎                                           | `Appium`（默认）或`Selendroid`或`UiAutomator2`或`Espresso`用于Android或`XCUITest`iOS或`YouiEngine`用于使用You.i Engine构建的应用程序 |
| `platformName`                 | 使用哪个移动OS平台                                           | `iOS`，`Android`或`FirefoxOS`                                |
| `platformVersion`              | 移动OS版本                                                   | 例如`7.1`，`4.4`                                             |
| `deviceName`                   | 要使用的移动设备或模拟器的种类                               | `iPhone Simulator`，`iPad Simulator`，`iPhone Retina 4-inch`，`Android Emulator`，`Galaxy S4`，等....在iOS上，这应该是与仪器返回的有效设备之一`instruments -s devices`。在Android上，此功能目前被忽略，但仍然需要。 |
| `app`                          | 绝对本地路径*或*远程http URL到`.ipa`文件（IOS），`.app`文件夹（IOS模拟器），`.apk`文件（Android）或`.apks`文件（Android App Bundle），或`.zip`包含其中一个的文件（对于.app，.app文件夹必须是zip文件的根目录）。Appium将首先尝试在适当的设备上安装此应用程序二进制文件。请注意，如果您指定`appPackage`和`appActivity`功能，则Android不需要此功能（请参阅下文）。与...不相容`browserName`。请看[这里](https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/android/android-appbundle.md)有关`.apks`文件。 | `/abs/path/to/my.apk` 要么`http://myapp.com/app.ipa`         |
| `browserName`                  | 要自动化的移动Web浏览器的名称。如果自动化应用程序，则应为空字符串。 | 适用于iOS的“Safari”和适用于Android的“Chrome”，“Chromium”或“浏览器” |
| `newCommandTimeout`            | 在假设客户端退出并结束会话之前，Appium将等待来自客户端的新命令多长时间（以秒为单位） | 例如 `60`                                                    |
| `language`                     | 为iOS和Android设置的语言。它仅适用于iOS上的模拟器            | 例如 `fr`                                                    |
| `locale`                       | 为iOS和Android设置的区域设置。它仅适用于iOS上的模拟器。`fr_CA`iOS格式。`CA`Android格式（国家/地区名称缩写） | 例如`fr_CA`，`CA`                                            |
| `udid`                         | 连接的物理设备的唯一设备标识符                               | 例如 `1ae203187fc012g`                                       |
| `orientation`                  | （仅限Sim / Emu）以某个方向开始                              | `LANDSCAPE` 要么 `PORTRAIT`                                  |
| `autoWebview`                  | 直接进入Webview上下文。默认`false`                           | `true`， `false`                                             |
| `noReset`                      | 请勿在此会话之前重置应用程序状态。有关详细信息，请参见[此处](https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/other/reset-strategies.md) | `true`， `false`                                             |
| `fullReset`                    | 执行完全重置。有关详细信息，请参见[此处](https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/other/reset-strategies.md) | `true`， `false`                                             |
| `eventTimings`                 | 启用或禁用各种Appium内部事件的时间报告（例如，每个命令的开始和结束等）。默认为`false`。要启用，请使用`true`。然后，`events`在响应查询当前会话时，将时间报告为属性。请参阅[事件计时文档](https://github.com/appium/appium/blob/master/docs/en/advanced-concepts/event-timings.md)以了解此响应的结构。 | 例如， `true`                                                |
| `enablePerformanceLogging`     | （仅限Web和webview）启用Chromedriver（在Android上）或Safari（在iOS上）性能记录（默认`false`） | `true`， `false`                                             |
| `printPageSourceOnFindFailure` | 当查找操作失败时，打印当前页面源。默认为`false`。            | 例如， `true`                                                |

###  



### Android仅限

这些功能仅适用于基于Android的驱动程序（例如 [UiAutomator2](https://github.com/appium/appium/blob/master/docs/en/drivers/android-uiautomator2.md)）。

| 能力                              | 描述                                                         | 值                                                           |
| --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `appActivity`                     | 要从程序包启动的Android活动的活动名称。这通常需要在`.`（例如，`.MainActivity`代替`MainActivity`）之前。默认情况下，从包清单中收到此功能（action：android.intent.action.MAIN，category：android.intent.category.LAUNCHER） | `MainActivity`， `.Settings`                                 |
| `appPackage`                      | 您要运行的Android应用程序的Java包。默认情况下，从包清单（@package属性值）接收此功能 | `com.example.android.myApp`， `com.android.settings`         |
| `appWaitActivity`                 | 活动名称/名称，逗号分隔，用于您要等待的Android活动。默认情况下，此功能的值与for相同`appActivity`。您必须将它设置为第一个专注的应用程序活动名称，以防它与设置的名称不同，就`appActivity`好像您的功能具有`appActivity`和`appPackage`。 | `SplashActivity`，`SplashActivity,OtherActivity`，`*`，`*.SplashActivity` |
| `appWaitPackage`                  | 您要等待的Android应用程序的Java包。默认情况下，此功能的值与for相同`appActivity` | `com.example.android.myApp`， `com.android.settings`         |
| `appWaitDuration`                 | 用于等待appWaitActivity启动的超时（以毫秒为单位`20000`）（默认） | `30000`                                                      |
| `deviceReadyTimeout`              | 等待设备准备就绪时超时（以秒为单位）                         | `5`                                                          |
| `allowTestPackages`               | 允许安装`android:testOnly="true"`清单中的测试包。`false`默认情况下 | `true` 要么 `false`                                          |
| `androidCoverage`                 | 完全合格的仪器课程。在adb shell中传递给-w是仪器-e覆盖真实-w  | `com.my.Pkg/com.my.Pkg.instrumentation.MyInstrumentation`    |
| `androidCoverageEndIntent`        | 您自己实施的广播操作，用于将覆盖范围转储到文件系统中。传递给-a adb shell am -a | `com.example.pkg.END_EMMA`                                   |
| `androidDeviceReadyTimeout`       | 用于等待设备在引导后准备就绪的超时秒数                       | 例如， `30`                                                  |
| `androidInstallTimeout`           | 用于等待apk安装到设备的超时（以毫秒为单位）。默认为`90000`   | 例如， `90000`                                               |
| `androidInstallPath`              | 安装前将推送apk的设备上的目录名称。默认为`/data/local/tmp`   | 例如 `/sdcard/Downloads/`                                    |
| `adbPort`                         | 用于连接到ADB服务器的端口（默认`5037`）                      | `5037`                                                       |
| `systemPort`                      | `systemPort`用于连接[appium-uiautomator2-server](https://github.com/appium/appium-uiautomator2-server)或[appium-espresso-driver](https://github.com/appium/appium-espresso-driver)。默认值是`8200`一般和选择一个端口`8200`，以`8299`用于*appium-uiautomator2服务器*，它是`8300`来自`8300`于`8399`对*appium-咖啡驱动器*。并行运行测试时，必须调整端口以避免冲突。阅读[并行测试设置指南](https://github.com/appium/appium/blob/master/docs/en/advanced-concepts/parallel-tests.md#parallel-android-tests)了解更多详情。 | 例如， `8201`                                                |
| `remoteAdbHost`                   | 可选的远程ADB服务器主机                                      | 例如：192.168.0.101                                          |
| `androidDeviceSocket`             | Devtools套接字名称。仅在测试的应用程序是Chromium嵌入浏览器时才需要。套接字由浏览器打开，Chromedriver作为devtools客户端连接到它。 | 例如， `chrome_devtools_remote`                              |
| `avd`                             | 要发布的avd的名称                                            | 例如， `api19`                                               |
| `avdLaunchTimeout`                | avd启动并连接到ADB需要等待多长时间（默认`60000`）            | `300000`                                                     |
| `avdReadyTimeout`                 | avd完成启动动画需要等待多长时间（默认`120000`）              | `300000`                                                     |
| `avdArgs`                         | 启动avd时使用的其他模拟器参数                                | 例如， `-netfast`                                            |
| `useKeystore`                     | 默认情况下，使用自定义密钥库对apks进行签名`false`            | `true` 要么 `false`                                          |
| `keystorePath`                    | 自定义密钥库的路径，默认为〜/ .android / debug.keystore      | 例如， `/path/to.keystore`                                   |
| `keystorePassword`                | 自定义密钥库的密码                                           | 例如， `foo`                                                 |
| `keyAlias`                        | 密钥的别名                                                   | 例如， `androiddebugkey`                                     |
| `keyPassword`                     | 密钥密码                                                     | 例如， `foo`                                                 |
| `chromedriverExecutable`          | webdriver可执行文件的绝对本地路径（如果Chromium embedder提供自己的webdriver，则应该使用它而不是与Appium捆绑的原始chromedriver） | `/abs/path/to/webdriver`                                     |
| `chromedriverExecutableDir`       | 查找Chromedriver可执行文件的目录的绝对路径，用于自动发现兼容的Chromedrivers。如果`chromedriverUseSystemExecutable`是，则忽略`true` | `/abs/path/to/chromedriver/directory`                        |
| `chromedriverChromeMappingFile`   | 文件的绝对路径，将Chromedriver版本映射到它支持的最小Chrome。如果`chromedriverUseSystemExecutable`是，则忽略`true` | `/abs/path/to/mapping.json`                                  |
| `chromedriverUseSystemExecutable` | 如果`true`，绕过自动Chromedriver配置并使用随Appium下载的版本。如果`chromedriverExecutable`已设置则忽略。默认为`false` | 例如， `true`                                                |
| `autoWebviewTimeout`              | 等待Webview上下文变为活动状态的时间（以毫秒为单位）。默认为`2000` | 例如 `4`                                                     |
| `intentAction`                    | 将用于启动活动的意图操作（默认`android.intent.action.MAIN`） | 例如`android.intent.action.MAIN`，`android.intent.action.VIEW` |
| `intentCategory`                  | 将用于启动活动的意图类别（默认`android.intent.category.LAUNCHER`） | 例如`android.intent.category.LAUNCHER`，`android.intent.category.APP_CONTACTS` |
| `intentFlags`                     | 将用于启动活动的标志（默认`0x10200000`）                     | 例如 `0x10200000`                                            |
| `optionalIntentArguments`         | 将用于启动活动的其他意图参数。请参阅[Intent参数](http://developer.android.com/reference/android/content/Intent.html) | 例如`--esn <EXTRA_KEY>`，`--ez <EXTRA_KEY> <EXTRA_BOOLEAN_VALUE>`等等。 |
| `dontStopAppOnReset`              | 在使用adb启动应用程序之前，不会停止正在测试的应用程序的进程。如果被测试的应用程序是由另一个锚点应用程序创建的，则将此设置为false将允许锚点应用程序的进程在使用adb的测试应用程序启动期间保持活动状态。换句话说，如果`dontStopAppOnReset`设置为`true`，我们将不会`-S`在`adb shell am start`调用中包含该标志。在省略或设置此功能的情况下`false`，我们包含该`-S`标志。默认`false` | `true` 要么 `false`                                          |
| `unicodeKeyboard`                 | 启用Unicode输入，默认 `false`                                | `true` 要么 `false`                                          |
| `resetKeyboard`                   | 在运行具有`unicodeKeyboard`功能的Unicode测试后，将键盘重置为其原始状态。如果单独使用则忽略。默认`false` | `true` 要么 `false`                                          |
| `noSign`                          | 使用调试键跳过检查和签名应用程序，仅适用于UiAutomator，而不适用于selendroid，默认`false` | `true` 要么 `false`                                          |
| `ignoreUnimportantViews`          | 调用`setCompressedLayoutHierarchy()`uiautomator函数。此功能可以加快测试执行速度，因为Accessibility命令将更快地运行而忽略某些元素。忽略的元素将无法找到，这就是为什么此功能也被实现为可切换的*设置*和功能。默认为`false` | `true` 要么 `false`                                          |
| `disableAndroidWatchers`          | 禁用监视应用程序没有响应和应用程序崩溃的android观察者，这将减少Android设备/模拟器上的CPU使用率。此功能仅适用于UiAutomator，而不适用于selendroid，默认情况下`false` | `true` 要么 `false`                                          |
| `chromeOptions`                   | 允许为ChromeDriver传递chromeOptions功能。有关更多信息，请参阅[chromeOptions](https://sites.google.com/a/chromium.org/chromedriver/capabilities) | `chromeOptions: {args: ['--disable-popup-blocking']}`        |
| `recreateChromeDriverSessions`    | 移至非ChromeDriver webview时，请终止ChromeDriver会话。默认为`false` | `true` 要么 `false`                                          |
| `nativeWebScreenshot`             | 在网络环境中，使用原生（adb）方法截取屏幕截图，而不是代理ChromeDriver。默认为`false` | `true` 要么 `false`                                          |
| `androidScreenshotPath`           | 将放置屏幕截图的设备上的目录名称。默认为`/data/local/tmp`    | 例如 `/sdcard/screenshots/`                                  |
| `autoGrantPermissions`            | 让Appium自动确定您的应用所需的权限，并在安装时将其授予应用。默认为`false`。如果`noReset`是`true`，则此功能不起作用。 | `true` 要么 `false`                                          |
| `networkSpeed`                    | 设置网络速度仿真。指定最大网络上载和下载速度。默认为`full`   | `['full','gsm', 'edge', 'hscsd', 'gprs', 'umts', 'hsdpa', 'lte', 'evdo']`检查[-netspeed选项](https://developer.android.com/studio/run/emulator-commandline.html)有关avds的速度仿真的更多信息 |
| `gpsEnabled`                      | 在开始会话之前切换模拟器的gps位置提供程序。默认情况下，仿真器将根据其配置方式启用或不启用此选项。 | `true` 要么 `false`                                          |
| `isHeadless`                      | 设置此功能，`true`以便在不需要显示设备显示时运行仿真器无头。`false`是默认值。*isHeadless*也支持iOS，检查特定于XCUITest的功能。 | 例如， `true`                                                |
| `otherApps`                       | 在运行测试之前要安装的应用程序或应用程序列表（作为JSON数组） | 例如`"/path/to/app.apk"`，`https://www.example.com/url/to/app.apk`，`["/path/to/app-a.apk", "/path/to/app-b.apk"]` |
| `adbExecTimeout`                  | 用于等待adb命令执行的超时（以毫秒为单位）。默认为`20000`     | 例如， `50000`                                               |
| `localeScript`                    | 设置区域设置[脚本](https://developer.android.com/reference/java/util/Locale) | 例如，` "Cyrl"`（西里尔文）                                  |
| `skipDeviceInitialization`        | 跳过设备初始化，其中包括：安装和运行设置应用或设置权限。当设备已用于自动化并且为下一次自动化做好准备时，可用于提高启动性能。默认为`false` | `true` 要么 `false`                                          |
| `chromedriverDisableBuildCheck`   | 设置`--disable-build-check`Chrome webview测试的chromedriver标志 | `true` 要么 `false`                                          |
| `skipUnlock`                      | 在会话创建期间跳过解锁。默认为`false`                        | `true` 要么 `false`                                          |
| `unlockType`                      | 使用特定锁定模式解锁目标设备，而不是仅使用帮助应用程序唤醒设备。它具有`unlockKey`功能。默认为未定义。`fingerprint`仅适用于Android 6.0+和模拟器。在android驱动程序中读取[解锁文档](https://github.com/appium/appium-android-driver/blob/master/docs/UNLOCK.md)。 | `['pin', 'password', 'pattern', 'fingerprint']`              |
| `unlockKey`                       | 要解锁的关键模式`unlockType`。                               | 例如，'1111'                                                 |

####  

#### 仅限UIAutomator2

这些功能仅在[UiAutomator2驱动程序](https://github.com/appium/appium/blob/master/docs/en/drivers/android-uiautomator2.md)上可用

| 能力                               | 描述                                                         | 值                |
| ---------------------------------- | ------------------------------------------------------------ | ----------------- |
| `uiautomator2ServerLaunchTimeout`  | 用于等待uiAutomator2服务器启动的超时（以毫秒为单位）。默认为`20000` | 例如，`20000`     |
| `uiautomator2ServerInstallTimeout` | 用于等待安装uiAutomator2服务器的超时（以毫秒为单位）。默认为`20000` | 例如，`20000`     |
| `skipServerInstallation`           | 跳过uiAutomator2服务器安装并从设备使用uiAutomator2服务器。当设备上已安装适当版本的uiAutomator2服务器时，可用于提高启动性能。默认为`false` | `true`要么`false` |

#### 仅限浓缩咖啡

这些功能仅适用于[Espresso驱动程序](https://github.com/appium/appium/blob/master/docs/en/drivers/android-espresso.md)

| 能力                          | 描述                                                         | 值             |
| ----------------------------- | ------------------------------------------------------------ | -------------- |
| `espressoServerLaunchTimeout` | 用于等待espresso服务器启动的超时（以毫秒为单位）。默认为`30000` | 例如， `50000` |

###  