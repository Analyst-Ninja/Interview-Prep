import random

class Dog:
    info = "a domestic animal"

    def __init__(self, name):
        self.name = name
        self.lucky_number = random.randint(0,10)

    def bark(self):
        print(f"Woof!!, My name is {self.name} and my lucky number is {self.lucky_number}")

dog1 = Dog('Fido')
dog2 = Dog('Sarah')

dog1.bark()
dog2.bark()

# ------------------------------------
# Challenge -> Add one method that uses/ modifiy an instance variable

class Table:
    info = "A furniture used for mostly studying"

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def describe(self):
        print(f"Name - {self.name}\nHeight - {self.height}")

t1 = Table('LaptopTable', 1)
t2 = Table('DesktopTable', 3)

t1.describe()
t2.describe()

        