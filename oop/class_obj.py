# OOP in Python

# MAke a class (Basic Blueprint) and create an object of that class

class Student:
    name = "Muneeb" #Blueprint
    age = 25

s1=Student() #Object

print(s1.name)
print(s1.age) #Output: 25


# =========================================================


# Constructor in Python
# A constructor is a special method in Python classes. It is defined with the __init__ method with double underscores before and after init.
#  The __init__ method is called when the class is instantiated.
#  It accepts the self-keyword as a first argument which allows accessing the attributes or methods of the class.


class Student:
    college="FAST" #Class Attribute
    name = "Anomy" #Class Attribute

    def __init__(self,name,age): #Parameterized Constructor
        self.name=name         #Instance Attribute > class attribute
        self.age=age
        print("Adding a new student")

s1=Student("Muneeb",24)
print(s1.name)
print(s1.age)

print(Student.college)


# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.

# =========================================================



# Methods in Python
# Methods are functions defined inside the body of a class.
# They are used to define the behaviors of an object.

class Student:
    college = "FAST"  # Class Attribute

    def __init__(self, name, age, marks): 
        self.name = name  
        self.age = age
        self.marks = marks
        print("Adding a new student")

        # Method to display the student details
    def display(self):
        print(f"Name: {self.name} Age: {self.age}")

    def cal_avg(self):
        sum = 0
        for marks in self.marks:
            sum += marks
        print(sum/len(self.marks)) 


s1 = Student("Muneeb", 24 , [90, 80, 70])
s1.display()
s1.cal_avg()

# =========================================================


# Static Method in Python
# Static methods are methods that are bound to a class rather than its object.

class Student:
    college = "FAST"  # Class Attribute
    @staticmethod      # Decorator

    def welcome():  # self is not required
        print("Welcome to FAST")

Student.welcome()

# =========================================================


# private and public methods in Python
# Private methods are those methods that should not be accessed directly from outside the class.

class person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def display(self):
        print(f"Name: {self.name} Age: {self.__age}")

        def __private_method(self):
            print("This is a private method")


p1 = person("Muneeb", 24)
p1.display()
print(p1.__age) #This will give an error

# p1.__private_method() #This will give an error
# p1._person__private_method() #This will also give an error

# =========================================================

# Static Method in Python
# Static methods are methods that are bound to a class rather than its object.

class A:
    @staticmethod
    def display():
        print("This is a static method")

# A.display() #Output: This is a static method

# =========================================================

# Class Method in Python
# Class methods are bound to the class and not the object of the class.

class Person:
    age = 25

    @classmethod
    def changeAge(cls):
        cls.age = 30

# Person.changeAge()
print(Person.age) #Output: 30

# =========================================================


# Property Decorator in Python
# The property decorator is used to define properties in a class.(real time update the value)

class Student:
    def __init__(self, phy, eng,math):
        self.phy = phy
        self.eng = eng
        self.math = math

    # def avg(self):
    #     return (self.phy + self.eng + self.math)/3 #this approch is not good because it is not real time update the value
        
    @property
    def avg(self):
        return (self.phy + self.eng + self.math)/3 #this approch is good because it is real time update the value
    
s1 = Student(90, 80, 70)
print(s1.avg) #Output: 80.0

s1.phy = 80
print(s1.avg) #Output: 76.66666666666667