# File IO in Python
# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files.

# File Handling
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "b" - Binary - Opens a file in binary format. This is useful for reading and writing binary data like images
# "t" - Text - Default value. Text mode

# ================================================================================================

import os

f=open('file.txt','r')
data=f.read()
print(data)
f.close()

# ================================================================================================

# f=open('file.txt','r')
# data=f.readline()
# print(data)
# f.close()

# ================================================================================================

f=open('file.txt','w') # w mode will overwrite the file and if file does not exist it will create a new file
f.write('Some data')
f.close()

# ================================================================================================

f=open('file.txt','a')
f.write('Some data')
f.close()

# ================================================================================================

# f=open('file.txt','x')
# f.write('Some data')
# f.close()

# ================================================================================================

# updated Method

with open('file.txt','r') as f: # with keyword will automatically close the file  use alias f for file
    data=f.read()
    print(data)

# ================================================================================================

os.remove('file.txt') # remove file
# ================================================================================================