
import requests
import sys
import os

from lxml import etree
from http import client

# client.HTTPConnection._http_vsn = 10
# client.HTTPConnection._http_vsn_str = 'HTTP/1.0'



os.chdir('dataCrawl/xywy')
sys.path.append('/Users/pengfei/Desktop')
# sys.path.append('/home/liublack')
# from ..Disease import Disease
# from ..Symptom import Symptom
# from ..Cuter import Cuter
from medical.dataCrawl.Disease import Disease
from medical.dataCrawl.Symptom import Symptom
from medical.dataCrawl.Cuter import Cuter
from medical.dataCrawl.DBConc import DBConc

ROOT_URL = 'http://jib.xywy.com/html/jizhenke.html'
JB_DOMAIN = 'http://jib.xywy.com'
ZZ_DOMAIN = 'http://zzk.xywy.com'
# DICTS = map(lambda x: os.getcwd() + x, ['./symptomsDic.txt', './diseasesDic.txt'])
DICTS = ['./symptomsDic.txt', './diseasesDic.txt']
DISEASE_MAXD = 5 # 设置疾病递归的最大深度
SYMPTOM_MAXD = 10 # 设置症状递归的最大深度

CUT = False
SAVE = True

cuter = Cuter(DICTS) if CUT else None
connec = DBConc()
# connec.clearDB()
print(os.getcwd())

diseaseSet = set()
symptomSet = set()

def load(file, s):
    if os.path.exists(file):
        f = open(file, 'r+')
        for line in f.readlines():
            s.add(line.strip())
    else:
        f = open(file, 'w')
    return f

fSymptom = load('symptoms.txt', symptomSet)
fDisease = load('diseases.txt', diseaseSet)


def processRootUrl(rootUrl):
    html = getHTML(rootUrl)

    # 得到所有的急诊科疾病的url
    urls = html.xpath('//ul[@class="ks-ill-list clearfix mt10"]//a/@href')

    print('急诊科疾病链接:', urls)

    for url in urls:
        # processDisease(JB_DOMAIN + url, d = 0, maxd = DISEASE_MAXD)
        try:
            print('root disease url:', url)
            processDisease(JB_DOMAIN + url, d = 0, maxd = DISEASE_MAXD)
        except Exception:
            print('[failed] disease parse failed, url:', url)
    print('finished')

def processDisease(url, d, maxd):
    if (d > maxd) :
        return

    print('disease 第', d, '层')
    html = getHTML(url)

    # 得到疾病名称
    diseaseName = html.xpath('//div[@class="jb-name fYaHei gre"]/text()')[0].strip()
    print('processing disease:', diseaseName)
    # 首先检查集合是否已经存在此疾病，若存在，则直接返回
    if diseaseName in diseaseSet:
        print(diseaseName, '已经处理过')
        return 
    diseaseSet.add(diseaseName)
    fDisease.write(diseaseName + '\n')
    fDisease.flush()

    parseDisease(html, cut = CUT, save = SAVE) # 记录下疾病的所有数据
    
    # 处理并发症
    uri = html.xpath('//div[@class="jib-navbar fl bor pr"]//a/@href')[2]
    print(diseaseName,'的并发症uri', uri)
    processRelatedDisease(JB_DOMAIN + uri, recursion = True, d = d + 1, maxd = maxd)

    # 处理症状cc
    uri = html.xpath('//div[@class="jib-navbar fl bor pr"]/div[2]//a/@href')[0]
    symptomUrlList = getHTML(JB_DOMAIN + uri).xpath('//span[@class="db f12 lh240 mb15 "]/a/@href') # 得到症状的所有链接
    print(diseaseName,'的症状url', symptomUrlList)
    for url in symptomUrlList:
        try:
            processSymptom(url, 0, SYMPTOM_MAXD)
        except Exception:
            print('[falied] symptom parse failed', url)

