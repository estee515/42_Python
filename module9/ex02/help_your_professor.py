#!/opt/pyenv/shims/python3
import sys

def average(students: dict[str, int | float]) -> float:
    """Calculates the average grade of a class dictionary."""
    if not students:
        return 0.0

    total_grades = 0.0
    for key, grade in students.items():
        # Validate data types
        if not isinstance(grade, (int, float)):
            print(f"Error: Wrong type for student '{key}'", file=sys.stderr)
            sys.exit(1)
            
        # Validate range rules
        if grade < 0 or grade > 20:
            print(f"Error: Invalid grade value {grade} for student '{key}'", file=sys.stderr)
            sys.exit(1)
            
        total_grades += grade
        
    return total_grades / len(students)


# Test cases
class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9,
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B):.2f}.")
print(f"Average for class 3C: {average(class_3C):.2f}.")
