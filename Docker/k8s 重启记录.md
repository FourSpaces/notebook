# k8s 重启记录



### **环境、软件准备**

1、安装 ebtables ethtool，否则后边执行 `kubeadm init` 的时候会报错。

```
$ yum install ebtables ethtool
```

2、修改网络开启桥接网络支持，只针对（RHEL/CentOS 7）系统。

```
$ cat <<EOF >  /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sysctl --system

或者
$ vim /usr/lib/sysctl.d/00-system.conf  # 将 net.bridge.bridge-nf-call-iptables 值改成 1

# 然后修改当前内核状态
$ echo 1 > /proc/sys/net/bridge/bridge-nf-call-iptables
```

3、关闭 SELinux，目的为了允许容器能够与本机文件系统交互。

```
$ setenforce 0
$ systemctl daemon-reload
```

4、修改节点的 hostname，因为 kubernetes 是根据 hostname 来标示各节点的。

```
# Master 节点
$ echo "master.localdomain" > /etc/hostname 
$ echo "116.196.116.33   master.localdomain" >> /etc/hosts
$ sysctl kernel.hostname=master.localdomain # 不重启情况下使内核修改生效
```

```
# Node 节点
$ echo "node0.localdomain" > /etc/hostname 
$ echo "10.236.65.135   node0.localdomain" >> /etc/hosts
$ sysctl kernel.hostname=node0.localdomain # 不重启情况下使内核修改生效
```





### **软件安装配置**

我们知道 kubernetes 环境底层是依赖 Docker 的，所以这里软件安装包括了 Docker 安装， kubelet、kubeadm、kubectl 组件安装，以及一些初始化配置工作。

Master 和 Node 节点由于分工不一样，所以安装的服务不同，最终安装完毕，Master 和 Node 启动的核心服务分别如下：

| Master 节点             | Node 节点    |
| ----------------------- | ------------ |
| etcd-master             | kube-flannel |
| kube-apiserver          | kube-proxy   |
| kube-controller-manager | other apps   |
| kube-dns                |              |
| kube-flannel            |              |
| kube-proxy              |              |
| kube-scheduler          |              |

### 安装配置kubelet

```
# 配置 yum 源
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=http://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=0
repo_gpgcheck=0
gpgkey=http://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg
        http://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF

#设置完成后，安装kubelet、kubeadm、kubectl 组件
$ yum install -y kubelet kubeadm kubectl

# 设置开机启动，以及启动各组件
$ systemctl enable kubelet && systemctl start kubelet
```



### 要配置一下 kubelet，主要修改配置文件

```
vim /etc/systemd/system/kubelet.service.d/10-kubeadm.conf

[Service]
Environment="KUBELET_KUBECONFIG_ARGS=--kubeconfig=/etc/kubernetes/kubelet.conf --require-kubeconfig=true"
Environment="KUBELET_SYSTEM_PODS_ARGS=--pod-manifest-path=/etc/kubernetes/manifests --allow-privileged=true"
Environment="KUBELET_NETWORK_ARGS=--network-plugin=cni --cni-conf-dir=/etc/cni/net.d --cni-bin-dir=/opt/cni/bin"
Environment="KUBELET_DNS_ARGS=--cluster-dns=10.96.0.10 --cluster-domain=cluster.local"
Environment="KUBELET_AUTHZ_ARGS=--authorization-mode=Webhook --client-ca-file=/etc/kubernetes/pki/ca.crt"
Environment="KUBELET_CGROUP_ARGS=--cgroup-driver=systemd"
ExecStart=/usr/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_SYSTEM_PODS_ARGS $KUBELET_NETWORK_ARGS $KUBELET_DNS_ARGS $KUBELET_AUTHZ_ARGS $KUBELET_CGROUP_ARGS  $KUBELET_EXTRA_ARGS
```

修改完成之后，需要重新 reload 一下 kubelet 服务。

```
systemctl daemon-reload
```






### 配置启动kubelet

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

### 配置master节点 [ 在`master`节点操作 ]

```
# 1.11 版本 centos 下使用 ipvs 模式会出问题
# 参考 https://github.com/kubernetes/kubernetes/issues/65461

# 生成配置文件
cat >kubeadm-master.config<<EOF
apiVersion: kubeadm.k8s.io/v1alpha2
kind: MasterConfiguration
kubernetesVersion: v1.11.1
imageRepository: registry.cn-hangzhou.aliyuncs.com/google_containers
api:
  advertiseAddress: 11.11.11.111

controllerManagerExtraArgs:
  node-monitor-grace-period: 10s
  pod-eviction-timeout: 10s

networking:
  podSubnet: 10.244.0.0/16
  
kubeProxy:
  config:
    # mode: ipvs
    mode: iptables
EOF

# 提前拉取镜像
# 如果执行失败 可以多次执行
kubeadm config images pull --config kubeadm-master.config

# 初始化
kubeadm init --config kubeadm-master.config
```

