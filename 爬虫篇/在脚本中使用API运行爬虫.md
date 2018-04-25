## 在脚本中使用API运行爬虫

除了常用的 `scrapy crawl` 来启动Scrapy，您也可以使用 [API](http://scrapy-chs.readthedocs.io/zh_CN/1.0/topics/api.html#topics-api) 在脚本中启动Scrapy。

需要注意的是，Scrapy是在Twisted异步网络库上构建的， 因此其必须在Twisted reactor里运行。

您可以使用的第一个实用程序来运行您的蜘蛛是scrapy.crawler.CrawlerProcess。 该类将为您启动一个Twisted反应器，配置日志记录和设置关闭处理程序。 这个类是所有Scrapy命令使用的类。

这是一个示例，显示如何运行单个蜘蛛。

```
import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider(scrapy.Spider):
    # Your spider definition
    ...

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MySpider)
process.start() # 该脚本将阻塞在此处，直到爬行完成
```

确保检查CrawlerProcess文档以了解其使用细节。

如果您在Scrapy项目中，还有一些额外的帮助者可以在项目中导入这些组件。 您可以自动导入将其名称传递给CrawlerProcess的蜘蛛，并使用get_project_settings获取具有项目设置的Settings实例。



下面给出了如何实现的例子，使用 [testspiders](https://github.com/scrapinghub/testspiders) 项目作为例子。

```
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

# 'followall' 是该项目的蜘蛛之一的名称。
process.crawl('testspider', domain='scrapinghub.com')
process.start() # 该脚本将阻止此处，直到爬行完成
```

还有一个Scrapy实用程序可以更好地控制爬网过程：scrapy.crawler.CrawlerRunner。 这个类是一个薄的封装，封装了一些简单的助手来运行多个爬虫，但它不会以任何方式启动或干扰现有的反应堆。

使用这个类后，应该在调度你的蜘蛛之后显式地运行反应器。 建议您使用CrawlerRunner而不是CrawlerProcess，如果您的应用程序已经使用Twisted，并且要在同一个反应器中运行Scrapy。

请注意，在蜘蛛完成后，您也必须自己关闭Twisted反应堆。 这可以通过向CrawlerRunner.crawl方法返回的延迟添加回调来实现。

以下是其使用示例，以及在MySpider完成运行后手动停止反应器的回调。



```
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

class MySpider(scrapy.Spider):
    # Your spider definition
    ...

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()

d = runner.crawl(MySpider)
d.addBoth(lambda _: reactor.stop())
reactor.run() # 该脚本将阻止此处，直到爬行完成
```