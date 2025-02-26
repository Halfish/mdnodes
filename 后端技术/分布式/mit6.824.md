# MIT 6.824 分布式系统

[MIT 6.824](https://pdos.csail.mit.edu/6.824/schedule.html)

参考资料：
- 这里有很多相关的参考资料：[MIT6.824: Distributed System](https://csdiy.wiki/并行与分布式系统/MIT6.824/)
- 一些实现的细节：[OneSizeFitsQuorum/MIT6.824-2021](https://github.com/OneSizeFitsQuorum/MIT6.824-2021/tree/master)
- 纯代码：[PKUFlyingPig/MIT6.824](https://github.com/PKUFlyingPig/MIT6.824/tree/master)
- 课程中文翻译：[MIT6.824](https://mit-public-courses-cn-translatio.gitbook.io/mit6-824)

## Paper
Paper
- [MapReduce 2004](https://pdos.csail.mit.edu/6.824/papers/mapreduce.pdf)
- [GFS 2003](https://pdos.csail.mit.edu/6.824/papers/gfs.pdf)
- [Raft (extended) 2014](https://pdos.csail.mit.edu/6.824/papers/raft-extended.pdf)
- [ZooKeeper 2010](https://pdos.csail.mit.edu/6.824/papers/zookeeper.pdf)

课程没有提到 BigTable，但其实也很重要。

## Lab
Lab
- [Lab 1: MapReduce](https://pdos.csail.mit.edu/6.824/labs/lab-mr.html)
- [Lab 2: Key/Value Server](https://pdos.csail.mit.edu/6.824/labs/lab-kvsrv.html)
- [Lab 3: Raft](https://pdos.csail.mit.edu/6.824/labs/lab-raft.html)
- [Lab 4: Fault-tolerant Key/Value Service](https://pdos.csail.mit.edu/6.824/labs/lab-kvraft.html)
- [Lab 5: Sharded Key/Value Service](https://pdos.csail.mit.edu/6.824/labs/lab-shard.html)


### Lecture 2 - RPC and Threads

为什么用 go？
- 好用的 rpc 框架
- 内存安全，有垃圾回收；多线程。

《Effective Go》

- 线程 Threads vs Goroutes
    - 每个线程有自己的 program counter，stack，register
    - I/O concurrency
    - Multi Parallelism
    - Convenience
- 异步 Asynchronous I/O
    - 也可以叫 event-driven programming 事件驱动编程
    - 底层依赖 epoll 这种 I/O 多路复用

Thread challenges
- n = n + 1，异步带来的数据竞争问题

### GFS

GFS 原理
- GFS 把大文件拆解成多个 64MB 的 file chunk，分散存储到不同的服务器上。
- GFS架构由一个 master 和多个 chunkserver 组成。
- master 存储文件的 chunk 信息，chunkserver 具体存储 chunk 内容。
- client 用户端现请求 master，查询到 chunk 的具体地址，然后去 chunkserver 上拿数据。
- master 如果挂了，由 slave（平常负责只读）转正；
- chunk server 会把一份 chunk 存储 3 个副本（replica），以确保数据高可用性。

![](../../img/GFS-architecture.png)

### MapReduce
MapReduce 系统能利用大量的技术处理涉及大数据的复杂问题。

![](../../img/map-reduce-overview.png)

系统架构
1. Map 任务，把数据拆分成 key->value 对，也叫中间文件（Intermediate files）存储到硬盘中。
2. Reduce 任务，读取中间文件，汇总

### BigTable

类似 GFS，但是用来存储结构化数据（类似 MongoDB 存储 json？）

按照列来存储数据。但是支持行和列的索引。

BigTable 是 NoSQL，因为行数据不必包含所有的列。
