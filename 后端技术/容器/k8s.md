官方主页：https://kubernetes.io/

Kubernetes, k8s, 是一个便捷的，可扩展的开源平台，用来管理容器化的工作负荷和服务。中间的 8 表示省略的字母的数量

工具：

- kubectl，Kubernetes command-line tool，用来管理 k8s 集群。
- 文档：https://kubectl.docs.kubernetes.io/references/kubectl/
- 文档：https://kubernetes.io/docs/reference/kubectl/overview/

运维一般有三种运行应用的模式，第一种是运行在物理机上。第二种是用虚拟机；第三种是容器，比虚拟机更加轻量。k8s 是管理容器的工具。

## 安装

安装 kubectl 工具，可以参考官方文档：https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
```

安装 k3s，可以参考官方文档：https://k3s.io/

```bash
curl -sfL https://get.k3s.io | sh -
```

安装 minikube，可以参考官方文档：https://minikube.sigs.k8s.io/docs/start/

```bash
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```

minikube 包含图像化的 dashboard，方便查看集群状态。

安装 kind (K8s In Docker)，可以参考官方文档：https://kind.sigs.k8s.io/docs/user/quick-start/

```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.30.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

## API Resources（API 资源）

```bash
# 查看当前支持的各种资源，以及 API 版本号
kubectl api-resources
```

### Pod

Pod 是 Kubernetes 中最小的部署单元，一个 Pod 可以包含一个或多个容器。

```bash
# 根据 yaml 部署 Deployment
kubectl apply -f grafana.yaml

# 删除 Deployment
kubectl delete -f grafana.yaml

# 删除不在运行的pod
kubectl delete pod --context=gz --namespace=fleet-service-dev --field-selector=status.phase!=Running
```

### Volume

Volume 是 Kubernetes 中的一种抽象，用于持久化存储数据。Volume 可以被多个 Pod 共享，也可以被单个 Pod 使用。

```bash
# 查看 volume
kubectl get pv <pv-name> -o yaml
kubectl describe pv <pv-name>
```

### PersistentVolumeClaim

PersistentVolumeClaim (PVC) 是用户对存储资源的一种声明，它请求特定大小和访问模式的存储卷。

```bash
# 查看 pvc
kubectl get pvc
kubectl describe pvc <pvc-name>

# 查看 pvc 的详细信息
kubectl get pvc <pvc-name> -o yaml
```

### Secret

Secret 用来存储敏感信息，比如密码、token 等。这些信息会被加密存储，然后通过环境变量或者挂载到容器中，供容器使用。

**创建 secret**

```bash
# 从原始数据创建
kubectl create secret generic db-user-pass \
    --from-literal=username=admin \
    --from-literal=password='S!B\*d$zDsb='

# 从文件创建
kubectl create secret generic db-user-pass \
--from-file=./username.txt \
--from-file=./password.txt
```

**查看**

```bash
kubectl get secrets
kubectl describe secrets
```

**解码**

```bash
# 输出为文件
kubectl get secret db-user-pass -o jsonpath='{.data}'

# base64解码
echo 'UyFCXCpkJHpEc2I9' | base64 --decode

# 合并上面两步
kubectl get secret db-user-pass -o jsonpath='{.data.password}' | base64 --decode
```

### ConfigMap

ConfigMap 用于存储配置数据，可以被 Pod 作为环境变量或者挂载到容器中，供容器使用。

```bash
# 创建 configmap
kubectl create configmap game-config --from-file=game.properties

# 操作 configmap
kubectl get/describe/delete/edit configmap game-config
```

### Deployment

Deployment 控制 Pod 的数量和状态，确保指定数量的 Pod 正常运行。

```bash
# 删除 deployment
kubectl scale deployment project-caocao-cron --context=ali-cn-shenzhen --namespace=fleet-service-staging --replicas 0
kubectl delete deployment project-caocao-cron --context=ali-cn-shenzhen --namespace=fleet-service-staging
```

### Service

Service 为不同的多个 pod 提供同一的对外 IP，并自动做负载均衡。

### Ingress

Ingress 是一种 API 对象，用于管理对集群中服务的外部访问，通常通过 HTTP/HTTPS 路由流量。

Ingress 可以提供负载均衡、SSL 终止和基于名称的虚拟主机等功能。

它允许你将多个服务暴露给外部网络，而不需要为每个服务配置单独的负载均衡器。

Ingress 通常需要配合 Ingress Controller 使用，Ingress Controller 是一个实际处理请求的软件，它根据 Ingress 规则来路由流量。

常见的 Ingress Controller 有 NGINX Ingress Controller、Traefik 等。

```bash
# 查看 ingress
kubectl get ingress
kubectl describe ingress

# 查看 ingress controller
kubectl get pods -n ingress-nginx
kubectl describe pods -n ingress-nginx <pod-name>

# 查看 ingress controller 日志
kubectl logs -n ingress-nginx <pod-name>

# 查看 ingress controller 配置
kubectl exec -it -n ingress-nginx <pod-name> -- cat /etc/nginx/nginx.conf
```
