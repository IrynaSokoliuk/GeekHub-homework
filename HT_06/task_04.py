"""
Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона,
і вертатиме список простих чисел всередині цього діапазона.
Не забудьте про перевірку на валідність введених даних
та у випадку невідповідності - виведіть повідомлення.
"""


def is_prime(n: int) -> bool:
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def prime_list(start: int, end: int):
    primes = []
    for el in range(start, end + 1):
        if is_prime(el):
           primes.append(el)
    return primes


def start():
    try:
        start = int(input("Write start num: "))
        end = int(input("Write end num: "))
        if start > end:
            print("Start > end error!")
        else:
            print("Primes list: ", prime_list(start, end))
    except ValueError:
        print("Invalid data!")


start()
