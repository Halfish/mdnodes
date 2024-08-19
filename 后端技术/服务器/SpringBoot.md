# SpringBoot

参考：[尚硅谷新版SSM框架全套视频教程，Spring6+SpringBoot3最新SSM企业级开发](https://www.bilibili.com/video/BV1AP411s7D7)

## 1. Maven
Apache Maven 是一个项目构建，以及依赖管理的工具。

项目构建主要包括(清理->编译->测试->报告->打包->部署)这些过程。

参考：
- 官网：https://maven.apache.org/

java的项目结构常用的有下面几种
- idea: `src/, web/`
- eclipse: `src/, webcontent/`
- maven: `src/, webapp/`

配置阿里云远程仓库：
```xml
<mirror>
    <id>aliyunmaven</id>
    <mirrorOf>*</mirrorOf>
    <name>阿里云公共仓库</name>
    <url>https://maven.aliyun.com/repository/public</url>
</mirror>
```

更多配置，参考[阿里云/Maven镜像](https://developer.aliyun.com/mirror/maven/)

配置项目的 JDK
1. 在 maven 的 settings 里配置，全局生效。
2. 在 gradle 的 build.gradle 中配置。
3. 在 maven 或者 gradle 的命令行参数里指定。
4. 在项目的 pom.xml 文件里配置，只针对项目生效。
5. 在 IDE 中指定，如 eclipse，IDEA 中都可以设置项目的JDK版本。
