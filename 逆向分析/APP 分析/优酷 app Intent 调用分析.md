# 优酷 app Intent 调用分析



### Intent 事例

```Java
public void startYouku(View view) {
// SAMPLE INTENT for youku video detail page
// 05-12 15:46:13.638 1660-1685/? I/ActivityManager: START u0 {act=android.intent.action.VIEW cat=[android.intent.category.BROWSABLE] dat=youku://play?spm=a2hww.20020887.m_205923.5~5~5~5~5!7~5~5~A&ishttps=1&action=play&vid=XMzU5ODUxNDM0NA&source=yksmartbanner&ua=Mozilla/5.0 (Linux; Android 7.1.1; MIX 2 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36&ccts=1526111173434&cookieid=1526109589838PZc|1xl9ol flg=0x14000000 pkg=com.youku.phone cmp=com.youku.phone/com.youku.ui.activity.DetailActivity (has extras)} from uid 10176 on display 0

        Intent intent = new Intent(Intent.ACTION_VIEW);
        //intent.setData(Uri.parse("youku://play?spm=a2hww.20020887.m_205923.5~5~5~5~5!7~5~5~A&ishttps=1&action=play&vid=XMzU5ODUxNDM0NA&source=yksmartbanner&ua=Mozilla/5.0 (Linux; Android 7.1.1; MIX 2 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36&ccts=1526111173434&cookieid=1526109589838PZc|1xl9ol"));
        //intent.setData(Uri.parse("youku://play?ishttps=1&action=play&vid=XMzI2OTUzOTE2&source=youku://root&ua=123456&ccts=1527846755334&cookieid=112"));
//        intent1.setData(Uri.parse("youku://play?spm=a2hww.20020887.m_205923.5~5~5~5~5!7~5~5~A&action=play&vid=XMzU5ODUxNDM0NA"));

        intent.addCategory(Intent.CATEGORY_BROWSABLE);
//        intent1.addFlags(0x14000000);
        intent.setData(Uri.parse("youku://play"));
        intent.setPackage("com.youku.phone");
        ComponentName cmp = new ComponentName("com.youku.phone", "com.youku.ui.activity.DetailActivity");
        intent.setComponent(cmp);
        intent.putExtra("system_info", "{\"childGender\":-1,\n" +
                "\t\"deviceId\":\"WwJSWxpPubUDAJhsu81fr4Ss\",\n" +
                "\t\"pid\":\"cdafa455e77a8ce0\",\n" +
                "\t\"childAgeMonth\":-1,\n" +
                "\t\"time\":1527854060,\n" +
                "\t\"ouid\":\"\",\n" +
                "\t\"guid\":\"5d5881125a210a946743bac911db6807\",\n" +
                "\t\"btype\":\"Coolpad+8712\",\n" +
                "\t\"os\":\"Android\",\n" +
                "\t\"network\":\"WIFI\",\n" +
                "\t\"operator\":\"\",\n" +
                "\t\"brand\":\"Coolpad\",\n" +
                "\t\"resolution\":\"854*480\",\n" +
                "\t\"osVer\":\"5.1\",\n" +
                "\t\"appPackageKey\":\"com.youku.phone\",\n" +
                "\t\"ver\":\"7.3.0\"\n" +
                "\t}");

        intent.putExtra("video_channel_type", 1); // 没搞明白 1 和 2 的区别
        intent.putExtra("referrer", "youku://root");
        intent.putExtra("cid", 97); //感觉像是城市ID
        intent.putExtra("type", "JUMP_TO_SHOW");

        intent.putExtra("stage_photo", "http://ykimg.alicdn.com/product/image/2018-05-31/8e9d8ee75b2dc55b3b3491e21754731a.jpg");
        intent.putExtra("sessionId", "XMzI2OTUzOTE2;1527853115411");
        intent.putExtra("video_id", "XMzI2OTUzOTE2");


        startActivity(intent);
        String tsg = "testOnetee=";
        System.out.println(tsg + intent);
        System.out.println(tsg + " intent.getExtras().keySet() = " + intent.getExtras().keySet());
        for (String s : intent.getExtras().keySet()) {
            System.out.println(tsg + " key=" + s + "  v=" + intent.getExtras().get(s));
        }
    }
```



