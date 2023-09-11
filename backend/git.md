# Git



## 分支 Branch

### 删除分支
```bash
# 删除本地分支，不能在要删除的分支上操作，且分支必须得提交到远程
git branch -d <branch_name>

# 强制删除本地分支，不需要被推送或者合并
git branch -D <branch_name>

# 删除远程分支
git push origin --delete origin/fix_02

# 删除以后，同步列表（远程已删除的分支不会再显示，但是本地的还在）
git fetch -p(--prune)
```
