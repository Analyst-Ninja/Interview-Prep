import sys
import os

args = sys.argv

class Todo:
    def __init__(self, fileName):
        self.fileName = fileName
        self.read_todos()
        # self.show_todo()

    def read_todos(self):
        try:
            with open(self.fileName, 'r') as file:
                self.todos = file.readlines()
        except:
            self.todos = []
            self.write_todos()
        return self.todos
    
    def write_todos(self):
        with open(self.fileName, 'w') as file:
            file.writelines(self.todos)
        return 0
    
    def edit_todo(self, index, todo):
        self.todos[index-1] = todo
        self.write_todos()
        return 0
    
    def add_todo(self, todo_to_add):
        self.todos.append(todo_to_add + '\n')
        self.write_todos()
        return 0
    
    def remove_todo(self, index):
        self.todos.pop(index-1) 
        self.write_todos()
        return 0

    def __repr__(self):
        self.todos = self.read_todos()
        if len(self.todos) == 0:
            print('You have no todo \n**********************\n')
        else:
            print('Here is your Todos \n**********************\n')
            for i, v in enumerate(self.todos):
                print(f"{i+1}. {v}",end='')
            print()

        print(f'To view Todos\n{os.path.basename(__file__)}\n')
        print(f'To add a todo\n{os.path.basename(__file__)} add todo_to_add\n')
        print(f'To edit a todo\n{os.path.basename(__file__)} edit todo# new_todo\n')
        print(f'To remove a todo\n{os.path.basename(__file__)} remove todo#\n')
        
        return 0
    
    def show_todo(self):
        self.__repr__()


app = Todo('file.txt')

if len(args) == 1:
    app.show_todo()
elif len(args) == 3:
    if args[1] == 'add':
        app.add_todo(args[2])
    elif args[1] == 'remove':
        try:
            app.remove_todo(int(args[2]))
        except Exception as e:
            print(e)
            sys.exit(1)
    else:
        print('Option not allowed')
        app.show_todo()
elif len(args) == 4:
    if args[1] == 'edit':
        try:
            app.edit_todo(int(args[2]),args[3])
        except Exception as e:
            print(e)
            sys.exit(1)
    else:
        print('Option not allowed')
else:
    print('Incorrect Number of arguments passed (required - 0,2,3)')
    app.show_todo()





