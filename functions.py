# 1. Function to add two numbers

def add(a, b):
    return a + b

# 2. Function to find the factorial of a number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 3. Function to check if a number is prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 4. Function to reverse a string

def reverse_string(s):
    return s[::-1]

# 5. Function to find the maximum number in a list

def find_max(lst):
    if not lst:
        return None
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

print(add(3, 5))  # Output: 8
print(factorial(5))  # Output: 120
print(is_prime(7))  # Output: True
print(reverse_string("Muneeb"))  # Output: beenuM
print(find_max([3, 1, 7, 4, 9]))  # Output: 9