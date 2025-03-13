# Function Logical Questions

# 1: Write a function to find the missing number in a list of n unique numbers from 1 to n+1.


def find_missing_number(arr):
    n = len(arr)
    total = (n + 1) * (n + 2) / 2
    sum_of_arr = sum(arr)
    return total - sum_of_arr


# 2: Write a function to find the sum of all elements in a list using recursion.
def sum_of_elements(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_of_elements(lst[1:])
    


# 3: Write a function that checks whether a given number is prime or not.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.50) + 1):
        if n % i == 0:
            return False
    return True



# 4: Write a function that reverses a given string without using built-in functions like [::-1] or reversed().

def reverse_string(s):

    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string

    return reversed_string

print(reverse_string("Muneeb"))



# 5: Write a function that checks whether a given string is a palindrome or not.

def is_palindrome(s):

    reverse_string = ""
    for char in s:
        reverse_string = char + reverse_string
        return s == reverse_string
    print(is_palindrome("radar"))


# 6: Write a function to return the first non-repeating character in a given string. If all characters repeat, return None.

def first_non_repeating_char(s):
    
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in s:
        if char_count[char] == 1:
            return char

    return None

print(first_non_repeating_char("hello"))
print(first_non_repeating_char("hehllo world"))


# 7: Write a function that takes a number and keeps summing its digits until a single-digit number is obtained.

def sum_digits(n):
    
    while n > 9:
        n = sum(int(digit) for digit in str(n))

    return n

print(sum_digits(38)) # 2
print(sum_digits(9)) # 9