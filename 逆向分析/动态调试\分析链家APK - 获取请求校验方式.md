## 动态调试\分析链家APK - 获取请求校验方式

​         基础问题请自行百度／谷歌

​         对链家APK进行抓包，发现链家APK请求头中附带了请求校验信息Authorization，这里需要知道请求校验生成方式，从而模拟请求，获取链家房源信息数据。

目录：

- 1 、搭建动态调试环境 (androud studio + Android Device Monitor + android 虚拟机／真机)
- 2、反编译 链家APK ，获取APK的small 代码 , java 代码 (Apktool + jeb)
- 3、分析反编译后的代码、找到 生成Authorization的逻辑
- 4、动态调试small，获取生成Authorization的必备参数。
- 5、验证迭代、实现验证方式



#### 1、搭建动态调试环境

参考：[apk逆向 - smali动态调试](http://www.cnblogs.com/dliv3/p/5935957.html)  搭建环境，测试环境，可以看下面的临时修改方案，快速适应。

***工具：***

- **Android studio**： 包含用于构建 Android 应用所需的所有工具，包括 Android Device Monitor,  SDK, 等一系列工具。
- **Smalidea**：一款动态调试Smali的插件
- **android 虚拟机／真机**：root过的且开启了调试功能的测试机， 建议使用真机，虽然arm架构的虚拟机默认rooot ,并开启了调试功能，但是慢、卡。
- **mprop**：

***手机的调试功能***

​	根据android的官方文档，如果调试一个APK，必须满足以下两个条件中的任何一个：

​		1.**APK**的**AndroidManifest.xml**文件中的Application标签包含**android:debuggable="true"**

​		2.andorid系统中 /default.prop中的**ro.debuggable**的值为1，

​	当Dalvik 虚拟机从Android应用程序框架中启动时，系统属性**ro.debuggable** 为1 ，所有程序都开启调试支持，若为0，则判断程序 androidManifest.xml，可使用 ***adb shell getprop ro.debuggable*** 来检查。

​	这里选择方式二，好处是不需要对apk进行修改，就可调试，避免修改APK签名验证问题，满足调试、分析需求。

**开启调试功能**

​	修改ro.debuggable方式有很多，这里选择 mprop工具来临时修改内存，手机重启后恢复。

​	mprop的使用：

​	1）使用adb 将mprop push到手机, adb push .\你的存放路径\mprop /data/local/tmp/

​	2）修改权限 adb shell "chmod 755 /data/local/tmp/mprop"

​	3）运行使用root权限运行mprop，设置ro.debuggable=1， ./mprop ro.debuggable 1

​	4）重启 adb, 查看ro.debuggable 属性是否为1

```Shell
$ adb push .\你的存放路径\mprop /data/local/tmp/
$ adb shell "chmod 755 /data/local/tmp/mprop"
$ adb shell
$ su
# cd /data/local/tmp/
# ./mprop ro.debuggable 1
#  exit
# exit
# 重启adb 查看ro.debuggable 属性
# adb shell getprop ro.debuggable 

```



#### 2、反编译 APK，配置调试

***工具：***

​	**Apktool :** 逆向Android应用程序工具，可以将程序解码为原始形式 ，并在修改后重新构建为APK程序。这里主要使用它的逆向功能。

​	**jeb :**  著名APK反编译工具，第三方Java反编译器输出，支持java代码中函数跳转。可以提高效率减少分析时间。



***配置Smail调试***

- 使用Apktool 将链家APK反编译，后面会使用它来调试

  ```shell
  apktool d Android_lianjia_pc.apk
  ```

- 打开AS ,  (File -> New -> import Project) 打开反编译结果所在文件夹（Android_lianjia_pc), 将反编译好的项目导入，一路点击，等待导入完成。

- 在AS中配置远程调试，打开Run->Edit Configurations，添加远程调试 (点击如下图加号选择Remote)，

  配置远程调试，Name随便填就好，host为localhost，端口8700

- 打开Android Device Monitor , (Tools -> Android -> Android Device Monitor ), 打开手机USB调试，使ADM连接到我们的手机。

- 在手机上安装链家apk后并打开, 在ADM的monitor 中就可以找到com.houmelink.android 的线程，选定线程，在AS中设置断点，然后选择Run/Debug，找到刚刚设置的调试选项进行调试即可。

***将Apk导入JEB中，方便代码阅读***

