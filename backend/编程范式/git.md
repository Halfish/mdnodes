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

## stash（储藏）
可以暂时把当前分支的修改存储起来。

```bash
# 假设当前已经有了一些修改，包括已经 git add 的文件。
# 存储当前状态
git stash

# 查看素有的stash
git stash list

# 应用和删除第一个stash
git stash pop

# 移除 stash
git stash drop stash@{0}
git stash clear

# 查看 diff
git stash show
```