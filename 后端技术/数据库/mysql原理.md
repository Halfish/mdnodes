
mysql 5.7 & 8.0 是两个经典的版本。

### MySQL server 层的查询步骤

服务端接收和处理客户端的请求，主要有下面几个工作
1. 创建和维护连接池和线程池，负责和不同的客户端通信。
2. 做账号认证，以及权限的管理。

在把 SQL 送到存储引擎真正查询 SQL 语句前，主要可以分成三步：
1. **查询缓存**：看下有没有一样的命令。由于效率不高，所以 MySQL 8.0 后删除了这个。
2. **语法解析器**：词法分析（分析关键字）+ 语法分析（分析语法）。
3. **优化器**：
    - 决定是全表检索还是按照索引检索。
    - 优化语句，如外连接转成内连接、表达式简化、子查询转成连接等。
    - 可以用 `EXPLAIN` 语句来查看某个语句的执行计划。

后续把执行计划送到存储引擎里执行。

### 存储引擎
存储引擎主要负责数据的存储、提取和写入操作。不同的存储引擎向 MySQL server 提供统一的调用接口，包含了几十个底层函数。

`SHOW ENGINES` 可以查看所有支持的引擎。


### 环境变量
`SHOW VARIABLES LIKE 'default_storage_engine';`
`SHOW VARIABLES like 'max_connections';`
`SHOW VARIABLES LIKE 'default%';`

### 编码
MySQL中的 `utf8` 编码其实是 `utf8mb3`的别名，阉割了补充字符，只支持 BMP 字符集，即 0~65535 之间的字符。不支持补充字符集，所以一些生僻字，或者 emoji 符号是没法显示。

如果需要的话，可以用 `utf8mb4`（2010年，5.5.3版本引入），这个才是真正的 utf8 编码。

### InnoDB
InnoDB 的内存和磁盘之间读写，都是以页为单位，每次至少16KB；

InnoDB 行格式有 `Compact, Redundant(MySQL<5.0), Dynamic, Compressed` 四种。用于存储行数据的序列化。
```bash
mysql> CREATE TABLE record_format_demo (
    ->     c1 VARCHAR(10),
    ->     c2 VARCHAR(10) NOT NULL,
    ->     c3 CHAR(10),
    ->     c4 VARCHAR(10)
    -> ) CHARSET=ascii ROW_FORMAT=COMPACT;
Query OK, 0 rows affected (0.03 sec)
```

- Compact，最经典；
- Redundant，在 MySQL 5.0 之前会用，已经废弃。
- Dynamic，默认的格式，一点点区别。
- Compressed，在 Dynamic 的基础上压缩以节省空间。

### 数据页

### NULL
1. count(*) 正常，count(col) 会忽略 NULL 数据。
2. 执行非等于查询 > < != 时，会忽略 NULL 数据。只能加上 `isnull(col)` 才行。
3. sum() 包含 NULL 时，结果为 NULL；
4. 增加了查询难度，如 col != null, col <> null 都不能用，只能用 `isnull(col)` 或者 `is not null`.


### 日志
参考：
- https://javaguide.cn/database/mysql/mysql-logs.html
- https://juejin.cn/post/7068299741888512031

redo 日志是物理日志，会刷新硬盘。让 mysql 有回复崩溃的能力。
binlog 是逻辑日志，记录了数据库的更新操作。保证了数据库集群架构的一致性。

```bash
# 是否启用binlog日志
show variables like 'log_bin';
​
# 查看详细的binlog日志配置信息
show global variables like '%log%';
​
# 查看binlog的目录
show global variables like "%log_bin%";
​
# 查看binlog文件日志列表
show binary logs;
​
# 查看最新一个binlog日志文件名称和Position（操作事件pos结束点）
show master status;
​
# 刷新log日志，自此刻开始产生一个新编号的binlog日志文件
# 每当mysqld服务重启时，会自动执行此命令，刷新binlog日志；在mysqldump备份数据时加 -F 选项也会刷新binlog日志；
flush logs;
​
# 查看第一个binlog文件内容
show binlog events  
​
# 查看具体一个binlog文件的内容
show binlog events in 'master.000001';
​
# 重置(清空)所有binlog日志
reset master;
​
# 删除slave的中继日志
reset slave;
​
# 删除指定日期前的日志索引中binlog日志文件
purge master logs before '2022-02-22 00:00:00';
​
# 删除指定日志文件
purge master logs to 'master.000001';
```

