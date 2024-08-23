# IoC 容器

## XML

## 标注

常见的几个标注
- `@Component` 默认标注
- `@Repository`, `@Service`, `@Controller`，和 `@Component` 作用一样。
- `@PostContruct` 执行初始化，`@PreDestroy` 析构之前
- `@Scope(scopeName = ConfigurableBeanFactory.SCOPE_SINGLETON/SCOPE_PROTYPE)` 指定单例、多例

依赖注入的标注
- `@Autowired` 自动装配注解，可以用来做依赖注入。在 IoC 容器中查找指定类型的组件对象，设置属性。
    - 如果找不到对象，装配失败
    - 找到一个，执行装配
    - 找到不止一个，用 `@Qualifier(value="userService2")` 注解，否则失败
- `@Resource(name="userService2")` = `@Autowired` + `@Qualifier(value="userService2")`
    - JSR-250，Java中定义的，Spring框架实现的注解
    - 一个注解顶两个
    - 需要额外导入包 `jakarta.annotation-api`

直接赋值
- `@Value("${jdbc.username:admin}")` 直接赋值，冒号后面的 `admin` 是默认值。
