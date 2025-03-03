## 0. 概述
mysql 5.7 & 8.0 是两个经典的版本。

几个命令行：
- `mysqld` 是 MySQL 的 daemon 服务。
- `mysqld_safe` 会间接调用 mysqld，还会启动另一个监控进程，可以重启后台。而且出错时可以把出错信息定位到日志里。
- `mysql.server` 类似 `mysqld_safe`，没找到这个命令。
- `mysql` 客户端命令。

配置文件在 `/etc/mysql/mysql.conf.d/mysqld.cnf`.
日志在 `/var/log/mysql/error.log` 文件里。


## 1. 安装与初始化

Ubuntu 下安装 server 和 client

```bash
# 1. mysql-server
# 包括MySQL服务器守护进程 (mysqld)，数据库引擎，服务器端配置文件
sudo apt install mysql-server

# 2. mysql-client
# 包括MySQL命令行客户端 (mysql)，其他客户端工具，如 mysqladmin, mysqldump, mysqlimport 等
sudo apt install mysql-client
```

Mac下安装 mysql
```bash
# 安装服务端和客户端
brew inistall mysql

# 启动服务
brew services start mysql

# 修改密码（可选）
mysql_secure_installation

# 进入 mysql
mysql -u root -p
```

启动 mysql 守护进程

```bash
# 立即启动服务，并且设置开机启动
sudo systemctl start mysql
# 设置开机启动
sudo systemctl enable mysql

# 下面的命令不太推荐，service 是个老版本的命令
sudo service start/status/stop mysqld    # 启动 mysql 后台服务
```

连接数据库
```bash
# 在 Ubuntu 上，具体是 `/user/bin/mysql` 和 `/usr/sbin/mysqld`. 
# 默认连接是没有密码的。
sudo mysql -u root
```

用户和密码管理
```bash
# 重设密码
/usr/bin/mysqladmin -u root password 'new-password'
```

在 MySQL里创建新用户
```sql
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'your_password';
```

修改用户密码
```sql
ALTER USER 'username'@'localhost' IDENTIFIED BY 'newpassword';
FLUSH PRIVILEGES;
EXIT;
```

给用户 `admin` 控制数据库 `mydb` 的所有权限。
```sql
GRANT ALL PRIVILEGES ON mydb.* TO 'admin'@'%';
FLUSH PRIVILEGES;
EXIT
```

**允许远程访问**

直接编辑 `/etc/mysql/my.cnf`，配置 `bind_address: 0.0.0.0`。


## 2. 数据库相关操作

### 2.1 数据库管理
```sql
show full processlist;      # 查看所有进程
kill <pid>;                 # 杀死某个进程
```

### 2.2 查看数据库
```sql
show databases;             # 展示所有的数据库
use research_platform;     # 使用该数据库
show tables;                # 展示数据库中所有的表
describe team;              # 描述表 team 有哪些属性

# 修改数据库
create database fisheries;      # 创建数据库（注意 sql 语句有分号）
drop database fisheries;        # 删除数据库
```

```bash
# 导入数据
mysqlimport -u root -p --local mytbl dump.txt

# 导出数据
mysqldump -u root -p RUNOOB runoob_tbl > dump.txt

# 导入数据
# 方法1：不行
LOAD DATA LOCAL INFILE "/var/lib/mysql-files/area.sql" INTO table OperationArea;
# 方法2：可以！
mysql -u root -p table_name < area.sql
```

查看数据库表占据的空间大小
```
SELECT
    table_schema AS 'Database',
    SUM(data_length + index_length) / 1024 / 1024 AS 'Size (MB)'
FROM
    information_schema.tables
GROUP BY
    table_schema;
```

### 2.3 表相关操作
表管理
```sql
# 创建表
create table images(url varchar(20), label varchar(20));

# 修改属性
alter table images add i INT;
alter table images drop i

# 清空表格
truncate images
drop table images;    # 删除表；

新建列
alter table table_name add column column_name string(32) not NULL default '0'
```

