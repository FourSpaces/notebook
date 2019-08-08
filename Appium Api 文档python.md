# Appium Api 文档python



## Status

检索服务器的当前状态

```
selenium.webdriver.common.utils.is_url_connectable(port)

```



## 执行手机 命令
执行一个原生手机命令
```
self.driver.execute_script("mobile: scroll", {'direction': 'down'})

```

## Session
### 创建
创建一个新会话
```
desired_caps = desired_caps = {
  'platformName': 'Android',
  'platformVersion': '7.0',
  'deviceName': 'Android Emulator',
  'automationName': 'UiAutomator2',
  'app': PATH('/path/to/app')
}
self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

```

### 结束
结束正在运行的会话
```
self.driver.quit() 。
```

### 获得会话功能
检索指定会话的功能
```
desired_caps = self.driver.desired_capabilities()
```

### 上一页
如果可能，在浏览器历史记录中向后导航（仅限Web上下文）
```
self.driver.back()
```

### 截图
获取当前视口/窗口/页面的屏幕截图
```
screenshotBase64 = self.driver.get_screenshot_as_base64()


```