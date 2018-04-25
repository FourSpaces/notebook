# Core API

New in version 0.15.

This section documents the Scrapy core API, and it’s intended for developers of extensions and middlewares.

## Crawler API

Scrapy API的主要入口点是[`Crawler`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler) 通过`from_crawler`类方法传递给扩展的对象。此对象提供对所有Scrapy核心组件的访问，并且它是扩展访问它们并将其功能挂接到Scrapy的唯一方式。

扩展管理器负责加载和跟踪已安装的扩展，并通过[`EXTENSIONS`](https://doc.scrapy.org/en/latest/topics/settings.html#std:setting-EXTENSIONS)包含所有可用扩展的词典以及它们的顺序的设置进行[配置，](https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#topics-downloader-middleware-setting)类似于您[配置下载器中间件的方式](https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#topics-downloader-middleware-setting)。

- **class scrapy.crawler.Crawler (*spidercls*, *settings*) **

  Crawler对象必须用一个[`scrapy.spiders.Spider`](https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.Spider)子类和一个 [`scrapy.settings.Settings`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.Settings)对象实例化 。

  - `settings`

    此抓取工具的设置管理器。这被扩展和中间件用于访问该爬虫的Scrapy设置。有关Scrapy设置的介绍，请参阅[设置](https://doc.scrapy.org/en/latest/topics/settings.html#topics-settings)。对于API请参阅[`Settings`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.Settings)类。


  - `signals`

    该爬虫的信号管理器。这被扩展和中间件用来将自己锁定到Scrapy功能。有关信号的介绍，请参阅[Signals](https://doc.scrapy.org/en/latest/topics/signals.html#topics-signals)。对于API请参阅[`SignalManager`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.signalmanager.SignalManager)类。


  - `stats`

    此抓取工具的统计信息收集器。这用于扩展和中间件以记录其行为的统计信息，或访问其他扩展收集的统计信息。有关统计信息收集的介绍，请参阅[统计信息收集](https://doc.scrapy.org/en/latest/topics/stats.html#topics-stats)。对于API请参阅[`StatsCollector`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.statscollectors.StatsCollector)类。


  - `extensions`

    跟踪启用的扩展的扩展管理器。大多数扩展将不需要访问该属性。有关扩展的介绍和Scrapy上的可用扩展列表，请参阅[扩展](https://doc.scrapy.org/en/latest/topics/extensions.html#topics-extensions)。


  - `engine`

    执行引擎，用于协调调度程序，下载程序和蜘蛛之间的核心爬行逻辑。某些扩展可能希望访问Scrapy引擎，以检查或修改下载程序和调度程序的行为，尽管这是高级用法，并且此API尚不稳定。


  - `spider`

    蜘蛛目前正在爬行。这是构建爬行程序时提供的spider类的一个实例，它是在[`crawl()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler.crawl)方法中给出的参数之后创建的。


  - `crawl`（** args*，**\* kwargs *）

    在执行引擎处于运动状态时，通过使用给定的args和kwargs参数实例化其spider类来启动爬网程序 。返回爬网完成时触发的延迟。


- **class  scrapy.crawler.CrawlerRunner(*settings=None*) **

  这是一个方便的帮助类，用于跟踪，管理和运行已安装的Twisted [reactor](https://twistedmatrix.com/documents/current/core/howto/reactor-basics.html)内的爬虫。

  CrawlerRunner对象必须用[`Settings`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.Settings)对象实例化 。

  除非编写手动处理爬行过程的脚本，否则不应该需要该类（因为Scrapy负责相应使用它）。有关[示例，](https://doc.scrapy.org/en/latest/topics/practices.html#run-from-script)请参阅[脚本](https://doc.scrapy.org/en/latest/topics/practices.html#run-from-script)中的[运行Scrapy](https://doc.scrapy.org/en/latest/topics/practices.html#run-from-script)。

  - `crawl（crawler_or_spidercls，*args，**kwargs）`

    使用提供的参数运行爬网程序。它会调用给定的Crawler的[`crawl()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler.crawl)方法，同时保持它的跟踪，以便稍后停止。如果crawler_or_spidercls不是[`Crawler`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler) 实例，则此方法将尝试使用此参数创建一个作为提供给它的蜘蛛类的参数。返回爬网完成时触发的延迟。参数：**crawler_or_spidercls**（[`Crawler`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler)实例， [`Spider`](https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.Spider)子类或字符串） - 已经创建的爬虫，或者项目内部的蜘蛛类或蜘蛛的名字来创建它**args**（[*list*](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.loader.SpiderLoader.list)） - 初始化蜘蛛的参数**kwargs**（*dict*） - 关键字参数来初始化蜘蛛


  - `crawlers`

    设置的[`crawlers`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler)由开始[`crawl()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.CrawlerRunner.crawl)和这个类进行管理。


  - `create_crawler（crawler_or_spidercls ）`

    返回一个[`Crawler`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler)对象。如果crawler_or_spidercls是爬网程序，它将按原样返回。如果crawler_or_spidercls是Spider子类，则为其构建新的Crawler。如果crawler_or_spidercls是一个字符串，该函数将在Scrapy项目中使用该名称查找一个具有该名称的spider（使用spider loader），然后为其创建一个Crawler实例。


  - `join`（）

    返回所有托管[`crawlers`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.CrawlerRunner.crawlers)已完成执行时触发的延迟。


  - `stop`（）

    同时停止所有正在进行的抓取工作。返回一个延迟，当它们全部结束时触发。



- **class  scrapy.crawler.CrawlerProcess(*settings=None*, *install_root_handler=True*) ** 

  基地： [`scrapy.crawler.CrawlerRunner`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.CrawlerRunner)

  一个类在一个进程中同时运行多个scrapy爬虫。

  该类[`CrawlerRunner`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.CrawlerRunner)通过添加对启动Twisted [reactor](https://twistedmatrix.com/documents/current/core/howto/reactor-basics.html)和处理关闭信号的支持来扩展，如键盘中断命令Ctrl-C。它还配置顶级日志记录。

  此应用程序应该比您的应用程序[`CrawlerRunner`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.CrawlerRunner)中没有运行另一个Twisted [反应堆](https://twistedmatrix.com/documents/current/core/howto/reactor-basics.html)更合适 。

  CrawlerProcess对象必须用[`Settings`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.Settings)对象实例化 。

  | 参数：  | **install_root_handler** - 是否安装根日志记录处理程序（默认值：True |
  | ---- | ---------------------------------------- |
  |      |                                          |

  除非编写手动处理爬行过程的脚本，否则不应该需要该类（因为Scrapy负责相应使用它）。有关[示例，](https://doc.scrapy.org/en/latest/topics/practices.html#run-from-script)请参阅[脚本](https://doc.scrapy.org/en/latest/topics/practices.html#run-from-script)中的[运行Scrapy](https://doc.scrapy.org/en/latest/topics/practices.html#run-from-script)。

  - `crawl`（*crawler_or_spidercls*，** args*，**\* kwargs *）

    使用提供的参数运行爬网程序。它会调用给定的Crawler的[`crawl()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler.crawl)方法，同时保持它的跟踪，以便稍后停止。如果crawler_or_spidercls不是[`Crawler`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler) 实例，则此方法将尝试使用此参数创建一个作为提供给它的蜘蛛类的参数。返回爬网完成时触发的延迟。参数：**crawler_or_spidercls**（[`Crawler`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler)实例， [`Spider`](https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.Spider)子类或字符串） - 已经创建的爬虫，或者项目内部的蜘蛛类或蜘蛛的名字来创建它**args**（[*list*](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.loader.SpiderLoader.list)） - 初始化蜘蛛的参数**kwargs**（*dict*） - 关键字参数来初始化蜘蛛


  - `crawlers`

    设置的[`crawlers`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler)由开始[`crawl()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.CrawlerProcess.crawl)和这个类进行管理。


  - `create_crawler`（*crawler_or_spidercls *）

    返回一个[`Crawler`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler)对象。如果crawler_or_spidercls是爬网程序，它将按原样返回。如果crawler_or_spidercls是Spider子类，则为其构建新的Crawler。如果crawler_or_spidercls是一个字符串，该函数将在Scrapy项目中使用该名称查找一个具有该名称的spider（使用spider loader），然后为其创建一个Crawler实例。


  - `join`（）

    返回所有托管[`crawlers`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.CrawlerProcess.crawlers)已完成执行时触发的延迟。


  - `start`（*stop_after_crawl = True *）

    此方法从一个扭曲的[反应器](https://twistedmatrix.com/documents/current/core/howto/reactor-basics.html)，其调整池的大小来 [`REACTOR_THREADPOOL_MAXSIZE`](https://doc.scrapy.org/en/latest/topics/settings.html#std:setting-REACTOR_THREADPOOL_MAXSIZE)，并安装基于DNS缓存[`DNSCACHE_ENABLED`](https://doc.scrapy.org/en/latest/topics/settings.html#std:setting-DNSCACHE_ENABLED)和[`DNSCACHE_SIZE`](https://doc.scrapy.org/en/latest/topics/settings.html#std:setting-DNSCACHE_SIZE)。如果stop_after_crawl为True，则在使用完所有爬网程序后，反应堆将停止[`join()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.CrawlerProcess.join)。参数：**stop_after_crawl**（*boolean*） - 当所有爬虫完成时停止或反应堆


  - `stop`（）

    同时停止所有正在进行的抓取工作。返回一个延迟，当它们全部结束时触发。


## Settings API

- `scrapy.settings.``SETTINGS_PRIORITIES`

  设置Scrapy中默认设置优先级的键名和优先级的字典。

  每个项目定义一个设置入口点，给它一个用于识别的代码名称和一个整数优先级。在设置和检索[`Settings`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.Settings)课程中的值时，优先级较高的优先级优先级较低 。

  ```
  SETTINGS_PRIORITIES  =  { 
      'default' ： 0 ，
      'command' ： 10 ，
      'project' ： 20 ，
      'spider' ： 30 ，
      'cmdline' ： 40 ，
  }

  ```

  有关每个设置来源的详细说明，请参阅： [设置](https://doc.scrapy.org/en/latest/topics/settings.html#topics-settings)。


- `scrapy.settings.``get_settings_priority`(*priority*)

  小型帮助函数，用于在[`SETTINGS_PRIORITIES`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.SETTINGS_PRIORITIES)字典中查找给定的字符串优先级 并返回其数值，或直接返回给定的数字优先级。


- *class*`scrapy.settings.``Settings`(*values=None*, *priority='project'*)

  该对象存储用于配置内部组件的Scrapy设置，并可用于任何进一步的自定义。

  它是一个直接的子类，并支持所有的方法 [`BaseSettings`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.BaseSettings)。另外，在这个类的实例化之后，新对象将具有在已经填充的[内置设置参考中](https://doc.scrapy.org/en/latest/topics/settings.html#topics-settings-ref)描述的全局默认设置。


- *class*`scrapy.settings.``BaseSettings`(*values=None*, *priority='project'*)

  这个类的实例像字典一样，但是存储优先级以及它们的对，并且可以被冻结（即被标记为不可变）。`(key, value)`

  键值条目可以在初始化时通过`values` 参数传递，并且它们将采用该`priority`级别（除非`values`已经是实例[`BaseSettings`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.BaseSettings)，在这种情况下将保留现有的优先级）。如果`priority` 参数是一个字符串，则会查找优先级名称 [`SETTINGS_PRIORITIES`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.SETTINGS_PRIORITIES)。否则，应该提供一个特定的整数。

  一旦创建了对象，就可以使用该[`set()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.BaseSettings.set)方法加载或更新新设置 ，并且可以使用字典的方括号表示法或[`get()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.BaseSettings.get)实例的 方法及其值转换变体来访问。当请求存储的密钥时，将检索具有最高优先级的值。

  - `copy`（）

    制作当前设置的深层副本。此方法返回[`Settings`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.Settings)该类的新实例，并使用相同的值和优先级填充。对新对象的修改不会反映在原始设置上。


  - `copy_to_dict`（）

    复制当前设置并转换为字典。此方法返回一个新的字典，其中填入与当前设置相同的值和优先级。对返回的词典的修改不会反映在原始设置上。此方法可用于在Scrapy shell中打印设置。


  - `freeze`（）

    禁用对当前设置的进一步更改。调用此方法后，设置的当前状态将变为不可变。试图通过该[`set()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.BaseSettings.set)方法及其变体来改变数值将不可能，并且会被警告。


  - `frozencopy`（）

    返回当前设置的不可变副本。[`freeze()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.BaseSettings.freeze)在返回的对象中调用别名[`copy()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.BaseSettings.copy)。


  - `get`（*名称*，*默认=无*）

    获取设置值而不影响其原始类型。参数：**名称**（*字符串*） - 设置名称**default**（*any*） - 如果未找到设置，则返回的值


  - `getbool`（*名称*，*默认= False *）

    获取一个布尔值作为设置值。`1`，`'1'`，TRUE`和`'True'`回报`True`，同时`0`，`'0'`，`False`，`'False'`和`None`回报`False`。例如，使用此方法时，通过设置为的环境变量填充的设置 `'0'`将返回`False`。参数：**名称**（*字符串*） - 设置名称**default**（*any*） - 如果未找到设置，则返回的值


  - `getdict`（*名称*，*默认=无*）

    获取设置值作为字典。如果设置的原始类型是字典，它的副本将被返回。如果它是一个字符串，它将被评估为JSON字典。如果它是一个 [`BaseSettings`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.BaseSettings)实例本身，它将被转换为一个字典，其中包含它将返回的所有当前设置值[`get()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.BaseSettings.get)，并丢失关于优先级和可变性的所有信息。参数：**名称**（*字符串*） - 设置名称**default**（*any*） - 如果未找到设置，则返回的值


  - `getfloat`（*名称*，*默认值= 0.0 *）

    以浮点形式获取设置值。参数：**名称**（*字符串*） - 设置名称**default**（*any*） - 如果未找到设置，则返回的值


  - `getint`（*名称*，*默认= 0 *）

    以int形式获取设置值。参数：**名称**（*字符串*） - 设置名称**default**（*any*） - 如果未找到设置，则返回的值


  - `getlist`（*名称*，*默认=无*）

    获取设置值作为列表。如果设置原始类型是一个列表，它的一个副本将被返回。如果它是一个字符串，它将被“，”拆分。例如，`'one,two'`使用此方法时，通过设置为环境变量填充的设置 将返回一个列表['one'，'two']。参数：**名称**（*字符串*） - 设置名称**default**（*any*） - 如果未找到设置，则返回的值


  - `getpriority`（*名字*）

    返回设置的当前数字优先级值，或者`None`如果给定`name`不存在。参数：**名称**（*字符串*） - 设置名称


  - `getwithbase`（*名字*）

    获取类似字典的设置及其_BASE 对应的组合。参数：**名称**（*字符串*） - 字典式设置的名称


  - `maxpriority`（）

    返回所有设置中存在的最高优先级的数值，或返回`default`从 [`SETTINGS_PRIORITIES`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.SETTINGS_PRIORITIES)没有存储设置的数值。


  - `set`（*名称*，*值*，*优先级='项目' *）

    存储具有给定优先级的键/值属性。*在*配置Crawler对象*之前*（通过`configure()`方法）应该填充设置，否则它们不会有任何效果。参数：**名称**（*字符串*） - 设置名称**值**（*任何*） - 与设置关联的值**优先级**（*字符串**或**整数*） - 设置的优先级。应该是关键 [`SETTINGS_PRIORITIES`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.SETTINGS_PRIORITIES)或整数


  - `setmodule`（*模块*，*优先级='项目' *）

    从具有给定优先级的模块存储设置。这是一个辅助函数调用 [`set()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.BaseSettings.set)的每一个全局声明大写变量`module`与所提供的`priority`。参数：**模块**（*模块对象**或**字符串*） - 模块或模块的路径**优先级**（*字符串**或**整数*） - 设置的优先级。应该是关键 [`SETTINGS_PRIORITIES`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.SETTINGS_PRIORITIES)或整数


  - `update`（*值*，*优先='项目' *）

    存储具有给定优先级的键/值对。这是一个辅助函数调用 [`set()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.BaseSettings.set)为每一个项目`values` 与所提供的`priority`。如果`values`是字符串，则假定它是JSON编码的，并且先用解析成字典`json.loads()`。如果它是一个 [`BaseSettings`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.BaseSettings)实例，则将使用每个按键优先级并`priority`忽略该参数。这允许用单个命令插入/更新具有不同优先级的设置。参数：**值**（字典或字符串或[`BaseSettings`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.BaseSettings)） - 设置名称和值**优先级**（*字符串**或**整数*） - 设置的优先级。应该是关键 [`SETTINGS_PRIORITIES`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.SETTINGS_PRIORITIES)或整数

## SpiderLoader API

- *class*`scrapy.loader.``SpiderLoader`

  这个类负责检索和处理整个项目中定义的蜘蛛类。

  可以通过在[`SPIDER_LOADER_CLASS`](https://doc.scrapy.org/en/latest/topics/settings.html#std:setting-SPIDER_LOADER_CLASS)项目设置中指定它们的路径来使用自定义蜘蛛加载器 。他们必须完全实现`scrapy.interfaces.ISpiderLoader`接口以保证无错执行。

  - `from_settings`（*设置*）

    Scrapy使用这个类方法来创建类的一个实例。它使用当前的项目设置调用，并且它会在[`SPIDER_MODULES`](https://doc.scrapy.org/en/latest/topics/settings.html#std:setting-SPIDER_MODULES) 设置的模块中递归地加载发现的蜘蛛。参数：**设置**（[`Settings`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.Settings)实例） - 项目设置


  - `load`（*spider_name *）

    用给定的名字获得蜘蛛类。它会查看以前加载的名为spider_name的蜘蛛类的spider，如果找不到则会引发KeyError。参数：**spider_name**（*str*） - 蜘蛛类名称


  - `list`（）

    获取项目中可用蜘蛛的名称。


  - `find_by_request`（*请求*）

    列出可以处理给定请求的蜘蛛名称。将尝试匹配请求的网址与蜘蛛的域名。参数：**请求**（[`Request`](https://doc.scrapy.org/en/latest/topics/request-response.html#scrapy.http.Request)实例） - 查询请求

## Signals API

- *class*`scrapy.signalmanager.``SignalManager`(*sender=_Anonymous*)

  - `connect`（*接收器*，*信号*，**\* kwargs *）

    将接收器功能连接到信号。信号可以是任何对象，尽管Scrapy带有一些预定义的信号，这些信号记录在[Signals](https://doc.scrapy.org/en/latest/topics/signals.html#topics-signals) 部分。参数：**接收器**（*可调用*） - 要连接的功能**信号**（*物体*） - 要连接的信号


  - `disconnect`（*接收器*，*信号*，**\* kwargs *）

    从信号中断开接收器功能。这与该[`connect()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.signalmanager.SignalManager.connect)方法具有相反的效果，并且参数是相同的。


  - `disconnect_all`（*信号*，**\* kwargs *）

    断开所有接收器与给定信号的连接。参数：**信号**（*对象*） - 要从中断开的信号


  - `send_catch_log`（*信号*，**\* kwargs *）

    发送信号，捕获异常并记录它们。关键字参数传递给信号处理程序（通过[`connect()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.signalmanager.SignalManager.connect)方法连接）。


  - `send_catch_log_deferred`（*信号*，**\* kwargs *）

    像[`send_catch_log()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.signalmanager.SignalManager.send_catch_log)但支持从信号处理程序返回[延迟](https://twistedmatrix.com/documents/current/core/howto/defer.html)。返回所有信号处理程序延迟后被触发的延迟。发送信号，捕获异常并记录它们。关键字参数传递给信号处理程序（通过[`connect()`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.signalmanager.SignalManager.connect)方法连接）。


## Stats Collector API

在该[`scrapy.statscollectors`](https://doc.scrapy.org/en/latest/topics/stats.html#module-scrapy.statscollectors)模块下有几个Stats Collector ，它们都实现了由[`StatsCollector`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.statscollectors.StatsCollector) 该类定义的Stats Collector API （它们都继承自该类）。

- *class*`scrapy.statscollectors.``StatsCollector`

  - `get_value`（*键*，*默认=无*）

    如果不存在，则返回给定统计密钥的值或默认值。


  - `get_stats`（）

    作为字典获取当前正在运行的蜘蛛的所有统计数据。


  - `set_value`（*键*，*值*）

    为给定的统计信息键设置给定的值。


  - `set_stats`（*统计*）

    用`stats`参数中传递的字典覆盖当前的统计信息。


  - `inc_value`（*key*，*count = 1*，*start = 0 *）

    假定给定的起始值（未设置时），按给定的计数递增给定统计密钥的值。


  - `max_value`（*键*，*值*）

    仅当同一个键的当前值小于值时，才为给定键设置给定值。如果给定键没有当前值，则该值始终设置。


  - `min_value`（*键*，*值*）

    仅当同一个键的当前值大于值时，才为给定键设置给定值。如果给定键没有当前值，则该值始终设置。


  - `clear_stats`（）

    清除所有统计信息。

  以下方法不是统计信息收集API的一部分，而是在实现自定义统计信息收集器时使用：

  - `open_spider`（*蜘蛛*）

    打开给定的蜘蛛进行统计信息收集。


  - `close_spider`（*蜘蛛*）

    关闭给定的蜘蛛。在此之后，不能访问或收集更多具体的统计数据。