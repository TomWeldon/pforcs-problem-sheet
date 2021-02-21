# Program to find the approximate sqaure root of a positive floting point number
# Author: Tom Weldon G00398828


# Declaring the input postive floating point number
sqRootNum = float(0)

# Creating the sqrt function with sqRootNum as the input argument
def sqrt(sqRootNum):
    # Request to input a positive number
    sqRootNum = float(input('Please enter a positive number : '))
    
    # Declaring numIter as a range from 0 to 100
    numIter = range(0,100)

    # Assigning input number sqRootNum to variable called number
    number = sqRootNum

    # for loop containing the formula to calculate the square root of a number. Iterates through the range numIter
    # The more iterations of the formula are worked through the more accurate the sqaure root calculation is
    # number == to the sqaure root calulation. Initial calculation has sqRootNum ==  number.
    # This changes as the iterations are worked through. sqRootNum remains constant
    for i in numIter:

        number = (number + (sqRootNum / number)) / 2
    # Return of the function is number(square root of input number) and sqRootNum (original inpput number)
    return number, sqRootNum

# Returns result in a tuple and  assigned to a variable called approx
# Square root calculation, number = approx[0], the first element of the tuple
# input sqRootNum = approx[1] the second element of the tuple 
approx = sqrt(sqRootNum)

# boolean statement for sqRootNum >= 0
positiveNum = approx[1] >= 0

# If input (sqRootNum) is positive the calculation is printed to one decimal place.
# If input number is negative the message 'You did not enter a positive number the program will close' is displayed
# and the program ends
if positiveNum:
    print('The sqaure root of {} is approx {:.1f}'.format(approx[1], approx[0]))
else:
    print('You did not enter a positive number the program will close')