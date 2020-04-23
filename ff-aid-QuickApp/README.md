

## 快应用APP前端：

### 写在前面：
1. 主入口文件为Tabber/tabber.ux
2. 以下的.ux文件中均由template模板和script脚本两部分组成

#### 一、应用模块总导航

Tabbar 导航栏分别导向一键求救界面（主界面）、流行疾病自测界面和我的界面（用户信息界面）
·包含tabbar.ux和tabbar.css文件

#### 二、一键求救功能模块

- Help 一键求救界面（主界面）
  ·包含help.ux和help.css文件
- Condition 患者症状输入界面
  ·包含condition.ux和condition.css文件
- Prejudice 病情初判界面
  ·包含prejudice.ux和prejudice.css文件
- Guigance 急救指导界面
  ·包含guidance.ux和guidance.css文件

#### 三、流行疾病自测功能模块

- Detection 流行疾病自测界面
  ·包含detection.ux、detection.css和illtype.ux文件，其中illtype.ux文件为自定义组件，内容是不同流行疾病类型对应的症状列表
- Detectionresult 检测结果界面
  ·包含detectionresult.ux和detectionresult.css文件
- Detectionanalyse 阶段综合分析界面
  ·包含detectionanalyse.ux文件，与检测结果界面共用detectionresult.css样式文件

#### 四、用户信息管理模块

- My 以导航形式分别导向注册界面和登录界面
  ·包含my.ux和my.css文件
- Register 注册界面
  ·包含register.ux和register.css文件
- Login 登录界面
  ·包含login.ux文件，与注册界面共用register.css样式文件

#### 五、卡片

- Card 负一屏卡片
- 包含card.ux和card.css文件

#### 六、其他

- Common 公用组件和样式文件夹
- MyCamera 用于人脸识别和人脸认证的相机界面
  ·包含mycamera.ux和camera.css文件