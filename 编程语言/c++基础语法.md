# C++基础语法

## 字符串（C语言风格）

```c++
void *memcpy(void *dest, const void *src, size_t n);

// 把 src 指向的字符串赋值到 dest 中;
// 如果 dest 不够大，可能会造成缓冲区溢出；
char strcpy(char *dest, const char *src)
    
// 把 src 指向的字符串赋值到 dest 中，最多赋值 n 个字符；
// 注意，如果 src 长度小于 n，dest 的剩余部分将会用空字符填充；也就是说 strncpy 总会拷贝 n 个字符；
// 包含在头文件 <string.h> 中
char *strn cpy(char *dest, const char *src, size_t n);

// 比较字符串的字典序，num 是比较的最长字符数
int strncmp ( const char * str1, const char * str2, size_t num );

// 把 source 的前 num 个字符追加到 destination 中去
char * strncat ( char * destination, const char * source, size_t num );

// 考察 任意一个 str2 的字符在 str1 中出现的第一个位置，如果 str1 与 str2 交集为空，正好返回的是 str1 的长度；
// 如 str1 = “abc12”，str2 = “123”，返回 3
size_t strcspn ( const char * str1, const char * str2 );

# 格式化字符串到文件中
int fprintf(FILE *stream, const char *format, ...)

// 包含在 `<stdio.h>` 头文件中
// 格式化字符串，类似 python 中的 format 或者 print “a = %d” % (12) 这种方法；
// s 格式化后的字符串放置的指针，n 最大的长度，超过这个会截断；
// 注意 s 的大小起码是 n，这个是调用者需要确认的。可能有【缓冲区】溢出的风险。X
// 如果格式化后的字符串大于 n，会直接截断
// 注意这个函数起码有四个参数，不要写错了，否则可能会出core；
int snprintf ( char * s, size_t n, const char * format, ... );

// 如 sscanf(“Bruce 12”, “%s %d”, name, &age);  这里这里 age 是 int，用 scanf 是要传入指针
// 和 scanf 类似，只不过是从 str 中读取而不是输入流
// 有个特殊的用法，比如 sscanf(“bruce jsodu :1132”, “%[^:]%d”, name, &age)，这里的 %[^:] 表示遇到 : 就停止；
// 同理 %[a-z] 表示只读取 a-z，遇到非 a-z 就立刻停止。
int sscanf ( const char * s, const char * format, ...);
```

## C/C++ 语言关键字

C/C++ 语言关键字
- `volatile`
    * 告诉编译器这个变量是易变的，每次都要从内存中读取，而不是从 CPU 的寄存器中读取。
    * 有点复杂，参考 https://liam.page/2018/01/18/volatile-in-C-and-Cpp/
- `extern`，两个作用
    * `extern “C” void fun(int a, int b);` 告诉编译器用 C 的规则去命名函数，而不是像 C++ 那样重命名（这样可以支持函数重载）。
    * `extern int g_var;`  多次声明一个变量
- `inline`
    * 内联函数，向编译器提出申请，是否可以进行宏替换，可能会被拒绝。
    * 内联函数只有在特别简单的时候才有意义。
- `restrict`
    * 保证一个指针独享一片内存，即不会有其他指针指向这篇内存
- `register`
- `union`
    * 联合体，和结构体有点像，但是联合体的所有成员变量会共享存储空间。
- `struct`
- `typedef`
- `mutable`
    * 在C++中，mutable也是为了突破const的限制而设置的。
    * 被mutable修饰的变量，将永远处于可变的状态，即使在一个const函数中。
    * 一个常见的应用场景的是用在互斥量上。
- `override`，C++11特性
    * 如 `void foo() override;`
    * 表示该成员函数是虚函数，且继承自基类中的虚函数
- `final`，C++11特性
    * 如 `void foo() final;`
    * 表示该成员函数/虚类是最后一个虚函数或者虚类，不能再被继承；
- `decltype`，C++11特性
    * 用来得到变量的类型
    * `int i = 33;`
    * `decltype(i) j = i * 2;`

