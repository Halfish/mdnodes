# Flask 源码阅读


## Flask 项目
Pallets 组织开发的几个项目
- Flask
    - 轻量级 WSGI 的 web 应用框架
    - 起初只是封装一下 werkzeug 和 jinja
- Quart
    - 快速的 WSGI web 应用框架，是一个异步版本的 flask
- Jinja
    - 是一个快速的（fast），表现力强（expressive），扩展性（extensible）的模板引擎。
    - 类似 JSX
- Click
    - 命令行工具
    - 方便处理命令行参数，运行命令
- Werkzeug（德语里的工具）
    - 是一个全面的（comprehensive）的 WSGI Web 应用库
    - 包括：
        - 交互式的调试器，可以检查浏览器中的堆栈信息和源码
        - request 对象，包含请求头，请求参数，表格数据，文件，cookies
        - response 对象，封装了其他 WSGI 应用和处理流数据
        - 路由系统，可以已匹配 URLs
        - HTTP 实用工具，用来处理实体标签，缓存控制，事件代理，cookies，文件等
        - 基于线程的 WSGI 服务器
        - 测试客户端，用于测试时模拟 HTTP 请求
- ItsDangerous
    - 用于加密和解密数据，或者说序列化和反序列化
- MakeupSafe
    - 用于转义字符，以用在 HTML 或者 XML 中。
    - 如 `<` 符号会被转义成 `&lt;`，以免被浏览器认为是标签的开始。