## 闭包

如果内部函数的定义包含了在外部函数里定义的对象的引用，内部函数就会变成闭包



内部函数引用了外部函数里定义的对象，或者外部函数之外。



### 装饰器

装饰器 是在函数调用之上的修饰[是一个函数，接受函数对象]，是声明一个函数或方法时，才会应用的额外调用。

语法：@装饰器函数名(装饰器参数) 

- 被修饰的函数

 ```python
@decorator(dec_opt_args)
def function():
	pass
 ```

- 装饰器的堆叠

```
@deco2
@decol
def func():
	pass
等价于
func = deco2(deco1(func))

```

- 有参、无参装饰器

  ```Python
  @deco
  def foo():
    pass
  # 等价于 foo = deco(foo)

  @decomaker(deco_args)
  def foo():
  	pass
  # 返回以函数作为参数的装饰器, decomaker(deco_args)返回了一个函数对象。用foo作为这个函数对象的参数。
  # 等价于 foo = decomaker(deco_args)(foo)

  @decol(deco_arg)
  @deco2
  def func():
    pass
  # 等价于 func = decol(deco_arg)(deco2(func))

  ```

- 装饰器的说明



```
# 可以用其他的变量来作为函数的别名
# foo() , foo是指函数对象的引用， foo()函数对象的调用
# 函数调用中使用* 和**符号来指定元祖和字典的元素作为非关键字参数以及关键字参数
```



### 可变长度的参数

- 非关键字可变长参数（元祖 *）

  ```
  def function_name([formal_args,] *vargs_tuple):
  	# 除了必备参数外，多出的非关键字参数都会被顺序存入vargs_tuple元祖中
  	pass
  ```

- 关键字可变长参数（字典 **）

  ```
  def function_name([formal_args,] [*vargst,] **vargsd):
  	pass
  ```

- 调用带有可变长参数对象函数

  ```
  # 函数原型
  def newfoo(arg1, arg2, *nkw, **kw):
  	pass
  # 调用方式一
  newfoo(10, 20, 30, 40, foo=50, bar=60)
  # 调用方式二
  newfoo(10, 20, *(30, 40), **{'foo'=50, 'bar'=60})
  # 调用方式三
  aTuple = (30, 40)
  aDict = {'foo'=50, 'bar'=60}
  newfoo(10, 20, *aTuple, **aDict)
  ```



### 函数式编程

- 匿名函数 **lambda**

  ```
  lambda [arg1[, arg2,,,argN]]: expression
  ```

  匿名不需要以标准的方式来声明，对象也不会在任何名称空间内创建名字。

  lambda，表达式，定义和声明必须放在同一行

  ```
  def usuallyAdd2(x, y=2): return x+y  <=> lambda x, y=2: x+y
  def showAllAsTuple(*z): return z  <=> lambda *z: z
  ```

- 内建函数 **apply()**

  ```
  apply(func[, nkw][, kw])
  ```

  用可选的参数来调用func,  nkw 为非关键字参数， kw 为关键字参数。返回值是函数调用的返回值。



- 内建函数  **filter()**

  ```
  filter(func, seq)
  ```

  调用一个布尔函数func来迭代遍历每个seq中的元素：返回一个使func返回值为ture的元素的序列

  给定一个对象的 序列和一个过滤函数，每个元素都通过这个过滤器进行筛选，保留函数返回为真的对象。

- 内建函数 **map()**

  ```
  map(func, seq1[,seq2...])
  ```

  将函数fund 作用于给定的序列(s)的每个元素，并用一个列表来提供返回值。

  如果fund 为None，fund 表现为一个身份函数，返回一个含有每个序列中元素集合的n个元素的列表



- 内建函数 **reduce()**

  ```
  reduce(func, seq[,init])
  ```

  将二元函数（一个接收两个值作为输入，返回一个值作为输出）作用于seq 序列的元素，每次携带一对(先前的结果以及下一个序列元素)，连续地将现有的结果和下一个值作用在获得的随后的结果上，最后减少我们的序列为一个单一的返回值。如果初始值init给定，第一个比较会是init 和第一个序列元素，而不是序列的头两个元素



### 偏函数应用

将任意数量（顺序）的参数的函数转化成另一个带剩余参数的函数对象。

```
# 用functional模块中的partial 函数
from operator import add, mul
from functools import partial
add1 = paryial(add, 1)
ss = add1(10)
print(ss) # 11
```

? 固定参数总是放在运行时刻参数的左边。

关键字参数出现在形参之后。



### 变量的作用域

变量在程序中的作用范围，可见性。

- 全局变量和局部变量

  定义在函数内部的变量有局部作用域，模块中最高级别的变量有全局作用域。

  全局变量存活时间：除非被删除，否则存活到脚本运行结束，

  局部变量存活时间：函数调用开始存活，函数结束，变量结束

- 局部变量首先会被搜索到，所以用一个局部变量来“隐藏”或者覆盖一个全局变量。

- global 语句,  在函数内部修改，引用全局变量

- Python 的嵌套作用域，让嵌套函数，能够访问（外部作用域）。



### 闭包

在一个内部函数里，对外部作用域（不是全局作用域）的变量进行引用，那么这个内部函数就是闭包。

**自由变量**：定义在外部函数内的但由内部函数引用或者使用的变量

Scheme 和 Haskell

不同于变量是 因为那些变量存活在一个对象的名称空间，但闭包变量存活在一个函数的名称空间和作用域。

> 闭包的词法变量不属于全局名称空间域或者局部名称空间域，属于其他的命名空间，带着‘流浪’的作用域。 
>
> 闭包变量存活在一个函数的名称空间和作用域

