# Python 基础知识

## 1. 数据结构

- 字符串
  - 格式化输出，"Bruce: %s -> %d" % ('age', 100)
  - join，split，count，punctuation，find & index （找不到时返回-1 还是异常）
  - b"bruce"，表示 byte，py3.x 的写法，因为字符串在 3 里默认是 unicode
  - r"bruce"，表示原始字符，这里转义字符会失效
  - u"bruce"，表示 unicode，特别是中文字符串的时候用的比较多
- 列表 list []
  - append，insert，pop，extend（合并 list），remove，index，len()，切片访问
  - 合并两个列表 c = a + b （注意是是直接把 b 里的元素接在 a 后面，可以重复）
  - 可以改写，不能做哈希的 key
- 元组 tuple ()
  - 快，有写保护，不可写，可以做哈希的 key
  - 里面的元素是不变的（浅拷贝）
- 字典 dict {} 是用哈希表实现的
  - 访问 d.keys() / d.values() / d.items()
  - 判断是否有键值 `d.has_key('name') # True or False`
  - d.get('key', -1) 可以赋予一个默认值
  - d.setdefault('key', -1) 跟 get 函数类似，但是会改变字典
  - d.pop('key')
  - 合并两个字典：c = dict(a.items() + b.items())
  - 设置默认值，如果该键值之前就有，那么不会覆盖
    - d.setdefault('Age', 0)
- 集合 set {}
  - 集合中的元素不重复，复杂度？
  - add, remove
  - 交集 s1 & s2，即取两个集合共同的部分，既在 s1，又在 s2 中的元素
  - 并集 s1 | s2，即合并两个集合，在 s1 或者在 s2 中的元素
  - 差集 s1 - s2，在 s1 中且不在 s2 中的元素
  - 对称差集 s1 ^ s2，只在 s1 或者 只在 s2 中的元素
- 哈希 Hash
  - Hash Set 哈希集合，实现 set
  - Hash Table/Map 哈希表，实现 dict
