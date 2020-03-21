class Mammal:
    def walk(self):
        print("Walking")

class Dog(Mammal):
    pass

class Cat(Mammal):
    pass

dogObj = Dog()
dogObj.walk()