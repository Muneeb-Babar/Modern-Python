# 1: Write a program that takes an integer N as input and prints all even numbers from 1 to N using a for loop.

number=int(input("Enter a number: "))
for i in range(1, number+1):
    if i % 2 == 0:
        print(i, end=" ")
# Output: Enter a number: 10
# 2 4 6 8 10


# 2: Write a program that calculates the factorial of a given number N using a for loop.

number=int(input("Enter a number: "))
factorial=1

for i in range(1, number+1):
    factorial *= i
    print("Factorial of", number, "is", factorial)


# 3: Write a Python program that takes a number as input and calculates the sum of its digits using a for loop.

number = input("Enter a number: ")  

sum_digits = 0  

for digit in number:
    sum_digits += int(digit)  

print("Sum of digits is:", sum_digits)


# 4: Write a program that takes a string as input and prints it in reverse order using a for loop.

string = input("Enter a string: ")
reverse_string = ""

for char in string:
    reverse_string += char
    print("Reverse of the string is:", reverse_string)


# 5: Write a program that takes a string as input and counts the number of vowels (a, e, i, o, u) using a for loop.

string = input("Enter a string: ")
vowels = "aeiou"
count = 0

for char in string:
    if char in vowels:
        count += 1
        print("Number of vowels is:", count)


# 6: Write a program that takes two numbers start and end as input and prints
# all prime numbers between them using a for loop.

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

prime_numbers = []
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_numbers.append(num)
            print("Prime numbers between", start, "and", end, "are:", prime_numbers)


# 7:Write a program that prints a right-angled triangle pattern using a for loop.
# Example (N = 5):


n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print("*" * i)
    print("")


