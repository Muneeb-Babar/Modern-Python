# List
# list and their mehtods

cities=['karachi','Lahore','Islamabad']
print(cities)

# cities[0] 
# cities[1]="Something" #update or get value in the list

#Methods of List

# 1.append() : Add an element to the end of the list
cities.append("Quetta")
print(cities)

# 2.insert() : Insert an element at a specified position in the list
cities.insert(1,"Multan")
print(cities)

# 3.remove() : Remove the first occurrence of the element in the list
cities.remove("Multan")
print(cities)

# 4.pop() : Remove the element at the specified position in the list
cities.pop(1)
print(cities)

# 5.index() : Return the index of the first occurrence of the element in the list
print(cities.index("karachi"))

# 6.count() : Return the number of occurrences of the element in the list
print(cities.count("karachi"))

# 7.sort() : Sort the list in ascending order
cities.sort()

# ==================================================

# Tuple
# tuple and their methods

# A tuple is an ordered, immutable (unchangeable) collection in Python.
# It allows duplicate values and is commonly used to store related pieces of information together.

# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)

# Accessing elements
print(my_tuple[0])  # Output: 10
print(my_tuple[-1]) # Output: 50 (Last element)

# Slicing a tuple
print(my_tuple[1:4]) # Output: (20, 30, 40)

# Tuple with mixed data types
mixed_tuple = (1, "Hello", 3.14, True)

# Nested Tuple
nested_tuple = (1, 2, (3, 4, 5))

# Tuple unpacking
a, b, c = (100, 200, 300)
print(a, b, c)  # Output: 100 200 300

# Tuple methods
# 1.count() : Return the number of occurrences of the element in the tuple
print(mixed_tuple.count(1))
print(mixed_tuple.count("Hello"))
# 2.index() : Return the index of the first occurrence of the element in the tuple
print(mixed_tuple.index(1))
print(mixed_tuple.index("Hello"))
# 3.len() : Return the number of elements in the tuple
print(len(mixed_tuple))

my_tuple = (10, 20, 30, 40, 20, 50)

print(my_tuple.count(2))  # Output: 30
print(my_tuple.index(20))  # Output: 1 
print(len(my_tuple))  # Output: 6
print(sum(my_tuple)) 

my_list = [1, 2, 3, 4]
new_tuple = tuple(my_list)
print(new_tuple)  # Output: (1, 2, 3, )


# Immutability of Tuples

my_tuple = (1, 2, 3)
my_tuple[0] = 100  # This will raise an error because tuples are immutable

# TypeError: 'tuple' object does not support item assignment

# =====================================================================

# Dictionary
# dictionary and their methods

# A dictionary is an unordered collection of key-value pairs in Python.
# It allows duplicate keys but not duplicate values.
# Each key must be unique and immutable, while values can be of any data type.

student = {
    "name": "Muneeb",
    "age": 25,
    "skills": ["Python", "JavaScript","React"]
}

# Getting all keys
print(student.keys())  # Output: dict_keys(['name', 'age', 'skills'])

# Getting all values
print(student.values())  # Output: dict_values(['Muneeb', 25, ['Python', 'JavaScript']])

# Getting all key-value pairs
print(student.items())  
# Output: dict_items([('name', 'Muneeb'), ('age', 25), ('skills', ['Python', 'JavaScript'])])

# Updating dictionary
student.update({"city": "Karachi"})
print(student)  
# Output: {'name': 'Muneeb', 'age': 25, 'skills': ['Python', 'JavaScript'], 'city': 'Karachi'}

# Removing an element
student.pop("age")
print(student)  
# Output: {'name': 'Muneeb', 'skills': ['Python', 'JavaScript','React'], 'city': 'Karachi'}

# Copying dictionary
copy_dict = student.copy()
print(copy_dict)  # Output: Same as student dictionary


# =====================================================================

# Set
# set and their methods

# A set is an unordered collection of unique elements in Python.
# It does not allow duplicate values and is commonly used to remove duplicates from a list.

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements to a set
my_set.add(6)

# Removing elements from a set
my_set.remove(2)

# Checking if an element is in a set
print(3 in my_set)  # Output: True

# =====================================================================



