#--------------------------- LIBRARIES
from random import randint
from math import prod
import statistics as stat
#--------------------------- VARIABLES
numbers = []
#--------------------------- FUNCTIONS
def generate_random_numbers(count):
    return [randint(1, 10000) for _ in range(count)]

def stats_calculator(args, mode="basic"):

   if not args or mode not in ["basic", "advanced", "scientific"]:
       return None

   result = {
       "Максимальное число": max(args),
       "Минимальное число": min(args),
       "Среднее арифметическое": stat.mean(args)
   }

   if mode in ["advanced", "scientific"]:
       result["Медиана"] = stat.median(args)
       result["Мода"] = stat.mode(args)

   if mode == "scientific":
       result["Среднее геометрическое"] = stat.geometric_mean(args)
       result["Среднее гармоническое"] = stat.harmonic_mean(args)

   return result
#---------------------------
try:
    answer = int(input("Введите количество чисел для совершения операций: "))
    mode_client = input("Введите режим использования калькулятора (basic/advanced/scientific): ").strip().lower()

    if answer <= 0:
        print("Количество чисел должно быть больше нуля.")
    else:
        numbers = generate_random_numbers(answer)
        final = stats_calculator(args=numbers, mode=mode_client)

        if final:
            for name, value in final.items():
                print(f"{name} - {value}")
        else:
            print("Нет данных/ неверно указан режим")

except ValueError:
    print("Некорректно введено число")
