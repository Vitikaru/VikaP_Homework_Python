from math import ceil


def square(side):
    return ceil(side * side)


side = float(input("Сторона: "))
print(f' Площадь квадрата - {ceil(side * side)}')
