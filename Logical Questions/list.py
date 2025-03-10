# List Logical Questions

# 1: Given a list of numbers, write a Python program to find the second-largest number.

num_list = [10, 20, 4, 45, 99]
num_list.sort(reverse=True)  
second_largest = num_list[1]  

print(second_largest) 

# 2:Write a Python program to remove duplicate elements from a list.

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_number=set(numbers)
print(list(unique_number))

# 3: Write a Python program to find the most occurring element in a list.

numbers = [1, 3, 2, 1, 4, 1, 3, 2, 1]

# Create an empty dictionary to store the count of each number
frequency_dict = {}

# occurrence of each number

for num in numbers:

    if num in frequency_dict:
        frequency_dict[num] += 1
    else:
        frequency_dict[num] = 1

# Find the number with the highest frequency

most_frequent = max(frequency_dict, key=frequency_dict.get)
print(f"most_frequent number is : {most_frequent}")

# 4: Write a program to reverse a list without using reverse() or [::-1]

numbers = [1, 2, 3, 4, 5]

reverse_list=[]

for i in range(len(numbers)-1,-1,-1):
    reverse_list.append(numbers[i])

print(reverse_list)

# 5:Given a list of n-1 numbers in a sequence from 1 to n, find the missing number.

numbers=[1, 2, 4, 5, 6] 
n=6

expected_sum=n*(n+1)//2
actual_sum=sum(numbers)

missing_number=expected_sum - actual_sum

print(f"Missing Number is : {missing_number}")


# 6: Given a list, rotate it to the right by k positions. k=2

numbers = [1, 2, 3, 4, 5]
k = 2

k=k % len(numbers) # Ensure k is within the range of list length

# rotate the list to the right by k positions
rotated_list = numbers[-k:] + numbers[:-k]

print(rotated_list)


# 7: Write a Python function to check if a list is a palindrome (same forward and backward).

numbers = [1, 2, 3, 2, 1]

is_palindrome = numbers == numbers[::-1] #check reverse method
print(is_palindrome)  # Output: True


# 8: Given two sorted lists, merge them into a single sorted list.

list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged_list = sorted(list1 + list2)
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]


# 9:Given a list with different data types (integers, floats, and strings), separate them into different lists.

# Input: [1, "hello", 2.5, 3, "world", 4.8]  
# Output:  
# Integers: [1, 3]  
# Floats: [2.5, 4.8]  
# Strings: ["hello", "world"]

mixed_list = [1, "hello", 2.5, 3, "world", 4.8]
integers = []
floats = []
strings = []

for x in mixed_list:
    if isinstance(x, int):
        integers.append(x)

    elif isinstance(x, float):
        floats.append(x)

    elif isinstance(x, str):
        strings.append(x)

print("Integers:", integers)  # Output: [1, 3]
print("Floats:", floats)  # Output: [2.5, 4.8]
print("Strings:", strings)  # Output: ['hello', 'world']


# 10: Given a nested list (a list of lists), write a Python function to flatten it into a single list.

nested = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat_list = []

for sublist in nested:
    for item in sublist:
        flat_list.append(item)

print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
