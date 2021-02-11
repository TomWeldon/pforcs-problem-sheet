# Weekly Task 4. Taking a positive integer and carrying out a required calculation
# in a loop until integer 1 is reached.
# Author: Tom Weldon G00398828


# Input request for a positive integer
num1 = int(input('Please enter a positive integer: '))

# Set Boolean condition for a positive integer
posInteger = num1 > 1

# If positive integer the original input number is printed and then a while loop is entered
# which loops as long as the output calculation within the loop is greater than 1
# Two conditions are set in the loop: 
# 1. A calculation for an even number (integer % 2 == 0), which is
#    the integer / 2
# 2. A calculation for an odd number (integer % 2 == 1), which is the (integer * 3) +1 
# For each iteration of the if or elif condition the output is printed

if posInteger:
    
    print(num1, end = ' ')
    while num1 > 1:

        if (num1 % 2 == 0):
            num1 = num1 / 2
            print(int(num1), end = ' ')
            
        elif(num1 % 2 ==1):
            num1 = (num1 * 3) + 1
            print(int(num1), end = ' ')

# If the boolean condition is False (No postive integer > 1) the else staement is invoked and the
# message 'No positive number entered. Program will exit!' along with program finish

else:
    print('No positive number entered. Program will exit!')