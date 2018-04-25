## Request 请求头常见标识

```
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding:gzip, deflate, br
Accept-Language:zh-CN,zh;q=0.9,en;q=0.8
Connection:keep-alive
Host:bj.lianjia.com
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36
```

upgrade-insecure-requests: 浏览器自动升级请求, 我们的页面是 https 的，而这个页面中包含了大量的 http 资源（图片、iframe等），页面一旦发现存在上述响应头，会在加载 http 资源时自动替换成 https 请求。

## 请求字段[[编辑](https://zh.wikipedia.org/w/index.php?title=HTTP%E5%A4%B4%E5%AD%97%E6%AE%B5&action=edit&section=5)]

| 协议头字段名                                   | 说明                                       | 示例                                       | 状态                                       |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| Accept                                   | 能够接受的回应内容类型（Content-Types）。参见内容协商。       | `Accept: text/plain`                     | 常设                                       |
| Accept-Charset                           | 能够接受的字符集                                 | `Accept-Charset: utf-8`                  | 常设                                       |
| Accept-Encoding                          | 能够接受的编码方式列表。参考[HTTP压缩](https://zh.wikipedia.org/wiki/HTTP%E5%8E%8B%E7%BC%A9)。 | `Accept-Encoding: gzip, deflate`         | 常设                                       |
| Accept-Language                          | 能够接受的回应内容的自然语言列表。参考 内容协商 。               | `Accept-Language: en-US`                 | 常设                                       |
| Accept-Datetime                          | 能够接受的按照时间来表示的版本                          | `Accept-Datetime: Thu, 31 May 2007 20:35:00 GMT` | 临时                                       |
| Authorization                            | 用于超文本传输协议的认证的认证信息                        | `Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==` | 常设                                       |
| [Cache-Control](https://zh.wikipedia.org/wiki/%E7%BD%91%E9%A1%B5%E5%BF%AB%E7%85%A7) | 用来指定在这次的请求/响应链中的所有缓存机制 都必须 遵守的指令         | `Cache-Control: no-cache`                | 常设                                       |
| Connection                               | 该浏览器想要优先使用的连接类型[[8\]](https://zh.wikipedia.org/wiki/HTTP%E5%A4%B4%E5%AD%97%E6%AE%B5#cite_note-rfc7230_connection-8) | `Connection: keep-alive``Connection: Upgrade` | 常设                                       |
| Cookie                                   | 之前由服务器通过 Set- Cookie （下文详述）发送的一个 超文本传输协议Cookie | `Cookie: $Version=1; Skin=new;`          | 常设: 标准                                   |
| Content-Length                           | 以 八位字节数组 （8位的字节）表示的请求体的长度                | `Content-Length: 348`                    | 常设                                       |
| Content-MD5                              | 请求体的内容的二进制 MD5 散列值，以 Base64 编码的结果        | `Content-MD5: Q2hlY2sgSW50ZWdyaXR5IQ==`  | 过时的[[9\]](https://zh.wikipedia.org/wiki/HTTP%E5%A4%B4%E5%AD%97%E6%AE%B5#cite_note-9) |
| Content-Type                             | 请求体的 多媒体类型 （用于POST和PUT请求中）               | `Content-Type: application/x-www-form-urlencoded` | 常设                                       |
| Date                                     | 发送该消息的日期和时间(按照 RFC 7231 中定义的"超文本传输协议日期"格式来发送) | `Date: Tue, 15 Nov 1994 08:12:31 GMT`    | 常设                                       |
| Expect                                   | 表明客户端要求服务器做出特定的行为                        | `Expect: 100-continue`                   | 常设                                       |
| From                                     | 发起此请求的用户的邮件地址                            | `From: user@example.com`                 | 常设                                       |
| Host                                     | 服务器的域名(用于虚拟主机 )，以及服务器所监听的[传输控制协议](https://zh.wikipedia.org/wiki/%E4%BC%A0%E8%BE%93%E6%8E%A7%E5%88%B6%E5%8D%8F%E8%AE%AE)端口号。如果所请求的端口是对应的服务的标准端口，则端口号可被省略。[[10\]](https://zh.wikipedia.org/wiki/HTTP%E5%A4%B4%E5%AD%97%E6%AE%B5#cite_note-10) 自超文件传输协议版本1.1（HTTP/1.1）开始便是必需字段。 | `Host: en.wikipedia.org:80``Host: en.wikipedia.org` | 常设                                       |
| If-Match                                 | 仅当客户端提供的实体与服务器上对应的实体相匹配时，才进行对应的操作。主要作用时，用作像 PUT 这样的方法中，仅当从用户上次更新某个资源以来，该资源未被修改的情况下，才更新该资源。 | `If-Match: "737060cd8c284d8af7ad3082f209582d"` | 常设                                       |
| If-Modified-Since                        | 允许在对应的内容未被修改的情况下返回304未修改（ 304 Not Modified ） | `If-Modified-Since: Sat, 29 Oct 1994 19:43:31 GMT` | 常设                                       |
| If-None-Match                            | 允许在对应的内容未被修改的情况下返回304未修改（ 304 Not Modified ），参考 超文本传输协议 的[实体标记](https://zh.wikipedia.org/wiki/HTTP_ETag) | `If-None-Match: "737060cd8c284d8af7ad3082f209582d"` | 常设                                       |
| If-Range                                 | 如果该实体未被修改过，则向我发送我所缺少的那一个或多个部分；否则，发送整个新的实体 | `If-Range: "737060cd8c284d8af7ad3082f209582d"` | 常设                                       |
| If-Unmodified-Since                      | 仅当该实体自某个特定时间已来未被修改的情况下，才发送回应。            | `If-Unmodified-Since: Sat, 29 Oct 1994 19:43:31 GMT` | 常设                                       |
| Max-Forwards                             | 限制该消息可被代理及网关转发的次数。                       | `Max-Forwards: 10`                       | 常设                                       |
| Origin                                   | 发起一个针对 跨来源资源共享 的请求（要求服务器在回应中加入一个‘访问控制-允许来源’（'Access-Control-Allow-Origin'）字段）。 | `Origin: http://www.example-social-network.com` | 常设: 标准                                   |
| Pragma                                   | 与具体的实现相关，这些字段可能在请求/回应链中的任何时候产生多种效果。      | `Pragma: no-cache`                       | 常设但不常用                                   |
| Proxy-Authorization                      | 用来向代理进行认证的认证信息。                          | `Proxy-Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==` | 常设                                       |
| Range                                    | 仅请求某个实体的一部分。字节偏移以0开始。参见[字节服务](https://zh.wikipedia.org/w/index.php?title=%E5%AD%97%E8%8A%82%E6%9C%8D%E5%8A%A1&action=edit&redlink=1)。 | `Range: bytes=500-999`                   | 常设                                       |
| [Referer](https://zh.wikipedia.org/wiki/HTTP%E5%8F%83%E7%85%A7%E4%BD%8D%E5%9D%80) [*sic*] [[11\]](https://zh.wikipedia.org/wiki/HTTP%E5%A4%B4%E5%AD%97%E6%AE%B5#cite_note-11) | 表示浏览器所访问的前一个页面，正是那个页面上的某个链接将浏览器带到了当前所请求的这个页面。 | `Referer: http://en.wikipedia.org/wiki/Main_Page` | 常设                                       |
| TE                                       | 浏览器预期接受的传输编码方式：可使用回应协议头 Transfer-Encoding 字段中的值；另外还可用"trailers"（与"分块 "传输方式相关）这个值来表明浏览器希望在最后一个尺寸为0的块之后还接收到一些额外的字段。 | `TE: trailers, deflate`                  | 常设                                       |
| User-Agent                               | 浏览器的[浏览器身份标识字符串](https://zh.wikipedia.org/wiki/%E7%94%A8%E6%88%B7%E4%BB%A3%E7%90%86) | `User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0` | 常设                                       |
| Upgrade                                  | 要求服务器升级到另一个协议。                           | `Upgrade: HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11` | 常设                                       |
| Via                                      | 向服务器告知，这个请求是由哪些代理发出的。                    | `Via: 1.0 fred, 1.1 example.com (Apache/1.1)` | 常设                                       |
| Warning                                  | 一个一般性的警告，告知，在实体内容体中可能存在错误。               | `Warning: 199 Miscellaneous warning`     | 常设                                       |







| 应答头              | 说明                                       |
| ---------------- | ---------------------------------------- |
| Allow            | 服务器支持哪些请求方法（如GET、POST等）。                 |
| Content-Encoding | 文档的编码（Encode）方法。只有在解码之后才可以得到Content-Type头指定的内容类型。利用gzip压缩文档能够显著地减少HTML文档的下载时间。Java的GZIPOutputStream可以很方便地进行gzip压缩，但只有Unix上的Netscape和Windows上的IE 4、IE 5才支持它。因此，Servlet应该通过查看Accept-Encoding头（即request.getHeader("Accept-Encoding")）检查浏览器是否支持gzip，为支持gzip的浏览器返回经gzip压缩的HTML页面，为其他浏览器返回普通页面。 |
| Content-Length   | 表示内容长度。只有当浏览器使用持久HTTP连接时才需要这个数据。如果你想要利用持久连接的优势，可以把输出文档写入 ByteArrayOutputStream，完成后查看其大小，然后把该值放入Content-Length头，最后通过byteArrayStream.writeTo(response.getOutputStream()发送内容。 |
| Content-Type     | 表示后面的文档属于什么MIME类型。Servlet默认为text/plain，但通常需要显式地指定为text/html。由于经常要设置Content-Type，因此HttpServletResponse提供了一个专用的方法setContentType。 |
| Date             | 当前的GMT时间。你可以用setDateHeader来设置这个头以避免转换时间格式的麻烦。 |
| Expires          | 应该在什么时候认为文档已经过期，从而不再缓存它？                 |
| Last-Modified    | 文档的最后改动时间。客户可以通过If-Modified-Since请求头提供一个日期，该请求将被视为一个条件GET，只有改动时间迟于指定时间的文档才会返回，否则返回一个304（Not Modified）状态。Last-Modified也可用setDateHeader方法来设置。 |
| Location         | 表示客户应当到哪里去提取文档。Location通常不是直接设置的，而是通过HttpServletResponse的sendRedirect方法，该方法同时设置状态代码为302。 |
| Refresh          | 表示浏览器应该在多少时间之后刷新文档，以秒计。除了刷新当前文档之外，你还可以通过setHeader("Refresh", "5; URL=http://host/path")让浏览器读取指定的页面。 注意这种功能通常是通过设置HTML页面HEAD区的＜META HTTP-EQUIV="Refresh" CONTENT="5;URL=http://host/path"＞实现，这是因为，自动刷新或重定向对于那些不能使用CGI或Servlet的HTML编写者十分重要。但是，对于Servlet来说，直接设置Refresh头更加方便。 注意Refresh的意义是"N秒之后刷新本页面或访问指定页面"，而不是"每隔N秒刷新本页面或访问指定页面"。因此，连续刷新要求每次都发送一个Refresh头，而发送204状态代码则可以阻止浏览器继续刷新，不管是使用Refresh头还是＜META HTTP-EQUIV="Refresh" ...＞。 注意Refresh头不属于HTTP 1.1正式规范的一部分，而是一个扩展，但Netscape和IE都支持它。 |
| Server           | 服务器名字。Servlet一般不设置这个值，而是由Web服务器自己设置。     |
| Set-Cookie       | 设置和页面关联的Cookie。Servlet不应使用response.setHeader("Set-Cookie", ...)，而是应使用HttpServletResponse提供的专用方法addCookie。参见下文有关Cookie设置的讨论。 |
| WWW-Authenticate | 客户应该在Authorization头中提供什么类型的授权信息？在包含401（Unauthorized）状态行的应答中这个头是必需的。例如，response.setHeader("WWW-Authenticate", "BASIC realm=＼"executives＼"")。 注意Servlet一般不进行这方面的处理，而是让Web服务器的专门机制来控制受密码保护页面的访问（例如.htaccess）。 |