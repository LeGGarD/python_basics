from itertools import cycle, count

try:
    i = int(input("Введите со скольки вы хотите начать считать: "))
    itr_obj = iter(count(i))
    print(f"Выводим 10 чисел, начиная с {i}: ")
    n = 0
    a_list = []
    while n < 10:
        item = next(itr_obj)
        a_list.append(item)
        n += 1
    print(a_list)
except ValueError:
    print("Вводить можно только целое натуральное число")

try:
    itr_obj2 = iter(cycle(input("Введите любую строку: ")))
    n2 = int(input('Введите сколько раз вы хотите перебрать строку по элементам: '))
    print(f"Теперь перебираем строку {n2} раз")
    list_ = []
    while n2 > 0:
        item = next(itr_obj2)
        list_.append(item)
        n2 -= 1
    print(f"Вот ваши перебранные буквы:\n{list_}")
except ValueError:
    print("Вводить можно только целое натуральное число")

print("Это была моя самая полезная программа за последнюю жизнь :D Спасибо за пользование")
