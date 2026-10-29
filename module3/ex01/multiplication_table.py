#!/opt/pyenv/shims/python3

number = int(input("Enter a number "))

counter = 0

while counter <10:
	print(f"{counter} X {number} = {counter * number}")

	counter = counter + 1

