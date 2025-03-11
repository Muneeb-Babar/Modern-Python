
# Tuple Logical Questions

# 1. Convert a Tuple of Strings to a Single Concatenated String

tup = ('Hello', 'World', 'Python')
result = ' '.join(tup)
print(result)
# Output: Hello World Python


# 2. Find the Tuple with the Maximum Sum of Elements

tup_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
max_sum = max(tup_list, key=sum)
print(max_sum)
# Output: (7, 8, 9)


# 3. Convert a Tuple of Tuples to a Dictionary

tup = (("a", 1), ("b", 2), ("c", 3))
result = dict(tup)
print(result)
# Output: {'a': 1, 'b': 2, 'c': 3}


# 4. Find the Intersection of Two Tuples
tup1 = (1, 2, 3, 4, 5)
tup2 = (3, 4, 5, 6, 7)
result = tuple(set(tup1) & set(tup2))
print(result)
# Output: (3, 4, 5)


# 5. Given a tuple of strings, find the length of each string and return it as a tuple.

tup = ("apple", "banana", "cherry")
result = tuple(len(x) for x in tup)
print(f"Length of each tuple index {result}")
# Output: (5, 6, 6)


# 6. Replace a Specific Element in a Tuple
# (Tuples are immutable, so to replace an element, we must create a new tuple.)

tup = (1, 2, 3, 4, 5)
new_tup = tup[:2] + (100,) + tup[3:]
print(new_tup)
# Output: (1, 2, 100, 4, 5)