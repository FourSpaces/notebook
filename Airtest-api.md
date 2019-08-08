## Airtest-api



常用的函数

```
stop_app("com.meta.xyx")   # 关闭 包名为 "com.meta.xyx"的 app
start_app("com.meta.xyx")	# 打开 包名为 "com.meta.xyx"的 app

sleep(16)	# 暂停等待 16 秒

device().get_top_activity()		# 返回当前置顶的包名、活动名称
print(device().get_top_activity())	# 输出 返回的当前置顶的包名、活动名称

```



s