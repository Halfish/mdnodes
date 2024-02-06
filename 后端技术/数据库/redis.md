# redis 

![](https://redis.io/images/redis.png)

- 首页：https://redis.io
- 中文首页：https://www.redis.com.cn/

redis 是基于 BSD 协议开源的内存型数据结构存储系统，用于做数据库、缓存和消息中间件。

redis 支持的数据结构

---

因为 redis 是个 key-value 的服务器，但是 value 支持更多的类型。

###  字符串（String，用 set 和 get 命令）

- 存储的字符串（包括 key 和 value）是二进制安全的（binary-safe），即不会解析任何的字符串，仅仅当做原始的字符串流。
- 像 C++ 中的字符串会以 \0 作为字符串的结束符，这就不是 binary-safe 的。
- 可以用来存储二进制文件，如图片音频等，字符串的大小不能超过 512M。

```bash
# 设置键值，EX 是过期时间，NX 表示不强制覆盖
$ SET key value [EX seconds] [PX milliseconds] [NX|XX]
$ GET key
$ DEL key [key ...]
```

### 哈希（Hash，HMSET，HGET 命令）
- 和 Python 中的字典（dict）、Ruby 中的哈希很像
- 存储如 `{'name': 'bruce', 'age': '14'}` 这样的数据结构
- HMSET 最多支持 `2^32 - 1` 个键值对

```bash
$ HMSET key field value [field value ...]
$ HMGET key field [field ...]

$ HSET key field value
$ HGET key field

$ HGETALL *
```

### 列表（List，lpush lrange）
- 其实是链表，根据插入的次序来排序的字符串集合
- 插入和删除的复杂度是 `O(1)`，但是索引的效率很低
- lpush, rpush 来插入元素，lrange 类似 python 里的切片，lpop，rpop 操作
- 列举下面两种 lists 使用的场景
    - 社交网络中用户最后 post 的更新。
    - 消费者-生产者模型里的消息队列
- 用 ltrim 来设置 list 的个数上限。
- brpop、blpop 来做 block 操作，如果 list 说空的，会等待直到不为空。

```bash
# 插入链表左边/右边
$ LPUSH/RPUSH key value [value ...]

# 返回 [start, stop] 范围内的链表元素
$ LRANGE key start stop
```

### 比特（Bitmaps）
- 由字节流组成的数组。
- setbit key 10 1 # 把第十个比特设置成 1
- getbit key 10
- bitcount key # 数一下有多少个 1
- bitop 比特操作，支持 AND, OR, XOR, NOT
- bitpos 返回第一个 0 或者 1 的比特位置

### 集合（Set，sadd 命令）
有两种集合，`无序集合 set` 和`有序集合 zset`，都不允许重复元素

**无序集合**，只支持字符串的集合，无序集合中最多可以存放 `2^32 - 1` 个元素。
```bash
# 添加元素到集合中
$ SADD key member [member ...]

# 查看集合所有元素
$ SMEMBERS key
```

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
```
# 取范围内的元素，withscore 则一起返回分数；（比如用来取前 10 的排）
ZRANGE key start stop [WITHSCORES]      # 升序
ZREVRANGE key start stop [WITHSCORES]   # 降序

# 取某些分数范围内的元素
ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count]
```

# HyperLogLogs
- 概率数据结构，用来估计集合的势（cardinality）

---


分布式锁？redis.lock.Lock
redis 和 lua 有什么关系
- redis 的事务竟然是假的？！