def processSymptom(url, d, maxd):
    '''处理疾病的伴随症状'''
    if (d > maxd):
        return
    print('symptom 第', d, '层')
    html = getHTML(url)
    symptomName = html.xpath('//div[@class="jb-name fYaHei gre"]/text()')[0]

    print('processing symptom:', symptomName)
    # 检查症状是否已经在症状集合中，若存在，直接返回
    if symptomName in symptomSet:
        return
    symptomSet.add(symptomName)
    fSymptom.write(symptomName + '\n')
    fSymptom.flush()

    parseSymptom(html, cut = CUT, save = SAVE)

    # 处理症状的伴随症状
    uris = html.xpath('//ul[@class="about-zzlist clearfix"]//a/@href')
    print('症状', symptomName, '的伴随症状uris:', uris)
    for uri in uris:
        try:
            processSymptom(ZZ_DOMAIN + uri, d + 1, maxd) # 递归下去以便记录下更多的症状
        except Exception:
            print('[failed] disease parse failed', ZZ_DOMAIN + uri)

# def processRelatedSymptoms(url, recursion = False):
#     '''处理症状的并发症状'''



def processRelatedDisease(url, recursion = False, d = None, maxd = None):
    '''处理并发症(并发的疾病)
    @deleted 注意这里不和症状一样递归下去是为了让数据库中的疾病大多数都是急诊科的疾病
    使用递归收集更多疾病
    '''
    html = getHTML(url)
    relatedDiseasesUrls = html.xpath('//a[@class="gre mr15"]/@href')
    relatedDiseasesNames = html.xpath('//a[@class="gre mr15"]/text()')
    relatedDiseasesNames = list(map(lambda x: x.strip(), relatedDiseasesNames))
    print('并发病URLs', relatedDiseasesUrls)
    # diseaseSet.update(relatedDiseases)
    if recursion:
        for url in relatedDiseasesUrls:
            # processDisease(url, d, maxd)
            try:
                processDisease(url, d, maxd)
            except Exception:
                print('[failes] disease parse failed', url)
    return relatedDiseasesNames

def getHTML(url):
    response = requests.get(url, stream = True) # stream有没有用不知道
    response.encoding = 'gb2312'
    response = response.text
    html = etree.HTML(response)
    return html

def parseDisease(html, cut = False, save = False):
    '''解析疾病并存储'''
    disease = Disease()

    # 获取疾病名称
    diseaseName = html.xpath('//div[@class="jb-name fYaHei gre"]/text()')[0].strip()
    disease['name'] = diseaseName

    # 获取疾病别名
    # pass

    # 获取易感人群
    susceptiblePopulation = html.xpath('//div[@class="fl jib-common-sense"]/p[1]/span[2]/text()')[0]
    disease['susceptiblePopulation'] = susceptiblePopulation.strip()

    # 获取疾病科室
    department = html.xpath('//p[@class="clearfix mt5"]/span[@class="fl treat-right"]/text()')[0]
    disease['department'] = department.strip()

    # 获取疾病并发症
    uri = html.xpath('//div[@class="jib-navbar fl bor pr"]//a/@href')[2]
    relatedDiseases = processRelatedDisease(JB_DOMAIN + uri, recursion = False)
    disease['relatedDiseases'] = relatedDiseases

    # 获取疾病典型症状
    uri = html.xpath('//div[@class="jib-navbar fl bor pr"]/div[2]//a/@href')[0]
    typicalSymptomUrlList = getHTML(JB_DOMAIN + uri).xpath('//span[@class="db f12 lh240 mb15 "]/a/text()') # 得到症状的所有链接
    disease['typicalSymptoms'] = list(map(lambda x: x.strip(), typicalSymptomUrlList))

    #============================接下来处理QA======================================
    QAUrl = html.xpath('//ul[@class="dep-nav f14 clearfix"]//a/@href')[2]
    qa = parseQA(JB_DOMAIN + QAUrl)
    disease['QA'] = qa

    #================================ 接下来处理疾病介绍页面=============================

    # 获取疾病介绍页面
    introductionUrl = html.xpath('//ul[@class="dep-nav f14 clearfix"]//a/@href')[1]
    html = getHTML(JB_DOMAIN + introductionUrl)

    # 获取疾病相关链接
    uris = html.xpath('//div[@class="jib-nav fl bor"]//a/@href')
    # names = html.xpath('//div[@class="jib-nav fl bor"]//a/text()')
    # names = ['简介', '病因', '预防', '并发症', '症状', '检查', '诊断鉴别', '治疗', '护理', '饮食保健']
    
    # 获取疾病简介
    html = getHTML(JB_DOMAIN + uris[0])
    description = html.xpath('//div[@class="jib-articl-con jib-lh-articl"]/p/text()')[0]
    disease['description'] = description

    # 剩下的东西
    names = ['reason', 'prevention', 'complication', 'symptom', 'examination', 'treatment', 'care', 'dietHealth']
    for i, name in enumerate(names):
        html = getHTML(JB_DOMAIN + uris[i + 1])
        content = html.xpath('string(//div[@class="jib-janj bor clearfix"]/div[2])')
        # if len(content) == 0:
        #     content = html.xpath('//div[@class=" jib-articl fr f14 jib-lh-articl"]')
        # if len(content) == 0:
        #     print(name, '没有解析成功')
        #     continue
        # content = content[0]
        # content = etree.tostring(content, encoding='gb2312', xml_declaration=False).decode('gb2312')
        disease[name] = content 
    
    print('disease:', disease)
    if cut:
        cuter.cutAndSave(disease)
    if save:
        connec.insertDisease(disease)

    return disease
    
    



