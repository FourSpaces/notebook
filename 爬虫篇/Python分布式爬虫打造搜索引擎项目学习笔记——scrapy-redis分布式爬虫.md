## Python分布式爬虫打造搜索引擎项目学习笔记——scrapy-redis分布式爬虫

** 发表于 2017-07-01 | ** 更新于 2017-07-03 | ** 分类于 [Scrapy ](http://lawtech0902.com/categories/Scrapy/)| ** | ** 阅读次数 144

[![img](https://ww4.sinaimg.cn/large/006tNc79gy1feirgm2h0lj31gi0ag0ve.jpg)](https://ww4.sinaimg.cn/large/006tNc79gy1feirgm2h0lj31gi0ag0ve.jpg)

## **分布式爬虫要点**

[![img](https://ws3.sinaimg.cn/large/006tNc79gy1fh4hbyf2moj30h50byq4t.jpg)](https://ws3.sinaimg.cn/large/006tNc79gy1fh4hbyf2moj30h50byq4t.jpg)

### **分布式爬虫的优点**

- 充分利用多机器的宽带加速爬取
- 充分利用多机的IP加速爬取速度

问题：**为什么scrapy不支持分布式？**

答：在scrapy中scheduler是运行在队列中的，而队列是在单机内存中的，服务器上爬虫是无法利用内存的队列做任何处理，所以scrapy不支持分布式。

### **分布式爬虫需要解决的问题**

- requests队列集中管理
- 去重集中管理

综上，我们需要使用Redis来解决这些问题。

## **Redis基础知识**

Redis的基础知识在我早前的文章中已经学习过了，在这里就不介绍了，直接看之前的文章就行。

传送门：[Redis学习笔记](http://lawtech0902.com/categories/Redis/)

## **scrapy-redis编写分布式爬虫代码**

传送门：1.[scapy-redis Github](https://github.com/rmax/scrapy-redis) 2.[scrapy-redis 文档](http://scrapy-redis.readthedocs.io/en/stable/)

其实大部分的逻辑是一样的，只需要在spider中加入`redis_key = 'spidername:start_urls'`，以及修改一些settings.py中配置即可。

## **scrapy-redis源码解析**

[![img](https://ws2.sinaimg.cn/large/006tNc79gy1fh5szm7gkpj30920bo0tq.jpg)](https://ws2.sinaimg.cn/large/006tNc79gy1fh5szm7gkpj30920bo0tq.jpg)

### **项目结构**

**connection.py**

负责根据setting中配置实例化redis连接。被dupefilter和scheduler调用，总之涉及到redis存取的都要使用到这个模块。

**dupefilter.py**

负责执行requst的去重，实现的很有技巧性，使用redis的set数据结构。但是注意scheduler并不使用其中用于在这个模块中实现的dupefilter键做request的调度，而是使用queue.py模块中实现的queue。

当request不重复时，将其存入到queue中，调度时将其弹出。

**queue.py**

其作用如II所述，但是这里实现了三种方式的queue：

FIFO的SpiderQueue，SpiderPriorityQueue，以及LIFI的SpiderStack。默认使用的是第二中，这也就是出现之前文章中所分析情况的原因（链接：）。

**pipelines.py**

这是是用来实现分布式处理的作用。它将Item存储在redis中以实现分布式处理。

另外可以发现，同样是编写pipelines，在这里的编码实现不同于文章（链接：）中所分析的情况，由于在这里需要读取配置，所以就用到了from_crawler()函数。

**scheduler.py**

此扩展是对scrapy中自带的scheduler的替代（在settings的SCHEDULER变量中指出），正是利用此扩展实现crawler的分布式调度。其利用的数据结构来自于queue中实现的数据结构。

scrapy-redis所实现的两种分布式：爬虫分布式以及item处理分布式就是由模块scheduler和模块pipelines实现。上述其它模块作为为二者辅助的功能模块。

**spider.py**

设计的这个spider从redis中读取要爬的url,然后执行爬取，若爬取过程中返回更多的url，那么继续进行直至所有的request完成。之后继续从redis中读取url，循环这个过程。

分析：在这个spider中通过connect signals.spider_idle信号实现对crawler状态的监视。当idle时，返回新的make_requests_from_url(url)给引擎，进而交给调度器调度。

### **架构解析**

Scrapy架构：

[![img](https://ws2.sinaimg.cn/large/006tNc79ly1fh5vaf92i0j30jk0ba0un.jpg)](https://ws2.sinaimg.cn/large/006tNc79ly1fh5vaf92i0j30jk0ba0un.jpg)

scrapy-redis架构：

[![img](https://ws1.sinaimg.cn/large/006tNc79gy1fh5v9jlr53j30j50b240g.jpg)](https://ws1.sinaimg.cn/large/006tNc79gy1fh5v9jlr53j30j50b240g.jpg)

如上图所示，scrapy-redis在scrapy的架构上增加了redis，基于redis的特性拓展了如下组件：

- 调度器（Scheduler）：scrapy-redis调度器通过redis的set不重复的特性，巧妙的实现了Duplication Filter去重（DupeFilter set存放爬取过的request）。Spider新生成的request，将request的指纹到redis的DupeFilter set检查是否重复，并将不重复的request push写入redis的request队列。调度器每次从redis的request队列里根据优先级pop出一个request, 将此request发给spider处理。
- Item Pipeline：将Spider爬取到的Item给scrapy-redis的Item Pipeline，将爬取到的Item存入redis的items队列。可以很方便的从items队列中提取item，从而实现items processes 集群

## **集成bloomfilter到scrapy-redis中**

传送门：[bloomfilter算法详解及实例](http://www.it610.com/article/4376832.htm)

算法实现：[bloomfilter_imooc](https://github.com/liyaopinner/BloomFilter_imooc)

`dupefilter.py`：

```
import logging
import time

from scrapy.dupefilters import BaseDupeFilter
from scrapy.utils.request import request_fingerprint

from . import defaults
from .connection import get_redis_from_settings
from ScrapyRedisTest.utils.bloomfilter import PyBloomFilter, conn

logger = logging.getLogger(__name__)


# TODO: Rename class to RedisDupeFilter.
class RFPDupeFilter(BaseDupeFilter):
    """Redis-based request duplicates filter.

    This class can also be used with default Scrapy's scheduler.

    """

    logger = logger

    def __init__(self, server, key, debug=False):
        """Initialize the duplicates filter.

        Parameters
        ----------
        server : redis.StrictRedis
            The redis server instance.
        key : str
            Redis key Where to store fingerprints.
        debug : bool, optional
            Whether to log filtered requests.

        """
        self.server = server
        self.key = key
        self.debug = debug
        self.logdupes = True

        self.bf = PyBloomFilter(conn=conn, key=key)

    @classmethod
    def from_settings(cls, settings):
        """Returns an instance from given settings.

        This uses by default the key ``dupefilter:<timestamp>``. When using the
        ``scrapy_redis.scheduler.Scheduler`` class, this method is not used as
        it needs to pass the spider name in the key.

        Parameters
        ----------
        settings : scrapy.settings.Settings

        Returns
        -------
        RFPDupeFilter
            A RFPDupeFilter instance.


        """
        server = get_redis_from_settings(settings)
        # XXX: This creates one-time key. needed to support to use this
        # class as standalone dupefilter with scrapy's default scheduler
        # if scrapy passes spider on open() method this wouldn't be needed
        # TODO: Use SCRAPY_JOB env as default and fallback to timestamp.
        key = defaults.DUPEFILTER_KEY % {'timestamp': int(time.time())}
        debug = settings.getbool('DUPEFILTER_DEBUG')
        return cls(server, key=key, debug=debug)

    @classmethod
    def from_crawler(cls, crawler):
        """Returns instance from crawler.

        Parameters
        ----------
        crawler : scrapy.crawler.Crawler

        Returns
        -------
        RFPDupeFilter
            Instance of RFPDupeFilter.

        """
        return cls.from_settings(crawler.settings)

    def request_seen(self, request):
        """Returns True if request was already seen.

        Parameters
        ----------
        request : scrapy.http.Request

        Returns
        -------
        bool

        """
        fp = self.request_fingerprint(request)

        if self.bf.is_exist(fp):
            return True
        else:
            self.bf.add(fp)
            return False
        # This returns the number of values added, zero if already exists.
        # added = self.server.sadd(self.key, fp)
        # return added == 0

    def request_fingerprint(self, request):
        """Returns a fingerprint for a given request.

        Parameters
        ----------
        request : scrapy.http.Request

        Returns
        -------
        str

        """
        return request_fingerprint(request)

    def close(self, reason=''):
        """Delete data on close. Called by Scrapy's scheduler.

        Parameters
        ----------
        reason : str, optional

        """
        self.clear()

    def clear(self):
        """Clears fingerprints data."""
        self.server.delete(self.key)

    def log(self, request, spider):
        """Logs given request.

        Parameters
        ----------
        request : scrapy.http.Request
        spider : scrapy.spiders.Spider

        """
        if self.debug:
            msg = "Filtered duplicate request: %(request)s"
            self.logger.debug(msg, {'request': request}, extra={'spider': spider})
        elif self.logdupes:
            msg = ("Filtered duplicate request %(request)s"
                   " - no more duplicates will be shown"
                   " (see DUPEFILTER_DEBUG to show all duplicates)")
            self.logger.debug(msg, {'request': request}, extra={'spider': spider})
            self.logdupes = False
```

[# Scrapy，Python，Redis](http://lawtech0902.com/tags/Scrapy%EF%BC%8CPython%EF%BC%8CRedis/)