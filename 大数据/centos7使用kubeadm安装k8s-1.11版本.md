# centos7使用kubeadm安装k8s-1.11版本

### 环境说明

#### 组织结构

```
lab1: master 172.16.17.120
lab2: node 172.16.17.141
lab3: node 172.16.17.142
```

### 关闭防火墙

```
systemctl stop firewalld
systemctl disable firewalld
```

### 安装配置docker

> v1.11.0版本推荐使用docker v17.03,  如下操作在所有节点操作

#### 安装docker

```
# 卸载安装指定版本docker-ce
yum remove -y docker-ce docker-ce-selinux container-selinux
yum install -y --setopt=obsoletes=0 \
docker-ce-17.03.1.ce-1.el7.centos \
docker-ce-selinux-17.03.1.ce-1.el7.centos
```

#### 启动docker

```
systemctl enable docker && systemctl restart docker
```

### 安装 kubeadm, kubelet 和 kubectl

> 如下操作在所有节点操作

#### 使用阿里镜像安装

```
# 配置源
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF

# 安装
yum install -y kubelet-1.11.2 kubeadm-1.11.2 kubectl-1.11.2 ipvsadm
```

### 配置系统相关参数

```
# 临时禁用selinux
# 永久关闭 修改/etc/sysconfig/selinux文件设置
sed -i 's/SELINUX=permissive/SELINUX=disabled/' /etc/sysconfig/selinux
setenforce 0

# 临时关闭swap
# 永久关闭 注释/etc/fstab文件里swap相关的行
swapoff -a

# 开启forward
# Docker从1.13版本开始调整了默认的防火墙规则
# 禁用了iptables filter表中FOWARD链
# 这样会引起Kubernetes集群中跨Node的Pod无法通信

iptables -P FORWARD ACCEPT

# 配置转发相关参数，否则可能会出错
cat <<EOF >  /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
vm.swappiness=0
EOF
sysctl --system

# 加载ipvs相关内核模块
# 如果重新开机，需要重新加载， 敲黑板，划重点
modprobe ip_vs
modprobe ip_vs_rr
modprobe ip_vs_wrr
modprobe ip_vs_sh
modprobe nf_conntrack_ipv4
lsmod | grep ip_vs
```

## 修改各节点的hostname

```

```



### 配置hosts解析

> 如下操作在所有节点操作

```
cat >>/etc/hosts<<EOF
172.16.17.120 lab1
172.16.17.141 lab2
172.16.17.142 lab3
EOF
```

### 配置启动kubelet

> 如下操作在所有节点操作

```
# 配置kubelet使用国内pause镜像
# 配置kubelet的cgroups
# 获取docker的cgroups
DOCKER_CGROUPS=$(docker info | grep 'Cgroup' | cut -d' ' -f3)
echo $DOCKER_CGROUPS
cat >/etc/sysconfig/kubelet<<EOF
KUBELET_EXTRA_ARGS="--cgroup-driver=$DOCKER_CGROUPS --pod-infra-container-image=registry.cn-hangzhou.aliyuncs.com/google_containers/pause-amd64:3.1"
EOF

# 启动
systemctl daemon-reload
systemctl enable kubelet && systemctl start kubelet
```

### 配置master节点

> 如下操作在`master`节点操作

```
# 1.11.0 版本 centos 下使用 ipvs 模式会出问题
# 参考 https://github.com/kubernetes/kubernetes/issues/65461

# 生成配置文件
cat >kubeadm-master.config<<EOF
apiVersion: kubeadm.k8s.io/v1alpha2
kind: MasterConfiguration
kubernetesVersion: v1.11.2
imageRepository: registry.cn-hangzhou.aliyuncs.com/google_containers
api:
  # 这里设置为 master 的ip地址
  advertiseAddress: 172.31.53.104

controllerManagerExtraArgs:
  node-monitor-grace-period: 10s
  pod-eviction-timeout: 10s

networking:
  podSubnet: 10.244.0.0/16
  
kubeProxy:
  config:
    mode: ipvs
    # mode: iptables
EOF

# 提前拉取镜像
# 如果执行失败 可以多次执行
kubeadm config images pull --config kubeadm-master.config

# 初始化
kubeadm init --config kubeadm-master.config
```

这里会输出 kubeadm join的信息，请保留下来

例子如下：

