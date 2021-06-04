#!/bin/bash
for file in *.pdf; do pdftotext -layout -nopgbrk -eol unix "$file" "../DataConverted/${file%.*}.txt"; done
