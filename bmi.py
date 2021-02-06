#Calculation of BMI
#Tom Weldon:

#request to input weight in kg and height in cm
weight = int(input('Please enter your weight in kilos:'))
height = int(input('Please enter your height in cm:'))

#Coversion of height from cm to m and calculation of BMI 
bmi = weight / ((height/100)**2)


#Confirmation of input of height in cm and weight in kg
#Output BMI to two decinal places
print('Your height is {}cm and your weight is {}kg'.format(height, weight))
print('Your BMI is {:.2f}'.format(bmi))