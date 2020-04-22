## FF-AID

#### 项目概述：

FF-AID是一款基于多设备互联的智能急救快应用。即点即用，一键求救。根据用户对突发疾病的语音描述，自动提取症状列表，查找相关疾病，并结合人脸识别匹配的患者既往病史等信息，计算给出置信度前三的疾病列表，完成病情初判。智能生成可能伴随病症待用户确认，以完善病情描述，得出二次判断。响应“互联网+医疗”形式，以最及时最准确的病情判断和急救指导提高患者的生存率。



#### 项目结构

项目主要包含三个模块

- ff-aid-App: 快应用前端：使用html+css+js 快应用框架
> - ff-aid-python: 算法：使用python编写
> - ff-aid-master: Java后端：使用Springboot + Maven



### 快应用APP前端：

---

#### 写在前面：以下的.ux文件中均由template模板和script脚本两部分组成

##### 一、应用模块总导航

Tabbar 导航栏分别导向一键求救界面（主界面）、流行疾病自测界面和我的界面（用户信息界面）
·包含tabbar.ux和tabbar.css文件

##### 二、一键求救功能模块

- Help 一键求救界面（主界面）
  ·包含help.ux和help.css文件
- Condition 患者症状输入界面
  ·包含condition.ux和condition.css文件
- Prejudice 病情初判界面
  ·包含prejudice.ux和prejudice.css文件
- Guigance 急救指导界面
  ·包含guidance.ux和guidance.css文件

##### 三、流行疾病自测功能模块

- Detection 流行疾病自测界面
  ·包含detection.ux、detection.css和illtype.ux文件，其中illtype.ux文件为自定义组件，内容是不同流行疾病类型对应的症状列表
- Detectionresult 检测结果界面
  ·包含detectionresult.ux和detectionresult.css文件
- Detectionanalyse 阶段综合分析界面
  ·包含detectionanalyse.ux文件，与检测结果界面共用detectionresult.css样式文件

##### 四、用户信息管理模块

- My 以导航形式分别导向注册界面和登录界面
  ·包含my.ux和my.css文件
- Register 注册界面
  ·包含register.ux和register.css文件
- Login 登录界面
  ·包含login.ux文件，与注册界面共用register.css样式文件

##### 五、卡片

- Card 负一屏卡片
- 包含card.ux和card.css文件

##### 六、其他

- Common 公用组件和样式文件夹
- MyCamera 用于人脸识别和人脸认证的相机界面
  ·包含mycamera.ux和camera.css文件