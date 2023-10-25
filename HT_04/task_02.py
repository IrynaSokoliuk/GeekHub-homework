"""
Create a custom exception class called NegativeValueError. 
Write a Python program that takes an integer as input and raises the NegativeValueError if the input is negative. 
Handle this custom exception with a try/except block and display an error message.
"""

class NegativeValueError(Exception):
    def __init__(self, text):
        self.txt = text


num = input("Write a number: ")

try:
    num = int(num)
    if num < 0:
        raise NegativeValueError("You give negative number!")
except NegativeValueError as ex:
    print(ex)
