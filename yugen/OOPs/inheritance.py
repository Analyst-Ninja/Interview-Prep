import random

class Animal:
    info = "A living orgainism that feeds on organic matter."

    def __init__(self, name):
        self.name = name
        print('An animal is created')

class Dog(Animal):
    info = "a domestic animal"

    def __init__(self, name):
        super().__init__(name)
        print('An dog is created')
        self.lucky_number = random.randint(0,10)
        self.fur = ""

    def bark(self):
        print(f"Woof!!, My name is {self.name} and my lucky number is {self.lucky_number}")

class Bulldog(Dog):
    info = "A dog of bull dog breed"

    def __init__(self, name):
        super().__init__(name)
        print('A bulldog is created')

dog1 = Bulldog('Fido')
# Child Class Variable overwrite the Parent Class Varibale
# print(dog1.info)

# ----------------------------------------------------
# Challenge: Add a subclass to your previous class

class Furniture:
    info = 'Decorative and utility item in home'

    def __init__(self, name, furnitureType):
        self.name = name
        self.furnitureType = furnitureType
        print('A firniture is created')

class Table(Furniture):
    info = "A furniture used for mostly studying"

    def __init__(self, name, height):
        self.height = height
        super().__init__(name,'Table')
        print('A table is craeted')

    def describe(self):
        print(f"Name - {self.name}\nHeight - {self.height}\nFurniture Type - {self.furnitureType}")

t1 = Table('LaptopTable', 1)

t1.describe()







