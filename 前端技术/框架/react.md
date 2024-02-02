## React
React 是一个 JavaScript 库，用来构建 UI 界面。

### 链接
- [React.dev](https://react.dev/)
- [阮一峰-React技术栈](https://www.ruanyifeng.com/blog/2016/09/react-technology-stack.html)
- [阮一峰-React入门实例教程](https://www.ruanyifeng.com/blog/2016/01/babel.html)

### React Components
React Components 是 JavaScript functions.

React.Fragment 相当于是 <></>，可以用来返回多个元素。
```js
<>
  <OneChild />
  <AnotherChild />
</>
```

### JSX
JSX 可以结合 html 标签和 js 代码。

### state 状态管理
数据管理，响应式.

### ReactDOM

### Element
和 Flutter 有点像，element 是实际要渲染的 DOM 的抽象。React element 使用 objects 描述的，创建起来比较简单。

### React 组件的生命周期
组件的[生命周期](https://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/)主要分三步：
1. 挂载（Mount）
  - 组件完全挂载在网页中，会调用 `compoentDidMount` 函数。
  - 组件的渲染并且构造 DOM 元素插入到页面的过程称为组件的装载。
  - 装载阶段执行的函数会在组件实例被创建和插入 DOM 中时被触发，这个过程主要实现组件状态的初始化。
2. 更新（Update）
  - 属性（Props）或状态（State）的改变会触发一次更新阶段，但是组件未必会重新渲染，这取决于 shouldComponentUpdate。
  - 每次组件因为 state 和 props 变化而更新时，在重新渲染前该生命周期函数都会触发 `shouldComoponentUpdate`，常用语性能的调优。
  - 调用 `componentDidUpdate]` 函数。
3. 卸载（Unmount）
  - 调用 `componentWillUnmound` 函数。

### 多平台
支持桌面端和移动端。

### 框架
React 只是一个 UI 库，没法做 Routing 和 data fetching，官方推荐 Next.js 和 Remix，这两个是 full-stack React framework.

### Remix & Next.js & Vite
React 只是个 UI Library，真正要搭建一个项目，需要 Remix / Next.js / Vite 这样的框架。比如做一些数据请求，路由跳转、服务端渲染（SSR）等工作。

Remix 和 Next.js 的对比
- Next.js 更适合上手，Remix 则得折腾一番。
- Remix 适合做管理后台，对数据加载、嵌套数据、组件路由、异常数理等做的比较好。

### 一些 react 相关的库
- `@emotion/react` 用来方便的写 css 代码。
