fwords = open('words.txt', 'w')
fvecs = open('vecs.txt', 'w')

import os
print(os.getcwd())
os.chdir('/Users/pengfei/Desktop/medical/model/w2v')
with open('w2v.wv', 'r') as f:
    for line in f.readlines():
        words = line.strip().split(' ')
        fwords.write(words[0] + '\n')
        fvecs.write('\t'.join(words[1:]) + '\n')
        # print(' '.join(words[1:]))
fwords.close()
fvecs.close()

# with open('w2v.wv', 'r') as f:
#     for line in f.readlines():
#         words = line.split(' ')
#         # print(words)
#         fwords.write(words[0] + '\n')
#         fvecs.write(' '.join(word[1: ] + '\n')