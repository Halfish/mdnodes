# 增查改删 CRUD

参考：[深入了解 MySQL 的 JSON 数据类型（关系型数据库里的 NoSQL 初）](https://learnku.com/laravel/t/13185/in-depth-understanding-of-json-data-type-of-mysql-nosql-in-relational-database)

## 1. 增加
- 在 insert 时直接作为参数带进去，可以存任何对象。
- `JSON_OBJECT(key1, value1, key2, value2, ... kn, vn)`
    - 构建 JSON 对象，其实就是 dict；
- `JSON_ARRAY(a1, a2, ... an)`
    - 构建 JSON 数据
- `JSON_MERGE(obj1, obj2, ... objn)`
    - 可以合并多个元素成一个 JSON 对象


## 2. 查找
- `JSON_EXTRACT('json', '$.attr.subattr')`
    - 读取 json 字段的某个属性
    - 可以当做普通的字段名使用，比如放在 where 语句中；
    - 也可以用 `->` 别名代替，如 `'json'->'$.attr.subattr`;


## 3.更新
- `JSON_INSERT('json', '$.attr.subattr', 'new value')`
    - 增加一个属性值；（没有这个属性才会执行）
- `JSON_REPLACE('json', '$.attr.subattr', 'updated value')`
    - 更新一个属性值（有这个属性才会执行）
- `JSON_SET('json', '$.attr.subattr', 'updated value')`
    - 创建或者更新一个属性值

## 4. 删除
- `JSON_REMOVE('json', '$.attr.subattr')`
    - 删除一个属性值