JWT, Json Web Token 原理
- 参考 [阮一峰 JWT](https://www.ruanyifeng.com/blog/2018/07/json_web_token-tutorial.html)
  - 传统的 session_id / cookie 的方式，拓展性不好，服务器集群得共享 session；如果存在数据库里，代码开发量大。
  - JWT 可以做到不保存 session 数据，所有数据保存在客户端，每次请求发挥服务器，服务器验证即可。
  - JWT 由三个部分组成，Header.Payload.Signature；
  - Header和Payload 是不加密的，Signature 是对前两个字段的签名，防止数据篡改。（用参数和密钥生成哈希，如果参数变了，哈希也得变）
  - JWT 怎么用
    - 可以放在 Cookie 里；存储在 localStorage 里；
    - 每次客户端与服务器通信时，都要带上这个 JWT；可以在 Cookie 里自动发送，但是这样不能跨域；
    - 更好的做法是放在 HTTP 请求头的 Authorization 字段里。
    - 另一种做法是放在 POST 请求的数据体（body）里。
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
    - 文档：
    - create_access_token: 创建 token
    - @jwt_required()，接口需要 access_token；
    - get_jwt_identity，拿到 access_token；
    - set_access_token/set_refresh_token，设置返回的 HTTP Response 的 Set-Cookie 字段。浏览器收到后，会自动记录下 Cookie；
  