#! python3
from os import listdir 
from os.path import isfile, join
import docx
import sys
import re
from bs4 import BeautifulSoup

# retrieve file names and stores it into a list
files = [f for f in listdir(".") if (isfile(join( ".", f)) and f != "parser.py")]
print(files)

listOfWords = []

def getListOfWords(fileName):
    tempListOfWords = []
    file = open(fileName, "r")
    text = file.readlines()
    tempListOfWords.extend(text)
    
    for word in tempListOfWords:
        listOfWords.append(word.strip())
    
    print(listOfWords)

# Able to retrieve text from the Word Documents only
def getTextFromDocFiles(fileName):
    doc = docx.Document(fileName)
    fullText = []
    changedText = []
    for paragraph in doc.paragraphs:
        fullText.append(paragraph.text)
    for line in fullText: 
        line.strip()
        if line == '' or line.strip() == '':
            continue
        changedText.append(line.strip())

    HTMLParser(changedText)

    return '\n'.join(fullText)

# HTML Validator
# Should return the line number, line if false
def HTMLParser(text):
    for line in text:
        if (line == '' or line == '\n'):
            continue
        if (bool (BeautifulSoup(line, "html.parser").find()) == False):
            print(bool (BeautifulSoup(line, "html.parser").find()))
            print(line)

#getTextFromDocFiles(files[3])
#getTextFromTextFiles(files[0])
x = str(sys.argv[1])
getListOfWords(x)