# Class Methods and Static Methods

# Regular methods automatically pass instance as the first argument
# Class methods automatically pass class as the first argument
# Static methods do not pass anything by default
# Static methods are like regular functions but they have a logical connection
# with the class and that's why they are included

class Employee:
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay
    @classmethod # This is a decorator
    # 'cls' stands for class
    def set_raise_amt(cls, amt):
        cls.raise_amt = amt
    @staticmethod
    def print_message():
        print("Note that Saturdays and Sundays are off!")

# Automatically takes 'cls' argument similar to 'self'
Employee.set_raise_amt(1.05)

# Instances
emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Yum', 'Kim', 50000)

print(emp_1.raise_amt)
print(emp_2.raise_amt)

Employee.print_message()