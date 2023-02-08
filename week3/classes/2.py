class Shape:
    def area(self):
        print(0)
    
class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        print(self.length ** 2)
    
length = int(input())
p1 = Shape()
p2 = Square(length)

p1.area()
p2.area()