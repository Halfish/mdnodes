

定义 Column 时
- `default` 字段只是在用 sqlalchemy 客户端时起作用;
- 如果用裸的 sql 语句，需要用 `server_default` 字段。


mysql 中的 Boolean 类型只是 tinyint(1) 的别称。

如何在 sqlalchemy 中指定布尔类型
```python
from sqlalchemy.sql import expression

is_active = Column(Boolean, default=True, server_default='0')       # 可以
is_active = Column(Boolean, default=True, server_default=expression.true())     # 可以

is_active = Column(Boolean, default=True, server_default='t')       # 不可以！
is_active = Column(Boolean, default=True, server_default='true')    # 不可以！
is_active = Column(Boolean, default=True, server_default=text('true'))  # 不可以？

```