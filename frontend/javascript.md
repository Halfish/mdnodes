
## 模块（Module）

语法
- `require/exports`
    - 是 CommonJS 引入的语法。
    - 现在的浏览器不支持，只有 Node.js 支持，一般在服务端使用；
    - 运行时动态加载
- `import/export`
    - 是 ES6 引入的语法
    - 静态编译

## Ajax
Ajax, AJAX = Asynchronous JavaScript and XML（异步的 JavaScript 和 XML）。

AJAX 不是新的编程语言，而是一种使用现有标准的新方法。

AJAX 最大的优点是在不重新加载整个页面的情况下，可以与服务器交换数据并更新部分网页内容。


XMLHttpRequest 对象用于和服务器交换数据。

```js
xmlhttp = new XMLHttpRequest();

// 发送请求
xmlhttp.open("GET","ajax_info.txt",true);
xmlhttp.send();

// 处理 Response
xmlhttp.onreadystatechange=function() {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        document.getElementById("myDiv").innerHTML = xmlhttp.responseText;
    }
}
```

## jQuery
```js
jQuery.getJSON(url, data, success(data, status ,xhr))

```

## JavaScript Promise
Javascript Promise 是 ES6 新增的一个类，目的是更加优雅的书写复杂的异步任务。

Promise 可以很方便的处理多个异步任务。有三个函数：
1. then：用于处理 Promise 成功状态的回调函数。
2. catch：用于处理 Promise 失败状态的回调函数。
3. finally：无论 Promise 是成功还是失败，都会执行的回调函数。

```js
new Promise(function (resolve, reject) {
    // 要做的事情...
    const result = 'Hello';
    relove('success');      // 表示正常
    // reject('failed');    // 表示失败了
    return result;
}).then(result => {
    // 正常时执行，result 是 Promise 返回的结果
}).catch(error => {
    // 报错时执行
}).finally(
    // 一定会执行
);
```

## ArrayBuffer 和 Uint8Array

`ArrayBuffer` 是用来存储二进制数据的，`Uint8Array` 这是读取二进制数据的一种视图，即每个字节都会被转成一个数字，范围是 0~255；

构造 ArrayBuffer / Uint8Array
```js
// 构造 Uint8Array，大于 255 的，高位 bit 会被忽略
const array = new Uint8Array([3, 255, 16, 256]); // 3, 255, 16, 0

// 构造 ArrayBuffer
const buf = new ArrayBuffer(3); // 3个字节
```

转换方法如下：
```js
// ArrayBuffer to Uint8Array
const buffer = new ArrayBuffer(3);
const array = new Uint8Array(ab, 0, 3)

// Uint8Array -> ArrayBuffer
const array = new Uint8Array([3, 255, 16]);
const buffer = array.buffer;
```

和字符串的转换
```js
// Uint8Array/ArrayBuffer -> String
const decoder = new TextDecoder('utf-8');
const str = decoder.decode(input)

// String -> Uint8Array
const encoder = new TextEncoder();
const array = encoder.encode(str)
```

# Passive 的问题
https://blog.csdn.net/weixin_44514894/article/details/116088933

如果 touch start/move 没有加上 `passive: true`，会有如下提醒，想让你加上。
```
[Violation] Added non-passive event listener to a scroll-blocking <某些> 事件. Consider marking event handler as 'passive' to make the page more responsive. See <URL>
```
加上以后，浏览器就不会有默认行为，会提升scroll的体验。
```
window.addEventListener('touchmove', func, {passive: true});
```
后者直接用库 `default-passive-events`，放在 main.js 里即可。


经过上面的操作，浏览器的默认行为触发不了了，每次 touchmove 想去触发默认行为，但是会失败，所以会有下面的报错：
```
Unable to preventDefault inside passive event listener invocation
```
所以要想办法取消默认行为，反正我们也不想响应。
