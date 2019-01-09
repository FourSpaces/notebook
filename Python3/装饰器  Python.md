### 装饰器  Python

装饰模式有很多经典的使用场景，例如插入日志、性能测试、事务处理等等，有了装饰器，就可以提取大量函数中与本身功能无关的类似代码，从而达到代码重用的目的。下面就一步步看看Python中的装饰器。

**一个简单的需求**

现在有一个简单的函数”myfunc”，想通过代码得到这个函数的大概执行时间。

我们可以直接把计时逻辑方法”myfunc”内部，但是这样的话，如果要给另一个函数计时，就需要重复计时的逻辑。所以比较好的做法是把计时逻辑放到另一个函数中（”deco”），如下：

![img](http://ww4.sinaimg.cn/mw690/aa213e02gw1ewkmoy2p8sj20kh09iq4j.jpg)

但是，上面的做法也有一个问题，就是所有的”myfunc”调用处都要改为”deco(myfunc)”。

下面，做一些改动，来避免计时功能对”myfunc”函数调用代码的影响：

![img](http://ww3.sinaimg.cn/mw690/aa213e02gw1ewkmoz5pd6j20n70brtb1.jpg)

经过了上面的改动后，一个比较完整的装饰器（deco）就实现了，装饰器没有影响原来的函数，以及函数调用的代码。例子中值得注意的地方是，Python中一切都是对象，函数也是，所以代码中改变了”myfunc”对应的函数对象。

**装饰器语法糖**

在Python中，可以使用”@”语法糖来精简装饰器的代码：

![img](http://ww4.sinaimg.cn/mw690/aa213e02gw1ewkmp09vp8j20lo0b8taq.jpg)

使用了”@”语法糖后，我们就不需要额外代码来给”myfunc”重新赋值了，其实”@deco”的本质就是”myfunc = deco(myfunc)”，当认清了这一点后，后面看带参数的装饰器就简单了。

**被装饰的函数带参数**

前面的例子中，被装饰函数的本身是没有参数的，下面看一个被装饰函数有参数的例子：

![img](http://ww2.sinaimg.cn/mw690/aa213e02gw1ewkmp1eh7mj20l60b9q51.jpg)

从例子中可以看到，对于被装饰函数需要支持参数的情况，我们只要使装饰器的内嵌函数支持同样的签名即可。

也就是说这时，”addFunc(3, 8) = deco(addFunc(3, 8))”。

这里还有一个问题，如果多个函数拥有不同的参数形式，怎么共用同样的装饰器？在Python中，函数可以支持(*args, **kwargs)可变参数，所以装饰器可以通过可变参数形式来实现内嵌函数的签名。

**带参数的装饰器**

装饰器本身也可以支持参数，例如说可以通过装饰器的参数来禁止计时功能：

![img](http://ww1.sinaimg.cn/mw690/aa213e02gw1ewkmp3cmxsj20p50jkn15.jpg)

通过例子可以看到，如果装饰器本身需要支持参数，那么装饰器就需要多一层的内嵌函数。

这时候，”addFunc(3, 8) = deco(True)( addFunc(3, 8))”，”myFunc() = deco(False)( myFunc ())”。

**装饰器调用顺序**

装饰器是可以叠加使用的，那么这是就涉及到装饰器调用顺序了。对于Python中的”@”语法糖，装饰器的调用顺序与使用 @ 语法糖声明的顺序相反。

![img](http://ww4.sinaimg.cn/mw690/aa213e02gw1ewkmp48x12j20ld0cd40w.jpg)

在这个例子中，”addFunc(3, 8) = deco_1(deco_2(addFunc(3, 8)))”。

**Python内置装饰器**

在Python中有三个内置的装饰器，都是跟class相关的：staticmethod、classmethod 和property。

- staticmethod 是类静态方法，其跟成员方法的区别是没有 self 参数，并且可以在类不进行实例化的情况下调用
- classmethod 与成员方法的区别在于所接收的第一个参数不是 self （类实例的指针），而是cls（当前类的具体类型）
- property 是属性的意思，表示可以通过通过类实例直接访问的信息

对于staticmethod和classmethod这里就不介绍了，通过一个例子看看property。

![img](http://ww1.sinaimg.cn/mw690/aa213e02gw1ewkmp5xioqj20ij09m3zr.jpg)

注意，对于Python新式类（new-style class），如果将上面的 “@var.setter” 装饰器所装饰的成员函数去掉，则Foo.var 属性为只读属性，使用 “foo.var = ‘var 2′” 进行赋值时会抛出异常。但是，对于Python classic class，所声明的属性不是 read-only的，所以即使去掉”@var.setter”装饰器也不会报错。

**总结**

本文介绍了Python装饰器的一些使用，装饰器的代码还是比较容易理解的。只要通过一些例子进行实际操作一下，就很容易理解了。