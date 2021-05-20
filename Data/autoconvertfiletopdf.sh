#!/bin/bash
for file in *.pdf; do pdftotext -layout -nopgbrk "$file" "../DataConverted/${file%.*}.txt"; done
