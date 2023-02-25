#Write a Python program to convert degree to radian.
import math

def degree_to_radian(degree):
    return (pi / 180) * degree

pi = math.pi

degree = int(input("Input degree: "))

print("Output radian:", f'{degree_to_radian(degree):.6f}')