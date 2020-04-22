## FF-AID

#### 项目概述：

FF-AID是一款基于多设备互联的智能急救快应用。即点即用，一键求救。根据用户对突发疾病的语音描述，自动提取症状列表，查找相关疾病，并结合人脸识别匹配的患者既往病史等信息，计算给出置信度前三的疾病列表，完成病情初判。智能生成可能伴随病症待用户确认，以完善病情描述，得出二次判断。响应“互联网+医疗”形式，以最及时最准确的病情判断和急救指导提高患者的生存率。



#### 项目结构

项目主要包含三个模块,本模块对应Java后端工程：

- **ff-aid-master: Java后端：使用Springboot + Maven**
> - ff-aid-App: 快应用前端：使用html+css+js 快应用框架
> - ff-aid-python: 算法：使用python编写



##### JAVA后端：

项目的主入口文件为 FfaidApplication 入口函数为 main

``` java
@SpringBootApplication
public class FfaidApplication {

    public static void main(String[] args) {
        SpringApplication.run(FfaidApplication.class, args);
    }

}
```



基于Springboot，采用Maven组织项目，项目结构如下：

![image](ff-aid-master/image/image-20200420141012087.png)

##### 1. controller层：定义项目接口，包装VO提供给前端，API遵循restful原则

![image-20200420141917457](ff-aid-master/image/image-20200420141917457.png)

- **UserController**：用户操作接口，包含了**项目的大部分核心功能接口**，以及用户的基本操作

> - UrgentTelController：紧急联系人接口，包含了对紧急联系人的信息管理接口
> - IllDataController：既往病史接口，包含了对既往病史的管理接口
> - Neo4jController：Neo4j数据库访问接口，用于定义访问Neo4j非关系型数据库的接口
> - AidDataController：急救信息管理接口

项目已配置Swagger文档，具体接口表述和参数等信息可以查阅Swagger文档：

http://121.199.2.219:8080/swagger-ui.html

##### 2. Service层：主要的业务逻辑代码

![image-20200420152640879](ff-aid-master/image/image-20200420152640879.png)

- **UserService**：用户操作业务逻辑，**包含了项目的大部分核心功能的业务逻辑**，以及用户的基本操作

> - UrgentTelController：紧急联系人相关操作业务逻辑
> - IllDataController：既往病史接口相关操作业务逻辑
> - Neo4jController：Neo4j数据库访问修改操作业务逻辑
> - AidDataController：急救信息管理相关操作业务逻辑

##### 3. Dao层/Mapper层：数据持久层，连接数据库

![image-20200420153427830](ff-aid-master/image/image-20200420153427830.png)

![image-20200420153455644](ff-aid-master/image/image-20200420153455644.png)

#####  4. domain层：定义pojo对象

![image-20200420154127652](ff-aid-master/image/image-20200420154127652.png)

- 急救信息
- 既往病史
- 紧急联系人
- 用户

##### 5. faceapi：人脸识别操作

![image-20200420153535310](ff-aid-master/image/image-20200420153535310.png)

- FaceAdd   包含了人脸录入相关函数和业务逻辑
- FaceIdentify   包含了人脸识别相关函数和业务逻辑

##### 6. speechapi：语音识别，转文字操作

![image-20200420154356974](ff-aid-master/image/image-20200420154356974.png)

- AsrMain   包含了语音识别函数和业务逻辑
- common   文件夹中包含了语音识别相关的工具类

##### 7. util：包含了项目中的所有工具类

![image-20200420155410742](ff-aid-master/image/image-20200420155410742.png)

- BaiduAuth   用于获得百度AI接口的权限
- Base64Util    用于格式转换（人脸识别图像需要为64base）

- FileUploadUtil & FileUtil   文件相关操作工具类
- GsonUtils   用于解析Json字符串
- AdviceUtils   流行病给出建议相关类

##### 8. VO:  包装提供给前端的数据类型

![image-20200420160506486](ff-aid-master/image/image-20200420160506486.png)

- Output  返回给客户端的病情判断结果
- Description   病情初判的完整信息
- Symptoms   包含症状属性
- TelResult   返回给客户端的病人紧急联系人
- Result  人脸识别对应的结果

##### 9. config： 配置文件

![image-20200420160540839](ff-aid-master/image/image-20200420160540839.png)

- 对应项目的Swagger配置

##### 10. Exception

![image-20200420160630019](ff-aid-master/image/image-20200420160630019.png)

- 异常处理操作