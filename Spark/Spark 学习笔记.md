# Spark 学习笔记

## RDD

用户可以使用两种方法创建 RDD:

- 读取一个外部数据集，我们在本书前面的章节中已经见过使用 SparkContext. textFile() 来读取文本文件作为一个字符串 RDD 的示例，
- 在驱动器程序里分发驱动器程 序中的对象集合(比如 list 和 set)。



RDD 支持两种类型的操作:

**转化操作**(transformation)和**行动操作** 

**转化操作**会由一个 RDD 生成一个新的 RDD。例如，根据谓词匹配情况筛选数 据就是一个常见的转化操作。在我们的文本文件示例中，我们可以用筛选来生成一个只存 储包含单词 Python 的字符串的新的 RDD，如例 3-2 所示。 

例 3-2:调用转化操作 filter()
 \>>> pythonLines = lines.filter(lambda line: "Python" in line) 





**行动操作**会对 RDD 计算出一个结果，并把结果返回到驱动器程序中，或把结 果存储到外部存储系统(如 HDFS)中。first() 就是我们之前调用的一个行动操作，它 会返回 RDD 的第一个元素，如例 3-3 所示。 

例 3-3:调用 first() 行动操作 >>> pythonLines.first() 

```
      u'## Interactive Python Shell'
```





总的来说，每个 Spark 程序或 shell 会话都按如下方式工作。 

1. (1)  从外部数据创建出输入 RDD。 
2. (2)  使用诸如 filter() 这样的转化操作对 RDD 进行转化，以定义新的 RDD。 
3. (3)  告诉 Spark 对需要被重用的中间结果 RDD 执行 persist() 操作。 
4. (4)  使用行动操作(例如 count() 和 first() 等)来触发一次并行计算，Spark 会对计算进行 优化后再执行。 



## 创建RDD

​	创建RDD的方式：

- 读取外部数据集
- 在驱动器程序中对一个集合进行并行化



​	创建 RDD 最简单的方式就是把程序中一个已有的集合传给 SparkContext 的 parallelize() 方法，如例 3-5 至例 3-7 所示。这种方式在学习 Spark 时非常有用，它让你可以在 shell 中 快速创建出自己的 RDD，然后对这些 RDD 进行操作。不过，需要注意的是，除了开发原 型和测试时，这种方式用得并不多，毕竟这种方式需要把你的整个数据集先放在一台机器 的内存中。 

val lines = sc.parallelize(List("pandas", "i like pandas")) AW



更常用的方式是从外部存储中读取数据来创建 RDD。外部数据集的读取会在第 5 章详 细介绍。不过，我们已经接触了用来将文本文件读入为一个存储字符串的 RDD 的方法 SparkContext.textFile()，用法如例 3-8 至例 3-10 所示。 

lines = sc.textFile("/path/to/README.md") 





RDD 的转化操作是返回一 个新的 RDD 的操作，比如 map() 和 filter()， 

行动操作则是向驱动器程序返回结果或 把结果写入外部系统的操作，会触发实际的计算，比如 count() 和 first()。 

如 果对于一个特定的函数是属于转化操作还是行动操作感到困惑，你可以看看它的返回值类 型:转化操作返回的是 RDD，而行动操作返回的是其他的数据类型。 



最后要说的是，通过转化操作，你从已有的 RDD 中派生出新的 RDD，Spark 会使用谱系 图(lineage graph)来记录这些不同 RDD 之间的依赖关系。Spark 需要用这些信息来按需 计算每个 RDD，也可以依靠谱系图在持久化的 RDD 丢失部分数据时恢复所丢失的数据。 图 3-1 展示了例 3-14 中的谱系图。 

图 3-1:日志分析过程中创建出的 RDD 谱系图 



 

## 常见的RDD转化操作, 数据为{1, 2, 3, 4}

