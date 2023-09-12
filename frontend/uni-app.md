
地图的坑：https://juejin.cn/post/7116722725212651528

生命周期
- [应用生命周期](https://zh.uniapp.dcloud.io/collocation/App.html#applifecycle)
    - `onLaunch()` App 初始化完成时触发（全局支只触发一次）
    - `onShow()` App 从后台进入前台显示时触发
- [页面生命周期](https://zh.uniapp.dcloud.io/tutorial/page.html#lifecycle)
    - `onInit()` 早于 onLoad；别用，只有百度小程序支持。
    - `onLoad()` 页面加载，数据、方法、props、slots 都有了；还没有 DOM 树；这里适合联网获取后台数据，更新data
    - `onShow()` 每次页面显示都会触发
    - `onReady()` 页面渲染完成，DOM 树可用
- [Vue组件生命周期](https://cn.vuejs.org/guide/essentials/lifecycle)
    - `mounted()` 组件完成实话渲染，并创建 DOM 节点后
