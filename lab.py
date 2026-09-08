#--------------------------- LIBRARIES
from math import sqrt
#--------------------------- VARIABLES
a = int(input("Введите коэффициент A:"))
b = int(input("Введите коэффициент B:"))
c = int(input("Введите коэффициент C:"))
#--------------------------- FUNCTIONS
def solve_quadratic_diskriminant():
    discriminant = b**2 - (4 * a * c)
    if discriminant < 0: return print("Нет решения в действительных числах")
    elif discriminant == 0: return print(f'Единственным корнем уравнения является {-b * 2 * a}')
    else: return print(f'Первый корень уравнения: {(-b + sqrt(discriminant)) / 2 * a}, второй корень: {(-b - sqrt(discriminant)) / 2 * a}')
#---------------------------
while True:
    solve_quadratic_diskriminant()
    break