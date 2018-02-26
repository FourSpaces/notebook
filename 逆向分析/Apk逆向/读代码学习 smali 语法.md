# 读代码学习 smali 语法

### smali 代码

``` Smali
## 基本信息
#.class <访问权限> <类名>
#.super <父类名>
#.source <源文件名>
.class public Lcom/example/weicheng/myapp/MainActivity;
.super Landroid/support/v7/app/AppCompatActivity;
.source "MainActivity.java"

## 类变量声明
#.field <访问权限> <变量名>:<变量类型>
# 局部变量声明：
#.local <初始值>,<变量名>:<变量类型>
# instance fields
.field btn_register:Landroid/widget/Button;
.field edit_sn:Landroid/widget/EditText;
.field edit_userName:Landroid/widget/EditText;

## 类方法声明
#.method <访问权限> <方法名>(参数原型) <方法原型>
#    [.prologue]    // 指定代码开始位置
#    [.param]       // 指定方法参数
#    [.line]        // 指定代码在源代码中的行数，混淆后可能不存在
#    [.locals]  // 使用的局部变量个数
#    <代码体>
#.end method
# direct methods
.method public constructor <init>()V
    .locals 0

    .prologue
    .line 14
    invoke-direct {p0}, Landroid/support/v7/app/AppCompatActivity;-><init>()V

    return-void
.end method



.method static synthetic access$000(Lcom/example/weicheng/myapp/MainActivity;Ljava/lang/String;Ljava/lang/String;)Z
    .locals 1
    .param p0, "x0"    # Lcom/example/weicheng/myapp/MainActivity;
    .param p1, "x1"    # Ljava/lang/String;
    .param p2, "x2"    # Ljava/lang/String;

    .prologue
    .line 14
    invoke-direct {p0, p1, p2}, Lcom/example/weicheng/myapp/MainActivity;->checkSN(Ljava/lang/String;Ljava/lang/String;)Z

    move-result v0

    return v0
.end method

.method public static byteArrayToStr([B)Ljava/lang/String;
    .locals 1
    .param p0, "byteArray"    # [B

    .prologue
    .line 75
    if-nez p0, :cond_0

    .line 76
    const/4 v0, 0x0

    .line 79
    :goto_0
    return-object v0

    .line 78
    :cond_0
    new-instance v0, Ljava/lang/String;

    invoke-direct {v0, p0}, Ljava/lang/String;-><init>([B)V

    .line 79
    .local v0, "str":Ljava/lang/String;
    goto :goto_0
.end method

.method private checkSN(Ljava/lang/String;Ljava/lang/String;)Z
    .locals 10
    .param p1, "userName"    # Ljava/lang/String;
    .param p2, "sn"    # Ljava/lang/String;

    .prologue
    const/4 v9, 0x0

    .line 49
    if-eqz p1, :cond_0

    :try_start_0
    invoke-virtual {p1}, Ljava/lang/String;->length()I

    move-result v7

    if-nez v7, :cond_1

    .line 71
    :cond_0
    :goto_0
    return v9

    .line 51
    :cond_1
    if-eqz p2, :cond_0

    invoke-virtual {p2}, Ljava/lang/String;->length()I

    move-result v7

    const/16 v8, 0x10

    if-ne v7, v8, :cond_0

    .line 54
    const-string/jumbo v7, "MD5"

    invoke-static {v7}, Ljava/security/MessageDigest;->getInstance(Ljava/lang/String;)Ljava/security/MessageDigest;

    move-result-object v1

    .line 55
    .local v1, "digest":Ljava/security/MessageDigest;
    invoke-virtual {v1}, Ljava/security/MessageDigest;->reset()V

    .line 56
    invoke-virtual {p1}, Ljava/lang/String;->getBytes()[B

    move-result-object v7

    invoke-virtual {v1, v7}, Ljava/security/MessageDigest;->update([B)V

    .line 57
    invoke-virtual {v1}, Ljava/security/MessageDigest;->digest()[B

    move-result-object v0

    .line 58
    .local v0, "bytes":[B
    invoke-static {v0}, Lcom/example/weicheng/myapp/MainActivity;->byteArrayToStr([B)Ljava/lang/String;

    move-result-object v3

    .line 59
    .local v3, "hexstr":Ljava/lang/String;
    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    .line 60
    .local v5, "sb":Ljava/lang/StringBuilder;
    const/4 v4, 0x0

    .local v4, "i":I
    :goto_1
    invoke-virtual {v3}, Ljava/lang/String;->length()I

    move-result v7

    if-ge v4, v7, :cond_2

    .line 61
    invoke-virtual {v3, v4}, Ljava/lang/String;->charAt(I)C

    move-result v7

    invoke-virtual {v5, v7}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;

    .line 60
    add-int/lit8 v4, v4, 0x2

    goto :goto_1

    .line 63
    :cond_2
    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    .line 64
    .local v6, "userSN":Ljava/lang/String;
    invoke-virtual {v6, p2}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z
    :try_end_0
    .catch Ljava/security/NoSuchAlgorithmException; {:try_start_0 .. :try_end_0} :catch_0

    move-result v7

    if-nez v7, :cond_0

    goto :goto_0

    .line 67
    .end local v0    # "bytes":[B
    .end local v1    # "digest":Ljava/security/MessageDigest;
    .end local v3    # "hexstr":Ljava/lang/String;
    .end local v4    # "i":I
    .end local v5    # "sb":Ljava/lang/StringBuilder;
    .end local v6    # "userSN":Ljava/lang/String;
    :catch_0
    move-exception v2

    .line 68
    .local v2, "e":Ljava/security/NoSuchAlgorithmException;
    invoke-virtual {v2}, Ljava/security/NoSuchAlgorithmException;->printStackTrace()V

    goto :goto_0
.end method

## 传入的参数寄存器由p表示，而函数内的本地寄存器则由v表示，多个的话则在后面加上0,1,2…
## 需要注意的是，在非static函数中，p0表示`this`，p1才表示第一个参数。

## 常量赋值
#主要是各种const
#const                   v0, 0x7F030018  # R.layout.activity_challenge   #从R中取出静态值
#const/4                 v3, 0x2   #4也可以换成16或者high16，表示取整数值
#const-string            v2, "Challenge"  # 取字符串
#const-class             v2, Context    #把类对象取出
# virtual methods
.method protected onCreate(Landroid/os/Bundle;)V
    .locals 2
    .param p1, "savedInstanceState"    # Landroid/os/Bundle;

    .prologue
    .line 22
    invoke-super {p0, p1}, Landroid/support/v7/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    .line 23
    const v0, 0x7f09001b

    invoke-virtual {p0, v0}, Lcom/example/weicheng/myapp/MainActivity;->setContentView(I)V

    .line 24
    const v0, 0x7f0b0022

    invoke-virtual {p0, v0}, Lcom/example/weicheng/myapp/MainActivity;->setTitle(I)V

    .line 25
    const v0, 0x7f070083

    invoke-virtual {p0, v0}, Lcom/example/weicheng/myapp/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/EditText;

    iput-object v0, p0, Lcom/example/weicheng/myapp/MainActivity;->edit_userName:Landroid/widget/EditText;

    .line 26
    const v0, 0x7f070067

    invoke-virtual {p0, v0}, Lcom/example/weicheng/myapp/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/EditText;

    iput-object v0, p0, Lcom/example/weicheng/myapp/MainActivity;->edit_sn:Landroid/widget/EditText;

    .line 27
    const v0, 0x7f070051

    invoke-virtual {p0, v0}, Lcom/example/weicheng/myapp/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/Button;

    iput-object v0, p0, Lcom/example/weicheng/myapp/MainActivity;->btn_register:Landroid/widget/Button;

    .line 29
    iget-object v0, p0, Lcom/example/weicheng/myapp/MainActivity;->btn_register:Landroid/widget/Button;

    new-instance v1, Lcom/example/weicheng/myapp/MainActivity$1;

    invoke-direct {v1, p0}, Lcom/example/weicheng/myapp/MainActivity$1;-><init>(Lcom/example/weicheng/myapp/MainActivity;)V

    invoke-virtual {v0, v1}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    .line 45
    return-void
.end method

```





