# Redis 实战

初始化 redis server 进程

```bash
# Ubuntu 下安装
sudo apt install redis-server

# 管理 redis 守护进程
sudo systemctl status redis-server

# 设置开机启动
sudo systemctl enable redis-server

# 命令行
redic-cli
```

设置密码

```bash
requirepass yourpassword
sudo systemctl restart redis
redis-cli -a yourpassword
```