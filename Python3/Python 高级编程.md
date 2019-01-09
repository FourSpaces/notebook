## Python 高级编程



类是对象的定义，实例是“真正的实物”，存放了类中所定义的对象的具体信息。



创建一个实例的过程被称为实例化

```
myFirstObject = MyNewObjectType()
```

类仅用作名词空间，将数据保存在变量中，对他们按名称空间进行分组。

self 参数代表实例对象本身。

>类名由大写字母打头，
>
>数据属性：应该像数据值的名字
>
>方法名指出对应值的行为



### 特殊方法

构造器在创建一个新的对象时被调用，

####类中的私有方法

```
__new__: 构造器，__new__必须返回一个合法的实例，这样解释在调用__init__时，就可以把实例作为self传递
__init__ : 实例创建后第一个被调用的方法，在这里可以设计实例属性
__del__ : 析构函数，释放对象时使用
__dict__: 获取类的属性. dir方法同样满足需求
__dalattr__:
__doc__:

__module__:

# 特殊类属性
C.__name__: 类C的名字
C.__doc__: 类C的文档字符串
C.__bases__: 类C的所有父类构成的元祖
C.__dict__: 类C的属性
C.__module__: 类C定义所在的模块
C.__class__: 实例C所对应的类
C.__mro__: 查找顺序属性


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



### 面向对象 OOD，OOP

面向对象设计（Object-oriented Design,OOD）

面向对象编程（Object-oriented Programming,OOP）



- 抽象／实现

  抽象是指对现实世界问题和实体的本质表现、行为和特征建模。



> Python 中的合成问题？
>
> 类像一个Python容器类型
>
> Python 不支持虚方法／抽象方法， 在基类中引发 NotImplementedError异常，获得类似的效果



### 类属性

类属性仅与被定义的类相绑定

实例数据属性是一直会用到的主要数据属性。

类数据属性仅当需要有更加‘静态’数据类型时才变的有用，和任何实例都无关。

（ 一个类中的一些数据对所有的实例来说，都是固定的）



数据属性：仅仅是所定义的类的变量，在类创建后被使用，要么由类中的方法更新，要么在主程序中被更新。

静态变量、静态数据，表示这些数据与所属类对象绑定的，不依赖任何类实例。相当于static 关键字。

方法名是类的属性，但却不能用类对象 来调用类方面，Python 中方法必须绑定到一个实例才能直接被调用



**默认构造器**

**`__init__()`** 应当返回None。

```
__init__() 不应当返回任何对象，因为实例对象是自动在实例化后调用返回的。
# 自我理解，在 __new__()创建实例后，调用 __init__()函数对实例做初始化，才导致__init__()不能返回实例。 还需要看源代码 才能确认
```

内建类型属性：

 ```
>> x = 3+0.14j
>> x.__class__
>> dir(x)

Out[107]: 
['__abs__', '__add__', '__bool__', '__class__','__delattr__','__dir__',
 '__divmod__','__doc__','__eq__','__float__','__floordiv__','__format__',
 '__ge__','__getattribute__','__getnewargs__','__gt__','__hash__','__init__',
 '__init_subclass__',
 '__int__',
 '__le__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__neg__',
 '__new__',
 '__pos__',
 '__pow__',
 '__radd__',
 '__rdivmod__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rfloordiv__',
 '__rmod__',
 '__rmul__',
 '__rpow__',
 '__rsub__',
 '__rtruediv__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__sub__',
 '__subclasshook__',
 '__truediv__',
 'conjugate',
 'imag',
 'real']

 ```

内建类型访问 `__dict__`  会失败，因为在内建类型中，不存在这个属性。



### 实例属性 VS 类属性

类属性：是与类相关的数据值。和实例无关，这些值像静态成员那样被引用，静态成员不会因为实例而改变值，实例中显示修改，也只是声明了一个同名实例属性而已。

实例属性：



类和实例都有名字空间，类事类属性的名称空间，实例事实例属性的。

类属性和实例属性，需要指出，可以采用类来访问类属性，如果实例没有同名属性，也可以用实例来访问。

**类属性可以通过类和实例来访问**

```python
calss C(object)
	version = 1.2
	
c = C()		# 实例化
C.version   # 通过类来访问
1.2
c.version.  # 通过类实例访问
1.2

C.version += 0.1   # 通过类 来更新
C.version
1.3

c.version			# 实例访问它，其值已被改变
1.3
```



> 当使用类引用version 时，才能更新类属性。
>
> 如果尝试在实例中设定或更新类属性会创建一个实例属性   c.version , 这个实例属性会阻止，实例对类属性C.version 的访问。
>
> 任何对实例属性的赋值都会创建一个实例属性。
>
> 删掉类属性
>
> del foo.x
>
> 再删一次就会报错
>
> AttributeError: l1
>
> 类属性存储 dict\list 类的变量时。
>
> 没有遮蔽不能删除掉。

```
class Foo(object):
	x = {2003: 'poe2'}
foo = Foo()
foo.x
{2003: 'poe2'}
foo.x[2004] = 'valid'
foo.x
{2003: 'poe2', 2004: 'valid'}
Foo.x 				# 修改生效
{2003: 'poe2', 2004: 'valid'}
del foo.x 			# 没有遮蔽所以不能删除掉
AttributeError: x

