# RSA算法（MD5withRSA）

![薄樱鬼](https://pic4.zhimg.com/v2-05a25cf64796c1f3b8ef4a3ade724a14_xs.jpg)

薄樱鬼

1 年前

RSA原理：RSA算法基于一个十分简单的数论事实，将两个大素数相乘十分容易，但反过来想要对其乘积进行因式分解却极其困难，因此可以将乘积公开作为加密密钥。

RSA缺点：RSA的keysize位数越高，其产生密钥对及加密、解密的速度越慢，这是基于大素数非对称加密算法的缺陷。

```
KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");
keyPairGenerator.initialize(1024);

```

1、基于java的Signature API 的私钥签名

```
PKCS8EncodedKeySpec pkcs8EncodedKeySpec = new PKCS8EncodedKeySpec(rsaPrivateKey.getEncoded());
KeyFactory keyFactory = KeyFactory.getInstance("RSA");
PrivateKey privateKey = keyFactory.generatePrivate(pkcs8EncodedKeySpec);
Signature signature = Signature.getInstance("MD5withRSA");
//初始化私钥
signature.initSign(privateKey);
//传入签名内容
signature.update(src.getBytes());
//生成签名
byte[] result = signature.sign();

```

通过Signature的getInstance获得MD5withRSA，然后使用signature的iniSign对私钥进行初始化，调用signature的update方法传入签名内容，最后调用signature的sign方法生成签名。

2、基于java的Signature API 的公钥验证

```
X509EncodedKeySpec x509EncodedKeySpec = new X509EncodedKeySpec(rsaPublicKey.getEncoded());
keyFactory = KeyFactory.getInstance("RSA");
PublicKey publicKey = keyFactory.generatePublic(x509EncodedKeySpec);
signature = Signature.getInstance("MD5withRSA");
//初始化公钥
signature.initVerify(publicKey);
//传入签名内容
signature.update(src.getBytes());
//核对签名
boolean bool = signature.verify(result);

```

![img](https://pic1.zhimg.com/80/v2-73050425d290a9cb4ffc04a54615627b_hd.jpg)