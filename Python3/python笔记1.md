### super(ErshoufangSpider, self).__init__(*args, **kwargs)
```
 sudo mongod --dbpath /data/mongodb/db --logpath /data/mongodb/log/mongodb.log --logappend all output going to: /data/mongodb/log/mongodb.log
```
### 类中的私有方法
```
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
```
### 路径相关
 获取当前运行脚本路径：os.path.abspath(__file__)
```python
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
### 判断是否存存在目录 和 文件
``` python

import os
 
import os
os.path.isfile('test.txt') #如果文件不存在就返回 False
os.path.isdir('/home/tim/workspace') #如果目录不存在就返回 False


os.path.exists(r'C:\1.TXT') #如果文件不存在就返回 False
os.path.exists('/home/tim/workspace') #如果目录不存在就返回 False

```
### python 依赖库 是写在一个专门的文件中的。
### python join
### python 三目运算符的实现
``` python
有问题的实现 1 and a or b  #如果 a 为 0,则会返回 b 数据

完美实现 (1 and [a] or [b])[0] # 完美避开数据陷阱 

test if test else []
```
#### 函数参数
- 可变长度参数

  函数调用中使用 * 和 ** 符号来指定元组合字典的元素作为非关键字或关键字参数的方法。

  - 非关键字可变长参数（元祖）

  ```python
  def function_name([formal_args,] *vargs_tuple):
  	pass
    #星号操作符后的形参作为元组传递到函数中，元组中保存了所有传递给函数的额外参数，如果没给出额外参数元组为空。
  ```

  - 关键字变量参数（字典）
  ```python
  def function_name([formal_args,][*vargst,] **vargsd):
      pass
  dictVarArgs(args='11',tt='11122', ss='22123')
  ```

  - 结合使用
  ```python
  def function_name([formal_args,] *vargs_tuple):
  	pass
  # 星号操作符后的形参作为元组传递到函数中，元组中保存了所有传递给函数的额外参数，如果没给出额外参数元组为空。
  ```

  ```python
  def record(self, *recordList, **recordDict):
  ```


####  常见问题

- is 与 == 的区别

  **Python 对象拥有三个特性／要素：**

  身份／ID：唯一标识对象的身份，该对象的内存地址。

  类型／type：表识对象的类型。

  值／value：对象的值。

​        **对象值比较 ，使用比较运算符**

​         ==, <, >, >=, <=, !=

​        **对象身份比较，使用 is**
    ​```python
    a = 10
    b = 10
    
    c = 1.2
    d = 1.2
    
    /> a is b   
    /> true
    
    /> c is d 
    false
    ​```
    整形对象和字符串对象是不可变对象，所以python 会高效的缓存它们，在应该创建新对象时，却没有创建。

### 常见内建函数
- 标准类型函数
```Python
cmp()  # 比较两个数的大小
str()  # 将对象转换为字符串
type() # 返回对象的类型
```
- 数字类型函数
```python 
# 工厂函数： 指函数为类对象，当你调用它们时，实际上是创建了一个类实例。
# 转换工厂函数
int(), long(), float(), complex(), bool(), 
整型、长整形、浮点型、复数、布尔值


# 功能函数
abs(num)       # 返回给定参数num的绝对值
coerce(num1, num2)    # 将num1 和 num2 转换为同一类型，以一个元祖的形式返回
divmod(num1, num2)    # 对两个参数的进行计算，返回除法的商 和 余数的元组
pow(num1, num2, mod=1)| **   # 进行指数运算，num1的num2次方，如果提供mod 参数，则将结果对mod进行取余运算。
rount(flt, ndig=1)     # 对浮点类型进行四舍五入。第二个参数告诉函数的结果精确位数。返回值为浮点型

```

#### Python 默认参数问题

如果在调用一个函数时,没有传递默认参数,则函数内的默认参数是对函数的默认参数属性__defaults__的引用,

如

```
def func(arg1=[]):
    arg1.append(2)
```

调用func时如果没有传参,上面的arg1就是func.__defaults__[0]的引用

没传递默认参数,会发生以下情况

由于func.__defaults__[0]是可变类型,导致每一次调用func,arg1都会对func.__defaults__[0]进行操作(func.__defaults__[0].append(2),

**Python**的默认参数只会在函数定义时被确定,而不是每次调用时重新确定,所以,一旦在函数中修改了默认参数,则再随后的调用中都会生效

由于有这个特性,在定义函数时,如果默认参数使用可变的对象类型,如上例子,则很可能导致逻辑出错,

所以,如不是特别需要,则不允许在函数内部对默认参数引用的func.__defaults__属性进行修改,如何能让一个对象不被修改?那就是在操作arg1前取消它对__defaults__的引用



#### Python 类变量与实例变量

实例变量是每个实例唯一的数据，类变量是由类的所有实例共享的属性和方法