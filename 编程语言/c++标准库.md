# C++ 标准库

## 1. 结构体

`struct` 和 `class` 在 `c++` 中的唯一区别就是默认成员变量（函数）是 `public`，而 `class` 是 `private`.

【编程规范】因此在选择 `struct` 和 `class` 时，前者一般只拿来做数据的聚合，后者在需要定义一些 `action` 时才需要。

*   `swap` 交换两个容器
*   `assign` 容器的赋值，某个或者某些位置位置赋值

迭代器

*   `begin()`, `end()`, `cbegin()`, `cend()` # 迭代器与常量迭代器
*   `rbegin()`, `rend()`, `crbegin()`, `crend()` # 反向迭代器与常量反向迭代器

## 2. STL

### 2.1 vector 数组，线性表

```c++
# 初始化
vector<int> v(10);      // 初始化 10 个元素，默认为 0
vector<int> v{10};      // 初始化 1 个元素，值为 10
vector<int> v(10, 1);   // 初始化 10 个元素，值为 1
vector<int> v{10, 1};   // 初始化 2 个元素，值为 10，1
```

成员变量

*   iterators: `begin`, `end`
*   capacity: `size`, `resize`, `capacity`, `empty`, `reserve`
*   element: `[]`, `at`, `front`, `back`
*   modifiers: `push_back`, `pop_back`, `insert`, `erase`, `swap`, `clear`

```c++
# 删除：
iter = v.erase(iter);   // 注意这里原本的 iter 不能再用，否则迭代器会失效；

# 把 a 数组插入到 b 数组中
b.insert(b.end(), a.begin(), a.end());
```

### 2.2 stack 栈，先进后出

```c++
bool empty() const;
size_type size() const;
const value_type& top() const;
void push (const value_type& val);
void pop();
void swap (stack& x);   // 交换两个栈
```

### 2.3 queue 队列，先进先出

```c++
bool empty() const;
size_type size() const;
const value_type & front() const; // 队列头
const value_type & back() const; // 指向最后一次 push 的元素
void push(const value_type & val); // 在队列尾增加新元素
void pop(); // 删掉 front 指向的元素
deque<int> dq; // 双向队列，有点像 list
```

其他函数

*   `operator []` 下标访问
*   `front`, `back` 栈头、尾
*   `pop_back`, `pop_front`, `push_back`, `push_front`
*   `shrink_to_fit`

### 2.4 list 双向链表

在任何位置的插入和删除操作效率都很高，不支持随机访问

*   `void assign(size_type n, const value_type& val);`
*   `void assign(InputIterator first, InputIterator last);`
*   `push_front, pop_front, push_back, push_front`
*   `insert, erase` // 插入和删除
*   `forward_list<int> fl;` // 单项链表，
*   `insert_after`
*   `emplace_after`
*   `erase_after`

### 2.5 priority\_queue 优先队列，即最大堆

属于关联容器

*   头文件 `#include <queue>`
*   最大堆`priority_queue<int> q(arr, arr+4);`
*   最小堆 `priority_queue<int, vector<int>, greater<int> > q(arr, arr + 4);`
*   入堆 `void push (const value_type& val);`
*   堆顶元素 `const value_type& top() const;`
*   删除堆顶元素 `void pop();`

### 2.6 set, multiset

红黑树（RB-tree, Red-Black Tree）实现的集合，元素不重复；元素之间已经排序。属于关联容器的一种

构造器

```c++
set<int> s1;
set<int> s2(arr, arr+5); // arr 是 int 数组
set<int> s3(s2);
set<int> s4(s3.begin() s4.end());
```

迭代器

```c++
s.begin() // 正常的迭代器，可以访问和修改；按照 key 的排序顺序遍历。（对红黑树进行中序遍历）
s.rbegin() // 逆向迭代器，指向最后一个元素
s.cbegin() // 常量迭代器，不可以修改指向的变量 
```

modifiers

插入 insert & emplace