```
Your Kubernetes master has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

You can now join any number of machines by running the following on each node
as root:

  kubeadm join 172.16.17.120:6443 --token 6owacm.6riuvjx5xscf2bn9 --discovery-token-ca-cert-hash sha256:d4582e162fe758d11a540bfde1a36f6ecf785837cd2feba80852d108a5baacce
```



注意： 如果初始化，或者配置出现问题，请重置

```
kubeadm reset
```



### 配置使用kubectl

> 如下操作在`master`节点操作

```
rm -rf $HOME/.kube
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# 查看node节点
kubectl get nodes

# 只有网络插件也安装配置完成之后，才能会显示为ready状态
# 设置master允许部署应用pod，参与工作负载，现在可以部署其他系统组件
# 如 dashboard, heapster, efk等
kubectl taint nodes --all node-role.kubernetes.io/master-
```

### 配置使用网络插件

> 如下操作在`master`节点操作

```
# 下载配置
mkdir flannel && cd flannel
wget https://raw.githubusercontent.com/coreos/flannel/v0.10.0/Documentation/kube-flannel.yml

# 修改配置
# 此处的ip配置要与上面kubeadm的pod-network一致
  net-conf.json: |
    {
      "Network": "10.244.0.0/16",
      "Backend": {
        "Type": "vxlan"
      }
    }

# 修改镜像
image: registry.cn-shanghai.aliyuncs.com/gcr-k8s/flannel:v0.10.0-amd64

# 如果Node有多个网卡的话，参考flannel issues 39701，
# https://github.com/kubernetes/kubernetes/issues/39701
# 目前需要在kube-flannel.yml中使用--iface参数指定集群主机内网网卡的名称，
# 否则可能会出现dns无法解析。容器无法通信的情况，需要将kube-flannel.yml下载到本地，
# flanneld启动参数加上--iface=<iface-name>
# iface 的值为 上面设置的IP地址所在的网卡，这里为eth1
    containers:
      - name: kube-flannel
        image: registry.cn-shanghai.aliyuncs.com/gcr-k8s/flannel:v0.10.0-amd64
        command:
        - /opt/bin/flanneld
        args:
        - --ip-masq
        - --kube-subnet-mgr
        - --iface=eth1

# 启动
kubectl apply -f kube-flannel.yml

# 查看
kubectl get pods --namespace kube-system
kubectl get svc --namespace kube-system
```



### 配置node节点加入集群

> 如下操作在所有`node`节点操作

```
# 此命令为初始化master成功后返回的结果
kubeadm join 172.16.17.120:6443 --token 6owacm.6riuvjx5xscf2bn9 --discovery-token-ca-cert-hash sha256:d4582e162fe758d11a540bfde1a36f6ecf785837cd2feba80852d108a5baacce
```

### 测试容器间的通信和DNS

> 配置好网络之后，kubeadm会自动部署coredns

### 小技巧

**忘记初始master节点时的node节点加入集群命令怎么办**

```
# 简单方法
kubeadm token create --print-join-command

# 第二种方法
token=$(kubeadm token generate)
kubeadm token create $token --print-join-command --ttl=0
```



## 配置 Web UI (Dashboard)

找到目录，这里以用户根目录为准：

```
cd ~
mkdir  dashboard
cd dashboard
wget https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard.yaml
```

修改 kubernetes-dashboard.yaml 文件

- 将 image 的地址 修改为

```
image: registry.cn-hangzhou.aliyuncs.com/google_containers/kubernetes-dashboard-amd64:v1.10.0
```

- 添加账号 和绑定角色

```

apiVersion: v1
kind: ServiceAccount
metadata:
  name: admin-user
  namespace: kube-system

--
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRoleBinding
metadata:
  name: admin-user
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: admin-user
  namespace: kube-system
```

执行

```
kubectl apply -f kubernetes-dashboard.yaml
```

### 获取Token

```
kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep admin-user | awk '{print $1}')
```

