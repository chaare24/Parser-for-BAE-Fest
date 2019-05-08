#! python3

import docx
import sys

x = str(sys.argv[1])

def getText(fileName):
    doc = docx.Document(fileName)
    fullText = []
    for paragraph in doc.paragraphs:
        fullText.append(paragraph.text)

    return '\n'.join(fullText)

print(getText(x))