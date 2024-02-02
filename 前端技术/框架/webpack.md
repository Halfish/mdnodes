## 0. Webpack
Webpack是一个模块打包工具(module bundler)，因为平常多用来对前端工程打包，所以也是一个前端构建工具。

模块打包，通俗地说就是：找出模块之间的依赖关系，按照一定的规则把这些模块组织合并为一个JavaScript文件。

安装
```bash
npm install --save-dev webpack@4.43.0 webpack-cli@3.3.12    
```

## 1. 入口和出口
```js
var path = require('path');  
module.exports = {
    // 项目打包入口目录
    context: path.resolve(__dirname, './src'),

    // 项目打包入口文件
    entry: './js/a.js',  // a.js里又引入了b.js

    // 打包出口
    output: {
        path: path.resolve(__dirname, ''),
        filename: 'bundle.js'
    },

    // 打包模式
    mode: 'none'
};
```

多入口打包
```js
entry: {
    app: ['core-js/stable', 'regenerator-runtime/runtime', './a.js'],
    vendor: './vendor'
},
output: {
    path: path.resolve(__dirname, ''),
    filename: '[name].js'
},
```
这样会打包出两个文件，'app.js' 和 'vendor.js'，各自会找各自的依赖。


## 2. Webpack loader
Loader是Webpack生态里一个重要的组成，我们一般称之为`预处理器`。

Webpack在进行打包的时候，对所有引入的资源文件，都当作模块来处理。但是 Webpack 自身只支持打包 JS 文件，图片和css等文件需要不同的 loader 来处理。

```js
const path = require('path');
  module.exports = {
    entry: './a.js',
    output: {
      path: path.resolve(__dirname, ''),
      filename: 'bundle.js'
    },
    // 这里用到了 css-loader / style-loader 预处理器，用来打包 css 文件
    module: {
      rules: [{
        // test 是一个正则表达式
        test: /\.css$/,
        // use 是要用到的 loader 数组
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.js$/,
        use: 'babel-loader',
        // exclude 表示不处理 node-modules 文件夹
        exclude: /node-modules/,
        // include 表示只处理 src 文件夹。
        include: /src/,
        // pre/post 表示该 loader 需要在所有的 loader 之前/之后执行。
        enforce: 'pre',
      }
      ]
    },
    mode: 'none'
  };
```

webpack 社区还有许多其他的成熟 loader
- `file-loader` / `url-loader` 处理文件（图片、视频等）
- `babel-loader` 对 ES6 转码
- `vue-loader` 处理 Vue 组件

当然，Webpack社区已经有比较成熟的loader了，我们可以直接拿来使用。本章会介绍一些常见的loader的使用，例如file-loader和url-loader来处理图片等资源，babel-loader来对ES6转码，vue-loader来处理vue组件。

下面的例子，定义了只有 `src/*.js` 引用的 `css` 文件才会被打包。
```js
rules: [{
    use: ['style-loader', 'css-loader'],
    // 要打包的目标资源
    resource: {
      test: /\.css$/,
      exclude: /node_modules/
    },
    // 引入资源的文件
    issuer: {
      test: /\.js$/,
      include: /src/
    }
  }]
```

## 3. Webpack Plugin 插件
下面的配置展示了如何引入插件 `clean-webpack-plugin`。

该插件可以用来清理每次打包后的资源。需要先安装：`npm i clean-webpack-plugin`

```js
const path = require('path');
  const { CleanWebpackPlugin } = require('clean-webpack-plugin');
  module.exports = {
    entry: './a.js',
    output: {
      path: path.resolve(__dirname, 'dist'),
      filename: 'bundle1.js'
    },
    plugins:[
      new CleanWebpackPlugin()    
    ],
    mode: 'none'
  };
```

下面的配置展示了如何引入插件 `copy-webpack-plugin`。

有些资源没有被任何地方引用，但是仍然想要放在打包后的资源目录，就可以用这个插件。
安装命令：`npm i copy-webpack-plugin`

```js
var path = require('path');
var CopyPlugin = require("copy-webpack-plugin");
module.exports = {
    entry: './a.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js'
    },
    plugins:[
        new CopyPlugin({
        patterns: [
            { from: path.resolve(__dirname, 'src/img/'), to: path.resolve(__dirname, 'dist/image/') },
        ],
        }),
    ],
    mode: 'none'
};
```

## 4. webpack 开发环境配置
可以用 `webpack --watch` 打开自身的监听模式，检测到文件变化后自动构建。

也可以用官方提供的 `webpack-dev-server` 工具来日常开发。

首先，通过命令 `npm i webpack-dev-server` 安装 DevServer，通过 `npx webpack-dev-server` 自动

配置里加一项 `devtool: 'source-map'` 就可以在 debug 模式下定位到原始文件。

## 5. webpack 生产环境配置
