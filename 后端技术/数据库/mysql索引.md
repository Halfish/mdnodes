参考：
-[廖雪峰-数据库索引](https://www.liaoxuefeng.com/wiki/1177760294764384/1218728442198976)

# 索引（Index）
什么是索引？索引是**关系数据库**中对某一列或多个列的值进行**预排序**的数据结构，一般是用 `B/B+` 树这样的结构。树的节点由 key，value 对组成，key 是已排序的索引列，value 是指向数据行的指针。

索引能够加快数据检索的速度，但是也会带来修改数据库（插入、修改、删除）的性能损失。

下面是一些创建所以的 SQL 语句示例。
```sql
# 创建索引
ALTER TABLE students ADD INDEX idx_score (score);
ALTER TABLE students ADD INDEX idx_name_score (name, score);

# 创建唯一索引，以约束该列的唯一性
ALTER TABLE students ADD UNIQUE INDEX uni_name (name);
# 仅创建唯一约束，而不创建索引
ALTER TABLE students ADD CONSTRAINT uni_name UNIQUE (name);
```

## 聚簇索引 (Clustered Index)
数据行的物理顺序和索引的排列顺序相同，一个表只能有一个聚簇索引。

搜索范围时特别有效。

## 非聚簇索引 (Nonclustered Index)
又叫二级索引
