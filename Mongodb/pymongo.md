##

在pymongo中使用find是得到1个游标对象的,如果你想实现MongoDB shell中find操作,例如:

> db.test.find()
> { "_id" : ObjectId("5838531e0f3577fc9178b834"), "name" : "zhangsan" }
> 在pymongo中需要使用find_one方法而不是find方法:

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
>>> [{u'_id': ObjectId('5838531e0f3577fc9178b834'), u'name': u'zhangsan'},...]Client for a MongoDB instance, a replica set, or a set of mongoses.

The client object is thread-safe and has connection-pooling built in.
If an operation fails because of a network error,
:class:`~pymongo.errors.ConnectionFailure` is raised and the client
reconnects in the background. Application code should handle this
exception (recognizing that the operation failed) and then continue to
execute.

The `host` parameter can be a full `mongodb URI
<http://dochub.mongodb.org/core/connections>`_, in addition to
a simple hostname. It can also be a list of hostnames or
URIs. Any port specified in the host string(s) will override
the `port` parameter. If multiple mongodb URIs containing
database or auth information are passed, the last database,
username, and password present will be used.  For username and
passwords reserved characters like ':', '/', '+' and '@' must be
percent encoded following RFC 2396::

    try:
        # Python 3.x
        from urllib.parse import quote_plus
    except ImportError:
        # Python 2.x
        from urllib import quote_plus

    uri = "mongodb://%s:%s@%s" % (
        quote_plus(user), quote_plus(password), host)
    client = MongoClient(uri)

Unix domain sockets are also supported. The socket path must be percent
encoded in the URI::

    uri = "mongodb://%s:%s@%s" % (
        quote_plus(user), quote_plus(password), quote_plus(socket_path))
    client = MongoClient(uri)

But not when passed as a simple hostname::

    client = MongoClient('/tmp/mongodb-27017.sock')

.. note:: Starting with version 3.0 the :class:`MongoClient`
  constructor no longer blocks while connecting to the server or
  servers, and it no longer raises
  :class:`~pymongo.errors.ConnectionFailure` if they are
  unavailable, nor :class:`~pymongo.errors.ConfigurationError`
  if the user's credentials are wrong. Instead, the constructor
  returns immediately and launches the connection process on
  background threads. You can check if the server is available
  like this::

    from pymongo.errors import ConnectionFailure
    client = MongoClient()
    try:
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
    except ConnectionFailure:
        print("Server not available")

.. warning:: When using PyMongo in a multiprocessing context, please
  read :ref:`multiprocessing` first.

