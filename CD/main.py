# height = int(input("Введите высоту ёлки: "))

# for i in range(1, height + 1):
#     print(" " * (height - i) + "*" * (2 * i - 1))

# print(" " * (height - 1) + "|")

# levels = int(input("Сколько ярусов у ёлки: "))

# for level in range(1, levels + 1):
#     for i in range(1, level * 3):
#         spaces = (levels * 3) - i
#         print(" " * spaces + "*" * (2 * i - 1))

# print(" " * (levels * 3 - 1) + "|")


import random

# Цвета ANSI
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
RESET = "\033[0m"

height = int(input("Введите высоту ёлки: "))

for i in range(1, height + 1):
    line = ""
    for j in range(2 * i - 1):
        # Рандомно выбираем: ёлка или игрушка
        if random.random() < 0.15:  # ~15% шанс на игрушку
            line += random.choice([RED + "o" + RESET, YELLOW + "o" + RESET])
        else:
            line += GREEN + "*" + RESET

    print(" " * (height - i) + line)

# Ствол
print(" " * (height - 1) + YELLOW + "|" + RESET)
