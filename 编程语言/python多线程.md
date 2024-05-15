[TOC]

# python 多线程

## 1. GIL 全局解释器锁
由于 GIL（Global Interpreter Lock，全局解释器锁）的存在，多线程同时只能有一个 python 线程在运行。而多进程下，每个进程都可以有自己的解释器，所以是真正的并行。

GIL 是 `CPython` 早年设计的局限性，因为内存管理（memory management）是不是线程安全的（thread safety），所谓引入了全局锁。

`CPython` 和 `PyPy` 都有 GIL，但是 `JPython` 和 `IronPython` 是没有的。

## 2. 多线程
参考博客：https://www.liujiangblog.com/course/python/79

python 多线程主要用的是 `threading.Thread` 类，定义如下：
```python
def threading.Thread(self, 
    group=None,         # group 是预留的参数
    target=None,        # target 是可调用的函数
    name=None,          # name 是线程名，字符串
    args=(),            # args 是函数参数
    kwargs=None, *, 
    daemon=None)        # daemon 是否是守护线程
```

重要的成员函数
```python
def start()
def run()               # 线程被 CPU 调度后，会自动执行该方法
def join([timeout])
def is_alive()
def getName()
def setName()
self.name
self.ident              # 线程的标识符，非零整数

# 默认是前台线程，daemon=False，主线程执行完毕后，等待前台线程执行完成后，程序才停止。
# 如果是后台线程，daemon=True，主线程执行完毕后，后台线程不论成功与否，均停止。
def setDaemon()
self.daemon
```

## 3. python 的线程锁机制

有下面几种线程锁机制
1. Lock 互斥锁
2. RLock 可重入锁
3. Semaphore 信号量
4. Event 事件
5. Condition Variable 条件变量
6. Barrier 阻碍

### 3.1 互斥量 Lock
```python
import threading

lock = threading.Lock()
lock.acquire()

#... 临界区，只允许单个线程访问

lock.release()
```

可重入锁 `threading.RLock` 和 `threading.Lock` 用法一样，只是可以多次调用 `acquire/release`。

也可以用 `with` 语法：
```python
lock = threading.Lock()
with lock:
    # data racing area
```

### 3.2 信号量 BoundedSemaphore
这个我不确定是不是信号量，感觉有些奇怪

主要涉及 `threading.BoundedSemaphore` 类，这种锁只允许固定的线程同时访问，限定比互斥锁松一些。
```
semaphore = threading.BoundedSemaphore(5)
semaphore.acquire()

# ... 这里最多允许 5 个线程访问，其余的只能排队

semaphore.release()
```

### 3.3 事件 Event
事件线程锁的机制是，定义一个全局的 Flag，为 True 时会阻塞 wait() 函数，当为 False 是线程不会阻塞。

主要涉及 `threading.Event` 类，包含四个函数

```python
def clear(), 令 Flag = False
2. set(), 令 Flag = True

# 当 Flag=True 或者 timeout 发生时立马返回，否则阻塞
def wait(timeout=None)

4. is_set()，判断 Flag 是否为 True
```

### 3.4 条件锁 Condition

主要涉及 `threading.Condition` 类，包含三个函数
```python
def acquire()           # 获取锁
def release()           # 释放锁
def wait([timeout])     # 释放锁，进入锁定池等待
def notify()            # 随机挑一个通知，进入锁定池
def notifyAll()         # 通知所有的
```

### 3.5 定时器 Timer
定时器 `Timer` 是一个小工具，用于指定 `n` 秒以后执行某函数，简单实用。
```python
import threading

def hello():
    print("hello world!")

t = Timer(1, hello)
t.start()
```

## 4. 线程池
ThreadPoolExecutor

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor() as executor:
    # Method 1,
    results = executor.map(func, [1, 2, 3])

    # Method 2,
    future = executor.submit(func, 1)
    result = future.result()
```

## 5. 多进程

## 6. 其他
通过 with 语句使用线程锁，示例如下：
```python
some_lock.acquire()
try:
    # do-something
finally:
    some_lock.release()
```

这样做的好处是，无论中间执行什么，都能保证线程锁会被释放，以防对其他线程造成影响。
