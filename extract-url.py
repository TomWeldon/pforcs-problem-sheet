# Program to extract URLs from a log file as a list. File to search is inputted from the command line.
# Author: Tom Weldon G00398828

# Import 're' and 'sys' python modules
import re, sys

# "regex" =  include all charaters except new line (/n) in a group(.*) between the 'Lookbehind assertion' on "T" from POST and GET 
# and Look ahead assertion on "HTTP" in a line in the input file
regex ="(?<=T)(.*)(?=HTTP)"

# Take a sample of a full accesss.log as an input file from the command line and assign it to variable 'filename'
filename = sys.argv[1]

# Declare a list named 'resultURL'
resultURL = []

# Using 'filename' as 'inputfile. Start a 'for loop' with each line in the input file 'filename' seached with re.findall() in the 
# regular expression 'regex'
# Assign each line's search result to variable 'foundTextList'.
with open(filename) as inputFile:
    for line in inputFile:
        foundTextList = re.findall(regex, line)
        
# Start an 'if statement' with the condition if the number of lines in 'foundTestList' is not equal to 0 each element is assigned to
# a variable called 'foundText'. Each line is then appeded to the list 'resultURL' as an element with any spaces at the beginning or end
# stripped out. 
        if (len(foundTextList)!= 0):
            
            foundText = foundTextList[0]
            resultURL.append(foundText.strip())
# Print out the complete list 'resultURL'          
print(resultURL) 

# To view each element of the list vertically. Take away the comments in the code below.

#for i in resultURL:
    #print(i)