# --------------------------- LIBRARIES
from random import randint
import statistics as stat

# --------------------------- FUNCTION
def stats_calculator(args, mode="basic"):
    if not args or mode not in ["basic", "advanced", "scientific"]:
        return None

    has_negative_in_list = False
    for chislo in args:
        if chislo < 0:
            has_negative_in_list = True

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
            result["Среднее геометрическое"] = "Среднее геометрическое не определено."
        else:
            result["Среднее геометрическое"] = stat.geometric_mean(args)
        result["Среднее гармоническое"] = stat.harmonic_mean(args)

    return result


# --------------------------- MAIN
try:
    answer = int(input("Введите количество чисел для совершения операций: "))
    mode_client = input("Введите режим использования калькулятора (basic/advanced/scientific): ").strip().lower()

except ValueError:
    print("Некорректно введено число")
else:
    if answer <= 0:
        print("Количество чисел должно быть больше нуля.")
    else:
        numbers = [randint(-10, 10000) for _ in range(answer)]
        final = stats_calculator(args=numbers, mode=mode_client)

        if final:
            for name, value in final.items():
                print(f"{name} - {value}")
        else:
            print("Нет данных/ неверно указан режим")