查询表
```sql
# 查询数据
select conf_id, title from conference_news where news_id > 10 or news_id < 3;
distinct
# where 子句，相当于 if，用做条件过滤
SELECT * from runoob_tbl WHERE runoob_author='菜鸟教程';

# like 子句，相当于 grep，用做字符串搜索过滤
SELECT * from runoob_tbl WHERE runoob_author LIKE '%COM';

# union 子句，用于连接两个 select 结果

# order by 子句，排序规则
SELECT * from runoob_tbl ORDER BY submission_date ASC; （ASC升序默认，DESC降序）

# group by 子句，分组，通常用于配合聚合函数，如 COUNT，AVG，SUM，MAX，MIN 等；
SELECT name, COUNT(*) FROM employee_tbl GROUP BY name;

# having 子句，类似 where，用于过滤条件，但是只能和 group by 一起用，用于分组后；
# where 则是分组前过滤，且 where 子句不能包含聚合函数；
select camp, MIN(register_time) as register_time from roles \
    group by camp HAVING register_time > '2018-12-01 00:00:00';

# LIKE查询语句，匹配字符串，默认忽略大小写，用 % 替代任意符号，类似正则里的 *
# % 任意多个字符; _任意单个字符；
select * from RiderUser where username like '%bruce*';

# 正则表达式
SELECT name FROM person_tbl WHERE name REGEXP '^[aeiou]|ok`$';
```

修改表数据
```sql
# 插入数据
insert into images (url, label) values ("<http://www.baidu.com>", “porn")
insert into conference_news (conf_id, title, link) values (1, "title", "<http://www.sysu.edu.cn>");

# 更新数据
update table_name SET field1=value1, field2=value2;

# 更新json字段：
update RiderUser set json=JSON_SET(json, "$`.max_waiting_time_before_dispatch", 20) where id=2;

# 删除数据
delete from conference_news where conf_id = 2;
delete from conference_news where title = "title”;
```

### 2.4 连接
**inner join 内连接，等值连接**：求两个表的交集；
```sql
SELECT a.runoob_id, a.runoob_author, b.runoob_count FROM runoob_tbl a INNER JOIN tcount_tbl b ON a.runoob_author = b.runoob_author;
```

**left join，左连接**：保留全部左表的数据，语法把 inner 换成 left 即可；

**right join，右连接**：保留全部右表的数据，语法把 inner 换成 right 即可；

### 2.5 json格式

参考：[深入了解 MySQL 的 JSON 数据类型（关系型数据库里的 NoSQL 初）](https://learnku.com/laravel/t/13185/in-depth-understanding-of-json-data-type-of-mysql-nosql-in-relational-database)

1. 增加
    - 在 insert 时直接作为参数带进去，可以存任何对象。
    - `JSON_OBJECT(key1, value1, key2, value2, ... kn, vn)`
        - 构建 JSON 对象，其实就是 dict；
    - `JSON_ARRAY(a1, a2, ... an)`
        - 构建 JSON 数据
    - `JSON_MERGE(obj1, obj2, ... objn)`
        - 可以合并多个元素成一个 JSON 对象
2. 查找
    - `JSON_EXTRACT('json', '$.attr.subattr')`
        - 读取 json 字段的某个属性
        - 可以当做普通的字段名使用，比如放在 where 语句中；
        - 也可以用 `->` 别名代替，如 `'json'->'$.attr.subattr`;
3.更新
    - `JSON_INSERT('json', '$.attr.subattr', 'new value')`
        - 增加一个属性值；（没有这个属性才会执行）
    - `JSON_REPLACE('json', '$.attr.subattr', 'updated value')`
        - 更新一个属性值（有这个属性才会执行）
    - `JSON_SET('json', '$.attr.subattr', 'updated value')`
        - 创建或者更新一个属性值
4. 删除
    - `JSON_REMOVE('json', '$.attr.subattr')`
        - 删除一个属性值

## 3. 索引

建立索引对于数据库的检索至关重要
- 创建索引：`CREATE INDEX indexName ON table_name (column_name)`
- 删除索引：`DROP INDEX [indexName] ON mytable;`
- 唯一索引：`CREATE UNIQUE INDEX indexName ON mytable(username(length))`
- 修改索引：`ALTER TABLE testalter_tbl ADD INDEX (c);`
- 显示索引：`SHOW INDEX FROM table_name;`

视图
虚拟的表。

安全
防止 sql 注入，不要相信用户的输入，要做校验；


## 4. 慢查询

用 `explain`，`show profiling` 命令解析查询的细节。

1. 索引设计优化
2. join表过多，需要优化
3. 数据表设计优化

如果 SQL 查询达到瓶颈
1. 读写分离（主从架构）
2. 分库分表

用 `mysqldumpslow` 命令把慢查询导出到本地。


## 5. 备份
备份的方案：
1. 物理备份：用 `xtrabackup` 工具来进行物理备份。
2. 逻辑备份：用 `mysqldump` 备份所有的 sql 语句。
    - 用 `mysqldump -u root -p --database > backup.sql` 备份数据
    - 用 `mysql -u root -p [dbname] < backup.sql` 恢复数据

## 6. 其他

修改 mysql 的默认密码
```sql
show databases;
use mysql;
update user set authentication\_string=PASSWORD("自定义密码") where user='root';
update user set plugin="mysql\_native\_password";
flush privileges;
quit;
```

重启 server
```bash
/etc/init.d/mysql restart;
sudo service mysql restart
```

## 7. 常见面试题

**drop、delete、truncate 有什么区别**
drop 会删除表结构，delete删除某些行数据、truncate 只保留表结构；drop 最快，delete 最慢
delete 语句是 dml，这个操作会放到 rollback segement 中，事务提交之后才生效。其他两个语句不能回滚；

**MYSQL 常见的引擎**

*   InnoDB（默认）
    *   优点：支持事务安全，对外键支持较好；
    *   缺点：耗空间和内存，插入速度较低
*   MyISAM
    *   优点：插入速度快
    *   缺点：
        - 存放于内存中，速度快，但是安全性不高；
        - 不能建立很大的表；

** MYSQL 的一些术语 **
- Schema，在 MYSQL 中，等于 database，其他一些数据，分database->schema->table三种层级。
- catalog，关系型数据库没有这个概念，其他的地方（特别是大数据领域的一些组件），用来做层级划分，比 database 等级大。是 database 的目录。
- collate，排序规则，自负编码
