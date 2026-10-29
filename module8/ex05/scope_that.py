#!/opt/pyenv/shims/python3

def add_one(num):
    return num + 1  #1. Returns a new integer that is one greater than the input number.

n = 42         #Prints 42
print(n)
n = add_one(n)  # integers are immutable so n remains unchanged
# n = add_one(n) would add one to n
print(n)