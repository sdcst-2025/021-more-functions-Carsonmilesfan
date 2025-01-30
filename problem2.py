#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""

def triangle(a,b,c):

    A = a ** 2
    B = b ** 2
    C = c ** 2
    
    if a >= b:
        if a >= c:
            d = a 
    if b > a:
        if b >= c:
            d = b 
    if c > a:
        if c > b:
            d = c

    if A + B + C - d ** 2 == d ** 2:
        sigmaboy = 2

    if A + B + C - d ** 2 > d ** 2:
        sigmaboy = 1

    if A + B + C - d ** 2 < d ** 2:
        sigmaboy = 3

    if a + b < d:
        sigmaboy = 0
            



    return sigmaboy

def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()
