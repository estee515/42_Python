#!/opt/pyenv/shims/python3

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

result = first_number * second_number

print(f"{first_number} X {second_number} = {result}")

if result < 0:
	print("The result is negative.")

elif result > 0:
	print("The result is positive.")

else:
	print("The result is positive and negative.")



