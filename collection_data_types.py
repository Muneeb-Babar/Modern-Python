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