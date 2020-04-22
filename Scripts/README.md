
### 项目部署方案

- 本项目目前已部署在云服务器，ip为121.199.2.219，端口号8080，可参照Swagger API文档访问接口

Swagger：http://121.199.2.219:8080/swagger-ui.html#/

#### 脚本FFAID.sh

- 该脚本对应于项目在云端部署的命令，需和jar包放在同一个文件夹执行
- 若需要自主部署，可能需要自行后端JAVA Maven项目打包，因为在后端调用算法Python模块，需要修改Python文件路径和数据文本路径，同时对于后端的文件存储位置也需要自主修改
- 若需要自主部署需要配置Python的相关环境，例如 py2neo，jieba，numpy，gensim等
- 运行脚本前要执行chmod 777 FFAID.sh使脚本具备执行权力
- 目前提供的jar包仅供参考，如果需要访问接口建议直接访问我们的服务器 ip

#### 关于运行代码需要修改的路径

- 在ff-aid-python中：confidenceBasedModel3.py文件中修改 SYMPTOM_DIC_PATH 为服务器symtomsDic.txt的路径

- 在ff-aid-master中：进入service文件夹中的UserService.java文件

  1. 修改UPLOAD_PATH为服务器中存放临时图片的文件夹
  2. 修改CHECK_PATH为服务器中存放临时校验图片的文件夹
  3. 修改函数 WordIdentify（）和函数 speechIdentifyDoc（）中 arguments 字符串中的路劲为服务器中存放 python 代码的路经

  

#### 注：

- 若有需求运行且运行过程有问题，可以联系电话/微信**13859994668**或在微信群中私戳我们~