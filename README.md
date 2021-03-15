# pforcs-problem-sheet


=======

## Week 02 Task: bmi.py
### Calculating BMI:

Steps to calculate BMI:

1. Print request to input weight in kg and height in cm
2. Assign bmi conversion to weight divided by height in meteres squared. Input height converted to m by dividing input height by 100
3. BMI output printed corrected to two decimal places.

### Sources:

How to format BMI result to two decimal places, {:.2f) was found at
https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python

## Week03 Task: bitcoin.py 
### Displaying Current Bitcoin Value

Steps to displaying current Bltcoin value:

1. Import the 'requests' library into the bitcoin.py file
2. Assign 'https://api.coindesk.com/v1/bpi/currentprice.json' to variable 'url'
3. Use a get request to import the url json file
4. Assign the returned json file to a dictionary variable named 'bitCoinDict'
5. To ascertain the current Bitcoin rate for USD, EUR and GPB the float_rate key value was accessed within the nested dictionaries
   'USD', 'EUR' and 'GPB', within the nested dictionary 'bpi', within the dictionary 'bitCoinDict
6. Each current bitcoin rate for USD, Euro and GBP printed on separate lines and aligned using \n \t and spaces.

### Sources:
How to access the 'float_rate' within the USD, EUR and GBP nested dictionaries was found at
https://www.programiz.com/python-programming/nested-dictionary

## Week04 Task: collatz.py
### Write a program that asks the user to input any positive integer and outputs the successive values based on a required calculation

Steps to carrying out required calculation

1. Print input request for a positive integer
2. Set the Boolean condition for the input int (num1 > 1)
3. If Boolean is True ie num1 > 1, the integer is printed and a while loop is entered.
   While num1 is > 1 an if statement if int is even and an elif statement if int is odd are invoked to carry out
   the required calclations. The integer output of the if and elif statements either odd or even are printed on each 
   iterations of the statements.
4. If Boolean is False ie num1 < 1 an else statement is invoked and the message 'No positive number entered. Program will exit!'
   is printed and progranm ended.

## Week05 Task: squareRoot.py
### Write a program which contains a function to calculate the sqaure root of a positive floating point number and prints the output

Steps to calculating and displaying the square root of a positive number

1. Declare the input positive number, 'sqRootNum'
2. Write the function named sqrt() with the input number 'sqRootNum' as the input arg.
   Assign a range from 0-100 to variable called 'numIter'
   Assign 'sqRootNum' to variable called 'number'. Initially the purpose of the assignment is to start 'number' with a value equal to 'sqRootNum'.
   'Number' will subsequently change while 'sqRootNum' remains constant.
   Start a for loop which will iterate to the value on 'numIter' range(0-100). Within the for loop insert the formula number = (number + (sqRootNum / number)) / 2.
   The resulting number at the end of the for loop will be the sqaure root of the input number (sqRootNum). On each iteration of the formula the resulting number
   is closer to the actual square root of the input number.
   On completion of the for loop the 'number'(actual square root) and input number (sqRootNum)are returned.
   These returns form a two element tuple
3. Assign the function sqrt() to a variable called 'approx'.
4. Declare a boolean statement which has a True condition, element two (approx[1]) of the resulting tuple from the sqrt() function assigned to 'approx' is >= 0.
5. If True, print the resulting message 'The sqaure root of (sqRootNum) is approx (number)'. The numbers are approx[1] and approx[0].
   The square root number is corrected to one decimal place.
6. If False(else), print message 'You did not enter a positive number the program will close'.

### Sources:
https://surajregmi.medium.com/how-to-calculate-the-square-root-of-a-number-newton-raphson-method-f8007714f64.

The website was used to identify the formula used to get  the square root of the input number.
x_i := (x_i + n / x_i) / 2

x_i = number (square root)
n = sqRootNum (input number)

## Week06 Task: es.py
### Write a program that input a text file from the command line and outputs the number of 'e's in the file
### Assumption is made that the output is to include upper and lowercase 'e's

Steps to calculating and print to screen the number of 'e's in a text file entered from the command line.

1. Import the Python Sys module
2. Assign the command line input argument (.txt file) to variable called filename
3. Create a function(readfile()) which reads in the .txt file (filename) and returns the the information in 'data'.
4. Call the function and assign it to a variable called 'char'
5. Initialise variable 'count' at 0.
6. Write a For Loop which iterates for each character in 'char'
7. Within the For Loop write an if and elif statement. If i == 'e' increment 'count' by 1.
   elif i == 'E' increment 'count' by 1. This captures the number of lower and uppercase 'e's 
8. Print out the 'count'(number) of 'e's in the input .txt file. Includes the number of both lower and uppercase 'e's.

### Sources:
https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python/7439162

This link was used as the source on how to read in a file from the command line. 

## Week07 Task: extract-url.py
### Write progrm to extract the URL to a list from each line of access.log file.
### The input file to search through is inputted from the command line

Steps to extracting te URL from each line of the given access.log file and adding to a list.

1. Import re and sys modules. re to use regular expressionas and sys to allow file input from the command line.
2. Creat the regular expression to search each line of the input file
3. Assign the input file argument (sys.argv[1]) to variable 'filename'
4. Declare a list named 'resultURL'
5. Using 'filename' as 'inputfile. Start a 'for loop' with each line in the input file 'filename' seached with re.findall() using the 
   regular expression 'regex'. Assign each line's search result to variable 'foundTextList'.
6. Start an 'if statement' with the condition if the number of lines in 'foundTestList' is not equal to 0 each element is assigned to
   a variable called 'foundText'. Each line is then appended to the list 'resultURL' as an element, with any spaces at the beginning or end
   removed. 
7. Resulting list is printed to screen using 'print(resultURL)'.

### Sources:
https://superuser.com/questions/576710/regex-to-return-string-between-2-specific-characters

This link was used as a source to aid creating the regular expression that will extract a section of a line between two characters or set of characters

(?<=period_1_)(.*)(?=.ssa)


## Week08 task: plottask.py
### Write a program that displays a plot of the functions f(x) = x, g(x)= x**2 and h(x)=X**3
### in the range [0,4] on the one set of axes.

Steps to plotting the functions f(x)=x, g(x)=x squared and h(x)=x cubed

1. Import modules numpy and matplotlib.pyplot
2. Assign the xpoints a range of 0-4 using np.arange()with a start point of 0 and a stop 
   point of 4 in steps of 0.1. This will dispaly a smother curve in the resulting plot.
3. Assign the values for f(x) = x, g(x) = x squared h(x)= x cubed.
   as fpoints, gpoints and hpoints
4. Create two font dictionaries 'font1' and 'font2' which will be used to display the title, the x axis label and
   the y axis label on the plot.
5. Assign the hex color '#ff9966' to the plot background.
6. Plot f(x)=x, colour red for plot line and a label for the plot line legend.
7. Plot g(x)=x**2, colour blue for plot line and a label for the plot line legend.
8. Plot h(x)=x**3, colour green for plot line and a label for the plot line legend.
9. Assign the hex colour  '#b3ffff' to the legend background.
10. Assign a title to the plot using font dictionary 'font1' and assign labels to
    x axis and y axis using font dictionary 'font2'
11. Export a figure of the plot as 'plot.png'
12. Display the plot using plt.show()


