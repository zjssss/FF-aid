import os
import sys

from gensim.models import KeyedVectors

# os.chdir('dataCrawl/xywy')
sys.path.append('/Users/pengfei/Desktop')

from medical.dataCrawl.DBConc import DBConc
print(os.getcwd())
model = KeyedVectors.load_word2vec_format('/Users/pengfei/Desktop/medical/data/w2v/w2v.wv', binary = False)
conec = DBConc()
# conec.establishAllRelationship(correlation = None)

print(conec.getDSCorrelation(wvmodel = model))