**0x01 smali生成**

使用apktool反编译apk后，会在反编译工程目录下生成一个smali文件夹![spacer.gif](https://p1.ssl.qhimg.com/t01a42eb0d8e6abd673.gif)

![http://p5.qhimg.com/t019b1faf9711fa7c27.png](https://p0.ssl.qhimg.com/t018f5080304e67ed09.png)

其中android下存放所调用库的smali文件，com才是我们自己写的代码的smali文件。

**0x02 基础语法**

**a.文件基本格式**

基本信息

```
.class <访问权限> <类名>
.super <父类名>
.source <源文件名>
# eg.
.class
 public Lcom/reoky/crackme/challengeone/activities/ChallengeActivity;    
                                                                       
.super
 Landroid/support/v4/app/FragmentActivity;                              
                                                                        
.source "ChallengeActivity.java"  //经过混淆后这项可能为空
```

类变量声明

```
.field <访问权限> <变量名>:<变量类型>
# eg.
.field actionBar:Landroid/app/ActionBar; <=对应源码=> ActionBar actionBar;
局部变量声明：
.local <初始值>,<变量名>:<变量类型>
#eg
.local v0, "ans":Ljava/lang/String; <=对应源码=> String ans="";
```

类方法声明

```
.method <访问权限> <方法名>(参数原型) <方法原型>
    [.prologue]    // 指定代码开始位置
    [.param]       // 指定方法参数
    [.line]        // 指定代码在源代码中的行数，混淆后可能不存在
    [.locals]  // 使用的局部变量个数
    <代码体>
.end method
# eg
.method public onTabReselected(Landroid/app/ActionBar$Tab;Landroid/app/FragmentTransaction;)V 
    .locals 0
    .param p1, "tab"    # Landroid/app/ActionBar$Tab; 
    .param p2, "fragmentTransaction"    # Landroid/app/FragmentTransaction;   
    .prologue 
    .line 55     //可能经过混淆后不存在
    return-void
.end method 
<=对应源码=>
public void onTabReselected(ActionBar$Tab tab, FragmentTransaction fragmentTransaction){
}
```

**b.原始类型**

****

```
B—byte
C—char
D—double
F—float
I—int
J—long
S—short
V—void
Z—boolean
[XXX—array
Lpackage/name/ObjName—object  // 前面表示对象所在包路径
```

**c.寄存器操作**

传入的参数寄存器由p表示，而函数内的本地寄存器则由v表示，多个的话则在后面加上0,1,2…

需要注意的是，在非static函数中，p0表示`this`，p1才表示第一个参数。

常量赋值

```
主要是各种const
const                   v0, 0x7F030018  # R.layout.activity_challenge   #从R中取出静态值
const/4                 v3, 0x2   #4也可以换成16或者high16，表示取整数值
const-string            v2, "Challenge"  # 取字符串
const-class             v2, Context    #把类对象取出
```

变量间赋值

```
move  vx,vy   # 将vy的值赋值给vx，也可以是move-object等
move-result vx  # 将上个方法调用后的结果赋值给vx，也可以是move-result-object
return-object vx # 将vx的对象作为函数返回值
new-instance            v0, ChallengePagerAdapter  # 实例化一个对象存入v0中
```

对象赋值

```
iput-object             a,(this),b   将a的值给b，一般用于b的初始化
iget-object             a,(this),b   将b的值给a，一般用于获取b的地址，接着调用它
# eg.
iput-object             v0, p0, ChallengeActivity->actionBar:ActionBar
iget-object             v0, p0, ChallengeActivity->actionBar:ActionBar
```

**d.函数操作**

最基础的函数操作一般有以下四个：

```
1.private：invoke-direct
2.public|protected： invoke-virtual
3.static：invoke-static
4.parent:  invoke-super
基本调用形式：invoke-xxx {参数},类;->函数(参数原型)
# eg.
invoke-super {p0, p1}, Landroid/support/v4/app/FragmentActivity;->onCreate(Landroid/os/Bundle;)V
<=对应源码=>
super.onCreate(savedInstanceState);  // 其中p0是this，其父类是FragmentActivity，p1,是savedInstanceState，其原型是Bundle；即调用p0->onCreate(p1)
```

**0x03 程序语句相关语法**

这里列举以下常见程序语句对应的smali语句，并与Android源码相比较分析

**a.判断语句**

****

```
if-eq vA, vB, :cond_X   如果vA等于vB则跳转到:cond_X
if-ne vA, vB, :cond_X   如果vA不等于vB则跳转到:cond_X
if-lt vA, vB, :cond_X   如果vA小于vB则跳转到:cond_X
if-ge vA, vB, :cond_X   如果vA大于等于vB则跳转到:cond_X
if-gt vA, vB, :cond_X   如果vA大于vB则跳转到:cond_X
if-le vA, vB, :cond_X   如果vA小于等于vB则跳转到:cond_X
if-eqz vA, :cond_X      如果vA等于0则跳转到:cond_X
if-nez vA, :cond_X      如果vA不等于0则跳转到:cond_X
if-ltz vA, :cond_X      如果vA小于0则跳转到:cond_X
if-gez vA, :cond_X      如果vA大于等于0则跳转到:cond_X
if-gtz vA, :cond_X      如果vA大于0则跳转到:cond_X
if-lez vA, :cond_X      如果vA小于等于0则跳转到:cond_X
```

**b.循环语句******

下面列出一个简单的for循环，其他也差不多

```
public void encrypt(String str) {
    String ans = "";
    for (int i = 0 ; i < str.length();i++){
        ans += str.charAt(i);
    }
    Log.e("ans:",ans);
}
<=对应smali=>
# public void encrypt(String str) {
.method public encrypt(Ljava/lang/String;)V 
.locals 4 
.param p1, "str"# Ljava/lang/String;
.prologue 
# String ans = "";
const-string v0, "" 
.local v0, "ans":Ljava/lang/String; 
# for (int i  0 ; i < str.length();i++){
# int i=0 =>v1
const/4 v1, 0x0
.local v1, "i":I
:goto_0# for_start_place
# str.length()=>v2
invoke-virtual {p1}, Ljava/lang/String;->length()I
move-result v2 
# i<str.length() 
if-ge v1, v2, :cond_0 
# ans += str.charAt(i); 
# str.charAt(i) => v2
new-instance v2, Ljava/lang/StringBuilder; 
invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V
invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
move-result-object v2 
#str.charAt(i) => v3
invoke-virtual {p1, v1}, Ljava/lang/String;->charAt(I)C 
move-result v3
# ans += v3 =>v0
invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder; 
move-result-object v2 
invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
move-result-object v0
# i++
add-int/lit8 v1, v1, 0x1
goto :goto_0
# Log.e("ans:",ans);
:cond_0
const-string v2, "ans:" 
invoke-static {v2, v0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I
return-void 
.end method
```

**c.switch语句**

```
public void encrypt(int flag) {
        String ans = null;
        switch (flag){
            case 0:
                ans = "ans is 0";
                break;
            default:
                ans = "noans";
                break;
        }
        Log.v("ans:",ans);
    }
<=对应smali=>
#public void encrypt(int flag) {
.method public encrypt(I)V 
    .locals 2
    .param p1, "flag"    # I
    .prologue
#String ans = null;
    const/4 v0, 0x0
    .local v0, "ans":Ljava/lang/String;
#switch (flag){
    packed-switch p1, :pswitch_data_0 # pswitch_data_0指定case区域的开头及结尾
#default: ans="noans"
    const-string v0, "noans"
#Log.v("ans:",ans)
    :goto_0
    const-string v1, "ans:"
    invoke-static {v1, v0}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I
    return-void
#case 0: ans="ans is 0"
    :pswitch_0      #pswitch_<case的值>
    const-string v0, "ans is 0"
    goto :goto_0  # break
    nop
    :pswitch_data_0 #case区域的结束
    .packed-switch 0x0   #定义case的情况
        :pswitch_0   #case 0
    .end packed-switch
.end method
```

​    其中case定义情况有两种：

```
1.从0开始递增
packed-switch p1, :pswitch_data_0
...
:pswitch_data_0
.packed-switch 0x0
    :pswitch_0
    :pswitch_1 
2.无规则switch
sparse-switch p1,:sswitch_data_0
...
sswitch_data_0
.sparse-switch
    0xa -> : sswitch_0
    0xb -> : sswitch_1 # 字符会转化成数组
```

**d.try-catch语句**

****

```
public void encrypt(int flag) {
    String ans = null;
    try {
        ans = "ok!";
    } catch (Exception e){
        ans = e.toString();
    }
    Log.d("error",ans);
}
<=对应smali=>
#public void encrypt(int flag) {
.method public encrypt(I)V
    .locals 3
    .param p1, "flag"    # I
    .prologue
#String ans = null;
    const/4 v0, 0x0
    .line 20
    .local v0, "ans":Ljava/lang/String;
#try { ans="ok!"; }
    :try_start_0  # 第一个try开始，
    const-string v0, "ok!"
    :try_end_0   # 第一个try结束(主要是可能有多个try)
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0
#Log.d("error",ans);
    :goto_0
    const-string v2, "error"
    invoke-static {v2, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I
    return-void
#catch (Exception e){ans = e.toString();}
    :catch_0 #第一个catch
    move-exception v1
    .local v1, "e":Ljava/lang/Exception;
    invoke-virtual {v1}, Ljava/lang/Exception;->toString()Ljava/lang/String;
    move-result-object v0
    goto :goto_0
.end method
```

**0x04 参考资料**

<http://blog.csdn.net/qq_24349189/article/details/52300419>

<http://lib.csdn.net/article/android/7043>

<http://devxeo.lofter.com/post/2da37d_cd7c69>

http://www.blogjava.net/midea0978/archive/2012/01/04/367847.html