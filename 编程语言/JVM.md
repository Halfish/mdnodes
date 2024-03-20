# JVM, Java Virtual Machine

参考：
- [Java Garbage Collection Basics](https://www.oracle.com/webfolder/technetwork/Tutorials/obe/java/gc01/index.html)
- [HotSpot Virtual Machine Garbage Collection Tuning Guide](https://docs.oracle.com/en/java/javase/17/gctuning/)

## HotSpot JVM

JVM 负责处理和解析 class 文件，将字节码文件编译成二进制机器码后执行。 class文件包含了JVM指令字节码，符号表等。

![HotSpot JVM架构](https://www.oracle.com/webfolder/technetwork/Tutorials/obe/java/gc01/images/gcslides/Slide1.png)

JVM 主要包含
- 类加载器
- 执行机器
- JIT 编译器
- 垃圾回收器

## GC，garbage collect 垃圾回收
垃圾回收指的是把内存heap中不再被引用的对象清理掉。
垃圾回收主要有下面几步：
1. 标记：标记哪些内存需要回收
2. 删除操作
    - 正常删除：把不再有引用的内存块放到 memory allocator的空余内存链表中。
    - 压缩后删除（delete with compacting）：把有引用的内存块放到一起，剩下的就是完整的空余内存块。

观察对象回收的行为，会发现程序运行一开始会大量创建对象，程序运行一段时间后，创建的新对象就越来越少。因此 HotSpot JVM 把堆内存分成下面几个部分：

![HotSpot Heap Structure](https://www.oracle.com/webfolder/technetwork/Tutorials/obe/java/gc01/images/gcslides/Slide5.png)

分别是：
1. Yong Generation
2. Old Generation
3. Permanent Generation


## JVM 性能调优
性能调优有两个目标
- responsiveness 及时响应
- throughput 吞吐量

