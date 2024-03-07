argo 是一个 CI/CD 的工具，主要用来部署。

## 1. argo workflow

工作流用到的常用命令
- **argo submit** 提交一个 argo workflow。
  - `argo submit xx.yaml --context gz -n infra-dev workflow`
- **argo list** 查看所有的工作流
  - `argo list --context gz -n infra-dev`
- **argo logs** 查看日志
  - 这个命令会阶段长的日志，建议用 `kubectl log` 查看。
- **argo stop** 停止工作流
  - `argo stop --context gz -n infra-dev {workflow-1} {workflow-2}`
- **argo terminate** 终止工作流
  - `argo terminate --context gz -n infra-dev {workflow-1} {workflow-2}`

## 2. workflow template
工作流模板指的是带参数的工作流，类似 jenkins jobs，可以输入参数后执行。

1. 创建模板：`k8s apply xx/workflow.yaml.jsonnet --context gz -n infra-dev`
2. 从模板提交工作流 `k8s submit_workflow_from_template --workflow-template command-worker -p command='echo my job' --context gz -n infra-dev`
3. 列出工作流模板：`kubectl get workflowtemplate --context gz -n infra-dev`
4. 删除模板 `kubectl delete workflowtemplate --context gz -n infra-dev`

## 3. cron workflow
定时工作流
1. 列出定时工作流：`kubectl get cronworkflow --context gz -n infra-dev` 
2. 描述定时工作流：`kubectl describe cronworkflow ci-flow0 --context gz -n infra-dev`
3. 删除定时工作流：`kubectl delete cronworkflow ci-flow0 --context gz -n infra-dev`

## 4. Github hook
查看从 github 触发的工作流：
```bash
kubectl --context sjc1 -n infra-offline-prod logs \
    --selector=app=github-hook-consumer --tail=5000 | grep workflow_template=pr-unit-test
```