| 函数                                         | 目的                                                         | 示例                                     | 结果                  |
| -------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------- | --------------------- |
| map()                                        | 将函数应用于 RDD 中的每个元 素，将返回值构成新的 RDD         | rdd.map(x => x + 1)                      | {2, 3, 4, 4}          |
| flatMap()                                    | 将函数应用于 RDD 中的每个元 素，将返回的迭代器的所有内 容构成新的 RDD。通常用来切 分单词 | rdd.flatMap(x => [x.to](http://x.to)(3)) | {1, 2, 3, 2, 3, 3, 3} |
| filter()                                     | 返回一个由通过传给 filter() 的函数的元素组成的 RDD           | rdd.filter(x => x != 1)                  | {2, 3, 3}             |
| distinct()                                   | 去重                                                         | rdd.distinct()                           | {1. 2. 3}             |
| sample(withRe placement， fraction， [seed]) | 对 RDD 采样，以及是否替换                                    | rdd.sample(false, 0.5)                   | 非确定的              |

> map() : **对 RDD中的所有数求平方**

```scala
val input = sc.parallelize(List(1, 2, 3, 4))
val result = input.map(x => x * x)
println(result.collect().mkString(","))

>>
1,4,9,16 
```



> flatMap() :  **对RDD中每个输入元素生成多个输出元素** 

​	返回值：**返回值序列的迭代器**

​	应用：  将输入的字符串切分为单词

```Scala
val lines = sc parallelize(List("hello world", "hi"))
val words = lines.flatMap(line => line.split(" "))
words.first()

>>
String = hello
```





## 针对两个RDD 的集合转化操作，数据为{1, 2, 3}, {3, 4, 5}



- **union**(other)：并集，返回一个包含两个 RDD 中所有元素的 RDD。这 在很多用例下都很有用，比如处理来自多个数据源的日志文件。 
- **intersection**(other)：交集，只返回两个 RDD 中都有的元素。intersection() 在运行时也会去掉所有重复的元素(单个 RDD 内的重复元素也会一起移除)。 
- **subtract**(other)：函数接收另一个 RDD 作为参数，返回 一个由只存在于第一个 RDD 中而不存在于第二个 RDD 中的所有元素组成的 RDD。和 intersection() 一样，它也需要数据混洗。 
- **cartesian**(other)：计算两个 RDD的笛卡尔积， 转化操作会返回 所有可能的 (a, b) 对，其中 a 是源 RDD 中的元素，而 b 则来自另一个 RDD。笛卡儿积在 我们希望考虑所有可能的组合的相似度时比较有用，比如计算各用户对各种产品的预期兴 趣程度。 求大规模 RDD 的笛卡儿积开销巨大。

| 函数名         | 目的                                     | 示例                    | 结果                        |
| -------------- | ---------------------------------------- | ----------------------- | --------------------------- |
| union()        | 生成一个包含两个 RDD 中所有元 素的 RDD   | rdd.union(other)        | {1, 2, 3, 3, 4, 5}          |
| intersection() | 求两个 RDD 共同的元素的 RDD              | rdd.intersection(other) | {3}                         |
| subtract()     | 移除一个 RDD 中的内容(例如移 除训练数据) | rdd.subtract(other)     | {1, 2}                      |
| cartesian()    | 与另一个 RDD 的笛卡儿积                  | rdd.cartesian(other)    | {{1, 3}, {1, 4}, ,,,{3, 5}} |

  

## RDD的行动操作

- **reduce()**: 接收一个函数作为参数，这个函数要操作两个RDD的元素类型并返回一个同样类型的新元素。累加
- **fold()**: 接收一个与reduce() 接收的函数签名相同的函数，再加上一个"初始值"来作为每一个分区第一次调用时的结果
- **aggregate()**：需要提供我们期待返回的类型的初始值，然后通过一个函数把RDD中的元素合并起来放入累加器，还需要提供第二个函数来将累加器两两合并。



fold() 和 reduce() 要求函数的返回值类型需要 和 我们所操作的RDD中的元素类型相同，这很符合像sum  这种操作的情况， 但 有时 我们确实需要返回一个不同类型的值。可以先对数据使用map()操作， 来把元素转为该元素和1的二元组，这样reduce() 就可以以二元组的形式进行归约。

> reduce() 

```Scala
val rdd = sc.parallelize(List(1, 2, 3, 4))
val sum = rdd.reduce((x, y) => x + y)

>>
sum: Int = 10
```

> fold()

```Scala

```

> aggregate()

```Scala
val rdd = sc.parallelize(List(1, 2, 3, 4))
val result = rdd.aggregate((0, 0))(
    (acc, value) => (acc._1 + value, acc._2 +1), 
    (acc1, acc2) => (acc1._1 + acc2._1, acc1._2 + acc2._2))
val avg = result._1 / result._2.toDouble

>>
avg: Double = 2.5

```

​	

单元测试、快速调试

- **collect() :** 将整个RDD 的内容返回驱动器程序，要求所有数据都必须能一同放入单台机器的内存中。
- **take(n) :** 返回RDD中的n 个元素，并且尝试只访问尽量少的分区，得倒一个不均衡的集合。
- **top(n) :** 从RDD中获取前几个元素，使用数据的默认顺序。
- **takeSample(withReplacement, num, seed) :** 从数据中获取一个采样，并指定是否替换。
- **foreach() :**  对RDD中的每个元素进行操作，而不需要把RDD发回本地。
- **count() :** 用来返回元素的个数。
- **countByValue() :** 返回一个从各值到值对应的计数的映射表。

**RDD基本的行动操作**

| 函数名                                    | 目的                                        | 示例                                                         | 结果                           |
| ----------------------------------------- | ------------------------------------------- | ------------------------------------------------------------ | ------------------------------ |
| collect( )                                | 返回RDD中的所有元素                         | rdd.collect()                                                | {1, 2, 3, 3}                   |
| count( )                                  | RDD中的元素个数                             | rdd.count()                                                  | 4                              |
| countByValue( )                           | 各元素在RDD中出现的次数                     | rdd.countByvalue()                                           | { (1, 1),  (2, 1),  (3, 2),  } |
| take( num )                               | 从RDD中返回num个元素                        | rdd.take(2)                                                  | {1, 2}                         |
| top( num )                                | 从RDD中按照提供的顺序返回最前面的num 个元素 | [rdd.top](http://rdd.top)( 2 )                               | {3, 3}                         |
| takOrdered( num )  ( ordering )           | 从RDD中按照提供的顺序返回最前面的num个元素  | rdd.takeOrdered(2)(myOrdering)                               | {3, 3}                         |
| takeSample( withReplacement, num, [seed]) | 从RDD中返回任意一些元素                     | rdd.takeSample(false, 1)                                     | 非确定的                       |
| reduce( func )                            | 并行整合RDD中所有数据(例如sum)              | rdd.reduce( (x, y) =>  x + y)                                | 9                              |
| fold( zero )( func )                      | 和reduce() 一样，但是需要提供初始值         | rdd,fold(0)( (x, y) => x + y)                                | 9                              |
| aggregate(zeroValue)(seqOp, combOp)       | 和reduce() 相似，但是通常返回不同类型的函数 | rdd.aggregate((0, 0))( (x, y) => (x._1 +y, x._2 + 1),   (x, y) => (x._1 + y._1, x._2 + y._2)   ) | (9, 4)                         |
| foreach( func )                           | 对RDD中的每个元素使用给定的函数             | rdd.foreach(func)                                            | 无                             |

## 初始ETL （抽取、转化、装载）

通过ETL 将数据转化为想要的形式，如键值对形式。



# 键值对操作

## pairRDD ( 包含键值对类型的RDD，包含二元组) 

- reduceByKey() 方法， 可以分别归约每个键对应的数据。
- join()  方法， 可以把两个RDD中键相同的元素组合到一起，合并为一个RDD。



Pair RDD 的转化操作，数据为键值对集合{ }

### Pair RDD 的转化操作(以键值对集合{(1, 2), (3, 4), (3, 6)} 为例

| 函数名                                                       | 目的                                                         | 示例                             | 结果                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------- | ------------------------------------------------- |
| reduceByKey(func)                                            | 合并具有相同键的值                                           | rdd.reduceByKey((x, y) => x + y) | {(1, 2), (3,  10)}                                |
| groupByKey()                                                 | 对具有相同键的值进行分组                                     | rdd.groupByKey()                 | {(1,  [2]), (3, [4, 6])}                          |
| combineBy  Key( createCombiner, mergeValue, mergeCombiners, partitioner) | 使用不同的返回类型合并具有 相同键的值                        |                                  |                                                   |
| mapValues(func)                                              | 对 pair RDD 中的每个值应用 一个函数而不改变键                | rdd.mapValues(x => x+1)          | {(1, 3), (3,  5), (3,  7)}                        |
| flatMapValues(func)                                          | 对 pair RDD 中的每个值应用 一个返回迭代器的函数，然后 对返回的每个元素都生成一个 对应原键的键值对记录。通常 用于符号化 | rdd.flatMapValues(x => (x to 5)) | {(1,  2), (1, 3), (1, 4), (1, 5), (3, 4), (3, 5)} |
| keys()                                                       | 返回一个仅包含键的 RDD                                       | rdd.keys()                       | {1, 3, 3}                                         |
| values()                                                     | 返回一个仅包含值的 RDD                                       | rdd.values()                     | {2, 4. 6}                                         |
| sortByKey()                                                  | 返回一个根据键排序的 RDD                                     | rdd.sortByKey()                  | {(1,  2), (3, 4), (3, 6)}                         |

### 针对两个Pair RDD  的转化操作( rdd = {(1, 2), (3, 4), (3.6)) other = {(3.9)}

| 函数名         | 目的                                                         | 示例                      | 结果                                               |
| -------------- | ------------------------------------------------------------ | ------------------------- | -------------------------------------------------- |
| subtractByKey  | 删掉 RDD 中键与 other RDD 中的键相同的元素                   | rdd.subtractByKey(other)  | {(1, 2)}                                           |
| join           | 对两个 RDD 进行内连接                                        | rdd.join(other)           | {(3, (4, 9)), (3, (6, 9))}                         |
| rightOuterJoin | 对两个 RDD 进行连接操作，确保第一 个 RDD 的键必须存在(右外连接) | rdd.rightOuterJoin(other) | {(3,(Some(4),9)), (3,(Some(6),9))}                 |
| leftOuterJoin  | 对两个 RDD 进行连接操作，确保第二 个 RDD 的键必须存在(左外连接) | rdd.leftOuterJoin(other)  | {(1,(2,None)), (3, (4,Some(9))), (3, (6,Some(9)))} |
| cogroup        | 将两个 RDD 中拥有相同键的数据分组 到一起                     | rdd.cogroup(other)        | {(1,([2],[])), (3, ([4, 6],[9]))}                  |

```
 val ts1 = pairs.filter{case (key, value) => value.length < 8} 
 ts1.collect()
 >>
 res5: Array[(String, String)] = Array((test,test), (123,123 456))
 
```

ad86dbed1555

### 聚合操作

归约会将键相同的值合并起来

reduceByKey() 与 reduce() 相当类似;它们都接收一个函数，并使用该函数对值进行合并。 

reduceByKey()  会返回一个由各键和对应键归约出来的结果值组成的新的 RDD。

foldByKey() 则与 fold() 相当类似;它们都使用一个与 RDD 和合并函数中的数据类型相 同的零值作为初始值。 与 fold() 一样，foldByKey() 操作所使用的合并函数对零值与另一 个元素进行合并，结果仍为该元素 



使用 reduceByKey() 和 mapValues() 来计算每个键的对应值的 均值 

```

```



