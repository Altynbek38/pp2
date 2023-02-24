import math

def apothem(l, n):
    return l / (2 * math.tan(180 / n))

def area(l, n, a):
    return (l * n * a) / 2

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side:"))
a = apothem(l, n)

print("The area of the polygon is:", area(l, n, a))