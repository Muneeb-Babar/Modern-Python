# Conditional Statement

# Example 01
# Ask user for their age and then print out a message based on their age

getAge=int(input("Enter Your Age"))

if getAge>=18:
    print("You are Eligible For CNIC")

else:
    print("You are Not Eligible For CNIC")

# Example 02
# Ask user for their Marks and then print out a message based on their Percentage

marks=int(input("Enter Your Marks"))

if marks>=80 and marks<=100:
    print("You are A+ Grade Student")

elif marks>=60 and marks<80:
    print("You are B Grade Student")

elif marks>=45 and marks<60:
    print("You are C Grade Student")

elif marks>=30 and marks<45:
    print("You are D Grade Student")

elif marks>=0 and marks<25:
    print("You are Fail")

else:
    print("Invalid Marks")

# ==============================

'''Nested Conditional Statement
Ask user for their age and gender then print out a message based on their age and gender
'''
age=int(input("Enter Your Age"))
gender=input("Enter Your Gender")

if gender.title() == "Female":
    print("You are Eligible Work in Urban Areas")

elif gender.title() == "Male":
    if age>=40 and age<=60:
        print("You are Eligible Work in Anywhere")

elif gender.title() == "Male":
    if age>=20 and age<40:
        print("You are Eligible Work in Urban Areas")

else:
    print("Invalid Gender Or Age")

# ================================================
