#!/opt/pyenv/shims/python3

def add_one(num):
    num = num + 1


n = 42
print(n)
add_one(n)  # integers are immutable so n remains unchanged
# n = add_one(n) would add one to n
print(n)