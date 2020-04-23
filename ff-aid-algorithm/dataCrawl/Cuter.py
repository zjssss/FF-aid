import jieba
import re
import os
from .Disease import Disease
from .Symptom import Symptom
from zhon.hanzi import punctuation
from medical.config import Configurer


class Cuter(object):
    def __init__(self, dicts = None):
        # jieba.enable_paddle() # 启动paddle模式。 0.40版之后开始支持，早期版本不支持
        # 加载词典
        if dict is not None:
            for d in dicts:
                jieba.load_userdict(d)
        # 加载停用词典
        # jieba.analyse.set_stop_words('/stopwords/baidu_stopwords.txt')
        if not os.path.isdir(Configurer.DISEASE_SENTENCE_DIR):
            os.makedirs(Configurer.DISEASE_SENTENCE_DIR)
        if not os.path.isdir(Configurer.SYMPTOM_SENTENCE_DIR):
            os.makedirs(Configurer.SYMPTOM_SENTENCE_DIR)

    def cutAndSave(self, item):
        baseDir = None
        if type(item) == Disease:
            baseDir = './diseases/'
        elif type(item) == Symptom:
            baseDir = './symptoms/'
        else:
            raise Exception('类型错误：类型不是Disease或Symptoms')
        f = open(baseDir + item['name'] + '.txt', "w")

        for pname in item:
            if type(item[pname]) == list:
                for content in item[pname]:
                    # content = re.sub(r'&#13;', '\n', content) # 剔除回车符
                    # content = re.sub(r'\s', '\n', content) # 剔除空格
                    # content = re.sub(r'<[\w\W]*?>', '', content) # 剔除标签
                    # content = re.sub(r'[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）]+', '', content) # 剔除符号
                    content = re.sub(r'[%s]+' %punctuation, '', content)
                    content = re.sub(r'[\s]+', '', content)
                    words = jieba.cut(content, cut_all = True, HMM = False) 
                    f.write(' '.join(words))
                    f.write('\n')
            else:
                content = item[pname]
                # content = re.sub(r'&#13;', '\n', content) # 剔除回车符
                # content = re.sub(r'\s', '\n', content) # 剔除空格
                # content = re.sub(r'<[\w\W]*?>', '', content) # 剔除标签
                # content = re.sub(r'[\s+\.\!\/_,$%^*(+\"\')：]+|[+——！，。？?、~@#￥%……&*（）：]+', '', content) # 剔除符号
                content = re.sub(r'[%s]+' %punctuation, '', content)
                content = re.sub(r'[\s]+', '', content)
                words = jieba.cut(content, cut_all = False, HMM = False) 
                f.write(' '.join(words))
                f.write('\n')
        f.close()

def test():
    pass

if __name__ == "__main__":
    test()