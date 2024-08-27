
## 事务

几个步骤
- `@EnableTransactionManagement` 开启事务注解的支持
- `TranactionManager` 把该组件放到容器里。
- `@Transactional` 添加事务，可以放到类或者方法上。
    - `@Transactional(readonly = false)` 只读模式的事务，提升效率，建议在类上加。
    - `@Transactional(timeout = 3)` 超时则抛出异常，事务回滚。
    - `@Transactional(rollbackFor = Exception.class)` 默认情况，只有发生 `RuntimeException` 才会回滚，这里可以指定。
    - `@Transactional(noRollbackFor = FileNotFoundException.class)` 指定不会滚。
    - `@Transactional(isolation = Isolation.READ_COMMITTED)` 指定隔离级别
    - `@Transactional(propagation = Propagation.REQUIRED)` 传播方法，
        - `REQUIRED`，（建议）如果父方法有事务，就加入；否则新建。
        - `REQUIRES_NEW` 直接新建事务，子事务是独立的。
        - ... 更多的选项参考文档


事务的并发问题
1. 脏读 (Dirty Read) 
    - 一个事务读取了另一个未提交事务的数据，若该事务回滚，这些读取的数据就变得无效。
    - 事务A更新了某条记录，事务B读取了该未提交的记录。如果事务A回滚，事务B读取的数据就是“脏”的。
2. 不可重复读 (Non-Repeatable Read) 
    - 一个事务在多次读取同一数据时，由于另一个事务的提交导致读取结果不同。
    - 事务A第一次读取数据，事务B修改并提交了该数据，事务A再次读取时发现数据已被更改。
3. 幻读 (Phantom Read) 
    - 一个事务在多次查询期间，由于另一个事务的插入或删除导致结果集中出现了“幻影”记录。
    - 事务A查询了满足某条件的记录集，事务B插入了一条新记录。事务A再次查询时，发现多出了一条“幻影”记录。


**事务的隔离级别**

| 隔离级别             | 概述                                                         | 解决问题                   | 典型问题                       | 并发性       |
|----------------------|--------------------------------------------------------------|----------------------------|--------------------------------|--------------|
| 读未提交 (Read Uncommitted) | 允许事务读取到未提交的数据。                                       | 无                          | 脏读、不可重复读、幻读           | 最高         |
| 读已提交 (Read Committed)   | 只能读取已提交的数据。大多数数据库的默认隔离级别。                   | 防止脏读                    | 不可重复读、幻读                 | 较高         |
| 可重复读 (Repeatable Read)  | 确保在同一事务中多次读取数据的结果一致。MySQL InnoDB 默认隔离级别。  | 防止脏读、不可重复读         | 幻读                            | 较低         |
| 可串行化 (Serializable)     | 强制事务顺序执行，避免所有并发问题。                                | 防止脏读、不可重复读、幻读   | 性能较低，适用于小规模数据操作   | 最低         |
