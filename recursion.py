# When a function call it self repeatly then it is called recursion.
# Recursion is a common mathematical and programming concept.
# It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
# The basic syntax of a recursive function is as follows:

def recursive_function():
    # some code
    recursive_function()
    # some code

'''The code must contain a condition to stop calling itself. Otherwise, the function calls itself infinitely.
Such function calls are called infinite recursion, and they eventually lead to a stack overflow error.
check stack block one by one then print the output'''


# Example of a recursive function

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    print(factorial(5))  # Output: 120
    # The base case is when n is equal to 1, at which point the function returns 1.

def show(n):
    if n == 0: # base case
        return
    print(n)
    show(n-1)

show(3)
# Output: 3 2 1 0
