

安装 ```pip install sqlalchemy```

参考官方文档：https://docs.sqlalchemy.org/en/14/tutorial/index.html

sqlalchemy 库分成两个模块，分别是
1. CORE
2. ORM，Object Relational Mapping，指的是把数据库的表结构用对象表示；


### 一、连接数据库
```python
from sqlalchemy import create_engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
```
这里的 `engine` 类型是 `sqlalchemy.future.Engine` 会维护一个线程池，负责和 sql 的长连接。

这里的 sqlite+pysqlite 是支持的一种方言，底层用了 `DBAPI` 来和数据库通信，支持的方言包括
1. sqlite+pysqlite
2. mysql+mysqldb
3. postgresql+psycopg2

这里的 `DBAPI` 指的是 "Python Database API Specification"，是 python 和数据库交流的底层接口，如 [psycopg2](https://www.psycopg.org/)，[mysqlclient](https://github.com/PyMySQL/mysqlclient) 等，能够提供连接数据库，执行 SQL 语句的功能。

代码中的 URL 结尾处是 `memory`，意思是会用内存中的数据库，而不是真实的数据库，主要用于实验。

### 二、Transction（数据库事务）和 DBAPI
```python
from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.commit()
```
这里的上下文管理器返回的 `conn` 类别是 `sqlalchemy.engine.Connection`，是一个 DBAPI 变量，可以执行 SQL 操作。

`execute` 语句返回的 `result` 是 `sqlalchemy.engine.ResultProxy`，底层是 DBAPI 的外观模式类。

`conn.commit()` 会把执行语句推送到数据库。

ORM 的写法
```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    result = session.execute(text(
        "UPDATE some_table SET y=:y WHERE x=:x"), [{"x": 9, "y":11}, {"x": 13, "y": 15}]
    session.commit()
```

### 三、Database Metadata（数据库元数据）
在 sqlalchemy 里，主要有三类数据库元数据
1. MetaData
2. Table
3. Column

创建表
```python
from sqlalchemy import MetaData
metadata = MetaData()

from sqlalchemy import Table, Column, Integer, String
user_table = Table(
    "user_account",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30), ForeignKey('xx.otherid'), nullable=False)),
    Column('fullname', String)
)
metadata.create_all(engine)
```
这里的概念基本和数据库一致。

ORM 写法
```python
>>> from sqlalchemy.orm import registry
>>> mapper_registry = registry()
>>> mapper_registry.metadata
MetaData()
>>> Base = mapper_registry.generate_base()

# 上面的写法可以合并成一句话
from sqlalchemy.orm import declarative_base
Base = declarative_base()
```

重新定义两个表
```python
>>> from sqlalchemy.orm import relationship
>>> class User(Base):
...     __tablename__ = 'user_account'
...
...     id = Column(Integer, primary_key=True)
...     name = Column(String(30))
...     fullname = Column(String)
...
...     addresses = relationship("Address", back_populates="user")
...
...     def __repr__(self):
...        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

>>> class Address(Base):
...     __tablename__ = 'address'
...
...     id = Column(Integer, primary_key=True)
...     email_address = Column(String, nullable=False)
...     user_id = Column(Integer, ForeignKey('user_account.id'))
...
...     user = relationship("User", back_populates="addresses")
...
...     def __repr__(self):
...         return f"Address(id={self.id!r}, email_address={self.email_address!r})"

>>> User.__table__
Table('user_account', MetaData(),
    Column('id', Integer(), table=<user_account>, primary_key=True, nullable=False),
    Column('name', String(length=30), table=<user_account>),
    Column('fullname', String(), table=<user_account>), schema=None)

>>> sandy = User(name="sandy", fullname="Sandy Cheeks")
>>> sandy
User(id=None, name='sandy', fullname='Sandy Cheeks')
```

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

### 四、操作数据

#### 4.1 insert 函数
```python
>>> from sqlalchemy import insert
>>> stmt = insert(user_table).values(name='spongebob', fullname="Spongebob Squarepants")
>>> print(stmt)
INSERT INTO user_account (name, fullname) VALUES (:name, :fullname)

>>> compiled = stmt.compile()
>>> compiled.params
{'name': 'spongebob', 'fullname': 'Spongebob Squarepants'}

>>> with engine.connect() as conn:
...     result = conn.execute(stmt)
...     conn.commit()

>>> result.inserted_primary_key
(1,)

# 也可以这样写
>>> with engine.connect() as conn:
...     result = conn.execute(
...         insert(user_table),
...         [
...             {"name": "sandy", "fullname": "Sandy Cheeks"},
...             {"name": "patrick", "fullname": "Patrick Star"}
...         ]
...     )
...     conn.commit()
```

#### 4.2 select 函数
```python
>>> from sqlalchemy import select

# CORE 写法
>>> stmt = select(user_table).where(user_table.c.name == 'spongebob')
>>> with engine.connect() as conn:
...     for row in conn.execute(stmt):
...         print(row)
BEGIN (implicit)
SELECT user_account.id, user_account.name, user_account.fullname
FROM user_account
WHERE user_account.name = ?
[...] ('spongebob',)
(1, 'spongebob', 'Spongebob Squarepants')
ROLLBACK

# ORM 写法
>>> stmt = select(User).where(User.name == 'bob').order_by(x).join(y)
>>> with Session(engine) as session:
...     for row in session.execute(stmt):
...         print(row)
```

#### 4.3 update & delete 函数
```python
# update
>>> from sqlalchemy import update
>>> stmt = (
...     update(user_table).where(user_table.c.name == 'patrick').
...     values(fullname='Patrick the Star')
... )
>>> print(stmt)
UPDATE user_account SET fullname=:fullname WHERE user_account.name = :name_1

# delete
>>> from sqlalchemy import delete
>>> stmt = delete(user_table).where(user_table.c.name == 'patrick')
>>> print(stmt)
```

### 五、用 ORM 操纵数据
```python
>>> squidward = User(name="squidward", fullname="Squidward Tentacles")
>>> session = Session(engine)
>>> session.add(squidward)
>>> session.new
IdentitySet([User(id=None, name='squidward', fullname='Squidward Tentacles')])
>>> session.flush()
>>> session.commit()
>>> session.rollback()
>>> session.close()

```

这里 flush 是把 SQL 语句提交到数据库并执行，但是事务并没有结束。
当 commit / rollback / close 被调用时才意味着事务的结束。


### 六、Session
参考：https://docs.sqlalchemy.org/en/13/orm/session_basics.html

概念
- `Engine`
- `Session`
- `Query` 由 Session.query 返回的对象，表示一次请求，还未正式连接数据库。
- `sessionmaker` 用来创建 Session，这样就不用每次都手动配置了。
    - 调用这个函数得在 global scope 的地方，比如 `__init__.py`
- `scopedsession`
    - session scope & transaction scope
    - 每个线程会保存一份 Session
    - 事务的隔离范围是在 create_engine 时就确定的

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# an Engine, which the Session will use for connection
# resources
some_engine = create_engine('postgresql://scott:tiger@localhost/')

# create a configured "Session" class
Session = sessionmaker(bind=some_engine)

# create a Session
session = Session()

# work with sess
myobject = MyObject('foo', 'bar')
session.add(myobject)
session.commit()
```

什么时候commit/close一个 Session？
- Session 在 committed / rolled_back /close 后会结束一个事务（Transaction）
- Session 可以处理多个事务。Session 和 Transaction 并不是一一对应的。

SQL设置了四种隔离级别
1. 读未提交（Read Uncommitted）
2. 读提交（Read Committed）
3. 可重复读（Repeatable Read）
4. 串行化（Serializable）

从上往下，隔离程度逐渐增强，性能逐渐变差。


| 隔离级别 | 脏读 | 不可重复读 | 幻读 |
| --- | --- | --- | --- |
| 读未提交 | X | X | X |
| 读提交  | O | X | X |
| 可重复读 | O | O | X |
| 串行化 | O | O | O |

其中，O 表示可以避免该问题出现，X 表示避免不了。