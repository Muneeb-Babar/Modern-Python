# 1. **Even or Odd:**  
#    Write a Python program that takes an integer input from the user and prints whether it is even or odd.

getNum=int(input("Enter Your Number: "))

if getNum%2==0:
    print("Even Number: ")

else:
    print("Odd Number: ")

# 2. **Positive, Negative, or Zero:**  
#    Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.

getNum=int(input("Enter Your Number: "))

if getNum>0:
    print("Positive Number: ")

elif getNum<0:
    print("Negative Number: ")

else:
    print("Zero")

# 3. **Largest of Three Numbers:**  
#    Write a Python program that takes three numbers as input and prints the largest among them but not use the max function.

num1=float(input("Enter First Number"))
num2=float(input("Enter Second Number"))
num3=float(input("Enter Third Number"))

if num1>num2 and num1>num3:
    largest=num1

elif num2>num1 and num2>num3:
    largest=num2

else:
    largest=num3

print("Largest Number is: ",largest)

# 4. **Leap Year Checker:**  
#    Write a Python program that checks if a given year is a leap year or not. (A leap year is divisible by 4 but not divisible by 100 unless also divisible by 400.)

year=int(input("Enter Year: "))

if year%4==0 and (year%100!=0 or year%400==0):
    print("Leap Year: ",year)

else:
    print("Not a Leap Year: ",year)

# 5. **Vowel or Consonant:**  
#    Write a Python program that takes a single character as input and checks if it is a vowel or consonant.

getWord=input("Enter Your Word")

getChar=getWord[0]

if getChar.lower() in 'aeiou':
    print("Vowel: ",getChar)

else:
    print("Consonant: ",getChar)

# 6. **Eligibility to Vote:**  
#    Write a Python program that takes age as input and prints whether the person is eligible to vote (18 years or older).

age=int(input("Enter Your Age: "))

if age>=18:
    print("Eligible to Vote: ",age)

else:
    print("Not Eligible to Vote: ",age)

# 7. **Grading System:**  
#    Write a Python program that takes marks as input and assigns a grade based on the following conditions:  
#    - 90 and above: A  
#    - 80-89: B  
#    - 70-79: C  
#    - 60-69: D  
#    - Below 60: F 

getMarks=int(input("Enter Your Marks"))

if getMarks>=90 and getMarks<=100:
    print("Grade: A")

elif getMarks>=80 and getMarks<90:
    print("Grade: B")

elif getMarks>=70 and getMarks<80:
    print("Grade: C")

elif getMarks>=60 and getMarks<70:
    print("Grade: B")

elif getMarks>=0 and getMarks<60:
    print("You Are Fail")

else:
    print("Invalid Marks")

# 8. **Triangle Validity Check:**  
#    Write a Python program that takes three sides of a triangle as input and checks if they can form a valid triangle. (A triangle is valid if the sum of any two sides is greater than the third side.)

triNum1=int(input("Enter First Side: "))
triNum2=int(input("Enter Second Side: "))
triNum3=int(input("Enter Third Side: "))

if triNum1+triNum2>triNum3 and triNum2+triNum3>triNum1 and triNum1+triNum3>triNum2:
    print("Perimeter of Triangle: ",triNum1+triNum2+triNum3)
    
else:
    print("Invalid Triangle")

# 9. **Divisibility Test:**  
#    Write a Python program that takes a number as input and checks whether it is divisible by both 5 and 7.

num=int(input("Enter Number: "))

if num%5==0 and num%7==0:
    print("Number is Divisible by 5 and 7")

else:
    print("Number is Not Divisible by 5 and 7")

# 10. **Password Authentication:**  
# Write a Python program that prompts the user to enter a password.
# If the password matches the stored password (`"webdev"`), print `"Access Granted"`;
# otherwise, print `"Access Denied"

getPassword=input("Enter Your Password")
securepassword="webdev"

if getPassword==securepassword:
    print("Access Granted")

else:
    print("Access Denied")
