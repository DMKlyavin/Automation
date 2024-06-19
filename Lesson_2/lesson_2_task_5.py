month = int(input("Введите номер месяца (в диапазоне от 1 до 12) "))
def month_to_season(month):
        if month in [12, 1, 2]:
            print(f"Номер месяца {month} является зимним месяцем")
        elif month in [3, 4, 5]:
            print(f"Номер месяца {month} является весенним месяцем")
        elif month in [6, 7, 8]:
             print(f"Номер месяца {month} является летним месяцем")
        elif month in [9, 10, 11]:
             print(f"Номер месяца {month} является осенним месяцем")
month_to_season(month)
    