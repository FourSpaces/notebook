####连接池

​        在后台，Redis py使用连接池【connection pool】来管理连接来管理连接到redis服务。默认情况下，每一个redis实例创建将创建自己的连接池。可以通过连接池实例redis的connection_pool参数来使用已经创建的连接实例。你可以为了实现客户端分片或更精细的控制管理而选择它

```
>>> pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
>>> r = redis.Redis(connection_pool=pool)
```



#### Connections

ConnectionPools 管理 一个连接集合，redis-py ships 具有两种连接类型，默认连接是一个基于TCP标准的连接。UnixDomainSocketConnection【unix 域下的套接字连接】允许 for 在客户端运行一些 通过unix 域下的套接字连接策略。使用UnixDomainSocketConnection连接, 简单通过unix_socket_path主题。这是一个字符串的UNIX域套接字文件，此外，确保unixsocket参数是你redis.conf文件定义。默认情况下它会被注释掉。

```
>>> r = redis.Redis(unix_socket_path='/tmp/redis.sock')
```

你能创建你的Connection子类, 这可能是有用的如果你想连接  socket 异步框架中的套接字行为，使用你自己的连接客户端类实例，你需要创建一个连接池，通过你的连接类凭据。传递给池的其他关键字参数将被传递给初始化时指定的类。

```
>>> pool = redis.ConnectionPool(connection_class=YourConnectionClass,
                                your_arg='...', ...)
```







#### redis-py 2.10.6

key-value存储系统Redis的Python 客户端

key-value存储系统Redis的Python 接口



[](http://travis-ci.org/andymccurdy/redis-py)

#### Installation  安装

redis-py 需要 运行的Redis 服务器，Redis 安装略













