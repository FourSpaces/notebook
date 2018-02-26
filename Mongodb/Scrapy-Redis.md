# Scrapy-Redis

Redis-based components for Scrapy.

- Free software: MIT license
- Documentation: [https://scrapy-redis.readthedocs.org](https://scrapy-redis.readthedocs.org/).
- Python versions: 2.7, 3.4+

## Features

- Distributed crawling/scraping

  > 您可以启动多个共享一个redis队列的spider实例。 最适合广泛的多域抓取。

- Distributed post-processing

  > Scraped项目被压入到redis队列中，这意味着你可以开始尽可能多的后处理进程共享项目队列。

- Scrapy plug-and-play components

  > 计划程序+复制过滤器，项目管道，基本蜘蛛。

## Requirements

- Python 2.7, 3.4 or 3.5
- Redis >= 2.8
- `Scrapy` >= 1.0
- `redis-py` >= 2.10

## Usage

在您的项目中使用以下设置：

```
# 修改scrapy默认的调度器为scrapy重写的调度器 启动从reids缓存读取队列调度爬虫
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 确保所有蜘蛛通过redis共享相同的重复过滤器。
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Default requests serializer is pickle, but it can be changed to any module
# with loads and dumps functions. Note that pickle is not compatible between
# python versions.
# Caveat: In python 3.x, the serializer must return strings keys and support
# bytes as values. Because of this reason the json or msgpack module will not
# work by default. In python 2.x there is no such issue and you can use
# 'json' or 'msgpack' as serializers.
#SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"

# 默认请求串行器是pickle，但是它可以被改变到任何模块
# 加载和转储功能。 请注意，泡菜之间不兼容
# python版本。
# 注意：在python 3.x中，序列化程序必须返回字符串键和支持
# 字节作为值。 因为这个原因，json或msgpack模块不会
# 默认工作。 在Python 2.x中没有这样的问题，你可以使用
# “json”或“msgpack”作为序列化程序。
#SCHEDULER_SERIALIZER =“scrapy_redis.picklecompat”

# 调度状态持久化，不清理redis缓存，允许暂停/启动爬虫
SCHEDULER_PERSIST = True

# 请求调度使用优先队列（默认)
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'


# Alternative queues.
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'

# 请求调度使用FIFO队列
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'
# 请求调度使用LIFO队列
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'



# Max idle time to prevent the spider from being closed when distributed crawling.
# This only works if queue class is SpiderQueue or SpiderStack,
# and may also block the same time when your spider start at the first time (because the queue is empty).
# 最大的空闲时间，避免分布式爬取得情况下爬虫被关闭
# 此设置只适用于SpiderQueue和SpiderStack
# 也是爬虫第一次启动时的等待时间（应为队列是空的）
#SCHEDULER_IDLE_BEFORE_CLOSE = 10

# Store scraped item in redis for post-processing.
# 存储爬取到的item，一定要在所有的pipeline最后，即设定对应的数字大于其他pipeline
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300
}

# The item pipeline serializes and stores the items in this redis key.
# item pipeline 序列化并将项目存储在redis项中
#REDIS_ITEMS_KEY = '%(spider)s:items'

# The items serializer is by default ScrapyJSONEncoder. You can use any
# importable path to a callable object.
# 项目序列化程序默认是ScrapyJSONEncoder。你可以使用任何
# 可调用对象的可导入路径
#REDIS_ITEMS_SERIALIZER = 'json.dumps'

# 指定redis的地址和端口(可选，程序将使用默认的地址localhost:6379)
#REDIS_HOST = 'localhost'
#REDIS_PORT = 6379

# 声明redis的url地址（可选）
# 如果设置了这一项，则程序会有限采用此项设置，忽略REDIS_HOST 和 REDIS_PORT的设置
#REDIS_URL = 'redis://user:pass@hostname:9001'

# 自定义redis客户端参数（即：套接字超时等）
#REDIS_PARAMS  = {}
# 使用自定义的redis客户端类。
#REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient'

# If True, it uses redis' ``spop`` operation. This could be useful if you
# want to avoid duplicates in your start urls list. In this cases, urls must
# be added via ``sadd`` command or you will get a type error from redis.
#REDIS_START_URLS_AS_SET = False

# 默认启动RedisSpider和RedisCrawlSpider的urls键
#REDIS_START_URLS_KEY = '%(name)s:start_urls'

# 对于redis，使用utf-8以外的其他编码。
#REDIS_ENCODING = 'latin1'

```

Note

Version 0.3 changed the requests serialization from marshal to cPickle, therefore persisted requests using version 0.2 will not able to work on 0.3.

## Running the example project

这个例子说明了如何在多个蜘蛛实例中共享一个蜘蛛的请求队列，非常适合广泛的爬网。

1. Setup scrapy_redis package in your PYTHONPATH

   在您的PYTHONPATH中安装scrapy_redis软件包

2. Run the crawler for first time then stop it:

   第一次运行爬虫，然后停止它：

   ```
   $ cd example-project
   $ scrapy crawl dmoz
   ... [dmoz] ...
   ^C

   ```

3. 再次运行搜寻器以恢复停止的爬网:

   ```
   $ scrapy crawl dmoz
   ... [dmoz] DEBUG: Resuming crawl (9019 requests scheduled)

   ```

4. 启动一个或多个其他scrapy爬虫:

   ```
   $ scrapy crawl dmoz
   ... [dmoz] DEBUG: Resuming crawl (8712 requests scheduled)

   ```

5. Start one or more post-processing workers:

   启动一个或多个后处理工作者

   ```
   $ python process_items.py dmoz:items -v
   ...
   Processing: Kilani Giftware (http://www.dmoz.org/Computers/Shopping/Gifts/)
   Processing: NinjaGizmos.com (http://www.dmoz.org/Computers/Shopping/Gifts/)
   ...

   ```

## Feeding a Spider from Redis

类scrapy_redis.spiders.RedisSpider使蜘蛛能够从redis中读取URL。 如果第一个请求产生更多的请求，则redis队列中的url将被一个接一个地处理，蜘蛛将在从redis获取另一个url之前处理这些请求。

例如，用下面的代码创建一个myspider.py文件:

```
from scrapy_redis.spiders import RedisSpider

class MySpider(RedisSpider):
    name = 'myspider'

    def parse(self, response):n
        # do stuff
        pass

```

Then:然后

1. run the spider:

   ```
   scrapy runspider myspider.py

   ```

2. push urls to redis:

   ```
   redis-cli lpush myspider:start_urls http://google.com

   ```

