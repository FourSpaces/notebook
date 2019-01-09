# kubernetes-bootcamp - 模块1

此交互式场景的目标是使用minikube部署本地开发Kubernetes群集
在线终端是一个预配置的Linux环境，可以用作常规控制台（可以键入命令）。

 点击后面跟着ENTER标记的代码块将在终端中执行该命令。



### 集群启动并运行

> 我们已经为您安装了minikube。 
> 通过运行minikube version命令检查它是否安装正确：

```
$ minikube version
minikube version: v0.26.0
```

> 好的，我们可以看到minikube已经到位。
>
> 运行minikube start命令启动集群

```
minikube start
```

> 大！ 您现在在您的在线终端中拥有一个正在运行的Kubernetes群集。 Minikube为你启动了一个虚拟机，并且一个Kubernetes集群现在正在该VM中运行。

### 群集版本

> 为了在这个训练营中与Kubernetes交互，我们将使用命令行界面kubectl。 我们将在下一个模块中详细解释kubectl，但现在我们只是看一些集群信息。 要检查是否安装了kubectl，您可以运行kubectl version命令：

```
kubectl version
```

> OK，kubectl已经配置完毕，我们可以看到客户端的版本以及服务器。 客户端版本是kubectl版本; 服务器版本是安装在主服务器上的Kubernetes版本。 您还可以查看有关构建的详细信息。



### 群集细节

> 我们来看看集群的细节。 我们将通过运行kubectl cluster-info来完成此操作：

 ```
kubectl cluster-info
 ```

> 我们有一个跑步大师和一个仪表板。 Kubernetes仪表板允许您在UI中查看您的应用程序。 在本教程中，我们将专注于部署和探索我们的应用程序的命令行。 要查看集群中的节点，请运行kubectl get nodes命令：

```
kubectl get nodes
```

> 该命令显示可用于托管我们的应用程序的所有节点。 现在我们只有一个节点，并且我们可以看到它的状态已准备好（它已准备好接受要部署的应用程序）。





## 



## 下载 kubectl

```
wget https://dl.k8s.io/v1.9.0/kubernetes-client-linux-amd64.tar.gz
tar -xzvf kubernetes-client-linux-amd64.tar.gz
cp kubernetes/client/bin/kube* /usr/bin/
chmod a+x /usr/bin/kube*
```



```
wget https://github.com/kubernetes/kubernetes/releases/download/v1.10.2/kubernetes.tar.gz

tar -xzvf kubernetes-client-linux-amd64.tar.gz
```





