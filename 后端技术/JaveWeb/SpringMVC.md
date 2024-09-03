## Spring MVC

Spring MVC 基于 Servlet API，一般作为表述层的首选。

- `DispatcherServlet` 用来出来所有的请求，负责分发到具体的业务。
- `HandlerMapping, HandlerAdapter` 业务映射


注解
- `@RequestMapping` 指定URL路径
- `@ResponseBody` 直接返回字符串，不去找视图解析器
- `@RequestParam` 请求参数，如 `?name=Bruce&age=2`
- `@PathVariable` 接收动态路径上的属性，如 `/{username}/{age}`。
- `@RequestBody` 接收 json 请求，一般用于 POST 方法。
    - 需要导入 `jackson-databind` 依赖
    - `@EnableWebMvn` 加入 json处理器，在配置类上加入这个注解
- `@CookieValue` 接收 cookie
- `@RequestHeader` 接收请求头
- 原生对象: `HttpServletRequest`, `HttpServletResponse`, `HttpSession` 等
- 共享域: 看不懂，老项目才需要

逻辑视图
- 即用 jsp 写的网页，前后端混合开发。
- 视图解释器会配置
