# MIT 6.824 分布式系统

[MIT 6.824](https://pdos.csail.mit.edu/6.824/schedule.html)


## Paper
Paper
- [MapReduce 2004](https://pdos.csail.mit.edu/6.824/papers/mapreduce.pdf)
- [GFS 2003](https://pdos.csail.mit.edu/6.824/papers/gfs.pdf)
- [Raft (extended) 2014](https://pdos.csail.mit.edu/6.824/papers/raft-extended.pdf)
- [ZooKeeper 2010](https://pdos.csail.mit.edu/6.824/papers/zookeeper.pdf)

## Lab
Lab
- [Lab 1: MapReduce](https://pdos.csail.mit.edu/6.824/labs/lab-mr.html)
- [Lab 2: Key/Value Server](https://pdos.csail.mit.edu/6.824/labs/lab-kvsrv.html)
- [Lab 3: Raft](https://pdos.csail.mit.edu/6.824/labs/lab-raft.html)
- [Lab 4: Fault-tolerant Key/Value Service](https://pdos.csail.mit.edu/6.824/labs/lab-kvraft.html)
- [Lab 5: Sharded Key/Value Service](https://pdos.csail.mit.edu/6.824/labs/lab-shard.html)


### Lecture 1 - Introduction

mapreduce
- The whole computation is called job
- map/reduce task

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

### Lecture 3 - GFS

GFS 把大文件拆解成多个 16MB 的 file chunk，分散存储到不同的服务器上。

只有一个 master，多个 chunk server，
