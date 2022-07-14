

name = input("Введите Ваше имя: ")
age = input("Введите Ваш возраст: ")
age = int(age)
if age == 16:
    print(f"Dear {name} need to wait one year")
elif 70 <= age <= 90:
    print(f"You are lucky {name} and welcome")
elif age > 121:
    print(f'You are not real {name}.')
elif age > 16:
    print(f"Welcome {name} on our website:)")
else:
    print(f"I'm sorry {name} you are too young.")