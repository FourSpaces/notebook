#### 自定义Item Exporters 

1. ​

- 实例化exporter后的执行流程

  [ 1 ] 调用 `start_exporting()`  以标识 exporting 过程的开始

  [ 2 ] 对要导出的每个项目调用 [`export_item()`](http://scrapy-chs.readthedocs.io/zh_CN/1.0/topics/exporters.html#scrapy.exporters.BaseItemExporter.export_item) 方法

  [ 3 ] 最后调用 [`finish_exporting()`](http://scrapy-chs.readthedocs.io/zh_CN/1.0/topics/exporters.html#scrapy.exporters.BaseItemExporter.finish_exporting) 表示 exporting 过程的结束

