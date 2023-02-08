class Capital:
    def __init__(self):
        self.low = ""
    
    def getString(self):
        self.low = input()


    def printString(self):
        print(self.low.upper())
    
p1 = Capital()

p1.getString()

p1.printString()