### Intent 参数

```
Intent { act=android.intent.action.VIEW dat=youku://play pkg=com.youku.phone cmp=com.youku.phone/com.youku.ui.activity.DetailActivity (has extras) } 

# 参数部分
dat=youku://play 

Extras=Bundle[
{
system_info=
	{"childGender":-1,
	"deviceId":"WwJSWxpPubUDAJhsu81fr4Ss",
	"pid":"cdafa455e77a8ce0",
	"childAgeMonth":-1,
	"time":1527853069,
	"ouid":"",
	"guid":"5d5881125a210a946743bac911db6807",
	"btype":"Coolpad+8712",
	"os":"Android",
	"network":"WIFI",
	"operator":"",
	"brand":"Coolpad",
	"resolution":"854*480",
	"osVer":"5.1",
	"appPackageKey":"com.youku.phone",
	"ver":"7.3.0"
	}, 

video_channel_type=2, 
referrer=youku://root, 
cid=97, 
type=JUMP_TO_SHOW, 
stage_photo=http://ykimg.alicdn.com/product/image/2018-06-01/716a5e1ed6b69178355aac32a6c409f3.jpg, sessionId=37465befbfbdefbfbd7f;1527853115411, 
video_id=37465befbfbdefbfbd7f

}

]
```



### 参数解释

```
system_info:
	- name: deviceId  设备的唯一ID deviceId
    - value: WwJSWxpPubUDAJhsu81fr4Ss
    
    - pid: 进程IDß
    - value: cdafa455e77a8ce0
    
    - 
```



最简单的代码

```
 public void startYouku(View view) {
// SAMPLE INTENT for youku video detail page
// 05-12 15:46:13.638 1660-1685/? I/ActivityManager: START u0 {act=android.intent.action.VIEW cat=[android.intent.category.BROWSABLE] dat=youku://play?spm=a2hww.20020887.m_205923.5~5~5~5~5!7~5~5~A&ishttps=1&action=play&vid=XMzU5ODUxNDM0NA&source=yksmartbanner&ua=Mozilla/5.0 (Linux; Android 7.1.1; MIX 2 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36&ccts=1526111173434&cookieid=1526109589838PZc|1xl9ol flg=0x14000000 pkg=com.youku.phone cmp=com.youku.phone/com.youku.ui.activity.DetailActivity (has extras)} from uid 10176 on display 0

        Intent intent = new Intent(Intent.ACTION_VIEW);
        intent.addCategory(Intent.CATEGORY_BROWSABLE);
        intent.setData(Uri.parse("youku://play"));
        intent.setPackage("com.youku.phone");
        ComponentName cmp = new ComponentName("com.youku.phone", "com.youku.ui.activity.DetailActivity");
        intent.putExtra("video_id", "XMzI2OTUzOTE2");
        startActivity(intent);
        }
    }
```



### 获取集数列表

```
http://v.youku.com/page/playlist?&l=debug&pm=3&vid=893381655&fid=0&showid=326258&sid=0&componentid=38011&videoCategoryId=97&isSimple=false&videoEncodeId=XMzU3MzUyNjYyMA%3D%3D&page=2&callback=tuijsonp20
```



```
https://acs.youku.com/h5/mtop.youku.haixing.play.h5.detail.single/1.0/?jsv=2.4.11&appKey=24679788&t=1527862347004&sign=58a57578a62e5bce80de2bca8b47315c&v=1.0&type=originaljson&dataType=json&api=mtop.youku.haixing.play.h5.detail.single
```

