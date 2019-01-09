# scrapy_zs  项目手册

###  项目启动流程

####  第一步、clone自己的项目
`git clone git@github.com:zaoshu/XXXXX.git`

#### 第二步、添加scrapy_zs 源
`git remote add scrapy_zs git@github.com:zaoshu/scrapy_zs.git`

#### 第三步、拉取模板代码
`git fetch scrapy_zs`

#### 第四步、将模板代码合并到当前分支

`git merge scrapy_zs/master`

#### 第五步、第一次上传代码
```bush
git add filename （若有多个文件，以空格分开）
git commit -m '第一次提交'
git push origin develop
```
### 一些常见情况
- 向git提交代码依然和第五步一样
- 当`scrapy_zs`更新时，需要使用第三步、第四步合并代码
- 如果出现冲突应该解决冲突，`git checkout filename`

---
### 项目部署

1. 切换至 `develop` 分支
2. 在 `README.md` 文件中说明爬虫需要的配置参数
3. 生成 CI 配置
> 1. 需要上线爬虫时，请运行根目录下的 `build_deployment_config.py` 脚本。
> 2. 脚本将在根目录生成 .circleci, .tools, 文件夹 和 .gitignore, Dockerfile, Makefile, requirements.txt 文件
> 3. 文件都已配好，还需要向 `requirements.txt` 中添加**你需要的用到模块**，构建镜像的时候会自动安装。
配置完成的项目结构如下图所示：