```c++
// 声明一个联合体
union RecordType    // Declare a simple union type
{
    char   ch;
    int    i;
    long   l;
    float  f;
    double d;
    int *int_ptr;
};

RecordType t;
t.i = 5;           // t holds an int
t.f = 7.25;        // t now holds a float
```

编译器选项
- `#progma once`
- progma 是编译器选项，once 意思是让头文件只被载入一次
- 即替代 #ifndef XXX #include XXX #endif
- https://en.wikipedia.org/wiki/Pragma_once

声明与定义
1. 定义
    - 一个变量，比如 int a; 或者 int a = 10; 这里编译器会创建一个变量，分配内存，命名；
    - 不要在头文件里定义变量，因为头文件可能会被多次包含
    - 同一个变量只能定义一次，不允许重复定义；
2. 声明
    - 告诉编译器变量的类型，但是不分配内存；
    - 声明的变量已经在外部定义了，如果没有定义，链接的时候应该会出错。
    - 可以多次声明一个变量；

## 数据结构

指针
- 指针常量和常量指针
    - 常量指针
        * 是一个指针，只能够读取内存中的数据，不能修改数据的属性。
        * `const int *p;` 这里声明了一个常量指针
    - 指针常量
        * 是一个常量，只不过这个常量的类型是“指针”类型（常量可以是 int，float， 指针）
        * 这个指针只能指向一个地方，不允许指向别的地方
        * `int * const p = &a;`
- 函数指针和指针函数
    - 函数指针：函数指针是指向函数的指针变量
        * 例如下面的声明：`typedef int (*fun_ptr)(int,int);` 声明一个指向同样参数、返回值的函数指针类型
        * 可以这样用：`int (* p)(int, int) = & max;` &可以省略
    - 指针函数

数组
- `size_t` 来表示数组的下标类型，这个关键字是在 `cstddef` 头文件里定义的

函数
- 函数重载（overload），指的是定义的函数名一样，但是参数不一样。

枚举
- C++中的枚举实质上就是整形，会造成类型不安全的隐患；而且存在命名空间冲突的问题。为此，C++11引入了强类型枚举

```c++
// 标准C++枚举
enum Side {
    LEFT,
    RIGHT,
};

enum Thing {
    WRONG,
    RIGHT, // RIGHT和Side中的RIGHT冲突
};

// C++11 强类型枚举
enum class Side {
    LEFT,
    RIGHT,
};

enum class Thing {
    WRONG,
    RIGHT, // RIGHT和Side中的RIGHT不会冲突
};
```

pair
- 这个类型属于标准库类型，定义在头文件 `<utility>` 中
- 用 `make_pair` 生成一个新的 pair

NODEBUG 预处理变量
```c++
//文件开头可以这样写，如果不想要可以注释掉
#def NDEBUG

#ifndef NDEBUG
    cerr << __func__ << ": wrong” << endl;    // __func__ 是编译器定义的一个与不静态变量，用来存放函数名
#endif
```

计算函数运行时间
```c++
#include <ctime>

clock_t begin_time = clock();

// do something

clock_t end_time = clock();
double elapsed_secs = double(end_time - begin_time) / CLOCKS_PER_SEC;
```

## 内存管理

内存管理
- 内存存储（局部变量声明以后要手动初始化，全局变量系统会给初始化）
    - 栈（stack）
        * 存储函数的局部变量，函数结束后释放，由操作系统管理；
        * 栈一般比较小，比如 4M，你声明一个 500w 大小的 int 数据就会爆栈。
        * 栈是从高地址到低地址增长的，因此先定义的局部变量的地址一般大于后定义的局部变量地址。
    - 堆（heap）
        * new/delete 出来的变量，编译器不去释放，由程序来做。
        * 这部分的变量存放在内存中，大小跟你内存条大小有关。
    - 自由存储区
        * malloc/free 分配的内存块
    - 全局/静态存储区
    - 全局变量和静态变量
    - 常量存储区
        * 常量，不允许修改
