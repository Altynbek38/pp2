#Write a Python program to calculate the area of a trapezoid.
def area_of_trapezoid(a, b, h):
    return (a + b) * h / 2

h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))

print("Expected Output:", area_of_trapezoid(a, b, h))