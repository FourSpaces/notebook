# Scrapy API  相关的代码



**操作日志相关代码**

```python

"""
这里是一个配置启动多爬虫流程
"""

class runSpider(threading.Thread):
    def __init__(self, spider_name, spider_loader):
        threading.Thread.__init__(self)
        self.spider_instance = spider_loader.load(spider_name)
        self.runner = CrawlerRunner()

    def run(self):
        d = self.runner.crawl(BaiduShopListSpider)
        # d.addBoth(lambda _: reactor.stop())
        reactor.run() # the script will block here until the crawling is finished


def run_bass():
    """
    运行全部爬虫
    :return:
    """
    settings = get_project_settings()
    spider_loader = SpiderLoader(get_project_settings())
    spider_list = spider_loader.list()
    print(spider_loader.list())

    threads = []
    #  多线程运行爬虫
    if 'baidu_shop_list' in spider_list:
        # spider_instance = spider_loader.load('baidu_shop_list')
        upthread = RunSpiderProcess('baidu_shop_list', spider_loader)
        upthread.start()
        threads.append(upthread)
        print('baidu_shop_list')

    if 'baidu_shop_details' in spider_list:
        # spider_instance = spider_loader.load('baidu_shop_list')
        upthread = RunSpiderProcess('baidu_shop_details', spider_loader)
        upthread.start()
        threads.append(upthread)
        print('baidu_shop_details')

    if 'baidu_shop_comment' in spider_list:
        # spider_instance = spider_loader.load('baidu_shop_list')
        upthread = RunSpiderProcess('baidu_shop_comment', spider_loader)
        upthread.start()
        threads.append(upthread)
        print('baidu_shop_comment')

    if 'base64_shop' in spider_list:
        # spider_instance = spider_loader.load('baidu_shop_list')
        upthread = RunSpiderProcess('base64_shop', spider_loader)
        upthread.start()
        threads.append(upthread)
        print('base64_shop')

    if 'geo_crawl' in spider_list:
        # spider_instance = spider_loader.load('baidu_shop_list')
        upthread = RunSpiderProcess('geo_crawl', spider_loader)
        upthread.start()
        threads.append(upthread)
        print('geo_crawl')

class RunSpiderProcess(Process):
    def __init__(self, spider_name, spider_loader):
        super().__init__()
        self.spider_instance = spider_loader.load(spider_name)
        self.runner = CrawlerRunner()

    def run(self):
        d = self.runner.crawl(self.spider_instance)
        d.addBoth(lambda _: reactor.stop())
        reactor.run()  # the script will block here until the crawling is finished
```

