# 斗鱼 app Intent 调用分析



### Intent 事例

```java

```



### Intent 源码

```
Intent { cmp=air.tv.douyu.android/tv.douyu.view.activity.PlayerActivity (has extras) } 
dat=null Extras=Bundle[{roomId=4888040}]
intent.getExtras().keySet() = android.util.MapCollections$KeySet@c8d8bf56
key=roomId v=4888040
```



```
Intent { cmp=air.tv.douyu.android/com.douyu.module.user.login.LoginDialogActivity (has extras) } dat=null Extras=Bundle[{fromActivityName=tv.douyu.view.activity.MainActivity, fullScreen=false, fac=startup_loading, reg_tran_bean=RegTranBean{roomId='null', cateId='null', tagId='null', childId='null', vid='null', lon='', lat='', imei='', fac=''}, KEY_LOGIN_TYPE=0}]
intent.getExtras().keySet() = android.util.MapCollections$KeySet@c160acb0
 key=fromActivityName v=tv.douyu.view.activity.MainActivity
 key=fullScreen v=false
 key=fac v=startup_loading
 key=reg_tran_bean v=RegTranBean{roomId='null', cateId='null', tagId='null', childId='null', vid='null', lon='', lat='', imei='', fac=''}
 key=KEY_LOGIN_TYPE v=0
```



```
Intent { act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] flg=0x10000000 pkg=air.tv.douyu.android cmp=air.tv.douyu.android/tv.douyu.view.activity.SplashActivity (has extras) } dat=null Extras=Bundle[{_META_|_sender_=Bundle[{_META_|_ui_callback_=com.meta.xyx233.core.home.LoadingActivity$1@2fea5376}]}]
intent.getExtras().keySet() = android.util.MapCollections$KeySet@60c80c6c
 key=_META_|_sender_ v=Bundle[{_META_|_ui_callback_=com.meta.xyx233.core.home.LoadingActivity$1@2fea5376}]
```



```
douyutvtest://platformapi/startApp?room_id=" + t + "&isVertical=" + e + "&room_src=" + n + "&isVideo=" + r


douyutvtest://platformapi/startApp?room_id=3318573&isVertical=1&room_src=https://rpic.douyucdn.cn/live-cover/appCovers/2018/05/30/3318573_20180530091644_big.jpg&isVideo=0
```

 参数部分 见：https://m.douyu.com/4888040 源码部分



## 小程序接口



### 获取直播列表

```
curl -H 'Host: wxapp.douyucdn.cn' -H 'Content-Type: application/json' -H 'Accept: */*' -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E302 MicroMessenger/6.6.6 NetType/4G Language/zh_CN' -H 'Referer: https://servicewechat.com/wxca1e8ba3fe18ff11/2/page-frame.html' -H 'Accept-Language: zh-cn' --compressed 'https://wxapp.douyucdn.cn/api/room/list?type=&page=29'


curl -H 'Host: wxapp.douyucdn.cn' -H 'Content-Type: application/json' -H 'Accept: */*' -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E302 MicroMessenger/6.6.6 NetType/4G Language/zh_CN' -H 'Referer: https://servicewechat.com/wxca1e7ba3fe18ff12/2/page-frame.html' -H 'Accept-Language: zh-cn' --compressed 'https://wxapp.douyucdn.cn/api/room/list?type=&page=27'
```

