JavaEE 是 Java Platform Enterprise Edition 的缩写，即 Java 企业平台。

JavaEE 是在 JavaSE 的基础上，开发的一系列基于服务器的组件、API标准和通用架构。

JavaEE 最核心的组件就是基于 Servlet 标准的 Web 服务器，开发者编写的应用程序是基于 Servlet API并运行在 Web 服务器内部的。


## Servlet 入门
```java
// 4.0 以及以前，Oracle维护
import javax.servlet.*;
// 5.0之后，Eclipse开源社区维护
import jakarta.servlet.*;

// WebServlet注解表示这是一个Servlet，并映射到地址/:
@WebServlet(urlPatterns = "/")
public class HelloServlet extends HttpServlet {
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        // 设置响应类型:
        resp.setContentType("text/html");
        // 获取输出流:
        PrintWriter pw = resp.getWriter();
        // 写入响应:
        pw.write("<h1>Hello, world!</h1>");
        // 最后不要忘记flush强制输出:
        pw.flush();
    }
}
```

支持 Servlet API 的 Web 服务器。
- Tomcat: 有 Apache 开发的开源免费服务器。
- Jetty: 由 Eclipse 开发的开源免费服务器。
- GlassFish: 一个开源的全功能 JavaEE服务器。

servlet 类似 flask blueprint


把 `hello.war` 包放到 Tomcat 的 `webapps` 目录下，然后启动 Tomcat 就可以运行了。

编写 main() 方法，启动 Tomcat 服务器：
```java
public class Main {
    public static void main(String[] args) throws Exception {
        // 启动Tomcat:
        Tomcat tomcat = new Tomcat();
        tomcat.setPort(Integer.getInteger("port", 8080));
        tomcat.getConnector();
        // 创建webapp:
        Context ctx = tomcat.addWebapp("", new File("src/main/webapp").getAbsolutePath());
        WebResourceRoot resources = new StandardRoot(ctx);
        resources.addPreResources(
                new DirResourceSet(resources, "/WEB-INF/classes", new File("target/classes").getAbsolutePath(), "/"));
        ctx.setResources(resources);
        tomcat.start();
        tomcat.getServer().await();
    }
}
```

Filter 类似装饰器，可以对请求做一些预处理和后处理的工作。

## Maven
`maven clean package`

## Spring
Spring 是一个支持快速开发 JavaEE 应用程序的框架。

Spring Framework主要包括几个模块：
- 支持IoC和AOP的容器；
    - IoC, Inversion of Control，控制反转。
    - 负责创建、销毁和维护组件（组件叫做 JavaBean）（如数据库链接的组件），供其他服务使用。
- 支持JDBC和ORM的数据访问模块；
- 支持声明式事务的模块；
- 支持基于Servlet的MVC开发；
- 支持基于Reactive的Web开发；
- 以及集成JMS、JavaMail、JMX、缓存等其他模块。


AOP是Aspect Oriented Programming，即面向切面编程。
- 主要用于：权限检查、日志、事务
- AOP本质上只是一种代理模式的实现方式

Hibernate作为ORM框架，它可以替代JdbcTemplate，但Hibernate仍然需要JDBC驱动
JPA就是JavaEE的一个ORM标准，它的实现其实和Hibernate没啥本质区别

## Spring Boot
Spring Boot 是一个基于 Spring 的套件，预装了一系列的组件。

## 技术资料
- [凤凰架构](https://icyfenix.cn/)