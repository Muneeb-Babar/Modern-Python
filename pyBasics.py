print('Wellcome to Python')

# Variable Declearation

myName="Muneeb"
myAge=25
weight=55.5
is_present=True

print(myName)

# Check Type

print(type(myName))
print(type(myAge))
print(type(is_present))

mainNumber=24
addNumber=1

mainNumber +=addNumber #we can perform all operations like +,-,*,/
print(mainNumber)
# Output: 25


#Now understand the concept of typecate

24 + int("1") #This is typecate

# Math expressions: Unfamiliar operators

7%3 #remainder operator
2**3 #power

# Math expressions: Eliminating ambiguity (PEMDAS)
(1 + 3) * 4
(2 * 4) * 4 + 2

# Concatenating Text Strings Methods

first_name="Muneeb"
last_name="Babar"

first_name+" "+last_name # METHIOD-1

concat_name=f"{first_name} {last_name}" # METHOD-2

"{0} {1}".format(first_name, last_name)  # METHOD-3


print(concat_name)

# =========================================================


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





