

kill pod
```
kubectl scale deployment project-caocao-cron --context=ali-cn-shenzhen --namespace=fleet-service-staging --replicas 0

kubectl delete deployment project-caocao-cron --context=ali-cn-shenzhen --namespace=fleet-service-staging
```

---

```bash
# 根据 yaml 部署 Deployment
kubectl apply -f grafana.yaml

# 删除 Deployment
kubectl delete -f grafana.yaml

# 删除不在运行的pod
kubectl delete pod --context=gz --namespace=fleet-service-dev --field-selector=status.phase!=Running

```
