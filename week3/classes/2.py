class Shape:
    def __init__(self, length):
        self.length = length
    
    def area1(self):
        print(0)
    
class Square(Shape):
    def area2(self):
        print(self.length ** 2)
    
length = int(input())

p2 = Square(length)

p2.area1()
p2.area2()