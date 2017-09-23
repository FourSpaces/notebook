##

在pymongo中使用find是得到1个游标对象的,如果你想实现MongoDB shell中find操作,例如:

> db.test.find()
{ "_id" : ObjectId("5838531e0f3577fc9178b834"), "name" : "zhangsan" }
在pymongo中需要使用find_one方法而不是find方法:

```
>>> print db.test.find_one()
{u'_id': ObjectId('5838531e0f3577fc9178b834'), u'name': u'zhangsan'}
```

```
>>> print db.test.find()
<pymongo.cursor.Cursor at 0x7f4ac789e450>
>>> result = []
>>> for x in db.test.find():
result.append(x)
>>> print(result)
>>> [{u'_id': ObjectId('5838531e0f3577fc9178b834'), u'name': u'zhangsan'},...]
```

