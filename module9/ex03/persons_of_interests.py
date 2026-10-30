#!/opt/pyenv/shims/python3

def famous_births(names: dict[str, dict[str, str]]) -> None:
    # 1. Use a list comprehension and dict.get() to safely extract valid records
    valid_scientists = [
        info for info in names.values() 
        if isinstance(info, dict) and "date_of_birth" in info and "name" in info
    ]
    
    if not valid_scientists:
        print("No valid scientist data found.")
        return

    # 2. Sort directly by 'date_of_birth' using a lambda function key
    valid_scientists.sort(key=lambda x: x["date_of_birth"])

    # 3. Clean string interpolation loop
    for scientist in valid_scientists:
        print(f"{scientist['name']} is a great scientist born in {scientist['date_of_birth']}.")


# Fixed input data (changed {"name"} to a proper dictionary)
women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecilia Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"},
    "bibou": {"name": "Bibou Doe", "date_of_birth": "2100"},
    "who": {"name": "Unknown Scientist"},  # Fixed the syntax error here
}

famous_births(women_scientists)