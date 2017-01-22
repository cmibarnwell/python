#Area of Circle program written by Caleb Barnwell
#Computer Science, 10-11-15

import math

def areaOfCircle(r):
    """Finds area of a circle with a given radius."""
    power=math.pow(r, 2)
    area=power*math.pi
    print(area)

rad=input("Please input value for radius: ")
rad_float=float(rad)
areaOfCircle(rad_float)
