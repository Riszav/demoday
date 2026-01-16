db = [
    {"phone": "+996", "password": "12356789"},
    {"username": "1234asda", "password": "2004you"},
]

username = input("Введите Логин: ")
password = input("Введите Пароль: ")


is_authenticated = False

for user in db:
    if username == user["username"] and password == user["password"]:
        print("Успешный вход! Добро пожаловать,", username)
        is_authenticated = True
        break

if not is_authenticated:
    print("Неверный логин или пароль")
