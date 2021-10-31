# Classes and Instances

class Employee:
    def __init__(self, first, last, pay):
        #Instance Variables - different for every instance
        self.first = first
        self.last = last
        self.pay = pay
    # Functions in a class are called methods
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# Setting instance variables
emp_1 = Employee('Zach', 'Smith', 50000)

print(f'Greetings {emp_1.fullname()}!')

# Both of the below lines do the same thing
# The first one automatically passes 'self' as an argument but in the latter we need to specify the instance
# to retrieve its data
emp_1.fullname()
Employee.fullname(emp_1)



# Output:
'''
Greetings Zach Smith!
'''