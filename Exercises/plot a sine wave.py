import math
import pylab

y_values = []
x_values = []
number = 0.0

while number < math.pi * 4:
    y_values.append(math.sin(number))
    x_values.append(number)
    number += 0.05


pylab.plot(x_values,y_values, 'ro')
pylab.show()