```c++
pair<iterator,bool> insert (const value_type& val); // 返回该元素的迭代器 ，返回是否插入元素
iterator insert (iterator position, const value_type& val); // 在某迭代器后面插入元素
void insert (InputIterator first, InputIterator last); // 比如 insert(arr, arr+5);
pair<iterator, bool> emplace(Args&& ... args); // 直接在 set 中构造新元素，而非拷贝插入
```

删除 erase

```c++
void erase (iterator position); // 迭代器
size_type erase (const value_type& val); // 返回的是 0 或者 1，表示删除的元素的个数
void erase (iterator first, iterator last);
```

查找 find & count

```c++
iterator find (const value_type& val) const; // 查找元素，O(logN) 复杂度
s.find(30) != s.end() // 判断找到了没有
s.count(30) // 存在返回 1，不存在返回 0
```

map\<string, int> m; multimap\<string, int> mm;

*   红黑树实现的字典，key 需要重载 `operator <` 函数，用法参考上面的 set
*   只能按照 key 排序，不能按照 value 排序。
*   属于关联容器的一种，相当于 Python 中的字典（dict）
*   都在头文件 &lt;map&gt; 中

用法示例：

```c++
map<string, int> m;     // 声明
m["age"] = 14;          // 赋值
m.insert(make_pair("age", 14));     // 插入操作
m.size()    // 取大小
m.find("age") != m.end()    // 查找操作
cout << m.find("age").second() << endl;
m.count("age");         // 只会返回 0 或者 1
```

### 2.7 unordered\_map，unordered\_multimap

哈希表实现的 map 和 multimap，key 需要重载 hash\_value()

`#include <unordered_map>`
`typedef unordered_map<string, int> mymap;`

*   用法和上面的 map 一致，只是实现起来不一样。虽然哈希函数的复杂度是 O(1)，但是 re-hash 也带来了不稳定性；
*   而且哈希函数速度也不一定那么快的，因此要综合考虑。
*   map 基于红黑树实现，最坏和平均的复杂度都是 O(logN)，比较稳定。

### 2.8 unordered\_set, unordered\_multiset

用哈希函数实现的 set 和 multiset
algorithm

*   `reverse(v.begin(), v.end());`
*   `sort(v.begin(), v.end(), cmp);`

STL 模板类的排序

*   像 vector，set，map 都是支持排序的，有两种方法
*   在 sort 函数的第三个参数中传入一个 compare 函数
*   在构造对象的时候传入一个 struct compare 参数
*   像 map 只支持 key 的排序，如果要根据 value 排序，需要把 pair 元素放到 vector 或者 set 中再去排序。

situation 1, 给 sort 函数传入一个 compare 函数

```c++
bool compare(pair<string, int> pair1, pair<string, int> pair2) {
    return pair1.second > pair2.second;
}

vector<string, int> vec;
// ... insert element to vec

sort(vec.begin(), vec.end(), compare); // 传入这个 compare 函数来自定义排序规则
```

situation 2

```c++
struct heap_compare {
    bool operator()(Node *node1, Node *node2) {
        return node1->freq > node2->freq;
    }
}
priority_queue<Node *, vector<Node *>, heap_compare> min_heap; // 定一个最小堆
```

### 3 字符串 string

其实是 `class std::basic_string<char>` 的一个 `typedef`.

初始化

```c++
string s1; // 空串
string s2(s1);  // 将 s2 初始化为 s1 的一个副本，此时 s1 == s2 为 true，但是如果 s1 或者 s2 改变了，那么 s1 == s2 为 false
string s3("abcdef");
string s4(4, 'c');  // 初始化成 4 个 c，即 "cccc"
```

读取字符串

```c++
cin >> s1;  // 读取，遇到空格停止
getline(cin, s2);  // 读取一行，遇到 '\n' 停止
getline(cin, s3, '\t') // 自定义停止符，遇到 '\t' 停止
```

对象访问

```c++
s.empty(); // 判断是否为空，布尔型
s.size(); s.length();  // 返回字符的个数，两个函数完全相同，返回的类型是 string::size_type/size_t 而非 int 
s.capacity();  // 容器的当前容量
s.substr(3, 2);  // 从下标为 3 的地方，连续 2 个字符组成的字串
s.find("good") // 查找函数，如果找到则返回第一个字符的下标，否则返回 string::npos 这个数字
const char *ch = s.c_str(); // 转换成 char
```

