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
    invalid_dates = []

    if not dates:
        print("Ошибка, укажите число большее 0!")
        return [[], []]

    for current in dates:
        try:
            parsed_time = datetime.strptime(current, "%d.%m.%Y") #почитать про стрип лол)
            if parsed_time.year <= 2026:
                valid_dates.append(current)
            else:
                invalid_dates.append(current)
        except ValueError:
            invalid_dates.append(current)

    return valid_dates, invalid_dates


# ---------------------------
how_much_dates = int(input("Сколько дат сгенерировать и проверить? ")) # закинуть в блок трай

generate_dates(how_much_dates)
answer = check_dates(dates_list)
print(f'Количество дат прошедших проверку: {len(answer[0])}, количество дат не прошедших проверку: {len(answer[1])}')
