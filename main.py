import os  # Rule F401: Unused import
import sys # Rule F401: Unused import

def main():
    unused_var = 42  # Rule F841: Local variable is assigned to but never used
    
    # Rule E501: Line too long (standard limit is usually 88 characters)
    print("This is an incredibly long string that is designed to exceed the character limit of a standard line in Python code according to the ruff linter settings.")

    print("kmsksmksmksm Breaking things for science!")

if __name__ == "__main__":
    main()
