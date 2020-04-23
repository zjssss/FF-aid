# config
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class Configurer(object):
    DISEASE_DICT_PATH = '/Users/pengfei/Desktop/medical/data/diseasesDic.txt'
    SYMPTOM_DICT_PATH = '/Users/pengfei/Desktop/medical/data/symptomsDic.txt'
    DISEASE_SENTENCE_DIR = '/Users/pengfei/Desktop/medical/data/disease'
    SYMPTOM_SENTENCE_DIR = '/Users/pengfei/Desktop/medical/data/symptom'
    DS_CORRELATION_PATH = '/Users/pengfei/Desktop/medical/data/correlation.txt'

    def __init__(self):
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)