"""
Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000,
и яка вертатиме True, якщо це число просте і False - якщо ні.
"""


def is_prime(n):
    if 0 <= n <= 1000:
        d = 2

        while d * d <= n and n % d != 0:
            d += 1

        if d * d > n:
            print("Число просте")
            return True
        else:
            print("Число складене")
            return False
    return False


is_prime()
