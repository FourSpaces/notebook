![img](http://7xr8qy.com1.z0.glb.clouddn.com/avatar/537bea2bafb24259f0e72b08fcb01ce5-36)

腾讯应用加固的脱壳分析和修复

 26 July, 2015

首先这篇文章是具体参考[【原创】**应用加固的脱壳分析和修复](http://bbs.pediy.com/showthread.php?p=1353353)，上文作者在今年2月12号发了一篇文章详细分析了整个过程，由于腾讯加固的技术也不断演进，所以我在上文的基础，分析现在7月份腾讯加固采用的新方法。与上文重复的部分就不再过多说明，所以阅读本文之前，要首先看懂上文的大致思路。

### 1.反编译apk

首先，看一下原apk和加固后的文件变化情况，主要是修改了AndroidManifest.xml和classes.dex，以及新增了libmain.so和libshell.so两个文件。
然后下载最新的Apktool的源码进行编译，得到apktool-cli.jar这个文件。然后直接进行反编译，如无意外的出错了。因为腾讯加固就是利用一些Apktool的bug来阻止反编译，但是又不影响安卓程序的加载。

第一个错误，是腾讯加固时添加了两个同名的ID，attr/fasten，导致反编译时出错。由于这些ID是腾讯加固添加进去的，对于程序没有影响，所以我在Apktool的做法是直接忽略这种同名的ID。其实这个问题是Apktool的bug导致的，我这种忽略的方法是治标不治本，如果这些ID在程序中是有用的就不能这样做了。

```
Exception in thread "main" brut.androlib.AndrolibException: Multiple res specs: attr/fasten
	at brut.androlib.res.data.ResType.addResSpec(ResType.java:70)
	at brut.androlib.res.decoder.ARSCDecoder.readEntry(ARSCDecoder.java:221)
	at brut.androlib.res.decoder.ARSCDecoder.readConfig(ARSCDecoder.java:191)
	at brut.androlib.res.decoder.ARSCDecoder.readType(ARSCDecoder.java:159)
	at brut.androlib.res.decoder.ARSCDecoder.readPackage(ARSCDecoder.java:116)
	at brut.androlib.res.decoder.ARSCDecoder.readTable(ARSCDecoder.java:78)
	at brut.androlib.res.decoder.ARSCDecoder.decode(ARSCDecoder.java:47)
	at brut.androlib.res.AndrolibResources.getResPackagesFromApk(AndrolibResources.java:538)
	at brut.androlib.res.AndrolibResources.loadMainPkg(AndrolibResources.java:63)
	at brut.androlib.res.AndrolibResources.getResTable(AndrolibResources.java:55)
	at brut.androlib.Androlib.getResTable(Androlib.java:64)
	at brut.androlib.ApkDecoder.setTargetSdkVersion(ApkDecoder.java:209)
	at brut.androlib.ApkDecoder.decode(ApkDecoder.java:92)
	at brut.apktool.Main.cmdDecode(Main.java:165)
	at brut.apktool.Main.main(Main.java:81)

```

第二个错误，是由于腾讯加固修改了DexCode里面的debugInfoOff，竟然把这个位置的偏移量置成0xFFFFFFFF。这在解析dex文件是肯定会显示invalid DEX，所以看下面的提示信息就是说读取offet时out of range了，我的做法是忽略0xFFFFFFFF这种过大的偏移量。

```
org.jf.util.ExceptionWithContext: Encountered small uint that is out of range at offset 0xffb78
	at org.jf.dexlib2.dexbacked.BaseDexBuffer.readSmallUint(BaseDexBuffer.java:54)
	at org.jf.dexlib2.dexbacked.DexBackedMethodImplementation.getDebugInfo(DexBackedMethodImplementation.java:126)
	at org.jf.dexlib2.dexbacked.DexBackedMethodImplementation.getDebugItems(DexBackedMethodImplementation.java:131)
	at org.jf.baksmali.Adaptors.MethodDefinition.addDebugInfo(MethodDefinition.java:575)
	at org.jf.baksmali.Adaptors.MethodDefinition.getMethodItems(MethodDefinition.java:377)
	at org.jf.baksmali.Adaptors.MethodDefinition.writeTo(MethodDefinition.java:238)
	at org.jf.baksmali.Adaptors.ClassDefinition.writeDirectMethods(ClassDefinition.java:283)
	at org.jf.baksmali.Adaptors.ClassDefinition.writeTo(ClassDefinition.java:112)
	at org.jf.baksmali.baksmali.disassembleClass(baksmali.java:226)
	at org.jf.baksmali.baksmali.access$000(baksmali.java:56)
	at org.jf.baksmali.baksmali$1.call(baksmali.java:150)
	at org.jf.baksmali.baksmali$1.call(baksmali.java:148)
	at java.util.concurrent.FutureTask.run(FutureTask.java:262)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
	at java.lang.Thread.run(Thread.java:745)

```

第三个问题，也是由于debugInfoOff引起的，在创建debug结构体时，如果偏移量为0xFFFFFFFF，就看做偏移量为0x0。

```
java.lang.ArrayIndexOutOfBoundsException: -1
	at org.jf.dexlib2.dexbacked.BaseDexReader.readBigUleb128(BaseDexReader.java:158)
	at org.jf.dexlib2.dexbacked.util.DebugInfo$DebugInfoImpl.iterator(DebugInfo.java:104)
	at org.jf.baksmali.Adaptors.MethodDefinition.addDebugInfo(MethodDefinition.java:575)
	at org.jf.baksmali.Adaptors.MethodDefinition.getMethodItems(MethodDefinition.java:377)
	at org.jf.baksmali.Adaptors.MethodDefinition.writeTo(MethodDefinition.java:238)
	at org.jf.baksmali.Adaptors.ClassDefinition.writeDirectMethods(ClassDefinition.java:283)
	at org.jf.baksmali.Adaptors.ClassDefinition.writeTo(ClassDefinition.java:112)
	at org.jf.baksmali.baksmali.disassembleClass(baksmali.java:226)
	at org.jf.baksmali.baksmali.access$000(baksmali.java:56)
	at org.jf.baksmali.baksmali$1.call(baksmali.java:150)
	at org.jf.baksmali.baksmali$1.call(baksmali.java:148)
	at java.util.concurrent.FutureTask.run(FutureTask.java:262)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
	at java.lang.Thread.run(Thread.java:745)

org.jf.util.ExceptionWithContext: -1
	at org.jf.util.ExceptionWithContext.withContext(ExceptionWithContext.java:54)
	at org.jf.baksmali.Adaptors.MethodDefinition.(MethodDefinition.java:161)
	at org.jf.baksmali.Adaptors.ClassDefinition.writeDirectMethods(ClassDefinition.java:282)
	at org.jf.baksmali.Adaptors.ClassDefinition.writeTo(ClassDefinition.java:112)
	at org.jf.baksmali.baksmali.disassembleClass(baksmali.java:226)
	at org.jf.baksmali.baksmali.access$000(baksmali.java:56)
	at org.jf.baksmali.baksmali$1.call(baksmali.java:150)
	at org.jf.baksmali.baksmali$1.call(baksmali.java:148)
	at java.util.concurrent.FutureTask.run(FutureTask.java:262)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
	at java.lang.Thread.run(Thread.java:745)
Caused by: java.lang.ArrayIndexOutOfBoundsException: -1
	at org.jf.dexlib2.dexbacked.BaseDexReader.skipUleb128(BaseDexReader.java:191)
	at org.jf.dexlib2.dexbacked.util.DebugInfo$DebugInfoImpl.getParameterNames(DebugInfo.java:251)
	at org.jf.dexlib2.dexbacked.util.DebugInfo$DebugInfoImpl.getParameterNames(DebugInfo.java:81)
	at org.jf.dexlib2.dexbacked.DexBackedMethodImplementation.getParameterNames(DexBackedMethodImplementation.java:136)
	at org.jf.dexlib2.dexbacked.DexBackedMethod.getParameterNames(DexBackedMethod.java:153)
	at org.jf.dexlib2.dexbacked.DexBackedMethod$1.iterator(DexBackedMethod.java:131)
	at java.util.AbstractCollection.toArray(AbstractCollection.java:137)
	at com.google.common.collect.ImmutableList.copyOf(ImmutableList.java:258)
	at org.jf.baksmali.Adaptors.MethodDefinition.(MethodDefinition.java:93)
	... 10 more

```

如果大家懒得去修改Apktool源码，可以直接用我的apktool-cli.jar来进行反编译。

### 2.理解加固原理

反编译后发现，AndroidManifest.xml里面有些变动，多了一行，但是好像对这版本Apktool的反编译和编译没啥影响，所以就没有理会AndroidManifest.xml文件。

```
<serviceandroid:name="com.tencent.mm.fasten.check.log" />

```

然后明显看到新增了两个so，估计跟2月份的加固方法相差不大，这一点可以通过查看反编译后StubShell的smali代码证明。
但是有一点区别的是StubShell里面有三个smail文件ProxyShell.smali、ShellHelper.smali和TxAppEntry.smali。之前只有两个，现在多了一个TxAppEntry.smali，脱壳时要把腾讯相应的smail删除干净。
而dex文件的隐藏方法并没有变动，可以用2月份原作者写的FixTXShellDex工具来恢复隐藏数据。我这里就不详细说明了。

### 3.具体的脱壳步骤

a.把加固的apk解压，对classes.dex文件用FixTXShellDex工具进行修复，然后把修复好的classes.dex放回去apk包中。
b.使用Apktool加载apktool-cli.jar进行反编译，得到把反编译的代码中如下语句的全部替换为空：

```
invoke-static {v0, v1},Lcom/tencent/StubShell/ShellHelper;->StartShell(Ljava/lang/String;I)Z
invoke-static {p0},Lcom/tencent/StubShell/TxAppEntry;->LoadResSo(Landroid/content/Context;)V

```

而且把该com/tencent/StubShell目录下的三个smali文件删除。把lib目录下的libmain.so和libshell.so删除。
c.重新用Apktool打包APK，脱壳成功。收工。

Apktool的修改后的源码在我的[github](https://github.com/kesuki/Apktool)中。

### 4.后续更新

2015/07/30更新：竟然过了几天，腾讯又修改了一下Manifest.xml，把安卓application入口改成com.tencent.StubShell.TxAppEntry。
然后下面增加一个meta-data为TxAppEntry，保存原来的程序入口。所以把原来的入口放回application中就好了。如下：

```
<application android:debuggable="true" android:icon="@drawable/ic_launcher" android:label="@string/app_name" android:name="com.tencent.StubShell.TxAppEntry" android:theme="@style/AppTheme">
        <service android:name="com.tencent.mm.fasten.check.log"/>
        <meta-data android:name="TxAppEntry" android:value="android.app.Application"/>

```

 更多

 [加固](http://www.mak-blog.com/tag/%e5%8a%a0%e5%9b%ba)  [腾讯](http://www.mak-blog.com/tag/%e8%85%be%e8%ae%af)