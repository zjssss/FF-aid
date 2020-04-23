from py2neo import Graph , Node, Relationship
import jieba
import sys
import json


# SYMPTOM_SET_PATH = '/Users/pengfei/Desktop/medical/data/symptoms.txt'
SYMPTOM_DICT_PATH = '/Users/pengfei/Desktop/medical/data/symptomsDic.txt'
DS_CORRELATION_PATH = '/Users/pengfei/Desktop/medical/data/correlation.txt'


class BayesDiagnoser():
    def __init__(self, description = None, symptoms = None,
                 age = None, gender = None):
        self.description = description
        self.symptoms = symptoms
        self.age = age
        self.gender = gender
        self.correlation = None
        self.symptomSet = self.getSymptomSet() # 获取所有可能的症状集合
        self.graph = Graph("http://liublack.cn:7474",auth=("neo4j","200001"))
        # self.connec = DBConc()
        # self.diseaseItemProerties = ['name', 'department','description', 'position','reason', 
        #     'symptom', 'examination','treatment', 'complication', 
        #     'prevention', 'care', 'typicalSymptoms', 'relatedDiseases']
        self.diseaseItemProerties = ['name']
        self.diseasesForMoreSymptoms = 3

        jieba.set_dictionary(SYMPTOM_DICT_PATH)
    def diagnose(self, filteNum = None):

        # 第一步，根据病情描述获取症状列表
        symptomList = self.getSymptoms()
        print('识别到的症状:', symptomList)

        # 第二步，根据症状列表获取所有相关的疾病
        diseaseSet = self._getDiseaseFromSymptoms(symptomList)
        diseaseList = list(diseaseSet)
        print('可能的疾病:', diseaseList)
        
        # 第三步，计算所有疾病的置信度
        scores = self._calDiseaseScore(diseaseList, symptomList)

        # 第四步，根据置信度得到预测疾病
        diseaseList = list(zip(diseaseList, scores))
        diseaseList.sort(key = lambda x: x[1], reverse = True)
        print('疾病的置信度为:', diseaseList)

        # 第五步，筛选出前diseasesForMoreSymptoms个疾病,并查找相关症状
        relatedSymptoms = self._getSymptomsFromDisease(diseaseList[0 : self.diseasesForMoreSymptoms])
        relatedSymptoms  = list(relatedSymptoms - set(symptomList))

        # 第六步，给出最终结果
        if filteNum is not None:
            diseaseList = diseaseList[0 : filteNum]

        diseaseDetials = self._getDiseaseDetails(diseaseList)
        # relatedSymptoms = self._getRelatedSymptoms(symptomList)
        
        result = {"disease": diseaseDetials, "symptoms":relatedSymptoms}
        result = json.dumps(result, ensure_ascii = False)
        print('最终结果:', result)
        return result
        

    def loadCorrelation(self):
        correlation = dict()
        with open(DS_CORRELATION_PATH, 'r') as f:
            for line in f.readlines():
                d = eval(line)
                correlation[d['name']] = d['data']
        self.correlation = correlation
        return correlation

    def getSymptomSet(self):
        s = set()
        with open(SYMPTOM_DICT_PATH, 'r') as f:
            for line in f.readlines():
                s.add(line.strip().split(' ')[0])
        return s

    def getSymptoms(self):
        if self.symptoms is None:
            self.symptoms = []
        else:
            map(lambda s: s.strip(), self.symptoms)
        self.symptoms.extend(self.processDesc())
        return self.symptoms

    def processDesc(self):
        if self.description is None:
            return []
        self.description = ''.join(self.description.split(' '))
        symptoms = []
        words = list(jieba.cut(self.description))
        print('分词结果：', words)
        for word in words:
            if word in self.symptomSet:
                symptoms.append(word)
        return symptoms

    def _calDiseaseScore(self, diseaseList, symptomList):
        scores = []
        if self.correlation is None:
            self.loadCorrelation()

        for disease in diseaseList:
            score = 1.0
            for symptom in symptomList:
                try:
                    score *= self.correlation[disease][symptom][0]
                except Exception:
                    score *= 0.1
                # score *= 1
            scores.append(score)
        return scores


    def _getSymptomsFromDisease(self, diseaseList):
        symptomSet = set()
        for disease in diseaseList:
            try:
                statement = 'MATCH (disease {name: "%s"})-[]->(n:symptom) RETURN n.name as name' %disease[0]
                cursor = self.graph.run(statement)
                while cursor.forward():
                    symptomSet.add(cursor.current['name'])
            except Exception as e:
                print(e)
        return symptomSet

    def _getDiseaseFromSymptoms(self, symptomList):
        diseaseSet = set()
        for symptom in symptomList:
            try:
                statement = 'MATCH (n:disease)-[]->(symptom {name: "%s"}) RETURN n.name as name' %symptom
                cursor = self.graph.run(statement)
                while cursor.forward():
                    diseaseSet.add(cursor.current['name'])
            except Exception as e:
                print(e)
        return diseaseSet
    
    def _existHaveRelationship(self, disease, symptom):
        ndisease = self.graph.nodes.match('disease', name = disease).first()
        nsymptom = self.graph.nodes.match('symptom', name = symptom).first()
        if ndisease is None or nsymptom is None:
            return False
        rel = self.graph.match_one((ndisease, nsymptom), r_type = 'd-s')
        return rel is not None
    
    def _getDiseaseDetails(self, diseaseList):
        details = [{'name' : d[0]} for d in diseaseList ]
        return details
    
    def _getRelatedSymptoms(self, symptomList):
        symptoms = set()
        for symptom in symptomList:
            node = self.graph.nodes.match('symptom', name = symptom).first()
            rels = self.graph.match((node, None) ,r_type = 's-s')
            relatedSymptoms = [rel.end_node['name'] for rel in rels ]
            symptoms.update(relatedSymptoms)
        return list(symptoms)
            


def diagnose(description, symptoms = None, age = None, gender = None, filteNum = 1):
    diagnoser = BayesDiagnoser(description = description, symptoms = symptoms, 
                age = age, gender = gender) 
    return diagnoser.diagnose(filteNum = filteNum)
    

if __name__ == "__main__":
    diagnose('我裂开了呀，我干咳，头痛，头晕,口吐白沫，昏迷,咳嗽', filteNum = 1)