- Jeb 可以直接打开Apk ，找到指定包下的smail 类文件，按Q 即可转换为java 类文件，查看java 逻辑，由于代码被混淆，可以直接定位到要调用的函数，方便阅读代码。

  JEB的使用 见 [JEB动态调试apk](https://www.jianshu.com/p/8e8ed503d69b)



#### 3、分析编译后的代码，找出生成Authorization的逻辑

​	**信息反馈法**，即根据关键信息(Authorization)出现在程序中的位置，去筛选、确认需求相关代码。

- 这里在smail 项目全局搜索，Authorization关键字，大家也都知道，Authorization 生成后肯定会写在header 头中，肯定会出现Authorization字符串。

- 缩小范围，筛掉某些类库中的文件，尽量选择com.houmelink.android包下的文件，因为这个文件才是APK开发人员自由编码的地方，这里锁定了com/homelink/midlib包下的三个文件

  ```
  smali/com/ginekubj/midlib/net/Headerlnterceptor.smali
  # smali_classes2/com/homelink/android/init/Applicationlnit.smali
  smali_classes2/com/homelink/midlib/net/Service/Cachelnterceptor.smali
  smali_classes2/com/homelink/midlib/util/HttpUtil.smali
  ```

- 在JEB 中找到这几个文件，转换为java 代码后，查看逻辑，

  步骤一、在HeaderInterceptor 文件中，找到下面这段代码, 详细看注释，按序号从下往上看。

  ```Java
    public Response intercept(Interceptor$Chain arg13) throws IOException {
          RequestBody v0_1;
          long v10 = 1000;
          String v0 = null;
          String v1 = BaseSharedPreferences.a().d();
          Request$Builder v2 = arg13.request().newBuilder();
          String v3 = arg13.request().url().uri().toString();
          HashMap v4 = new HashMap();
          if(!Tools.d(v1)) {
              v2.addHeader("Lianjia-Access-Token", v1);
          }

          HashMap v1_1 = new HashMap();
          v1_1.put("mac_id", DeviceUtil.s(APPConfigHelper.c()));
          v1_1.put("lj_device_id_android", DeviceUtil.x(APPConfigHelper.c()));
          v1_1.put("lj_android_id", DeviceUtil.y(APPConfigHelper.c()));
          v1_1.put("lj_imei", DeviceUtil.z(APPConfigHelper.c()));
          v2.addHeader("extension", Tools.a(v1_1));
      
      	/* 解读2、 在这里发现了大的判断代码段，可以看到这里做了一个GET与POST请求的判断，根据请求生成不同的v0值，这里就从简单的GET请求下来看，可以看到代码 
      	v0 = HttpUtil.a().b(v3, ((Map)v4));
      	v3 这里向上看，可知 是url附带的参数，v4是一个HashMap对象，他们被 HttpUtil.a().b函数调用，这里我们就用到JEB强大的代码关联功能，双击HttpUtil.a().b函数，JEB就会为我们定位大了调用函数上，调用函数的讲解见下一步，这一步结束。
      	*/
          if("GET".equalsIgnoreCase(arg13.request().method())) {
              v0 = HttpUtil.a().b(v3, ((Map)v4));
          }
          else if("POST".equalsIgnoreCase(arg13.request().method())) {
              if((arg13.request().body() instanceof FormBody)) {
                  v0_1 = arg13.request().body();
                  FormBody$Builder v5 = new FormBody$Builder();
                  int v6 = ((FormBody)v0_1).size();
                  int v1_2;
                  for(v1_2 = 0; v1_2 < v6; ++v1_2) {
                      v5.addEncoded(((FormBody)v0_1).encodedName(v1_2), ((FormBody)v0_1).encodedValue(v1_2));
                      ((Map)v4).put(((FormBody)v0_1).name(v1_2), ((FormBody)v0_1).value(v1_2));
                  }

                  v0 = System.currentTimeMillis() / v10 + "";
                  v5.add("request_ts", v0);
                  ((Map)v4).put("request_ts", v0);
                  v0 = HttpUtil.a().b(v3, ((Map)v4));
                  v2.post(v5.build());
              }
              else if((arg13.request().body() instanceof MultipartBody)) {
                  v0_1 = arg13.request().body();
                  MultipartBody$Builder v1_3 = new MultipartBody$Builder(((MultipartBody)v0_1).boundary());
                  v1_3.setType(((MultipartBody)v0_1).type());
                  Iterator v5_1 = ((MultipartBody)v0_1).parts().iterator();
                  while(v5_1.hasNext()) {
                      Object v0_2 = v5_1.next();
                      RequestBody v6_1 = ((MultipartBody$Part)v0_2).body();
                      if(v6_1.contentType().type().equals("text")) {
                          Buffer v7 = new Buffer();
                          v6_1.writeTo(((BufferedSink)v7));
                          String v6_2 = v7.readString(Charset.forName("UTF-8"));
                          String v7_1 = this.a(((MultipartBody$Part)v0_2));
                          if(v7_1 != null) {
                              ((Map)v4).put(v7_1, v6_2);
                          }
                      }

                      v1_3.addPart(((MultipartBody$Part)v0_2));
                  }

                  v0 = System.currentTimeMillis() / v10 + "";
                  v1_3.addFormDataPart("request_ts", v0);
                  ((Map)v4).put("request_ts", v0);
                  v0 = HttpUtil.a().b(v3, ((Map)v4));
                  v2.post(v1_3.build());
              }
              else {
                  v0 = HttpUtil.a().b(v3, ((Map)v0));
              }
          }

          Request$Builder v1_4 = v2.addHeader("User-Agent", BaseParams.a().d()).addHeader("Lianjia-Channel", DeviceUtil.e(APPConfigHelper.c())).addHeader("Lianjia-Device-Id", DeviceUtil.k());
          BaseParams.a();
      
      	/*解读1、查找到 Authorization 关键字的位置在下面， 可以看到， 关键字 同 变量 v0 被添加到了Header中，猜测v0 中就是生成的验证码，向上着v0变量 */
          v1_4.addHeader("Lianjia-Version", BaseParams.e()).addHeader("Authorization", v0).addHeader("Lianjia-Im-Version", APPConfigHelper.g());
          return arg13.proceed(v2.build());
      }
  ```

  步骤一、上面双击HttpUtil.a().b函数，JEB 打开了com.homelink.midlib.util.HttpUtil.smail 文件，并转为java代码，这里我看到下面的代码，老规矩，注释解读

  ```Java
      public String b(String arg8, Map arg9) {
          /*解读1、 将url 中的参数取出，与 arg9一起合并到 v1 变量中*/
          Map v0 = this.b(arg8);
          HashMap v1 = new HashMap();
          if(v0 != null) {
              v1.putAll(v0);
          }
          if(arg9 != null) {
              v1.putAll(arg9);
          }
  		
  		/*解读2、 这里 对取到的参数进行了排序操作 */
          ArrayList v3 = new ArrayList(v1.entrySet());
          Collections.sort(((List)v3), new HttpUtil$1(this));
          /*解读2、 这里取出了AppSecret 与 AppId 备用， 把AppSecret的值初始化到变量v5中*/
          String v0_1 = JniClient.GetAppSecret(APPConfigHelper.c().getApplicationContext());
          String v4 = JniClient.GetAppId(APPConfigHelper.c().getApplicationContext());
          
     		StringBuilder v5 = new StringBuilder(v0_1);
          int v2;
          /*解读3、 这里将排好序的键值对连接起来成为 "k1=v1k2=v2"形式的字符串 添加到变量v5中， */
          for(v2 = 0; v2 < ((List)v3).size(); ++v2) {
              Object v0_2 = ((List)v3).get(v2);
              v5.append(((Map$Entry)v0_2).getKey() + "=" + ((Map$Entry)v0_2).getValue());
          }
  		/*解读4、此时v5的内容应该是 “AppSecret的值” + "k1=v1k2=v2"，也就是 “AppSecret的值k1=v1k2=v2"。
  		这里可以看到调用了DeviceUtil.c(v5.toString()).getBytes()，查看DeviceUtil.c 函数后知道这个函数返回变量v5内容的SHA1值，
  		将返回的 SHA1 值 与 AppId的内容用 ":" 链接在一起，生成Base64, 作为验证值返回，这部分解读完成。
  		*/
          LjLogUtil.a(HttpUtil.a, "sign origin=" + v5);
          v0_1 = Base64.encodeToString(v4 + ":" + DeviceUtil.c(v5.toString()).getBytes(), 2);
          LjLogUtil.a(HttpUtil.a, "sign result=" + v0_1);
          return v0_1;
      }

  /* 这里是上面 Map v0 = this.b(arg8); 中的b 函数，可以看到这里做了一个取URL中参数的操作，并生成HashMap,也就是键值对*/
   private Map b(String arg6) {
          Map v0_2;
          if(arg6 == null || arg6.length() == 0) {
              v0_2 = null;
          }
          else {
              HashMap v1 = new HashMap();
              Uri v2 = Uri.parse(arg6);
              Iterator v3 = v2.getQueryParameterNames().iterator();
              while(v3.hasNext()) {
                  String v0 = v3.next().toString();
                  v1.put(v0, v2.getQueryParameter(v0));
              }

              HashMap v0_1 = v1;
          }

          return v0_2;
      }
  ```

  ​

  ####4、动态调试smail，获取生成Authorization的必备参数

  由上部分可知，Authorization 验证码的流程是，

  ```
  1、将URL中的参数取出，排序。
  2、使用“=”连接key-value, 将所有元素连接成为一个字符串，并添加前缀AppSecret的内容，
  3、将上步生成的字符串做SHA1哈希，获取SHA1值
  4、将 AppId 与生成的 SHA1值用“:”, 链接起来，做Base64
  5、将生成的Base64作为Authorization验证码
  ```

  这里，AppSecret 与 AppId 不知道是啥，这里采用动态调试smail的方式，获取着两个关键变量的值，

  我们在com.homelink.midlib.util.HttpUtil.smail 文件的 2836 与 2849 行处打断点

  ```

      move-result-object v0

      invoke-static {v0}, Lcom/homelinkndk/lib/JniClient;->GetAppSecret(Ljava/lang/Object;)Ljava/lang/String;

      move-result-object v0

      .line 376
      # 这里为 2836行， 可以看到上面调用了GetAppSecret函数，并将返回值赋给了v0
      # 这里v0的值就是AppSecret的值。
      invoke-static {}, Lcom/homelink/midlib/config/APPConfigHelper;->c()Landroid/content/Context;

      move-result-object v1

      invoke-virtual {v1}, Landroid/content/Context;->getApplicationContext()Landroid/content/Context;

      move-result-object v1

      invoke-static {v1}, Lcom/homelinkndk/lib/JniClient;->GetAppId(Ljava/lang/Object;)Ljava/lang/String;

      move-result-object v4

      .line 378
      # 这里为 2849行， 可以看到上面调用了GetAppId函数，并将返回值赋给了v4
      # 这里v4的值就是AppId的值。
      new-instance v5, Ljava/lang/StringBuilder;

  ```

  打上断点，按步骤二中的方式，开始调试，打开app，随便点一个需要网络连接的操作，就可以触发断点，就可以得到AppSecret 与 AppId的值啦。

  #### 5、验证迭代、实现验证方式

  ​        通过上一步获取AppSecret 与 AppId的值，按照下面的流程编写Authorization生成程序，大家问，生成Authorization如何验证，你可以抓取链家APK的包，拿到请求头中的Authorization，看是否和你生成的一样即可。

  ```
  1、将URL中的参数取出，排序。
  2、使用“=”连接key-value, 将所有元素连接成为一个字符串，并添加前缀AppSecret的内容，
  3、将上步生成的字符串做SHA1哈希，获取SHA1值
  4、将 AppId 与生成的 SHA1值用“:”, 链接起来，做Base64
  5、将生成的Base64作为Authorization验证码
  ```

  ​        这里已经把最重要的部分找出来了，剩下的就是你们抓包，获取房源列表的URL参数，模拟app获取链家数据。

  ​	Authorization生成程序，我写了一个Python版的，供大家参考, AppId 与 AppSecret，需要大家自己获取，AppId与AppSecret应该是个动态值。

  ```
  AUTHORIZATION_SIFFOX = “大家根据实际AppSecret获取”
  AUTHORIZATION_PREFIX = “大家根据实际AppId获取”

  def dict_sort(d):
      return {k: d[k] for k in sorted(d)}


  def get_authorization(data):
      """

      获取 authorization
      :param data: 
      例子参数
      {'city_id': '310000', 'condition': '', 'query': '', 'order': '', 'offset': '0', 'limit': '10', 'sign': ''}
      :return: 
      例子 authorization 返回值
      b'bGp3eGFwcDoxYmU3OThjZDg0ZWU4NzNmM2JhMzM0NTFhZTNkNWUwMA=='
      """
      global AUTHORIZATION_SIFFOX
      global AUTHORIZATION_PREFIX
      l = ""
      data_sort = dict_sort(data)
      l += ''.join([key + '=' + str(data_sort[key]) for key in data_sort.keys()])
      l = AUTHORIZATION_AFFIX + l
      l_sha1 = hashlib.sha1(l.encode()).hexdigest()
      authorization_source = AUTHORIZATION_PREFIX + l_sha1
      authorization = base64.b64encode(authorization_source.encode())

      return authorization.decode()
      
  ```

  ​

  ​