搜索操作

```c++
s.find              // 第一次出现的位置
s.rfind             // 最后一次出现的位置
s.find_first_of     // 任何一个字符第一次出现的位置
s.find_last_of      // 任何一个字符最后一次出现的位置
s.find_first_not_of     // 第一个不在候选里的字符
s.find_last_not_of      // 最后一个不在候选里的字符
```

对象操作

```c++
s.push_back('c')    // 在后面插入字符
s.append("hello")   // 在后面插入字符串
s.resize(14, 'a');  // 重新设置大小，自定填充字符为 'a'，如果原来的长度小于 14 则截断。
s.insert(1, "abc")  // 在下标为 1 的位置插入
s.replace(1, 3, "very good");   // 在下标为 1 的地方，把后面三个字符替换掉
s.erase(5, 2);      // 删掉下标从 5 开始的 2 个字符

// string 和数值类型的转换。
to_string() // 可以把 int, long, long long, unsigned, unsigned long, unsigned long long, float, double, long double 等转换成字符串
stoi(), stol(), stoll() // 可以把字符串转换成 int, long, long long 类型
long long stoll (const string& str, size_t* idx = 0, int base = 10);
long long stoll (const wstring& str, size_t* idx = 0, int base = 10);
stof(), stod(), stold() // 可以把字符串转换成 float, double, long double 类型
stoul(), stoull() // 可以把字符串转换成无符号的 unsigned long, unsigned long long 类型

// C 函数中可以用如 atol 之类的函数来转换，注意和上面的函数区分开。
long int atol ( const char * str );
long int strtol (const char* str, char** endptr, int base);
int atoi (const char * str);
double atof (const char* str);
```

## 3. 基本输入输出流

### 3.1 基本的输入输出流

对应头文件 `<iostream>` 定义了四个对象，分别对应

1.  标准输入 `cin`;
2.  标准输出流 `cout`;
3.  非缓冲-标准错误流 `cerr`;
4.  缓冲-标准错误流 `clog`.

释义：

*   非缓冲的意思是会立马输出，缓冲的意思是会先把流存储在缓冲区，直到填满或者缓冲区刷新才输出。
*   这四个都是 iostream 类的实例，其中 cin 属于 istream 类，cout, cerr 和 clog 属于 ostream 类；
*   可以用 while(std::cin >> str) 来读取数量不定的输入数据。
*   cin 读字符的时候，会跳过空格和换行符，需要用 getchar 函数来读。
*   cout 输出时，可以用 iomanip 中的控制符来格式化输出，比如浮点数精度，小数点位数，字符宽度等。

### 3.2 文件输入输出流

对应头文件 &lt;fstream&gt;，这个标准库定义了三种数据类型，分别是

1.  文件流 std::fstream
2.  输入文件流 std::ifstream，
3.  输出文件流 ofstream

释义：

