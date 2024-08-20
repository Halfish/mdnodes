# JavaEE

JavaEE
- JavaEE 是 `Java Platform Enterprise Edition` 的缩写，即 Java 企业平台。
- JavaEE 是在 JavaSE 的基础上，开发的一系列基于服务器的组件、API标准和通用架构。
- JavaEE 最核心的组件就是基于 `Servlet` 标准的 Web 服务器，开发者编写的应用程序是基于 Servlet API并运行在 Web 服务器内部的。

## Servlet
Servlet 是运行在Java服务器上的一个小程序，属于应用服务器和数据库的中间层，用于处理业务逻辑和客户端的用户请求。

每个 `servlet` 配置可以类比 `python` 中的 `flask` 中的 `blueprint`。

## Tomcat
支持 Servlet API 的 Web 服务器。
- Tomcat: 由 Apache 开发的开源免费服务器。
- Jetty: 由 Eclipse 开发的开源免费服务器。
- GlassFish: 一个开源的全功能 JavaEE服务器。

注意 Servlet 和 Tomcat 的版本。
- 用Servlet<=4.0时，选择Tomcat 9.x或更低版本；
- 使用Servlet>=5.0时，选择Tomcat 10.x或更高版本。

## JSP
Java Server Pages，就是总体以HTML语言为主，混合了Java变量和简单逻辑的文件。

## Maven
Maven是一个Java项目管理和构建工具
- 定义项目结构，项目依赖
- 自动化构建（编译，测试，打包，发布）

类似 `vite`, `webpack`, `gradle`, `bazel`, `cmake`, `bcloud`

如执行下面的命令：`maven clean package`。

## Spring
[Spring](https://spring.io/) 是一个支持快速开发 JavaEE 应用程序的框架。

Spring Framework主要包括几个模块：
- 支持IoC和AOP的容器；
    - IoC, Inversion of Control，控制反转。
        - IOC是一种编程原则，它将对象创建和依赖管理的责任从应用程序代码中移出，交给Spring容器来管理。
        - Spring容器负责创建、销毁和维护组件（组件叫做 JavaBean）（如数据库链接的组件），供其他服务使用。
        - 其实就是抽象，比如 `UserService` 会把**用户**相关的逻辑抽象成一个 `UserRepository`。
    - AOP是 Aspect Oriented Programming，即面向切面编程。
        - 主要用于：权限检查、日志、事务
        - AOP本质上只是一种代理模式的实现方式
- 支持JDBC和ORM的数据访问模块；
    - Hibernate：流行的ORM框架，基于JPA实现对象关系映射。依赖 JDBC驱动。
    - JPA（Java Persistence API）：Java标准的ORM规范。它的实现其实和Hibernate没啥本质区别
    - MyBatis：半自动化的持久层框架，灵活且**性能较好**，简单容易学习。
- 支持声明式事务的模块；
- 支持基于Servlet的MVC开发；
- 支持基于Reactive的Web开发；
- 以及集成JMS、JavaMail、JMX、缓存等其他模块。

注意不同 spring 版本下的各模块的版本：

| 项目            | Spring 5.x            | Spring 6.x            |
|-----------------|-----------------------|-----------------------|
| **JDK版本**     | >= 1.8                | >= 17                 |
| **Tomcat版本**  | 9.x                   | 10.x                  |
| **Annotation包**| `javax.annotation`    | `jakarta.annotation`  |
| **Servlet包**   | `javax.servlet`       | `jakarta.servlet`     |
| **JMS包**       | `javax.jms`           | `jakarta.jms`         |
| **JavaMail包**  | `javax.mail`          | `jakarta.mail`        |

### IoC（Inversion of Control，控制反转）
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    private final UserRepository userRepository;

    @Autowired // Spring自动注入UserRepository，不需要手动去创建
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public void performOperation() {
        userRepository.saveUser();
    }
}
```
在上述例子中，UserService 不再负责 UserRepository 的创建，而是由Spring容器自动管理和注入。这就是IOC的体现。

### AOP（Aspect-Oriented Programming，面向切面编程）
定义：AOP是一种编程范式，它允许将横切关注点（如日志记录、事务管理、权限检查等）从业务逻辑中分离出来，以模块化的方式应用到业务逻辑中。

AOP通过下面几个核心概念来实现这一目标。
- 切面（Aspect）：封装横切关注点的模块，通常是一个类。
- 通知（Advice）：切面中的具体行为，如方法执行前、执行后或抛出异常时的操作。
- 切入点（Pointcut）：指定通知应用到哪些连接点（Join Point），如方法执行、对象实例化等。
- 连接点（Join Point）：程序执行的某个特定点，如方法调用或异常抛出。

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.After;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class LoggingAspect {

    @Before("execution(* com.example.UserService.*(..))")
    public void logBefore() {
        System.out.println("Before method execution");
    }

    @After("execution(* com.example.UserService.*(..))")
    public void logAfter() {
        System.out.println("After method execution");
    }
}
```
在上述例子中，LoggingAspect 是一个切面，它包含了两个通知 logBefore 和 logAfter，分别在 UserService 的每个方法执行前后自动记录日志。
业务逻辑代码与日志记录代码实现了分离，这就是AOP的作用。


## Spring Boot
Spring Boot
- Spring Boot是基于Spring框架的一个子项目，旨在简化Spring应用程序的配置和开发。
- 它通过提供默认配置和开箱即用的功能，帮助开发者快速创建基于Spring的应用程序，而无需编写大量的配置代码。


## Swagger/OpenAPI
用于 API 文档生成与测试。

# 技术资料
- [凤凰架构](https://icyfenix.cn/)
