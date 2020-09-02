ex_list = list(input("Введите любое кол-во цифр:  "))

print(f"Вот ваш список: {ex_list}")
print("Теперь меняем местами близь стоящие элементы:")

new_list = ex_list[0::2]
new_list2 = ex_list[1::2]
n = 0

for el in new_list2:
    new_list.insert(n, el)
    n += 2

print(new_list)

