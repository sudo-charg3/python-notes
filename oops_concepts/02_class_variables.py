# Class Variables


class Employee:
    
    # Creating class variables is simple
    raise_amount = 1.04
    no_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # Note the use of class name instead of self
        Employee.no_of_employees += 1

    def apply_raise(self):
        # Note that using self.raise_amount would make it possible to make raise_amount
        # different for different instances.
        # However using Employee.raise_amount the value would be fixed for all instances 
        # since it is the raise_amount of the class, hence there would be no chance to change the val
        # for any instance
        self.pay = int(self.pay * self.raise_amount)

# self or class name both can be used to get this var 
# it doesnt matter because both refer to the same class variable which is constant
# and cannot be changed by any instance
print('*******************')
print(Employee.no_of_employees)

# Setting instance variables
emp_1 = Employee('Zach', 'Smith', 50000)
emp_2 = Employee('Mark', 'Torque', 50000)

print(emp_1.no_of_employees)
print('*******************')

# Changing Class Variables
# Verifying the concept described above:
emp_1.apply_raise()
print(emp_1.__dict__)
print(emp_1.pay)

emp_2.raise_amount = 1.05
emp_2.apply_raise()
print(emp_2.__dict__)
print(emp_2.pay)



# Output:
'''
*******************
0
2
*******************
{'first': 'Zach', 'last': 'Smith', 'pay': 52000}
52000
{'first': 'Mark', 'last': 'Torque', 'pay': 52500, 'raise_amount': 1.05}
52500
'''