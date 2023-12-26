### InfluxDB

时序数据库

参考：
- [官方文档](https://jasper-zhang1.gitbooks.io/influxdb/content/)

概念：
- database，数据库
- measurement：相当于数据库中的表
- point：表里的一行数据
- time：记录时间，主索引，会自动生成
- fields：没有索引的属性
- tags：有索引的属性
- series：特定tag下的某个制定指标的时序取值集合


### influxDB 数据存储架构
每个 database 可以有多个 RP（retention policy数据保存策略），但是只有一个默认策略。

### 基本操作

```bash
# 数据库相关
show databases
create database mydb1
drop database mydb1
use mydb1

# 表操作
show measurements
select * from weather
insert weather,altitude=1000,area=北 temp=11,humidity=-4
drop measurements weather

# 用户操作
show users
CREATE USER influx WITH PASSWORD ‘influxdb’;
SET PASSWORD FOR influx = ‘influx’
drop user admin;
```

---


用  grafana 去可视化；