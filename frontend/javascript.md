
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
