def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


try:
    year = int(input("Введите год: "))
    print(is_year_leap(year))
except ValueError:
    print("Пожалуйста, введите целое число")
