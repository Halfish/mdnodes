# v2ray

## 链接
v2ray / v2fly

- 源码：https://github.com/v2fly/v2ray-core
- 官网：https://www.v2fly.org/
- 教程: https://itlanyan.com/v2ray-tutorial/
- 新V2Ray白话文指南：https://guide.v2fly.org/

其他用到的一些链接：
- VULTR: https://www.vultr.com/


## 安装 v2ray

```bash
# 下载安装脚本
curl -O https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh

# 执行安装
sudo bash install-release.sh

# 启动服务
sudo systemctl start/enable/status/stop v2ray
```


## 运行 v2ray

v2ray 需要下面几种链路：
1. v2ray server，配置 inbound / outbound 协议；
2. v2ray client，配置 inbound / outbound 协议；
3. chrome 插件，如 SwitchyOmega

流量路径：
浏览器 -> `client inbound` -> `client outbound` -> `server inbound` -> `server outbound`


## 配置防火墙
配置防火墙，把 vmess 端口加入规则。
```bash
sudo ufw allow 16823
sudo ufw status
```

结果为：
```bash
➜  sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere
16823                      ALLOW       Anywhere
22/tcp (v6)                ALLOW       Anywhere (v6)
16823 (v6)                 ALLOW       Anywhere (v6)
```

## 测试思路
1. 测试是否ping的通，可以用 https://tools.ipip.net/ping.php
2. 用站长工具查看端口是否开放，https://tool.chinaz.com/port
3. 用外网查看端口是否开放，https://www.yougetsignal.com/tools/open-ports/

如果内网端口没开放，但是外网端口开放了，说明 IP 被封了，只能重建机器；
如果内网和外网都关闭了，可能是服务器的防火墙限制了端口。

## Mac 下的守护进程

编辑 `~/Library/LaunchAgents/com.v2ray.plist`

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>Label</key>
        <string>com.v2ray</string>
        <key>ProgramArguments</key>
        <array>
            <string>/opt/homebrew/bin/v2ray</string>
            <string>run</string>
            <string>-config</string>
            <string>/Users/zhangxiaobin/.v2ray/client.json</string>
        </array>
        <key>RunAtLoad</key>
        <true/>
        <key>KeepAlive</key>
        <true/>
        <key>StandardOutPath</key>
        <string>/tmp/v2ray.log</string>
        <key>StandardErrorPath</key>
        <string>/tmp/v2ray.err</string>
    </dict>
</plist>
```

启动守护进程
```bash
# 修改权限
chmod 644 ~/Library/LaunchAgents/com.v2ray.plist

# 启动守护进程
launchctl load ~/Library/LaunchAgents/com.v2ray.plist

# 查看进程
ps aux | grep v2ray
```