# Task week 8: Write a program to plot f(x)=x, g(x)=x**2 and h(x)=x**3 for x in range 1-4
# Author: Tom Weldon

# import python modules numpy and matplotlip.pyplot
import numpy as np
import matplotlib.pyplot as plt

# Assign the x points a range of 0-4 using np.arange with a start point of 0 a stop point of 4 and steps of 0.1
# This gives a smoother curve to display the range 0-4
xpoints = np.arange(0,4,0.1)

# Assign the values for f(x)=x, g(x)=x**2 and h(x)=x**3
fpoints = xpoints
gpoints = xpoints**2
hpoints = xpoints**3

# Create two font dictionaries for plot 'Title' and x and y 'Labels'
font1 = {'family':'arial','color':'#0033cc','size':20}
font2 = {'family':'arial','color':'#008080','size':10}

# Assign a colour to the plot background
ax = plt.axes()
ax.set_facecolor("#ff9966")

# Plot f(x)=x, colour red for plot line and a label for the plot line legend. 
plt.plot(xpoints,fpoints, color ='r', label = 'f(x) = x')
plt.legend()

# Plot g(x)=x**2, colour blue for plot line and a label for the plot line legend.
plt.plot(xpoints,gpoints, color = 'b', label = 'g(x) = x**2')
plt.legend()

# Plot h(x)=x**3, colour green for plot line and a label for the plot line legend.
plt.plot(xpoints,hpoints, color = 'g', label = 'h(x) = x**3')

# Assign a colour to the legend background
plt.legend(facecolor='#b3ffff')

# Assign a title to the plot graph with 'font1'
plt.title('Function Plot of f,g,h', fontdict = font1)

# Assign a label to the x axis with a font type of 'font2'
plt.xlabel('X Values range 1-4', fontdict = font2)

# Assign a label to the y axis with a font type of 'font2'
plt.ylabel('Functions of X Values for f,g,h', fontdict = font2)

# Export a figure of the plot as 'Plot.png'
plt.savefig('Plot.png')

# Show the plot onscreen
plt.show()
