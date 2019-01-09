[Shadow Of Winger](http://wingerted.com/)

[首页](http://wingerted.com/) [归档](http://wingerted.com/archives/) [关于](http://wingerted.com/about)

[NULL](http://wingerted.com/2018/02/25/NULL/)2018-02-25NULL显然, 今天是一个值得纪念的日子, 在这里, 发生了一件大事, 见证了新时代的开始.今天, 微信, QQ, 微博等社交工具无法修改资料, 系统均在维护.往后会怎么样呢?[airflow-usage](http://wingerted.com/2017/02/26/airflow-usage/)2017-02-26Airflow 的运行流程对于Airflow的使用来说了解整个Airflow的运行流程是非常重要的，否则就会出现很多无法预料的行为，关于这部分，本少爷也是踩了很多的坑。DAG，TASK和他们的实例首先要明白一个概念，无论是DAG，还是TASK都是一个描述一个抽象的逻辑。
真正在某个时间点运行的DAG或TASK才是运行的实例。在Airflow中，DAG的实例叫做**Dag Run**， Task的实例叫做**Task Instance**Airflow 执行组件Airflow的调度和执行流程中有两个核心的组件Scheduler：这个是整个Airflow的调度器，Airflow所有DAG的调度过程是由Scheduler轮询来处理的。触发条件达到后，会丢给Executor执行。Executor：现在的Executor有三种：SequnceExecutor：提供本地执行，并且串行执行一个DAG中的所有Task，基本上只用在初期的Airflow概念验证阶段LocalExecutor：这个是比较常用的Executor，可以在本地并行执行一个DAG内的所有TaskCeleryExecutor：这个是在大型任务调度场景，或者是表较复杂的任务分离场景中需要用到的Executor。顾名思义，在这个Executor下，Airflow使用了Celery这个强大的Python分布式队列框架去分发任务，然后在这样的环境下，需要在执行任务的机器上启用Airflow Worker来处理队列中的请求。在一个Airflow中同时只能一个Executor启动，不能给指定的DAG指定ExecutorPool：这个Pool虽然不是Airflow的核心，但也跟整个Airflow的执行流程相关。任何一个Task其实都是指定了Pool这个参数的，即使没有自己指定，其实也是归结到了Default Pool这么个池子中。Pool本身是个抽象的概念，由Slot组成，可以建立任何一个Pool，指定Slot的数量。任何一个使用了这个Pool的Task Instance就需要占用一个Slot，Slot用完了，Task就处于等待状态。Airflow 执行参数在整个Airflow的执行流程中，有几个参数，控制了整个调度流程的并行度，但是在文档中却没有好好的写明白。parallelism：这个参数指定了整个Airflow系统，在任何一刻能同时运行的Task Instance的数量，这个数量跟DAG无关，只跟Executor和Task有关。举个例子：如果parallelism=15, 这时你有两个DAG，A和B，如果A需要同时开跑10个Task，B也要同时开跑10个Task，两个DAG同时触发，那么这时候同时在跑的Task数量只能是15，其余的5个会等之前的Task运行完了触发，这时的状态不会显示在web上。而且在这种情况下，触发的顺序是不确定的。dag_concurrency：这个参数指定了同一个Dag Run中能同时运行的Task Instance的个数max_active_runs_per_dag：这个参数指定了同一个Dag能被同时激活的Dag Run的数量non_pooled_task_slot_count：这个参数指定了默认的Pool能同时运行的Task Instance的数量，如果你的Task没有指定Pool选项，那么这个Task就是属于这个默认的Pool的Airflow 执行状态对于Airflow来说，Dag Run和Task Instance都有自己的执行状态，而且这两者的执行状态**不关联**，也就是说有可能某一个Dag Run是Success的，但是这个Dag Run里的Task Instance确是Failed或者无状态的，反之亦然。怎么会出现这种情况呢？一般来说，正常的调度行为下，这种情况是不会出现的，但是如果说我们的Dag写错了，Task跑错了呢？错误的处理方法：直接在Dag Run的菜单中删除这个跑错的Dag Run，然后让调度器重跑，或者Backfill它但这时，实际上这个Dag Run跑过的Task Instance的状态还在数据库中，于是实际上根本就没有运行Task就调度器就自动判断跑完了。直接删除Task Instance也是一样的情况，调度器会认为这个Dag Run是Success的状态所以就不跑它。但这时可以Backfill所以正确的做法是使用Clear当我们Clear一个Task Instance时，这个Task Instance所属的Dag Run的状态会立即被置为Running，这样调度器就会认为这个Dag Run要继续跑。当然，如果我们同时删除了一批Task Instance和它们所属的Dag Run的话，调度器也会正常的重新开始执行，实际上这样的操作方式，在界面上更容易一点。在清空状态或重跑时，暂停当前Dag的调度是比较靠谱的，否则会出现，清空到一半，当中的某个任务已经开始被调度的情况，所以最好全部清空完毕后，再打开调度器。One more thing，还有非常重要的一点，如果当前有Task Instance在运行，这时我们如果删除了这个Task Instance的状态或者Clear它的状态，实际在后台运行着的任务**并不会停止**！所以需要手工Kill这个任务的运行，然后这时Scheduler进程收到了子进程（我们的运行的Task）异常退出的状态，就会把这个Task Instance的任务状态重新写成Failed，然后我们就又要清空一遍，所以**在重跑任务前，一定要先停止调度，然后Kill当前正在运行的任务进程，最后清空任务状态**。[introduce-to-airflow](http://wingerted.com/2017/02/20/introduce-to-airflow/)2017-02-20Airflow 抽象理解在介绍Airflow之前，我们需要了解任务依赖的概念任务依赖通常，在一个运维系统，数据分析系统，或测试系统等大型系统中，我们会有各种各样的依赖需求。比如，**时间依赖**：任务需要等待某一个时间点触发**外部系统依赖**：任务依赖Mysql中的数据，HDFS中的数据等等，这些不同的外部系统需要调用接口去访问**机器依赖**：任务的执行只能在特定的某一台机器的环境中，可能这台机器内存比较大，也可能只有那台机器上有特殊的库文件**任务间依赖**：任务A需要在任务B完成后启动，两个任务互相间会产生影响**资源依赖**：任务消耗资源非常多，使用同一个资源的任务需要被限制，比如跑个数据转换任务要10个G，机器一共就30个G，最多只能跑两个，我希望类似的任务排个队**权限依赖**：某种任务只能由某个权限的用户启动也许大家会觉得这些是在任务程序中的逻辑需要处理的部分，但是我认为，这些逻辑可以抽象为**任务控制逻辑**的部分，和实际**任务执行逻辑**解耦合如何理解Crontab现在让我们来看下最常用的依赖管理系统，Crontab在各种系统中，总有些定时任务需要处理，每当在这个时候，我们第一个想到的总是crontab。确实，crontab可以很好的处理定时执行任务的需求，但是对于crontab来说，执行任务，只是调用一个程序如此简单，而程序中的各种逻辑都不属于crontab的管辖范围（很好的遵循了KISS）所以我们可以抽象的认为：**crontab是一种依赖管理系统，而且只管理时间上的依赖。**Airflow的处理依赖的方式现在重点Airflow来了，看下它是怎么处理我们遇到的依赖问题。Airflow的核心概念，是DAG(有向无环图)，DAG由一个或多个TASK组成，而这个DAG正是解决了上文所说的任务间依赖。Task A 执行完成后才能执行 Task B，多个Task之间的依赖关系可以很好的用DAG表示完善Airflow完整的支持crontab表达式，也支持直接使用python的datatime表述时间，还可以用datatime的delta表述时间差。这样可以解决任务的时间依赖问题。Airflow在CeleryExecuter下可以使用不同的用户启动Worker，不同的Worker监听不同的Queue，这样可以解决用户权限依赖问题。Worker也可以启动在多个不同的机器上，解决机器依赖的问题。Airflow可以为任意一个Task指定一个抽象的Pool，每个Pool可以指定一个Slot数。每当一个Task启动时，就占用一个Slot，当Slot数占满时，其余的任务就处于等待状态。这样就解决了资源依赖问题。Airflow中有Hook机制(其实我觉得不应该叫Hook)，作用时建立一个与外部数据系统之间的连接，比如Mysql，HDFS，本地文件系统(文件系统也被认为是外部系统)等，通过拓展Hook能够接入任意的外部系统的接口进行连接，这样就解决的外部系统依赖问题。当然， 这些并不是Airflow的设计目的，Airflow设计时，只是为了很好的处理ETL任务而已，但是其精良的设计，正好可以用来解决任务的各种依赖问题。具体的Airflow使用方式请直接参考官方文档[Hello World](http://wingerted.com/2016/10/30/hello-world/)2016-10-30Welcome to [Hexo](https://hexo.io/)! This is your very first post. Check [documentation](https://hexo.io/docs/) for more info. If you get any problems when using Hexo, you can find the answer in [troubleshooting](https://hexo.io/docs/troubleshooting.html) or you can ask me on [GitHub](https://github.com/hexojs/hexo/issues).Quick StartCreate a new post`$ hexo new "My New Post"`More info: [Writing](https://hexo.io/docs/writing.html)Run server`$ hexo server`More info: [Server](https://hexo.io/docs/server.html)Generate static files`$ hexo generate`More info: [Generating](https://hexo.io/docs/generating.html)Deploy to remote sites`$ hexo deploy`More info: [Deployment](https://hexo.io/docs/deployment.html)

   

由 [Hexo](https://hexo.io/) 强力驱动 | 主题 - [Even](https://github.com/ahonn/hexo-theme-even)© 2017 - 2018  Winger





### #

```
Dag（有向无环图）是一组定向任务
依赖于取决于。 一个dag也有一个时间表，一个开始结束日期
（可选的）。 对于每个时间表（例如，每天或每小时），DAG需要运行
每个单独的任务都满足作为他们的依赖。 有些任务有
根据他们过去的属性，这意味着他们无法运行
直到他们以前的时间表（和上游任务）完成。

 DAG本质上充当任务的命名空间。 task_id只能添加一次到DAG。

    :param dag_id: The id of the DAG
    	:type dag_id: string
    :param description: DAG 的描述，例如 显示在webserver上
    	:type description: string
    :param schedule_interval: 定义DAG运行频率， timedelta被添加到您的最新任务实例中，dateutil会找下一个时间段
    	:type schedule_interval: datetime.timedelta or
        dateutil.relativedelta.relativedelta or str that acts as a cron
        expression
    :param start_date: 调度程序会从开始时间进行尝试回填
    	:type start_date: datetime.datetime
    :param end_date: 超出日期，DAG将不会运行，对于开放式调度而言，无所畏惧
    	:type end_date: datetime.datetime
    :param template_searchpath: 这个文件夹列表，定义了jinja 在哪里寻找你的模版，请注意，jinja / airflow包含DAG文件的默认路径b
    	:type template_searchpath: string or list of stings
    :param user_defined_macros: 传递给jinja模版中的字典，例如，传递``dict（foo ='bar'）``
         通过这个参数可以让你在所有的忍者中都可以使用{{foo}}与此DAG相关的模板。 请注意，你可以通过任何
         类型的对象在这里。
    	:type user_defined_macros: dict
    :param user_defined_filters: a dictionary of filters that will be exposed
        in your jinja templates. For example, passing
        ``dict(hello=lambda name: 'Hello %s' % name)`` to this argument allows
        you to ``{{ 'world' | hello }}`` in all jinja templates related to
        this DAG.
    :type user_defined_filters: dict
    :param default_args: A dictionary of default parameters to be used
        as constructor keyword parameters when initialising operators.
        Note that operators have the same hook, and precede those defined
        here, meaning that if your dict contains `'depends_on_past': True`
        here and `'depends_on_past': False` in the operator's call
        `default_args`, the actual value will be `False`.
    	:type default_args: dict
    :param params: a dictionary of DAG level parameters that are made
        accessible in templates, namespaced under `params`. These
        params can be overridden at the task level.
    	:type params: dict
    :param concurrency: 允许同时运行任务实例的数量
    	:type concurrency: int
    :param max_active_runs: 超出此范围的活动DAG运行的最大数量
         DAG的数量在运行状态下运行，调度程序不会创建
         新的活动DAG运行
    	:type max_active_runs: int
    :param dagrun_timeout: 指定DagRun应该运行多久超时/失败，这样就可以创建新的DagRun
    	:type dagrun_timeout: datetime.timedelta
    :param sla_miss_callback: 指定在报告SLA超时时调用的函数。
    	:type sla_miss_callback: types.FunctionType
    :param default_view: 指定DAG默认视图（树，图形，持续时间，甘特图，landing_times）
    	:type default_view: string
    :param orientation: 在图形视图中指定DAG方向（LR，TB，RL，BT）
    	:type orientation: string
    :param catchup: 执行调度程序追赶（或只运行最新）？ 默认为True
    :type catchup: bool
```

