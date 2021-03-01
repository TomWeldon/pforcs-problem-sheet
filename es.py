# Program for inputting  a text file in the command line and output the number of 'e's in the file
# The program was written on the assumption that number of 'e's is to include both lower and uppercase characters.
# Author: Tom Weldon G00398828

# Import sys module into program
import sys

# Assigning the input argument(input text file) in the command line to 'filename'
filename = sys.argv[1]

# Create the function 'readfile()' to read in the input file('filename') and return data (the contents of the 'filename')
def readFile():
        with open(filename, 'r') as f:
            data = f.read()
    
            return data

# Call the function readFile() and assign to var named 'char'
char = readFile()

# Initialise count at 0
count = 0
# For loop to iterate through all the characters in char. Nested 'if' statement to increment 'count' by 1 if lowercase 'e'
# is found in 'char'. 'elif' statement to increment 'count' by 1 if uppercase 'E' is found
for i in char:
    if i == 'e':
    
    
        count += 1
    elif i == 'E':

        count += 1


# Print the output of the number of 'e's found in the input file. Includes both lowercse 'e's and uppercase 'E's   
print('There are {} occurences of letter \"e\"  in the file {}' .format(count, filename))