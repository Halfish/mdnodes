
官方主页：https://kubernetes.io/

Kubernetes, k8s, 是一个便捷的，可扩展的开源平台，用来管理容器化的工作负荷和服务。中间的 8 表示省略的字母的数量

工具：
- kubectl，Kubernetes command-line tool，用来管理 k8s 集群。
- 文档：https://kubectl.docs.kubernetes.io/references/kubectl/
- 文档：https://kubernetes.io/docs/reference/kubectl/overview/

运维一般有三种运行应用的模式，第一种是运行在物理机上。第二种是用虚拟机；第三种是容器，比虚拟机更加轻量。k8s是管理容器的工具。

### 1. Deployment

如何删除 deployment？

```bash
kubectl scale deployment project-caocao-cron --context=ali-cn-shenzhen --namespace=fleet-service-staging --replicas 0

kubectl delete deployment project-caocao-cron --context=ali-cn-shenzhen --namespace=fleet-service-staging
```

### 2. Service

Service 为不同的多个 pod 提供同一的对外 IP，并自动做负载均衡。

### 3. Pod

```bash
# 根据 yaml 部署 Deployment
kubectl apply -f grafana.yaml

# 删除 Deployment
kubectl delete -f grafana.yaml

# 删除不在运行的pod
kubectl delete pod --context=gz --namespace=fleet-service-dev --field-selector=status.phase!=Running

```

### 4. Secret

创建 secret
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

查看
```bash
kubectl get secrets
kubectl describe secrets

```

解码
```bash
# 输出为文件
kubectl get secret db-user-pass -o jsonpath='{.data}'

# base64解码
echo 'UyFCXCpkJHpEc2I9' | base64 --decode

# 合并上面两步
kubectl get secret db-user-pass -o jsonpath='{.data.password}' | base64 --decode
```

### 5. Ingress
Ingress 用来通信
