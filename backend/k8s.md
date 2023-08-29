

kill pod
```
kubectl scale deployment project-caocao-cron --context=ali-cn-shenzhen --namespace=fleet-service-staging --replicas 0

kubectl delete deployment project-caocao-cron --context=ali-cn-shenzhen --namespace=fleet-service-staging
```

---

docker 清除缓存
```
docker system prune -a
```