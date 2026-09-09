#--------------------------- LIBRARIES
from random import randint
from math import prod
import statistics as stat
#--------------------------- VARIABLES
numbers = []
#--------------------------- FUNCTIONS
def generate_random_numbers():
    for count in range(answer):
        numbers.append(randint(1, 10000))
    return True

def stats_calculator(args, mode="basic"):
    if mode == "basic" and args:
        return [
                max(args),
                min(args),
                stat.mean(args)
        ]
    elif mode == "advanced" and args:
        return [
                max(args),
                min(args),
                stat.mean(args),
                stat.median(args),
                stat.mode(args)
        ]
    elif mode == "scientific" and args:
        return [
                max(args),
                min(args),
                stat.mean(args),
                stat.median(args),
                stat.mode(args),
                prod(args) / len(args),
                stat.harmonic_mean(args)
                ]
    return None
#---------------------------
answer = int(input("Введите количество чисел для совершения операций "))
mode_client = input("Введите режим использования калькулятора - basic/advanced/scientific ")

generate_random_numbers()
final = stats_calculator(args=numbers, mode=mode_client)
#--------------------------- FINAL(NO REASON TO LOOK)
if not numbers or not mode_client: print("Нет данных")
if mode_client == "basic" and numbers: print(f"Максимальное число - {final[0]} \nминимальное число - {final[1]} \nсреднее ариф. - {final[2]}")
if mode_client == "advanced" and numbers: print(f"Максимальное число - {final[0]} \nминимальное число - {final[1]} \nсреднее ариф. - {final[2]} \nмедиана - {final[3]} \nмода - {final[4]}")
if mode_client == "scientific" and numbers: print(f"Максимальное число - {final[0]} \nминимальное число - {final[1]} \nсреднее ариф. - {final[2]} \nмедиана - {final[3]} \nмода - {final[4]} \nсреднее геом - {final[5]} \nсреднее гармоническое - {final[6]}")
#---------------------------
