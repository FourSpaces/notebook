# k8s 命令



### 命名空间

```
# 查询
kubectl get namespaces

# 列出所有命名空间
get namespaces --show-labels

# 创建命名空间 yaml，development 替换为你的命名空间名字
apiVersion: v1
kind: Namespace
metadata:
   name: development
   labels:
     name: development

# 创建命名空间 json, development 替换为你的命名空间名字
{
  "kind": "Namespace",
  "apiVersion": "v1",
  "metadata": {
    "name": "development",
    "labels": {
      "name": "development"
    }
  }
}

# Pod/RC/Service中指定Namespace，如果不指定Namespace，则默认是"default"的Namespace

```

Kubernetes命名空间为集群中的Pods，Services和Deployments提供了适用范围。

### Deployment

