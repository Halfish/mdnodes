# AOP

## AOP（Aspect-Oriented Programming，面向切面编程）

定义：AOP是一种编程范式，它允许将横切关注点（如日志记录、事务管理、权限检查等）从业务逻辑中分离出来，以模块化的方式应用到业务逻辑中。


AOP 是通过代理来实现的，代理有三种
1. 静态代理，直接实现和要代理的类实现同一个接口，手动掉代理的类的方法。
2. 动态代理，用 JDK原生的代理，Spring里有集成，需要实现一个接口
3. 动态代理，Cglib，已集成到 Spring 里，不需要实现一个接口

**AOP 底层架构**
1. 最上层，Spring基于注解的AOP
2. AspectJ 注解层，早起的 AOP框架，现在 Spring仍保留调用方式，但是重写了。
3. 实现层：动态代理和cglib


几个相关的注解
- `@Before` 代码执行之前
- `@AfterReturning` 
- `@AfterThrowing`
- `@After`
- `@Around`

```java
try {
    @Before
    ...user code
    @AfterReturning
} catch () {
    @AfterThrowing
} finally {
    @After
}
```

切点表达式
1. 固定语法 `execution`
2. 访问修饰符，`public / private`
3. 返回值参数 `String / int / void`
4. 包的位置
    - 具体包 `com.atguigu.service.impl`
    - 单层模糊 `com.atguigu.service.*`
    - 多层模糊 `com..impl`
5. 类名
    - 具体：`CalculatorPureImpl`
    - 模糊 `*`
    - 不分模糊 `*Impl`
6. 方法名，语法和类名一致
7. 参数
    - 没有参数：`()`
    - 有具体参数 `(String)`, `(String, int)`
    - 模糊参数 `(..)`
    - 不分模糊 `(String..)`, `(..int)`


环绕通知
- `@Around` 相当于是自定义的方式，比较灵活


定义多个切面的优先级
- 优先级高的，before先执行，after最后执行。
- 用 `@Aspect + @Order` 注解去规定切面的优先级。
- 值越小，优先级越高
