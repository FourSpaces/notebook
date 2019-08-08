### StreamSets 数据清洗



#### 概念理解



**管道：**

​	管道描述了从原始系统到目标系统的数据流，并定义了如何沿途转换数据。

管道验证不会阻止重复数据。要避免将重复数据写入目标，请配置管道逻辑以删除重复数据或防止生成重复数据。

请注意，您无法将事件流与数据流合并。事件记录必须从事件生成阶段流向目标或执行程序，而不与数据流合并。有关事件框架和事件流的更多信息，请参阅[数据流触发器概述](http://ambari.bigdata.org:18630/docs/datacollector/UserGuide/Event_Handling/EventFramework-Title.html#concept_cph_5h4_lx)。



**目录源**

目录源从目录中的文件读取数据。要处理的文件必须共享文件名模式并完全写入。要从仍在写入的活动文件中读取数据，请使用文件尾部原点



使用record：attribute或record：attributeOrDefault函数来访问属性中的信息