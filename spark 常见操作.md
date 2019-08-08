## spark 常见操作



#### 创建Dataset 的方法

-  Spark在 SparkSession中使用 read功能读入存储系统中的文件

  ```
  val people = spark.read.parquet("...").as[Person]  //Scala
  
  Dataset<Person> people = spark.read().parquet("...").as(Encoders.bean(Person.class)); //Java
  ```

- Dataset也可以通过现有 Dataset进行转换创建。

  ```
  // Scala版本:在已有 的 Dataset[Person]中使用 map 转换函数，获取 Person 中的姓名 ， 将生成新的 Dataset[String];
  val names = people.map(_.name)
  
  // Java版本:在已有的数据集 Dataset<String>中使用 map转换函数，通过(Person p) -> p.name 获取 Person 中的姓名，编码器指定姓名屈性的类型为 String 类型，生成新的姓名的数据集 Dataset<String>
  
  Dataset<String> names = people.map((Person P) -> p.name, Encoders.STRING );
  
  ```

  

#### 

```
// 从DataSet 中选择一列
vak ageCol = people("age")		// 在scala 中
column ageCol = people.col("age");	// 在Java 中


// 创建一个新的列， 每个人的年龄增加10
people("age") + 10		// 在scala 中
people.col("age").plus(10);		// 在Java 中


```



使用 spark.read.parquet 分别读入 parquet 格式的人员数据及
部门数据，过滤出年龄大千 30 岁的人员，根据部门 1D 和部门数据进行 join, 然后按照姓名、
性别分组 ， 再使用 agg 方法，调用内贾函数 avg计算出部门中的平均工资、人员的最大年龄 。

```
// scala 代码

val people = spark.read.parquet("...")
val department = spark.read.parquet("...")
people.filter("age > 30")
   .join(department, people("deptId") === department("id"))
   .groupBy(department("name"), "gender")
   .agg(avg(people("salary")), max(people("age")))
   
// java 代码
Dataset<Row> people = spark.read().parquet("...");
Dataset<Row> department = spark.read().parquet("...")
people.filter("age".gt(30))
   .join(department, people.col("deptId").equalTo(department("id")))
   .groupBy(department.col("name"), "gender")
   .agg(avg(people.col("salary")), max(people.col("age")));
```

