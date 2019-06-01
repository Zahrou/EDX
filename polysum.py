

import math

def polysum(n, s):
    """ Takes 2 arguments (number of sides 'n' and side length 's')
        Returns the sum of area and perimeter squared of the polygon
        rounded to 4 decimals
        """
    
    area = (0.25*n*(s*s))/(math.tan(math.pi/n))
    perimeter = n*s
    summation = area + perimeter**2
    rounded_4 = round(summation, 4)
    return rounded_4

print(polysum(32, 19))
