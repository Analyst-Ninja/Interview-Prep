import pickle

class Todo:
    def __init__(self, todo, important, priority = 'Normal'):
        self.todo = todo
        self.important = important
        self.priority = priority
    
    def __repr__(self):
        return f'Todo: {self.todo}\n Important: {self.important} \n Priority: {self.priority}\n'
        
todos = [
    Todo('Walk the dog', True),
    Todo('Walk the cat', False),
    Todo('Go for a stroll', True, 'High'),
]

with open('file.txt','wb') as file:
    pickle.dump(todos, file)

with open('file.txt','rb') as file:
    new_todos = pickle.load(file)

print(new_todos)