- 枚举 enum
  - 语法：
    - from enum import Enum
    - 定义枚举：Month = Enum(‘Month’, (‘Jan’, ‘Feb’, ‘Mar'))
    - 访问元素：Month.Jan, Month[“Jan”]
    - 访问 name 和 value 值（本质还是整数）：Month.Jan.value, Month.Jan.name
  - 如果要精确控制枚举类型，可以派生出自定义类：

```python
from enum import Enum, unique

@unique        # unique 装饰器保证了枚举值的唯一性
def Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
```

## 2. 官方库

### 2.1 内置函数

- `sum(iterable, start=0, /)`
  - 加和操作
- `all(iterable, /)`
  - 参数是一个可迭代对象，只有全部元素都是 True 的时候才返回 True，否则返回 False
- `any(iterable, /)`
  - 同 `all`，但是只要有一个为 True 就会返回 True
- `iter(iterable) -> iterator`
  - 把一个可迭代对象转化成一个迭代器
- `dir([object])`
  - 传入一个 class/module，返回这个 class/module 的所有属性（attribute）

### 2.2 future 模块

- 可以让你在 Python2.x 中用上 Python3.x 的特性

```python
from __future__ import absolute_import

// 这里 `/` 表示小数除法，`//` 表示整除
from __future__ import division

// 只能用 `print()` 函数，不能用 `print 'hello'`
from __future__ import print_function
```

### 2.3 collections

collections 是 Python 内建的一个集合模块，提供了许多有用的集合类

- namedtuple
  - 可以很方便地创建类和属性
  - from collections import namedtuple
  - Point = namedtuple('Point', ['x', 'y'])
  - p = Point(1, 2)
  - print p.x, p.y
  - return Point(x=3, y=4)
- deque
  - 双向列表，高效实现插入和删除操作
  - q.appendleft()
  - q.popleft()
- defaultdict
  - 字典，但是不会抛出 KeyError 的异常
  - dd = defaultdict(lambda: 'N/A')
  - dd['key'] # 'N/A'
- OrderedDict
  - 字典，但是会保持 Key 的插入顺序排序
- Counter
  - 简单的计数器，比如用来统计词频
  - 合并多个 Counter 可以用 sum([Counter(['alice', 'bob']), Counter(['alice', 'cindy'])], Counter())

### 2.4 时间日期

时间模块 datetime 和 timedelta

- datetime.strftime
  - 把 datetime 对象格式化成字符串，"f" 表示 "format"
  - 参考 [docs.python.org/datetime](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)
- datetime.strptime
  - 把字符串格式化成 datetime 对象；"p" 表示 "parse"
  * `datetime.strptime("2020-01-02", "%Y-%m-%d")`

```python
from datetime import datetime

now = datetime.now()

# strftime, datetime -> str
now.strftime('%Y-%m-%d %H:%M:%S') # 输出 '2024-02-06 17:00:43'

# strptime, str -> datetime
dt = datetime.strptime("2020-01-02", "%Y-%m-%d")
print(dt)
```

### 2.5 随机数

```python
import random

# 在 [1, 10] 之间随机选一个，闭区间。
random.randint(1, 10)

# 随机选 1 个元素
random.choice(["Alice", 12, ("Hello", "World"), -0.1])

# 随机选 k 个元素
random.choices(['Hello', 'World'], weights=[0.1, 0.9], k=3)
```

### 2.6 JSON 模块

```python
import json

# 序列化成字符串
d = {'name': 'Bruce', 'age': 14}
json.dumps(d)

# 反序列化
s = '[1, 2]'
json.loads(s)

```

注意 json.dumps 在处理中文时会有一个坑。

```python
# 默认会输出 '{"Name": "\\u4e2d\\u56fd"}'
json.dumps({'name': '中国'})

# 需要加个参数，输出为：'{"Name": "中国"}'
json.dumps({"name" : "中国'}, ensure_ascii=False)
```

### 2.7 序列化

主要是 pickle 这个库。

```python
import cPickle               # python2，纯 C 实现，效率高
import _pickle as cPickle    # python3
import pickle as cPickle     # python3 推荐用法，纯 python 实现

# 1. 序列化/反序列化成字符串
data_string = cPickle.dumps(["Bruce", 2, 0.891])
data_list = cPickle.loads(data_string)

# 2. 序列化/反序列化成文件
with open('data.pickle', 'wb') as f:
     cPickle.dump(["Bruce", 2, 0.891], f)
data_list = cPickle.load(open('data.pickle', 'rb'))
```

### 2.8 日志

| level | 备注 |
| --- | --- |
| DEBUG | 详细信息，调试时才会关心的（默认不打印）|
| INFO | 用于证明事情按照预期工作（默认不打印）|
| WARNING | 有些不希望发生的发生了，比如硬盘快满了（默认打印）|
| ERROR | 严重错误（默认打印）|
| CRITICAL | 致命错误，程序应该立即终止（默认打印）|

## 3. 语法知识

### 3.1 with 语句

with 是一种控制流语句，定义进入该 block 做什么，出该 block 做什么。常用于文件打开读取，数据库打开连接。其实可以用 try except finally 代替。

上下文管理器（Context Manager），需要实现 `__exter__` 和 `__exit__` 两个函数，就可以用 with 语句了。

```python
import sqlite3

class DataConn:
    def __init__(self,db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self,exc_type,exc_val,exc_tb):
        self.conn.close()
        if exc_val:
            raise

if __name__ == "__main__":
    db_name = "test/test.db"
    with DataConn(db_name) as conn:
        cursor = conn.cursor()
```

### 3.2 Package（包）

包（Package）的意思是说，我们写好了一些工具函数和工具类，想封装起来给别的函数用，比如库函数之类的，就需要用到包。

package（包） & module（模块） 的区别？

1. package 上面解释过了，必须要有 `__init__.py`
2. modules 在 python 里指的 .py 结尾的 python 文件
3. package 可以包含 package 和 module，其实就是文件夹的意思

```python
# 这个就是从包的路径下找到模块，然后引用模块里的变量和函数。
from package.module import *
```

需要在包的路径下面添加 `__init__.py` 文件，这个路径才能成为一个包，才能被引用。

```python
# packageA 下的 __init__.py 文件这样写：
__all__ = [
    "a.py",
    "b.py",
]

# 在别的地方用 * 引用包，只能引用到 __all__ 里的模块。
from packageA import *
```

同样，在普通 `.py` 文件里的 `__all__` 变量，也是 `import *` 会参考此变量，否则会把所有不以 `_` 开头的成员都 `import` 进去

### 3.3 可迭代对象和迭代器

*可迭代对象*

凡是可作用于 for 循环的对象都是 `Iterable` 类型（可迭代对象），如 `list、dict、str、tuple`，可以重载类的 `__iter__(self): return self` 函数来得到可迭代对象

---

*迭代器*

凡是可以作用于 next 函数的对象的都是 `Iterator` 类型，是惰性计算序列。如 generator（生成器），所以说生成器是迭代器的一种，这种惰性计算的迭代器可以大大减少内存消耗

一般函数中包含 yield 关键字，函数就成了一个生成器，可以用 next 函数调用，或者直接迭代。最后会 raise StopIteration，比如重写 `__next__` 函数的时候就用得着

注意实现 `__next__` 函数的时候，需要用 return 关键字而不是 yield。可以用 b = iter(a) 把可迭代对象 a 变成迭代器 b。python 3.3 以后增加了 send 和 yield from 等特性


### 3.4 装饰器
下面构造了一个可以检测函数运行时间的装饰器
```python
def timing_val(func):
    def wrapper(*arg, **kw):
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        return (t2 - t1), res, func.__name__
    return wrapper
```

几种常用的装饰器
- `@property` 可以把类的方法变成属性值，会自动生成 getter, setter 函数;
- `@classmethod` 类方法，和类本身绑定。
- `@staticmethod` 静态方法，和类不绑定，只属于类的作用域。

### 3.5 闭包（closure）
闭包（closure）就是某个函数返回了一个子函数，但是返回的子函数里，却用到了不属于自己作用于的变量，那么这个子函数和变量加起来就是闭包。

```python
function A(y) { return lambda x: x + y }
```
和函数指针不同的是，闭包里的函数可以访问闭包里的变量，虽然此时的环境（调用该函数的作用域）按理说已经和闭包里变量声明的作用不同了。

### 3.6 反射（reflection mechanisms）
个人理解就是用字符串去找特定的函数，得到函数名以后就可以用了，但是为什么要用反射就不是很理解了，这个貌似很复杂。

```python
# getattr
foo_func = getattr(classA, 'foo')

# hasattr
hasattr(classA, 'foo')

# setattr，相当于 classA.foo = foo_func
setattr(classA, 'foo', foo_func)

# delattr
delattr(classA, 'foo')
```

import common 和 __import__('commom') 的功能是一样的，但是后者是反射机制实现的

### 3.7 类的特殊成员函数
类特殊成员
- `__init__()`：在 init 中执行所有的初始化工作；
- `__new__()`：和 init 函数类似，但是调用会比 init 更前，且可以不 return 当前的类。
- `__repr__()` 类似 __str__()
- `__del__()`：析构函数；引用计数的方式回收内存。调用 `del obj`；时会调用该函数；
- `__dir__()`：调动 dir(obj) 时，会调用该函数，返回所有属性名和方法名；
- `__dict__()`：类的内部词典；
- `__slots__`: 用于限制类的实例的属性
