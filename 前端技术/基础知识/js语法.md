# JavaScript

## 导论

JavaScript 是一门什么样的语言？
- JS 是一种轻量级的脚本语言（script language），不具备开发操作系统的能力，只是个能用来调用其他大型应用程序（如浏览器）的脚本。
- JS 是一种嵌入式语言（embedded language），本身提供的核心语法不多，只适合调用宿主环境的 API；
- JS 是一种对象模型语言，支持面向对象和函数式编程。

JavaScript 的语法主要包括下面几个部分：
1. 基本语法，如变量、控制流等
2. 标准库，Object，Array，Math，Date 等
3. DOM，如 Document，Element 等；
4. 浏览器 API，如 Windows，History，Cookie 等

JavaScript 历史
- 1990年底，万维网（WWW）在欧洲核能研究组织诞生。
- 1992年，美国国家超级电脑中心（NCSA）开发了第一个浏览器 Mosaic（马赛克）
- 1994年10月，NCSA程序员成立 Mosaic公司，后改名 Netscape（网景公司）。
- 1994年12月，新一代浏览器 Netscape Navigator发布1.0版本，市场份额超过90%
- 1995年，Netscape员工 Brendan Eich 基于 Scheme 语言开发了浏览器脚本语言
- 1995年，脚本语言开始叫做 Mosaic，后改名 LiveScript，12月改名为 JavaScript
- 1996年，Netscape Navigator 2.0 正式内置了 JavaScript 语言

JavaScript 发展史
- 1996年，微软模仿 JavaScript 开发了一种近似的语言，叫做 JScript，内置于 IE3.0；
- 1996年，Netscape公司决定把 JavaScript 提交给国际标准化组织（ECMA，European Computer Manufacturers Association），希望 JavaScript 能成为国际组织，以此抵抗微软。
- 1997年7月，ECMA发布了第一版浏览器脚本语言的标准 ECMAScript 1.0版；（这是语言的标准，而JavaScript是语言的实现）
- 1998年6月，ECMAScript 2.0 版发布
- 1999年12月，ECMAScript 3.0 版发布，成为 JavaScript 通行标准
- 2007年10月，ECMAScript 4.0 草案发布，但是升级目标太过激进被大公司反对，
- 2008年7月，4.0版本被废除，项目命名为“Harmony”，涉及功能改善的部分发布为 ECMAScript 3.1 版本，
- 2009年12月，ECMAScript 3.1 版本改名为 ECMAScript 5.0 bing正式发布
- Harmony 项目一分为二，可行的设想为 JavaScript.next 继续开发，不成熟的设想为 JavaScript.next.next 
- 2011年6月，ECMAScript5.1 发布，到2012年底，所有的主流浏览器都支持了 ECMAScript 5.1。
- 2015年6月，ECMAScript 6.0 正式发布，并更名为 ECMAScript 2015


## 基本语法

全局变量
- `a = 1`，如果在函数外，该表达式会隐式声明一个全局变量。不推荐这么做。
- `var a = 1`，声明并赋值一个变量。如果在函数外声明，则为全局变量。
- 用 `let` 或者 `const` 替代 `var`，同样可以声明全局变量，但是不会挂载到 `windows` 对象上
- 在 `Node.js` 中，需要挂载到 global 对象上，`global.a = 1`，才能声明一个全局变量。

变量提升（hoisting）
- JavaScript 引擎的工作方式是，先解析代码，获取所有被声明的变量，然后再运行。
- `console.log(a); var a = 1;` 是可以运行的，会输出 `undefined`，因为 `a` 会被先声明；

数据类型
- 原始类型（primitive type）
  - 数值（整数、浮点数）、字符串、布尔值
- 合成类型（complex type）、
  - 对象：由多个原始类型的值合成。
    - 侠义的对象（object）
    - 数组（array）
    - 函数（function）
- undefined 变量未定义
- null 变量为空

类型运算符
- `typeof` 运算符，返回字符串。
  - `typeof a;          // "undefined"`
  - `typeof "hello"     // "string"`
  - `typeof 32          // "number"`
  - `typeof []          // "object"`
  - `typeof {}          // "object"`
  - `typeof null        // "object"`     历史遗留问题，为了兼容以前的代码
- `instanceof` 运算符，二元操作符
    - `[1,2,3] instanceof Array  // true`

null 和 undefined 的区别
- `null` 和 `undefined` 都表示无
- 在布尔表达式中都可以转成 `false`；
- 转换数值类型时，`null` 为 `0`，`undefined` 为 `NaN`
  - `null + 4         // 4`
  - `undefined + 4    //  NaN`

JavaScript 里的数值
- JavaScript 浮点数由 64 个二进制位组成
  - a. 第一位，符号位，0表示正数，1表示负数
  - b. 第2~12位（共11位），指数部分
  - c. 第 13~64 位（共52位）：小数部分（即有效数字）
- 根据 `IEEE754` 标准，浮点数表示成 $(-1)^a * (c+1) * 2^{b-1023}$ 的形式
  - a 符号位
  - b 指数部分，取值 0~2047，即 $2^{-1023}$ ~ $2^{1024}$
  - c 有效数字，取值的绝对值小于 $2^{53}$，即 $-2^{53}+1$ ~ $2^{53}-1$

数值范围
- JavaScript 只能处理 15 位数字，超过可能会丢失精度。
- 如果数字大于 $2^{1024}$，会发生正向溢出。
  - `Math.pow(2, 1023)   // 8.98846567431158e+307`
  - `Math.pow(2, 1024)   // Infinity`
- 最小的正数是 $2^{-1023-52} = 2^{-1075}$，小于这个数直接转成 `0`.
  - `Math.pow(2, -1074)    // 5e-324`
  - `Math.pow(2, -1075)    // 0`
- 上面提到的最大值和最小值有定义
  - `Number.MAX_VALUE // 1.7976931348623157e+308`
  - `Number.MIN_VALUE // 5e-324`

字符串
- 由于历史原因，JavaScript 只支持两个字节的 UTF-16
- base64 转码
  - `btoa()` 把任意值转成 base64 编码的字符串（注意是先把变量变成 string，再转）
  - `atob()` 把 base64 编码的字符串转回字符串
- 中文的转接码
  - `btoa(encodeURIComponent("你好hello"))`
  - `decodeURIComponent(atob("JUU0JUJEJUEwJUU1JUE1JUJEaGVsbG8="))`

对象
- 返回键值 `Object.keys(object) // [key1, key2]`