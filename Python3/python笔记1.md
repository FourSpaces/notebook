 # super(ErshoufangSpider, self).__init__(*args, **kwargs)


 sudo mongod --dbpath /data/mongodb/db --logpath /data/mongodb/log/mongodb.log --logappend all output going to: /data/mongodb/log/mongodb.log


# 类中的私有方法
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 乘方


#路径相关
 获取当前运行脚本路径：os.path.abspath(__file__)
```
import os

print '***获取当前目录***'
print os.getcwd()
print os.path.abspath(os.path.dirname(__file__))

print '***获取上级目录***'
print os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print os.path.abspath(os.path.dirname(os.getcwd()))
print os.path.abspath(os.path.join(os.getcwd(), ".."))

print '***获取上上级目录***'
print os.path.abspath(os.path.join(os.getcwd(), "../.."))

```

# 判断是否存存在目录 和 文件
```

import os
 
import os
os.path.isfile('test.txt') #如果文件不存在就返回 False
os.path.isdir('/home/tim/workspace') #如果目录不存在就返回 False


os.path.exists(r'C:\1.TXT') #如果文件不存在就返回 False
os.path.exists('/home/tim/workspace') #如果目录不存在就返回 False

```



# python 依赖库 是写在一个专门的文件中的。


# python join


# python 三目运算符的实现
有问题的实现 1 and a or b  #如果 a 为 0,则会返回 b 数据
完美实现 (1 and [a] or [b])[0] # 完美避开数据陷阱 



