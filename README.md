# Hukumpedia
<p align="center">
  <a href="https://github.com/ahmadcah/Hukumpedia">
    <img src="Logo Hukumpedia/IMG_4828.PNG" alt="Logo" width="300" height="300">
  </a>
  <h3 align="center">Bangkit Capstone Project 2021</h3>
</p>

### Tool
* [webscrapper](https://webscraper.io/)
* [Internet Download Manager](https://www.internetdownloadmanager.com/)
* [Poppler](https://packages.ubuntu.com/source/focal/poppler)
* [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
* [pytesseract](https://pypi.org/project/pytesseract/)
* [imagemagick](https://imagemagick.org/script/download.php)
* [ghostscript](https://www.ghostscript.com/download/gsdnld.html)

### Step from machine learning
1. Scrap all pdf file link in [JDIHN](https://jdihn.go.id/)
2. put the link to the internet donwload manager and download the files ant put it to one file
3. convert the pdf file to txt with shell [script](https://github.com/ahmadcah/Hukumpedia/blob/master/Data/autoconvertfiletopdf.sh) + poppler in WSL or linux computer inside pdf folder
4. run ocr script to fix 0kb file txt
5. Merge the File using this [script](https://github.com/ahmadcah/Hukumpedia/blob/master/Python/txtprocessing/mergetxtfileintoone.py)
6. train model with [this](https://github.com/ahmadcah/Hukumpedia/tree/master/Google_Colab)(transfer file from colab to could storage script inside).
7. make vm instance at gcp with 4 cpu and 16 GB ram specification.
8. deploy the model with flask and follow this [step](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04) for more clear instruction (still work at june 2021).
9. now model can be accesed by ip external.