*   注意在 c++ 中进行文件处理，必须包含 &lt;iostream&gt; 和 &lt;fstream&gt; 两个头文件
*   注意和 python 的不同，如果文件流没能成功打开文件（比如因为文件不存在等），程序是不会报错的或者抛出异常的，需要自己判断一下。用 if (!fin) {} 来判断是否成功打开文件。
*   ifstream 用来读文件，ofstream 用来写文件，fstream 可以用来读和写。
    上面三种类都包含下面几个函数
    *   `void open(const char* filename, ios::openmode mode);`
    *   \`ios\:openmode 是打开文件的模式，有好几种，包括：
        *   ios::ate 文件打开后定位到文件末尾
        *   ios\:in 读取模式
        *   ios::out 写入模式
        *   ios::app 追加模式
        *   ios::trunc 截断模式，若文件已存在，把文件长度设为 0；若是 out，默认就是截断。
        *   ios::binary 二进制文件格式，对比下面的 ios::text，主要是对换行符出的不同。
            *   ios::binary 不针对换行符做修改。
            *   ios::text 会把 `\n` 替换成 windows 下的 `\r\n`
        *   ios::text 文本文件格式
    *   `void close();`
    *   `bool fail();`  // 判断文件是否被成功打开。也可以用 !fin 替代 fin.fail()
    *   `char get();` // 读取一个字符；

### 3.3 字符串输入输出流 对应头文件 &lt;sstream&gt;

定义了三个类，分别是

1.  字符串输入输出流 stringstream
2.  字符串输入流 istringstream
3.  字符串输出流 ostringstream

输入流相关的函数，如何读取流？

*   `std::istream& std::istream::get (char& c);`
    *   从输入流中读取一个字符串，赋值给 `c` 变量
*   `std::istream& std::istream::getline (char* s, streamsize n);`
    *   从输入流中读取字符，直到遇到终止符号，赋值给 `s` 变量
    *   默认终止符是换行符
*   `std::istream& std::istream::getline (char*s, streamsize n, char delim);`
    *   额外提供自定义的换行符，是上面函数的重载。
    *   注意 `getline` 会丢弃换行符，但是 `get` 不会
*   `std::getline(istream &fin, string &str, char delim);`
    *   全局函数，和上面的两个 `getline` 用法类似
    *   比较推荐全局的 `std::getline` 函数

流的随机访问

主要是 seek 和 tell 函数，且主要用在文件流中
- seek 会把流重定位到指定的位置，tell 会告诉我们流的当前位置（从文件头开始算的字节数）
    - TELLQ 和 TELLG 分别是告诉我们输入流和输出流的位置，SEEKQ 和 SEEKG 同理。
    - 我一般 tellg 和 - seekg 用的多。
- seek 有两个重载的函数
    - seekg(streampos pos);     // 这里的 pos 是流的绝对地址
    - seekg(streamoff off, ios_base::seekdir way);
        - 这里的 off 是偏移量，way 是起始位置。
        - way 可以是下面三种取值之一：ios::beg, ios::end, ios::cur

读文件示例
```c++
#include <iostream>     // for std
#include <fstream>      // for ifstream

int main(){
    std::ifstream infile;
    infile.open("query.txt.gbk", std::ios::in);
    std::string query;
    while (!infile.eof()) {
        std::getline(infile, query, '\n');
        std::cout << query.length() << std::endl;
        std::cout << query << std::endl;
    }
    return 0;
}
```

写文件示例

```c++
ofstream outfile;
outfile.open(“file.dat”, ios::out | ios::trunc); // 覆盖的方式写文件，追加可以用 ios::app
outfile >> “Bruce” >> endl;
outfile >> “Hello World!” << endl;
outfile.close();
```

字符串流的应用：翻转一组数字

```c++
vector<int> nums{123,456,789};
vector<int> reversed_nums;
for(auto n : nums) {
    ostringstream digit;
    digit << n;     // 先把数组输出到字符串流中
    string str_n = digit.str();     // 从字符串流中取出字符串
    reverse(str_n.begin(), str_n.end());

    int reversed_n;
    istringstream rev_n(str_n); // 把字符串输入到字符串流中
    rev_n >> reversed_n; // 从字符串流中取出数字
    reversed_nums.push_back(reversed_n);
}
// reversed_nums: {321, 654, 987}

// 把整个文件流 load 到内存里，然后再慢慢解析（不过貌似速度提升不大）

// step1 读取文件
fin.open(“a.txt”, ios::in);

// step2, 得到文件的大小（单位：字节，byte）
fin.seekg(0, ios::end);
streampos length = fin.tellg(); 
fin.seekg(0, ios::beg);

// step3, 一次读取整个文件，放到字节流里去，以方便读取
vector<char> buff(length);
fin.read(&buff[0], length);
stringstream stream;
stream.rdbuf()->pubsetbuf(&buff[0], length);