:Parameters:
  - `host` (optional): hostname or IP address or Unix domain socket
    path of a single mongod or mongos instance to connect to, or a
    mongodb URI, or a list of hostnames / mongodb URIs. If `host` is
    an IPv6 literal it must be enclosed in '[' and ']' characters
    following the RFC2732 URL syntax (e.g. '[::1]' for localhost).
    Multihomed and round robin DNS addresses are **not** supported.
  - `port` (optional): port number on which to connect
  - `document_class` (optional): default class to use for
    documents returned from queries on this client
  - `tz_aware` (optional): if ``True``,
    :class:`~datetime.datetime` instances returned as values
    in a document by this :class:`MongoClient` will be timezone
    aware (otherwise they will be naive)
  - `connect` (optional): if ``True`` (the default), immediately
    begin connecting to MongoDB in the background. Otherwise connect
    on the first operation.

  | **Other optional parameters can be passed as keyword arguments:**

  - `maxPoolSize` (optional): The maximum allowable number of
    concurrent connections to each connected server. Requests to a
    server will block if there are `maxPoolSize` outstanding
    connections to the requested server. Defaults to 100. Cannot be 0.
  - `minPoolSize` (optional): The minimum required number of concurrent
    connections that the pool will maintain to each connected server.
    Default is 0.
  - `maxIdleTimeMS` (optional): The maximum number of milliseconds that
    a connection can remain idle in the pool before being removed and
    replaced. Defaults to `None` (no limit).
  - `socketTimeoutMS`: (integer or None) Controls how long (in
    milliseconds) the driver will wait for a response after sending an
    ordinary (non-monitoring) database operation before concluding that
    a network error has occurred. Defaults to ``None`` (no timeout).
  - `connectTimeoutMS`: (integer or None) Controls how long (in
    milliseconds) the driver will wait during server monitoring when
    connecting a new socket to a server before concluding the server
    is unavailable. Defaults to ``20000`` (20 seconds).
  - `serverSelectionTimeoutMS`: (integer) Controls how long (in
    milliseconds) the driver will wait to find an available,
    appropriate server to carry out a database operation; while it is
    waiting, multiple server monitoring operations may be carried out,
    each controlled by `connectTimeoutMS`. Defaults to ``30000`` (30
    seconds).
  - `waitQueueTimeoutMS`: (integer or None) How long (in milliseconds)
    a thread will wait for a socket from the pool if the pool has no
    free sockets. Defaults to ``None`` (no timeout).
  - `waitQueueMultiple`: (integer or None) Multiplied by maxPoolSize
    to give the number of threads allowed to wait for a socket at one
    time. Defaults to ``None`` (no limit).
  - `heartbeatFrequencyMS`: (optional) The number of milliseconds
    between periodic server checks, or None to accept the default
    frequency of 10 seconds.
  - `appname`: (string or None) The name of the application that
    created this MongoClient instance. MongoDB 3.4 and newer will
    print this value in the server log upon establishing each
    connection. It is also recorded in the slow query log and
    profile collections.
  - `event_listeners`: a list or tuple of event listeners. See
    :mod:`~pymongo.monitoring` for details.
  - `socketKeepAlive`: (boolean) **DEPRECATED** Whether to send
    periodic keep-alive packets on connected sockets. Defaults to
    ``True``. Disabling it is not recommended, see
    https://docs.mongodb.com/manual/faq/diagnostics/#does-tcp-keepalive-time-affect-mongodb-deployments",

  | **Write Concern options:**
  | (Only set if passed. No default values.)

  - `w`: (integer or string) If this is a replica set, write operations
    will block until they have been replicated to the specified number
    or tagged set of servers. `w=<int>` always includes the replica set
    primary (e.g. w=3 means write to the primary and wait until
    replicated to **two** secondaries). Passing w=0 **disables write
    acknowledgement** and all other write concern options.
  - `wtimeout`: (integer) Used in conjunction with `w`. Specify a value
    in milliseconds to control how long to wait for write propagation
    to complete. If replication does not complete in the given
    timeframe, a timeout exception is raised.
  - `j`: If ``True`` block until write operations have been committed
    to the journal. Cannot be used in combination with `fsync`. Prior
    to MongoDB 2.6 this option was ignored if the server was running
    without journaling. Starting with MongoDB 2.6 write operations will
    fail with an exception if this option is used when the server is
    running without journaling.
  - `fsync`: If ``True`` and the server is running without journaling,
    blocks until the server has synced all data files to disk. If the
    server is running with journaling, this acts the same as the `j`
    option, blocking until write operations have been committed to the
    journal. Cannot be used in combination with `j`.

  | **Replica set keyword arguments for connecting with a replica set
    - either directly or via a mongos:**

  - `replicaSet`: (string or None) The name of the replica set to
    connect to. The driver will verify that all servers it connects to
    match this name. Implies that the hosts specified are a seed list
    and the driver should attempt to find all members of the set.
    Defaults to ``None``.

  | **Read Preference:**

  - `readPreference`: The replica set read preference for this client.
    One of ``primary``, ``primaryPreferred``, ``secondary``,
    ``secondaryPreferred``, or ``nearest``. Defaults to ``primary``.
  - `readPreferenceTags`: Specifies a tag set as a comma-separated list
    of colon-separated key-value pairs. For example ``dc:ny,rack:1``.
    Defaults to ``None``.
  - `maxStalenessSeconds`: (integer) The maximum estimated
    length of time a replica set secondary can fall behind the primary
    in replication before it will no longer be selected for operations.
    Defaults to ``-1``, meaning no maximum. If maxStalenessSeconds
    is set, it must be a positive integer greater than or equal to
    90 seconds.

  | **Authentication:**

  - `username`: A string.
  - `password`: A string.

    Although username and password must be percent-escaped in a MongoDB
    URI, they must not be percent-escaped when passed as parameters. In
    this example, both the space and slash special characters are passed
    as-is::

      MongoClient(username="user name", password="pass/word")

  - `authSource`: The database to authenticate on. Defaults to the
    database specified in the URI, if provided, or to "admin".
  - `authMechanism`: See :data:`~pymongo.auth.MECHANISMS` for options.
    By default, use SCRAM-SHA-1 with MongoDB 3.0 and later, MONGODB-CR
    (MongoDB Challenge Response protocol) for older servers.
  - `authMechanismProperties`: Used to specify authentication mechanism
    specific options. To specify the service name for GSSAPI
    authentication pass authMechanismProperties='SERVICE_NAME:<service
    name>'

  .. seealso:: :doc:`/examples/authentication`

  | **SSL configuration:**

  - `ssl`: If ``True``, create the connection to the server using SSL.
    Defaults to ``False``.
  - `ssl_certfile`: The certificate file used to identify the local
    connection against mongod. Implies ``ssl=True``. Defaults to
    ``None``.
  - `ssl_keyfile`: The private keyfile used to identify the local
    connection against mongod.  If included with the ``certfile`` then
    only the ``ssl_certfile`` is needed.  Implies ``ssl=True``.
    Defaults to ``None``.
  - `ssl_pem_passphrase`: The password or passphrase for decrypting
    the private key in ``ssl_certfile`` or ``ssl_keyfile``. Only
    necessary if the private key is encrypted. Only supported by python
    2.7.9+ (pypy 2.5.1+) and 3.3+. Defaults to ``None``.
  - `ssl_cert_reqs`: Specifies whether a certificate is required from
    the other side of the connection, and whether it will be validated
    if provided. It must be one of the three values ``ssl.CERT_NONE``
    (certificates ignored), ``ssl.CERT_REQUIRED`` (certificates
    required and validated), or ``ssl.CERT_OPTIONAL`` (the same as
    CERT_REQUIRED, unless the server was configured to use anonymous
    ciphers). If the value of this parameter is not ``ssl.CERT_NONE``
    and a value is not provided for ``ssl_ca_certs`` PyMongo will
    attempt to load system provided CA certificates. If the python
    version in use does not support loading system CA certificates
    then the ``ssl_ca_certs`` parameter must point to a file of CA
    certificates. Implies ``ssl=True``. Defaults to
    ``ssl.CERT_REQUIRED`` if not provided and ``ssl=True``.
  - `ssl_ca_certs`: The ca_certs file contains a set of concatenated
    "certification authority" certificates, which are used to validate
    certificates passed from the other end of the connection.
    Implies ``ssl=True``. Defaults to ``None``.
  - `ssl_crlfile`: The path to a PEM or DER formatted certificate
    revocation list. Only supported by python 2.7.9+ (pypy 2.5.1+)
    and 3.4+. Defaults to ``None``.
  - `ssl_match_hostname`: If ``True`` (the default), and
    `ssl_cert_reqs` is not ``ssl.CERT_NONE``, enables hostname
    verification using the :func:`~ssl.match_hostname` function from
    python's :mod:`~ssl` module. Think very carefully before setting
    this to ``False`` as that could make your application vulnerable to
    man-in-the-middle attacks.

  | **Read Concern options:**
  | (If not set explicitly, this will use the server default)

  - `readConcernLevel`: (string) The read concern level specifies the
    level of isolation for read operations.  For example, a read
    operation using a read concern level of ``majority`` will only
    return data that has been written to a majority of nodes. If the
    level is left unspecified, the server default will be used.

