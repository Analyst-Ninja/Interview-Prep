import random

class Dog:
    # class variable
    info = "A domestic animal"

    def __init__(self, name):
        # self is a instance of this class
        self.name = name
        print('I am alive!!')
        # luck_number --> Instance Variable
        self.lucky_number = random.randint(1,10)

dog1 = Dog('Fido')
dog2 = Dog('Sheru')

# print(dog1.lucky_number, dog2.lucky_number)

# dog1.name = 'Fido'

print(dog1.name)

# AttributeError -> As name instance variable is not being created for the dog2
print(dog2.name)



# ------------------------------
# Challenge --> Make a class and assign a instance variable
class Table:
    info = "A furniture used for mostly studying"

    def __init__(self, name, height):
        self.name = name
        self.height = height

t1 = Table('LaptopTable', 1)
t2 = Table('DesktopTable', 3)

print(t1.name, t1.height)
print(t2.name, t2.height)
