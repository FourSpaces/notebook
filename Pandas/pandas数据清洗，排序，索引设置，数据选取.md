# pandas数据清洗，排序，索引设置，数据选取

原创 2017年03月29日 21:34:23

- 标签：
- [数据](http://so.csdn.net/so/search/s.do?q=%E6%95%B0%E6%8D%AE&t=blog)


- **10538

> 此教程适合有pandas基础的童鞋来看，很多知识点会一笔带过，不做详细解释

**Pandas数据格式**

- Series

- DataFrame：每个column就是一个Series

  基础属性shape,index,columns,values，dtypes，describe(),head(),tail() 
  统计属性Series： count(),value_counts()，前者是统计总数，后者统计各自value的总数

------

df.isnull() df的空值为True 
df.notnull() df的非空值为True

- 修改列名

```
df.rename(columns = {'key':'key2'},inplace=True)


1234
```

- 更改数据格式astype()

```
isin                 #计算一个“Series各值是否包含传入的值序列中”的布尔数组
unique               #返回唯一值的数组
value_counts         #返回一个Series，其索引为唯一值，值为频率，按计数降序排列123
```

------

#### **数据清洗**

- 丢弃值drop()

```
df.drop(labels, axis=1)# 按列（axis=1），丢弃指定label的列,默认按行。。。1
```

- 丢弃缺失值dropna()

```
# 默认axi=0（行）；1（列），how=‘any’
df.dropna()#每行只要有空值，就将这行删除
df.dropna(axis=1)#每列只要有空值，整列丢弃
df.dropna(how='all')# 一行中全部为NaN的，才丢弃该行
df.dropna(thresh=3)# 每行至少3个非空值才保留12345
```

- 缺失值填充fillna()

```
df.fillna(0)
df.fillna({1:0,2:0.5}) #对第一列nan值赋0，第二列赋值0.5
df.fillna(method='ffill') #在列方向上以前一个值作为值赋给NaN123
```

- 值替换replace()

```
# 将df的A列中 -999 全部替换成空值
df['A'].replace(-999, np.nan)
#-999和1000 均替换成空值
obj.replace([-999,1000],  np.nan)
# -999替换成空值，1000替换成0
obj.replace([-999,1000],  [np.nan, 0])
# 同上，写法不同，更清晰
obj.replace({-999:np.nan, 1000:0})12345678
```

- 重复值处理duplicated()，unique()，drop_duplictad()

```
df.duplicated()#两行每列完全一样才算重复，后面重复的为True，第一个和不重复的为false，返回true
               #和false组成的Series类型
df.duplicated('key')#两行key这一列一样就算重复

df['A'].unique()# 返回唯一值的数组（类型为array）

df.drop_duplicates(['k1'])# 保留k1列中的唯一值的行，默认保留第一行
df.drop_duplicates(['k1','k2'], take_last=True)# 保留 k1和k2 组合的唯一值的行，take_last=True 保留最后一行12345678
```

------

#### **排序**

- 索引排序

```
# 默认axis=0，按行索引对行进行排序；ascending=True，升序排序
df.sort_index()
# 按列名对列进行排序，ascending=False 降序
df.sort_index(axis=1, ascending=False) 1234
```

- 值排序

```
# 按值对Series进行排序，使用order()，默认空值会置于尾部
s = pd.Series([4, 6, np.nan, 2, np.nan])
s.order()

df.sort_values(by=['a','b'])#按列进行排序12345
```

- 排名

```
a=Series([7,-5,7,4,2,0,4])
a.rank()#默认method='average'，升序排名（ascending=True），按行（axis=0）
#average 值相等时，取排名的平均值
#min 值相等时，取排名最小值
#max 值相等时，取排名最大值
#first值相等时，按原始数据出现顺序排名123456
```

------

#### **索引设置**

- reindex() 
  更新index或者columns， 
  默认：更新index，返回一个新的DataFrame

```
# 返回一个新的DataFrame，更新index，原来的index会被替代消失
# 如果dataframe中某个索引值不存在，会自动补上NaN
df2 = df1.reindex(['a','b','c','d','e'])

# fill_valuse为原先不存在的索引补上默认值，不在是NaN
df2 = df1.reindex(['a','b','c','d','e'],  fill_value=0)

# inplace=Ture，在DataFrame上修改数据，而不是返回一个新的DataFrame
df1.reindex(['a','b','c','d','e'],  inplace=Ture)

# reindex不仅可以修改 索引(行)，也可以修改列
states = ["Texas","Utah","California"]
df2 = df1.reindex( columns=states )12345678910111213
```

- set_index() 
  将DataFrame中的列columns设置成索引index 
  打造层次化索引的方法

```
# 将columns中的其中两列：race和sex的值设置索引，race为一级，sex为二级
# inplace=True 在原数据集上修改的
adult.set_index(['race','sex'], inplace = True) 

# 默认情况下，设置成索引的列会从DataFrame中移除
# drop=False将其保留下来
adult.set_index(['race','sex'], inplace = True) 1234567
```

- reset_index() 
  将使用set_index()打造的层次化逆向操作 
  既是取消层次化索引，将索引变回列，并补上最常规的数字索引

```
df.reset_index()1
```

------

#### **数据选取**

- [] 
  只能对行进 行（row/index） 切片，前闭后开df[0:3]，df[:4]，df[4:]
- where 布尔查找

```
 df[df["A"]>7]1
```

- isin

```
# 返回布尔值
s.isin([1,2,3])
df['A'].isin([1,2,3])
df.loc[df['A'].isin([5.8,5.1])]选取列A中值为5.8，5.1的所有行组成dataframe1234
```

- query 
  多个where整合切片，&：于，|：或　

```
 df.query(" A>5.0 & (B>3.5 | C<1.0) ")　1
```

- loc ：根据名称Label切片

```
# df.loc[A,B] A是行范围，B是列范围
df.loc[1:4,['petal_length','petal_width']]

# 需求1：创建一个新的变量 test
# 如果sepal_length > 3 test = 1 否则 test = 0
df.loc[df['sepal_length'] > 6, 'test'] = 1
df.loc[df['sepal_length'] <=6, 'test'] = 0

# 需求2：创建一个新变量test2 
# 1.petal_length>2 and petal_width>0.3 = 1 
# 2.sepeal_length>6 and sepal_width>3 = 2 3.其他 = 0
df['test2'] = 0
df.loc[(df['petal_length']>2)&(df['petal_width']>0.3), 'test2'] = 1
df.loc[(df['sepal_length']>6)&(df['sepal_width']>3), 'test2'] = 21234567891011121314
```

- iloc：切位置

```
df.iloc[1:4,:]1
```

- ix：混切 
  名称和位置混切，但效率低，少用

```
df1.ix[0:3,['sepal_length','petal_width']]1
```

- map与lambda

```
alist = [1,2,3,4]
map(lambda s : s+1, alist)#map就是将自定义函数应用于Series每个元素

df['sepal_length'].map(lambda s:s*2+1)[0:3]1234
```

- apply和applymap 
  apply和applymap是对dataframe的操作，前者操作一行或者一列，后者操作每个元素

```
These are techniques to apply function to element, column or dataframe.

Map: It iterates over each element of a series. 
df[‘column1’].map(lambda x: 10+x), this will add 10 to each element of column1.
df[‘column2’].map(lambda x: ‘AV’+x), this will concatenate “AV“ at the beginning of each element of column2 (column format is string).

Apply: As the name suggests, applies a function along any axis of the DataFrame.
df[[‘column1’,’column2’]].apply(sum), it will returns the sum of all the values of column1 and column2.
df0[['data1']].apply(lambda s:s+1)

ApplyMap: 对dataframe的每一个元素施加一个函数
func = lambda x: x+2
df.applymap(func), dataframe每个元素加2 (所有列必须数字类型)12345678910111213
```

- contains

```
# 使用DataFrame模糊筛选数据(类似SQL中的LIKE)
# 使用正则表达式进行模糊匹配,*匹配0或无限次,?匹配0或1次
df_obj[df_obj['套餐'].str.contains(r'.*?语音CDMA.*')] 

# 下面两句效果一致
df[df['商品名称'].str.contains("四件套")]
df[df['商品名称'].str.contains(r".*四件套.*")]1234567
```

版权声明：本文为博主原创文章，未经博主允许不得转载。