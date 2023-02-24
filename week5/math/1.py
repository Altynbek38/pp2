import math

def degree_to_radian(degree):
    radian = (p / 180) * degree
    return radian

p = math.pi
degree = int(input("Input degree: "))

print("Output radian:", degree_to_radian(degree))