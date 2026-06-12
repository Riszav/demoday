database = []

while True:
    print("1. Добавить отзыв")
    print("2. Показать все отзывы")
    print("3. Выйти")
    choice = input("Выберите действие (1, 2, 3): ")

    if choice == "1":
        name = input("Введите ваше имя: ")
        review = input("Введите ваш отзыв: ")
        stars = input("Введите количество звезд (1-5): ")
        database.append({"name": name, "review": review, "stars": stars})
        print("Отзыв добавлен!")
    elif choice == "2":
        if not database:
            print("Нет отзывов для отображения.")
        else:
            for i, v in enumerate(database, start=1):
                print(f"{i}. {v['name']} - {v['review']} ({v['stars']} звезд)")
        # print(database)
        # for review in database:
        #     print(f"{review['name']} - {review['review']} ({review['stars']} звезд)")
    elif choice == "3":
        print("Выход из программы. До свидания!")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")
    print("\n")