```python
def counter():
    n = 0
    def incr():
        nonlocal n
        x = n
        n += 1
        return x
    return incr
# 情景1
c = counter() 
print(c())
0
print(c())
1
print(c())
2
# 情景2
print(counter()())
0
print(counter()())
0
print(counter()())
0

```

从情景1 可以看到，函数中变量 n 的值没被初始化成为0，而是在上一次调用的基础上加一，

情景2 就比较符合我们先前所想了，情景1 和 情景2 的区别是，情景1中，获取到内部函数的函数名称，去调用，这个函数名称包括了 外层的作用域，外层的 变量n 相对内层函数 incr 而言, 相当于全局变量，

-----------------------

## 什么是名称空间

名称空间是存放名字的地方，对于x=1来说，1存放在内存中，x这个名字和x=1之间的绑定关系存放在名称空间中。

### 名称空间的加载顺序

对于test.py来说

```
1、Python解释器先启动，先加载内置名称空间
2、对于test.py这个文件，加载文件中的全局名称空间，如函数名，定义的变量名
3、在执行文件中的代码的时候，调用函数，临时产生局部名称空间
```

### 名字的查找顺序

局部名称空间--》全局名称空间--》内置名称空间

**在全局无法查看局部的，在局部可以查看全局的**

## 作用域

作用域就是范围

- 全局作用域：内置名称空间、全局名称空间属于这个范围，全局存活，全局有效
- 局部作用域：局部名称空间属于该范围，临时存活，局部有效

作用域在函数定义的时候就确定了，与函数的调用位置无关

### 查看作用域：globals(),locals()

LEGB 代表名字查找顺序: locals -> enclosing function -> globals -> **builtins**
locals 是函数内的名字空间，包括局部变量和形参
enclosing 外部嵌套函数的名字空间（闭包中常见）
globals 全局变量，函数定义所在模块的名字空间
builtins 内置模块的名字空间

## 闭包函数

内部函数包含对外部作用域而非全局作用域的引用

```
def counter():
    n = 0
    def incr():
        nonlocal n
        x = n
        n+=1
        return x
    return incr

c = counter() # c 就是函数incr
print(c)
print(c()) # 0
print(c()) # 1
print(c()) # 2
print(c()) # 3

print(c.__closure__[0].cell_contents) # 擦看闭包的元素
```

### 闭包的意义与作用

返回的函数对象，不仅仅是一个函数对象，在该函数外还包裹了一层作用域，使得函数无论在何处被调用，都优先使用自己外层的作用域

应用：延迟计算

```
import requests

def index(url):
    def get():
        response = requests.get(url)
        response.encoding = 'utf-8'
        return response.text
    return get
baidu = index('http://www.baidu.com')
print(baidu())
```

## 装饰器

装饰器是闭包函数的一种应用场景

### 一 为什么用装饰器

开放封闭原则：对修改封闭，对扩展开放

### 二 什么是装饰器

装饰器他人的器具，本身可以是任意可调用对象，被装饰者也可以是任意可调用对象。
强调装饰器的原则：1 不修改被装饰对象的源代码 2 不修改被装饰对象的调用方式
装饰器的目标：在遵循1和2的前提下，为被装饰对象添加上新功能

### 三 装饰器的使用

```
import time

def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        stop_time = time.time()
        print('run time is %s'%(stop_time-start_time))
        return res
    return wrapper


@timer
def foo():
    time.sleep(3)
    print('foo run')
foo()
```



###  递归

函数自己调用自己，有结束条件，就是递归函数。



### 生成器

迭代器：给非序列对象一个像序列的迭代器接口，用于调用获取下一个元素的next()

协同程序：可以运行的独立函数调用，可以暂停或者挂起，并从程序离开的地方继续或者重新开始。在调用者和(被调用者)协同程序之间有通信，

生成器：挂起返回出中间值，并多次继续的协同程序 被称为生成器，

​		语法上讲，生成器是一个带**yield**语句的函数，**yield**能返回一个值给调用者，并暂停执行，当生成器的**next()** 方法被调用的时候，它会充离开的地方继续

​		一个函数或者自程序只能返回(**return**)一次， 

> 一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。

```python
def simpleGen():
	yield 1
	yield '2 --> punch!'
	
myG.__next__()
Out[39]: 1
myG.__next__()
Out[40]: '2 --> punch!'
myG.__next__()
Traceback (most recent call last):
  File "/Users/weicheng/anaconda/lib/python3.6/site-packages/IPython/core/interactiveshell.py", line 2881, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-41-47b92780d935>", line 1, in <module>
    myG.__next__()
StopIteration


错误：AttributeError: ‘generator’ object has no attribute ‘next’
原因：python 3.x中 generator（有yield关键字的函数则会被识别为generator函数）中的next变为__next__了,next是python 3.x以前版本中的方法
```

迭代穿越一个巨大的数据集合。

加强的生成器特性

next() 获取下一个生成的值，

send() 将值回送给生成器

close() 在生成器中抛出异常，要求生成器退出

```shell
def counter(start_at=0):
	count = start_at
	while True:
		val = (yield count)
		if val is not None:
			count = val
		else:
			count += 1
# 运行
count = counter(5)
count.__next__()
Out[44]: 5
count.__next__()
Out[45]: 6
count.send(10)
Out[46]: 10
count.__next__()
Out[47]: 11
count.close()
count.__next__()
Traceback (most recent call last):
  File "/Users/weicheng/anaconda/lib/python3.6/site-packages/IPython/core/interactiveshell.py", line 2881, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-49-12e48eebfdc5>", line 1, in <module>
    count.__next__()
StopIteration


```



