# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import openpyxl
from py2neo import Graph, Node, Relationship
from .items import MedicalItem
from .items import DieaseItem
from .settings import NEO4J_URL
from .settings import NEO4J_USERNAME
from .settings import NEO4J_PASSWORD


class DiseasePipeline(object):

    def __init__(self):
        self.graph = Graph(NEO4J_URL, auth = (NEO4J_USERNAME, NEO4J_PASSWORD))
        self.graph.delete_all()
        # self.file = open('test.txt', "a+")
    def process_item(self, item, spider):
        # self.file.write(str(item) + '\n\n')
        # self.file.flush()

        item['name'] = item['name'].strip()

        node = self.graph.nodes.match('disease', name = item['name']).first()
        if node is None:    # 如果不存在这种疾病，那就创建它
            node = Node('disease', **item)
            self.graph.create(node)
            node = self.graph.nodes.match('disease', name = item['name']).first()
        else:               # 如果已经存在了这个疾病，那就更新它
            node.update(item)
            self.graph.merge(node, 'disease', 'name')

        # 建立相关疾病的联系
        relatedDiseases = item['relatedDisease']
        for disease in relatedDiseases:
            disease = disease.strip()
            newNode = self.graph.nodes.match('disease', name = disease).first()

            if newNode is None:    # 如果不存在这种疾病，那就创建它,从而能够建立联系
                newNode = Node('disease', name = disease)
                self.graph.create(newNode)
                newNode = self.graph.nodes.match('disease', name = disease).first()

            # 查询两种疾病之间是否存在相关联系，若不存在，则创建这个联系
            r = Relationship(node, "ralate", newNode)
            if self.graph.match_one((node, newNode), r_type = 'relate') is None:
                self.graph.create(r)
        
        # 建立疾病与症状之间的联系
        symptoms = item['typicalSymptom'].split('、')
        for symptom in symptoms:
            symptom = symptom.strip() # 消除多余的空格
            newNode = self.graph.nodes.match('symptom', name = symptom).first()
            
            if newNode is None: # 如果不存在这个症状，那就创建它
                newNode = Node('symptom', name = symptom)
                self.graph.create(newNode)
                newNode = self.graph.nodes.match('symptom', name = symptom).first()
                       
            # 查询两种疾病之间是否存在伴随联系，若不存在，则创建这个联系
            r = Relationship(node, 'have', newNode)
            if self.graph.match_one((node, newNode), r_type = 'have') is None:
                self.graph.create(r)


class MedicalPipeline(object):
    wb = openpyxl.Workbook()
    ws = wb.active
    names = MedicalItem.names
    def __init__(self):
        self.ws.append(self.names)
    
    def process_item(self, item, spider):
        row = []
        for name in self.names:
            row.append(item[name])
        self.ws.append(row)
        self.wb.save('./data/data.xlsx')
        return item
    def close_spider(self, spider):
        self.wb.save('./data/data.xlsx')