# Hukumpedia
capstone project bangkit 2021
### Tool
* [webscrapper](https://webscraper.io/)
* [Internet Download Manager](https://www.internetdownloadmanager.com/)
* [Poppler](https://packages.ubuntu.com/source/focal/poppler)
* [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
* [pytesseract](https://pypi.org/project/pytesseract/)
* [imagemagick](https://imagemagick.org/script/download.php)
* [ghostscript](https://www.ghostscript.com/download/gsdnld.html)

### Step
1. Scrap all pdf file link in [JDIHN](https://jdihn.go.id/)
2. put the link to the internet donwload manager and download the files ant put it to one file
3. convert the pdf file to txt with shell [script](https://github.com/ahmadcah/Hukumpedia/blob/master/Data/autoconvertfiletopdf.sh) + poppler in WSL or linux computer inside pdf folder
4. run ocr script to fix 0kb file txt
5. to be continued
