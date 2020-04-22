## FF-AID

#### 项目概述：

FF-AID是一款基于多设备互联的智能急救快应用。即点即用，一键求救。根据用户对突发疾病的语音描述，自动提取症状列表，查找相关疾病，并结合人脸识别匹配的患者既往病史等信息，计算给出置信度前三的疾病列表，完成病情初判。智能生成可能伴随病症待用户确认，以完善病情描述，得出二次判断。响应“互联网+医疗”形式，以最及时最准确的病情判断和急救指导提高患者的生存率。



#### 项目结构

项目主要包含三个模块,本模块对应Java后端工程：

 - ff-aid-master: Java后端：使用Springboot + Maven
 - ff-aid-App: 快应用前端：使用html+css+js 快应用框架
 - ff-aid-python: 算法：使用python编写

--- 
#### 项目部署方案

- 本项目目前已部署在云服务器，ip为121.199.2.219，端口号8080，可参照Swagger API文档访问接口

Swagger：http://121.199.2.219:8080/swagger-ui.html#/

##### 脚本FFAID.sh

- 该脚本对应于项目在云端部署的命令，需和jar包放在同一个文件夹执行
- 若需要自主部署，可能需要自行后端JAVA Maven项目打包，因为在后端调用算法Python模块，需要修改Python文件路径和数据文本路径，同时对于后端的文件存储位置也需要自主修改
- 若需要自主部署需要配置Python的相关环境，例如 py2neo，jieba，numpy，gensim等
- 运行脚本前要执行chmod 777 FFAID.sh使脚本具备执行权力
- 目前提供的jar包仅供参考，如果需要访问接口建议直接访问我们的服务器 ip

##### 关于运行代码需要修改的路径

- 在ff-aid-python中：confidenceBasedModel3.py文件中修改 SYMPTOM_DIC_PATH 为服务器symtomsDic.txt的路径

- 在ff-aid-master中：进入service文件夹中的UserService.java文件

  1. 修改UPLOAD_PATH为服务器中存放临时图片的文件夹
  2. 修改CHECK_PATH为服务器中存放临时校验图片的文件夹
  3. 修改函数 WordIdentify（）和函数 speechIdentifyDoc（）中 arguments 字符串中的路劲为服务器中存放 python 代码的路经

  

##### 注：

- 若有需求运行且运行过程有问题，可以联系电话/微信**13859994668**或在微信群中私戳我们~