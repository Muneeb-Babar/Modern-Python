# Polymorphism in Python
# Polymorphism is the ability to present the same interface for different data types.

# Polymorphism in Python is achieved by using method overloading and method overriding.

# Method Overloading in Python
# Method overloading is the ability to define multiple methods with the same name but different parameters.

# Method overloading is not supported in Python. Python does not support method overloading.
# However, you can achieve method overloading using default arguments.


# Example-1
class Student:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def display(self):
        if self.age is not None:
            print(f"Name: {self.name} Age: {self.age}")
        else:
            print(f"Name: {self.name}")

s1 = Student("Muneeb",20)
s1.display()

# Operator Overloading in Python
# Operator overloading is the ability to define the behavior of operators for user-defined data types.

print(10+20) # Output: 30
print("Hello"+"World") # Output: HelloWorld
print({1,2,3}+{4,5,6}) # Output: {1, 2, 3, 4, 5, 6}

# polymorphism says that the same operator or function can be used for different types.

# Dander Methods in Python
# Dander methods are special methods that start and end with double underscores.
# They are also called magic methods or special methods.

class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def show(self):
        print(f"{self.real}i+{self.imag}j")

    def __add__(self, num2):
        real = self.real + num2.real
        imag = self.imag + num2.imag
        return complex(real, imag)
    

c1 = complex(1, 2)
c2 = complex(3, 4)
c3 = c1 + c2
c3.show()
# Output: 4i+6j   

# =========================================================

