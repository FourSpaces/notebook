

```
# Master 节点
$ echo "master.localdomain" > /etc/hostname 
$ echo "10.236.65.125   master.localdomain" >> /etc/hosts
$ sysctl kernel.hostname=master.localdomain # 不重启情况下使内核修改生效
```



```
# Node 节点
$ echo "node0.localdomain" > /etc/hostname 
$ echo "10.236.65.135   node0.localdomain" >> /etc/hosts
$ sysctl kernel.hostname=node0.localdomain # 不重启情况下使内核修改生效
```





配置好各节点hosts文件

关闭系统防火墙

```
systemctl stop firewalld
systemctl disable firewalld
```



关闭SElinux

```
setenforce 0

vim /etc/selinux/config
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

关闭swap

```
swapoff -a
```

5.配置系统内核参数使流过网桥的流量也进入iptables/netfilter框架中，在/etc/sysctl.conf中添加以下配置

```
net.bridge.bridge-nf-call-iptables = 1
net.bridge.bridge-nf-call-ip6tables = 1
sysctl -p
```



## 使用阿里云yum镜像

配置yum源，由于google被墙，可以使用阿里云搭建的yum源

```
#docker yum源
cat >> /etc/yum.repos.d/docker.repo <<EOF
[docker-repo]
name=Docker Repository
baseurl=http://mirrors.aliyun.com/docker-engine/yum/repo/main/centos/7
enabled=1
gpgcheck=0
EOF

#kubernetes yum源
cat >> /etc/yum.repos.d/kubernetes.repo <<EOF
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/
enabled=1
gpgcheck=0
EOF
```



安装Docker

```
sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
  
yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
    
yum install docker-ce-17.03.2.ce

sudo yum install -y --setopt=obsoletes=0 \
     docker-ce-17.03.2.ce \
     docker-ce-selinux-17.03.2.ce
```

kubernetes安装：

```
#查看版本
yum list kubeadm –showduplicates
yum list kubernetes-cni –showduplicates
yum list kubelet –showduplicates
yum list kubectl –showduplicates
#安装软件
yum install -y kubernetes-cni-0.6.0-0.x86_64 kubelet-1.10.0-0.x86_64 kubectl-1.10.0-0.x86_64 kubeadm-1.10.0-0.x86_64
```

启动Docker 与 kubelet 服务

```
systemctl enable docker && systemctl start docker
systemctl enable kubelet && systemctl start kubelet
```

下载 K8S镜像

```
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://u0f6ag2l.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```





```
#!/bin/bash
images=(kube-proxy-amd64:v1.10.0 kube-scheduler-amd64:v1.10.0 kube-controller-manager-amd64:v1.10.0 kube-apiserver-amd64:v1.10.0
etcd-amd64:3.1.12 pause-amd64:3.1 kubernetes-dashboard-amd64:v1.8.3 k8s-dns-sidecar-amd64:1.14.8 k8s-dns-kube-dns-amd64:1.14.8
k8s-dns-dnsmasq-nanny-amd64:1.14.8)
for imageName in ${images[@]} ; do
  docker pull keveon/$imageName
  docker tag keveon/$imageName k8s.gcr.io/$imageName
  docker rmi keveon/$imageName
done
```



## 配置 kubelet

安装完成后，我们还需要对`kubelet`进行配置，因为用`yum`源的方式安装的`kubelet`生成的配置文件将参数`--cgroup-driver`改成了`systemd`，而`docker`的`cgroup-driver`是`cgroupfs`，这二者必须一致才行，我们可以通过`docker info`命令查看：

```
$ docker info |grep Cgroup
Cgroup Driver: cgroupfs
```

修改文件`kubelet`的配置文件`/etc/systemd/system/kubelet.service.d/10-kubeadm.conf`，将其中的`KUBELET_CGROUP_ARGS`参数更改成`cgroupfs`：

```
Environment="KUBELET_CGROUP_ARGS=--cgroup-driver=cgroupfs"
```

另外还有一个问题是关于交换分区的，之前我们在[手动搭建高可用的kubernetes 集群](https://blog.qikqiak.com/post/manual-install-high-available-kubernetes-cluster/)一文中已经提到过，`Kubernetes`从1.8开始要求关闭系统的 Swap ，如果不关闭，默认配置的`kubelet`将无法启动，我们可以通过 kubelet 的启动参数`--fail-swap-on=false`更改这个限制，所以我们需要在上面的配置文件中增加一项配置(在`ExecStart`之前)：

```
Environment="KUBELET_EXTRA_ARGS=--fail-swap-on=false"
```

当然最好的还是将`swap`给关掉，这样能提高`kubelet`的性能。修改完成后，重新加载我们的配置文件即可：

```
$ systemctl daemon-reload
```



初始化kubeadm 

```

# 清除etcd 目录
rm -rf /var/lib/etcd/*
# 清除 manifests 目录
 rm -rf /etc/kubernetes/manifests/*.yaml
 kubeadm reset

kubeadm init \
	--kubernetes-version=v1.10.0 \
	--pod-network-cidr=10.244.0.0/16 \
	--apiserver-advertise-address=master.k8s.samwong.im
```

```
kubeadm init \
  --kubernetes-version=v1.10.0 \
  --pod-network-cidr=10.244.0.0/16 \
  --ignore-preflight-errors= Swap \
  --apiserver-advertise-address=116.196.116.33
  
```





```
Your Kubernetes master has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

   Mkdir -p $HOME/.kube
   Sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
   Sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
   Https://kubernetes.io/docs/concepts/cluster-administration/addons/

You can now join any number of machines by running the following on each node
As root:

   kubeadm join 116.196.116.33:6443 --token 1ilcgw.5dcjem9zigcx9r6y --discovery-token-ca-cert-hash sha256:32a4cc6c615e25c68d35cbe7aa939c917c62a8bf12554795772bbd53a42bbc2b --ignore-preflight-errors=Swap
```



```
您的Kubernetes主人已成功初始化！

要开始使用群集，您需要以普通用户身份运行以下内容：

   Mkdir -p $HOME/.kube
   Sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
   Sudo chown $(id -u):$(id -g) $HOME/.kube/config
   
您现在应该将pod网络部署到群集。
使用下列选项之一运行“kubectl apply -f [podnetwork] .yaml”：
Https://kubernetes.io/docs/concepts/cluster-administration/addons/

您现在可以通过在每个节点上运行以下内容来加入任意数量的计算机
作为根：

kubeadm join 116.196.116.33:6443 --token 1ilcgw.5dcjem9zigcx9r6y --discovery-token-ca-cert-hash sha256：32a4cc6c615e25c68d35cbe7aa939c917c62a8bf12554795772bbd53a42bbc2b --ignore-preflight-errors=Swap
[preflight] Running pre-flight checks.  
```