```
Name:         admin-user-token-qrj82
Namespace:    kube-system
Labels:       <none>
Annotations:  kubernetes.io/service-account.name=admin-user
              kubernetes.io/service-account.uid=6cd60673-4d13-11e8-a548-00155d000529

Type:  kubernetes.io/service-account-token

Data
====
token:      eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLXFyajgyIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiI2Y2Q2MDY3My00ZDEzLTExZTgtYTU0OC0wMDE1NWQwMDA1MjkiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06YWRtaW4tdXNlciJ9.C5mjsa2uqJwjscWQ9x4mEsWALUTJu3OSfLYecqpS1niYXxp328mgx0t-QY8A7GQvAr5fWoIhhC_NOHkSkn2ubn0U22VGh2msU6zAbz9sZZ7BMXG4DLMq3AaXTXY8LzS3PQyEOCaLieyEDe-tuTZz4pbqoZQJ6V6zaKJtE9u6-zMBC2_iFujBwhBViaAP9KBbE5WfREEc0SQR9siN8W8gLSc8ZL4snndv527Pe9SxojpDGw6qP_8R-i51bP2nZGlpPadEPXj-lQqz4g5pgGziQqnsInSMpctJmHbfAh7s9lIMoBFW7GVE8AQNSoLHuuevbLArJ7sHriQtDB76_j4fmA
ca.crt:     1025 bytes
namespace:  11 bytes
```

## 访问

### API Server

如果Kubernetes API服务器是公开的，并可以从外部访问，那我们可以直接使用API Server的方式来访问，也是比较推荐的方式。

对于API Server来说，它是使用证书进行认证的，我们需要先创建一个证书：

1.首先找到`kubectl`命令的配置文件，默认情况下为`/etc/kubernetes/admin.conf`，在上面，我们已经复制到了`$HOME/.kube/config`中。

2.然后我们使用`client-certificate-data`和`client-key-data`生成一个*p12*文件，可使用下列命令：

```
# 生成client-certificate-data
grep 'client-certificate-data' ~/.kube/config | head -n 1 | awk '{print $2}' | base64 -d >> kubecfg.crt

# 生成client-key-data
grep 'client-key-data' ~/.kube/config | head -n 1 | awk '{print $2}' | base64 -d >> kubecfg.key

# 生成p12，这里会让输入两次密码一样的秘密，这里我输入123456，
# 一会安装证书会用到
openssl pkcs12 -export -clcerts -inkey kubecfg.key -in kubecfg.crt -out kubecfg.p12 -name "kubernetes-client"
```

3.最后导入上面生成的p12文件，重新打开浏览器：

```
https://172.16.17.120:6443/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/
```

使用刚才获取到的token 进行登录

## 集成Heapster

Heapster是容器集群监控和性能分析工具，天然的支持Kubernetes和CoreOS。

Heapster支持多种储存方式，本示例中使用`influxdb`，直接执行下列命令即可：

```
kubectl create -f http://mirror.faasx.com/kubernetes/heapster/deploy/kube-config/influxdb/influxdb.yaml
kubectl create -f http://mirror.faasx.com/kubernetes/heapster/deploy/kube-config/influxdb/grafana.yaml
kubectl create -f http://mirror.faasx.com/kubernetes/heapster/deploy/kube-config/influxdb/heapster.yaml
kubectl create -f http://mirror.faasx.com/kubernetes/heapster/deploy/kube-config/rbac/heapster-rbac.yaml
```



### 测试容器间的通信和DNS

> 配置好网络之后，kubeadm会自动部署coredns

#### 启动

```
kubectl run nginx --replicas=2 --image=nginx:alpine --port=80
kubectl expose deployment nginx --type=NodePort --name=example-service-nodeport
kubectl expose deployment nginx --name=example-service
```

#### 查看状态

```
kubectl get deploy
kubectl get pods
kubectl get svc
kubectl describe svc example-service
```

#### DNS解析

```
kubectl run curl --image=radial/busyboxplus:curl -i --tty
nslookup kubernetes
nslookup example-service
curl example-service
```

#### 访问测试

```
# 10.96.59.56 为查看svc时获取到的clusterip
curl "10.96.59.56:80"

# 32223 为查看svc时获取到的 nodeport
http://11.11.11.112:32223/
http://11.11.11.113:32223/
```

#### 清理删除

```
kubectl delete svc example-service example-service-nodeport
kubectl delete deploy nginx curl
```

### 小技巧

**忘记初始master节点时的node节点加入集群命令怎么办**

```
# 简单方法
kubeadm token create --print-join-command

# 第二种方法
token=$(kubeadm token generate)
kubeadm token create $token --print-join-command --ttl=0
```

### 

参考：

https://www.qikqiak.com/post/use-kubeadm-install-kubernetes-1.10/

https://cloud.tencent.com/developer/article/1010569

https://my.oschina.net/hgfdoing/blog/2249596

https://www.maogx.win/posts/32/

https://www.ctolib.com/docs/sfile/kubernetes-handbook/practice/dashboard-addon-installation.html