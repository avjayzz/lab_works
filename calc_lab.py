# --------------------------- LIBRARIES

import statistics as stat
from random import randint


# --------------------------- FUNCTION
def stats_calculator(*args, mode="basic"):
    if not args or mode not in ["basic", "advanced", "scientific"]:
        return None

    has_negative_in_list = any(chislo < 0 for chislo in args)

    result = {
        "Максимальное число": max(args),
        "Минимальное число": min(args),
        "Среднее арифметическое": stat.mean(args)
    }

    if mode in ["advanced", "scientific"]:
        result["Медиана"] = stat.median(args)
        result["Мода"] = stat.mode(args)

    if mode == "scientific":
        if has_negative_in_list:
            result["Среднее геометрическое"] = "Не определено (есть отрицательные числа)"
            result["Среднее гармоническое"] = "Не определено (есть отрицательные числа)"
        else:
            result["Среднее геометрическое"] = stat.geometric_mean(args)
            result["Среднее гармоническое"] = stat.harmonic_mean(args)

    return result


# --------------------------- MAIN

try:
    answer = int(input("Введите количество чисел для совершения операций: "))

    if answer <= 0:
        print("Количество чисел должно быть больше нуля.")
    else:
        mode_client = input("Введите режим (basic/advanced/scientific): ").strip().lower()
        numbers = [randint(-10, 10000) for _ in range(answer)]

        final = stats_calculator(*numbers, mode=mode_client)

        if final:
            print(f"\nСгенерированные числа: {numbers}\n")
            for name, value in final.items():
                print(f"{name}: {value}")
        else:
            print("Нет данных или неверно указан режим.")

except ValueError:
    print("Ошибка: Некорректно введено число.")
