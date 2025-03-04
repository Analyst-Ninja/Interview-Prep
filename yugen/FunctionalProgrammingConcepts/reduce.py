class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name} : {self.score}" 
    
students = [
    Student('Rohit', 100),
    Student('Ajay', 100),
    Student('Kartik', 100),
    Student('Bholu', 60),
]

sum = 0
for i in students:
    sum+=i.score 

print(sum/len(students))

from functools import reduce

total_score = reduce(lambda total, student : total + student.score ,students,0)

print(total_score/ len(students))

# ----------------------------------------------
# Challenge: use reduce to multiply all values

numbers = [1,2,3,4,5]

product_of_nums = reduce(lambda prod, number : prod * number, numbers,1)

print(product_of_nums)