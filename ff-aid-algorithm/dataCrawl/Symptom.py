import jieba
import py2neo


class Symptom(object):
    keys = ['name', 'description', 'reason', 
            'prevention', 'examination', 'diagnose', 'QA', 'relatedSymptoms']

    def __init__(self, data = None):
        self.data = dict()
        if data is not None:
            for key in Symptom.keys:
                self.data[key] = data[key] if data[key] is not None else ''
    
    def __iter__(self):
        return iter(self.data)

    def __setitem__(self, key, value):
        if key not in Symptom.keys:
            raise Exception(key + ' not in ' + str(Symptom.keys))
        self.data[key] = value

    def __getitem__(self, key):
        if key not in Symptom.keys:
            raise Exception(key + ' not in ' + str(Symptom.keys))
        return self.data[key]

    def __str__(self):
        return str(self.data)

    def insertDB(self):
        '''插入到neo4j数据库'''
        pass
