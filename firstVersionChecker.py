# Charles Arellano
# Keyword Checker for BAE2019
# Returns Line Number, Email Address
# Where the keyword is found

import csv

# define variables
check = True

# Attempts to open file
done = False
while not done:
    var = input("Enter file name: ")
    try:
        inFile = open(var)
        done = True
    except:
        print("File is not found")
        

# Function for switch statement
def label(index):
    switcher = {
        3: "Found in Prompt: ",
        9: "Found in Like to be included: "
        }
    return switcher.get(index)

# Skips the first line
inFile.readline()

# Set to 2 to follow Google Sheet convention
counter = 2


# Uses file given
with inFile as tsvFile:
    # sets the delimiter
    reader = csv.reader(tsvFile, delimiter='\t')

    userInputString = input("Enter a keyword: ")

    # reads in each line
    for row in reader:

        # indexes the length of the list
        for index in range(len(row)):

            # Checks for user input words
            if(row[index].lower().find(userInputString.lower() +' ') != -1 or (
                row[index].lower().find(' ' + userInputString.lower() +' ') != -1) or(
                    row[index].lower().find(' ' + userInputString.lower()) != -1)):
                if (index == 3 or index == 9):
                    print("Line number: " + str(counter))
                    print("Email Address:" + row[1] + (
                         "\n"+label(index) + row[index]) + '\n')
        counter += 1

# Remove from list
# Look into changing font
# output to file
# Change input to while loop

## Added a feature to allow user to input the desired string
## Fixed so that the end cases would be chcked
