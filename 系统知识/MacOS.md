


## Brew

**替换国内源**

1. 第一步，替换 git 仓库：
```bash
# 替换 brew.git 的地址
git -C "$(brew --repo)" remote set-url origin https://mirrors.ustc.edu.cn/brew.git
```

2. 第二步，编辑 `~/.zshrc` 配置 HomeBrew bottles 镜像。
```bash
# 中科大镜像
export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles
```

3. 第三步、更新和验证
```bash
source ~/.zshrc
brew update
```
