# TopTop 分析



### 获取用户信息

```
curl -H 'Host: api.taptapdada.com' -H 'User-Agent: okhttp/3.6.0' --compressed 'https://api.taptapdada.com/user/v1/detail?id=15232025&X-UA=V%3D1%26PN%3DTapTap%26VN_CODE%3D517%26LOC%3DCN%26LANG%3Dzh_CN%26CH%3Ddefault%26UID%3D36d85b58-9f06-4e18-a94b-6caa26defb7a'

curl -H 'Host: api.taptapdada.com' -H 'User-Agent: okhttp/3.6.0' --compressed 'https://api.taptapdada.com/user/v1/detail?id=15232025&X-UA=V%3D1%26PN%3DTapTap%26VN_CODE%3D517%26LOC%3DCN%26LANG%3Dzh_CN%26CH%3Ddefault%26UID%3D36d85b58-9f06-4e18-a94b-6caa26defb7a'


https://api.taptapdada.com/user/v1/detail?id=15232025&X-UA=

V=1&
PN=TapTap&
VN_CODE=517&
LANG=zh_CN&
CH=default&
LOC=CN&
UID=36d85b58-9f06-4e18-a94b-6caa26defb7a


https://api.taptapdada.com/user/v1/detail?id=15232025&X-UA=V%3d1%26PN%3dTapTap%26VN_CODE%3d517%26LANG%3dzh_CN%26CH%3ddefault%26LOC%3dCN
```



##  获取用户玩过的游戏

```
curl -H 'Host: api.taptapdada.com' -H 'User-Agent: okhttp/3.6.0' --compressed 'https://api.taptapdada.com/user-app/v1/by-user?X-UA=V%3D1%26PN%3DTapTap%26VN_CODE%3D517%26LOC%3DCN%26LANG%3Dzh_CN%26CH%3Ddefault%26UID%3D36d85b58-9f06-4e18-a94b-6caa26defb7a&sort=updated&from=0&user_id=15232025&limit=10'


https://api.taptapdada.com/user-app/v1/by-user?X-UA=V%3D1%26PN%3DTapTap%26VN_CODE%3D517%26LOC%3DCN%26LANG%3Dzh_CN%26CH%3Ddefault%26UID%3D36d85b58-9f06-4e18-a94b-6caa26defb7a

&sort=updated
&from=0
&user_id=15232025
&limit=10
```



### 获取用户玩的最多的游戏

```
curl -H 'Host: api.taptapdada.com' -H 'User-Agent: okhttp/3.6.0' --compressed 'https://api.taptapdada.com/user-app/v1/purchased-by-user?from=0&user_id=15232025&limit=10&X-UA=V%3D1%26PN%3DTapTap%26VN_CODE%3D517%26LOC%3DCN%26LANG%3Dzh_CN%26CH%3Ddefault%26UID%3D36d85b58-9f06-4e18-a94b-6caa26defb7a'
```



### 获取游戏论坛等级

```
curl -H 'Host: api.taptapdada.com' -H 'User-Agent: okhttp/3.6.0' --compressed 'https://api.taptapdada.com/forum-level/v1/by-user?user_id=15232025&X-UA=V%3D1%26PN%3DTapTap%26VN_CODE%3D517%26LOC%3DCN%26LANG%3Dzh_CN%26CH%3Ddefault%26UID%3D36d85b58-9f06-4e18-a94b-6caa26defb7a'
```



### 获取某用户所以评论列表

```
curl -H 'Host: api.taptapdada.com' -H 'User-Agent: okhttp/3.6.0' --compressed 'https://api.taptapdada.com/feed/v1/by-user?action=publish_review&user_id=15232025&X-UA=V%3D1%26PN%3DTapTap%26VN_CODE%3D517%26LOC%3DCN%26LANG%3Dzh_CN%26CH%3Ddefault%26UID%3D36d85b58-9f06-4e18-a94b-6caa26defb7a'
```



### 获取某用户回复列表

