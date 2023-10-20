
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

