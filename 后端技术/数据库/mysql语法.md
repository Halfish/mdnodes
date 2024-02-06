# 1. 安装与初始化
```
# 安装
sudo yum install mysql
sudo yum install mysql-server
conda install mysql

sudo apt install mysql-server
sudo apt install mysql-client

# 启动
sudo service start/status/stop mysqld    # 启动 mysql 后台服务
sudo systemctl start/status/stop mysqld
/usr/bin/mysqladmin -u root password 'new-password’    # 重设密码
/usr/bin/mysqladmin -u root -h zhangxiaobin.bcc-szth.baidu.com password 'new-password’    # 重设密码
```

# 2. 数据库相关操作

## 2.1 数据库管理
```
show full processlist;      # 查看所有进程
kill <pid>;                 # 杀死某个进程
```

## 2.2 查看数据库
```
show databases;             # 展示所有的数据库
use research_platform;     # 使用该数据库
show tables;                # 展示数据库中所有的表
describe team;              # 描述表 team 有哪些属性

# 修改数据库
create database fisheries;      # 创建数据库（注意 sql 语句有分号）
drop database fisheries;        # 删除数据库

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

## 2.3 表相关操作
表管理
```
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
```
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
```
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

## 2.3 连接
**inner join 内连接，等值连接**：求两个表的交集；
```
SELECT a.runoob_id, a.runoob_author, b.runoob_count FROM runoob_tbl a INNER JOIN tcount_tbl b ON a.runoob_author = b.runoob_author;
```

**left join，左连接**：保留全部左表的数据，语法把 inner 换成 left 即可；

**right join，右连接**：保留全部右表的数据，语法把 inner 换成 right 即可；

# 3. 事务（transaction）

事务具有四个条件，ACID
- 原子性，Atomicity，一个事务的所有操作，要么全部完成，要么全部不完成。执行错误时需要回滚。
- 一致性，Consistency，在事务开始之前和事务结束以后，数据库的完整性没有被破坏。
- 隔离性，Isolation，允许多个事务并发执行。
- 持久性，Durability，事务处理结束后，对数据的修改是永久的，及时系统故障也不会丢失。可以在 SQL 语句两端执行事务的指令：BEGIN, ROLLBACK, COMMIT 等；

# 4. 索引

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

# 5. 其他

修改 mysql 的默认密码
```
show databases;
use mysql;
update user set authentication\_string=PASSWORD("自定义密码") where user='root';
update user set plugin="mysql\_native\_password";
flush privileges;
quit;
```

重启 server
```
/etc/init.d/mysql restart;
sudo service mysql restart
```

# 6. 常见面试题

**drop、delete、truncate 有什么区别**
drop 会删除表结构，delete删除某些行数据、truncate 只保留表结构；drop 最快，delete 最慢
delete 语句是 dml，这个操作会放到 rollback segement 中，事务提交之后才生效。其他两个语句不能回滚；

**超键、候选键、主键、外键的区别**
- 超键：super key，在关系中能够表示元素的属性集（可以有多个属性）称为关系模式的超键。
- 候选键：是最小的超键，即没有冗余元素的超键
*- 主键：数据库表中对存储数据对象予以唯一和完整标示的数据列或属性的组合。一个数据里只能有一个主键，且不能确实或者为 null；
- 外键：在当前表中存在另一个表的主键，称为此表的外键。

**数据的三大范式**
- 第一范式：每个列都不可以再拆分
- 第二范式：在第一范式的基础上，非主键列完全依赖于主键，而不能是依赖于主键的一部分。
- 第三范式：在第二范式的基础上，非主键列只依赖于主键，不依赖于其他非主键。

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
