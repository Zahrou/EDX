

import math

def polysum(n, s):
    """ Takes 2 arguments (number of sides 'n' and side length 's')
        Returns the sum of area and perimeter of the polygon
        rounded to 4 decimals """
    
    area = (0.25*n*(s^2))/math.tan(math.pi/n)
    perimeter = n*s
    area_perimeter = area + perimeter
    rounded_4 = round(area_perimeter, 4)
    return rounded_4

print(polysum(10, 7))
