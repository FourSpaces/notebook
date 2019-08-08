### scala 函数部分



```
List(1,9,2,4,5).span(_<3)       // (List(1),List(9, 2, 4, 5))，碰到不符合就结束

List(1,9,2,4,5).partition(_<3) // (List(1, 2),List(9, 4, 5))，扫描所有


```

