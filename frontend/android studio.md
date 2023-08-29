## 一、Android Studio 版本

| 版本号       | 中文   | 发布时间 | 备注 |
| ------------ | ------ | -------- | ---- |
| Hedgehog     | 刺猬   | 2023.1.1 |
| Giraffe      | 长颈鹿 | 2022.3.1 |
| Flamingo     | 火烈鸟 | 2022.2.1 |
| Electric Eel | 电鳗   | 2022.1.1 |
| Dolphin      | 海豚   | 2021.3.1 |
| Chipmunk     | 花栗鼠 | 2021.2.1 |      |
| Bumblebee    | 大黄蜂 | 2021.1.1 |
| Arctic Fox   | 北极狐 | 2020.3.1 |

## 二、Android version

Google APIs Intel x86_64 Atom System Image API 33


## 三、Android SDK Platform
安卓开发工具，可以用 SDK Manager 或者 `sdkmanager` 命令行来管理。

包括 `SDK Platforms` 和 `SDK build Tools`，前者是 Android 版本，后者是安卓开发工具。


## 四、Gradle
Gradle 是用来打包安卓的，用 Groovy/Kotlin 语言编写.

Gradle = ant + maven
- ant 是用 xml 形式写的脚本，可以自动运行。
- maven 是负责管理 jar 包，版本依赖，版本升级的工具。

Gradle 有两个概念，
- 项目（projects）：可以为不同的设备构建不同的版本，如安卓端、桌面端、iOS端、小米、华为等；
- 任务（tasks）：项目由一个个任务组成，如编译、打包、执行等。


配置
- gradle 的版本是配置的，如 `android/Pilot/gradle/wrapper/gradle-wrapper.properties`
- 默认 gradle 7.0 版本 ？会在 `~/.gradle` 下缓存数据。
- 如果版本不对，可以删除 ~/.gradle 下面的缓存重试。

## 五、Java & JDK

比较乱，得按照时间线梳理一下。（参考[这篇博客](https://juejin.cn/post/6844903839682789390)）

Java 的历史
- `Java` 是 Sun 公司于 1995 年发布的一门编程语言以及开放平台，后来 Sun 公司被 Oracle 公司收购。
- Sun 公司为 JVM 发布了 JVM 规范，任何公司都可以按照此规范开发 JVM 语言，如现在的 Kotlin、Scala 等。
- `Open JDK` 是 Sun 公司在 2009 发布的完全自由，开放源码的 Java平台标准版（Java SE）免费开源实现，按照 GPL 协议发布。

Android 和 Java
- Android 首先用的 Java 是基于 Apache 协议发布的 `Harmony` 版本。
- 由于 Harmony 本身限制，以及 Oracle 公司的起诉，从 Android N (7.0) 开始，Google 开始用 OpenJDK 来替代 Harmony。

JDK 版本
- openJDK 1.8  `/usr/lib/jvm/java-8-openjdk-amd64`
- openJDK 1.11: `/home/xiaobinzhang/Android/JDK/openlogic-openjdk-11.0.19+7-linux-x64`

ponypilot 项目要用 Java 11.
