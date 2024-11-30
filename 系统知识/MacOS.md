

## 安装 Brew

需要用国内的镜像环境来安装，参考[Homebrew中文网](https://brew.idayer.com/)：

```bash
export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.ustc.edu.cn/brew.git"
export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/homebrew-core.git"
export HOMEBREW_API_DOMAIN="https://mirrors.ustc.edu.cn/homebrew-bottles/api"
export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.ustc.edu.cn/homebrew-bottles/bottles"

/bin/bash -c "$(curl -fsSL https://gitee.com/ineo6/homebrew-install/raw/master/install.sh)"
```


## 替换 Brew 源

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
