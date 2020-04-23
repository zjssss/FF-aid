# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DieaseItem(scrapy.Item):
    names = ['name','otherName', 'department','description', 'position','reason', 
            'symptom', 'examination','treatment', 'complication', 
            'prevention', 'care', 'typicalSymptom', 'relatedDisease']
    name = scrapy.Field()  # 疾病名称
    otherName = scrapy.Field() # 疾病别名
    department = scrapy.Field() # 科室
    description = scrapy.Field()  # 概述
    position = scrapy.Field() # 发病部位
    reason = scrapy.Field()  # 病因
    symptom = scrapy.Field()  # 症状
    examination = scrapy.Field()  # 检查
    treatment = scrapy.Field()  # 治疗方案
    complication = scrapy.Field()  # 并发症
    prevention = scrapy.Field()  # 预防
    care = scrapy.Field()  # 饮食保健
    typicalSymptom = scrapy.Field() # 典型症状
    relatedDisease = scrapy.Field() # 相关疾病

class MedicalItem(scrapy.Item):
    names = ['title', 'description', 'reason', 'symptom', 'examination',
                 'treatment', 'complication', 'prevention', 'care']
    title = scrapy.Field()  # 疾病名称
    description = scrapy.Field()  # 概述
    reason = scrapy.Field()  # 病因
    symptom = scrapy.Field()  # 症状
    examination = scrapy.Field()  # 检查
    treatment = scrapy.Field()  # 治疗方案
    complication = scrapy.Field()  # 并发症
    prevention = scrapy.Field()  # 预防
    care = scrapy.Field()  # 饮食保健
