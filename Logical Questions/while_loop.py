# While Loop Logical Questions


# 1:Print any table using while loop

getNumber=int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{getNumber} * {i} = ", i*getNumber)
    i += 1
else:
    print("Loop is completed")


# 2:Print Numbers from 1 to N using while loop

n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i)
    i += 1


# 3:Write a program that takes a number as input and calculates the sum of its digits using a while loop.

number = int(input("Enter a number: "))
sum=0
while number > 0:
    sum += number % 10
    number //= 10
print("Sum of digits is:", sum)


# 4:Write a program to check if a given number is prime using a while loop.

number=int(input("Enter a number: "))
i=2
while i<number:
    if number%i==0:
        print("Not Prime")
        break
    i+=1
else:
    print("Prime")


# 5:Write a program to print the Fibonacci series up to n terms using a while loop.

n = int(input("Enter a number: "))
a, b = 0, 1
count = 0
while count < n:
    print(a)
    a, b = b, a+b
    count += 1


# 6:Write a program that checks whether a number is a palindrome 
# (reads the same forward and backward) using a while loop.

number = int(input("Enter a palindrome number: "))
orignal = number
reverse = 0

while number > 0:
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number //= 10
    print("Original number is:", orignal)
    print("Reverse number is:", reverse)

if orignal == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# 7:Write a program to find the factorial of a number using a while loop.

number = int(input("Enter a number: "))
factorial = 1
i = 1
while i <=number:
    factorial *= i
    i += 1
print("Factorial is:", factorial)