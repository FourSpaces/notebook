# 打开各大视频app 的方法



## 优酷视频



### **youku-open-app.js**

```javascript
$("#" + c + " .installed").click(function() {
        if (-1 != navigator.userAgent.indexOf("MicroMessenger"))
            return Log.log(1, "tp=1&cp=4009386&cpp=1000752"), window.open("http://a.app.qq.com/o/simple.jsp?pkgname=com.youku.phone&g_f=992258", "target=_blank"), !1;
        $("body").append("<div class='yk-mask' style='height:" + $(document).height() + "px;'></div>");
        $("#player").css("visibility", "hidden");
        $("#wintipsApp").show();
        if (null != window.navigator.userAgent.match(/android/i)&&-1 != window.navigator.userAgent.indexOf("Chrome"))
            window.open("intent://play?vid=" + videoIdEn + "&source=mplaypage&cookieid=" + e + "#Intent;scheme=youku;package=com.youku.phone;end;");
        else {
            var a = document.createElement("iframe");
            a.height = 0;
            a.width = 0;
            a.src = "youku://play?vid=" + videoIdEn + "&source=mplaypage&cookieid=" + e;
            $("body").append(a)
        }
        "app-download" == c ? f = "tp=1&cp=4008914&cpp=1000687" : "paike-download" ==
        c && (f = "tp=1&cp=4009034&cpp=1000752");
        "app-download" == c ? f = "tp=1&cp=4008914&cpp=1000687" : "paike-download" == c && (f = "tp=1&cp=4009034&cpp=1000752");
        1 == window.ispaike && (f = "tp=1&cp=4009150&cpp=1000752");
        Log.log(1, f)
    });
```



优酷open app 格式：

```
youku://play?vid=XMzU4NjMwNjA4NA

youku://play?vid=XMzU5NzI4NTg1Ng

youku://play?vid=XMzU5OTk3MDA0MA

youku://play?vid=XMzU5OTkwMzM4OA
```



## 爱奇艺视频

源URL： http://m.iqiyi.com/v_19rrdkbu90.html#30-26-15-7

```
vid 参见
http://cache.m.iqiyi.com/jp/tmts/1050059400/2c3d67cb3e8448d34459f9ceeabb7a0e/?uid=&cupid=qc_100001_100102&platForm=h5&qyid=a3052def1a8b4285d74383d14beadbf1&agenttype=12&type=m3u8&nolimit=&k_ft1=8&rate=1&sgti=12_a3052def1a8b4285d74383d14beadbf1_1526552409909&codeflag=1&preIdAll=_0a717c47c5678dd3505ed1500dd8382c-229763217_df17f9fe7aa70365a81d051869efb449-225245017_24871dbc1fd5c2f035e7e47367b0d665-_610405a4789ab03db9ae7ad2165782af-229704217_a5b1e232d938b5f5c4acafc4984a4856-229121417_5a08933ca39f7541dc92b17c7f0938ce&dfp=e1fcef99df98e24043afb2a4a1eb1dae893e24c098bfc838bd780d92bfd9004b98&qd_v=1&qdy=a&qds=0&tm=1526552410&src=02020031010000000000&vf=9715cae4bdb2d8ad5d71b26fac0913c6&callback=tmtsCallback

从中取出
```



爱奇艺open app 格式：

```
qiyi-iphone://paly?vid=2c3d67cb3e8448d34459f9ceeabb7a0e
```



## 腾讯视频



腾讯open app 格式：

```

```

