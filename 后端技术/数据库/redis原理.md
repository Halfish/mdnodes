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
    - `noeviction`, 默认不淘汰。
    - `volatile-ttl`, TTL越小越先被淘汰。
    - `allkeys-random`，随机淘汰
    - `volatile-random`，设置了 TTL 随机淘汰
    - `allkey-lru`，全体key，基于LRU算法淘汰
    - `volatile-lru`，设置了TTL的key，基于LRU算法淘汰
    - `allkey-lfu`，全体key，基于LFU算法淘汰
    - `volatile-lfu`，设置了TTL的key，基于LFU算法淘汰
- LRU（Least Recently Used）很久没用的会被优先删除
- LFU（Least Frequency Used）用的少的会被优先删除

## Redis 系统设计

- 缓存雪崩（Cache Avalanche）
    - 缓存服务器宕机，或者单量缓存集中失效
    - 导致大量请求直接涌入数据库造成数据库短时间内承受巨大压力
    - 甚至造成数据库崩溃或者整个系统不可用的现象。
- 缓存击穿（Cache Breakdown）
    - 和缓存雪崩类似，但是只是少数的特点数据失效，后果没那么严重。
- 缓存穿透（Cache Penetration）
    - 缓存和数据库中都没有数据，比如请求一个不存在的商品 ID，每次都要请求数据库
    - 解决方法是缓存空值，以及参数校验，尽量不要走数据库
    - 也可以用布隆过滤器过滤掉数据库中必然不存在的请求。

## Redis 持久化

Redis 一共有三种数据持久化的方案：
1. **AOF**（Append On File）日志：每执行一条写命令，就把该命令已追加的方式写到一个文件里。
    - 如果命令执行，但是日志还没记录就宕机了，可能忽悠数据丢失的风险。
    - 写日志是在主线程里执行的，可能会阻塞后续的操作。
    - 写回硬盘策略
        - Always 每次执行完写命令就同步日志到硬盘
        - Everysec 每秒一次把缓冲区的内容写到硬盘
        - No 由操作系统决定何时把缓冲区内容写到硬盘
    - AOF 重写机制
        - 避免 AOF 文件越来越大
        - 类似一次内存快照，用新的 AOF文件替换旧的。
        - 由单独的子进程 bgrewriteaof 来完成
        - 主线程正在执行的操作，会拷贝一份到缓冲区，子进程也就把缓冲区的内容拷贝到 AOF 文件。
2. **RDB**（Redis Database Backup）快照：将某一个时刻的内存数据，以二进制的方式写入磁盘。
    - `save` 命令，在主线程中执行，会阻塞主线程。
    - `bigsave` 命令，创建子进程来生成 RDB 文件，避免主线程阻塞。
3. 混合持久化方式：Redis4.0新增的方式，集成了 AOF 和 RBD 的优点。
    - AOF 日志丢失数据少，但是数据恢复慢；RDB快照容易丢数据，但是恢复快；
    - 混合持久化的方案：前半部分是 RDB快照，后部分是 AOF 增量数据；


## 秒杀系统

技术方案
- 页面有 cdn 缓存
- 限制用户 1 秒内只能发送一次请求，拦截无效请求。
- 用 Redis 记录请求，以及扣减商品。拦截后续所有的请求。
- 把成功的订单请求放到中间件里，逐个处理。
