import json


def lists_collab(list_1, list_2):
    max_len = max([len(list_1), len(list_2)])
    try:
        for i in range(0, max_len):
            yield [list_1[i], list_2[i]]
    except IndexError:
        print("Функция применима только для списков одинаковой длинны")


with open("text_7.txt", "r", encoding="utf-8") as f:
    content = f.readlines()
    profit_count = [int(el.split()[2]) - int(el.split()[3]) for el in content]
    print(f"{36 * '- '}\nРасчет доходов - затрат, каждой компании:\n{36 * '- '}\n{profit_count}\n")
    profits = [el for el in profit_count if el > 0]
    avg_prof = f"{float(sum(profits) / len(profits)):.2f}"
    print(f"{36 * '- '}\nСредний доход по всем компаниям, не учитывая убыточных:\n{36 * '- '}\n{avg_prof}\n")
    names = [el.split()[0] for el in content]
    fin_list = [{el[0]: el[1] for el in lists_collab(names, profit_count)}, {"average_profit": avg_prof}]
    print(
        f"{36 * '- '}\nСписок фирм с их прибылью + средняя выручка у всех компаний, не считаю убыточные\n{36 * '- '}\n{fin_list}")

with open("text_77.json", "w", encoding="utf-8") as f:
    json.dump(fin_list, f, ensure_ascii=False, sort_keys=True, indent=4)