```
curl -H 'Host: api.taptapdada.com' -H 'User-Agent: okhttp/3.6.0' --compressed 'https://api.taptapdada.com/feed/v1/by-user?action=reply&user_id=15232025&X-UA=V%3D1%26PN%3DTapTap%26VN_CODE%3D517%26LOC%3DCN%26LANG%3Dzh_CN%26CH%3Ddefault%26UID%3D36d85b58-9f06-4e18-a94b-6caa26defb7a'
```



### 获取某用户帖子列表

```
curl -H 'Host: api.taptapdada.com' -H 'User-Agent: okhttp/3.6.0' --compressed 'https://api.taptapdada.com/feed/v1/by-user?action=publish_topic&user_id=15232025&X-UA=V%3D1%26PN%3DTapTap%26VN_CODE%3D517%26LOC%3DCN%26LANG%3Dzh_CN%26CH%3Ddefault%26UID%3D36d85b58-9f06-4e18-a94b-6caa26defb7a'
```



### 获取游戏评论列表



```
https://api.taptapdada.com/review/v1/by-app?app_id=4682&from=0&limit=10&X-UA=V%3D1%26PN%3DTapTap%26VN_CODE%3D517%26LOC%3DCN%26LANG%3Dzh_CN%26CH%3Ddefault%26UID%3D36d85b58-9f06-4e18-a94b-6caa26defb7a
```

```
curl -H 'Host: www.taptap.com' -H 'Accept: */*' -H 'Content-Type: application/json' -H 'Cookie: tap_sess=eyJpdiI6InErMjFxQkwyZTJCbVhyXC9GbXVSWXZRPT0iLCJ2YWx1ZSI6IldcLzE3Qk80WjF5MnVscjFPT0dXMUJFZE94M2V3K0ZaRE1Bd3RwQVV2bmJjUGtOZDBjdVBBMW1HQitCcStYN0grQ2lndGhpaWkrWnViaGVyUmhBakl1QT09IiwibWFjIjoiYTI1ZTRkYTcwOGZjNzc4MDVmM2EzNjdiMzQ5ZmEyNDBkNWM1ZjZjOThmY2JmNWFkZGYyY2I2OTkwM2JiYjExMCJ9' -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E302 MicroMessenger/6.6.6 NetType/WIFI Language/zh_CN' -H 'Referer: https://servicewechat.com/wxe411b73681831d00/4/page-frame.html' -H 'Accept-Language: zh-cn' --compressed 'https://www.taptap.com/webapi/review/v1/list?app_id=130841&X-UA=V%3D1%26PN%3DWeChat%26LANG%3Dzh_CN%26VN%3D0.0.1%26LOC%3DCN%26PLT%3DiOS'



curl -H 'Host: www.taptap.com' -H 'Accept: */*' -H 'Content-Type: application/json' -H 'Cookie: tap_sess=eyJpdiI6Ik0wYXcwUEkwZTNcLzhpeHhjWk9yTDdnPT0iLCJ2YWx1ZSI6IkNpNWR5cWw5OHhZT29DTUJHaUI5eEV3ZXpUWTY2Q1RSSldIZWhWRVcwY25objZVM2JRb0hucEc1anNQSTdocndrNFMrUlRNVVZOVTBmSytYQnhhOHF3PT0iLCJtYWMiOiI5NjMzYWNhYjY1YzZlZGNmNGIzNzNkZjhmMGFmMDFiNjgyN2E1Y2I3ZDM3YmQxYjY0MDZmYTRlMTljMTVkOTQyIn0=' -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E302 MicroMessenger/6.6.6 NetType/WIFI Language/zh_CN' -H 'Referer: https://servicewechat.com/wxe411b73681831d00/4/page-frame.html' -H 'Accept-Language: zh-cn' --compressed 'https://www.taptap.com/webapi/review/v1/list?app_id=64403&limit=10&from=10&X-UA=V%3D1%26PN%3DWeChat%26LANG%3Dzh_CN%26VN%3D0.0.1%26LOC%3DCN%26PLT%3DiOS'
```

