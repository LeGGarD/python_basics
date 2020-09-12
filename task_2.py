with open("text_2.txt", 'r', encoding='utf-8') as f:
    content = f.readlines()
    print(f"В этом файле {len(content)} строк.\n{36 * '* '}")
    w_q = 0

    for i, el in enumerate(content, 1):
        print(f"В {i} строке - {len(el.split())} слов(а)")
        w_q += len(el.split())

    print(f"{36 * '* '}\nВсего в файле {w_q} слов")
