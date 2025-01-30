#!python3

"""
Create a function that determines the length of a hypotenuse given the lengths of 2
shorter sides
2 input parameters
float: the length of one side of a right triangle
float: the length of the other side of a right triangle

return: float value for the length of the hypotenuse rounded to 2 decimals
        None if the hypotenuse does not exist

Sample assertions:
assert hypotenuse(6,8) == 10
(2 points)
"""

import math
def hypotenuse(a,b):
    if a >= 0:
        if b >= 0:
            A = float(a)
            B = float(b)
            c = A ** 2 + B ** 2
            C = math.sqrt(c)
            C = round(C, 2)
        else:
            C = None
    else:
        C = None
    
    return C

assert hypotenuse(6,8) == 10
assert hypotenuse(5,12) == 13
assert hypotenuse(4,6) == 7.21
assert hypotenuse(-3,4) == None