
# Encapsulation in Python

# Encapsulation is the process wrapping data and functions into a single unit of an object.
# Encapsulation in Python is achieved by using private methods and attributes.
# Private methods and attributes are prefixed with a double underscore.

class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year

    def getBrand(self):
        return self.__brand
    
    def getModel(self):
        return self.__model
    
    def getYear(self):
        return self.__year
    
    def setBrand(self, brand):
        self.__brand = brand

car1 = Car("Toyota", "Corolla", 2019)
print(car1.getBrand())
print(car1.getModel())
print(car1.getYear())
# The above code will print the brand, model, and year of the car object.

car1.setBrand("Honda")
print(car1.getBrand())
# The above code will change the brand of the car object.


class Account:
    def __init__(self,balance,account_number):
        self.__balance=balance
        self.__account_number=account_number
        

    def debit(self,amount):
        self.__balance -= amount
        print(f"RS: {amount} Amount debited successfully")
        print(f"Total balance is: {self.__balance}")

    def credit(self,amount):
        self.__balance += amount
        print(f"RS: {amount} Amount credited successfully")
        print(f"Total balance is: {self.__balance}")

    def getBalance(self):
        return self.__balance
    

account1=Account(1000, 123456)
account1.debit(500)
account1.credit(1000)
        
        