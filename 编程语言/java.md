# Java
参考：
- [Java Guide](https://javaguide.cn/)
- [二哥的Java进阶之路](https://javabetter.cn/)

## Java 历史
时间线
- 1995年，Sun公司正式发布了Java语言，主要用于网络编程。Sun公司在2009年被甲骨文公司（Oracle）收购。
- Java8, 2014年发布，最经典的版本
- Java11，2018年发布，长期支持的版本
- Java21，最新的版本

JAVA_HOME/bin 带的几个可执行文件
- `java`，就是 JVM，Java 虚拟机，可以执行编译后的代码。
- `javac`，Java的编译器，把Java源文件编译成字节码 .class
- `jar`，把一组 .class 文件打包成 .jar 文件，便于发布。
- `javadoc`，从Java源码中自动提取注释，并生成文档。
- `jdb`，Java调试器

## 基本语法
Overload 和 Override 区别？
- Overload 是多个函数使用同一个名字，但是参数不同
- Override 指的是子类对父类方法的重写。
- 加上`@override`以后，编译器会自动帮检查重写的函数签名是否正确。

## 面向对象
Java中的多重继承问题
- 不支持多重继承，因为可能会面临钻石问题，即子类继承自两个父类，可能会有歧义。
- 可以用接口实现多重继承，因为接口只定义方法，不实现方法，所以没有歧义。

建议多用组合，少用继承
- 组合就是把一个类作为另一个类的变量，直接用，这样耦合性小一些。
- 如果是继承，父类改了方法，子类可能也要跟着改，这在复杂的继承关系中很难维护。

什么是多态（polymorphism）？
- 多态指的是用单个符号代表多个不同的类型。
- 在面向对象（OOP，Object-Oriented-Programming）中，多态指的是为不同类型的实体提供单一的接口。

Ad-hoc 源自于希腊语，意思是 for this。一般指的是“专门”为了某个问题或者事情的解决方案，可以翻译成特设，比如特设委员会。这个词相反的意思是通用的。
Ad-hoc network 指的是自适应，不需要人为干预的网络。

什么是抽象类？
- `abstract class Animal` 用 abstract 修饰的类叫做抽象类。
- 抽象类不能被实例化，抽象类必须要有抽象方法，但是也可以有自己的方法和变量。
- 如果抽象类的所有方法都是抽象方法，没有变量，就叫做接口（`interface`）
- 一个类不能继承自多个类，但是可以实现多个接口。

匿名类
- 是个好东西，可以不用很麻烦的声明一个子类。直接在声明的时候，去重写需要的虚函数。一次性，日抛型的。

## classpath
classpath 类似 C++ 下的 lib path，用于搜索 class 文件。
- 可以设置：`/usr/shared:/usr/local/bin:/home/liaoxuefeng/bin`
- 不要在系统中设置 classpath，会污染整个系统环境，建议在启动 JVM 时设置 classpath。
- 即：`java -cp xxx` 或者 `java --classpath xxx`

class version
- 除了 JDK 有版本，java class 也有版本。
- Java 11 -> class 55
- Java 17 -> class 61

模块和包
- module 是为了瘦身，java 把自己的 rt.jar 拆分成了几十个 *.jmod
- 包相当于命名空间。


## Java 核心类
核心类
- `String` 字符串，是不可变的，是常量，线程安全的。
- `StringBuffer` 是线程安全的，对方法加了同步锁。
- `StringBuidler` 用于构造字符串。
- `StringJoiner` 类似 python 里的 join 函数
- AutoBox，可以在 `Integer` 和 `int` 之间转换。
- JavaBean，自动生成 get & set 函数。
- 枚举类 `enum Weekend { SUNDAY, SATURDAY }`
- 记录类 `record Point(int x, int y) {}`，相当于给类和方法加上 final 关键字，这样就无法派生子类，实例化后属性也没法修改。
- `BigInteger` & `BigDecimal` 大数
- `Math` & `HexFormat` & `Random` & `SecureRandom`

equals 和 == 有什么区别？
- `==` 除了基本类型，默认比较的是引用地址。
- `equals` 默认也是比较引用地址，但是如果重写了这个函数，会调用这个函数的逻辑。

hashCode 有什么用？
- 当把一个对象放到 HashMap 里时，判断条件是 hashCode && equals，
- 如果 hashCode 不同，对象也不同，此时就减少了 equals 的比较次数。
- hashCode 也是存放哈希值的地方。好的哈希算法会减少哈希碰撞。
- 重写 equals 时，一定也要重写 hashCode 方法。否则 hashCode 不一样的话，根本到不了 equals 的逻辑。

## Java 异常处理
异常的体系的 root class 是 Throwable，下面有两个子类：Error 和 Exception，Error 是严重的错误，不要捕获。Exception 则是可以处理的异常。

Java规定：
- 必须捕获的异常，包括 `Exception` 及其子类，但不包括 `RuntimeException` 及其子类。
- 不需要捕获的异常，包括 `Error` 及其子类，`RuntimeException` 及其子类，如数组越界,空指针等。

可以用 `e.printStackTrace()` 打印调用栈。

Java 虚拟机默认会忽略断言，可以用 `-enableassertions / -ea` 打开。很少用，建议永单元测试。

日志
1. JDK logging
   - `java.util.logging.Logger` Java自带的日志库。
2. Log4j
   - 比较复杂的日志库，用 `log4j2.xml` 来配置。
3. Commons Logging
   - `org.apache.commons.logging.Log` 
   - 阿帕奇的日志，底层是调用上面的两个。
4. SLF4J
   - `import org.slf4j.Logger`
   - 是对 Commons Logging 的改进，主要是支持 `logging.debug("a: {}", a)` 这样的写法。
5. Logback
   - 是 Log4j 的改进，性能更好。

一般是 Commons Logging + Log4j 的组合，但是更多的项目开始转向 SLF4j + Logback 的组合。

## Java Bean
Java Bean 是一种符合特定规范的 Java 类，用于封装数据。Java Bean 主要用于简化 Java 组件的管理，特别是在图形用户界面（GUI）构建和企业应用开发中。它的定义和使用有一些标准的要求和规范。

Java Bean 的规范
- 具有一个无参构造函数：Java Bean 必须有一个无参构造函数，使得 Java Bean 可以被创建和初始化，而不需要额外的参数。
- 属性可通过 getter 和 setter 方法访问：属性的访问和修改必须通过公共的 getter 和 setter 方法实现。方法名应遵循 getPropertyName 和 setPropertyName 的命名规则。
- 可序列化：Java Bean 类通常实现 Serializable 接口，以支持对象的序列化和反序列化过程。
- 属性是私有的：属性应该是私有的，通过公共的 getter 和 setter 方法来访问和修改这些属性。

```java
import java.io.Serializable;

public class Car implements Serializable {

    private static final long serialVersionUID = 1L;

    // 私有属性
    private String model;
    private int year;

    // 无参构造函数
    public Car() {
    }

    // Getter 和 Setter 方法
    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    @Override
    public String toString() {
        return "Car{model='" + model + "', year=" + year + "}";
    }
}

```

## 反射（Reflection）
反射是为了解决在运行时期，对某个实例的类型一无所知的情况下，如何调用其属性和方法，类似 python 里的 `getattr/setattr`。

`Class` 类是 JVM 描述 Java Class 的一个类。每当我们定义一个类，Java 虚拟机会创建一个 Class 实例，用于描述这个类的所有信息，如包名，属性和方法等。

通过Class实例获取class信息的方法称为反射（Reflection）。
1. 如果知道类名，直接获取静态变量，如 `Class c = String.class;`
2. 如果只有实例，直接调用 getClass 方法，如 `Class c = s.getClass();`
3. 通过完整的类名拿到，如 `Class c = Class.forName("java.lang.String");`

因为 JVM 中，同一个类的 Class 实例是唯一的，所以上面三种方法拿到的实例其实是一样的。

动态代理指的是在运行时动态创建一个接口的实例。

## 注解（Annotation）
注解是放在 Java 类、方法前面的一种特殊“注释”，主要分三种：
1. 编译器使用的，编译完就扔掉了，如 `@Override` 让编译器检查是否重写了父类方法，`SuppressWarnings` 让编译器忽略警告。
2. class 使用的注解，一般是底层库使用的，会存在于 class 文件中，但是不会在运行时被 JVM 加载。
3. 程序运行时的注解，程序加载后一直存在。如 `@PostConstruct` 可以让构造函数之后自动调用。

可以用 `@interface` 来自定义注解。

## 泛型
其实就是 C++ 里的模板。比如数组 `ArrayList<Integer>` 

Java 其实在定义泛型的时候，会把 T 当做是 Object 处理，然后运行时把 T 做类型转换。

```
┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐

│   (\_(\     (\_/)     (\_/)     (\_/)      (\(\   │
    ( -.-)    (•.•)     (>.<)     (^.^)     (='.')
│  C(")_(")  (")_(")   (")_(")   (")_(")   O(_")")  │

└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘
```

## 集合

Java标准库自带的 `java.util` 提供了集合类：`Collection`，是除了 `Map` 外所有的集合类的根接口。

Java 集合类主要有下面三种:
1. `List`，有序集合，如 `ArrayList`，`LinkedList`;
2. `Set`，无序集合，如
3. `Map`，哈希表，如 `HashMap`，`SortedMap`，`TreeMap`，`EnumMap`

Java 集合有几种特性：
1. 接口和实现是分离的，上面提到的三种都是接口，具体实现有 `ArrayList`, `LinkedList`.
2. 集合支持泛型
3. 集合的访问是通过迭代器实现。

下面的集中遗留的类不应该再使用：`HashTable`, `Vector`, `Stack`；

用哈希表的时候，需要实现 `equals` 和 `hashCode` 函数。
- 前者用于比较两个元素是否相同；
- 后者用于计算 hash key；

Properties 属性文件。

其他的数据结构
- `Queue` 先进先出队列。
- `PriorityQueue` 优先队列。
- `Deque` 双向队列
- `Stack` 栈

## IO
- `File` 对象
- `InputStream / OutputStream` 输入输出流。`FileInputStream / FileOutputStream`
- 序列化，可以实现 `Serializable` 接口。
- `Reader / Writer` 和 `FileReader / FileWriter`

## 日期
日期
- `Data` 和 `Calendar`

## 单元测试
JUnit

## 正则
直接用 `String.matches` 函数。
