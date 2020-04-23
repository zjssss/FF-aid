# FF-AID 项目算法文件夹

本文件夹为FF-AID项目算法文件夹，主要实现了**医疗数据获取**，**医疗实体相关性自动判断算法**，**疾病诊断算法**，**流行疾病预测算法**，**词嵌入模型训练**等。

## 文件夹概况


### /dataCrawl
存储与爬取医疗数据相关的代码
* #### /dataCrawl/feiha
  爬取飞华网的相关代码
* #### /dataCrawl/xywy
  爬取寻医问药网的相关代码
* #### /dataCrawl/stopwords
  项目所用停用词

### /model
疾病诊断算法、词嵌入算法等代码
* #### /model/diagnoser
  疾病诊断、流行病预测算法相关代码
* #### /model/w2v
  word2vec相关代码
--- 
### 算法代码使用解释
  算法使用部分主要分为三个模块：

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
