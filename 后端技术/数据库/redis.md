# redis 

![](https://redis.io/images/redis.png)

- 首页：https://redis.io
- 中文首页：https://www.redis.com.cn/

redis 是基于 BSD 协议开源的内存型数据结构存储系统，用于做数据库、缓存和消息中间件。

## 1. redis 支持的数据结构

因为 redis 是个 key-value 的服务器，但是 value 支持更多的类型。

### 1.1 字符串（String，用 set 和 get 命令）

Redis 用的字符串类型是自己实现的 Simple Dynamic String，简单动态字符串，如 `sdshdr16` 的定义如下
```c
struct __attribute__ ((__packed__)) sdshdr16 {
    uint16_t len;       // 字符串长度
    uint16_t alloc;     // 字符串总共可用的长度
    unsigned char flags;    // 低3位保存类型，高5位没用到
    char buf[];         // 实际存储字符串
};
```

SDS有下面的特点：
- 记录字符串的长度，不会有缓冲区溢出的问题。
- 内存空间采用预分配和惰性回收的机制，避免频繁的内存操作。
- 存储的字符串（包括 key 和 value）是二进制安全的（binary-safe），即不会解析任何的字符串，仅仅当做原始的字符串流。
- C++ 中的字符串是以 \0 作为字符串的结束符，这就不是 binary-safe 的。
- 可以用来存储二进制文件，如图片音频等，字符串的大小不能超过 512M。


常见命令：
```bash
# 设置键值，EX 是过期时间，NX 表示不强制覆盖
$ SET key value [EX seconds] [PX milliseconds] [NX|XX]
$ GET key
$ DEL key [key ...]
```

更多的命令
```bash
# 不存在则设置成功，存在则设置失败
SETNX key value   

# 10 秒后过期
EXPIRE key 10

# 等同于上面两个命令，但这个是原子操作
SET key value ex 10 nx

# 查看某个 key 的过期时间，返回还剩几秒过期
TTL key

# 查看所有的 keys
KEYS *
```

### 1.2 哈希（Hash）
- 和 Python 中的字典（dict）、Ruby 中的哈希很像
- 存储如 `{'name': 'bruce', 'age': '14'}` 这样的数据结构
- Redis中的哈希表最多支持 `2^32 - 1` 个键值对

```bash
# 添加
HSET key field value [field value ...]
# 获取
HGET key field [field ...]
# 删除
HDEL key field [field ...]

# 查看所有的哈希表
HGETALL *
# 获取所有 keys
HKEYS key
# 获取所有 values
HVALS key

# 判断哈希表 key 是否存在 field
HEXISTS key field
# 获取哈希表 keys 数量
HLEN key
# 自增，需要 value 为整型
HINCRBY key field 1
```

哈希表有两种实现
- `ziplist`
    - 一种连续内存的数据结构，存放 key, value
    - 查找是线性扫描的，复杂度是 O(N)
    - 只有键值对少于 512 个，且长度小于 64 字节，才会采用 `ziplist` 这种结构。
- `hashtable`
    - 经典的哈希表实现。有 rehash 算法来解决冲突。
    - 缺点是要额外的结构来维护哈希表。
    - 当哈希表数量变大，会从 `ziplist` 转成 `hashtable`。


### 1.3 列表（List，lpush lrange）
- 其实是链表，根据插入的次序来排序的字符串集合
- 插入和删除的复杂度是 `O(1)`，但是索引的效率很低
- 列举下面两种 lists 使用的场景
    - 社交网络中用户最后 post 的更新。
    - 消费者-生产者模型里的消息队列
- 用 ltrim 来设置 list 的个数上限。
- brpop、blpop 来做 block 操作，如果 list 说空的，会等待直到不为空。

```bash
# 插入链表左边/右边
LPUSH/RPUSH key value [value ...]

# 返回 [start, stop] 范围内的链表元素
LRANGE key start stop

# 获取长度
LLEN key

# 删除
LPOP / RPOP
```

Redis 里的列表有三种实现
- `ziplist` 类似小数组，索引效率高
- `linkedlist` 双向链表，增删效率高，索引效率低
- `quicklist` 从 Redis 5.0 引入的数据结构，是多个 `ziplist` 组成的双向链表。


### 1.4 集合（`Set`）
有两种集合，`无序集合 set` 和`有序集合 zset`，都不允许重复元素

**无序集合**，只支持字符串的集合，无序集合中最多可以存放 `2^32 - 1` 个元素。
```bash
# 添加元素到集合中
SADD key member [member ...]
# 删除元素
SREM key member [member ...]

# 是否在集合中
SISMEMBER key member

# 查看集合所有元素
SMEMBERS key
# 查看集合的大小
SCARD key

# 两个集合的差集
SDIFF set1 set2
# 两个集合的交集
SINTER set1 set2
# 两个集合的并集
SUNION set1 set2
```

Redis无序集合底层的实现是
- `inset` 有序的整数集合，插入和删除的复杂度是 `O(N)`
- `hashtable` 哈希表

### 1.5 有序集合（`Zset`）
**有序集合（zset）** 就麻烦一些，允许元素重复，且每个元素都会关联一个 `double` 类型的分数。集合元素会按照降序排序。

修改：
```bash
# 添加元素，NX 表示只能创建，member 必须不存在；XX 则相反，是更新（覆盖），member 必须存在；
# 注意这里是先 score，再 key！顺序不要弄反了
ZADD key [NX|XX] [CH] [INCR] score member [score member ...]

# 创建，或者叠加（不是覆盖），和上面的 incr 参数相同
ZINCRBY key increment member
```

查询：
```bash
# 取范围内的元素，withscore 则一起返回分数；（比如用来取前 10 的排）
ZRANGE key start stop [WITHSCORES]      # 升序
ZREVRANGE key start stop [WITHSCORES]   # 降序

# 取某些分数范围内的元素
ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count]

# 获取排名
ZRANK key member
ZREVRANK key member

# 获取分数
ZSCORE key member
```

有序集合底层有两种：
1. `skiplist` 跳表
   - 在链表的基础上增加了多级索引，增删改查的复杂度均为 `O(N)`
   - 跳表特别适合 `ZRANGE` 这种范围查找
2. `hashtable` 哈希表
    - 用于快速获取元素，如 `ZSCORE`, `ZADD`, `ZREM`


### 1.5 比特（Bitmaps）
- 由字节流组成的数组。
- setbit key 10 1 # 把第十个比特设置成 1
- getbit key 10
- bitcount key # 数一下有多少个 1
- bitop 比特操作，支持 AND, OR, XOR, NOT
- bitpos 返回第一个 0 或者 1 的比特位置


### 1.6 HyperLogLogs
- 概率数据结构，用来估计集合的势（cardinality）

---

## 2 分布式锁

### 2.1 最简单版本的分布式锁
```bash
# 直接加锁
set lock_name thread_name nx ex 100

# 释放锁
del lock_name
```

改进点1：分布式锁的误删
- 线程1先获取锁，执行业务阻塞，直到redis锁超时自动删除，但是此时线程1还在执行。
- 线程2在锁超时后可以重新获取锁，但是可能会被线程1误删除。
- 线程3会乘虚而入，和线程2存在数据竞争的问题，此时是线程不安全的。
- 改进思路：释放锁之前，先判断下是不是自己的锁。


改进点2：分布式锁的原子性问题
- 上述的改进点存在问题，即在判断是否是自己的锁和释放锁之间，可能会阻塞（比如full GC），此时有可能超时释放锁，仍然再存数据竞争的问题。
- 解决方法：用 lua 脚本编写上面的逻辑（判断是不是自己的锁，然后删除锁），脚本执行是原子性的。

```bash
# 执行 lua 脚本，相当于执行 `SET name bruce`
eval "redis.call('set', 'name', 'bruce')" 0

# 带参数的脚本
eval "return redis.call('set', KEYS[1], ARGV[1])" 1 name bruce
```

```lua
if (redis.call('get', KEYS[1]) == ARGV[1]) then
    return redis.call('del', KEYS[1])
end
return 0
```

### 2.2 Redssion

上面的分布式锁仍然存在问题
1. 不可重入：函数A调用函数B，两个函数都需要用同一把锁，此时会死锁。
2. 不可重试：没有重试机制，等等可能锁就释放了。
3. 超时释放：超时释放锁可能会有问题。
4. Redis主从一致性：Redis分布式集群存在同步延迟。

可以用 Redission 解决，这个是基于 Java 封装的分布式锁。

**1. 可重入锁的原理**
- 原本用的是 set key value，现在用 mset key field count
- 每次重复一次，记录一下次数，直到次数为 0，再删除锁。

**2. 重试锁的原理**
- 先尝试获取所，如果失败了，则订阅一下释放锁的事件。直到超时。

**3. 超时释放的原理（看门狗机制）**
- 启动一个看门狗线程，不断刷新过期时间，永远续期
- 如果当前进程挂了，那么看门狗线程也会挂，就不会续期，也就会执行过期。
- 释放锁时，记得停止看门狗线程。

**4. 主从一致性问题**
- 设置多个主节点，获取锁也要在每个主节点上获取，叫做连锁（`MultiLock`）。
- 这样当一个主节点宕机，也不会影响整体的分布式锁。
