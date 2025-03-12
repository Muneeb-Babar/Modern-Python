# Example 1: while loop

count = 0
while count < 5:
    print("Count is:", count)
    count += 1


# Example 2: while loop

number = 10
while number > 0:
    print("Number is:", number)
    number -= 2


# Example 3: while loop

getNumber=int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{getNumber} * {i} = ", i*getNumber)
    i += 1
else:
    print("Loop is completed")

# Example 4: while loop

getNumber=int(input("Enter a number: "))
i = 10
while i >= 1:
    print(f"{getNumber} * {i} = ", i*getNumber)
    i -= 1
else:
    print("Loop is completed")

# Example 5: while loop with break and continue

count = 0
while count < 10:
    if count == 5:
        print("Breaking the loop at count:", count)
        break
    if count % 2 == 0:
        count += 1
        continue
    print("Count is:", count)
    count += 1


# ============================================================


# Example 1: for loop

for i in range(5):
    print("i is:", i)

# Example 2: for loop
# The range() function generates a sequence of numbers starting from 0 up to, but not including, the specified number.
# The step size is 1 by default, but it can be changed to any positive integer.
'''(start, end, step)'''

for i in range(10, 20, 2): 
    print("i is:", i)

# Example 2: for loop

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit is:", fruit)

# Example 3: for loop

for i in range(1, 11):
    print(f"{getNumber} * {i} = ", i*getNumber)
else:
    print("Loop is completed")

# Example 4: for loop

for i in range(10, 0, -1):
    print(f"{getNumber} * {i} = ", i*getNumber)
else:
    print("Loop is completed")


# Example 5: for loop with break and continue

for i in range(10):
    if i == 7:
        print("Breaking the loop at i:", i)
        break
    if i % 2 == 0:
        continue
    print("i is:", i)