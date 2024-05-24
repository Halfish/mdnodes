## 服务端配置

编辑 `/user/local/etc/v2ray/config.json` 如下：

```json
{
  "inbounds": [
    {
      "port": 16823, // 服务器监听端口
      "protocol": "vmess", // 主传入协议
      "settings": {
        "clients": [
          {
            "id": "625ed725-09c1-f52c-a740-b65384ffac25", // 用户 ID，客户端与服务器必须相同
            "alterId": 0 // v4.28.1 版本之后必须设置为 0 以启用 VMessAEAD
          }
        ]
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "freedom", // 主传出协议
      "settings": {}
    }
  ]
}
```

## 客户端配置

Windows 下建议用 V2RayN 客户端

```json
{
  "inbounds": [
    {
      "port": 1080, // 监听端口
      "protocol": "socks", // 入口协议为 SOCKS 5
      "sniffing": {
        "enabled": true,
        "destOverride": ["http", "tls"]
      },
      "settings": {
        "auth": "noauth" //socks的认证设置，noauth 代表不认证，由于 socks 通常在客户端使用，所以这里不认证
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "vmess", // 出口协议
      "settings": {
        "vnext": [
          {
            "address": "[your-server-ip]", // 服务器地址，请修改为你自己的服务器 IP 或域名
            "port": 16823, // 服务器端口
            "users": [
              {
                "id": "625ed725-09c1-f52c-a740-b65384ffac25", // 用户 ID，必须与服务器端配置相同
                "alterId": 0 // 此处的值也应当与服务器相同
              }
            ]
          }
        ]
      }
    }
  ]
}
```
