橙光APP 分析

```
07-05 18:30:01.402 915-935/? I/ActivityManager: Process com.mediatek.mtklogger (pid 15618) has died
07-05 18:30:01.403 915-935/? W/ContextImpl: Calling a method in the system process without a qualified user: android.app.ContextImpl.sendBroadcast:1539 com.android.server.am.OppoExtraActivityManagerService.setKeyLockModeNormal:47 com.android.server.am.ActivityManagerService.appDiedLocked:6423 com.android.server.am.ActivityManagerService$AppDeathRecipient.binderDied:1449 android.os.BinderProxy.sendDeathNotice:559 
07-05 18:30:01.403 915-935/? D/ActivityManager: SVC-handleAppDiedLocked: app = ProcessRecord{92b1483 15618:com.mediatek.mtklogger/u0a50}, app.pid = 15618
07-05 18:30:01.482 915-957/? I/ActivityManager: START u0 {act=android.intent.action.VIEW cat=[android.intent.category.BROWSABLE] dat=oplayer://org/wakeapp?action=GAMEDETAIL&gName=官居几品&gIndex=194818 flg=0x10000000 cmp=main.opalyer/.SplashActivity (has extras)} from uid 10063 from pid 25352 on display 0
07-05 18:30:01.483 23117-6009/? I/SafeCenter.AppProtectService: activityStarting() intent: Intent { act=android.intent.action.VIEW cat=[android.intent.category.BROWSABLE] dat=oplayer://org/wakeapp?action=GAMEDETAIL&gName=官居几品&gIndex=194818 flg=0x10000000 cmp=main.opalyer/.SplashActivity (has extras) }
07-05 18:30:01.492 915-957/? D/ActivityManager: insertTaskAtTop:adjust mOnTopOfHome of the task:TaskRecord{27e9d600 #3 A=com.android.settings U=0 sz=3}, oldOnTopOfHomeValue:1, insert task:TaskRecord{1c44e39 #54 A=main.opalyer U=0 sz=3}
07-05 18:30:01.521 915-957/? V/WindowManager: addAppToken: AppWindowToken{216522c token=Token{168075df ActivityRecord{980dc7e u0 main.opalyer/.SplashActivity t54}}} to stack=1 task=54 at 3
07-05 18:30:01.533 915-2194/? V/WindowManager: Changing focus from Window{3cf627c6 u0 com.android.browser/com.android.browser.BrowserActivity EXITING} to Window{7a6ba96 u0 com.android.browser/com.android.browser.BrowserActivity} Callers=com.android.server.wm.WindowManagerService.removeWindowLocked:3267 com.android.server.wm.WindowManagerService.removeWindow:3203 com.android.server.wm.Session.remove:203 android.view.IWindowSession$Stub.onTransact:233 
07-05 18:30:01.535 915-952/? I/WindowManager: Gaining focus: Window{7a6ba96 u0 com.android.browser/com.android.browser.BrowserActivity}
07-05 18:30:01.535 915-952/? I/WindowManager: Losing focus: Window{3cf627c6 u0 com.android.browser/com.android.browser.BrowserActivity EXITING}
07-05 18:30:01.551 915-2170/? I/ActivityManager: Process com.coloros.gesture (pid 15653) has died
```





## scheme 协议

```
oplayer://org/wakeapp?action=GAMEDETAIL&gName=官居几品&gIndex=194818
```





### 获取全部分类

```
curl -H 'Cache-Control: max-age=1296000' -H 'User-Agent: Mozilla/5.0 (Linux; Android 5.1; OPPO A59s Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36' -H 'x-env: ' -H 'x-ts: 1531103632' -H 'x-sign: c8a57277d99f555c1e6d38fe3b1a67a7' -H 'x-skey: 77ff70ec8c53b6d057549714d4052f8c' -H 'Host: iapi.66rpg.com' --compressed 'http://iapi.66rpg.com/game/v2/channel/get_channel_summary?pack_name=main.opalyer&nt=wifi&token=276185ff2750c781099e34424a5e71e9&device_code=OPPOA59s&android_cur_ver=2.14.237.0702&skey=77ff70ec8c53b6d057549714d4052f8c&channel=wandoujia&sv=A59s_11_A.12_180302'
```



