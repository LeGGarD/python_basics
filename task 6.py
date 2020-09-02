my_list = []

while True:
    n = int(input("Введите кол-во товаров, которые хотите внести в список:  "))
    num = 1

    while n > 0:
        name = input("Введите название товара:  ")
        price = input("Введите цену товара:  ")
        quantity = input("Введите кол-во товара:  ")
        product = (num, {"название": name, "цена": price, "кол-во": quantity, "ед": "шт."})
        num += 1
        my_list.append(product)
        n -= 1

    print("Вот ваша структура данных 'Товары':")
    for el in my_list:
        print(el)

    print("Теперь проводим аналитику товаров:")

    my_dict = {}
    num = 0

    my_list_names = []
    my_list_price = []
    my_list_quantity = []

    for el in my_list:
        my_list_names.append(el[1].get("название"))
        my_list_price.append(el[1].get("цена"))
        my_list_quantity.append(el[1].get("кол-во"))

    my_dict = {"название": my_list_names, "цена": my_list_price, "кол-во": my_list_quantity, "ед": "шт."}

    for el in my_dict.items():
        print(el)

    menu = input("Если хотите выйти из программы - напишите q \nЕсли хотите продолжить - нажмите Enter: ")

    if menu.lower() == "q":
        break
    else:
        continue
