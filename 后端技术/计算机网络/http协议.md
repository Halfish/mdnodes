
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