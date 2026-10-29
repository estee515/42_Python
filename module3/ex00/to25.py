#!/opt/pyenv/shims/python3

number = int(input("Enter a number less than 25 "))

if number >25:
	print("Error")
else:
	while number<=25:
		print(f"Inside the loop, my variable is {number}")
		number = number + 1 
