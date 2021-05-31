from PIL import Image as Pimage
from wand.image import Image as Wimage
import sys
from io import BytesIO
import pyocr.builders
import glob
import os
import re

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % lang)


def _convert_pdf2jpg(in_file_path: str, resolution: int = 300) -> Pimage:
    with Wimage(filename=in_file_path, resolution=resolution).convert("jpg") as all_pages:
        for page in all_pages.sequence:
            with Wimage(page) as single_page_image:
                yield Pimage.open(BytesIO(bytearray(single_page_image.make_blob(format="jpeg"))))


for filename in glob.glob('../../DataConverted/*.txt'):
    if os.path.getsize(filename) == 0:
        PDF_file = '../../Data/{0}pdf'.format(re.search(r'\\.*\.', filename).group(0)[1:])
        f = open(filename, 'a', encoding='utf-8')
        for img in _convert_pdf2jpg(PDF_file):
            txt = tool.image_to_string(img, lang=lang, builder=pyocr.builders.TextBuilder())
            f.write(txt)
        f.close()
