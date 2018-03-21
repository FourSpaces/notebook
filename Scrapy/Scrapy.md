3. 学习资料

接触 Scrapy，是因为想爬取一些知乎的数据，最开始的时候搜索了一些相关的资料和别人的实现方式。

Github 上已经有人或多或少的实现了对知乎数据的爬取，我搜索到的有以下几个仓库：

    https://github.com/KeithYue/Zhihu_Spider 实现先通过用户名和密码登陆再爬取数据，代码见 zhihu_spider.py。
    https://github.com/immzz/zhihu-scrapy 使用 selenium 下载和执行 javascript 代码。
    https://github.com/tangerinewhite32/zhihu-stat-py
    https://github.com/Zcc/zhihu 主要是爬指定话题的topanswers，还有用户个人资料，添加了登录代码。
    https://github.com/pelick/VerticleSearchEngine 基于爬取的学术资源，提供搜索、推荐、可视化、分享四块。使用了 Scrapy、MongoDB、Apache Lucene/Solr、Apache Tika等技术。
    https://github.com/geekan/scrapy-examples scrapy的一些例子，包括获取豆瓣数据、linkedin、腾讯招聘数据等例子。
    https://github.com/owengbs/deeplearning 实现分页获取话题。
    https://github.com/gnemoug/distribute_crawler 使用scrapy、redis、mongodb、graphite实现的一个分布式网络爬虫,底层存储mongodb集群,分布式使用redis实现,爬虫状态显示使用graphite实现
    https://github.com/weizetao/spider-roach 一个分布式定向抓取集群的简单实现。

其他资料：

    http://www.52ml.net/tags/Scrapy 收集了很多关于 Scrapy 的文章，推荐阅读
    用Python Requests抓取知乎用户信息
    使用scrapy框架爬取自己的博文
    Scrapy 深入一点点
    使用python，scrapy写（定制）爬虫的经验，资料，杂。
    Scrapy 轻松定制网络爬虫
    在scrapy中怎么让Spider自动去抓取豆瓣小组页面

scrapy 和 JavaScript 交互例子：

    用scrapy框架爬取js交互式表格数据
    scrapy + selenium 解析javascript 实例

还有一些待整理的知识点：

    如何先登陆再爬数据
    如何使用规则做过滤
    如何递归爬取数据
    scrapy的参数设置和优化
    如何实现分布式爬取


# scrapy 读文档记录

##  Selector有四个基本的方法(点击相应的方法可以看到详细的API文档):

```
xpath(): 传入xpath表达式，返回该表达式所对应的所有节点的selector list列表 。
css(): 传入CSS表达式，返回该表达式所对应的所有节点的selector list列表.
extract(): 序列化该节点为unicode字符串并返回list。
re(): 根据传入的正则表达式对数据进行提取，返回unicode字符串list列表。

```

每个 .xpath() 调用返回selector组成的list，因此我们可以拼接更多的 .xpath() 来进一步获取某个节点。

嵌套选择器(selectors) 
```
for sel in response.xpath('//ul/li'):
    title = sel.xpath('a/text()').extract()
    link = sel.xpath('a/@href').extract()
    desc = sel.xpath('text()').extract()
    print title, link, desc

```

## 
Scrpay的追踪链接的机制: 当您在回调函数中yield一个Request后, Scrpay将会调度,发送该请求,并且在该请求完成时,调用所注册的回调函数。

##  保持抓取到的数据
需要对爬取到的item做更多更为复杂的操作，您可以编写 Item Pipeline 。
```
scrapy crawl dmoz -o items.json

```

## 命令行工具
Scrapy 会通过读取环境变量来设置

SCRAPY_SETTINGS_MODULE
SCRAPY_PROJECT

## 
scrapy.cfg 存放的目录被认为是 项目的根目录 
```
scrapy startproject myproject  #创建Scrapy项目 myproject

scrapy genspider mydomain mydomain.com  #创建spider 

```
## 全局命令 
startproject
：scrapy startproject <project_name>
：在 project_name 文件夹下创建一个名为 project_name 的Scrapy项目。

settings
runspider
shell
fetch
view
version

## 项目(Project-only)命令
crawl , scrapy crawl <spider>  ,  运行爬虫
check ，scrapy check [-l] <spider>  ， 运行 contract 检查
list  ，scrapy list  ,  列出当前项目中所有可用的spider
edit  , scrapy edit <spider> , 使用 EDITOR 中设定的编辑器编辑给定的spider
parse , scrapy parse <url> [options] , 获取给定的URL并使用相应的spider分析处理。
genspider 创建spider

bench

## 运行参数
Spider参数通过使用-a选项的crawl命令传递。 例如：
```
scrapy crawl myspider -a category=electronics
```
```
import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'

    def __init__(self, category=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.example.com/categories/%s' % category]
        # ...
```

pylint zaoshu.py |less