def parseSymptom(html, cut = False, save = False):
    symptom = Symptom()

    # 获取症状名称
    symptomName = html.xpath('//div[@class="jb-name fYaHei gre"]/text()')[0]
    symptom['name'] = symptomName

    # 获取并发症状
    relatedSymptoms = html.xpath('//ul[@class="about-zzlist clearfix"]//a/text()')
    relatedSymptoms = list(map(lambda x: x.strip(), relatedSymptoms))
    symptom['relatedSymptoms'] = relatedSymptoms

    # 获取QA
    QAUrl = html.xpath('//ul[@class="dep-nav f14 clearfix"]//a/@href')[2]
    if not QAUrl.startswith('/'):
        QAUrl = '/' + QAUrl
    qas = parseQA(ZZ_DOMAIN + QAUrl)
    symptom['QA'] = qas

    # =================接下来处理症状详情==================================
    introductionUrl = html.xpath('//ul[@class="dep-nav f14 clearfix"]//a/@href')[1]
    if not introductionUrl.startswith('/'):
        introductionUrl = '/' + introductionUrl
    html = getHTML(ZZ_DOMAIN + introductionUrl)

    names = ['description', 'reason', 'prevention', 'examination', 'diagnose']
    urls = html.xpath('//ul[@class="zz-nav-list clearfix"]//a/@href')
    for i, name in enumerate(names):
        html = getHTML(ZZ_DOMAIN + urls[i])
        content = html.xpath('string(//div[@class="zz-articl fr f14"])')
        symptom[name] = content

    print('symptom:', symptom)

    if cut:
        cuter.cutAndSave(symptom)
    if save:
        connec.insertSymptom(symptom)
    return symptom

def parseQA(url):
    html = getHTML(url)
    qa = []
    qalinks = html.xpath('//div[@class="pb10 bor-dash"]/div[@class="user-ask clearfix mt10 "]//a/@href')
    for link in qalinks:
        if not link.startswith('http'):
            continue
        html = getHTML(link)
        title = html.xpath('string(//p[@class="fl dib fb"])')
        question = html.xpath('string(//div[@id="qdetailc"])')

        qa.append(title)
        qa.append(question)

        ansList = html.xpath('//div[@class="pt10 mb5 clearfix pr qsdetail"]/div/div[1]')
        for ans in ansList:
            ans = ans.xpath('string(.)')
            qa.append(ans)
            print('ans:', ans)
        # ans = list(map(lambda x: etree.tostring(x, encoding='gb2312', xml_declaration=False).decode('gb2312'), ans))
        
    return qa




def main():
    processRootUrl(ROOT_URL)

    # with open('symptoms.txt', 'w') as f:
    #     for symptom in symptomSet:
    #         f.write(symptom + '\n')
    # with open('diseases.txt', 'w') as f:
    #     for disease in diseaseSet:
    #         f.write(disease + '\n')
        

if __name__ == "__main__":
    main()    