import random
import string

def password_generator():
    length = 8
    password = ''
    ran_pass = string.ascii_letters + string.digits + string.punctuation

    for i in range(length):
        password += random.choice(ran_pass)
    return password
    
print(password_generator(), end='')

# Output: 8 characters password