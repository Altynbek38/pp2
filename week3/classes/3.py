class Shape:
    def area(self):
        print(0)
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print(self.length * self.width)
    
length = int(input())
width = int(input())

p1 = Shape()
p2 = Rectangle(length, width)

p1.area()
p2.area()