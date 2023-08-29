

## 一、创建 App

createApp
- 创建 App

createSSRApp
- SSR 指的是服务端渲染 
- https://cn.vuejs.org/guide/scaling-up/ssr.html


SFC, Single File Component，单文件组件


## 二、API 风格

选项式 API（Option API）
```js
<script>
export default {
  // data() 返回的属性将会成为响应式的状态
  // 并且暴露在 `this` 上
  data() {
    return {
      count: 0
    }
  },

  // methods 是一些用来更改状态与触发更新的函数
  // 它们可以在模板中作为事件处理器绑定
  methods: {
    increment() {
      this.count++
    }
  },

  // 生命周期钩子会在组件生命周期的各个不同阶段被调用
  // 例如这个函数就会在组件挂载完成后被调用
  mounted() {
    console.log(`The initial count is ${this.count}.`)
  }
}
</script>

<template>
  <button @click="increment">Count is: {{ count }}</button>
</template>
```

组合式 API（Composition API）

```js
<script setup>
import { ref, onMounted } from 'vue'

// 响应式状态
const count = ref(0)

// 用来修改状态、触发更新的函数
function increment() {
  count.value++
}

// 生命周期钩子
onMounted(() => {
  console.log(`The initial count is ${count.value}.`)
})
</script>

<template>
  <button @click="increment">Count is: {{ count }}</button>
</template>
```


## 三、模板

#### v-html
嵌套 HTML

```html
<!-- rawHtml 原本是字符串，但是这里当做 HTML 代码来解析 -->
<p>Hello <span v-html="rawHtml"></span></p>
```

#### v-bind
用来绑定 HTML 标签属性
```html
<!-- 绑定 id 属性 --> 
<div v-bind:id="dynamicId"></div>
<!-- 简写 --> 
<div :id="dynamicId"></div>

<!-- 布尔型 --> 
<button :disabled="isDisabled"> Button </button>
```


#### v-if / v-else / v-show
```html
<!-- 当布尔值为 false 时，会移除该元素 -->
<p v-if="seen"> Now you see me. </p>
<p v-else> Oh No </p>

<!-- 当布尔值为 false 时，会隐藏该元素  -->
<p v-show="seen"> Now you see me. </p>
```

#### v-on
绑定事件，会监听 DOM 事件

```html
<!-- 监听事件 -->
<a v-on:click="doSomething"></a>

<!-- 用 @ 简写 -->
<a @click="doSomething></a>
```

## 四、响应式基础（Reactivity Fundamentals）
声明响应式状态

在组合式 API，建议用 `ref` 函数来声明响应式状态。
```js
import { ref } from 'vue'

const count = ref(0);

// 在 js 里，需要用 .value 来取值，模板里就不用
console.log(count.value);
```

`nextTick()` 函数可以用来用来更新 DOM，刷新缓存。

reactive 函数

```js
import {reactive } from 'vue'

const state = reactive({count: 0});
```

reactive 会返回原始对象的代理，并提供响应。
reactive 有一些局限性，如
- 只能用于对象类型，如 Map、Set，不能用于 `string`，`number`，`boolean` 类型。
- 不能替换整个对象，否则响应式连接会丢失。
- 对结构操作不友好，将属性传给函数时，会丢失响应相连接。


## 五、计算属性
一些复杂的计算，可以放到 `computed()` 里计算，就不用在模板写了。有点像 @property.

## 六、class 和 style 绑定，list 渲染

class 属性
```js
<div class="static" :class="{ active: isActive }"></div>

// 会渲染成
<div class="static active"></div>
```

style 属性
```js
const styleObject = reactive({
    color: 'red',
    fontSize: '13px',
})

<div :style="styleObject"></div>
```

列表渲染
```js
// 展开 List
<li v-for="item in items">
    {{ item.message }}
</li>

// 展开 Object
<li v-for="(key value) in myObject">
    {{ key }} -> {{ value }}
</li>
```

## 七、侦听器（watchers）
```js
const question = ref(0)

watch(question, async (newQuestion, oldQuestion) => {
    console.log(newQuestion);
    console.log(oldQuestion);
})
```

## 八、组件基础

一个单文件组件（SFC）的例子
```js
<script setup>
import { ref } from 'vue'

const count = ref(0)

// 定义属性
defineProps(['title'])
defineProps({
    title: String,
    likes: Number,
})
</script>

<template>
  <button @click="count++">You clicked me {{ count }} times.</button>
</template>
```

可以这样使用组件
```js
const posts = ref([
    {id: 1, title: "Alice"},
    {id: 2, title: "Bob"},
    {id: 3, title: "Cindy"},
])
<BlogPost
    v-for="post in posts"
    :key="post.id"
    :title="post.title"
/>
```

## 九、组件事件
template 中可以自定义事件
```js
// 这里用 emit 出发自定义事件
<button @click="$emit('someEvent')"> click me </button>

// 这里是父组件，可以自定义事件的回调
<MyCompoment @some-event="callback" />
```

template 中的 `$emit` 函数不能在 `<script setup>` 中使用，可以用 `defineEmits()` 替代，
```js
<script setup>
const emit = defineEmits(['inFocus', 'submit'])

function buttonClick() {
    emit('submit')
}
</script>
```

## 十、路由 Router
在 SPA 中，路由是客户端（浏览器）控制的，在服务端渲染的应用中，后端会根据不同的 URL 返回新的 HTML，浏览器会重新渲染页面。


## 十一、slot
用来给 Component 模板中的内容占位。

```html
<!-- 假设 <MyCompoment> 中的模板这样写 -->
<button class="my-btn">
    <slot></slot>
</button>

<!-- 使用组件时 -->
<MyComponent>
    这段内容会替代 slot 里的内容
</MyComponent>
```

带名字的 slot 稍微麻烦点，需要用到 `v-shot` 指令。
```html
<!-- BaseLayout 组件里这样写 -->
<div class="container">
  <header>
    <slot name="header"></slot>
  </header>
  <main>
    <slot></slot>
  </main>
  <footer>
    <slot name="footer"></slot>
  </footer>
</div>

<!-- 使用组件时 -->
<BaseLayout>
  <template v-slot:header>
    <!-- header 插槽的内容放这里 -->
  </template>

  <!-- 可以用 # 简写来替代 v-shot -->
  <template #default>
    <p>Default Content</p>
  </template>

  <template #footer>
    <p>Default Content</p>
  </template>

</BaseLayout>
```