// step4, 字节流处理起来很方便
string line;
while(getline(stream, line)) {
    // do something with line
}
```

# 4. 泛型算法（genetic algorithm）

*   STL 提供了一组独立于容器的算法，这些算法是运行在迭代器之上，只执行迭代器的操作（遍历，赋值，删除等）
*   泛型算法不执行容器的操作，因此无法改变容器的大小。
*   这些算法是通用的，因此叫做泛型
*   这些算法大部分包括在头文件 algorithm 中
```c++
find          // 查找操作
accumulate    // 累加求和
equal         // 比较元素是否相同，返回布尔类型
fill          // 批量赋值（用来清空？）
fill_n        // 和 fill 用法类似
copy          // 批量拷贝
sort          // 排序
unique        // 消除重复元素
```

## 5. 命名空间

*   不要在头文件里使用 using namespace std; 
*   否则会被其他文件 include 进去，引发命名冲突
*   命名冲突的时候，编译器正常报错，很难 debug
*   使用 using std::cin 来替代 using namespace std; 效果一样的。

## 6. 模板（template）

*   函数模板 template&lt;typename T&gt;
    *   注意这里没有分号。
*   类模板 template&lt;class T&gt;
*   可变参数的模板
    template\<typename T, typename… Args>
*   模板的特例化
    *   定义了模板，并不意味着所有的类型都是通用的，可能我们想额外指定某些类型来自己定义
    *   用空的尖括号来指定参数，template <> int compare(const char\* const \&p1, const char\* \&p2);
    *   特例化适用于函数模板和类模板。
    *   类模板可以被部分特例化（也叫偏特化，partial specialization），但是函数模板不支持部分特例化。

## 7. C++ 11 才有的标准库类型

### 7.1 tuple 类型

tuple 类型

*   可以这样定义 `tuple<T1, T2, T3, …, Tn> t;` 其中 `Ti` 是不同的类型。
*   用 `make_tuple` 构建新的 tuple
*   下标的索引有点不方便，需要调用 `get<i>(t)` 这种方式。
*   用 `==` 和 `!=` 来比较两个 tuple

我感觉可以用 struct 来聚合数据，以此替代这个。

*   tuple，不知道这个数据结构设计的初衷是什么。
*   如果成员变量不需要名字的话，还是挺方便的。可以看作是个更强大的 pair
*   可以和 std::tie 结合一起用，std::tuple\_cat ？
*   可以尝试用 typedef 来让代码更简洁。

## 7.2 bitset 类型

该标准库类型在头文件 bitset 中。

构造函数

*   bitset&lt;n&gt; b; // n 是二进制位的个数
*   用一个整型值来初始化 bitset，这个值首先被转换成 unsigned long long，然后被当做位模式来处理，剩余高位置零，超过则丢弃。
*   用 string 类型初始化 bitset，直接表示位模式。
*   bitset 操作
    *   b.any(), b.all(), b.none(), b.count(), b.size()
    *   b.to\_ulong(), b.to\_ullong() 返回 unsigned (long) long 类型，可能会抛出 overflow\_error 的异常。
    *   b.to\_string(zero, one); 返回一个字符串
*   支持流，cin >> bits; cout << bits;

## 8. 正则表达式

定义在 regex 文件中

*   注意正则表达式的编译是很慢的，尽量避免不必要的正则表达式，不要的循环内重复编译正则表达式。
*   类 regex，表示正则表达式的一个匹配规则，可以用 string 初始化
*   函数 regex\_match，如果 regex 规则和字符串匹配，返回 true，否则返回 false
*   函数 regex\_search，如果 regex 规则和字符串的任一个子串匹配，返回 true，否则返回 false
*   函数 regex\_replace，替换匹配的字符串

# 9. 随机数

c 语言里有 rand 头文件，但是在 C++ 里建议用 default\_random\_engine 类

*   uniform\_int\_distribution&lt;unsigned&gt; u(0, 10)
*   uniform\_real\_distribution&lt;double&gt; u(0, 1)
*   normal\_real\_distribution<> n(4, 1.5); // 4 是均值，1.5 是标准差
*   bernoulli\_distribution b(0.55);

生成 0\~9 的随机数

```c++
uniform_int_distribution<unsigned> u(0, 9);
default_random_engine e(1234); // 1234 是随机数种子（seed）
for (size_t i = 0; i < 10; ++i) {
    cout << u(e) << endl;
}
```