### GTID
博客链接
- [深入理解 MySQL 5.7 GTID 系列（一）](https://cloud.tencent.com/developer/article/1395925)
- [深入理解MySQL 5.7 GTID系列（二）：GTID相关内部数据结构](https://cloud.tencent.com/developer/article/1396288)

MySQL GTID是 5.6 版本加入的一个强大的特性。

Mysql GTID 全称为Global Transaction Identifie，在整个复制的过程中完全唯一。即主从数据库中数据迁移时，这个值始终是一样的。

全局变量
- `GTID_EXECUTED` 已经执行的 GTID 集合；
- `GTID_PURGED` 已经清楚的 GTID 集合；


### 日志

日志类型
1. `二进制日志`：记录所有更改数据库的语句
    - 数据复制：用于主从服务器同步
    - 数据恢复：用于数据库故障时的恢复。
    - `show variables like '%log_bin%'` 查看bin日志路径
    - `mysqlbinlog -v /var/lib/mysql/binlog.000064`
    - 可以用 `mysqlbinlog` 直接恢复数据
    - `show binlog events in binlog.000064`
2. `错误日志`：记录error级别的日志
    - `show variables like '%log_err%'` 查看错误日志路径
3. `通用查询日志`：记录用户所有的操作，如指令，连接等
    - `show variables like '%general%'`
    - `set global general_log=on` 打开通用日志
4. `慢查询日志`：查询时间超过 `long_query_time` 的查询。
5. `中继日志(replay log)`：从服务器（slave server）读取的日志，用于同步数据
6. `数据定义语句日志`：记录数据定义语句执行的元数据操作。


redo log 和 bin log 区别？
- redo Log 是物理日志，记录磁盘和数据页的修改。bin log 是逻辑日志，记录数据做了什么操作。
- redo log 用于事务的持久性；bin log 用于主从数据库的数据一致性。


### 主从同步
主从同步主要有三个线程：
1. `二进制日志转储线程`，发送更新的二进制日志 binlog 给从库。（写binlog是另外的程序）
2. `从库 I/O 线程`，从库主动连接到主库，请求 binlog 更新部分，并拷贝到本地的中继日志。
3. `从库 SQL 线程`，读取从库中的中继日志，执行日志中的事件。最终保持主从同步。


### 数据的三大范式

键的概念
- 超键：能唯一标志元组的属性集合叫做超键
- 候选键：如果超键不包含多余的属性，这个超键就是候选键
- 主键：从候选键集合中选一个作为主键
- 外键：某个键是表1的主键，但是不是表2的主键，就叫做表2的外键。

三大范式：
- 第一范式（1NF）
    - 尽量拆分列
    - 每个列都不可以再拆分，为了确保数据表中每个列具有**原子性**。
- 第二范式（2NF）
    - 尽量拆分表
    - 在第一范式的基础上，非主键列完全依赖于主键，而不能是依赖于主键的一部分。
    - 不拆分表，增删改查数据时有很多问题。
- 第三范式（3NF）
    - 非主键列之间不能有关系
    - 在第二范式的基础上，非主键列只依赖于主键，不依赖于其他非主键。
    - 如员工表和部门表两个表，员工表里可以由部门ID，但是没必要有部门名称和部门介绍等列。

更多范式：
- 巴斯-科德范式（BCNF）
- 第四范式（4NF）
- 第五范式（5NF）

范式的优缺点：
- 优点：有助于消除数据冗余
- 缺点：降低了查询效率，因为要做表关联。

反范式化：
- 实际工作中，范式只是一种标准，不一定要严格遵循
- 可以通过一定的冗余来减少表关联，从而提升查询性能。
