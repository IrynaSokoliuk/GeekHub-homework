"""
Написати функцію <bank> , яка працює за наступною логікою:
користувач робить вклад у розмірі <a> одиниць строком на <years> років під <percents> відсотків
(кожен рік сума вкладу збільшується на цей відсоток, ці гроші додаються до суми вкладу
і в наступному році на них також нараховуються відсотки).
Параметр <percents> є необов'язковим і має значення
по замовчуванню <10> (10%). Функція повинна принтануть суму, яка буде на рахунку,
а також її повернути (але округлену до копійок).

"""


def bank(start_summ, percentage, years):
    total_summ = start_summ
    for _ in range(years):
        year_profit = total_summ * percentage / 100
        total_summ += year_profit
    total_summ = round(total_summ, 2)
    print(f"Ваш капітал після {years} років становить {total_summ}$")
    return total_summ


bank()
