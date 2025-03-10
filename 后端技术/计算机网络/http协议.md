
## http1.0 和 http2.0

时间线
- 1989年万维网（WWW）诞生
- 1991年，HTTP 0.9 超简单的协议，只支持 GET 方法。
- 1996年，HTTP 1.0，听加了 POST、HEAD 方法，引入了状态码和响应头
- 1997年，HTTP 1.1，引入持久连接和管道化，支持分块传输编码、缓存控制等；
- 2009年，谷歌提出 SPDY 协议，实现了多路复用、请求优先级、压缩头部等
- 2015年，HTTP 2.0 发布，基于 SPDY，引入二进制分帧、多路复用、头部压缩（HPACK）；
- 2020年，基于 QUIC 协议的 HTTP/3 发布，基于 UDP 传输。


HTTP 1.1 的缺点
- 无状态 -> session + cookie / token
- 不安全 -> http + tls = https

HTTP 2.0 的改进
- 二进制分帧，是多路复用的基础
- 多路复用

HTTP 3.0
- 基于 QUIC (Quick UDP Internet Connections) 协议，是基于 UDP 协议的。
- 引入多路复用，内嵌 TLS 加密协议。
- 智能拥塞控制算法。

## 状态码

状态码
- 1xx 信息响应
- 2xx 成功
    - 200 成功
- 3xx 重定向
    - 301 Moved Permanently，永久重定向
    - 302 Found, Moved Temporarily 临时重定向
- 4xx 客户端错误
    - ​400 Bad Request：请求格式错误（如参数错误）。
    - ​401 Unauthorized：需要身份验证（如未携带有效Token）。
    - ​403 Forbidden：服务器拒绝请求（已认证但无权限）。
    - ​404 Not Found：请求的资源不存在。
    - ​405 Method Not Allowed：请求方法不被允许（如用POST访问只支持GET的接口）。
- 5xx 服务器错误
    - 500 Internal Server Error：服务器内部错误（通用错误）。
    - ​502 Bad Gateway：网关或代理服务器从上游收到无效响应。
    - ​503 Service Unavailable：服务暂时不可用（如维护或过载）。
    - ​504 Gateway Timeout：网关等待上游服务器响应超时。