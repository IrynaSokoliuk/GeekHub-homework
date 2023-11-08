"""
Напишіть функцію,яка прймає рядок з декількох слів і повертає довжину найкоротшого слова.
Реалізуйте обчислення за допомогою генератора.
"""


def shortest_word_length(input_string):
    words = input_string.split()
    shortest_str = min(len(word) for word in words)
    return shortest_str


input_str = input("write the sentence: ")
result = shortest_word_length(input_str)
print(result)
