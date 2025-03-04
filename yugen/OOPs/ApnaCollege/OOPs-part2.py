# # 1. del 

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student('Rohit')
# # del s1 # delete the whole obj
# del s1.name # delete the obj's attribute
# print(s1)
# print(s1.name)

# 2. Private(like) attributes and methods

# Conceptual Implementations in Python:
# Private attributes & methods are meant to be used only within the class and are not
# accessible from outside the class.

# class Person:

#     __name = 'Anonymous'

#     def __hello(self):
#         print("Hello  Person!!")

#     def welcome(self):
#         self.__hello()

# p1 = Person()

# # print(p1.__hello())
# # print(p1.__name())
# p1.welcome()

# # 3. Inheritance
# # Type: 1. Single Inheritance 2. Multi Level Inheritance 3. Multiple Inheritance
# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print('Car Started!!')

#     @staticmethod
#     def stop():
#         print('Car Stopped!!')

# class Toyota(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()
    
# car1 = Toyota('Prius', 'Disel')

# print(car1.name,car1.type)

# Class method -> Use to modifiy the class attribute
# A class method is bound to the class & receives the class as an implicit first argument.
# Note - static method can't access or modify class state & generally for utility.

# class Person:
#     name = 'Anomymous'
    
#     # def change_name(self, name):
#     #     self.name = name
#     #     Person.name = name # 1st Way
#     #     self.__class__.name = name # 2st Way
#     @classmethod
#     def change_name(cls, name):
#         cls.name = name # 3rd Way

# p1 = Person() 
# p1.change_name('Rohit')
# print(p1.name)
# print(Person.name)

# -----------------------------------
# Challenge: Create a class to get the avg of the marks scored by a student

# class Student:
#     def __init__(self, phy, chem, maths):
#         self.phy = phy
#         self.chem = chem
#         self.maths = maths

#     @property
#     def percentage(self):
#         return str(round((self.phy + self.chem + self.maths) / 3,2)) + " %"
    
# s1 = Student(100,98,99)
# print(s1.percentage)

# s1.phy = 97
# print(s1.percentage)

# Polymorphism
# ----------------------------------------------------------
# Operator Overloading

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def __repr__(self):
#         return f"{self.real}i + {self.img}j"
    
#     def __add__(self, other):
#         newReal = self.real + other.real
#         newImg = self.img + other.img
#         return Complex(newReal, newImg)
    
#     def __sub__(self, other):
#         newReal = self.real - other.real
#         newImg = self.img - other.img
#         return Complex(newReal, newImg)
    
# num1 = Complex(3,4)
# print(num1)

# num2 = Complex(1,2)
# print(num2)

# num3 = num1 + num2
# print(num3)

# num4 = num1 - num2
# print(num4)

# ----------------------------------------------------
# Pratice Problems

# Qs. Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the
# circle.

# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return round(math.pi * self.radius * self.radius, 2)

#     def perimeter(self):
#         return round(2 * math.pi * self.radius, 2)
    
# c1 = Circle(8)

# print(c1.area())
# print(c1.perimeter())

# Problem 2:

# Qs. Define a Employee class with attributes role, department & salary &
# showDetaiIs( ) method.
# Create an Engineer class that inherits properties from Employee &
# attributes : name & age.

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        return {
            'role' : self.role,
            'dept' : self.dept,
            'salary' : self.salary,
        }
    
class Engineer(Employee):
    def __init__(self, name, age):
        super().__init__('Data Engineer', 'BIU', 53000)
        self.name = name
        self.age = age

    def showDetails(self):
        data = super().showDetails()
        data['name'] = self.name
        data['age'] = self.age
        return data
    
# emp1 = Employee('Data Engineer', 'BIU', 53000)
# print(emp1.showDetails())

eng1 = Engineer('Rohit', 27)
print(eng1.showDetails())