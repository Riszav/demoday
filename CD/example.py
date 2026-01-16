import random

random_number = random.randint(1, 10)
attemps = 3

while True:
    print("У вас осталось попыток ", attemps)
    user_number = int(input("Введите число от 1 до 10: "))
    attemps -= 1
    if user_number == random_number:
        print("Угадал!")
        break
    elif user_number > random_number:
        print("Число меньше!")
    elif user_number < random_number:
        print("Число больше!")

    else:
        print("Вы ввели число, не корректно")
    if attemps == 0:
        print("Вы проиграли!")
        break
