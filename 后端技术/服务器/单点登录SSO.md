## SSO, Single Point Authorization

单点登录有下面几种常用的协议
1. SAML，Security Assertion Markup Language 
  - 用于基于 Web 的单点登录；
  - 但是协议比较老（2005年），是设计用来处理 Web 的登录，对 App 的支持不太好。
2. OAuth2，2012年创立，可以再很多场合使用。
  - 主要分下面几步：
    - Client 向用户请求权限；用户准许；
    - Client向 Auth获取授权，拿到 Token；
    - Client 拿着 Token 去访问资源；
  - 优缺点：
    - 默认在 HTTPS 下工作。
    - OAuth2是一个授权协议，而不是认证协议。
3. OIDC，Open ID Connect 
  - 在 OAuth2 的基础上做了身份层，是一个基于OAuth2协议的身份认证标准协议。
  - OIDC的优点是：简单的基于JSON的身份令牌（JWT），并且完全兼容OAuth2协议。
4. CAS, Central Authentication Service
  - 是一个企业级的开源的 SSO 认证框架，
  - CAS内部集成了CAS1,2,3，SAML1,2，OAuth2,OpenID 和 OpenID Connect协议。


单点登录主要用的是 JWT 的一些技术，参考另一篇笔记。
