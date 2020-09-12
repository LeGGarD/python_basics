def lists_collab(list_1, list_2):
    max_len = max([len(list_1), len(list_2)])
    try:
        for i in range(0, max_len):
            yield [list_1[i], list_2[i]]
    except ImportError:
        print("Функция применима только для списков одинаковой длинны")


with open("text_6.txt", "r", encoding='utf-8') as f:
    content = f.readlines()
    f.seek(0)

    print(f"{36 * '- '}\nСодержимое файла:\n{36 * '- '}\n{f.read()}\n")
    subjs = [el.split()[0][0:-1] for el in content]
    print(f"{36 * '- '}\nСписок уроков:\n{36 * '- '}\n{subjs}\n")

    sums = []
    for el in content:
        sum = 0
        for i in el.split():
            if "(" in list(i):
                sum += int(i[0:i.find("(")])
        sums.append(sum)

    print(f"{36 * '- '}\nОбщее кол-во занятий по каждому предмету:\n{36 * '- '}\n{sums}\n")
    print(f"{36 * '- '}\nСформированный словарь, типа 'Урок: кол-во занятий':\n{36 * '- '}\n",
          {el[0]: el[1] for el in lists_collab(subjs, sums)})
