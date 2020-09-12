with open('text_3.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    f.seek(0)
    print(f"{36 * '- '}\nСодержимое файла:\n{36 * '- '}\n{f.read()}\n")
    a = [el.split()[0] for el in content if float(el.split()[1]) < float(20000)]
    print(f"{36 * '- '}\nФамилии сотрудников, получающих меньше 20 000 у.е:\n{36 * '- '}\n{a}\n")


    def aver_income(a_list):
        inc = [el.split()[1] for el in a_list]
        inc_sum = float(0)
        for el in inc:
            inc_sum += float(el)
        return inc_sum / len(inc)


    print(f"{36 * '- '}\nСредняя величина дохода сотрудников:\n{36 * '- '}\n{aver_income(content):.2f}")
