
# Abstraction in Python

# Abstraction is the process of hiding the real implementation of an application from the user and emphasizing only on usage of it.
# In python, abstraction is achieved by using abstract classes and interfaces.

class Car:
    def __init__(self):
        self.acc=False
        self.brake=False
        self.clutch=False

    def start(self):
        self.acc=True
        self.brake=False
        self.clutch=True
        print("Car is started")

car1=Car()
car1.start()

# Output: Car is started
# It hides the internal implementation and highlights only the functionality.