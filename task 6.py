def my_func(word=""):
    """Title function

    :param word:
    :return:
    """
    return word.title()


new_list = []
n = 0
for el in input("Введите строку из латинских слов, разделенных пробелом: ").lower().split():
    marker = False
    for symb in el:
        if ord(symb) in list(range(97, 122)):
            pass
        else:
            n += 1
            marker = True
            break
    if marker is False:
        new_list.append(my_func(el))
    else:
        pass

print(f"Вы ввели НЕ латинские буквы минимум {n} раз")

print(" ".join(new_list))
