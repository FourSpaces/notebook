#  常见操作

## 登陆用户
```
mongo --port 27017 -u "adminUser" -p "adminPass" --authenticationDatabase "admin"

# 或者

mongo --port 27017

use admin
db.auth("adminUser", "adminPass")
```


## 创建数据库 

```
use datadb
```



## 创建用户、分配权限



```Mongoldb
use live_db
db.createUser(
  {
    user: "live_use",
    pwd: "4530d8aa82ad5a68",
    roles: [ { role: "readWrite", db: "live_db" }]
  }
)

结果：
Successfully added user: {
	"user" : "live_use",
	"roles" : [
		{
			"role" : "readWrite",
			"db" : "live_db"
		}
	]
}
```

