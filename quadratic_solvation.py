#--------------------------- LIBRARIES
from math import sqrt
#--------------------------- VARIABLES
a = int(input("Введите коэффициент A:"))
b = int(input("Введите коэффициент B:"))
c = int(input("Введите коэффициент C:"))
#--------------------------- FUNCTIONS
def solve_quadratic_diskriminant():
    if a == 0:
        if b != 0:
            print(f"Уравнение линейное. Единственный корень: {-c / b}")
        else:
            print("X - любое число")
        return

    discriminant = b**2 - (4 * a * c)
    if discriminant < 0:
        print("Нет решения в действительных числах")
    elif discriminant == 0:
        print(f'Единственным корнем уравнения является {-b / (2 * a)}')
    else:
        print(f'Первый корень уравнения: {(-b + sqrt(discriminant)) / (2 * a)}, второй корень: {(-b - sqrt(discriminant)) / (2 * a)}')
#---------------------------
solve_quadratic_diskriminant()
