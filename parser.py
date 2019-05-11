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

# Retrieve text from text files only
# Return list of words from 
def getListOfWords(fileName):
    tempListOfWords = []
    file = open(fileName, "r")
    text = file.readlines()
    tempListOfWords.extend(text)
    
    for word in tempListOfWords:
        listOfWords.append(word.strip().lower())
    
    print(listOfWords)

# Retrieve text from the Word Documents only
# Returns list, the filename [0] and the contents [1]
def getTextFromDocFiles(fileName):
    doc = docx.Document(fileName)
    fullText = []
    changedText = []
    results = []
    for paragraph in doc.paragraphs:
        fullText.append(paragraph.text)
    for line in fullText: 
        line.strip()
        if line == '' or line.strip() == '':
            continue
        changedText.append(line.strip().lower())
    
    results.append(fileName)
    results.append(changedText)

    #print(changedText)
    return results

# Still need to do text from text files only
def getTextFromTextFiles(fileName):
    txt = open(fileName, "r")
    changedText = []
    results = []
    lines = txt.readlines()
    for line in lines: 
        line.strip()
        if line == '' or line.strip() == '':
            continue
        changedText.append(line.strip().lower())
    
    results.append(fileName)
    results.append(changedText)

    #print(changedText)
    return results

# HTML Validator
# Should return the line number, line if false, need a counter to how many times it's false, if over 10 then don't output rest
def HTMLParser(text):
    for line in text:
        if (line == '' or line == '\n'):
            continue
        if (bool (BeautifulSoup(line, "html.parser").find()) == False):
            print(bool (BeautifulSoup(line, "html.parser").find()))
            print(line)

# Checks if the line contains the words
# Returns list, the filename [0] and the contents that contain the words [1]
def checkWords(text):
    results = []
    linesWithBadWords = []
    
    for line in text[1]:
        if any(word in line for word in listOfWords):
            linesWithBadWords.append(line)

    results.append(text[0])
    results.append(linesWithBadWords)

    return results

def main(): 
    # gets argument from the command line, pass in the text file
    getListOfWords(str(sys.argv[1]))

    for fN in files:
    # check for file name extensions, store in list and evaluate 
        if (fN == sys.argv[1]): continue
        if fN.endswith('.docx') or fN.endswith('.doc'):
            fileInfoDoc = getTextFromDocFiles(files[1])
            resultsDoc = checkWords(fileInfoDoc)
            print(resultsDoc)
        else:
            fileInfoTxt = getTextFromTextFiles(fN)
            resultsTxt = checkWords(fileInfoTxt)

    
    #createDoc for HTML problems 

    #createDoc for words
    
    

main()





