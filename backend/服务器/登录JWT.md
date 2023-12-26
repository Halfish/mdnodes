## JWT, Json Web Token 原理

JSON Web Token（简称 JWT）是目前最流行的跨域认证解决方案，参考 [阮一峰 JWT](https://www.ruanyifeng.com/blog/2018/07/json_web_token-tutorial.html)。

### 1. 传统的 session_id / cookie 的方式

因为 HTTP 协议是无状态的，用户无法和网站持续通信很不方便。因此诞生出 cookie/session 这种机制。

cookie 是存储在浏览器里的key=value键值对。主要是存储 session_id。而 session 是存储在后台的结构，记录会话的一些必要信息（比如登录态？）。

这种机制有一些弊端：
- 拓展性不好，服务器集群得共享 session；
- 如果存在数据库里，代码开发量大。

### 2. Access Token 和 Refresh Token
客户端登录后（比如用用户名密码登录），服务端会返回一个 Token，下次客户端可以直接拿Token去登录。Token使得服务器不用维护和存储Session，做到了服务器无状态化。

Access Token的有效期比较短，可以拿 Refresh Token 去刷新。如果 Refresh Token也过期了，用户只能重新登录了。

### 3. JWT, Json Web Token
JWT 是实现上面的 token 做法的一个流行方案。隐私 JWT 可以不保存 session 数据，所有数据保存在客户端，每次请求发挥服务器，服务器验证即可。

JWT 由三个部分组成，Header.Payload.Signature；
- Header和Payload 是不加密的，用 Base64URL 编码。
- Signature 是对前两个字段的签名，防止数据篡改。（用参数和密钥生成哈希，如果参数变了，哈希也得变）

JWT 怎么用
1. 用户登录，服务器验证用户名密码后，返回 access_token & refresh_token
2. 用户收到 token，放在 Cookie 或者 localStorage 里；
3. 每次客户端与服务器通信时，都要带上这个 JWT；
  - 可以在 Cookie 里自动发送，但是这样不能跨域；
  - 更好的做法是放在 HTTP 请求头的 Authorization 字段里。
  - 另一种做法是放在 POST 请求的数据体（body）里。

注意：
- secret 最好加密。
- 用 HTTPS 传输。
- 尽量把过期时间设置小一点。


### 4. flask 实现

这里主要介绍两个库：

flask-jwt
这个库可以在 payload 和 token 之间相互转换。
- jwt.encode 把 payload 编码成 token
- jwt.decode 把 token 解码出 payload


flask-jwt-extended
参考 flask 文档 [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/) 

常用的函数:
- create_access_token: 创建 token
- @jwt_required()，接口需要 access_token；
- get_jwt_identity，拿到 access_token；
- set_access_token/set_refresh_token，设置返回的 HTTP Response 的 Set-Cookie 字段。浏览器收到后，会自动记录下 Cookie；
