#!/opt/pyenv/shims/python3

table = 0 

while table <= 10:
	print(f"Table of {table}:",end=" ")

	multiplier = 0

	while multiplier <=10: 
		print(table * multiplier,end=" ")
		multiplier = multiplier + 1

	print ()
	table = table + 1
