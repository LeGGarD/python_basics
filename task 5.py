my_list = []

while True:
    n = 0
    print(f"Вот ваш список: {my_list}")
    num = input("Введите любое число, которое хотите добавить в рейтинг "
                "(либо напишите 'q', для завершения программы):  ")
    if num.lower() == "q":
        print(f"Вот последняя версия вашего списка: {my_list}")
        break
    elif len(my_list) == 0:
        my_list.append(int(num))
    else:
        num = int(num)
        for el in my_list:
            if num > el:
                my_list.insert(n, num)
                print(f"Вот ваш список после изменений: {my_list} \nИндекс последнего внесенного значения - {n}")
                n += 1
                break
            elif num < el:
                n += 1
                if my_list.index(el) + my_list.count(el) == len(my_list):
                    my_list.append(num)
                    print(f"Вот ваш список после изменений: {my_list} \nИндекс последнего внесенного значения - {n}")
                    break
                else:
                    continue
            else:
                if my_list.index(el) + my_list.count(el) == len(my_list):
                    my_list.append(num)
                    print(f"Вот ваш список после изменений: {my_list} \nИндекс последнего внесенного значения - {n}")
                    break
                else:
                    n += 1
                    continue

# Теперь все работает идеально. Решил заменой единички в 28-ой и 23-ей строкеах на my_list.count(el),
# разобрался почему так. Плюс теперь список изначально пустой и он может заполняться с нуля.