- C++ primitives
    1. `malloc / free` 属于 C 函数
    2. `new/delete`  C++表达式（expressions）
        * new 会做三件事，① 调用 `::operator new()` 函数，分配内存 ② 类型转换 ③ 调用构造函数
        * 同理，delete 也会做三件事，① 调用析构函数 ② 调用 `::operator delete()` 函数释放内存
    3. `::operator new() / ::operator delete()`，while 循环调用 malloc/free 函数；
        * 这个是 C++ 函数，全局函数，可以被重载
    4. `placement new`：只是 operator new 重载的一个版本。
        * 它并不分配内存，只是返回指向已经分配好的某段内存的一个指针。
        * 因此不能删除它，但需要调用对象的析构函数。
        * 太高级，一般不是为了效率，不要用。
    5. `allocator<T>::allocate() / allocator<T>::deallocate()`，C++ 标准库
    6. `new/delete` 是运算符号，由编译器解析，可以执行析构函数；
    7. `malloc/free` 是库函数，功能有限，基本只分配内存。

## 智能指针

智能指针
- 智能指针有三种，定义在头文件 <memory> 中，注意这三种都是模板类；
    - shared_ptr 共享指向对象的指针
        * 用引用计数来管理内存的创建和释放，多个 shared_ptr 可以指向同一个地址，最后一个析构时，才会真正回收内存。
        * 用法：shared_ptr<Base> p = make_shared<Base>(“parameter1”, “parameter2")
    - unique_ptr 独占指向对象的指针
        * 某个时刻只能有一个 unique_str 指向一个给定对象
        * 当 unique_ptr 被销毁时，其指向的对象也会被销毁
        * 只能移动（std::move），不支持拷贝和赋值，但是可以用 reset 和 release 来转移所有权
        * 用法：unique_ptr<Base> p = make_unique<Base>(“parameter1”, “parameter2")
    - weak_ptr 弱引用的指针，一般不单独使用，会指向 shared_ptr 所管理的对象
        * weak_ptr 可以绑定一个 shared_ptr，指向一个 shared_ptr 管理的对象，但是不影响 shared_ptr 的引用计数
        * 也就是说，如果引用计数为零，即使有 weak_ptr 指向该对象，内存还是会被释放。
        * 调用 lock 函数，返回空说明对象已经被销毁，返回一个 share_ptr 对象时说明对象还在。
        * 设计 weak_ptr 的目的是为了解决循环引用造成的内存泄漏问题。类似死锁。
    - auto_ptr 是 C++98 的类，禁用
        * C++98 有个 auto_ptr 的类，具有 unique_ptr 的部分特性，但是没法在容器中保存，也不能作为函数的返回值
        * 公司 C++ 标准禁用该类。
        * 智能指针支持 *p, p->func(), p.func() 操作，也能支持 swap(p, q), p.swap(q) 操作
- 使用 make_shared 函数来动态分配一个对象并初始化，这个函数只能返回 shared_ptr 类型的智能指针
    - shared_ptr<int> p = make_shared<int>(42);  // 定义一个值为 42 的 int 类型指针
- 引用计数（reference count）
    - 每个 shared_ptr 都有一个关联的计数器，当计数器变成 0 时，会自己释放管理的对象
    - 当传递参数，或者作为函数返回值，初始化另一个 shared_ptr 时，引用计数都会递增
    - 当 shared_ptr 被赋予一个新值，或者被销毁，或者局部的 shared_ptr 离开其作用域，计数器就会递减

allocator 类
- 使用 alloctor 类来做内存分配和初始化工作，这两步可以分开。
- 这是一个模板类，定义一个 allocator 对象，allocator<T> a 后，可以调用下面几个常用的函数
- `a.allocate(n)`      // 分配一段原始的、未构造的内存，保存为 n 个类型为 T 的对象
- `a.deallocate(p, n)`  // 释放指针 p 开始指向的内存，p 必须是之前 allocate 返回的指针
- `a.construct(p, args)`  // 用来构造对象
- `a.destroy(p)`         // 用来执行析构函数

当我们编写比较大型的程序时，异常、命名空间和面向对象（主要是多重继承和虚继承）比较有用。

异常处理
- throw 有点像 return 语句，后面跟的语句可能不会被执行。
- try 和 catch 总是成对出现，如果 throw 在栈展开的过程中一直没有找到对应的 catch 语句，程序可能会被终止。
- 空的 throw 语句只能出现在 catch 语句中（或者 catch 调用的函数里）
- 使用 try {} catch (…) {} 来接住所有的异常。
- （C++ 11特性）关键字 noexcept 可以用来标识函数不会抛出异常，虽然这个标识可能会被编译器忽略（即理论上是可以继续抛出异常的）
- （C++ 11特性）关键字 noexcept 也可以用来做一元运算符，求一个函数或者表达式是否会抛出异常，返回一个布尔值 true 或者 false
- 【编程规范】
    * 【建议】建议不要使用异常，除非已有项目/底层库使用了异常， 这时候必须要catch所有异常。
    * std::nothrow
    * 在用 new 申请堆内存时，如果内存耗尽，默认会抛出 std::bad_alloc 异常；
    * 如果不想抛出异常，可以用 `MyClass* class = new (std::nothrow) MyClass();` 来创建，然后检测 class 是否为空指针即可。

IO 操纵符（manipulator）
- 控制布尔类型的输出格式
  - `cout << boolalpha << true << endl << noboolalpha;  // 只会输出 “true"`
    - 其中 boolalpha 何 noboolalpha 就是操纵符
- 控制整型的进制位
    - `cout << oct << 20 << endl << “ “ << dec << 20 << endl;  // 会输出 “24 20"`
    - `cout << showbase << hex << 20 << endl << noshowbase;  // 会输出进制的前缀，”0x14"`
- 控制浮点数精度
    - `cout << setprecision(3) << sqrt(2.0) << endl; // 保留 3 位小数`
    - `cout.precision(3); cout << sqrt(2.0) << endl;`
- 科学记数法
    - `cout << scientific << 200 * sqrt(2.0) << endl;`
- 小数点
    - `cout << showpoint << 20.0 << noshowpoint << endl;`
- 补空白
    - `cout << left << “i =“ << setw(12) << 23 << endl;  // 左对齐`
    - `cout << right << “i=“ << setw(12) << -3.2 << endl; // 右对齐`
- 注意 setw 只影响下一个要输出的数字
- 控制输入格式
    - `cin  >> noskipws;  // 不忽略空白符`
    - `cin >> skipwd; // 忽略空白符`


rhs 指的是 right hand side，即右边的表达式；同理 lhs 是左边的表达式。

左值引用和右值引用和 std::move 和移动构造函数
- 比如有个表达式 int a = b + 1; 那么 a 就是左值，b + 1 就是右值；
- 右值表达式无法赋值给左值引用，如 int &a = b + 1; 因为左值引用相当于是取右值的地址，这里右值表达式相当于是一个临时变量，所以不合法。

std::ref 和 std::bind
- 什么是左值引用和右值引用？
- 参考：从四行代码看右值引用
- 左值引用，就是一般的引用，如 int & i = getVar(); 这里引用符号是在左边。i 就是左值，这边变量可以引用，getVar() 返回的临时变量就是右值，且是纯右值（prvalue）。
- 右值引用，为了解决临时对象的昂贵拷贝操作。如 T && i = getVar(); 这里两个 & 就是右值引用。这样 getVar() 返回的临时变量重获新生。

sleep
- 参考 `man 3 sleep; man 3 usleep`
- 需要 `#include <unistd.h>` 头文件
- `unsigned int sleep(unsigned int seconds);`  休眠 X 秒
- `int usleep(useconds_t usec);`   微秒，micro-seconds，10^-3 毫秒，10^-6秒

```
#include <unistd.h>

// 休眠 X 秒
unsigned int sleep(unsigned int seconds);

// 微秒，micro-seconds，10^-3 毫秒，10^-6秒
int usleep(useconds_t usec);

#include <chrono>
#include <thread>

// C++11 的写法
std::this_thread::sleep_for(std::chrono::milliseconds(100));
```

TODO：空的类，new 的时候；