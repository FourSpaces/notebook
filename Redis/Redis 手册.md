### Redis 手册

# redis 2.10.6

[Downloads ↓](https://pypi.python.org/pypi/redis#downloads)

Python client for Redis key-value store

The Python interface to the Redis key-value store.

## Installation

redis-py requires a running Redis server. See [Redis’s quickstart](http://redis.io/topics/quickstart) for installation instructions.

To install redis-py, simply:

```
$ sudo pip install redis

```

or alternatively (you really should be using pip though):

```
$ sudo easy_install redis

```

or from source:

```
$ sudo python setup.py install

```

## Getting Started  入门

```
>>> import redis
>>> r = redis.StrictRedis(host='localhost', port=6379, db=0)
>>> r.set('foo', 'bar')
True
>>> r.get('foo')
'bar'

```

## API Reference API参考

The [official Redis command documentation](http://redis.io/commands) does a great job of explaining each command in detail. redis-py exposes two client classes that implement these commands. The StrictRedis class attempts to adhere to the official command syntax. There are a few exceptions:

官方的Redis命令文档在详细解释每个命令方面做得很好。 redis-py公开了两个实现这些命令的客户端类。 StrictRedis类尝试遵守官方命令语法。 有一些例外：

- **SELECT**: Not implemented. See the explanation in the Thread Safety section below.

  未实现。 请参阅下面的“线程安全”部分中的说明。

- **DEL**: ‘del’ is a reserved keyword in the Python syntax. Therefore redis-py uses ‘delete’ instead.

  'del'是Python语法中的保留关键字。 因此redis-py使用'delete'来代替。

- **CONFIG GET|SET**: These are implemented separately as config_get or config_set.

  这些分别作为config_get或config_set来实现。

- **MULTI/EXEC**: These are implemented as part of the Pipeline class. The pipeline is wrapped with the MULTI and EXEC statements by default when it is executed, which can be disabled by specifying transaction=False. See more about Pipelines below.

  这些被实现为Pipeline类的一部分。 在执行时，默认情况下，管道是用MULTI和EXEC语句包装的，可以通过指定transaction = False来禁用。 查看更多关于下面的管道。

- **SUBSCRIBE/LISTEN**: Similar to pipelines, PubSub is implemented as a separate class as it places the underlying connection in a state where it can’t execute non-pubsub commands. Calling the pubsub method from the Redis client will return a PubSub instance where you can subscribe to channels and listen for messages. You can only call PUBLISH from the Redis client (see [this comment on issue #151](https://github.com/andymccurdy/redis-py/issues/151#issuecomment-1545015) for details).

  与管道类似，PubSub作为一个单独的类来实现，因为它将底层连接置于无法执行非pubsub命令的状态。 从Redis客户端调用pubsub方法将返回一个PubSub实例，您可以在其中订阅频道并侦听消息。 您只能从Redis客户端调用PUBLISH（有关详细信息，请参阅第151期的此评论）。

- **SCAN/SSCAN/HSCAN/ZSCAN**: The *SCAN commands are implemented as they exist in the Redis documentation. In addition, each command has an equivilant iterator method. These are purely for convenience so the user doesn’t have to keep track of the cursor while iterating. Use the scan_iter/sscan_iter/hscan_iter/zscan_iter methods for this behavior.

  * SCAN命令的实现与Redis文档中存在的一样。 另外，每个命令都有一个等价的迭代器方法。 这些纯粹是为了方便，所以用户在迭代时不必跟踪光标。 对此行为使用scan_iter / sscan_iter / hscan_iter / zscan_iter方法。

In addition to the changes above, the Redis class, a subclass of StrictRedis, overrides several other commands to provide backwards compatibility with older versions of redis-py:

除了上面所做的更改外，Redis类（StrictRedis的一个子类）还覆盖了其他几个命令，以便与旧版本的redis-py向后兼容：

- **LREM**: Order of ‘num’ and ‘value’ arguments reversed such that ‘num’ can provide a default value of zero.

  “num”和“value”参数的顺序相反，使得“num”可以提供默认值零。

- **ZADD**: Redis specifies the ‘score’ argument before ‘value’. These were swapped accidentally when being implemented and not discovered until after people were already using it. The Redis class expects *args in the form of: name1, score1, name2, score2, …

  Redis在“值”之前指定“分数”参数。 这些被实施时意外交换，直到人们已经使用它们之后才被发现。 Redis类期望* args的形式为：name1，score1，name2，score2，...

- **SETEX**: Order of ‘time’ and ‘value’ arguments reversed.

  “时间”和“价值”论点的顺序颠倒了

## More Detail 更多详情

### Connection Pools  连接池

Behind the scenes, redis-py uses a connection pool to manage connections to a Redis server. By default, each Redis instance you create will in turn create its own connection pool. You can override this behavior and use an existing connection pool by passing an already created connection pool instance to the connection_pool argument of the Redis class. You may choose to do this in order to implement client side sharding or have finer grain control of how connections are managed.

在后台，redis-py使用连接池来管理与Redis服务器的连接。 默认情况下，您创建的每个Redis实例将依次创建自己的连接池。 您可以通过将已创建的连接池实例传递给Redis类的connection_pool参数来覆盖此行为并使用现有连接池。 您可以选择这样做，以实现客户端分片或更好地控制连接的管理方式。

```
>>> pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
>>> r = redis.Redis(connection_pool=pool)

```

### Connections 连接

ConnectionPools manage a set of Connection instances. redis-py ships with two types of Connections. The default, Connection, is a normal TCP socket based connection. The UnixDomainSocketConnection allows for clients running on the same device as the server to connect via a unix domain socket. To use a UnixDomainSocketConnection connection, simply pass the unix_socket_path argument, which is a string to the unix domain socket file. Additionally, make sure the unixsocket parameter is defined in your redis.conf file. It’s commented out by default.

ConnectionPools管理一组Connection实例。 redis-py提供两种类型的连接。 默认的Connection是一个普通的基于TCP套接字的连接。 UnixDomainSocketConnection允许在与服务器相同的设备上运行的客户端通过unix域套接字进行连接。 要使用UnixDomainSocketConnection连接，只需将unix_socket_path参数（它是一个字符串）传递给unix域套接字文件。 此外，请确保您的redis.conf文件中定义了unixsocket参数。 它被默认注释掉了。

```
>>> r = redis.Redis(unix_socket_path='/tmp/redis.sock')

```

You can create your own Connection subclasses as well. This may be useful if you want to control the socket behavior within an async framework. To instantiate a client class using your own connection, you need to create a connection pool, passing your class to the connection_class argument. Other keyword parameters you pass to the pool will be passed to the class specified during initialization.

您也可以创建自己的Connection子类。 如果您想在异步框架中控制套接字行为，这可能很有用。 要使用自己的连接实例化客户端类，您需要创建一个连接池，将您的类传递给connection_class参数。 您传递给池的其他关键字参数将传递给在初始化过程中指定的类。

```
>>> pool = redis.ConnectionPool(connection_class=YourConnectionClass,
                                your_arg='...', ...)

```

### Parsers  解析器

Parser classes provide a way to control how responses from the Redis server are parsed. redis-py ships with two parser classes, the PythonParser and the HiredisParser. By default, redis-py will attempt to use the HiredisParser if you have the hiredis module installed and will fallback to the PythonParser otherwise.

解析器类提供了一种方法来控制如何解析来自Redis服务器的响应。 redis-py提供了两个解析器类，PythonParser和HiredisParser。 默认情况下，如果已安装hiredis模块，redis-py将尝试使用HiredisParser，否则将回退到PythonParser。

Hiredis is a C library maintained by the core Redis team. Pieter Noordhuis was kind enough to create Python bindings. Using Hiredis can provide up to a 10x speed improvement in parsing responses from the Redis server. The performance increase is most noticeable when retrieving many pieces of data, such as from LRANGE or SMEMBERS operations.

Hiredis是由Redis核心团队维护的C库。 Pieter Noordhuis非常友好地创建了Python绑定。 使用Hiredis可以使Redis服务器的响应速度提高10倍。 当检索许多数据时（例如从LRANGE或SMEMBERS操作），性能提升最为明显。

Hiredis is available on PyPI, and can be installed via pip or easy_install just like redis-py.

Hiredis在PyPI上可用，可以像redis-py一样通过pip或easy_install进行安装。

```
$ pip install hiredis

```

or

```
$ easy_install hiredis

```

### Response Callbacks  响应回调

The client class uses a set of callbacks to cast Redis responses to the appropriate Python type. There are a number of these callbacks defined on the Redis client class in a dictionary called RESPONSE_CALLBACKS.

客户端类使用一组回调来将Redis响应转换为适当的Python类型。 在名为RESPONSE_CALLBACKS的字典中，在Redis客户端类中定义了许多这样的回调。

Custom callbacks can be added on a per-instance basis using the set_response_callback method. This method accepts two arguments: a command name and the callback. Callbacks added in this manner are only valid on the instance the callback is added to. If you want to define or override a callback globally, you should make a subclass of the Redis client and add your callback to its RESPONSE_CALLBACKS class dictionary.

自定义回调可以使用set_response_callback方法在每个实例的基础上添加。 该方法接受两个参数：命令名称和回调。 以这种方式添加的回调仅在回调添加到的实例上有效。 如果要定义或覆盖全局回调，则应该创建Redis客户端的子类并将其回调添加到其RESPONSE_CALLBACKS类字典中。

Response callbacks take at least one parameter: the response from the Redis server. Keyword arguments may also be accepted in order to further control how to interpret the response. These keyword arguments are specified during the command’s call to execute_command. The ZRANGE implementation demonstrates the use of response callback keyword arguments with its “withscores” argument.

响应回调至少需要一个参数：来自Redis服务器的响应。 关键字参数也可以被接受，以便进一步控制如何解释响应。 这些关键字参数在命令调用execute_command期间被指定。 ZRANGE实现通过其“withscores”参数来演示响应回调关键字参数的使用。



### Thread Safety

Redis client instances can safely be shared between threads. Internally, connection instances are only retrieved from the connection pool during command execution, and returned to the pool directly after. Command execution never modifies state on the client instance.

Redis客户端实例可以安全地在线程之间共享。 在内部，连接实例只能在命令执行期间从连接池中获取，并在之后直接返回到池中。 命令执行不会修改客户端实例上的状态。

However, there is one caveat: the Redis SELECT command. The SELECT command allows you to switch the database currently in use by the connection. That database remains selected until another is selected or until the connection is closed. This creates an issue in that connections could be returned to the pool that are connected to a different database.

但是，有一个警告：Redis的SELECT命令。 SELECT命令允许您切换连接当前正在使用的数据库。 该数据库保持选定状态，直到选择另一个数据库或连接关闭。 这会产生一个问题，连接可能会返回到连接到不同数据库的池。

As a result, redis-py does not implement the SELECT command on client instances. If you use multiple Redis databases within the same application, you should create a separate client instance (and possibly a separate connection pool) for each database.

因此，redis-py不会在客户端实例上实现SELECT命令。 如果在同一应用程序中使用多个Redis数据库，则应为每个数据库创建一个单独的客户端实例（可能还有一个单独的连接池）。

It is not safe to pass PubSub or Pipeline objects between threads.

在线程之间传递PubSub或Pipeline对象是不安全的。

### Pipelines  管道

Pipelines are a subclass of the base Redis class that provide support for buffering multiple commands to the server in a single request. They can be used to dramatically increase the performance of groups of commands by reducing the number of back-and-forth TCP packets between the client and server.

流水线是基础Redis类的一个子类，它提供了在一个请求中缓存多个到服务器的命令的支持。 通过减少客户端和服务器之间来回TCP数据包的数量，它们可以用来显着提高命令组的性能。

Pipelines are quite simple to use:

流水线使用非常简单：

```
>>> r = redis.Redis(...)
>>> r.set('bing', 'baz')
>>> # Use the pipeline() method to create a pipeline instance
>>> pipe = r.pipeline()
>>> # The following SET commands are buffered
>>> pipe.set('foo', 'bar')
>>> pipe.get('bing')
>>> # the EXECUTE call sends all buffered commands to the server, returning
>>> # a list of responses, one for each command.
>>> pipe.execute()
[True, 'baz']

```

For ease of use, all commands being buffered into the pipeline return the pipeline object itself. Therefore calls can be chained like:

为了便于使用，缓冲到管道中的所有命令都返回管道对象本身。 因此，调用可以像链接一样：

```
>>> pipe.set('foo', 'bar').sadd('faz', 'baz').incr('auto_number').execute()
[True, True, 6]

```

In addition, pipelines can also ensure the buffered commands are executed atomically as a group. This happens by default. If you want to disable the atomic nature of a pipeline but still want to buffer commands, you can turn off transactions.

此外，管道还可以确保缓冲的命令作为一个组自动执行。 这是默认情况下发生。 如果你想禁用流水线的原子特性，但仍想缓冲命令，可以关闭事务。

```
>>> pipe = r.pipeline(transaction=False)

```

A common issue occurs when requiring atomic transactions but needing to retrieve values in Redis prior for use within the transaction. For instance, let’s assume that the INCR command didn’t exist and we need to build an atomic version of INCR in Python.

当需要原子事务但是需要在Redis中检索事务之前使用的值时，会出现一个常见问题。 例如，假设INCR命令不存在，我们需要在Python中构建INCR的原子版本。

The completely naive implementation could GET the value, increment it in Python, and SET the new value back. However, this is not atomic because multiple clients could be doing this at the same time, each getting the same value from GET.

完全天真的实现可以获取值，在Python中增加它，并设置新值。 但是，这不是原子的，因为多个客户端可能会同时这样做，每个客户端从GET获得相同的值。

Enter the WATCH command. WATCH provides the ability to monitor one or more keys prior to starting a transaction. If any of those keys change prior the execution of that transaction, the entire transaction will be canceled and a WatchError will be raised. To implement our own client-side INCR command, we could do something like this:

输入WATCH命令。 WATCH提供在开始交易之前监控一个或多个密钥的功能。 如果这些密钥中的任何一个在执行该事务之前发生了变化，那么整个事务将被取消，并且会引发WatchError。 为了实现我们自己的客户端INCR命令，我们可以这样做：

```
>>> with r.pipeline() as pipe:
...     while 1:
...         try:
...             # put a WATCH on the key that holds our sequence value
...             pipe.watch('OUR-SEQUENCE-KEY')
...             # after WATCHing, the pipeline is put into immediate execution
...             # mode until we tell it to start buffering commands again.
...             # this allows us to get the current value of our sequence
...             current_value = pipe.get('OUR-SEQUENCE-KEY')
...             next_value = int(current_value) + 1
...             # now we can put the pipeline back into buffered mode with MULTI
...             pipe.multi()
...             pipe.set('OUR-SEQUENCE-KEY', next_value)
...             # and finally, execute the pipeline (the set command)
...             pipe.execute()
...             # if a WatchError wasn't raised during execution, everything
...             # we just did happened atomically.
...             break
...        except WatchError:
...             # another client must have changed 'OUR-SEQUENCE-KEY' between
...             # the time we started WATCHing it and the pipeline's execution.
...             # our best bet is to just retry.
...             continue

```

Note that, because the Pipeline must bind to a single connection for the duration of a WATCH, care must be taken to ensure that the connection is returned to the connection pool by calling the reset() method. If the Pipeline is used as a context manager (as in the example above) reset() will be called automatically. Of course you can do this the manual way by explicitly calling reset():

请注意，由于Pipeline必须在WATCH期间绑定到单个连接，因此必须注意通过调用reset（）方法确保连接返回到连接池。 如果使用Pipeline作为上下文管理器（如上例），reset（）将自动调用。 当然，你可以通过明确地调用reset（）来手动完成这个操作：

```
>>> pipe = r.pipeline()
>>> while 1:
...     try:
...         pipe.watch('OUR-SEQUENCE-KEY')
...         ...
...         pipe.execute()
...         break
...     except WatchError:
...         continue
...     finally:
...         pipe.reset()

```

A convenience method named “transaction” exists for handling all the boilerplate of handling and retrying watch errors. It takes a callable that should expect a single parameter, a pipeline object, and any number of keys to be WATCHed. Our client-side INCR command above can be written like this, which is much easier to read:

存在一个名为“transaction”的简便方法，用于处理所有处理和重试监视错误的样板。 它需要一个可调用的应该期望一个单一的参数，一个管道对象，以及任何数量的键被监视。 我们上面的客户端INCR命令可以这样写，这更容易阅读：n

```
>>> def client_side_incr(pipe):
...     current_value = pipe.get('OUR-SEQUENCE-KEY')
...     next_value = int(current_value) + 1
...     pipe.multi()
...     pipe.set('OUR-SEQUENCE-KEY', next_value)
>>>
>>> r.transaction(client_side_incr, 'OUR-SEQUENCE-KEY')
[True]

```

### Publish / Subscribe

redis-py includes a PubSub object that subscribes to channels and listens for new messages. Creating a PubSub object is easy.

```
>>> r = redis.StrictRedis(...)
>>> p = r.pubsub()

```

Once a PubSub instance is created, channels and patterns can be subscribed to.

```
>>> p.subscribe('my-first-channel', 'my-second-channel', ...)
>>> p.psubscribe('my-*', ...)

```

The PubSub instance is now subscribed to those channels/patterns. The subscription confirmations can be seen by reading messages from the PubSub instance.

```
>>> p.get_message()
{'pattern': None, 'type': 'subscribe', 'channel': 'my-second-channel', 'data': 1L}
>>> p.get_message()
{'pattern': None, 'type': 'subscribe', 'channel': 'my-first-channel', 'data': 2L}
>>> p.get_message()
{'pattern': None, 'type': 'psubscribe', 'channel': 'my-*', 'data': 3L}

```

Every message read from a PubSub instance will be a dictionary with the following keys.

- **type**: One of the following: ‘subscribe’, ‘unsubscribe’, ‘psubscribe’, ‘punsubscribe’, ‘message’, ‘pmessage’
- **channel**: The channel [un]subscribed to or the channel a message was published to
- **pattern**: The pattern that matched a published message’s channel. Will be None in all cases except for ‘pmessage’ types.
- **data**: The message data. With [un]subscribe messages, this value will be the number of channels and patterns the connection is currently subscribed to. With [p]message messages, this value will be the actual published message.

Let’s send a message now.

```
# the publish method returns the number matching channel and pattern
# subscriptions. 'my-first-channel' matches both the 'my-first-channel'
# subscription and the 'my-*' pattern subscription, so this message will
# be delivered to 2 channels/patterns
>>> r.publish('my-first-channel', 'some data')
2
>>> p.get_message()
{'channel': 'my-first-channel', 'data': 'some data', 'pattern': None, 'type': 'message'}
>>> p.get_message()
{'channel': 'my-first-channel', 'data': 'some data', 'pattern': 'my-*', 'type': 'pmessage'}

```

Unsubscribing works just like subscribing. If no arguments are passed to [p]unsubscribe, all channels or patterns will be unsubscribed from.

```
>>> p.unsubscribe()
>>> p.punsubscribe('my-*')
>>> p.get_message()
{'channel': 'my-second-channel', 'data': 2L, 'pattern': None, 'type': 'unsubscribe'}
>>> p.get_message()
{'channel': 'my-first-channel', 'data': 1L, 'pattern': None, 'type': 'unsubscribe'}
>>> p.get_message()
{'channel': 'my-*', 'data': 0L, 'pattern': None, 'type': 'punsubscribe'}

```

redis-py also allows you to register callback functions to handle published messages. Message handlers take a single argument, the message, which is a dictionary just like the examples above. To subscribe to a channel or pattern with a message handler, pass the channel or pattern name as a keyword argument with its value being the callback function.

When a message is read on a channel or pattern with a message handler, the message dictionary is created and passed to the message handler. In this case, a None value is returned from get_message() since the message was already handled.

```
>>> def my_handler(message):
...     print 'MY HANDLER: ', message['data']
>>> p.subscribe(**{'my-channel': my_handler})
# read the subscribe confirmation message
>>> p.get_message()
{'pattern': None, 'type': 'subscribe', 'channel': 'my-channel', 'data': 1L}
>>> r.publish('my-channel', 'awesome data')
1
# for the message handler to work, we need tell the instance to read data.
# this can be done in several ways (read more below). we'll just use
# the familiar get_message() function for now
>>> message = p.get_message()
MY HANDLER:  awesome data
# note here that the my_handler callback printed the string above.
# `message` is None because the message was handled by our handler.
>>> print message
None

```

If your application is not interested in the (sometimes noisy) subscribe/unsubscribe confirmation messages, you can ignore them by passing ignore_subscribe_messages=True to r.pubsub(). This will cause all subscribe/unsubscribe messages to be read, but they won’t bubble up to your application.

```
>>> p = r.pubsub(ignore_subscribe_messages=True)
>>> p.subscribe('my-channel')
>>> p.get_message()  # hides the subscribe message and returns None
>>> r.publish('my-channel')
1
>>> p.get_message()
{'channel': 'my-channel', 'data': 'my data', 'pattern': None, 'type': 'message'}

```

There are three different strategies for reading messages.

The examples above have been using pubsub.get_message(). Behind the scenes, get_message() uses the system’s ‘select’ module to quickly poll the connection’s socket. If there’s data available to be read, get_message() will read it, format the message and return it or pass it to a message handler. If there’s no data to be read, get_message() will immediately return None. This makes it trivial to integrate into an existing event loop inside your application.

```
>>> while True:
>>>     message = p.get_message()
>>>     if message:
>>>         # do something with the message
>>>     time.sleep(0.001)  # be nice to the system :)

```

Older versions of redis-py only read messages with pubsub.listen(). listen() is a generator that blocks until a message is available. If your application doesn’t need to do anything else but receive and act on messages received from redis, listen() is an easy way to get up an running.

```
>>> for message in p.listen():
...     # do something with the message

```

The third option runs an event loop in a separate thread. pubsub.run_in_thread() creates a new thread and starts the event loop. The thread object is returned to the caller of run_in_thread(). The caller can use the thread.stop() method to shut down the event loop and thread. Behind the scenes, this is simply a wrapper around get_message() that runs in a separate thread, essentially creating a tiny non-blocking event loop for you. run_in_thread() takes an optional sleep_time argument. If specified, the event loop will call time.sleep() with the value in each iteration of the loop.

Note: Since we’re running in a separate thread, there’s no way to handle messages that aren’t automatically handled with registered message handlers. Therefore, redis-py prevents you from calling run_in_thread() if you’re subscribed to patterns or channels that don’t have message handlers attached.

```
>>> p.subscribe(**{'my-channel': my_handler})
>>> thread = p.run_in_thread(sleep_time=0.001)
# the event loop is now running in the background processing messages
# when it's time to shut it down...
>>> thread.stop()

```

A PubSub object adheres to the same encoding semantics as the client instance it was created from. Any channel or pattern that’s unicode will be encoded using the charset specified on the client before being sent to Redis. If the client’s decode_responses flag is set the False (the default), the ‘channel’, ‘pattern’ and ‘data’ values in message dictionaries will be byte strings (str on Python 2, bytes on Python 3). If the client’s decode_responses is True, then the ‘channel’, ‘pattern’ and ‘data’ values will be automatically decoded to unicode strings using the client’s charset.

PubSub objects remember what channels and patterns they are subscribed to. In the event of a disconnection such as a network error or timeout, the PubSub object will re-subscribe to all prior channels and patterns when reconnecting. Messages that were published while the client was disconnected cannot be delivered. When you’re finished with a PubSub object, call its.close() method to shutdown the connection.

```
>>> p = r.pubsub()
>>> ...
>>> p.close()

```

The PUBSUB set of subcommands CHANNELS, NUMSUB and NUMPAT are also supported:

```
>>> r.pubsub_channels()
['foo', 'bar']
>>> r.pubsub_numsub('foo', 'bar')
[('foo', 9001), ('bar', 42)]
>>> r.pubsub_numsub('baz')
[('baz', 0)]
>>> r.pubsub_numpat()
1204

```

### LUA Scripting

redis-py supports the EVAL, EVALSHA, and SCRIPT commands. However, there are a number of edge cases that make these commands tedious to use in real world scenarios. Therefore, redis-py exposes a Script object that makes scripting much easier to use.

To create a Script instance, use the register_script function on a client instance passing the LUA code as the first argument. register_script returns a Script instance that you can use throughout your code.

The following trivial LUA script accepts two parameters: the name of a key and a multiplier value. The script fetches the value stored in the key, multiplies it with the multiplier value and returns the result.

```
>>> r = redis.StrictRedis()
>>> lua = """
... local value = redis.call('GET', KEYS[1])
... value = tonumber(value)
... return value * ARGV[1]"""
>>> multiply = r.register_script(lua)

```

multiply is now a Script instance that is invoked by calling it like a function. Script instances accept the following optional arguments:

- **keys**: A list of key names that the script will access. This becomes the KEYS list in LUA.
- **args**: A list of argument values. This becomes the ARGV list in LUA.
- **client**: A redis-py Client or Pipeline instance that will invoke the script. If client isn’t specified, the client that intiially created the Script instance (the one that register_script was invoked from) will be used.

Continuing the example from above:

```
>>> r.set('foo', 2)
>>> multiply(keys=['foo'], args=[5])
10

```

The value of key ‘foo’ is set to 2. When multiply is invoked, the ‘foo’ key is passed to the script along with the multiplier value of 5. LUA executes the script and returns the result, 10.

Script instances can be executed using a different client instance, even one that points to a completely different Redis server.

```
>>> r2 = redis.StrictRedis('redis2.example.com')
>>> r2.set('foo', 3)
>>> multiply(keys=['foo'], args=[5], client=r2)
15

```

The Script object ensures that the LUA script is loaded into Redis’s script cache. In the event of a NOSCRIPT error, it will load the script and retry executing it.

Script objects can also be used in pipelines. The pipeline instance should be passed as the client argument when calling the script. Care is taken to ensure that the script is registered in Redis’s script cache just prior to pipeline execution.

```
>>> pipe = r.pipeline()
>>> pipe.set('foo', 5)
>>> multiply(keys=['foo'], args=[5], client=pipe)
>>> pipe.execute()
[True, 25]

```

### Sentinel support

redis-py can be used together with [Redis Sentinel](http://redis.io/topics/sentinel) to discover Redis nodes. You need to have at least one Sentinel daemon running in order to use redis-py’s Sentinel support.

Connecting redis-py to the Sentinel instance(s) is easy. You can use a Sentinel connection to discover the master and slaves network addresses:

```
>>> from redis.sentinel import Sentinel
>>> sentinel = Sentinel([('localhost', 26379)], socket_timeout=0.1)
>>> sentinel.discover_master('mymaster')
('127.0.0.1', 6379)
>>> sentinel.discover_slaves('mymaster')
[('127.0.0.1', 6380)]

```

You can also create Redis client connections from a Sentinel instance. You can connect to either the master (for write operations) or a slave (for read-only operations).

```
>>> master = sentinel.master_for('mymaster', socket_timeout=0.1)
>>> slave = sentinel.slave_for('mymaster', socket_timeout=0.1)
>>> master.set('foo', 'bar')
>>> slave.get('foo')
'bar'

```

The master and slave objects are normal StrictRedis instances with their connection pool bound to the Sentinel instance. When a Sentinel backed client attempts to establish a connection, it first queries the Sentinel servers to determine an appropriate host to connect to. If no server is found, a MasterNotFoundError or SlaveNotFoundError is raised. Both exceptions are subclasses of ConnectionError.

When trying to connect to a slave client, the Sentinel connection pool will iterate over the list of slaves until it finds one that can be connected to. If no slaves can be connected to, a connection will be established with the master.

See [Guidelines for Redis clients with support for Redis Sentinel](http://redis.io/topics/sentinel-clients) to learn more about Redis Sentinel.

### Scan Iterators

The *SCAN commands introduced in Redis 2.8 can be cumbersome to use. While these commands are fully supported, redis-py also exposes the following methods that return Python iterators for convenience: scan_iter, hscan_iter, sscan_iter and zscan_iter.

```
>>> for key, value in (('A', '1'), ('B', '2'), ('C', '3')):
...     r.set(key, value)
>>> for key in r.scan_iter():
...     print key, r.get(key)
A 1
B 2
C 3

```

### Author

redis-py is developed and maintained by Andy McCurdy ([sedrik@gmail.com](mailto:sedrik%40gmail.com)). It can be found here: <http://github.com/andymccurdy/redis-py>

Special thanks to:

- Ludovico Magnocavallo, author of the original Python Redis client, from which some of the socket code is still used.
- Alexander Solovyov for ideas on the generic response callback system.
- Paul Hubbard for initial packaging support.

 

| File                                     | Type         | Py Version | Uploaded on | Size |
| ---------------------------------------- | ------------ | ---------- | ----------- | ---- |
| [redis-2.10.6-py2.py3-none-any.whl](https://pypi.python.org/packages/3b/f6/7a76333cf0b9251ecf49efff635015171843d9b977e4ffcf59f9c4428052/redis-2.10.6-py2.py3-none-any.whl#md5=7d626abf2468ad326eafead648e8f4e7) ([md5](https://pypi.python.org/pypi?:action=show_md5&digest=7d626abf2468ad326eafead648e8f4e7)) | Python Wheel | py2.py3    | 2017-08-16  | 63KB |
| [redis-2.10.6.tar.gz](https://pypi.python.org/packages/09/8d/6d34b75326bf96d4139a2ddd8e74b80840f800a0a79f9294399e212cb9a7/redis-2.10.6.tar.gz#md5=048348d8cfe0b5d0bba2f4d835005c3b) ([md5](https://pypi.python.org/pypi?:action=show_md5&digest=048348d8cfe0b5d0bba2f4d835005c3b)) | Source       |            | 2017-08-16  | 95KB |
|                                          |              |            |             |      |

- **Author:** Andy McCurdy
- **Home Page:** <http://github.com/andymccurdy/redis-py>
- **Keywords:** Redis,key-value store
- **License:** MIT
- Categories
  - [Development Status :: 5 - Production/Stable](https://pypi.python.org/pypi?:action=browse&c=5)
  - [Environment :: Console](https://pypi.python.org/pypi?:action=browse&c=8)
  - [Intended Audience :: Developers](https://pypi.python.org/pypi?:action=browse&c=30)
  - [License :: OSI Approved :: MIT License](https://pypi.python.org/pypi?:action=browse&c=69)
  - [Operating System :: OS Independent](https://pypi.python.org/pypi?:action=browse&c=156)
  - [Programming Language :: Python](https://pypi.python.org/pypi?:action=browse&c=214)
  - [Programming Language :: Python :: 2](https://pypi.python.org/pypi?:action=browse&c=527)
  - [Programming Language :: Python :: 2.6](https://pypi.python.org/pypi?:action=browse&c=531)
  - [Programming Language :: Python :: 2.7](https://pypi.python.org/pypi?:action=browse&c=532)
  - [Programming Language :: Python :: 3](https://pypi.python.org/pypi?:action=browse&c=533)
  - [Programming Language :: Python :: 3.3](https://pypi.python.org/pypi?:action=browse&c=566)
  - [Programming Language :: Python :: 3.4](https://pypi.python.org/pypi?:action=browse&c=587)
  - [Programming Language :: Python :: 3.5](https://pypi.python.org/pypi?:action=browse&c=607)
  - [Programming Language :: Python :: 3.6](https://pypi.python.org/pypi?:action=browse&c=611)
- **Package Index Owner:** andymccurdy
- **DOAP record:** [redis-2.10.6.xml](https://pypi.python.org/pypi?:action=doap&name=redis&version=2.10.6)