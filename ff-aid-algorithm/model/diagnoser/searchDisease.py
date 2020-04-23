from py2neo import Graph , Node, Relationship
import jieba
import sys
import json


# SYMPTOM_SET_PATH = '/Users/pengfei/Desktop/medical/data/symptoms.txt'
# SYMPTOM_DICT_PATH = '/Users/pengfei/Desktop/medical/model/symptomsDic.txt'
DISEASE_DICT_PATH= '/Users/pengfei/Desktop/medical/data/diseasesDic.txt'


class DiseaseSeacher():
    def __init__(self, description = None):
        self.description = description
        self.diseaseSet = self.getDiseaseSet()
        self.graph = Graph("http://liublack.cn:7474",auth=("neo4j","200001"))
        self.diseaseItemProerties = ['name', 'department','description', 'position','reason', 
            'symptom', 'examination','treatment', 'complication', 
            'prevention', 'care', 'typicalSymptoms', 'relatedDiseases']

        jieba.set_dictionary(DISEASE_DICT_PATH)

    def search(self):
        diseases = self.processDesc()
        print('检测到的疾病：', diseases)
        diseaseDetails = self.getDiseaseDetails(diseases)
        return json.dumps(diseaseDetails, ensure_ascii = False)

    def getDiseaseSet(self):
        s = set()
        with open(DISEASE_DICT_PATH, 'r') as f:
            for line in f.readlines():
                s.add(line.strip().split(' ')[0])
        return s

    def processDesc(self):
        if self.description is None:
            return []
        self.description = ''.join(self.description.split(' '))
        diseases = []
        words = list(jieba.cut(self.description, cut_all = False))
        print('分词结果：', words)
        for word in words:
            if word in self.diseaseSet:
                diseases.append(word)
        return diseases
    
    def getDiseaseDetails(self, diseaseList):
        details = []
        for disease in diseaseList:
            node = self.graph.nodes.match('disease', name = disease).first()
            diseaseItem = dict()
            for pname in self.diseaseItemProerties:
                diseaseItem[pname] = node[pname]
            details.append(diseaseItem)
        return details

def searchDisease(description):
    searcher = DiseaseSeacher(description = description)
    return searcher.search()

if __name__ == "__main__":
    description = "冠心病怎么发噶大噶好给力卡"
    print(searchDisease(description))
