# JVM, Java Virtual Machine

参考：
- [Java Garbage Collection Basics](https://www.oracle.com/webfolder/technetwork/Tutorials/obe/java/gc01/index.html)
- [HotSpot Virtual Machine Garbage Collection Tuning Guide](https://docs.oracle.com/en/java/javase/17/gctuning/)
- [Tuning Garbage Collection with the 5.0 Java™ Virtual Machine](https://www.oracle.com/java/technologies/tuning-garbage-collection-v50-java-virtual-machine.html)

## JDK, JRE, JVM
JDK > JRE > JVM

JDK
- JRE, Java Runtime Environment
    - JVM：类加载器 + JIT 解释器 + 垃圾回收
    - 依赖库，如 `java.util`, `java.lang`，logging，Java archive，JDBC等
- 开发工具：如 `java/javac/jmap/javadoc/jdb/jar`，编译器、debugger

## HotSpot JVM

JVM 负责处理和解析 class 文件，将字节码文件编译成二进制机器码后执行。 class文件包含了JVM指令字节码，符号表等。

![HotSpot JVM架构](https://www.oracle.com/webfolder/technetwork/Tutorials/obe/java/gc01/images/gcslides/Slide1.png)

JVM 主要包含
- 类加载器
- 执行机器
- JIT 解释器
- 垃圾回收器

## GC，garbage collect 垃圾回收
垃圾回收指的是把内存heap中不再被引用的对象清理掉。
垃圾回收主要有下面几步：
1. 标记：标记哪些内存需要回收
2. 删除操作
    - 正常删除：把不再有引用的内存块放到 memory allocator的空余内存链表中。
    - 压缩后删除（delete with compacting）：把有引用的内存块放到一起，剩下的就是完整的空余内存块。

### Generational Garbage Collect 分代垃圾回收
观察对象回收的行为，会发现程序运行一开始会大量创建对象，程序运行一段时间后，创建的新对象就越来越少。因此 HotSpot JVM 把堆内存分成下面几个部分：

![HotSpot Heap Structure](https://www.oracle.com/webfolder/technetwork/Tutorials/obe/java/gc01/images/gcslides/Slide5.png)

分别是：
1. Yong Generation（包含 eden + survivor space）
    - 新的对象分配的内存会在这部分里，当这里的内存用完了，会触发一次 `Minor Garbage Collection`（次级垃圾回收）。
    - 这里的回收对象速度很快，如果对象存活 ，最终会被挪到 Old Generator里。
    - 次级垃圾回收会触发 `Stop the World Event`事件，意思是所有的应用线程都会停止，直到操作完成。是为了确保不会有新的对象分配。
2. Old Generation（也叫 Tenured）
    - 用来存储存活时间比较长的对象。只有对象存活一定的时间，才会从 Young generation 里挪过来。
    - 回收一次 old generation的内存，叫做 `Major Garbage Collection`（主垃圾回收）。
    - 主垃圾回收也会触发 `Stop the World Event`事件。
    - 主垃圾回收会更加耗时，因为需要处理所有的活跃对象（为了避免内存碎片，需要把活跃对象全部压缩到一起）
3. Permanent Generation
    - 主要用存放Java运行时需要的一些类和方法。
    - 在 `full garbage collection` 过程中会被回收内存。



## JVM 性能调优
性能调优有两个目标
- responsiveness 及时响应
- throughput 吞吐量

