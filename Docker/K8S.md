



## 1.准备

### 1.1系统配置

在安装之前，需要先做如下准备。两台CentOS 7.4主机如下：

```
cat /etc/hosts
192.168.61.11 node1
192.168.61.12 node2

cat /etc/hosts 119.29.185.209 node1
```

如果各个主机启用了防火墙，需要开放Kubernetes各个组件所需要的端口，可以查看[Installing kubeadm](https://kubernetes.io/docs/setup/independent/install-kubeadm/)中的”Check required ports”一节。 这里简单起见在各节点禁用防火墙：

```
systemctl stop firewalld
systemctl disable firewalld
```

禁用SELINUX：

```
setenforce 0
```

```
vi /etc/selinux/config
SELINUX=disabled
```

创建/etc/sysctl.d/k8s.conf文件，添加如下内容：

```
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
```

执行命令使修改生效。

```
modprobe br_netfilter
sysctl -p /etc/sysctl.d/k8s.conf
```

### 1.2安装Docker

```
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```

查看当前的Docker版本：

```
yum list docker-ce.x86_64  --showduplicates |sort -r
docker-ce.x86_64            18.03.0.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.12.1.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.12.0.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.09.1.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.09.0.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.06.2.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.06.1.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.06.0.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.03.2.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.03.1.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.03.0.ce-1.el7.centos             docker-ce-stable
```

Kubernetes 1.10已经针对Docker的1.11, 1.12, 1.13.1和17.03等版本做了验证，需要注意Kubernetes 1.10最低支持的Docker版本是1.11。 我们这里在各节点安装docker的17.03.2版本。

```
yum makecache fast

yum install -y --setopt=obsoletes=0 \
  docker-ce-17.03.2.ce-1.el7.centos \
  docker-ce-selinux-17.03.2.ce-1.el7.centos

systemctl start docker
systemctl enable docker
```

Docker从1.13版本开始调整了默认的防火墙规则，禁用了iptables filter表中FOWARD链，这样会引起Kubernetes集群中跨Node的Pod无法通信，在各个Docker节点执行下面的命令：

```
iptables -P FORWARD ACCEPT
```

可在docker的systemd unit文件中以ExecStartPost加入上面的命令：

```
ExecStartPost=/usr/sbin/iptables -P FORWARD ACCEPT
systemctl daemon-reload
systemctl restart docker
```





