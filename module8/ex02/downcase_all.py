#!/opt/pyenv/shims/python3

import sys

def downcase_all(text: str) -> str:
    """Converts a given string to lowercase."""
    return text.lower()

def main():
    # Check if any arguments were provided
    if len(sys.argv) < 2:
        print("none")
        return  # Exit early to avoid deep nesting

    # Process and print each argument
    for arg in sys.argv[1:]:
        print(downcase_all(arg))

if __name__ == "__main__":
    main()
