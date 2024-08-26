# Spring Framework

主要包含下面几个功能
1. IoC 核心容器：管理和实例化组件。
2. AOP & Aspects：面向切面编程。
3. TX：声明式事务管理。
4. Spring MVC：提供了面向Web应用程序的集成功能。


## 1. Spring 核心容器（Container）

### 1.1 组件和组件管理
常见业务逻辑，按照调用的顺序可以分成三种：
1. Servlet 层，控制层
2. Service 层，业务逻辑层
3. Dao 层，持久化层

可以把上面的所有层的组件用统一的方式管理，如自动创建和保存。我们只需要写配置。

有三种配置的方式：
1. XML配置方式：Spring第一版就支持，配置复杂，逐渐被淘汰。
2. 注解方式，从 Spring2.5 开始支持。通过在 Bean类上加注解（`@Component`，`@Service`，`@Autowired`等）
3. Java类，从Spring3.0开始支持，通过Java类来定义Bean、Bean之间的依赖关系。
（xml、注解、Java类）就行。

四中常见的 Spring IoC 容器
1. `ClassPathXmlApplicationContext`
    - 配置文件是 `xml` 格式
    - 读取项目路径（如`src`、`resources/`）下的 xml 文件
2. `FileSystemXmlApplicationContext`
    - 配置文件是 `xml` 格式
   - 文件存储到项目路径外
3. `AnnotationConfigApplicationContext`
    - 配置文件使用 `Java` 类
4. `WebApplicationContext`
    - web项目对应 IoC 容器


组件管理的步骤：
1. 配置 Bean（组件）
2. 实例化 IoC 容器。
3. 获取 Bean（组件）

### 1.2 基于 XML配置方式的组件管理

### 1.3 注解组件管理

### 1.4 Java类组件管理