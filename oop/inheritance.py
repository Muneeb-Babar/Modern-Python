# Inheritance in Python
# Inheritance is the process by which one class acquires the properties of another class.
# It provides code reusability and readability.


# types of inheritance in Python are:

# 1. Single Inheritance (One class inherits from one class)
# 2. Multiple Inheritance (One class inherits from multiple classes)
# 3. Multilevel Inheritance   (One class inherits from another class, which in turn inherits from another class)


# 1. Single Inheritance

# Example-1
class Animal:
    def __init__(self):
        print("Animal Constructor")
        
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def __init__(self):
        print("Dog Constructor")

dog1=Dog()
dog1.eat() # Output: Animal is eating
# In the above example, the Dog class inherits the Animal class. The Dog class can access the eat() method of the Animal class.


# Example-2

class Car:
    @staticmethod
    def start_engine():
        print("Engine is started")
    
    @staticmethod
    def stop_engine():
        print("Engine is stopped")

class Toyota(Car):
    def __init__(self,name):
        self.name=name
        print(f"{self.name} is created")

c1=Toyota("Corolla")
c1.start_engine()
c1.stop_engine()

# =========================================================

# 2. Multilevel Inheritance

# Example-1

class Car:
    @staticmethod
    def start_engine():
        print("Engine is started")
    
    @staticmethod
    def stop_engine():
        print("Engine is stopped")

class Toyota(Car):
    def __init__(self,name):
        self.name=name
        print(f"{self.name} is created")
    
class Corolla(Toyota):
    def __init__(self,model):
        self.model=model
        print(f"{self.model} is created")

c1=Corolla("GLI")
c1.start_engine()
c1.stop_engine()

# =========================================================


# 3. Multiple Inheritance

# Example-1

class A:
    varA="I am from class A"

class B:
    varB="I am from class B"

class C(A,B):
    varC="I am from class C"

c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

# =========================================================

#  Super() Function in Inheritance
# The super() function is used to give access to methods and properties of a parent or sibling class.

# Example-1

class Car:
    def __init__(self,type):
        self.type=type
    
    def start_engine(self):
        print("Engine is started")

class Toyota(Car):
    def __init__(self,type,name):
        super().__init__(type)
        self.name=name
        print(f"{self.name} is created")

c1=Toyota("Petrol","Corolla")
print(c1.type)
c1.start_engine()

# =========================================================
        
        




