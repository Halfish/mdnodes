
## 1. 基础
### 选择器

参考：https://www.ruanyifeng.com/blog/2009/03/css_selectors.html

基本的选择器：
1. 通用选择器，`*`，选择任何元素。如 `* { margin: 0; padding: 0; }`
2. 标签选择器，`E`，匹配所有使用标签 `E` 的元素。如 `p { font-size: 2em; }`。
3. class 选择器，`.info`，如 `.info { background: #0f0; }`。可以重复用。
4. id 选择器，`#footer`，如 `#footer { background: #f0f; }`。只能用一次。

## 2. CSS 布局
参考 [MDN/CSS_layout](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/CSS_layout/Introduction)

### 2.1 正常布局流（normal flow）
指的是不对页面进行任何控制，默认的浏览器布局模式。

块元素（Block Element）：占据一行
内联元素 （inline element）：不占据一行

`display` 属性可以覆盖默认的布局行为，如：
- `block` 块元素，可以设置宽高，占据一行
- `inline` 内联元素，不可以设置宽和高，行排列
- `inline-block` 内联元素，但是可以设置宽和高
- `table`; 表格布局
- `flex`; 盒子布局
- `grid` 表格布局

`float` 浮动布局
- `none` 啥都不做
- `left` 放在左边，允许文本和内联元素环绕，该元素从正常布局流中删除。
- `right` 放在右边，同上。

`position` 指定元素在文档中的位置
- `static`; 默认，根据页面的正常流进行定位。忽略 `z-index/top/left` 之类的偏移。
- `relative` 相对布局；先放在正常的位置，然后相对做一些偏移
- `absolute`; 绝对布局；元素会被移出正常文档流，并不为元素预留空间。根据最近的祖先元素进行定位；如果没有祖先，会根据 body 定位，并滚动。
- `fixed`; 固定布局；元素会被移出正常文档流，并不为元素预留空间；屏幕滚动时不会变；
- `sticky`; 现根据正常文档流一起定位，然后跟着最近的滚动祖先一起滚动。

`overflow`:
- `visible`: 默认值，内容不能被裁减并且可能渲染到边距盒（padding）的外部。
- `hidden`: 超过 padding 会被裁剪，不提供滚动条。
- `clip`: 类似 hidden，但是会禁止编程的方式滚动。
- `scroll`: 滚动
- `auto`: 滚动，但是自动隐藏滚动条

### 2.2 Flex, Flexible Box Layout Module，弹性盒子布局

参考：https://www.ruanyifeng.com/blog/2015/07/flex-grammar.html

```css
.box{
  display: -webkit-flex; /* Safari */
  display: flex;
}
```

注意，设为 Flex 布局以后，子元素的 `float`、`clear` 和`vertical-align` 属性将失效。
设置 `display: flex` 属性，只会影响子元素的布局方式。


有 6 个属性：
```css
box {
  flex-direction: row | row-reverse | column | column-reverse;
  flex-wrap: nowrap | wrap | wrap-reverse;
  flex-flow: <flex-direction> || <flex-wrap>;
  justify-content: flex-start | flex-end | center | space-between | space-around;
  align-items: flex-start | flex-end | center | baseline | stretch;
  align-content: flex-start | flex-end | center | space-between | space-around | stretch;
}
```

- `flex-direction`: 排列方向，主轴是垂直还是水平方向。
- `flex-wrap`：如果一条轴线排不下，怎么换行。
- `flex-flow`：flex-direction || flex-wrap
- `justify-content`: 项目在主轴上的对齐方式
- `align-items`：定义项目在交叉轴上如何对齐
- `align-content`: 定义了多根轴线的对齐方式


### 2.3 Grid 布局
首先要设置 Grid 布局
```css
.box {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;  /* 声明3列 */
  grid-template-rows: 100px 100px;     /* 声明2行 */
  gap: 10px;  /* 格子的间距 */
}
```

