import glob
import re
import csv

#for filename in glob.glob('../../DataConverted/UUD1945 .txt'):
with open('../../DataConverted/UUD1945 .txt', 'rb') as f:
    data = ''.join([x.decode('utf8') for x in f.readlines()])
    splitBAB = re.split(r'\bBAB\b', data)
    for i in range(len(splitBAB)):
        if i > 0:
            bab = splitBAB[i].split()[0] + " " + splitBAB[i].split('\n')[1].strip()
            splitPasal = re.split(r'\bPasal\b', splitBAB[i])
            for j in range(len(splitPasal)):
                if j > 0:
                    pasal = splitPasal[j].split()[0]
                    pasal = re.sub(r'[^a-zA-Z0-9]','',pasal)
                    print('BAB '+bab+' Pasal '+ pasal)



