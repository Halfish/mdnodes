[TOC]

# Maven
Apache Maven 是一个项目构建，以及依赖管理的工具。

项目构建主要包括(清理->编译->测试->报告->打包->部署)这些过程。

参考：
- 官网：https://maven.apache.org/
- [尚硅谷新版SSM框架全套视频教程，Spring6+SpringBoot3最新SSM企业级开发](https://www.bilibili.com/video/BV1AP411s7D7)

java的项目结构常用的有下面几种
- idea: `src/, web/`
- eclipse: `src/, webcontent/`
- maven: `src/, webapp/`

## 1. Maven配置
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

哪里可以配置项目的 JDK？
1. 在 maven 的 settings 里配置，全局生效。
2. 在 gradle 的 build.gradle 中配置。
3. 在 maven 或者 gradle 的命令行参数里指定。
4. 在项目的 pom.xml 文件里配置，只针对项目生效。
5. 在 IDE 中指定，如 eclipse，IDEA 中都可以设置项目的JDK版本。

## 2. 用 Maven 构建 Java Web 工程

maven 的 GAVP 属性:
- `Group ID` 组织名，类似包名，如 com.taobao.tddl
- `Artifact ID` 压缩包，产品线名-模块名，如 learnjava
- `Version`，版本号，如 `1.0.1`
- `Packaging` 将会打包的文件类型
  - 属性为 `jar`（默认），代表是普通的 Java 工程，打包以后是以 `.jar` 结尾的文件。
  - 属性为 `war`，代表的是 Java 的 Web 工程，打包以后是以 `.war` 结尾的文件。
  - 属性为 `pom`，Project Object Model，代表的是不会打包，一般是父工程。

如下面的例子：
```xml
<groupId>org.example</groupId>
<artifactId>maven-javase-project-01</artifactId>
<version>1.0-SNAPSHOT</version>
<packaging>jar</packaging>
```

怎么创建一个 Maven Web 项目？
1. 手动创建 `webapp/WEB-INF/web.xml` 文件，并修改 `packaging` 为 `war` 属性。
2. 用插件 `JBLJavaToWeb`

一个典型的由Maven构建的Web项目结构如下：
```bash
my-webapp/
├── src/
│   ├── main/
│   │   ├── java/                            # Java源代码文件存放目录
│   │   │   └── com/
│   │   │       └── example/
│   │   │           └── MyWebApp.java        # Java类文件，包含业务逻辑和控制器等
│   │   ├── resources/                       # 资源文件目录，例如配置文件、属性文件等
│   │   │   └── application.properties       # 示例配置文件
│   │   │   └── log4j.properties             # 日志配置文件
│   │   │   └── spring-mybatis.xml           # Spring Mybatis 配置文件
│   │   ├── webapp/                          # Web应用的Web内容目录
│   │   │   ├── WEB-INF/                     # Web应用的配置和JSP文件存放目录
│   │   │   │   └── web.xml                  # Web应用的核心配置文件
│   │   │   ├── META-INF/                    # 包含应用的元数据，如MANIFEST文件等
│   │   │   ├── index.jsp                    # 入口JSP文件，处理默认请求
│   │   │   └── assets/                      # 存放静态资源，如CSS、JavaScript、图像等
│   │   │       ├── css/
│   │   │       │   └── styles.css           # 样式表文件
│   │   │       └── js/
│   │   │           └── scripts.js           # JavaScript文件
│   ├── test/
│   │   ├── java/                            # Java测试代码存放目录
│   │   │   └── com/
│   │   │       └── example/
│   │   │           └── MyWebAppTest.java    # 单元测试类
│   │   └── resources/                       # 测试资源文件目录
├── target/                                  # 构建输出目录（由Maven自动生成）
│   ├── my-webapp-1.0-SNAPSHOT.war           # 打包后的Web应用WAR文件
│   ├── classes/                             # 编译后的字节码文件
│   ├── test-classes/                        # 编译后的测试字节码文件
│   └── ...                                  # 其他构建生成的文件
├── pom.xml       # Project Object Model     # Maven项目的核心配置文件，定义依赖、插件等
└── README.md                                # 项目说明文档（可选）
```

## 3. Maven管理版本依赖
在 `pom.xml` 中配置依赖包，
```xml
<dependencies>
    <dependency>
        <groupId></groupId>
        <artifactId></artifactId>
        <scope>compile</scope>
    </dependency>
</dependencies>
```

怎么查找依赖包呢？
1. 官网：https://mvnrepository.com 
2. 插件 `maven-search`

`scope`属性
- `compile`，在 `main` 和 `test` 里都可以用。
- `test`，只能在 `test` 里用，如 junit
- `runtime`，只能在打包和运行的时候用，如 mysql 的驱动，`Class.forName(com.mysql.cj.jdbc.Driver)`
- `provided`，在 `main`，`test` 中使用，打包和运行时不用。如 HttpServerlet

注意：如果原来下载失败了，可能是网络问题，需要去本地仓库删掉不完整的文件。然后重新下载。

## 4. Maven 命令

项目信息
```bash
# 获取 Maven 帮助信息。
mvn help:help

# 显示 Maven 的版本信息。
mvn --version

# 验证项目是否正确，所有必要的信息是否可用。
mvn validate
```

项目构建
```bash
# 编译项目的源代码。
mvn compile

# 编译测试代码。
mvn test-compile

# 根据项目的 pom.xml 文件打包项目，如生成 JAR 或 WAR 文件。
mvn package

# 清理项目，删除 target/ 目录中的所有生成文件。
mvn clean
```

项目部署
```bash
# 将项目的包安装到本地 Maven 仓库中，使得其他本地项目可以依赖该包。
# 部署只能是 jar 包，而非 war 包。
mvn install

# 将包发布到远程 Maven 仓库中，通常用于共享项目构建。
# 部署只能是 jar 包，而非 war 包。
mvn deploy
```

项目测试
```bash
# 运行测试用例。
mvn test

# 运行集成测试，检查项目是否正确。
mvn verify
```

项目生命周期
```bash
# 生成项目站点，包含项目的文档、报告等信息。
mvn site

# 先清理项目，再进行编译、测试、打包，并将包安装到本地仓库。
mvn clean install
```

插件和依赖管理
```bash
# 解析项目的依赖项，并下载所需的库。
mvn dependency:resolve

# 显示项目的依赖树结构。
mvn dependency:tree

# 分析项目的依赖使用情况，帮助清理未使用的依赖。
mvn dependency:analyze
```

其他命令
```bash
# 直接执行指定的主类，适用于快速测试。
mvn exec:java -Dexec.mainClass="com.example.Main"

# 检查项目依赖项的更新情况。
mvn versions:display-dependency-updates

# 使用模板生成一个新的 Maven 项目。
mvn archetype:generate

# 显示项目的有效 POM，包含继承和聚合后所有配置。
mvn help:effective-pom
```

注意 mvn 的命令周期，`compile -> test -> package -> install/deploy`，后面的命令会执行前面的命令。

`pom.xml` 里可以配置插件，如
```xml
<project xmlns="xxx">
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>mvn-war-plugin</artifactId>
                <version>3.2.2</version>
            <plugin>
        </plugins>
    </build>
</project>
```

## 5. Maven的继承和聚合特性

**Maven的继承**

假设项目有一个父工程和多个子工程（子模块），那么不同的子模块可能会有依赖版本冲突。

有两种思路解决。
1. 直接在父工程的 `pom.xml` 中引入该依赖模块。缺点是所有的子模块都会引入该依赖。
2. 在父工程的 `pom.xml` 只声明该依赖（用 `<dependencyManager>`标签），在子模块中引入（子工程不用写 version）。


**Maven的聚合**
在父工程的 `pom.xml` 里配置：
```xml
 <!-- Maven 的聚合，要统一管理哪些子工程的 artifactId -->
<modules>
    <module>shop-user</module>
    <module>shop-order</module>
</modules>
```

这样就能统一管理这些子工程。
