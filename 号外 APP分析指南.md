## 号外 APP分析指南



号外产品的理解与体验，

1，简述最满意的一种爬取设计代码。

2、分析号外APP的爬取和反爬原因。



一、从抓包来看。

```
version	1.72
time	1520912912540
verify	aa19ecfb075102aac738da0dd8f3de58

是对请求的部分参数做了MD5 加密验证。

先简单的对参数做一个MD5 看一下
https://api.hwoutput.com/v1/channel/defaultChannelList?version=1.72&time=1520913173139&verify=dc2e6e7ca26f239b2254bbe4d619653e
```

 对每个请求做了请求验证。

```
curl -H 'User-Agent: Dalvik/1.6.0 (Linux; U; Android 4.4.4; vivo Y13L Build/KTU84P)' -H 'Host: api-ext.mediav.com' --data '{"data":{"os":1,"sdkv":"1.3","sdkcorev":"1020","agappkey":"agPkuGsc7cFs","pver":"1","carrier":"","net":1,"m2id":"c905dbf609d165f0e4bf856b26af7db9"},"authName":"juhe1"}' --compressed 'https://api-ext.mediav.com/external/app/info'

```



二、从APP破解来看。





评论，用户信息浏览量。