year = input("Введите Ваш год рождения: ")
if not year.isdigit():
    year = input("Введите, пожалуйста, в формате цифры: ")

age = 2022 - int(year)
print(age)
if age == 21:
    print("You should visit Holland.")
elif age > 21:
    print("You should visit Vietnam.")
else:
    print("Travell everywhere!:)")