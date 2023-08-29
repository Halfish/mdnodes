

# 选择器

参考：https://www.ruanyifeng.com/blog/2009/03/css_selectors.html

基本的选择器：
1. 通用选择器，`*`，选择任何元素。如 `* { margin: 0; padding: 0; }`
2. 标签选择器，`E`，匹配所有使用标签 `E` 的元素。如 `p { font-size: 2em; }`。
3. class 选择器，`.info`，如 `.info { background: #0f0; }`。可以重复用。
4. id 选择器，`#footer`，如 `#footer { background: #f0f; }`。只能用一次。


# Flex Layout，弹性布局

参考：https://www.ruanyifeng.com/blog/2015/07/flex-grammar.html

```css
.box{
  display: -webkit-flex; /* Safari */
  display: flex;
}
```

注意，设为 Flex 布局以后，子元素的 `float`、`clear` 和`vertical-align` 属性将失效。


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

- flex-direction: 排列方向，主轴是垂直还是水平方向。
- flex-wrap：如果一条轴线排不下，怎么换行。
- flex-flow：flex-direction || flex-wrap
- justify-content: 项目在主轴上的对齐方式
- align-items：定义项目在交叉轴上如何对齐
- align-content: 定义了多根轴线的对齐方式
