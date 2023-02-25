#Write a Python program to calculate the area of regular polygon.
import math

def apothem(l, n):
    return l / (2 * math.tan(math.pi / n))

def area(l, n, a):
    return (l * a * n) / 2

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side:"))
a = apothem(l, n)

print("The area of the polygon is:", int(area(l, n, a)))