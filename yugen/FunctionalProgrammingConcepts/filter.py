class Student:
    def __init__(self, name , score):
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

res = list(filter(lambda x: x.score >= 70, students))

print(res)

# --------------------------------------------
# Challenge: Filter only the even numbers

numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x %2 ==0, numbers))

print(even_numbers)