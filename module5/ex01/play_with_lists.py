#!/opt/pyenv/shims/python3

numbers = [2,8,9,48,8,22,-12,2]

new_numbers = []

for number in numbers:
	new_numbers.append(number + 2)

print("Original list: ", numbers)
print("New list: ", new_numbers)
