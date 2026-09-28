# --------------------------- LIBRARIES
from random import randint
from datetime import datetime

# --------------------------- VARIABLES
dates_list = []


# --------------------------- FUNCTIONS
def generate_dates(how_much):
    for _ in range(how_much):
        date = randint(1, 50)
        month = randint(1, 20)
        year = randint(1, 5000)
        dates_list.append(f"{date}.{month}.{year}")
    return True


def check_dates(dates):
    valid_dates = []

    if not dates:
        print("Ошибка, укажите число большее 0!")
        return [[], []]

    for current in dates:
        try:
            parsed_time = datetime.strptime(current, "%d.%m.%Y")
            if parsed_time:
                valid_dates.append(current)
        except ValueError:
            continue

    return valid_dates


# ---------------------------
try:
    how_much_dates = int(input("Сколько дат сгенерировать и проверить? "))

except ValueError:
    print("Введенное значение не является числом")

else:
    generate_dates(how_much_dates)
    answer = check_dates(dates_list)
    print(f'Количество дат прошедших проверку: {len(answer[0])}, даты прошедшие проверку: {answer}')
    print(f'Самая ранняя дата - {sorted(answer)[0]}, самая позднаяя дата - {sorted(answer)[-1]}, ')
