# ST准备

获取服务器信息

### 获取http头搜集服务器信息

```
curl -I av1.xdrig.com

[root@hadoop10 jdk64]# curl -I https://av1.xdrig.com/
HTTP/1.1 200 OK
Date: Fri, 25 Jan 2019 06:10:33 GMT
Content-Type: application/octet-stream
Content-Length: 2
Connection: keep-alive
Server: nginx
```

### 通过设置User Agent 和Porxy代理突破服务限制

```
curl -I -A 'Mazilla/4.0 (compatible;MSIE 6.0;Windows NT5.0) ' https://av1.xdrig.com

[root@hadoop10 jdk64]# curl -I -A 'Mazilla/4.0 (compatible;MSIE 6.0;Windows NT5.0) ' https://av1.xdrig.com
HTTP/1.1 200 OK
Date: Fri, 25 Jan 2019 06:14:16 GMT
Content-Type: application/octet-stream
Content-Length: 2
Connection: keep-alive
Server: nginx
```



```
curl -I -X PUT https://av1.xdrig.com
curl -I -X GET https://av1.xdrig.com
curl -I -X HEAD https://av1.xdrig.com
curl -I -X POST https://av1.xdrig.com [x]
curl -I -X PUT https://av1.xdrig.com [x]
curl -I -X DELETE https://av1.xdrig.com [x]
curl -I -X OPTIONS https://av1.xdrig.com [X]


```

