# 大麦DM203/202/22D 路由器破解安装系统

> 不拆机刷breed和padavan










## 大麦DM203/202/22D，SSH破解方法

####  感谢列表：

1. yaoyuan298 的后台 ssh 设置页面地址  

http://www.right.com.cn/forum/thread-181708-1-1.html

2. wenreg 的编程器固件用来分析了源码 

http://right.com.cn/forum/thread-257108-1-1.html

#### 方法：

1. 打开 

http://192.168.10.1/upgrade.html

2. 开启 ssh 选：【开】，密码输入这个【最后面有一个空格】

```
123 | echo 6c216b27c8c9b051106c969e2077d4e9 > /ezwrt/bin/upgrade_passwd 
```

3. 点确定，然后提示密码错误没关系
4. 再次打开 

http://192.168.10.1/upgrade.html

5. 开启 ssh 选：【开】，密码输入这个，里面包含SSH登录公钥，可以使用自己的【最后面有一个空格】

```
123 | echo ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEA2tA3frFlnGsWmZeJMQuTzELWSplJN27FwXvVjan70bxnWSUvbGNV2rWD3zZo9jKoW5XmnZm46XCanWae8+LdIAk2HMG+IscjBCjfQBSHet0j2ODOt/WWOyMB67p5HGpa63kaWi4uT+ikB+xhNLRFOAxkHpnOpdnhFdU05mJ2GucEO3WEXeXnOaktJcFTcETC2VwbRPIzClsY9hero+3wNQS5CC0fU9r3J+XHqB+j8U/4wgIBBu5sflrwSofpS+g9a4vt+qJrqeXgDtz3SjxLUN2i5K6B0AxjxnC+R6a3+rtPPA3XEafaw7G58NjfnKOCu1A82gc3PhtdH60yzIPMGQ== dm > /etc/dropbear/authorized_keys 
```

6. 点确定，然后提示密码错误没关系
7. 再次打开 

http://192.168.10.1/upgrade.html

8. 开启 ssh 选 【开】，密码填写【dfc643】，点确定
9. 看到 start ssh success 即可
10. 然后用 ssh 软件连接如 putty，记得载入私钥，用户名是 root

> 用到的ssh 公钥与私钥

ssh 公钥

```
ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEA2tA3frFlnGsWmZeJMQuTzELWSplJN27FwXvVjan70bxnWSUvbGNV2rWD3zZo9jKoW5XmnZm46XCanWae8+LdIAk2HMG+IscjBCjfQBSHet0j2ODOt/WWOyMB67p5HGpa63kaWi4uT+ikB+xhNLRFOAxkHpnOpdnhFdU05mJ2GucEO3WEXeXnOaktJcFTcETC2VwbRPIzClsY9hero+3wNQS5CC0fU9r3J+XHqB+j8U/4wgIBBu5sflrwSofpS+g9a4vt+qJrqeXgDtz3SjxLUN2i5K6B0AxjxnC+R6a3+rtPPA3XEafaw7G58NjfnKOCu1A82gc3PhtdH60yzIPMGQ==
```

ssh私钥
```
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEA2tA3frFlnGsWmZeJMQuTzELWSplJN27FwXvVjan70bxnWSUv
bGNV2rWD3zZo9jKoW5XmnZm46XCanWae8+LdIAk2HMG+IscjBCjfQBSHet0j2ODO
t/WWOyMB67p5HGpa63kaWi4uT+ikB+xhNLRFOAxkHpnOpdnhFdU05mJ2GucEO3WE
XeXnOaktJcFTcETC2VwbRPIzClsY9hero+3wNQS5CC0fU9r3J+XHqB+j8U/4wgIB
Bu5sflrwSofpS+g9a4vt+qJrqeXgDtz3SjxLUN2i5K6B0AxjxnC+R6a3+rtPPA3X
Eafaw7G58NjfnKOCu1A82gc3PhtdH60yzIPMGQIBJQKCAQEAn6yy3+k8T4xqcBSi
Yg9eA8IR/xXpUfbjVdbn8cE7OC+Jr8EwcbBFkcK6LUNhWbZDgRpcLdEKZSioLavA
GcE5k+sLz8umbGfNcbz18H2u+MrizrHi9PF7d0MPPVC5Pj/Fzm0hEV/4SCZOL0ug
4UVHRJNrp6CrjciBqCX2K5P1UeV/OjuWJufE09OKf4ml2/S++RmBKI8TZLnPDV5f
gkihS9HhntxAyUneaU8oQcrPQuStb3dOJoJNC0oqY/pOQdI87UkeAyJEBxOOIIbo
rGaJIrV+bLQXMbgOlhjswW3Cd5zyU3j9ZpytRWd6GbY8AQuMOq5X+GHbpTTIlB8T
LMGxSQKBgQD+qA8TlJly5ctXUPSQNxyYDmln99uvOu66uzyf2Z/oZmfhNif2YrLp
cpVNhtcj/ZjCTJWcB+aFj8FKkdRrbNRYEUSbdy8C/qh+VCrDhEBTisoV/jXXNbGF
Ta8LOKw+aZmM6jze2283sQy+MnfnxlTtI3THbCpPeBk4I1eox06s4wKBgQDb979z
nXckOxFHceC6AkESIEGHDAaYpDTaMgRi+1LL9O8Bc5T2FjSajUxMccpHe5pIybXw
a3HJNHZiJjaN47Fr7y75+mpgx3fq0H4RXnjv/s78GJ5R7ezdci3D8vJJJhtG1fJH
oB+Ps4j1myTef4qcidAZUmBJAA8lFOiVq24P0wKBgA3D5SOnKuOdt/bhyAfLoK5F
99wbPE6pPVYzommBYpbwx1hIHdX3f0rjmV4i9t9Z0Ofodsop8MjzA4d9gRqQQtRT
9d7j2QcUrylsVVatM+jXEdes4FDSeExlEGF4r11R0PLcOqRDNnG2ixEzKRNygSGT
Nr6r5pyDCEg5QwI0SXEhAoGAHbmyFormljF+4CQlSZGaFzTKlbWEWdEAOSlaieqc
fG01DgizQ9l8uvB/7qeX4CV1ts8mbJjl3Otp8ZZ2Eyybb3NZYA0VS1k5t/KpQJ4Q
V8h81fV9LaqHyuXqgkNs2XPaLCq/4CplIUHGZmES0fWPRZYVM9qzEMioGcSOIhA/
Tj8CgYEAiNNmTC7dygJq3nFrP5voz9FqrgdHLemoryZpMNCAXJxUOUV2Q9L/qlGZ
ospsKD9Rc/B7VI2z66acLPiva0ijaumEkD6Fyq7rwR2gRKf2iKeBLrgN/A7RKadT
1YHF03yZB/SoBV5YYz/S/OS8rTxVhYnMOxQYw/Qla6Mz2OeigEs=
-----END RSA PRIVATE KEY-----
```