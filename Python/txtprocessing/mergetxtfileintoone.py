import glob
import shutil

outfilename = 'MergedData.txt'
with open(outfilename, 'wb') as outfile:
    for filename in glob.glob('../../DataConverted/*.txt'):
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
