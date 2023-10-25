"""
Create a Python program that repeatedly prompts the user for a number until a valid integer is provided. 
Use a try/except block to handle any ValueError exceptions, and keep asking for input until a valid integer is entered. 
Display the final valid integer.
"""

is_ok = False
while not is_ok:
    user_number = input("Write a number: ")

    try:
        user_number = int(user_number)
        is_ok = True
    except ValueError:
        print("Try again!")

print("This is valid integer! You win.")
