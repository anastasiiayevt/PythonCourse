print("Привет, странник!")
nickname = input("Введи свой никнейм: ")
gender = input("Введи свой пол: ")
age_str = input("Введи свой возвраст: ")
age_int = int(age_str)

# first check
if "admin" in nickname:
    print("Привет, повелитель!")

# second check
if 10 < age_int < 14 and gender == "М" or 30 < age_int and gender == "М":
    print("Советую Вам посмотреть ‘StarWars’ или 'Мандалорец'")
if 22 < age_int < 32 and gender == "Ж":
    print("Советую Вам посмотреть 'Трансформеры'")
elif age_int < 16 and gender == "Ж":
    print("Советую Вам посмотреть 'Инсургент'")
elif nickname == "Женя":
    print("Советую Вам посмотреть 'TENET'")
elif age_int < 11 and gender == "М":
    print("Советую Вам посмотреть 'TMNT'")

#third check
if nickname == 'Guido':
    print("Thank you very much!")
