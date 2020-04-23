import jieba
import py2neo
from py2neo import Graph, Node, Relationship

class Disease(object):
    keys = ['name','otherName', 'department','description','susceptiblePopulation' ,'reason', 
            'symptom', 'examination','treatment', 'complication', 
            'prevention', 'care', 'typicalSymptoms', 'relatedDiseases', 'QA','dietHealth']
    def __init__(self, data = None):
        self.data = dict()
        if data is not None:  
            for key in Disease.keys:
                self.data[key] = str(data[key]) if data[key] is not None else ''

    def __iter__(self):
        return iter(self.data)

    def __setitem__(self, key, value):
        if key not in Disease.keys:
            raise Exception(key + ' not in' + str(Disease.keys))
        self.data[key] = value
    
    def __getitem__(self, key):
        if key not in Disease.keys:
            raise Exception(key + ' not in' + str(Disease.keys))
        return self.data[key]
    
    def __str__(self):
        return str(self.data)
    
    def insertDB(self):
        '''插入到neo4j数据库中'''
        pass


def test():
    disease = Disease()
    disease['name'] = '心脏病'
    for pname in disease:
        print(pname, disease[pname])
    disease['1'] = 1 # 应该抛出异常

if __name__ == "__main__":
    test()
