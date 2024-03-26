# JVM, Java Virtual Machine

参考：
- [Java Garbage Collection Basics](https://www.oracle.com/webfolder/technetwork/Tutorials/obe/java/gc01/index.html)
- [HotSpot Virtual Machine Garbage Collection Tuning Guide](https://docs.oracle.com/en/java/javase/17/gctuning/)
- [Tuning Garbage Collection with the 5.0 Java™ Virtual Machine](https://www.oracle.com/java/technologies/tuning-garbage-collection-v50-java-virtual-machine.html)
- [面试官：如何进行 JVM 调优（附真实案例）](https://zhuanlan.zhihu.com/p/488615913)

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
- 类加载器 classLoader
- 执行机器
- 字节码解释器
- JIT 编译器
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
    - 主要用存放Java运行时需要的一些class、字符串常量等。
    - 在 `full garbage collection` 过程中会被回收内存。
    - Java 8 之后移除了，用元空间替代。
4. Metaspace
    - 替代 Permanent Generation
    - 和 Java 对象的堆内存的隔离的，不会有内存溢出的问题。（除非机器内存满了）

垃圾回收的主要过程如下：
1. 首先，新的对象分配在 Eden 内存中，清空 survivor 区域的内存。
2. Eden区域满了之后，次级垃圾回收（minor GC）会被执行。
3. 活跃的对象会被移到 S0 区域，不活跃的对象会被删掉。
4. 同理，Eden区域满了之后，会执行minor GC，把不活跃的对象删掉，活跃的对象挪到S1；同时S0里活跃的对象age+1，不活跃的删掉。此时S0清空了。
5. 下一次minor GC，Eden里活跃的对象挪到S0，清空S1；这样循环下去。
6. 当 survivor 区域的对象age到了阈值，就会把这部分对象挪到tunured区域。
7. 随着minor GC的执行，不断有对象挪到tunured区域，称作promoted。
8. 最终，tenured区域满了，会触发一次major GC；


### Java Garbage Collector
GC 相关的参数：
- `-Xms`，JVM启动时，初始的 heap 大小。
- `-Xmx` 最大的堆大小
- `-Xmn` 年轻代的堆的大小
- `-XX:PermSize` Permanent Generation 的堆大小。
- `-XX:MaxPermSize` 最大的 Permanent Generation 的堆大小。

Serial GC
- `-XX:+UseSerialGC`  默认用单核的CPU；

Parallel GC
- `-XX:ParallelGCThreads=<desired number>` 可以设置 Parallel GC 的线程数量。注意只影响 Young Generation 的并行数。
- `-XX:+UseParallelGC` 使用并行GC；
- `-XX:+UseParallelOldGC ` 这里 Old Generation 也是用并行的GC；

CMS Collector
- Concurrent Mark Sweep (CMS) Collector
- 这个 collector 不移动活跃的对象，如果内存碎片是个问题，就会重新申请一个大的 heap；
- `-XX:+UseConcMarkSweepGC`
- `-XX:ParallelCMSThreads=<n>`

The G1 Garbage Collector
- 又叫做 The Garbage First garbage collector，用来替代 CMS collector
- `-XX:+UseG1GC`

并发（concurency）是一个人吃三个馒头，并行（parallel）是三个人吃三个馒头。

## JVM 性能调优
性能调优有两个目标
- responsiveness 及时响应
- throughput 吞吐量

可以从下面几个方向做性能调优：
1. 调整堆的大小
2. 选择不同的垃圾回收器
3. 调整并发线程数
4. 调整内存区域划分的比例，如新生代和老年代的比例。
5. 监控和调优工具，如 `jmap, jstack, jstat`
