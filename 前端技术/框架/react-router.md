### React Router
和 Angular、Vue 不一样，React 只是个 js library，并不是个完整的框架。路由需要单独的库支持，一般都会用 react-router.

### Routers
主要是下面几个 Router
- `createBrowserRouter`，推荐用，会使用浏览器的完整 URL。
- `createHashRouter`，用类似 `host/#/anchor` 这样的 URL。
- `createMemoryRouter`，主要是用来测试。
- `createStaticRouter`，用于服务端渲染。

这个函数有很多参数，但是只有 `routes` 参数比较常用，其他的基本用不到。
```js
// Type Declaration
function createBrowserRouter(
  routes: RouteObject[],
  opts?: {
    basename?: string;
    future?: FutureConfig;
    hydrationData?: HydrationState;
    window?: Window;
  }
): RemixRouter;
```

下面是一个 `createBrowserRouter` 的例子。
```js
import * as React from "react";
import * as ReactDOM from "react-dom";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

import Root, { rootLoader } from "./routes/root";
import Team, { teamLoader } from "./routes/team";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,      
    loader: rootLoader,
    children: [
      {
        path: "team",
        element: <Team />,
        loader: teamLoader,
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <RouterProvider router={router} />
);
```

### Router Component
下面这几个是 Router Component，不支持 data API，不推荐用。
- `<BrowserRouter>`
- `<HashRouter>`
- `<MemoryRouter>`
- `<NativeRouter>`，用于 React Native 项目
- `<StaticRouter>`

参数和 `createBrowerRouter` 基本类似。
```js
function App() {
  return (
    <BrowserRouter basename="/app" future={{ v7_startTransition: true }}>
      <Routes>
        <Route path="/" /> {/* 👈 Renders at /app/ */}
      </Routes>
    </BrowserRouter>
  );
}
```

### Route
Routes 可以用 objects 的形式传递。
```js
const router = createBrowserRouter([
  {
    // it renders this element
    element: <Team />,

    // when the URL matches this segment
    path: "teams/:teamId",

    // with this data loaded before rendering
    loader: async ({ request, params }) => {
      return fetch(
        `/fake/api/teams/${params.teamId}.json`,
        { signal: request.signal }
      );
    },

    // performing this mutation when data is submitted to it
    action: async ({ request }) => {
      return updateFakeTeam(await request.formData());
    },

    // and renders this element in case something went wrong
    errorElement: <ErrorBoundary />,
  },
]);
```

Layout Routes，这里可以用 `<Outle />` 做占位符。
```html
<Route
  element={
    <div>
      <h1>Layout</h1>
      <Outlet />
    </div>
  }
>
   <!-- 二级路由，index 表示默认展示的标签 -->
  <Route path="/" index element={<h2>Home</h2>} />
  <Route path="/about" element={<h2>About</h2>} />
</Route>
```

loader 可以用来加载数据。
```js
<Route
  path="/teams/:teamId"
  loader={({ params }) => {
    return fetchTeam(params.teamId);
  }}
/>;

function Team() {
  let team = useLoaderData();
  // ...
}
```