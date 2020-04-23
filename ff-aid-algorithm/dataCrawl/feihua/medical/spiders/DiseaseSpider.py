import scrapy
import sys
import requests
import re
from ..items import DieaseItem
from lxml import etree

class DiseaseSpider(scrapy.Spider):
    name = 'diseaseSpider'
    domain = 'https://dise.fh21.com.cn'
    start_urls = ['https://dise.fh21.com.cn/department/illnesses.html']

    custom_settings = {
        'ITEM_PIPELINES' : {
            'medical.pipelines.DiseasePipeline': 300,
        }
    }

    def parse(self, response):
        self.logger.info('开始爬虫: ' +  response.url)
        '''遍历科室'''
        links = response.xpath('//ul[@class="level2"]/li/a/@href').extract()
        self.logger.info('科室链接:', links)
        for link in links:
            yield scrapy.Request(self.domain + link, callback = self.parseDepartment)

    def parseDepartment(self, response):
        '''遍历一个科室的疾病'''
        department = response.xpath('//ol[@class="dise_list_title"]//span/text()').get()
        links = response.xpath('//div[@class="dise_list"]//a[@class="link08"]/@href').extract()
        self.logger.info('疾病链接:' + str(links))
        for link in links:
            yield scrapy.Request(link, callback = self.parseDisease, meta = {'department':department})

        # 递归展开下一页
        pageLinks = response.xpath('//div[@class="pageStyle"]/p/a/@href').extract()
        destinition = response.xpath('//div[@class="pageStyle"]/p/a/text()').extract()

        for i, link in enumerate(pageLinks):
            if destinition[i].strip() == '下一页':
                self.logger.info('科室包含疾病的下一页链接: ' + link)
                yield scrapy.Request(self.domain + link, self.parseDepartment)


    
    def parseDisease(self, response):
        ''' 获取详细的疾病信息 '''
        item = DieaseItem()
        item['department'] = response.meta['department']
        name = response.xpath('//ol[@class="dise01"]/p/text()').get()
        otherName = response.xpath('//ol[@class="dise01"]/p/span/text()').get()

        self.logger.info('疾病名称:' + name)
        self.logger.info('疾病别名:' +  str(otherName))

        item['name'] = name
        item['otherName'] = otherName

        # 使用request爬取相关文章
        links = response.xpath('//dd[@class="dise02b"]/p/a/@href').getall()
        names = ['description', 'reason', 'symptom', 'examination',
            'treatment', 'complication', 'prevention', 'care']
        self.logger.info('疾病相关文章链接:' + str(links))
        for i, link in enumerate(links):
            # print('links:...', link)
            newResponse = requests.get(self.domain + link)
            newResponse.encoding = 'utf-8'
            html = etree.HTML(newResponse.text)
            text = html.xpath('string(//ul[@class="detailc"])').title() # 获取文章内容
            # self.logger.info(names[i] + ': ' + newResponse.text)
            item[names[i]] = re.sub('\s+', '', text)

        # 解析发病部位、典型症状、相关疾病
        item['position'] = response.xpath('//div[@class="dise03"]//dd/text()').extract()[0]
        item['typicalSymptom'] = response.xpath('//div[@class="dise03"]//dd/text()').extract()[2]
        item['relatedDisease'] = response.xpath('//div[@class="dise04"]//a/text()').extract()
        return item


        



        
    

