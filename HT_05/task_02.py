'''
Створiть 3 рiзних функцiї (на ваш вибiр). 
Кожна з цих функцiй повинна повертати якийсь результат 
(напр. інпут від юзера, результат математичної операції тощо). 
Також створiть четверту ф-цiю, яка всередині викликає 3 попереднi,
обробляє їх результат та також повертає результат своєї роботи. 
Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3.
'''


def get_and_print_name():
    name = input("Write your name: ")
    print(f"Welcome to Python world, {name}")
    return name


def get_and_print_age():
    age = input("Write your age: ")
    print(f"Your age is {age}")
    return age


def check_answer(res):
    if res == 4:
        print("It is correct! You win!")
        return True
    else:
        print("It is not correct!\n Try again :c")
        return False


def super_test():
    get_and_print_name()
    get_and_print_age()

    while True:
        answer = int(input("Write a correct answer: 2 + 2 = "))
        result = check_answer(answer)
        if result is True:
            break


super_test()
