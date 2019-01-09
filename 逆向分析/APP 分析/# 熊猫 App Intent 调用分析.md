# 熊猫 App Intent 调用分析



## Intent

```Java
Intent { flg=0x4000000 cmp=com.panda.videoliveplatform/.activity.LiveRoomActivity (has extras) } 
dat=null Extras=Bundle[{idRoom=60995, __referer=index4-recommend-recommendcate-hot_recommend-1_0-0, style_type=1, display_type=2}]
intent.getExtras().keySet() = android.util.MapCollections$KeySet@f4181782

 key=idRoom v=60995
 key=__referer v=index4-recommend-recommendcate-hot_recommend-1_0-0
 key=style_type v=1
 key=display_type v=2
```



scheme 协议

```
pandatv://openroom/9999?pdt=2.14.h.2.3jdu0kmn22k
```



```
url:   https://m.panda.tv/room.html?roomid=694596&pdt=2.1.b8.1.337gqoui16j

scheme:  pandatv://openroom/694596?pdt=2.14.h.2.70icnaltdbo

url:  https://m.panda.tv/room.html?roomid=479812&pdt=2.1.b0.1.73me4q4mj5j

scheme:  
pandatv://openroom/479812?pdt=2.14.h.2.2g658kukqt2



```



熊猫参数部分：

```

## 手游
game4-shouyou-livecate-items_shouyou_room-1_1-0		1	2
game4-shouyou-livecate-items_shouyou_room-1_4-0		1	2

## 吃鸡手游
game4-cjsy-livecate-items_cjsy_room-1_5-0	1	2
```





熊猫的 github 地址

`git@git.pandatv.com:webtech/sdk-pdt.git`



熊猫的生成方式



## 抓取方案：

抓取M站，

```
https://api.m.panda.tv/index.php?method=category.list&type=game

# 获取类别
https://m.panda.tv/recreation.html?cate=acg&pdt=2.12.c.1.1vdi0fa4b8n

# 获列表
https://api.m.panda.tv/ajax_get_live_list_by_cate?pageno=2&pagenum=10&__plat=h5&cate=acg
```