.. mongodoc:: connections

.. versionchanged:: 3.5
   Add ``username`` and ``password`` options. Document the
   ``authSource``, ``authMechanism``, and ``authMechanismProperties ``
   options.
   Deprecated the `socketKeepAlive` keyword argument and URI option.
   `socketKeepAlive` now defaults to ``True``.

.. versionchanged:: 3.0
   :class:`~pymongo.mongo_client.MongoClient` is now the one and only
   client class for a standalone server, mongos, or replica set.
   It includes the functionality that had been split into
   :class:`~pymongo.mongo_client.MongoReplicaSetClient`: it can connect
   to a replica set, discover all its members, and monitor the set for
   stepdowns, elections, and reconfigs.

   The :class:`~pymongo.mongo_client.MongoClient` constructor no
   longer blocks while connecting to the server or servers, and it no
   longer raises :class:`~pymongo.errors.ConnectionFailure` if they
   are unavailable, nor :class:`~pymongo.errors.ConfigurationError`
   if the user's credentials are wrong. Instead, the constructor
   returns immediately and launches the connection process on
   background threads.

   Therefore the ``alive`` method is removed since it no longer
   provides meaningful information; even if the client is disconnected,
   it may discover a server in time to fulfill the next operation.

   In PyMongo 2.x, :class:`~pymongo.MongoClient` accepted a list of
   standalone MongoDB servers and used the first it could connect to::

       MongoClient(['host1.com:27017', 'host2.com:27017'])

   A list of multiple standalones is no longer supported; if multiple
   servers are listed they must be members of the same replica set, or
   mongoses in the same sharded cluster.

   The behavior for a list of mongoses is changed from "high
   availability" to "load balancing". Before, the client connected to
   the lowest-latency mongos in the list, and used it until a network
   error prompted it to re-evaluate all mongoses' latencies and
   reconnect to one of them. In PyMongo 3, the client monitors its
   network latency to all the mongoses continuously, and distributes
   operations evenly among those with the lowest latency. See
   :ref:`mongos-load-balancing` for more information.

   The ``connect`` option is added.

   The ``start_request``, ``in_request``, and ``end_request`` methods
   are removed, as well as the ``auto_start_request`` option.

   The ``copy_database`` method is removed, see the
   :doc:`copy_database examples </examples/copydb>` for alternatives.

   The :meth:`MongoClient.disconnect` method is removed; it was a
   synonym for :meth:`~pymongo.MongoClient.close`.

   :class:`~pymongo.mongo_client.MongoClient` no longer returns an
   instance of :class:`~pymongo.database.Database` for attribute names
   with leading underscores. You must use dict-style lookups instead::

       client['__my_database__']

   Not::

       client.__my_database__
```
