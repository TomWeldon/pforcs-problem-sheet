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