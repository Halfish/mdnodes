# Redis 原理

## 单线程模型

源码分析：

跨平台的多路复用实现
- `ae_epoll.c` Linux下的实现
- `ae_evport.c` Solaris 平台下的实现
- `ae_kqueue.c` 类Unix平台，包含MacOS的实现
- `ae_select.c` 其他平台。
- `ae.c` 同意封装接口。

API
- aeApiCreate(aeEventLoop *) 创建多路复用程序，类比 `epoll_create`
- aeApiAddEvent(aeEventLoop *, int, int) 注册 FD，类比 `epoll_ctl`
- aeApiPoll(aeEventLoop *, timeval *) 等待 FD就绪，类比 `epoll_wait`

`server.c`
- Redis 处理I/O并发的逻辑和 epoll 类似。

## Redis 中的单线程

Redis 在 6.0 版本中引入了多线程
- 在 `读取客户端命令`，`写响应结果`时涉及网络 I/O 操作，采用了多线程。
- 核心的命令执行（纯内存操作），IO多路复用模块，依然是主线程（单线程）执行。

多线程提升了吞吐量，但是单个命令的时延没有提升。

## Redis 过期回收

```bash
# 设置最大内存
maxmemory 1gb

```

Redis内部用哈希表存储了每个 key 的过期时间。

过期策略：
- 惰性删除：访问时再去检查key的存活时间，过期了才删除。
- 周期删除：周期性的抽样部分过期的key，然后执行删除。有两类：
    - 定时任务，serverCron()，按照 server.hz 的频率来执行过期 key 清理，模式为 SLOW；（小于25毫秒）
    - 每个事件循环前会调用 beforeSleep() 函数，执行过期 key 清理，模式为 FAST；（小于1毫秒）

过期策略属于主线程，不会有多线程的同步问题。

## Redis 内存淘汰策略

当 Redis 内存使用达到阈值时，Redis 会主动挑选部分的 key 删除，以释放更多内存流程。

淘汰策略
- 每次执行命令之前，都会检查下是否需要淘汰内存。
- Redis支持8种策略
    - noeviction, 默认不淘汰。
    - volatile-ttl, TTL越小越先被淘汰。
    - allkeys-random，随机淘汰
    - volatile-random，设置了 TTL 随机淘汰
    - allkey-lru，全体key，基于LRU算法淘汰
    - volatile-lru，设置了TTL的key，基于LRU算法淘汰
    - allkey-lfu，全体key，基于LFU算法淘汰
    - volatile-lfu，设置了TTL的key，基于LFU算法淘汰
- LRU（Least Recently Used）很久没用的会被优先删除
- LFU（Least Frequency Used）用的少的会被优先删除
