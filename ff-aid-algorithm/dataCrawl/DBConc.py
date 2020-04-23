
from py2neo import Graph, Node, Relationship,Subgraph
from py2neo import walk
from medical.config import Configurer

from .Disease import Disease
from .Symptom import Symptom

import logging
import math
# import Disease
# import Symptom

class DBConc(object):
    def __init__(self):
        self.graph = Graph("http://liublack.cn:7474",auth=("neo4j","200001"))


    def search_one(self, label, name):
        node = self.graph.nodes.match(label, name = name).first()
        if label == 'disease':
            return Disease(Node)
        elif label == 'symptom':
            return Symptom(node)
        return None
    
    def search(self, label, **keys):
        pass

    def exist(self, label, name):
        node = self.graph.nodes.match(label, name = name).first()
        return node is not None

    def insertDisease(self, disease):
        if self.exist('disease', disease['name']):
            return
        if type(disease) != Disease:
            raise Exception('type(disease) not equals Disease')
        diseaseNode = Node('disease', **disease.data)
        self.graph.create(diseaseNode)

    def insertSymptom(self, symptom):
        if self.exist('symptom', symptom['name']):
            return
        if type(symptom) != Symptom:
            raise Exception('type(symptom) not equals Symptom')
        symptomNode = Node('symptom', **symptom.data)
        self.graph.create(symptomNode)

    def deleteRelationships(self, rtype):
        try:
            subG = Subgraph(relationships = self.graph.relationships.match(r_type = rtype))
            # self.graph.create(subG)
            self.graph.separate(subG)
        except ValueError as e:
            print(e)
        

    def establishRelationship(self, left, right, rtype, pname, correlation = None):
        self.deleteRelationships(rtype)
        nodes = self.graph.nodes.match(left)
        for lnode in nodes:
            print(type(lnode))
            names = lnode[pname]
            for name in names:
                rnode = self.graph.nodes.match(right, name = name).first()
                if rnode is None:
                    continue
                if self.graph.match_one((lnode, rnode), r_type = rtype) is None:
                    if correlation is not None: # 计算相关性
                        try:
                            value = correlation.similarity(lnode['name'], rnode['name'])
                            value = (value + 1) / 2
                        except KeyError as e:
                            print(e)
                            value = 1
                    else: 
                        value = 1
                    r = Relationship(lnode, rtype, rnode, value = value)
                    self.graph.create(r)
    def establishAllRelationship(self, correlation = None):
        self.establishRelationship('disease', 'disease', 'd-d','relatedDiseases', correlation = correlation)
        self.establishRelationship('disease', 'symptom', 'd-s', 'typicalSymptoms', correlation = correlation)
        self.establishRelationship('symptom', 'symptom', 's-s', 'relatedSymptoms', correlation = correlation)

    def getDSCorrelation(self, label = 'correlate', alpha = 0.3, maxDepth = 5, wvmodel = None):
        symptomSet = set()
        diseaseSet = set()
        result = {}
        with open(Configurer.SYMPTOM_DICT_PATH, 'r') as f:
            for line in f.readlines():
                symptomSet.add(line.split(' ')[0])
        logging.info('症状集加载完毕')
        with open(Configurer.DISEASE_DICT_PATH, 'r') as f:
            for line in f.readlines():
                diseaseSet.add(line.split(' ')[0])
        logging.info('疾病集合加载完毕')
        f = open(Configurer.DS_CORRELATION_PATH, 'w')
        
        for disease in diseaseSet:
            result[disease] = {}
            for symptom in symptomSet:
                result[disease][symptom] = ''
                try:
                    statement = 'match (p1:disease {name: "%s"}), (p2:symptom {name:"%s"}), p = shortestpath((p1)-[*..%d]-(p2)) return p' %(disease, symptom, maxDepth)
                    cursor = self.graph.run(statement)
                    path = cursor.current['p'] if cursor.forward() else None
                except  Exception as e:
                    path = None
        
                if path:
                    value, frac, n = (0, 0, 0)
                    for entity in walk(path):
                        if isinstance(entity, Relationship):
                            value += entity['value']
                            frac += (1 + alpha) ** n
                            n += 1
                    value /= frac
                    result[disease][symptom] = (value, 'shortest path')
                elif wvmodel:
                    try:
                        value = wvmodel.similarity(disease, symptom)
                        value = (value + 1) / 4
                        result[disease][symptom] = (value, 'w2vModel')
                    except KeyError as e:
                        logging.warning(str(e))
                if result[disease][symptom] == '':
                    value = 0.1
                    result[disease][symptom] = (0.1, 'cannot compute')

                logging.info('%s - %s - %s by %s\n' %(disease, result[disease][symptom][0], symptom, result[disease][symptom][1]))
            f.write(str(result[disease]) + '\n')
            f.flush()
        # f = open(Configurer.DS_CORRELATION_PATH, 'w')
        f.write('\n\n\n\n' + str(result))
        return result
                
                    



    def clearDB(self):
        self.graph.delete_all()



    def getSymptomsFromDisease(self, diseaseList):
        symptomSet = set()
        for disease in diseaseList:
            node = self.graph.nodes.match('disease', name = disease).first()
            rels = self.graph.match( (node, ), r_type = 'have')
            for r in rels:
                symptomSet.add(r.end_node['name'])
        return symptomSet

    def getDiseaseFromSymptoms(self, symptomList):
        diseaseSet = set()
        for symptom in symptomList:
            node = self.graph.nodes.match('symptom', name = symptom).first()
            rels = self.graph.match( (None, node), r_type = 'have')
            for r in rels:
                diseaseSet.add(r.start_node['name'])
        return diseaseSet
    
    def existHaveRelationship(self, disease, symptom):
        ndisease = self.graph.nodes.match('disease', name = disease).first()
        nsymptom = self.graph.nodes.match('symptom', name = symptom).first()
        if ndisease is None or nsymptom is None:
            return False
        rel = self.graph.match_one((ndisease, nsymptom), r_type = 'have')
        return rel is not None
    
    def getDiseaseDetails(self, diseaseList):
        details = []
        for disease in diseaseList:
            node = self.graph.nodes.match('disease', name = disease).first()
            diseaseItem = dict()
            for pname in self.diseaseItemProerties:
                diseaseItem[pname] = node[pname]
            details.append(diseaseItem)
        return details
    
    def getRelatedSymptoms(self, symptomList):
        symptoms = set()
        for symptom in symptomList:
            node = self.graph.nodes.match('symptom', name = symptom).first()
            rels = self.graph.match((node, None) ,r_type = 'relate')
            relatedSymptoms = [rel.end_node['name'] for rel in rels ]
            symptoms.update(relatedSymptoms)
        return list(symptoms)

    


            
            




