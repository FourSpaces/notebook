# Android逆向之smali语法宝典

![96](https://upload.jianshu.io/users/upload_avatars/1293861/55de45708cd6.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96)

 

[风澈vio](https://www.jianshu.com/u/2266aec7eb44)

 

**关注

2017.03.18 23:18* 字数 1307 阅读 2090评论 6喜欢 93

#### 前言

Android采用的是java语言进行开发，但是Android系统有自己的虚拟机Dalvik,代码编译最终不是采用的java的class，而是使用的smali。我们反编译得到的代码，jar的话可能很多地方无法正确的解释出来，如果我们反编译的是smali则可以正确的理解程序的意思。因此，我们有必要熟悉smali语法。

#### 关键字

.field private isFlag:z　---　定义变量
.method　---　方法
.parameter　---　方法参数
.prologue　---　方法开始
.line 12　---　此方法位于第12行
invoke-super　---　调用父函数
const/high16 v0, 0x7fo3　---　把0x7fo3赋值给v0
invoke-direct　---　调用函数
return-void　---　函数返回void
.end method　---　函数结束
new-instance　---　创建实例
iput-object　---　对象赋值
iget-object　---　调用对象
invoke-static　---　调用静态函数

#### 数据类型

java里面包含两种数据类型，基本数据类型和引用类型(包括对象)，同时映射到smali也是有这两大类型。

**基本数据类型**

- B　---　byte
- C　---　char
- D　---　double (64 bits)
- F　---　float
- I　---　int
- J　---　long (64 bits)
- S　---　short
- V　---　void　　　　只能用于返回值类型
- Z　---　boolean

**对象类型**

- Lxxx/yyy/zzz;　---　object

> `L`表示这是一个对象类型
> `xxx/yyy`是该对象所在的包
> `zzz`是对象名称
> `;`标识对象名称的结束

**数组类型**

- [XXX　---　array

> `[I`表示一个int型的一维数组，相当于`int[]`
> 增加一个维度增加一个`[`，如`[[I`表示`int[][]`
> 数组每一个维度最多255个;
> 对象数组表示也是类似，如String数组的表示是`[Ljava/lang/String`

#### 寄存器与变量

java中变量都是存放在内存中的，android为了提高性能，变量都是存放在寄存器中的，寄存器为32位，可以支持任何类型，其中long和double是64为的，需要使用两个寄存器保存。
寄存器采用v和p来命名
v表示本地寄存器，p表示参数寄存器，关系如下
如果一个方法有两个本地变量，有三个参数

> `v0`第一个本地寄存器
> `v1`第二个本地寄存器
> `v2 p0`(this)
> `v3 p1`第一个参数
> `v4 p2`第二个参数
> `v5 p3`第三个参数

当然，如果是静态方法的话就只有5个寄存器了，不需要存this了。
`.registers`使用这个指令指定方法中寄存器的总数
`.locals`使用这个指定表明方法中非参寄存器的总数，放在方法的第一行。

#### 方法和字段

**方法签名**
methodName(III)Lpackage/name/ObjectName;
如果做过ndk开发的对于这样的签名应该很熟悉的，就是这样来标识一个方法的。上面methodName标识方法名，III表示三个整形参数，Lpackage/name/ObjectName;表示返回值的类型。

**方法的表示**
Lpackage/name/ObjectName;——>methodName(III)Z
即 package.name.ObjectName中的 function boolean methondName(int a, int b, int c) 类似这样子

**字段的表示**
Lpackage/name/ObjectName;——>FieldName:Ljava/lang/String;
即表示： 包名，字段名和各字段类型

**方法的定义**
比如下面的一个方法

```
private static int sum(int a, int b) {
        return a+b;
}

```

使用编译后是这样

```
.method private static sum(II)I
    .locals 4   #表示需要申请4个本地寄存器
    .parameter
    .parameter #这里表示有两个参数
    .prologue
    .line 27 
    move v0, p0
    .local v0, a:I
    move v1, p1
    .local v1, b:I
    move v2, v0
    move v3, v1
    add-int/2addr v2, v3
    move v0, v2
    .end local v0           #a:I
    return v0
.end method

```

从上面可以看到函数声明使用.method开始 .end method结束，java中的关键词private,static 等都可以使用，同时使用签名来表示唯一的方法，这里是sum(II)I。

**声明成员**
.field private name:Lpackage/name/ObjectName;
比如：private TextView mTextView;表示就是
.field private mTextView:Landroid/widget/TextView;
private int mCount;
.field private mCount:I

#### 指令执行

smali字节码是类似于汇编的，如果你有汇编基础，理解起来是非常容易的。
比如：
move v0, v3 #把v3寄存器的值移动到寄存器v0上.
const v0， 0x1 #把值0x1赋值到寄存器v0上。
invoke-static {v4, v5}, Lme/isming/myapplication/MainActivity;->sum(II)I #执行方法sum(),v4,v5的值分别作为sum的参数。

#### 条件跳转分支

"if-eq vA, vB, :cond_x"　---　如果vA等于vB则跳转到:cond_x
"if-ne vA, vB, :cond_x"　---　如果vA不等于vB则跳转到:cond_x
"if-lt vA, vB, :cond_x"　---　如果vA小于vB则跳转到:cond_x
"if-ge vA, vB, :cond_x"　---　如果vA大于等于vB则跳转到:cond_x
"if-gt vA, vB, :cond_x"　---　如果vA大于vB则跳转到:cond_x
"if-le vA, vB, :cond_x"　---　如果vA小于等于vB则跳转到:cond_x
"if-eqz vA, :cond_x"　---　如果vA等于0则跳转到:cond_x
"if-nez vA, :cond_x"　---　如果vA不等于0则跳转到:cond_x
"if-ltz vA, :cond_x"　---　如果vA小于0则跳转到:cond_x
"if-gez vA, :cond_x"　---　如果vA大于等于0则跳转到:cond_x
"if-gtz vA, :cond_x"　---　如果vA大于0则跳转到:cond_x
"if-lez vA, :cond_x"　---　如果vA小于等于0则跳转到:cond_x





# Smali语法

![96](https://cdn2.jianshu.io/assets/default_avatar/2-9636b13945b9ccf345bc98d0d81074eb.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96)

 

[Pich](https://www.jianshu.com/u/2cb78e578e43)

 

**关注

2016.07.22 19:09* 字数 2582 阅读 4224评论 3喜欢 11赞赏 1

------

title: Smali语法
date: 2016-07-17 11:23:12
categories: Dalvik
tags:
\- Dalvik
\- Android
\- Smali

------

# 数据类型

Dalvik字节码只有两种格式：基本类型和引用类型。对象和数组属于引用类型

| 语法   | 含义            |
| ---- | ------------- |
| V    | void，只用于返回值类型 |
| Z    | boolean       |
| B    | byte          |
| S    | short         |
| C    | char          |
| I    | int           |
| J    | long          |
| F    | flot          |
| D    | double        |
| L    | Java类 类型      |
| [    | 数组类型          |

Ljava/lang/String; 相当于java.lang.String
[I 相当于一维int数组，int[]
[[I 相当于int[][]

# 方法

它使用方法名，参数类型和返回值来描述一个方法
package/name/ObjectName;->methodName(III)Z

package/name/ObjectName:一个类
methodName：方法名
III：参数类型
Z：返回值

(III)Z：方法签名

BakSmali生成的方法代码以.method指令开始，以.end method指令结束，根据方法的类型不同，可以会在方法前加#表示方法类型

\# vitual methods:虚方法，如：

```
# virtual methods
.method public get(Ljava/lang/String;)Lcn/woblog/markdowndiary/domain/Note;
    .locals 2
    .param p1, "noteId"    # Ljava/lang/String;

    .prologue
    .line 50
    iget-object v0, p0, Lcn/woblog/markdowndiary/repository/LocalNoteRepository;->orm:Lcom/litesuits/orm/LiteOrm;

    const-class v1, Lcn/woblog/markdowndiary/domain/Note;

    invoke-virtual {v0, p1, v1}, Lcom/litesuits/orm/LiteOrm;->queryById(Ljava/lang/String;Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcn/woblog/markdowndiary/domain/Note;

    return-object v0
.end method

```

\# direct methods:直接方法，如：

```
# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .locals 2
    .param p1, "context"    # Landroid/content/Context;

    .prologue
    .line 22
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    .line 23
    iput-object p1, p0, Lcn/woblog/markdowndiary/repository/LocalNoteRepository;->context:Landroid/content/Context;

    .line 24
    const-string v0, "note.db"

    invoke-static {p1, v0}, Lcom/litesuits/orm/LiteOrm;->newSingleInstance(Landroid/content/Context;Ljava/lang/String;)Lcom/litesuits/orm/LiteOrm;

    move-result-object v0

    iput-object v0, p0, Lcn/woblog/markdowndiary/repository/LocalNoteRepository;->orm:Lcom/litesuits/orm/LiteOrm;

    .line 25
    iget-object v0, p0, Lcn/woblog/markdowndiary/repository/LocalNoteRepository;->orm:Lcom/litesuits/orm/LiteOrm;

    const/4 v1, 0x1

    invoke-virtual {v0, v1}, Lcom/litesuits/orm/LiteOrm;->setDebugged(Z)V

    .line 26
    return-void
.end method

```

有些方法没有这样的注释

```
.method public save(Lcn/woblog/markdowndiary/domain/Note;)V
    .locals 1
    .param p1, "note"    # Lcn/woblog/markdowndiary/domain/Note;

    .prologue
    .line 37
    iget-object v0, p0, Lcn/woblog/markdowndiary/repository/LocalNoteRepository;->orm:Lcom/litesuits/orm/LiteOrm;

    invoke-virtual {v0, p1}, Lcom/litesuits/orm/LiteOrm;->save(Ljava/lang/Object;)J

    .line 38
    return-void
.end method

```

静态方法：

```
.method public static formatTime(J)Ljava/lang/String;
    .locals 4
    .param p0, "date"    # J

    .prologue
    .line 11
    new-instance v0, Ljava/text/SimpleDateFormat;

    const-string v1, "yyyy\u5e74MM\u6708dd\u65e5 EEEE"

    sget-object v2, Ljava/util/Locale;->CHINESE:Ljava/util/Locale;

    invoke-direct {v0, v1, v2}, Ljava/text/SimpleDateFormat;-><init>(Ljava/lang/String;Ljava/util/Locale;)V

    .line 13
    .local v0, "simpleDateFormat":Ljava/text/SimpleDateFormat;
    invoke-static {p0, p1}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/text/SimpleDateFormat;->format(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    return-object v1
.end method

```

# 字段

与方法表示很相似，只是字段没有方法签名和返回值，取而代之的是字段类型
Lpackage/name/ObjectName;->FiedlName:Ljava/lang/String;

其中字段名与字段类型用冒号“:”分割

```
# static fields
.field private static instance:Lcn/woblog/markdowndiary/repository/LocalNoteRepository;


# instance fields
.field private final context:Landroid/content/Context;

```

其中：
\# static fields：静态字段
\# instance fields：实例字段

# Dalvik指令集

他在调用格式上模仿了C语言的调用约定，[官方地址](https://link.jianshu.com/?t=https://source.android.com/devices/tech/dalvik/dalvik-bytecode.html),指令语法与助词有如下特点：

1. 采用采用从目标(destination)到源(source)的方法
2. 根据字节码的大小与类型不同，一些字节码添加了名称后缀已消除歧义
   2.1 32位常规类型的字节码未添加任何后缀
   2.2 64位常规类型的字节码添加 -wide后缀
   3.3 特殊类型的字节码根据具体类型添加后缀，-boolean,-byte,-char,-short,-int,-long,-float,-double,-object,-string,-class,-void之一
3. 根据字节码的布局和选项不同，一些字节码添加了字节后缀消除歧义，后缀与字节码直接用/分割
4. 在指令集的描述中，宽度值中每个字母表示宽度为4位

如：
move-wide/from16 vAA, vBBBB
move-wide/from16 v18, v0

move:基础字节码(base opcode)，标示是基本操作
wide:标示指令操作的数据宽度为64位宽度
from16:字节码后缀(opcode suffix),标示源(vBBBB)为一个16的寄存器引用变量
vAA:目的寄存器，v0~v255
vBBBB:源寄存器，v0~v65535

# 指令

## nop

空操作，被用来做对齐代码

## 数据定义

用来定义程序中用到的常量，字符串，类等数据
const/4 vA, #+B :将数组扩展为32位后赋给寄存器vA
const/16 vAA, #+BBBB
const vAA, #+BBBBBBBB：将数组赋值给寄存器vAA
const-wide/16 vAA, #+BBBBB ：将数值扩展为64位后赋给寄存器vAA
const-string vAA, string@BBBB：将字符串索引构造一个字符串并赋给vAA
const-class vAA, type@BBBB:通过类型索引获取一个类的引用并赋给寄存器vAA

```
private void testConst() {
    int a = 1;
    int b = 7;
    int c = 254;
    int d = 2345;
    int d1 = 65538;

    long e = 12435465657677L;
    float f = 123235409234.09097945F;
    double g = 111343333454999999999.912384375;
}

```

```
//-8到7用4，大于255小于等于65535用16
const/4 v0, 0x1

.line 25
.local v0, "a":I
const/4 v1, 0x7

.line 26
.local v1, "b":I
const/16 v2, 0xfe

.line 27
.local v2, "c":I
const/16 v3, 0x929

.line 28
.local v3, "d":I
const v4, 0x10002 //65538，大于65535用const v4

//long用const-wide
.line 30
.local v4, "d1":I
const-wide v6, 0xb4f5b835d4dL

.line 31
.local v6, "e":J
const v5, 0x51e58b39

.line 32
.local v5, "f":F
const-wide v8, 0x441824cbef6b9491L    # 1.11343333455E20

```

## 数据操作指令

move destination, source
根据字节码大小和类型不同，后面回天津不同的后缀
move vA, vB：vB寄存器值赋值给vA寄存器，都为4位
move-object vA,vB
move-result vAA：将上一个invoke类型的指令操作的单字非对象结果负责vAA寄存器
move-result-object vAA：将上一个invoke类型指令操作的对象赋值给vAA
move-exception vAA:保存一个运行时发生的异常vAA寄存器，必须是异常发生时的异常处理的第一条指令

```
private void testMove() {
    int a = 100;
    long b = 100000000000000000L;

    int c = a;
    long d = b;

    Log.d(TAG,c+"");
    Log.d(TAG,d+"");


    int e = getIntResult();
    Log.d(TAG,e+"");

    try {
        int f = e/c;
    } catch (ArithmeticException e1) {
        e1.printStackTrace();
    }catch (Exception e1) {
        e1.printStackTrace();
    }finally {

    }
}

```

```
//move-result-object
invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

invoke-virtual {v7, v1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

move-result-object v7

const-string v8, ""

invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

move-result-object v7

//move-result
invoke-direct {p0}, Lcom/woblog/testsmali/MainActivity;->getIntResult()I

move-result v6

//move exception
.line 35
:try_start_0
div-int v8, v6, v1
:try_end_0
.catch Ljava/lang/ArithmeticException; {:try_start_0 .. :try_end_0} :catch_0
.catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_1
.catchall {:try_start_0 .. :try_end_0} :catchall_0

.line 43
:goto_0
return-void

.line 36
:catch_0
move-exception v7

.line 37
.local v7, "e1":Ljava/lang/ArithmeticException;
:try_start_1
invoke-virtual {v7}, Ljava/lang/ArithmeticException;->printStackTrace()V
:try_end_1
.catchall {:try_start_1 .. :try_end_1} :catchall_0

goto :goto_0

.line 40
.end local v7    # "e1":Ljava/lang/ArithmeticException;
:catchall_0
move-exception v8

throw v8

.line 38
:catch_1
move-exception v7

.line 39
.local v7, "e1":Ljava/lang/Exception;
:try_start_2
invoke-virtual {v7}, Ljava/lang/Exception;->printStackTrace()V
:try_end_2
.catchall {:try_start_2 .. :try_end_2} :catchall_0

goto :goto_0


```

## 返回指令

return-void :返回一个void
return vAA:返回一个32位非对象类型的值，返回寄存器为8位
return-wide vAA：返回一个64位非对象类型的值，返回寄存器为8位
return-object vAA:返回一个对象类型

```
private String returnObject() {
    return new String("");
}

private float returnFloat() {
    return 12333334.00234345F;
}

private double returnDouble() {
    return 3425465767.9345865;
}

private long returnLong() {
    return 12445657999999L;
}

private int returnInt() {
    return 1024;
}

private void returnVoid() {
    int a = 3;
}

```

```
.method private returnDouble()D
    .locals 2

    .prologue
    .line 40
    const-wide v0, 0x41e9858eb4fde822L    # 3.4254657679345865E9

    return-wide v0
.end method

.method private returnFloat()F
    .locals 1

    .prologue
    .line 36
    const v0, 0x4b3c3116    # 1.2333334E7f

    return v0
.end method

.method private returnInt()I
    .locals 1

    .prologue
    .line 48
    const/16 v0, 0x400

    return v0
.end method

.method private returnLong()J
    .locals 2

    .prologue
    .line 44
    const-wide v0, 0xb51bb062a7fL

    return-wide v0
.end method

.method private returnObject()Ljava/lang/String;
    .locals 2

    .prologue
    .line 32
    new-instance v0, Ljava/lang/String;

    const-string v1, ""

    invoke-direct {v0, v1}, Ljava/lang/String;-><init>(Ljava/lang/String;)V

    return-object v0
.end method

.method private returnVoid()V
    .locals 1

    .prologue
    .line 52
    const/4 v0, 0x3

    .line 53
    .local v0, "a":I
    return-void
.end method

```

## 锁指令

锁指令多用在多线程程序中对同一对象的操作
monitor-enter vAA 为指定的对象获取锁
monitor-exit vAA 释放指定的对象的锁

```
private void callSynchronizeClassMethod() {
    synchronized (MainActivity.class) {
        Log.d("TAG","synchronized class");
    }
}

private void callSynchronizeMethod() {
    synchronized (this) {
        Log.d("TAG","synchronized this");
    }
}

private synchronized void callLockMethod() {
    Log.d("TAG","synchronized method");
}

```

```
.method private declared-synchronized callLockMethod()V
    .locals 2

    .prologue
    .line 43
    monitor-enter p0

    :try_start_0
    const-string v0, "TAG"

    const-string v1, "synchronized method"

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    .line 44
    monitor-exit p0

    return-void

    .line 43
    :catchall_0
    move-exception v0

    monitor-exit p0

    throw v0
.end method

.method private callSynchronizeClassMethod()V
    .locals 3

    .prologue
    .line 31
    const-class v1, Lcom/woblog/testsmali/MainActivity;

    monitor-enter v1

    .line 32
    :try_start_0
    const-string v0, "TAG"

    const-string v2, "synchronized class"

    invoke-static {v0, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 33
    monitor-exit v1

    .line 34
    return-void

    .line 33
    :catchall_0
    move-exception v0

    monitor-exit v1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v0
.end method

.method private callSynchronizeMethod()V
    .locals 2

    .prologue
    .line 37
    monitor-enter p0

    .line 38
    :try_start_0
    const-string v0, "TAG"

    const-string v1, "synchronized this"

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 39
    monitor-exit p0

    .line 40
    return-void

    .line 39
    :catchall_0
    move-exception v0

    monitor-exit p0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v0
.end method

```

## 实例操作

包括类型转换，检查和创建新实例
check-cast vAA, type@BBBB：将vAA中的对象转为指定类型，如果失败会抛出ClassCastException异常，如果类型B是基本类型，对于分基本类型的A来说运行始终是失败的
instance-of vA, vB, type@CCCC:判断vB寄存器的对象是否可以转为指定类型，如果可以vA为1，否则为0
new-instance vAA, type@BBBB:构造一个指定类型的对象，并赋值给vAA寄存器，不能是数组类型

```
CharSequence cs = new String();
Object o = cs;

String s = (String) cs;

//实例检测
if (s instanceof CharSequence) {
    Log.d("TAG", "ok");
} else {
    Log.d("TAG","no");
}


//创建实例
StringBuilder sb = new StringBuilder();
sb.append("Ok");

String s1 = new String("new string");
String s2 = "string";

```

```
new-instance v1, Ljava/lang/String;

invoke-direct {v1}, Ljava/lang/String;-><init>()V

.line 33
.local v1, "cs":Ljava/lang/CharSequence;
move-object v7, v1

.local v7, "o":Ljava/lang/CharSequence;
move-object v8, v1

.line 35
check-cast v8, Ljava/lang/String;

.line 38
.local v8, "s":Ljava/lang/String;
instance-of v12, v8, Ljava/lang/CharSequence;

if-eqz v12, :cond_0

.line 39
const-string v12, "TAG"

const-string v13, "ok"

invoke-static {v12, v13}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

.line 46
:goto_0
new-instance v11, Ljava/lang/StringBuilder;

invoke-direct {v11}, Ljava/lang/StringBuilder;-><init>()V

.line 47
.local v11, "sb":Ljava/lang/StringBuilder;
const-string v12, "Ok"

invoke-virtual {v11, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

.line 49
new-instance v9, Ljava/lang/String;

const-string v12, "new string"

invoke-direct {v9, v12}, Ljava/lang/String;-><init>(Ljava/lang/String;)V

.line 50
.local v9, "s1":Ljava/lang/String;
const-string v10, "string"

.line 51
.local v10, "s2":Ljava/lang/String;
return-void

.line 41
.end local v9    # "s1":Ljava/lang/String;
.end local v10    # "s2":Ljava/lang/String;
.end local v11    # "sb":Ljava/lang/StringBuilder;
:cond_0
const-string v12, "TAG"

const-string v13, "no"

invoke-static {v12, v13}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

goto :goto_0

```

## 数组操作

包括获取数组长度，新建数组，数组赋值，数组元素取值与赋值等
array-length vA, vB:获取vB寄存器中数组的长度并赋值给vA寄存器
new-array vA, vB, type@CCCC：构造指定类型(type@CCCC)与大小(vB)的数组，并赋值给vA寄存器
filled-new-array {vC,vD,vE,vF,vG}, type@BBBB:构造指定类型(type@BBBB)与大小vA的数组并填充数组内容，除了指定数组的大小还指定了参数个数
filled-new-array/range {vCCCC .. vNNNN}, type@BBBB:与上一条类似，只是参数使用取值范围，vC是第一个参数寄存器，N=A+C-1
fill-array-data vAA, +BBBBBBBB:vAA为寄存器数组引用，后面跟一个数据表
arrayop vAA, vBB, vCC：对vBB寄存器指定的数组元素进入取值或赋值。vCC指定数组元素索引，vAA寄存器用来存放读取的或需要设置的值。读取元素使用age类指令，赋值使用aput类指令，根据数组中存储的类指令后面会跟不同的后缀：
aget,aget-wide,aget-object,aget-boolean,aget-byte,aget-char,aget-short
aput,aput-wide,aput-object,aput-boolean,aput-byte,aput-char,aput-short

```
private void testArray() {
    int[] ints = new int[2];
    int[] ints1 = null;
    int[] ints2 = {1,2,3};

    Integer[] integers = new Integer[]{1,2,4};

    int[] strings = {1,2,3,4,5,6,5,6,6,6,6,6,6,7,7,8,8,8,8,8,1,1,1,3,3,5,6,54,5,6,56,567,67,6,34,45,45,6,56,57,45,45,5,56,56,7,34,543,543,6,56,56,45,4,54,5,45,56};

    //数组长度
    int length = ints.length;
    int length1 = ints2.length;
    int length2 = strings.length;

    //获取数组元素
    int string = strings[30];
    int string1 = ints2[1];

    //赋值
    strings[30] =  length;
    ints2[1] =  length2;
}

```

```
.method private testArray()V
    .locals 15

    .prologue
    const/16 v14, 0x1e

    const/4 v10, 0x3

    const/4 v13, 0x2

    const/4 v12, 0x1

    .line 27
    new-array v1, v13, [I

    .line 28
    .local v1, "ints":[I
    const/4 v2, 0x0

    .line 29
    .local v2, "ints1":[I
    new-array v3, v10, [I

    fill-array-data v3, :array_0

    .line 31
    .local v3, "ints2":[I
    new-array v0, v10, [Ljava/lang/Integer;

    const/4 v10, 0x0

    invoke-static {v12}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v11

    aput-object v11, v0, v10

    invoke-static {v13}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v10

    aput-object v10, v0, v12

    const/4 v10, 0x4

    invoke-static {v10}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v10

    aput-object v10, v0, v13

    .line 33
    .local v0, "integers":[Ljava/lang/Integer;
    const/16 v10, 0x3a

    new-array v9, v10, [I

    fill-array-data v9, :array_1

    .line 36
    .local v9, "strings":[I
    array-length v4, v1

    .line 37
    .local v4, "length":I
    array-length v5, v3

    .line 38
    .local v5, "length1":I
    array-length v6, v9

    .line 41
    .local v6, "length2":I
    aget v7, v9, v14

    .line 42
    .local v7, "string":I
    aget v8, v3, v12

    .line 45
    .local v8, "string1":I
    aput v4, v9, v14

    .line 46
    aput v6, v3, v12

    .line 47
    return-void

    .line 29
    :array_0
    .array-data 4
        0x1
        0x2
        0x3
    .end array-data

    .line 33
    :array_1
    .array-data 4
        0x1
        0x2
        0x3
        0x4
        0x5
        0x6
        0x5
        0x6
        0x6
        0x6
        0x6
        0x6
        0x6
        0x7
        0x7
        0x8
        0x8
        0x8
        0x8
        0x8
        0x1
        0x1
        0x1
        0x3
        0x3
        0x5
        0x6
        0x36
        0x5
        0x6
        0x38
        0x237
        0x43
        0x6
        0x22
        0x2d
        0x2d
        0x6
        0x38
        0x39
        0x2d
        0x2d
        0x5
        0x38
        0x38
        0x7
        0x22
        0x21f
        0x21f
        0x6
        0x38
        0x38
        0x2d
        0x4
        0x36
        0x5
        0x2d
        0x38
    .end array-data
.end method

```

## 异常指令

throw vAA:抛出vAA寄存器中指定类型的异常

```
private void throw2() {
    try {
        throw new Exception("test throw runtime exception");
    } catch (Exception e) {
        e.printStackTrace();
    }
}

private void throw1() {
    throw new RuntimeException("test throw runtime exception");
}

```

```
.method private throw1()V
    .locals 2

    .prologue
    .line 38
    new-instance v0, Ljava/lang/RuntimeException;

    const-string v1, "test throw runtime exception"

    invoke-direct {v0, v1}, Ljava/lang/RuntimeException;-><init>(Ljava/lang/String;)V

    throw v0
.end method

.method private throw2()V
    .locals 3

    .prologue
    .line 31
    :try_start_0
    new-instance v1, Ljava/lang/Exception;

    const-string v2, "test throw runtime exception"

    invoke-direct {v1, v2}, Ljava/lang/Exception;-><init>(Ljava/lang/String;)V

    throw v1
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    .line 32
    :catch_0
    move-exception v0

    .line 33
    .local v0, "e":Ljava/lang/Exception;
    invoke-virtual {v0}, Ljava/lang/Exception;->printStackTrace()V

    .line 35
    return-void
.end method

```

## 跳转指令

用于从当前地址跳转到指定的偏移处，提供了三种指令：无条件(goto),分支跳转(switch),条件跳转(if)
goto +AA:无条件跳转到指定偏移处，AA不能为0
goto/16 +AAAA
goto/32 +AAAAAAAA

packed-switch vAA, +BBBBBBBB:分支跳转，vAA寄存器为switch分支需要判断的值

if-test vA, vB, +CCCC 条件跳转指令，比较vA寄存器与vB寄存器的值，如果比较结果满足就跳转到CCCC指定的偏移处，不能为0，有以下几条：

if-eq:if(vA==vB)
if-ne:vA!=vB
if-lt:vA<vB
if-gt:vA>vB
if-le:vA<=vB
if-ge:vA>=vB

if-testz vAA, +BBBB:条件转移，拿vAA寄存器与0比较，如果比较结果满足或值为0就跳转到BBBB指定的偏移处，不为0

if-eqz:vAA==0
if-nez:vAA!=0
if-ltz:vAA<0
if-gtz:vAA>0
if-lez:vAA<=0
if-gez:vAA>=0

```
private void testIfz() {
    int a = 3;
    if (a == 0) {

    } else {

    }
    if (a != 0) {

    } else {

    }
    if (a < 0) {

    } else {

    }
    if (a > 0) {

    } else {

    }
    if (a <= 0) {

    } else {

    }
    if (a >= 0) {

    } else {

    }

    if (a < 5) {
        Log.d("TAG", "<5");
    } else if (a > 5) {
        Log.d("TAG", ">5");
    } else {
        Log.d("TAG", "=5");
    }
}

private void testIf() {
    int a = 2;
    int b = 3;
    if (a == b) {

    } else {

    }
    if (a != b) {

    } else {

    }
    if (a < b) {

    } else {

    }
    if (a > b) {

    } else {

    }
    if (a <= b) {

    } else {

    }
    if (a >= b) {

    } else {

    }

}

```

```
.method private testIf()V
    .locals 2

    .prologue
    .line 69
    const/4 v0, 0x2

    .line 70
    .local v0, "a":I
    const/4 v1, 0x3

    .line 71
    .local v1, "b":I
    if-ne v0, v1, :cond_0

    .line 76
    :cond_0
    if-eq v0, v1, :cond_1

    .line 81
    :cond_1
    if-ge v0, v1, :cond_2

    .line 86
    :cond_2
    if-le v0, v1, :cond_3

    .line 91
    :cond_3
    if-gt v0, v1, :cond_4

    .line 96
    :cond_4
    if-lt v0, v1, :cond_5

    .line 102
    :cond_5
    return-void
.end method

.method private testIfz()V
    .locals 3

    .prologue
    const/4 v1, 0x5

    .line 27
    const/4 v0, 0x3

    .line 28
    .local v0, "a":I
    if-nez v0, :cond_0

    .line 33
    :cond_0
    if-eqz v0, :cond_1

    .line 38
    :cond_1
    if-gez v0, :cond_2

    .line 43
    :cond_2
    if-lez v0, :cond_3

    .line 48
    :cond_3
    if-gtz v0, :cond_4

    .line 53
    :cond_4
    if-ltz v0, :cond_5

    .line 59
    :cond_5
    if-ge v0, v1, :cond_6

    .line 60
    const-string v1, "TAG"

    const-string v2, "<5"

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 66
    :goto_0
    return-void

    .line 61
    :cond_6
    if-le v0, v1, :cond_7

    .line 62
    const-string v1, "TAG"

    const-string v2, ">5"

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_0

    .line 64
    :cond_7
    const-string v1, "TAG"

    const-string v2, "=5"

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_0
.end method

```

## 比较指令

用于对两个寄存器的值比较
cmpkind vAA, vBB, vCC：vBB和vCC为要比较的值，结果放到vAA中
cmpl-float:单精度，vBB大于vCC，vAA=-1,等于vAA=0,小于vAA=1
cmpg-float：单精度，vBB大于vCC，vAA=1,等于vAA=0,小于vAA=-1
cmpl-double:双精度
cmpg-double:双精度
cmp-long:长整形

```
private void testCmpLong() {
    long a = 13;
    long b = 12;
    if (a < b) {
        Log.d("TAG", "<");
    } else if (a > b) {
        Log.d("TAG", ">");
    } else {
        Log.d("TAG", "=");
    }
}

private void testCmpDouble() {
    double a = 13.4;
    double b = 11.4;
    if (a < b) {
        Log.d("TAG", "<");
    } else if (a > b) {
        Log.d("TAG", ">");
    } else {
        Log.d("TAG", "=");
    }
}

private void testCmpFloat() {
    float a = 13.4F;
    float b = 10.4F;
    if (a < b) {
        Log.d("TAG", "<");
    } else if (a > b) {
        Log.d("TAG", ">");
    } else {
        Log.d("TAG", "=");
    }
}

```

```
.method private testCmpDouble()V
    .locals 6

    .prologue
    .line 46
    const-wide v0, 0x402acccccccccccdL    # 13.4

    .line 47
    .local v0, "a":D
    const-wide v2, 0x4026cccccccccccdL    # 11.4

    .line 48
    .local v2, "b":D
    cmpg-double v4, v0, v2

    if-gez v4, :cond_0

    .line 49
    const-string v4, "TAG"

    const-string v5, "<"

    invoke-static {v4, v5}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 55
    :goto_0
    return-void

    .line 50
    :cond_0
    cmpl-double v4, v0, v2

    if-lez v4, :cond_1

    .line 51
    const-string v4, "TAG"

    const-string v5, ">"

    invoke-static {v4, v5}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_0

    .line 53
    :cond_1
    const-string v4, "TAG"

    const-string v5, "="

    invoke-static {v4, v5}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_0
.end method

.method private testCmpFloat()V
    .locals 4

    .prologue
    .line 58
    const v0, 0x41566666    # 13.4f

    .line 59
    .local v0, "a":F
    const v1, 0x41266666    # 10.4f

    .line 60
    .local v1, "b":F
    cmpg-float v2, v0, v1

    if-gez v2, :cond_0 #>=

    .line 61
    const-string v2, "TAG"

    const-string v3, "<"

    invoke-static {v2, v3}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 67
    :goto_0
    return-void

    .line 62
    :cond_0
    cmpl-float v2, v0, v1

    if-lez v2, :cond_1 #<=

    .line 63
    const-string v2, "TAG"

    const-string v3, ">"

    invoke-static {v2, v3}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_0

    .line 65
    :cond_1
    const-string v2, "TAG"

    const-string v3, "="

    invoke-static {v2, v3}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_0
.end method

.method private testCmpLong()V
    .locals 6

    .prologue
    .line 34
    const-wide/16 v0, 0xd

    .line 35
    .local v0, "a":J
    const-wide/16 v2, 0xc

    .line 36
    .local v2, "b":J
    cmp-long v4, v0, v2

    if-gez v4, :cond_0

    .line 37
    const-string v4, "TAG"

    const-string v5, "<"

    invoke-static {v4, v5}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 43
    :goto_0
    return-void

    .line 38
    :cond_0
    cmp-long v4, v0, v2

    if-lez v4, :cond_1

    .line 39
    const-string v4, "TAG"

    const-string v5, ">"

    invoke-static {v4, v5}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_0

    .line 41
    :cond_1
    const-string v4, "TAG"

    const-string v5, "="

    invoke-static {v4, v5}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_0
.end method

```

## 字段操作指令

用来对 对象实例的字段进行读写操作。字段类型可以是Java中有效的类型，对于实例字段和静态字段有两类指令：
iget,iput对实例字段进行读，写
sget,sput对静态字段

会根据类型不同添加不同的后缀
iget，iget-wide,iget-object,iget-boolean,iget-byte,iget-char,iget-short
iput,iput-wide,iput-object,iput-boolean,iput-byte,iput-char,iput-short

sget,sget-wide,sget-object,sget-boolean,sget-byte,sget-char,sget-short
...

```
private void testInstanceFieldOperator() {
    //write
    InstanceObject instanceObject = new InstanceObject();
    instanceObject.aInt=1;
    instanceObject.aLong=12454L;
    instanceObject.aFloat=12344.45F;
    instanceObject.aDouble=123546.2;
    instanceObject.object=new Object();
    instanceObject.aBoolean=true;
    instanceObject.aByte=3;
    instanceObject.aChar='c';
    instanceObject.aShort=1;

    Log.d("TAG",String.valueOf(instanceObject.aInt));
    Log.d("TAG",String.valueOf(instanceObject.aLong));
    Log.d("TAG",String.valueOf(instanceObject.aFloat));
    Log.d("TAG",String.valueOf(instanceObject.aDouble));
    Log.d("TAG",String.valueOf(instanceObject.object));
    Log.d("TAG",String.valueOf(instanceObject.aBoolean));
    Log.d("TAG",String.valueOf(instanceObject.aByte));
    Log.d("TAG",String.valueOf(instanceObject.aChar));
    Log.d("TAG",String.valueOf(instanceObject.aShort));
}

private void testStatusFieldOperator() {
    //write
    StatusObject.aInt=1;
    StatusObject.aLong=12454L;
    StatusObject.aFloat=12344.45F;
    StatusObject.aDouble=123546.2;
    StatusObject.object=new Object();
    StatusObject.aBoolean=true;
    StatusObject.aByte=3;
    StatusObject.aChar='c';
    StatusObject.aShort=1;

    Log.d("TAG",String.valueOf(StatusObject.aInt));
    Log.d("TAG",String.valueOf(StatusObject.aLong));
    Log.d("TAG",String.valueOf(StatusObject.aFloat));
    Log.d("TAG",String.valueOf(StatusObject.aDouble));
    Log.d("TAG",String.valueOf(StatusObject.object));
    Log.d("TAG",String.valueOf(StatusObject.aBoolean));
    Log.d("TAG",String.valueOf(StatusObject.aByte));
    Log.d("TAG",String.valueOf(StatusObject.aChar));
    Log.d("TAG",String.valueOf(StatusObject.aShort));
}

```

```
.method private testInstanceFieldOperator()V
    .locals 5

    .prologue
    const/4 v4, 0x1

    .line 30
    new-instance v0, Lcom/woblog/testsmali/InstanceObject;

    invoke-direct {v0}, Lcom/woblog/testsmali/InstanceObject;-><init>()V

    .line 31
    .local v0, "instanceObject":Lcom/woblog/testsmali/InstanceObject;
    iput v4, v0, Lcom/woblog/testsmali/InstanceObject;->aInt:I

    .line 32
    const-wide/16 v2, 0x30a6

    iput-wide v2, v0, Lcom/woblog/testsmali/InstanceObject;->aLong:J

    .line 33
    const v1, 0x4640e1cd

    iput v1, v0, Lcom/woblog/testsmali/InstanceObject;->aFloat:F

    .line 34
    const-wide v2, 0x40fe29a333333333L    # 123546.2

    iput-wide v2, v0, Lcom/woblog/testsmali/InstanceObject;->aDouble:D

    .line 35
    new-instance v1, Ljava/lang/Object;

    invoke-direct {v1}, Ljava/lang/Object;-><init>()V

    iput-object v1, v0, Lcom/woblog/testsmali/InstanceObject;->object:Ljava/lang/Object;

    .line 36
    iput-boolean v4, v0, Lcom/woblog/testsmali/InstanceObject;->aBoolean:Z

    .line 37
    const/4 v1, 0x3

    iput-byte v1, v0, Lcom/woblog/testsmali/InstanceObject;->aByte:B

    .line 38
    const/16 v1, 0x63

    iput-char v1, v0, Lcom/woblog/testsmali/InstanceObject;->aChar:C

    .line 39
    iput-short v4, v0, Lcom/woblog/testsmali/InstanceObject;->aShort:S

    .line 41
    const-string v1, "TAG"

    iget v2, v0, Lcom/woblog/testsmali/InstanceObject;->aInt:I

    invoke-static {v2}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 42
    const-string v1, "TAG"

    iget-wide v2, v0, Lcom/woblog/testsmali/InstanceObject;->aLong:J

    invoke-static {v2, v3}, Ljava/lang/String;->valueOf(J)Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 43
    const-string v1, "TAG"

    iget v2, v0, Lcom/woblog/testsmali/InstanceObject;->aFloat:F

    invoke-static {v2}, Ljava/lang/String;->valueOf(F)Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 44
    const-string v1, "TAG"

    iget-wide v2, v0, Lcom/woblog/testsmali/InstanceObject;->aDouble:D

    invoke-static {v2, v3}, Ljava/lang/String;->valueOf(D)Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 45
    const-string v1, "TAG"

    iget-object v2, v0, Lcom/woblog/testsmali/InstanceObject;->object:Ljava/lang/Object;

    invoke-static {v2}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 46
    const-string v1, "TAG"

    iget-boolean v2, v0, Lcom/woblog/testsmali/InstanceObject;->aBoolean:Z

    invoke-static {v2}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 47
    const-string v1, "TAG"

    iget-byte v2, v0, Lcom/woblog/testsmali/InstanceObject;->aByte:B

    invoke-static {v2}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 48
    const-string v1, "TAG"

    iget-char v2, v0, Lcom/woblog/testsmali/InstanceObject;->aChar:C

    invoke-static {v2}, Ljava/lang/String;->valueOf(C)Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 49
    const-string v1, "TAG"

    iget-short v2, v0, Lcom/woblog/testsmali/InstanceObject;->aShort:S

    invoke-static {v2}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 50
    return-void
.end method

.method private testStatusFieldOperator()V
    .locals 4

    .prologue
    const/4 v2, 0x1

    .line 54
    sput v2, Lcom/woblog/testsmali/StatusObject;->aInt:I

    .line 55
    const-wide/16 v0, 0x30a6

    sput-wide v0, Lcom/woblog/testsmali/StatusObject;->aLong:J

    .line 56
    const v0, 0x4640e1cd

    sput v0, Lcom/woblog/testsmali/StatusObject;->aFloat:F

    .line 57
    const-wide v0, 0x40fe29a333333333L    # 123546.2

    sput-wide v0, Lcom/woblog/testsmali/StatusObject;->aDouble:D

    .line 58
    new-instance v0, Ljava/lang/Object;

    invoke-direct {v0}, Ljava/lang/Object;-><init>()V

    sput-object v0, Lcom/woblog/testsmali/StatusObject;->object:Ljava/lang/Object;

    .line 59
    sput-boolean v2, Lcom/woblog/testsmali/StatusObject;->aBoolean:Z

    .line 60
    const/4 v0, 0x3

    sput-byte v0, Lcom/woblog/testsmali/StatusObject;->aByte:B

    .line 61
    const/16 v0, 0x63

    sput-char v0, Lcom/woblog/testsmali/StatusObject;->aChar:C

    .line 62
    sput-short v2, Lcom/woblog/testsmali/StatusObject;->aShort:S

    .line 64
    const-string v0, "TAG"

    sget v1, Lcom/woblog/testsmali/StatusObject;->aInt:I

    invoke-static {v1}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 65
    const-string v0, "TAG"

    sget-wide v2, Lcom/woblog/testsmali/StatusObject;->aLong:J

    invoke-static {v2, v3}, Ljava/lang/String;->valueOf(J)Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 66
    const-string v0, "TAG"

    sget v1, Lcom/woblog/testsmali/StatusObject;->aFloat:F

    invoke-static {v1}, Ljava/lang/String;->valueOf(F)Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 67
    const-string v0, "TAG"

    sget-wide v2, Lcom/woblog/testsmali/StatusObject;->aDouble:D

    invoke-static {v2, v3}, Ljava/lang/String;->valueOf(D)Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 68
    const-string v0, "TAG"

    sget-object v1, Lcom/woblog/testsmali/StatusObject;->object:Ljava/lang/Object;

    invoke-static {v1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 69
    const-string v0, "TAG"

    sget-boolean v1, Lcom/woblog/testsmali/StatusObject;->aBoolean:Z

    invoke-static {v1}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 70
    const-string v0, "TAG"

    sget-byte v1, Lcom/woblog/testsmali/StatusObject;->aByte:B

    invoke-static {v1}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 71
    const-string v0, "TAG"

    sget-char v1, Lcom/woblog/testsmali/StatusObject;->aChar:C

    invoke-static {v1}, Ljava/lang/String;->valueOf(C)Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 72
    const-string v0, "TAG"

    sget-short v1, Lcom/woblog/testsmali/StatusObject;->aShort:S

    invoke-static {v1}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 73
    return-void
.end method

```

## 方法调用

在方法调用者我们可以看到有：

```
invoke-super {p0, p1}, Lcom/woblog/testsmali/BaseActivity;->onCreate(Landroid/os/Bundle;)V

invoke-virtual {p0, v0}, Lcom/woblog/testsmali/MainActivity;->setContentView(I)V

invoke-direct {p0}, Lcom/woblog/testsmali/MainActivity;->initMove()V

invoke-static {}, Lcom/woblog/testsmali/TimeUtil;->getCurrentTime()J

invoke-interface {v0}, Lcom/woblog/testsmali/ICallback;->onSuccess()V

```

## 数据转换

数据转换指令用于将一种数据类型转换为另一个类型，unop vA, vB:寄存器存储要转换的数据，vA存储转换后的数据
neg-int:整形求补
not-int:整形求反
neg-long:长整型求补
not-long:长整型求反
neg-float:单精度求补
not-float:
neg-double:
not-double:

int-to-long:整型转为长整型
int-to-float:整型转单精度浮点型
int-to-double:整型转双精度浮点型

int-to-byte:整型转字节型
int-to-char:整型转字符串
int-to-short:整型转短整型

long-to-int
long-to-float
long-to-double

float-to-int
float-to-long
float-to-double

double-to-int
double-to-long
double-to-float

```
private void testConvert() {
    int i1=13;

    //int 转其他类型
    long l1 = i1;
    float f1 = i1;
    double d1 = i1;

    byte b1 = (byte) i1;
    char c1 = (char) i1;
    short s1 = (short) i1;

    //long 转其他类型
    long l2 = 234444556576L;
    int i2 = (int) l2;
    float f2 = l2;
    double d2 = l2;

    //float 转其他类型
    float f10 =234399.9F;
    int i10 = (int) f10;
    long l10 = (long) f10;
    double d10 = f10;

    //double 转其他类型
    double d20 = 123344445.324;
    int i20 = (int) d20;
    long l20 = (long) d20;
    float f20 = (float) d20;
}

```

```
.method private testConvert()V
    .locals 29

    .prologue
    .line 30
    const/16 v16, 0xd

    .line 33
    .local v16, "i1":I
    move/from16 v0, v16

    int-to-long v0, v0

    move-wide/from16 v20, v0

    .line 34
    .local v20, "l1":J
    move/from16 v0, v16

    int-to-float v12, v0

    .line 35
    .local v12, "f1":F
    move/from16 v0, v16

    int-to-double v4, v0

    .line 37
    .local v4, "d1":D
    move/from16 v0, v16

    int-to-byte v2, v0

    .line 38
    .local v2, "b1":B
    move/from16 v0, v16

    int-to-char v3, v0

    .line 39
    .local v3, "c1":C
    move/from16 v0, v16

    int-to-short v0, v0

    move/from16 v28, v0

    .line 42
    .local v28, "s1":S
    const-wide v24, 0x3695fc0920L

    .line 43
    .local v24, "l2":J
    move-wide/from16 v0, v24

    long-to-int v0, v0

    move/from16 v18, v0

    .line 44
    .local v18, "i2":I
    move-wide/from16 v0, v24

    long-to-float v14, v0

    .line 45
    .local v14, "f2":F
    move-wide/from16 v0, v24

    long-to-double v8, v0

    .line 48
    .local v8, "d2":D
    const v13, 0x4864e7fa    # 234399.9f

    .line 49
    .local v13, "f10":F
    float-to-int v0, v13

    move/from16 v17, v0

    .line 50
    .local v17, "i10":I
    float-to-long v0, v13

    move-wide/from16 v22, v0

    .line 51
    .local v22, "l10":J
    float-to-double v6, v13

    .line 54
    .local v6, "d10":D
    const-wide v10, 0x419d6858f54bc6a8L    # 1.23344445324E8

    .line 55
    .local v10, "d20":D
    double-to-int v0, v10

    move/from16 v19, v0

    .line 56
    .local v19, "i20":I
    double-to-long v0, v10

    move-wide/from16 v26, v0

    .line 57
    .local v26, "l20":J
    double-to-float v15, v10

    .line 58
    .local v15, "f20":F
    return-void
.end method

```

## 数据运行指令

算术运算：加，减，乘，除，模，移位等
逻辑运算：与，或，非，异或等

binop vAA, vBB, vCC：将vBB寄存器与vCC寄存器进行运算，结果保存到vAA

上面的指令会根据数据类型的不同在基础后面添加数据类型后缀，如：-int或-long
add-type vBB：vBB寄存器与vCC寄存器值进行加法运算,+
sub-type vBB:-
mul-type vBB:*
div-type vBB:/
rem-type vBB:%
and-type vBB:and
or-type vBB:or
xor-type vBB:xor
shl-type vBB:左移vCC位，<<
shr-type vBB:右移vCC位，>>
ushr-type vBB:无符号>>

其中type可以为int,long,float,double

binop/2addr vA, vB:将vA寄存器与vB寄存器进行运算，结果保存到vA
binop/lit16 vA, vB, #+CCCC:将vB寄存器与常量CCCC进行运算，结果保存到vA
binop/lit8 vAA, vBB, #+CC:将vBB寄存器与常量CC进行运行，结果保存到vAA

## Dalvik hello world

首先写一个基本框架

```
.class public LHelloWorld; #定义类名
.super Ljava/lang/Object; #定义父类
.method public static main([Ljava/lang/String;)V #声明静态的main函数
    .locals 4 #使用的寄存器个数，包括一个参数寄存器
    .param p0, "args" #一个参数

    .prologue #代码起始指令


    # 这里是代码主体


    return-void
.end method

```

完整版如下：

```
.class public LHelloWorld; #定义类名
.super Ljava/lang/Object; #定义父类
.method public static main([Ljava/lang/String;)V #声明静态的main函数
    .locals 4 #使用的寄存器个数，包括一个参数寄存器
    .param p0, "args" #一个参数

    .prologue #代码起始指令


    const-string v1, "Hello World"

    sget-object v0, Ljava/lang/System;->out:Ljava/io/PrintStream;

    invoke-virtual {v0,v1}, Ljava/io/PrintStream;->println(Ljava/lang/String;)V


    return-void
.end method

```

### 编译smali

我们去官网下载smali.jar，然后运行

```
java -jar smali.jar -o classes.dex HelloWorld.smali

```

编译完后我们把classes.dex push到手机里面

```
adb push classes.dex /data/local/ 

```

### 运行

```
dalvikvm -cp /data/local/classes.dex HelloWorld  

```

加强版本

```
.class public LHelloWorld; #定义类名
.super Ljava/lang/Object; #定义父类
.method public static main([Ljava/lang/String;)V #声明静态的main函数
    .locals 10 #使用的寄存器个数，包括一个参数寄存器
    .param p0, "args" #一个参数

    .prologue #代码起始指令

    sget-object v0, Ljava/lang/System;->out:Ljava/io/PrintStream;

    # 空指令

    nop

    nop

    nop


    # 数据定义指令
    
    const/4 v2, 0x3

    const/16 v3, 0xffff ##不能大于65535

    #大于65535用-wide
    
    const-wide v4, 0x10000


    # 定义一个类 类型
    
    const-class v5, Ljava/lang/String;


    # 数据操作指令

    move v6, v5

    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V


    const-string v8, "\u8fd9\u662f\u624b\u5199\u7684\u0073\u006d\u0061\u006c\u0069\u0044\u0065\u006d\u006f"

    invoke-virtual {v7, v12}, Ljava/java/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilber;

    invoke-direct {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v0, v9}, Ljava/io/PrintStream;->println(Ljava/java/String;)V


    # 打印字符串

    const-string v1, "Hello World"


    invoke-virtual {v0,v1}, Ljava/io/PrintStream;->println(Ljava/lang/String;)V


    return-void
.end method

```

如果我的文章对来带来的帮助或者有不明白的地方，可加QQ群：129961195，大家一起交流

小礼物走一走，来简书关注我

赞赏支持

- 