```



### 绑定和方法调用

调用绑定方法：

调用非绑定方法：



###  静态方法和类方法

staticmethod

class method



`__bases__类属性` 对任何（子类），它是一个包含其父类的集合的元组。但不会包含父类的父类（爷爷类）

调用未绑定的基类方法，需要明确给出类的实例：

```
class C(P):
	def foo(self):
		P.foo(self)		# 显式调用父类方法
		super().foo()	# 更好的办法是使用super() 内建方法，super 为我们找到基类，并传进self
```

```
重写 __init__ 后不会自动调用基类的 __init__  这一点和JAVA是不一样的
```

**从标准类中派生**

```
# 不可变类型的例子
class RondFloat(float):
	def __new__(cls, val):
		# 使用round()函数对原型进行类舍入操作。
		return super().__new__(cls, round(val, 2))
		
# 可变类型的例子

```



**多重继承**

1 方法解释顺序（MRD）

事例：

```
class P1(object):			# 父类1
	def foo(self):
		print ('called P1-foo()')
class P2(object):			# 父类2
	def foo(self):
		print ('called P2-foo()')
	def bar(self):
		print('called P2-bar()')
class C1(P1, P2):			# 子类1，从 P1 P2 中派生
	pass
	
class C2(P1, P2):			# 子类2，从P1 P2 中派生
	def bar(self):	
		print('called C2-bar()')

class GC(C1, C2):		   # 定义子孙类
	pass
	
# 经典类的解释顺序，深度优先，从左向右
gc = GC()
gc.foo()		# GC => C1 => P1
called P1-foo()

gc.bar()		# GC => C1 => P1 => P2
called P2-bar()
# 首先在当前类(GC)中查找，没找到就向上查找最亲的父类C1, 未找到，就沿着树访问父类P1

# 新式类，广度优先
gc = GC()
gc.foo()		# GC => C1 => C2 => P1
called P1-foo()

gc.bar()		# GC => C1 => C2
called P2-bar()


```

经典MRO是由于，所有从object 派生出的类的继承结构变成了一个菱形



#### 类、实例和其它对象的内建函数

issubclass(sub, sup) ：判断sub 是否是sup 的子类

isinstance(obje1, obje2) ：判断obj1 是否是类obj2 的一个实例或孙子类实例 

hasattr(obje1, attribute) ：判断一个实例obje1是否有某个属性（attribute）

getattr(obje1, attribute) ：获取对象obje1的attribute的值

serattr(obje1, attribute) ：写入

delattr(obje1, attribute) ：删除

dir() : 列出一个模块的所有属性信息

super() : 找到相应的父类

vars() : 返回一个模块的属性键-值对

#### 用特殊方法定制类

包括了所有的 以双下滑线(__)开始以及结尾的类。 

```
将__repr__()作为__str__()的一个别名，就可以实现，__repr__()与__str__()使用__str__()的代码实习，而不必复制过去。

__repr__ = __str__

# 重载原位操作
重载一个__i*__()方法的唯一秘密是它必须返回 self
例如：
__repr__ = __str__
def __iadd__(self, other):
	self.hr += other.hr
	self.min += other.min
	return self
```

#### *授权

**包装** 对一个已存在的对象进行包装，可以是对一个已存在的对象增加新的、删除不要的或修改其它已存在的功能。

**授权**  包装的一个特性，用于简化处理相关命令性的功能，采用已存在的功能达到最大限度的代码重用。

​           授权的过程，即是所有更新的功能都是由新类的某部分来处理，存在功能就授权给对象的默认属性。

​	实现授权的关键点就是覆盖`__getattr__()`方法，在代码中包含一个对getattr()内建函数的调用，得到默认对象属性（数据属性或者方法）并返回它以便访问或调用。

**包装对象的简例**

```python
# 包装器
class WrapMe(object):
	def __init__ (self, obj):
		self.__data = obj
	def get(self):
		return self.__data
	def __repr__(self):
		return 'self.__data'    # 这里不是很明白，后面会处理
	def __str__(self):
		return srr(self.__data)
	def __getattr__(self, attr):
		return getattr(self,__data, attr)

wrappedList = WrapMe([123, 'foo', 45.5])
wrappedList.append('bar')
wrappedList.append(123)
wrappedList
[123, 'foo', 45.67, 'bar', 123]
wrappedList.index(45.67)
2
wrappedList.count(123)
2
wrappedList.pop()
123
wrappedList
[123, 'foo', 45.67, 'bar']

# 包装器只对已存在的方法进行授权，而特殊行为没有在类型的方法列表中，不能被访问，因为它们不是属性，只有通过访问实际对象【通过我们的get()方法】去访问，如切片能力。
# get()方法返回被包装的对象。
wrappedList.get()[3]
'bar'


__slots__ 类属性 ，由一序列型对象组成，由所有合法标识构成的实例属性的集合来表示。
__getattribute__() 当属性不能在实例的__dict__或它的类、或者祖先类中找到时，才会被调用。
优先级别：对__getattribute__()方法的执行方式做一个介绍。
类属性
数据描述符
实例属性
非数据描述符
默认为__getattr__()


```

OLD (not as good) 老的

Better 好

Even betert 更好



**描述符**

描述符是表示对象属性的一个代理。当需要属性时，可根据情况（通过描述符（如果有）或者采用常规方式（句点属性标识法）来访问它）

如果你的对象有代理，并且这个代理有一个“get”属性（实际为`__get__`），当这个代理被调用时，你就可以访问这个对象了。同样适用 set、delete.