#Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers.

number = int(input("Write an int number: "))
sum_1 = sum(range(1, number + 1))
print(f"Sum of the first {number} positive integers is: {sum_1}")
