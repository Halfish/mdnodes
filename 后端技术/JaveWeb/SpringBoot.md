
## Spring Boot


1. Spring Boot Starter

启动器（starter）引入了web开发需要的所有的依赖和配置。
- `spring-boot-starter-web` 官方启动器
- `spring-boot-starter-aop` 同上
- `spring-boot-starter-jdbc` 同上
- `mybatis-spring-boot-starter` 第三方启动器

2. SpringBootApplication 注解

主要的作用：
- `@SpringBootConfiguration` 配置类
- `@EnableAutoConfiguration` 自动加载其他配置类
- `@ComponentScan` 扫描包，默认扫描当前类所在的包

### Spring Boot 配置

配置会进行统一管理，配置在 `application.[properties/yaml/yml]` 中。 


### Spring Boot 项目打包

普通的web项目打包
- 打包成 war 格式
- 放到 tomcat/webapps/ 文件夹下面
- tomcat 启动会自动解压

SpringBoot 打包
- 打包成 jar 包，包含了服务器软件
- 记得添加插件 `spring-boot-maven-plugin` 依赖，否则可以打包但是运行有问题。
- 命令执行 java -jar xx
- 可以加参数，动态改变配置，如 `java -jar xxx -Dserver.port=8080`
