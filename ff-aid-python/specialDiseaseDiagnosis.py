from py2neo import Graph , Node, Relationship
import jieba
import sys
import json

# SYMPTOM_SET_PATH = '/Users/pengfei/Desktop/medical/model/symptoms.txt'
SYMPTOM_DIC_PATH = 'C:\\Users\\Administrator\\Desktop\\下\\OPPO\\v2\\symptomsDic.txt'


class Diagnoser():
    def __init__(self, description, disease, sep = ',', alpha = 0.2, S1_depth = 1, S2_depth = 5):
        self.description = description
        self.disease = disease
        self.S1_depth = S1_depth
        self.S2_depth = S2_depth
        self.sep = sep
        self.alpha = alpha

        self.symptoms = self.getSymptoms()
        
        self.symptomSet = self.getSymptomSet() # 获取所有可能的症状集合
        self.graph = Graph("http://liublack.cn:7474",auth=("neo4j","200001"))

        jieba.set_dictionary(SYMPTOM_DIC_PATH)
    def diagnose(self):
        node = self.graph.nodes.match('disease', name = self.disease).first()
        if node is None:
            raise Exception("no this disease.")
        symptoms = self._getSymptomsFromDisease([self.disease])
        # print(symptoms)
        frac = len(symptoms)
        prob = self.getSymptomsScore() / frac
        prob = prob if prob < 1 else  1
        print(prob)
        return prob

    # def diagnose(self):
    #     print(self.score(1))
    #     # 第一步，查找是否存在这个疾病
    #     node = self.graph.nodes.match('disease', name = self.disease).first()
    #     if node is None:
    #         raise Exception("no this disease.")

    #     # 第二部，提取S1，S2
    #     S1 = self.getS1()
    #     print("S1:", S1)
    #     # S2 = self.getS2()
    #     S2 = dict()
    #     print("S2", S2)

    #     # 第三步，获取所有用于计算概率的症状
    #     symptoms = set(S1).union(self.symptoms.intersection(set(S2)))

    #     # 计算概率
    #     prob = 1
    #     for symptom in symptoms:
    #         if symptom in S1 and symptom not in self.symptoms:
    #             prob *= 1 - self.score(S1[symptom])
    #         elif symptom in S1 and symptom in self.symptoms:
    #             prob *= self.score(S1[symptom])
    #         else:
    #             prob *= self.score(S2[symptom])
    #     diseases = self._getDiseaseFromSymptoms(list(self.symptoms))
       
    #     prob *= 1 / len(diseases) + 1
    #     # prob /= (1 / 2) ** (len(symptoms) - 1)
    #     print('prob:', prob)
    #     return prob

    def score(self, depth):
        value, frac, n = (1, 1, 1)
        for i in range(depth):
            value += 1
            frac += (1 + self.alpha) ** n
            n += 1
        value /= frac
        return value

    def getSymptomsScore(self):
        s = 0
        for symptom in self.symptoms:
            try:
                statement = statement = 'match (p1:disease {name: "%s"}), (p2:symptom {name: "%s"}), p = shortestpath((p1)-[*..%d]-(p2)) return p, length(p) as len' %(self.disease, symptom, self.S2_depth)
                cursor = self.graph.run(statement)
                s += self.score(cursor.current['len']) if cursor.forward() else 0
            except Exception as e:
                print(e)
        return s

    
        
    def getS1(self):
        s = dict()
        try:
            statement = 'match (p1:disease {name: "%s"}), (p2:symptom), p = (p1)-[*..%d]-(p2) return p, length(p) as len' %(self.disease, self.S1_depth)
            cursor = self.graph.run(statement)
            while cursor.forward():
                s[cursor.current['p'].end_node['name']] = cursor.current['len']
        except  Exception as e:
            print(e)
            raise Exception('提取S1错误')
        return s

    def getS2(self):
        s = dict()
        try:
            statement = 'match (p1:disease {name: "%s"}), (p2:symptom), p = (p1)-[*..%d]-(p2) where length(p)>%d return p, length(p) as len' %(self.disease, self.S2_depth, self.S1_depth)
            
            cursor = self.graph.run(statement)
            while cursor.forward():
                # if cursor.current['len'] > self.S1_depth:
                s[cursor.current['p'].end_node['name']] = cursor.current['len']
        except  Exception as e:
            print(e)
            raise Exception('提取S2错误')
        return s

    def getSymptomSet(self):
        s = set()
        with open(SYMPTOM_DIC_PATH, 'r',encoding="utf-8") as f:
            for line in f.readlines():
                s.add(line.strip().split(' ')[0])
        return s

    def getSymptoms(self):
        self.symptoms = set(self.description.strip().split(self.sep))
        return self.symptoms


    def _calDiseaseScore(self, diseaseList, symptomList):
        scores = []
        
        # 首先计算每一种症状对应的疾病数目
        scoreSymptom = []
        for symptom in symptomList:
            scoreSymptom.append( len (self._getDiseaseFromSymptoms([symptom])) )
        
        # 接下来计算每种疾病的置信度
        for disease in diseaseList:
            score = 0
            for idx, symptom in enumerate(symptomList):
                if self._existHaveRelationship(disease, symptom):
                    score += 1.0 / scoreSymptom[idx]
            scores.append(score)
        return scores





    def _getSymptomsFromDisease(self, diseaseList):
        symptomSet = set()
        for disease in diseaseList:
            node = self.graph.nodes.match('disease', name = disease).first()
            if node is None:
                continue
            rels = self.graph.match( (node, ), r_type = 'd-s')
            for r in rels:
                symptomSet.add(r.end_node['name'])
        return symptomSet

    def _getDiseaseFromSymptoms(self, symptomList):
        diseaseSet = set()
        for symptom in symptomList:
            node = self.graph.nodes.match('symptom', name = symptom).first()
            if node is None:
                continue
            rels = self.graph.match( (None, node), r_type = 'd-s')
            for r in rels:
                diseaseSet.add(r.start_node['name'])
        return diseaseSet

    
            
        

def diagnose(description, disease):
    # print(description)
    diagnoser  = Diagnoser(description, disease)
    return diagnoser.diagnose()
    

if __name__ == "__main__":
    diagnose(sys.argv[1], '新冠')