### Mongodb 去掉重复数据



数据库中 shop_base 集合中有重复 两个以上的重复 数据，需要删掉重复数据。

删除重复代码如下：

```
db.getCollection('shop_base').aggregate([
    {'$group': {'_id': '$sid', 'count':{$sum:1}, 'id_list':{'$max': '$_id'}} }, 
    {'$match': {'count':{'$gt':1}} },
]).forEach(function(x){
     print(db.getCollection('shop_base').remove({"_id" : x.id_list}))
    })
```

说明：

- 首先统计出 每个sid  的重复次数，列出最大的_id
-  筛选出重复次数大于1的
- 依据重复次数大于1的文档的id_list, 删除数据

