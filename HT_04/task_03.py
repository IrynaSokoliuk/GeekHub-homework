"""
Create a Python script that takes an age as input. 
If the age is less than 18 or greater than 120, raise a custom exception called InvalidAgeError. 
Handle the InvalidAgeError by displaying an appropriate error message.
"""

class InvalidAgeError(Exception):
    def __init__(self, text):
        self.txt = text


age = input("Write your age: ")

try:
    age = int(age)
    if age <= 18 or age >= 120:
        raise InvalidAgeError(
            "Not the right age, should be in range 18-120 ",
        )
except InvalidAgeError as ex:
    print(ex)
except ValueError:
    print("It is not age value! You should write int!")
else:
    print(f"Your age is {age}")