结果

```
[root@JDu4e00u53f7 k8s]# kubeadm init --config kubeadm-master.config
[init] using Kubernetes version: v1.11.1
[preflight] running pre-flight checks
I0730 19:51:00.306142   17946 kernel_validator.go:81] Validating kernel version
I0730 19:51:00.306345   17946 kernel_validator.go:96] Validating kernel config
[preflight/images] Pulling images required for setting up a Kubernetes cluster
[preflight/images] This might take a minute or two, depending on the speed of your internet connection
[preflight/images] You can also perform this action in beforehand using 'kubeadm config images pull'
[kubelet] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[preflight] Activating the kubelet service
[certificates] Generated ca certificate and key.
[certificates] Generated apiserver certificate and key.
[certificates] apiserver serving cert is signed for DNS names [master.localdomain kubernetes kubernetes.default kubernetes.default.svc kubernetes.default.svc.cluster.local] and IPs [10.96.0.1 192.168.0.3]
[certificates] Generated apiserver-kubelet-client certificate and key.
[certificates] Generated sa key and public key.
[certificates] Generated front-proxy-ca certificate and key.
[certificates] Generated front-proxy-client certificate and key.
[certificates] Generated etcd/ca certificate and key.
[certificates] Generated etcd/server certificate and key.
[certificates] etcd/server serving cert is signed for DNS names [master.localdomain localhost] and IPs [127.0.0.1 ::1]
[certificates] Generated etcd/peer certificate and key.
[certificates] etcd/peer serving cert is signed for DNS names [master.localdomain localhost] and IPs [192.168.0.3 127.0.0.1 ::1]
[certificates] Generated etcd/healthcheck-client certificate and key.
[certificates] Generated apiserver-etcd-client certificate and key.
[certificates] valid certificates and keys now exist in "/etc/kubernetes/pki"
[kubeconfig] Wrote KubeConfig file to disk: "/etc/kubernetes/admin.conf"
[kubeconfig] Wrote KubeConfig file to disk: "/etc/kubernetes/kubelet.conf"
[kubeconfig] Wrote KubeConfig file to disk: "/etc/kubernetes/controller-manager.conf"
[kubeconfig] Wrote KubeConfig file to disk: "/etc/kubernetes/scheduler.conf"
[controlplane] wrote Static Pod manifest for component kube-apiserver to "/etc/kubernetes/manifests/kube-apiserver.yaml"
[controlplane] wrote Static Pod manifest for component kube-controller-manager to "/etc/kubernetes/manifests/kube-controller-manager.yaml"
[controlplane] wrote Static Pod manifest for component kube-scheduler to "/etc/kubernetes/manifests/kube-scheduler.yaml"
[etcd] Wrote Static Pod manifest for a local etcd instance to "/etc/kubernetes/manifests/etcd.yaml"
[init] waiting for the kubelet to boot up the control plane as Static Pods from directory "/etc/kubernetes/manifests" 
[init] this might take a minute or longer if the control plane images have to be pulled
[apiclient] All control plane components are healthy after 43.504499 seconds
[uploadconfig] storing the configuration used in ConfigMap "kubeadm-config" in the "kube-system" Namespace
[kubelet] Creating a ConfigMap "kubelet-config-1.11" in namespace kube-system with the configuration for the kubelets in the cluster
[markmaster] Marking the node master.localdomain as master by adding the label "node-role.kubernetes.io/master=''"
[markmaster] Marking the node master.localdomain as master by adding the taints [node-role.kubernetes.io/master:NoSchedule]
[patchnode] Uploading the CRI Socket information "/var/run/dockershim.sock" to the Node API object "master.localdomain" as an annotation
[bootstraptoken] using token: c8vlnr.0jcoje4n1twbz3d4
[bootstraptoken] configured RBAC rules to allow Node Bootstrap tokens to post CSRs in order for nodes to get long term certificate credentials
[bootstraptoken] configured RBAC rules to allow the csrapprover controller automatically approve CSRs from a Node Bootstrap Token
[bootstraptoken] configured RBAC rules to allow certificate rotation for all node client certificates in the cluster
[bootstraptoken] creating the "cluster-info" ConfigMap in the "kube-public" namespace
[addons] Applied essential addon: CoreDNS
[addons] Applied essential addon: kube-proxy

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

  kubeadm join 192.168.0.3:6443 --token c8vlnr.0jcoje4n1twbz3d4 --discovery-token-ca-cert-hash sha256:101b24b73e24dffca3561f5304961a4387e6cda6b187d5f78575322734f639e5


```



### 配置使用kubectl [在`master`节点操作]



```
rm -rf $HOME/.kube
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# 查看node节点
©

# 只有网络插件也安装配置完成之后，才能会显示为ready状态
# 设置master允许部署应用pod，参与工作负载，现在可以部署其他系统组件
# 如 dashboard, heapster, efk等
kubectl taint nodes --all node-role.kubernetes.io/master-


```

