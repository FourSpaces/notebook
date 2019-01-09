# SQL 中常用的函数

CASE

```
CASE

简单case函数是case搜索函数的真子集 
简单case函数的使用方法与一些高级语言（如：java）中的switch语句相似:CASE给定匹配字段，WHEN给出具体的字段值，如果匹配到后返回THEN值。
简单case函数其实就是case搜索函数的‘=’逻辑的实现。case搜索函数可以实现简单case函数的所有功能，而简单case函数却不可实现case搜索函数的‘=’逻辑以外的功能。
case函数匹配原则 
case函数与switch的不同在于case仅返回第一个匹配到的结果，而switch则会在没有中断的情况下继续后面的判断，将会执行所有匹配的结果。
case搜索函数比简单case函数更加灵活 
case搜索函数与简单case函数相比的灵活之处在于可以在WHEN中书写判断式。

CASE sex
    WHEN '1' THEN '男'
    WHEN '2' THEN '女'
ELSE '其他' END

```

CAST()

```
# CAST()函数的参数是一个表达式，它包括用AS关键字分隔的源值和目标数据类型。以下例子用于将文本字符串'12'转换为整型:

SELECT CAST('12' AS int)
```