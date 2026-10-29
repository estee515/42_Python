#!/opt/pyenv/shims/python3

numbers = [2,8,9,48,8,22,-12,2]

result = set()

for number in numbers:
	if number > 5:
		result.add(number + 2)

print(numbers)

print(result)
