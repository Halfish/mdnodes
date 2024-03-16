
1. Robotaxi 后端功能和体验优化
    - 项目成果：完成了诸多后端功能开发迭代和优化。
    - 项目详情：
        - 行程分享：新增行程分享功能，乘客可以把自己的行程通过微信或者网页分享给亲友。
        - CityTimeConfig：单独拆分运营时间和节假日的配置，方便权限管理。
        - 语音通知：接入火山引擎的语音短信通知，如订单超时可以自动外呼给乘客。
        - 一键登录：后端通过阿里云接入通讯运营商的一键登录功能，优化登录/注册时的用户体验。
        - gcj02 坐标迁移: 迁移 gcj02 坐标，包括 onboard 和 mobile web 项目。
        - 自动驾驶成就数据统计重构： 用户驾驶成就的算法优化，根据 PlannerResult 识别 ADV 跨越障碍物，经过红绿灯等行为。
    - 相关链接：[#28580](https://github.corp.pony.ai/ponyai2/common/pull/28580), [#22789](https://github.corp.pony.ai/ponyai2/common/pull/22789), [#20928](https://github.corp.pony.ai/ponyai2/common/pull/20928), [#2690](https://github.corp.pony.ai/ponyai2/common/pull/2690), [#6674](https://github.corp.pony.ai/ponyai2/common/pull/6674)
2. RA-Client 接入 Robotaxi
    - 项目成员：xiaobinzhang (owner)
    - 项目成果：RA-Client 端上线了 Robotaxi Widget，RO可用来查看订单状态以及发送订单指令。该功能是 L4 无人运营的关键必要条件之一；
    - 项目详情：
        - RA-Client 支持显示订单、乘客信息，并支持控制订单状态，如取消 / 重置订单、绕圈，结束 post-trip 等；
        - RA-Voice 语音通话接入了飞连登录和赤兔权限控制，权限和人员的管理更加清晰。
    - 相关链接：[#9462](https://github.corp.pony.ai/ponyai2/common/pull/9462), [#11351](https://github.corp.pony.ai/ponyai2/common/pull/11351), [#10648](https://github.corp.pony.ai/ponyai2/common/pull/10648), [#16601](https://github.corp.pony.ai/ponyai2/common/pull/16601), [#17921](https://github.corp.pony.ai/ponyai2/common/pull/17921)
3. 集成阿里云呼叫中心
    - 项目成员：xiaobinzhang (owner)
    - 项目成果：RO 可以通过RA-Client 上的按钮，拨打订单绑定的隐私号，一键联系乘客。
    - 项目详情：
        - 前端嵌入阿里云web电话面板控件，支持飞连登录和权限认证。
        - 后端通过阿里云鉴权SDK，绑定阿里云账号与飞连邮箱，实现坐席的自动注册、登录和上线。
        - 通过接入火山引擎的隐私号服务，动态绑定和解绑用户的手机号，保护用户的隐私。
    - 相关链接：[云呼叫中心使用指南](https://ponyai.feishu.cn/docx/EuETdL4Kaodatdx7k5mcF7UxnUh), [云呼成本调研](https://ponyai.feishu.cn/sheets/YHhDsdsBJhEYt4tVFGJcAVnLnlg), [#40088](https://github.corp.pony.ai/ponyai2/common/pull/40088), [#41760](https://github.corp.pony.ai/ponyai2/common/pull/41760), [#27373](https://github.corp.pony.ai/ponyai2/common/pull/27373)
4. 锦江H5项目 - "pilot_uni_app"
 - 项目成员：xiaobinzhang (owner, H5), qiangzhichen(backend)
    - 项目成果：H5版本的 PonyPilot+ 开发完成，已接入“锦江荟”App和“锦江出行”微信公众号。
    - 项目详情：
        - pilot_uni_app 是 PonyPilot+ App的H5版本，集成了基础的打车功能，如账号注册和登录、订单管理、地图选点、站点搜索等功能。
        - 项目采用跨平台的前端框架 [uni-app](https://uniapp.dcloud.net.cn/) 开发，通过H5的方式嵌入到第三方App平台和微信公众号网页中。支持锦江会员的第三方的账号连通，以及唤起锦江平台App/Web端的订单支付功能。
    - 相关链接：[pilot_uni_app代码库](https://github.corp.pony.ai/service-and-application/pilot_uni_app),  [锦江对接文档&验收录屏](https://ponyai.feishu.cn/drive/folder/RcS5fik1El8yT6dr6zNciNyNnMg?from=from_copylink),
5. 企业用车
    - 项目成员：xiaobinzhang (owner)(Backend & Admin-web), kailiangtang(App), jiahuizhang(payment)
    - 项目成果：完成了后端和web管理页面的整体设计和开发工作。
    - 项目详情：
        - 在原有的 PonyPilot 账号体系上，企业用车支持批量导入企业用户。企业用户用车时可免付费，由企业管理员在管理网站上导出数据后进行财务结算。
    - 项目链接： [项目代码库](https://github.corp.pony.ai/service-and-application/enterprise-ride-admin), [后台技术设计文档](https://ponyai.feishu.cn/docx/VYAxdRvOmo3whQxU2CecS2jcnwX), [#41072](https://github.corp.pony.ai/ponyai2/common/pull/41072), [#42201](https://github.corp.pony.ai/ponyai2/common/pull/42201), [#45710](https://github.corp.pony.ai/ponyai2/common/pull/45710),
