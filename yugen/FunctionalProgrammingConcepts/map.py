class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [
    Student('Rohit', 100),
    Student('Ajay', 100),
    Student('Kartik', 100),
    Student('Bholu', 60),
]

student_results = []
for i in students:
    # if i.score >= 70:
    #     student_results.append(f"{i.name} Passed")
    # else:
    #     student_results.append(f"{i.name} Failed")

# One Liner
    student_results.append(f"{i.name} Passed") if i.score >= 70 else student_results.append(f"{i.name} Failed")


print(student_results)

# With Lamda
map_results = list(map(lambda x: f"{x.name} Passed" if x.score >= 70 else f"{x.name} Failed", students))

print(map_results)

# ---------------------------------------------------
# Challenge: Use map multiply the each value by 2

numbers = [1,2,3,4,5]
map_res = list(map(lambda x: x*2, numbers))

print(map_res)