
### 初始化

mysql 5.7 & 8.0 是两个经典的版本。

几个命令行：
- `mysqld` 是 MySQL 的 daemon 服务。
- `mysqld_safe` 会间接调用 mysqld，还会启动另一个监控进程，可以重启后台。而且出错时可以把出错信息定位到日志里。
- `mysql.server` 类似 `mysqld_safe`，没找到这个命令。
- `mysql` 客户端命令。

在 Ubuntu 上，具体是 `/user/bin/mysql` 和 `/usr/sbin/mysqld`. 没有密码。

配置文件在 `/etc/mysql/mysql.conf.d/mysqld.cnf`.

`sudo mysql -u root` 可以直接进去.

### MySQL server 层的查询步骤
客户端发起请求，客户端接收请求，处理后返回结果，这中间值主要可以分成三步：
1. 查询缓存：看下有没有一样的命令。MySQL8.0后删除了这个。
2. 语法解析：解析语法。
3. 查询优化：优化语句，如外连接转成内连接、表达式简化、子查询转成连接等。可以用 `EXPLAIN` 语句来查看某个语句的执行计划。

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
