# Wormhole

Wormhole意为虫洞，其目标是提供一个快速响应、自动同步的集群缓存框架。

Wormhole在每个客户端运行一个缓存管理器，用于管理本地缓存空间中的对象。而当任何一个节点的缓存对象发生变更（修改或删除）时，都将自动同步到其它节点。这意味着每个节点在获取缓存信息时，都是从本地内存中直接读取，因而可以快速获得响应。而仅当本地内存中无法获得相应缓存对象时，才轮询其它节点。并且在获得缓存对象时，立即缓存到本地内存中。

Wormhole在进行缓存对象远程传输时，需要将对象序列化，因此缓存对象需要实现java.io.Serializable接口。同时，Wormhole会将序列化后的二进制流转化为十六进制字符串，因此可以方便地通过HTTP/HTTPS/SOCKET协议进行传输。

Wormhole使用多线程异步进行数据的远程同步，以提高同步效率。并且在向远程缓存节点获取数据时，采用多个节点同时获取的方式，并且在收到任一节点数据时立即返回，避免个别节点故障引起的级联反应。