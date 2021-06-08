import glob
import shutil

outfilename = 'MergedData.txt'
outKUHP = "kuhpMerged.txt"
kuhp = ['KUHPIDANA','kolonialkuhperdatafix','KUHDAGANG','KUHAP']
with open(outKUHP, 'wb') as o:
    for i in kuhp:
        with open("../../DataConverted/"+i+".txt", 'rb') as readfile:
            shutil.copyfileobj(readfile, o)

#with open(outfilename, 'wb') as outfile:
#   for filename in glob.glob('../../DataConverted/*.txt'):
#        with open(filename, 'rb') as readfile:
 #           shutil.copyfileobj(readfile, outfile)"""
