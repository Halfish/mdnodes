
Alembic是一个轻量级的数据库迁移工具，是 SQLAlchemy 的 python 版数据库迁移工具.

- 官网：https://alembic.sqlalchemy.org/en/latest/
- 代码库：https://github.com/sqlalchemy/alembic
- 安装：`pip install alembic`

### 迁移环境 Migration Environment
```bash
yourproject/
    alembic/
        env.py
        README
        script.py.mako
        versions/
            3512b954651e_add_account.py
            2b1ae634e5cd_add_order_id.py
            3adcc9a56557_rename_username_field.py
```

- `yourproject` 是项目的目录
- `alembic` 目录下的文件是迁移环境
- `env.py` 提供连接 SQLAlchemy 数据库的功能
- `script.py.mako` 是 Moko 模板文件，用来产出 versions/ 目录下的迁移脚本

通过命令 `alembic init alembic` 创建迁移环境，会生成上述的目录和文件
通过命令 `alembic revision -m "create account table"` 创建迁移脚本，会在 versions/ 目录下生成一个 123abc_create_account_table.py 文件

可以在脚本里写数据库的操作，如添加、删除一个表等。
```python
from alembic import op

def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

def downgrade():
    op.drop_table('account')
```
更多操作参考：https://alembic.sqlalchemy.org/en/latest/ops.html

```bash
# 首次迁移
alembic upgrade head

# 再次迁移
alembic revision -m "add username table"
alembic upgrade head

# 其他操作方法
alembic upgrade abc123
alembic upgrade +2
alembic downgrade -1
alembic upgrade abc123+3
```

其他操作
```bash
# 查看当前版本
alembic current

# 查看历史版本
alembic history --version
alembic history -r-3:current

# 版本回退
alembic downgrade base

```
