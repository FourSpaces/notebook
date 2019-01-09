## haversine

```Python
def haversine(lat1, lon1, lat2, lon2):
    MILES = 3959
    lat1, lon1, lat2, lon2 = map(np.deg2rad, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    total_miles = MILES * c
    return total_miles
```

haversine 资料： http://www.cocoachina.com/ios/20141118/10238.html



### 地理空间距离计算原理：

下面着重介绍我们最常用的基于球面模型的地理空间距离计算公式，推导也只需要高中数学知识即可。

![earthmodel.png](http://cc.cocimg.com/api/uploads/20141117/1416225116560603.png)

**经纬度距离计算示意图**

该模型将地球看成圆球，假设地球上有A(ja,wa)，B(jb,wb)两点（注：ja和jb分别是A和B的经度，wa和wb分别是A和B的纬度），A和B两点的球面距离就是AB的弧长，AB弧长=R*角AOB（注：角AOB是A跟B的夹角，O是地球的球心，R是地球半径，约为6367000米）。如何求出角AOB呢？可以先求AOB的最大边AB的长度，再根据余弦定律可以求夹角。



**如何求出AB长度呢？**

1）根据经纬度，以及地球半径R，将A、B两点的经纬度坐标转换成球体三维坐标；

![daum_equation_1.png](http://cc.cocimg.com/api/uploads/20141117/1416225138258162.png)

2）根据A、B两点的三维坐标求AB长度;

![daum_equation_2.png](http://cc.cocimg.com/api/uploads/20141117/1416225149375439.png)

3）根据余弦定理求出角AOB;

![daum_equation_3.png](http://cc.cocimg.com/api/uploads/20141117/1416225156306369.png)

4）AB弧长=R*角AOB.

![daum_equation_4.png](http://cc.cocimg.com/api/uploads/20141117/1416225162105290.png)





**3.Lucene使用的地理空间距离算法**

目前美团团购app后台使用lucene来筛选团购单子和商家，lucene使用了spatial4j工具包来计算地理空间距离，而spatial4j提供了多种基于球面模型的地理空间距离的公式，其中一种就是上面我们推导的公式，称之为球面余弦公式。还有一种最常用的是Haversine公式，该公式是spatial4j计算距离的默认公式，本质上是球面余弦函数的一个变换，之前球面余弦公式中有cos(jb-ja)项，当系统的浮点运算精度不高时，在求算较近的两点间的距离时会有较大误差，Haversine方法进行了某种变换消除了cos(jb-ja)项，因此不存在短距离求算时对系统计算精度的过多顾虑的问题。

1）Haversine公式代码

2）Haversine公式性能

目前北京地区在线服务有5w个POI，计算一遍距离需要7ms。现在数据增长特别快，未来北京地区POI数目增大到100w时，我们筛选服务仅计算距离这一项就需要消耗144多ms，性能十分堪忧。（注：本文测试环境的处理器为2.9GHz Intel Core i7，内存为8GB 1600 MHz DDR3，操作系统为OS X10.8.3，实验在单线程环境下运行）

![599.jpg](http://cc.cocimg.com/api/uploads/20141117/1416225210219401.jpg)

**4.优化方案**

通过抓栈我们发现消耗cpu较多的线程很多都在执行距离公式中的三角函数例如atan2等。因此我们的优化方向很直接---消减甚至消除三角函数。基于此方向我们尝试了多种方法，下文将一一介绍。

4.1 坐标转换方法

1）基本思路

之前POI保存的是经纬度（lon,lat），我们的计算场景是计算用户位置与所有筛选出来的poi的距离，这里会涉及到大量三角函数计算。一种优化思路是POI数据不保存经纬度而保存球面模型下的三维坐标（x,y,z），映射方法如下：

x = Math.cos(lat) Math.cos(lon);

y = Math.cos(lat) Math.sin(lon);

z = Math.sin(lat);

那么当我们求夹角AOB时，只需要做一次点乘操作。比如求(lon1,lat1）和 (lon2,lat2）的夹角，只需要计算x1x2 + y1y2 + z1*z2， 这样避免了大量三角函数的计算。

在得到夹角之后，还需要执行arccos函数，将其转换成角度，AB弧长=角AOB*R（R是地球半径）。

此方法性能如下：

![58.jpg](http://cc.cocimg.com/api/uploads/20141117/1416225269875578.jpg)

2）进一步优化

美团是本地生活服务，我们的业务场景是在一个城市范围内进行距离计算，因此夹角AOB往往会比较小，这个时候sinAOB约等于AOB，因此我们可以将 Math.acos(cosAOB)R 改为Math.sqrt(1 - cosAOBcosAOB)*R，从而完全避免使用三角函数，优化后性能如下。

![59.jpg](http://cc.cocimg.com/api/uploads/20141117/1416225280734992.jpg)

4.2 简化距离计算公式方法

1）基本思路

我们的业务场景仅仅是在一个城市范围内进行距离计算，也就是说两个点之间的距离一般不会超过200多千米。由于范围小，可以认为经线和纬线是垂直的，如图所示，要求A（116.8，39,78）和B（116.9，39.68）两点的距离，我们可以先求出南北方向距离AM，然后求出东西方向距离BM，最后求矩形对角线距离，即sqrt(AMAM + BMBM)。

![latlng.png](http://cc.cocimg.com/api/uploads/20141117/1416225308821010.png)

简化距离计算示意图

南北方向AM = R纬度差Math.PI/180.0；

东西方向BM = R经度差Cos<当地纬度数* 180.0="">

这种方式仅仅需要计算一次cos函数。

我们对这个方法的有效性和性能进行验证。

1.1）有效性验证

我们首先检验这种简化是否能满足我们应用的精度，如果精度较差将不能用于实际生产环境。

我们的方法叫distanceSimplify，lucene的方法叫distHaversineRAD。下表是在不同尺度下两个方法的相差情况。

![00.jpg](http://cc.cocimg.com/api/uploads/20141117/1416225361690258.jpg)

可以看到两者在百米、千米尺度上几乎没有差别，在万米尺度上也仅有分米的差别，此外由于我们的业务是在一个城市范围内进行筛选排序，所以我们选择了北京左下角和右上角两点进行比较，两点相距有260多千米，两个方法差别17m。从精度上看该优化方法能满足我们应用需求。

1.2）性能验证

![5555.jpg](http://cc.cocimg.com/api/uploads/20141117/1416225392181973.jpg)

2）进一步优化

我们看到这里计算了一次cos这一三角函数，如果我们能消除此三角函数，那么将进一步提高计算效率。

如何消除cos三角函数呢？

采用多项式来拟合cos三角函数，这样不就可以将三角函数转换为加减乘除了嘛！

首先决定多项式的最高次数，次数为1和2显然都无法很好拟合cos函数，那么我们选择3先尝试吧，注：最高次数不是越多越好，次数越高会产生过拟合问题。

使用org.apache.commons.math3这一数学工具包来进行拟合。中国的纬度范围在10~60之间，即我们将此区间离散成Length份作为我们的训练集。

我们对此优化方法进行有效性和性能验证。

2.1）有效性验证

我们的优化方法叫distanceSimplifyMore，lucene的方法叫distHaversineRAD，下表是在不同尺度下两个方法的相差情况。

![32.jpg](http://cc.cocimg.com/api/uploads/20141117/1416225462258419.jpg)

可以看到在百米尺度上两者几乎未有差别，在千米尺度上仅有分米的区别，在更高尺度上如72千米仅有5.6m米别，在264千米也仅有8.1米区别，因此该优化方法的精度能满足我们的应用需求。

2.2）性能验证

![33.jpg](http://cc.cocimg.com/api/uploads/20141117/1416225475446193.jpg)

**5.实际应用**

坐标转换方法和简化距离公式方法性能都非常高，相比lucene使用的Haversine算法大大提高了计算效率，然而坐标转换方法存在一些缺点：

a）坐标转换后的数据不能被直接用于空间索引。lucene可以直接对经纬度进行geohash空间索引，而通过空间转换变成三维数据后不能直接使用。我们的应用有附近范围筛选功能（例如附近5km的团购单子），通过geohash空间索引可以提高范围筛选的效率；

b）坐标转换方法增大内存开销。我们会将坐标写入倒排索引中，之前坐标是2列（经度和纬度），现在变成3列（x,y,z），在使用中我们往往会将这数据放入到cache中，因此会增大内存开销；

c）坐标转换方法增大建索引开销。此方法本质上是将计算从查询阶段放至到索引阶段，因此提高了建索引的开销。

基于上述原因我们在实际应用中采用简化距离公式方法（通过三次多项式来拟合cos三角函数），此方法在团购筛选和商家筛选的距离排序、智能排序中已经开始使用，与之前相比，筛选团购时北京全城美食品类距离排序响应时间从40ms下降为20ms。

6 参考资料

<http://blog.csdn.net/liminlu0314/article/details/8553926>

<http://www.movable-type.co.uk/scripts/gis-faq-5.1.html>



