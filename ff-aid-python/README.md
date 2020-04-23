## FF-AID

#### 项目概述：

FF-AID是一款基于多设备互联的智能急救快应用。即点即用，一键求救。根据用户对突发疾病的语音描述，自动提取症状列表，查找相关疾病，并结合人脸识别匹配的患者既往病史等信息，计算给出置信度前三的疾病列表，完成病情初判。智能生成可能伴随病症待用户确认，以完善病情描述，得出二次判断。响应“互联网+医疗”形式，以最及时最准确的病情判断和急救指导提高患者的生存率。



#### 项目结构

项目主要包含三个模块,本模块对应Java后端工程：

- **ff-aid-python: 算法：使用python编写**

> - ff-aid-master: Java后端：使用Springboot + Maven
> - ff-aid-App: 快应用前端：基于快应用框架

---



### Python算法：

算法主要分为三个模块：

1. ##### 基于 ***贝叶斯优化***  的急救病情判断算法 

   *bayesBasedModel.py*

2. ##### 流行病检测算法                                   

   *specialDiseaseDiagnosis.py*

3. ##### 优化之前的急救病情判断算法

   *confidenceBasedModel.py*



##### 基于贝叶斯优化的急救病情判断算法：

- 对应代码为 bayesBasedModel.py 

- 主入口函数为 main 

  ``` python
  if __name__ == "__main__":
      diagnose(sys.argv[1], filteNum = 3)
  ```

  参数 sys.argv[1] 表示输入的病症，这里是通过调用获取的，若想要直接调用可以改成字符串如

  ```python
  if __name__ == "__main__":
      # diagnose(sys.argv[1], filteNum = 3)
      diagnose('这里有个人脸色苍白，呼吸困难，并且口吐白沫，还在地上抽搐', filteNum = 3)
  ```

  参数 filteNum 对应获得的置信度最高的几个病症，比如为3即表示获得置信度前三的疾病。

  

> 优化后的病情判断算法目前可以达到单词检测 5s-10s 左右的速度，相比于未优化时的算法有了巨大的进步



##### 流行病检测算法：

- 对应代码为 specialDiseaseDiagnosis.py

- 主入口程序为 main

  ```python
  if __name__ == "__main__":
      diagnose(sys.argv[1], '新冠 ')
  ```

  参数 sys.argv[1] 表示输入的病症，这里是通过调用获取的，若想要直接调用可以改成字符串如

  ```python
  if __name__ == "__main__":
      diagnose('头晕,咳嗽,干咳', '新冠 ')
  ```

  参数 ‘ 新冠 ’ 对应要检测的疾病，这里以新冠举例



> 流行病检测算法基本可以实现在 2s 内获得检测结果



##### 优化前的急救病情判断算法

- 对应代码为 confidenceBasedModel.py
- 使用方法和 bayesBasedModel.py 无异