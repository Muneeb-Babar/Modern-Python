# Dictionary Logic Questions

# 1: Write a Python program to merge two dictionaries.

dict1 = {"name": "Muneeb", "age": 25}
dict2 = {"city": "Karachi", "country": "Pakistan"}

dict1.update(dict2)
print(dict1)  # Output: {'name': 'Muneeb', 'age': 25, 'city': 'Karachi', 'country': 'Pakistan'}


# 2. Given a dictionary with numeric values, find the key with the highest value.

data = {'A': 10, 'B': 25, 'C': 15}

max_key = max(data, key=data.get)

print(f"Key with the highest value is : {max_key}")
# Output: Key with the highest value is : B

# 3. Count the Frequency of Elements in a List Using a Dictionary

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)
# Output: {1: 1, 2: 2, 3: 3, 4: 4}


# 4. Swap Keys and Values in a Dictionary (Reverse a Dictionary)

data = {'A': 1, 'B': 2, 'C': 3}
swapped_data = {}

for keys in data:
    value=data[keys] 
    swapped_data[value]=keys

print(swapped_data)
# Output: {1: 'A', 2: 'B', 3: 'C'}

# # Using dictionary comprehension
# reversed_data = {value: key for key, value in data.items()}
# print(reversed_data)
# # Output: {1: 'A', 2: 'B', 3: 'C'}


# 5. Remove a Key from a Dictionary

data = {'name': 'Muneeb', 'age': 25, 'city': 'Karachi'}
key_to_remove = 'age'

data.pop(key_to_remove)
print(data)
# Output: {'name': 'Muneeb', 'city': 'Karachi'}


# 6. Find Common Keys in Two Dictionaries

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 5, 'c': 10, 'd': 15}

# Using set intersection to find common keys
common_keys = dict1.keys() & dict2.keys()
print(common_keys)
# Output: {'b', 'c'}


# 7. Convert Two Lists into a Dictionary Given two lists, one of keys and one of values, create a dictionary.

keys = ['name', 'age', 'city']
values = ['Muneeb', 25, 'Karachi']

# data = dict(zip(keys, values))
# print(data)

data = {keys[i]: values[i] for i in range(len(keys))}
print(data)
# Output: {'name': 'Muneeb', 'age': 25, 'city': 'Karachi'}


# 8. Find the Sum of All Values in a Dictionary

data = {'A': 100, 'B': 200, 'C': 300}
total = sum(data.values())
print(total)
# Output: 600


# 9. Sort a Dictionary by Its Values Given a dictionary, sort it by its values in ascending order.

data = {'A': 100, 'B': 200, 'C': 50}
sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_data)
# Output: {'C': 50, 'A': 100, 'B': 200}



# 10. Count the Number of Words in a Sentence Using a Dictionary Given a sentence, count how many times each word appears.

sentence = "I am learning Python and Python is very easy to learn"
words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)







