# *Decorators allow us to wrap another function in order to
# extend the behaviour of the wrapped function, without
# permanently modifying it

class Student:
    @staticmethod
    def greet():
        print(f"Hello, Student!!")

    def __init__(self, name, age):
        self.name = name
        self.age = age

# s1 = Student('Rohit', 27)
# s2 = Student('Ajay', 27)
# print(s1.name)
# print(s1.age)
# s1.greet()
# s2.greet()

# ------------------------------------
# Challenge: 
# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, acct_no, acct_bal=0):
        self.acct_no = acct_no
        self.acct_bal = acct_bal
    
    def credit(self, credit_amt):
        self.acct_bal += credit_amt
        print(f'{credit_amt} has been credited')
        self.show_bal()

    def debit(self, debit_amt):
        self.acct_bal -= debit_amt
        print(f'{debit_amt} has been debited')
        self.show_bal()

    def show_bal(self):
        print(f'Account Balance: {self.acct_bal}')
        
acc1 = Account(123, 100)
acc1.show_bal()
acc1.debit(10)
acc1.credit(100000000000000000)