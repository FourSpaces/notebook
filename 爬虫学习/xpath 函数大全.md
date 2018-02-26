# [

# xpath 函数大全](http://www.cnblogs.com/cxd4321/archive/2007/09/24/903917.html)

在本文的第一部分中，我们介绍了XPath并讨论了各种各样的从简单到复杂的XPath查询。 通过把XPath查询应用到XML示例文件，我们详细说明了各种重要的XPath定义比如location step、context node、location path、axes和node - test。 我们然后讨论了多个简单查询组合成的复杂的XPath查询。 我们还讨论了无线二进制XML（WBXML）--XML在无线应用领域的对应物--的抽象结构。 最后我们介绍一个简单的XPath处理引擎的设计。
　　在这一部分里，我们打算讨论XPath的更进一步的特性--在一个XML文件上执行复杂检索的操作。 我们将讨论谓词或者过滤器查询以及在XPath中的函数的使用。我们将介绍各种的用于处理WSDL和WML的XPath查询。 我们还将增强我们的XPath引擎的功能，使之包括谓词、函数和不同的数据类型。
　　**过滤查询和谓词**
　　让我们从一个将返回任何XML文件当中的根节点的简单查询开始： 
　　./node()
　　我们可以更进一步，使用另一个简单查询，选择根节点的全部的直接子节点： 
　　./node()/*
　　如果你想要得到所有的是根节点的直接子节点并且只有一个type属性的节点，那么该怎么办呢？ 那么就使用下面的这个查询： 
　　./node()/*[attribute::type]
　　在代码段1中，这个查询将返回binding元素。 由此可见，写在方括号之内的代码attribute::query担负一个过滤器的功能。 XPath中的过滤器被称作谓词（predicate），写在方括号内。 一个谓词作用在一个结点集上--在这个例子中，结点集由根节点的所有的直接子节点组成---应用过滤条件(在这里，结点肯定有一个type属性)到结点集上。 产生的结果就是一个经过过滤的结点集。 
　　谓词可以从简单到很复杂。 也许XPath谓词的简单形式就像下面的查询中的只是一个数字，返回根元素的第二个子节点（message元素）： 
　　./node()/*[2]
　　查询语句./node()/message[attribute::name="TotalBill"]/text() 将寻找根元素的一个属性name值为TotalBill的特定的message子节点。 查询将返回特定的message元素的所有文本结点。 这个查询将返回代码段1中两个message元素中的第二个。 
　　**XPath 函数**
　　假定你想要回答下面对代码段1中的WSDL文件所提出的问题： 
      　　1. 最后一个operation元素的name属性的值是什么？
      2．定义元素有多少个message子元素？
      　　2. 根元素的第一个子元素的名称是什么？ 
      last()函数
      　　last()函数将总是指向结点集的最后一个结点。 下面的这个查询，当被应用于代码段1中的WSDL文件的时候，将返回第二message元素（即 名称是TotalBill的message元素）： 
      　　./node()/message[last()]
      　　注意下面的这条查询也返回相同的message元素： 
      　　./node()/message[2]
      　　这两个查询之间唯一的区别就是我们使用数字2来代替last()方法。 事实上在本例中last()函数返回的值就是2（特定location step的结点集中的结点数）。 把这两个相同的查询应用到代码段2中的WSDL文件，这次你会发现两个查询没有返回相同的结果。 代码段2中有三个message元素，所以现在last()函数返回数字3。 
      注意本讨论中的last()函数总是返回一个数字。
      　　position()函数
      　　如果你把下面的这些查询应用到代码段2中的WSDL文件， 
      　　./node()/message[1]/part
      　　./node()/message[2]/part
      　　./node()/message[3]/part
      　　它们将分别返回message元素的第一个、第二个和第三个part子元素。 由此可见节点集中的每个节点都有一个位置。 第一个节点的位置是1，第二个节点的位置是2，以此类推。 
      　　如果你想要得到除第二个以外的所有的message元素，你该怎么办？ 你可以使用position()函数取得一个节点的位置。 下面的这条查询将返回代码段2中的第一个和第三个message元素： 
      　　./node()/message[position()!=2]
      　　position()函数只是返回指定值所表示的节点的位置。 谓词[position()!=2] 把所有的message元素的位置和2做比较，然后找出位置不是2的节点。 
      　　count()函数
      　　代码段1中的portType元素有多少个message子元素？ 数一数你就发现有两个message元素。 在XPath中解决"多少个"这种问题是一个二步的操作。 首先，写一个用来找到你想要统计的所有的子元素的XPath查询。 然后地像下面给出的那样，把 XPath查询传送到count()函数中： 
      　　步骤1: ./node()/message
      　　步骤2: count(./node()/message) 
      　　count()函数统计XPath查询所得到的节点集中的节点数，并返回这个节点数。 
      　　name()、local-name()和namespace-uri()函数
      　　如果把下面的查询应用到代码段1中的WSDL文件的话，那么会出现什么情况呢？ 
      　　./node()/*[5]
      　　它返回根元素的第五个子元素（即service元素）。 service元素本身是一个完整结构，也包含子元素。 因此，这个XPath查询的返回值实际上是一个XML节点而不仅仅是一个元素名。 
      　　name()函数返回XML节点的名称。 例如，下面的查询应用到代码段1中将返回字符串"service"： 
      　　name(./node()/*[5])
      　　同样，下面的查询将返回字符串"wsd:definitions"（使用域名空间前缀的根元素的全名）：
      　　name(./node())
      　　local-name()和names
      pace-uri()函数与name()函数类似，除了local-name方法只返回不带域名空间前缀的元素的局部名称，而namespace-uri函数仅仅返回域名空间URI。举例来说，请在代码段1中试验下面的查询： 
      　　local-name(./node())
      　　namespace-uri(./node())
      　　第一个查询返回一个字符串" definitions"，而第二个查询返回" http://schemas.XMLsoap.org/wsdl/ "。 
      　　String函数
      　　我们已经知道name()、local-name()和namespace-uri()函数返回字符串。 XPath提供了许多函数用于处理字符串，比如string()、 substring()、substring-before()、 substring-after()、 concat()、starts-with()等等。 下面给出了一个例子来演示一下如何使用string()函数： 
      　　string(./node()/*[2]/part/attribute::name)
      　　上面的这条查询将寻找根元素的第二个子元素，然后它将得到根元素的第二子元素的所有的part子元素。 接着它将寻找part子元素的name属性，最后它把name属性的值转换为一个字符串格式。 当把这条语句应用到代码段1中的时候，它将输出bill。
      　　XPath也提供一些布尔函数，返回"true/false",研究一下下面的这条查询： 
      　　boolean(./node()/message)
      　　当把它应用到代码段1的时候，它返回true。 这是因为boolean()函数判断一个XPath查询产生的节点集是否为空（在我们的例子中，根元素包含两个message子元素）。 如果是空，boolean()函数返回false，否则返回true。 
      　　**一个复杂的WSDL处理实例**
      　　下面的WSDL处理方案使用了我们前面讨论过的所有的XPath概念。 这个方案的检索要求如下：
      　　寻找一个service元素，这个元素是definitions元素（根元素）的一个直接子元素，并且name属性与definitions元素的name属性匹配。 然后察看service元素，寻找一个port元素，这个port元素的binding属性与definitions元素的直接子元素binding的name属性匹配。
      　　这个WSDL过程可以用四步完成： 
      　　3. 查找definitions元素的name属性值。 下面给出的XPath查询（从代码段中返回字符串BillingService）执行这步操作： 
      string(//node()[1]/@name)
      　　4. 然后查找name属性匹配definitions元素的name的service元素。 下面的查询将返回所需要的service元素： 
      ./node()[1]/service[@name=string(//node()[1]/@name)]
      　　5. 然后查找binding元素的name属性值： 
      string(//node()[1]/binding/@name)
      　　6. 最后寻找需要的port元素： 
      ./node()[1]/service[@name=string(//node()[1]/@name)]
      　　/port[@binding=string(//node()[1]/binding/@name)]
      　　这个实例说明XPath谓词可以包含简单逻辑条件，函数调用乃至完整的XPath查询。
      　　使用XPath处理WML
      　　WML是WAP Forum定义的一种XML语言。 WML为小型设备的显示提供了一种表现格式。 WML对于一个小型设备就好像HTML对于一台个人电脑一样。
      　　想象一下，一个WML文件是由一组卡片(card)组成，每个卡片由一个card元素封装。 代码段３是一个简单WML文件，只包含两个card元素。
      　　下面的XPath查询将返回代码段3中包含在第一个卡片之内（这卡片id是" first"）的所有的p（paragraph）元素： 
      　　./node()/card[string(@id)="first"]/p
      　　下面这个查询返回第二个卡片中的第一段的文本内容： 
      　　string(./node()/card[string(@id)="second"]/p[1]/text())
      　　**实现XPath谓词与函数**
      　　我们现在将看看如何在我们前面的那个简单的XPath引擎中插入谓词与函数的支持。
      　　四个伪代码类XPathExpression（代码段4）、XPathLocationStep（代码段5）、XPathResult（代码段6）和Predicate（代码段7）组成了支持谓词与函数的更新的版本。 我们在上一篇文章介绍的XPath引擎的基础上，增加了下列功能，使之更加强大： 
      　　7. XPath可以返回各种类型的数据。 XPath可以返回节点、字符串、数字和布尔变量。 我们设计的XPath引擎只支持XML节点作为返回数据类型。 我们现在已经提供了一个名为XPathResult（见代码段6）的类来支持不同的数据类型。 基于我们的设计的实现需要扩展为每种数据类型分别地扩展XPathResult。 
      　　8. 更新的设计现在包括一个支撑函数的结构。 一个函数调用可以发生在一个XPath查询开始时，也可以发生在任何XPath location step。 因此，XPathExpression类（代码段4）和XPathLocationStep类（代码段5）现在都添加了对函数调用的支持。 
      　　9. 我们还提供了一个单独的类用于支持谓词（见代码段7）。 一个谓词可以只由一个逻辑条件组成也可以由一个完整的XPath查询组成。 因此，Predicate类构造器将判断谓词到底是一个完整的查询还是仅仅只是一个条件。 如果是一个完整的XPath查询，Predicate表达式将实例化一个新的XPathExpression对象，否则它将只是取得逻辑条件的值。
      **小结**
      　　在前面，我们讨论XPath中谓词与函数的语法和使用。 我们介绍WSDL和WML处理的实例并说明了如何构成更加复杂的XPath查询。 最后，我们增强了在第一篇文章中介绍的XPath引擎的功能。





## XPATH 做模糊查询

```
//div[contains(@class,"qualification")]//ul/li//img/@src
<div class="qualification fl" data-pid="">
          <h2 class="q-title">商家资质信息公示</h2>
          <ul class="fl">
            <p>营业执照</p>
            <li class="qualification-list fl">
              <div class="img-wrapper">
              <img src="http://p0.meituan.net/xianfu/c627e2db9eab0f3fcb47e158689798aa112470.jpg" class="">
              </div>
            </li>
          </ul>
          <ul class="fl">
            <p>餐饮服务许可证</p>
            <li class="qualification-list fl">
              <div class="img-wrapper">
              <img src="http://p1.meituan.net/xianfu/e3ea740f6df01106f816fc0d2974f78c275439.jpg" class="">
            </div>
            </li>
          </ul>
  </div>

```



starts-with ( ) 顾名思义，匹配一个属性开始位置的关键字

contains ( )  匹配一个属性值中包含的字符串

text ( )  匹配的是显示文本信息，此处也可以用来做定位用

eg

//input[starts-with(@name,'name1')]     查找name属性中开始位置包含'name1'关键字的页面元素

//input[contains(@name,'na')]         查找name属性中包含na关键字的页面元素

<a href="http://www.baidu.com">百度搜索</a>

xpath写法为 //a[text()='百度搜索'] 

或者 //a[contains(text(),"百度搜索")]