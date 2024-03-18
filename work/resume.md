PonyPilot+ APP
- 项目背景
    - PonyPilot+ 是小马智行研发的基于flutter框架的出行软件，是自动驾驶车队对外运营 Robotaxi 服务的对外平台。
- 工作内容
    - 积分商城
        - 独自开发和上线了积分商城系统的全部功能，主要包括积分任务的设计，商品的兑换流程，积分的管理等。
        - 项目主要包括后台数据库表设计以及flask接口功能实现，App内积分商城flutter页面的实现，以及基于React的管理页面。
    - PonyPilot+ H5 版本
        - 实现了包含基础功能的H5版本PonyPilot+，包括地图组件、站点搜索、完整的订单流程、以及支付功能等。
        - 项目基于 uniapp 开发，底层是 Vue 框架，通过WebView的方式用于嵌入到第三方App和微信公众号里。
    - RA-Client Robotaxi Widget
        - RA-Client 是远程操作员管理车辆和订单的工具，底层用的C++ ImGui开发，我主要负责和Robotaxi相关的Widget功能开发和维护。
        - Robotaxi Widget 主要支持显示订单和乘客信息，接入云呼平台和乘客联系，支持发送订单控制指令。

Fleet-Control-Center 后端管理系统
- 项目背景
    - FCC是PonyPilot+ App背后的，基于 python flask 框架开发的后端管理系统。
- 工作内容
    1. 虚拟派单优化
        - 普通虚拟单：重构和优化后台虚拟单生成的定时脚本，设计可配置的虚拟单生成流程，为不同业务类型的车辆生成对应的虚拟单。
        - 跨区域单：通过跨区域单，动态调度多个运营区域内的车辆数量到预设的比例。
        - 高峰期调度单：通过历史数据，提前调度空余的车辆到高峰期繁忙的站点，减轻运营压力。
    2. 自动驾驶成就
        - 后台根据onboard车辆状态数据和订单信息，生成行程的一些自动驾驶成就数据，如统计行程中通过红绿灯的个数和跨越障碍物的次数等。
        - 给用户累计里程生成排行榜，后端采用 redis zset 实现。
    3. 企业支付
        - 支持企业员工打车，后台记录所有企业订单，定期和企业对账。
        - 开发基于Material-UI 和 React框架的后台管理系统，用 k8s 部署到集群。
    4. 曹操出行
        - 支持在曹操出行 App 接入 Pony Robotaxi 服务。
        - 负责开发单独的 Agent 服务。通过桥接 Onboard ODP 模块和曹操出行后端服务，同步站点、订单、车辆等信息。

## 个人技能
个人技能
- 熟悉基于python的后端开发框架，如 flask，sqlalchemy, alembic, gunicorn, rq(Redis Queue), protobuf, grpc 等
- 熟悉前端web框架，如react，vue & uniapp，以及相关的项目开发工具，如 webpack, nodejs 等。有多个前端项目的开发经验。
- 熟悉移动端开发框架，开发过Android，flutter框架
- 熟悉 MySQL & NoSQL，了解 索引 & 事务，分布式
- 熟悉 kafka, 消息队列 了解分布式
- 熟悉 k8s, docker, jenkins, argo 等 DevOps 工具。
- 熟悉 Linux, bash, git, bazel, protobuf 开发工具链
- 熟悉 C++，了解 STL ，了解链接编译的基本原理。


挑战
- 业务驱动，弱化技术背景，目标导向。（解决方法：不要太深入某个技术，还是已解决问题为主。）
- 全栈，快速掌握一个方向的技能，并产出结果。如支持RO拨打电话（RA-Client C++，接入阿里云&火山引擎，flask接口，飞连登录，js前端）。


github link
