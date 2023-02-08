#Delete Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print("Hello my name is " + self.name)
    
p1 = Person("John", 36)
del p1.age

print(p1.age)