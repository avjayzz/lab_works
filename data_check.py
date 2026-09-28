# ---------------------------------------------------- LIBRARIES

from random import randint
from datetime import datetime


# ---------------------------------------------------- FUNCTIONS
def generate_dates(amount):
    dates = []
    for _ in range(amount):
        day = randint(1, 50)
        month = randint(1, 20)
        year = randint(1, 5000)
        dates.append(f"{day}.{month}.{year}")
    return dates


def check_dates(*dates):
    valid_dates_str = []
    parsed_dates = []
    future_dates = []

    now = datetime.now()

    for current in dates:
        try:
            parsed_time = datetime.strptime(current, "%d.%m.%Y")

            valid_dates_str.append(current)
            parsed_dates.append(parsed_time)

            if parsed_time > now:
                future_dates.append(current)

        except ValueError:
            continue

    if not parsed_dates:
        return [], 0, None, None, []

    earliest_date = min(parsed_dates).strftime("%d.%m.%Y")
    latest_date = max(parsed_dates).strftime("%d.%m.%Y")
    total_valid = len(valid_dates_str)

    return valid_dates_str, total_valid, earliest_date, latest_date, future_dates


# ----------------------------------------------------  MAIN

try:
    how_much_dates = int(input("Сколько дат сгенерировать и проверить? "))
    if how_much_dates <= 0:
        print("Ошибка: укажите число больше 0!")
    else:

        generated_dates = generate_dates(how_much_dates)
        print(f"Сгенерированные даты: {generated_dates}\n")

        valid, count, earliest, latest, future = check_dates(*generated_dates)

        print(f"Количество дат, прошедших проверку: {count}")
        if count > 0:
            print(f"Даты, прошедшие проверку: {valid}")
            print(f"Самая ранняя дата: {earliest}")
            print(f"Самая поздняя дата: {latest}")
            print(f"Будущие даты (относительно сегодня): {future}")
        else:
            print("Среди сгенерированных дат не оказалось ни одной корректной.")

except ValueError:
    print("Ошибка: Введенное значение не является целым числом.")
