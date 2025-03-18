# oop Logical Questions

# Basic Example. Write a Python class to reverse a string word by word.

class Reverse:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

r = Reverse()
print(r.reverse_words('hello world'))


# Qs 1. Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the
# circle.

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1=Circle(21)
print(c1.area())
print(c1.perimeter())


# Qs 2. Define a Employee class with attributes role, department & salary. This class also a
# showDetails( ) method.
# Create an Engineer class that inherits properties from Employee & has additional
# attributes: name & age.

class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetails(self):
        print(f'Role: {self.role}\nDepartment: {self.department}\nSalary: {self.salary}')

class Engineer(Employee):
    def __init__(self, name,age):
        super().__init__('Engineer','IT',50000)
        self.name=name
        self.age=age


# e1=Employee('Manager','HR',50000)
# e1.showDetails()

e2=Engineer('Muneeb',25)
e2.showDetails()


# Qs 3. Create a class called Order which stores item & its price.
# Use Dunder function _gt_() to convey that:
# order1 > order2 if price of order › price of order2

class Order:
    def __init__(self, item, price):
        self.item=item
        self.price=price

    def __gt__(self, other):
        return self.price > other.price
    
o1=Order('Laptop',50000)
o2=Order('Mobile',20000)
print(o1>o2) # True