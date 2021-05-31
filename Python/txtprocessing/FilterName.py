import os, glob, re

path = '../../Data/'
theStar = '*'
fileFormat = '.pdf'
for filename in glob.glob(path + theStar + fileFormat):
    realFileName = re.search(r'\\.*\.', filename).group(0)[1:]
    fiteredFileName = re.sub(r"[^a-zA-Z0-9-]", '', realFileName)
    os.rename(filename, path + fiteredFileName + fileFormat)