![CI配置完成图](https://raw.githubusercontent.com/BuleAnt/RepositoryResources/master/image/RecommendationMovie/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202018-03-23%20%E4%B8%8B%E5%8D%887.14.22.png)

- 找 @钱登胜 开通github repo，添加相关人员
- 提交代码
- 找 @钱登胜 开通服务器及数据库资源
- 找 @钱登胜 或者 @徐缓 配置 CircleCI
- 部署完成后检查爬虫是否正常运行


## 未知BUG，一定要来看这里

1. **不能改变已有目录名称和目录结构**，但是可以添加文件和目录，所有有标注的地方请勿占用（不然要自行解决冲突）
2. 所有的scrapy的相关配置请使用 `scrapy_zs/scrapy_zs/utils/spider_utils.py` 中的 `CustomSettings`类进行配置
3. 请勿修改 `scrapy_zs/scrapy_zs/utils` 目录下的任何东西。此目录为所有公用工具代码目录，
4. 如果第四步merge出现错误：`fatal: refusing to merge unrelated histories`，是Git版本问题，可以使用 `git merge scrapy_zs/master --allow-unrelated-histories`
5. ​

## 丰富scrapy_zs 项目内容
- 如果要修改或添加更多公用方法，请去 `scrapy_zs/dev`上开发，经过lc确定，然后在合并到所有项目中。



## 默认配置与建议

- 关于自定义 `PIPELINES`、`MIDDLEWARES` 的数值问题，建议大于200。因为默认的储存原始html管道数值是 `200`，默认的代理中间件数值是`520`，默认的启动日志监控数值是`520`
- 关于分布式，默认使用的是 `scrapy_redis` 的队列和去重，同时使用 `Redis`的 `set`类型: `REDIS_START_URLS_AS_SET = True`。所以如果你想传递 `start_urls`，一定记得使用 `sadd`
- 日志默认`INFO`级别




## 目前已经有的功能

### 1.自定义配置
配置结构：
	- 带 CUS_ 前缀的配置，是基于scrapy原始配置信息，添加了前缀，表示一样的效果
	- 带 En 前缀的配置，是scrapy_zs 项目增加配置，具体解释见下表 
	
CUS_ 前缀的配置信息参考[scrapy手册](http://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/settings.html)

> **CUS_ITEM_PIPELINES** 
>
> 保存项目中启用的pipeline及其顺序的字典, 默认添加了 日志监控、保存Html、系统集成 管道。 建议添加新的管道信息时，采用update() 进行更新，不要直接覆盖。例子见下面代码

> **CUS_SPIDER_MIDDLEWARES**
保存项目中启用的下载中间件及其顺序的字典，默认为空。例子见下面代码

> **CUS_DOWNLOADER_MIDDLEWARES**
保存项目中启用的下载中间件及其顺序的字典。默认添加了 代理中间件。

> **CUS_DOWNLOAD_DELAY**
下载器在下载同一个网站下一个页面前需要等待的时间。默认为0

> **CUS_CONCURRENT_REQUESTS_PER_DOMAIN**
对单个网站进行并发请求的最大值。默认为16

> **CUS_CONCURRENT_REQUESTS_PER_IP**
对单个IP进行并发请求的最大值。默认为16

> **CUS_CONCURRENT_REQUESTS**
Scrapy downloader 并发请求(concurrent requests)的最大值，默认为16

> **CUS_DOWNLOAD_TIMEOUT**
下载器超时时间，默认为10，单位(秒)

> **CUS_TIMEOUT**

> **CUS_COOKIES_ENABLED**
是否启用Cookie中间件。如果禁用，则不会将Cookie发送到Web服务器。默认为0

> **CUS_COOKIES_DEBUG**
如果启用，Scrapy会记录在请求中发送的所有Cookie（即Cookie头文件）以及在响应中收到的所有Cookie（即Set-Cookie头文件），默认为 0

> **CUS_RETRY_ENABLED**
是否启用重试中间件， 默认为0 

> **CUS_RETRY_HTTP_CODES**
> 重试的http请求返回值(code)。其他错误(DNS查找问题、连接失败及其他)则一定会进行重试。
> 默认为空

> **CUS_RETRY_TIMES**
重试最大次数，默认为16

> **CUS_RETRY_PRIORITY_ADJUST**
调整相对于原始请求的重试请求优先级：
	- 负数优先级调整（默认）意味着较低的优先级。
	- 正数调整意味着更高的优先级。

> **CUS_TMP_MONGODB_DB_NAME**

> **CUS_SCHEDULER**
用于爬取的调度器。

> **CUS_DUPEFILTER_CLAS**S
用于检测过滤重复请求的类，过滤器

> **CUS_SCHEDULER_QUEUE_CLASS**
>
> 请求调度使用优先队列
==================

> **CUS_REDIS_START_URLS_AS_SET**
如果需要避免起始网址列表出现重复，将CUS_REDIS_START_URLS_AS_SET设置为True，开启此选项urls必须通过sadd添加，否则会出现类型错误。

> **CUS_REDIS_ITEMS_KEY**
序列化项目管道作为redis Key存储

> **CUS_REDIS_ITEMS_SERIALIZER**
？默认使用ScrapyJSONEncoder进行项目序列化

> **CUS_REDIS_START_URLS_KEY**
RedisSpider和RedisCrawlSpider默认 start_usls 键

> **CUS_SCHEDULER_IDLE_BEFORE_CLOSE**
最大空闲时间防止分布式爬虫因为等待而关闭

> **CUS_SCHEDULER_PERSIST**
不清除Redis队列、这样可以暂停/恢复 爬取

> **CUS_LOG_MONITOR_TIME**

> **CUS_LOG_LEVEL** 
记录的最低级别。可用的级别是：CRITICAL, ERROR, WARNING, INFO, DEBUG.

> **CUS_LOG_FILE**
用于记录输出的文件名。

> **CUS_SAVE_HTML_DB**
保存HTML的MongoDb链接

> **CUS_RANDOM_UA_TYPE**
随机User Agent 类型

> **EnRedis**
是否启用Redis

> **EnRedisReduceMemory**
是否启用 Redis 内存压缩

> **EnProxy**
是否启用代理

> **EnLogMonitor**
是否启用日志监视器

> **EnSaveHtml**
是否保存html

> **EnFakeUserAgent**
启用 伪装UserAgent






文件：`scrapy_zs/scrapy_zs/utils/spider_utils.py`

用法：

```python
from ..utils.spider_utils import CustomSettings

c = CustomSettings()
c.CUS_DOWNLOAD_DELAY = 63
custom_settings = c()
```



### 2.启动代理中间件（默认打开）

文件：`scrapy_zs/scrapy_zs/utils/spider_utils.py`

用法：

```python
from ..utils.spider_utils import CustomSettings

c = CustomSettings()
c.EnProxy = True
custom_settings = c()
```

### 3.保存所有html/调用父类爬虫

文件：`scrapy_zs/scrapy_zs/utils/crawl.py`

用法：

```python
from ..utils.crawl import Spider

class GaodeSpider(Spider):
    name = 'gaode_spider'
	...
```

>共有4种不同的类，对应不同的爬虫，`Spider、CrawlSpider、SpiderRedis、CrawlSpiderRedis`

**注意**： 所有爬虫需要从 `crawl.py`中继承父类，保存html的功能已经自动打开，保存的表名为 `allowed_domains` 的第一个字符串，例如

`allowed_domains = ['iqiyi.com']` 表名为 `iqiyi`

代码为：

```python
db_name = spider.allowed_domains[0].split('.')[0]
```
>你可以选择你想要保存 html 的表名，用法 `c.CUS_SAVE_HTML_DB = iqiyi`

### 4.redis分布式爬虫

文件：`scrapy_zs/scrapy_zs/utils/spider_utils.py`

用法：

```python
from ..utils.spider_utils import CustomSettings

c = CustomSettings()
c.EnRedis = True
custom_settings = c()
```

### 5.集成参数设置

所有爬虫需要配置的参数都已经写好，文件：`scrapy_zs/scrapy_zs/utils/settings_.py`

用法：已经自动设置好，上线需要登登在在环境变量中配置好。



### 6.Mongo 和 Redis 客户端

在目录 `scrapy_zs/scrapy_zs/scrapy_zs/utils/` 下，有两个文件：`connection_mongodb.py`和 `connection_redis.py`，分别是Mongo与Redis的客户端，有需要直接从此导入，无需再实例化。

```python
from .utils.connection_mongodb import mongodb_client
from .utils.connection_redis import redis_client

```
**Mongo 基类**，用法：`from .utils.pipelines_ import MongodbPipeline as MP`

```python
class MongodbPipeline(object):
    collection_name_list = {}

    def __init__(self, mongo_db):
        self.mongodb = mongo_db
        self.client = None
        self.db = None

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         mongo_db=crawler.settings.get('MONGODB_DATABASE', 'iqiyi')
    #     )

    def open_spider(self, spider):
        _ = spider
        self.client = mongodb_client
        self.db = self.client[self.mongodb]

    def close_spider(self, spider):
        _ = spider
        self.client.close()

    def create_index(self):
        for collection_name, v in self.collection_name_list.items():

            for k, k_type in v:
                if k_type == 'unique':
                    self.db[collection_name].ensure_index(k, unique=True)
                else:
                    self.db[collection_name].ensure_index(k)

```

### 7.随机更换 UserAgent

默认已经打开 UserAgent，若要关闭，可以：`c.EnFakeUserAgent = False`，还可以选择对应的浏览器类别，例如：`c.CUS_RANDOM_UA_TYPE = 'google'`。(目前没有移动端)

该类继承`fake_useragent`，其用法如下
```python
from fake_useragent import UserAgent
ua = UserAgent()

ua.chrome
# Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
ua.google
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13
ua['google chrome']
# Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11
ua.firefox

# and the best one, random via real world browser usage statistic
ua.random
```



# 约定

1. 匹配代码和爬虫文件分开写，匹配文件目录是`scrapy_zs/scrapy_zs/parse/`，爬虫文件目录是`scrapy_zs/scrapy_zs/spiders/`
2. **目录`scrapy_zs/scrapy_zs/scrapy_zs/utils/`下所有文件不允许任何改变**，`scrapy_zs/doc/`为使用说明，`scrapy_zs/example/`为示例代码
3. 详细注释，每个函数指明 `param`及 `return`
4. git commit 规范
```
feat     (新功能)
fix      (问题修复)
refactor (代码重构)
style    (代码风格改动、格式变化等，无实现改动)
docs     (文档更新)
test     (增加、重构测试，无实现改动)
chore    (修改一些配置文件如 .gitignore 等，无实现改动)
```

---

小提示：使用 [pigar](https://github.com/damnever/pigar) 可以一键生成 `requirements.txt` 文件

Installation：`pip install pigar`

Usage：`pigar` 

![](https://raw.githubusercontent.com/Damnever/pigar/master/short-guide.gif)

---
22

# 目前存在的问题，
配置目录默认配置不全，如何将动态将信息配置到配置类中。