

### Deployment
kill pod
```
kubectl scale deployment project-caocao-cron --context=ali-cn-shenzhen --namespace=fleet-service-staging --replicas 0

kubectl delete deployment project-caocao-cron --context=ali-cn-shenzhen --namespace=fleet-service-staging
```

### Pod

```bash
# 根据 yaml 部署 Deployment
kubectl apply -f grafana.yaml

# 删除 Deployment
kubectl delete -f grafana.yaml

# 删除不在运行的pod
kubectl delete pod --context=gz --namespace=fleet-service-dev --field-selector=status.phase!=Running

```

### Secret

创建 secret
```
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
```
kubectl get secrets
kubectl describe secrets

```

解码
```
# 输出为文件
kubectl get secret db-user-pass -o jsonpath='{.data}'

# base64解码
echo 'UyFCXCpkJHpEc2I9' | base64 --decode

# 合并上面两步
kubectl get secret db-user-pass -o jsonpath='{.data.password}' | base64 --decode
```
