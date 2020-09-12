with open("text_5.txt", "w+", encoding='utf-8') as f:
    inp = "sample"
    while bool(inp) is True:
        inp = input("Введите числа разделенные пробелом, для подсчета их суммы, для выхода нажмите Enter: ")
        if inp == "":
            print(f"Последняя сумма всех чисел: {sum(val_for_sum)}")
            break
        f.write(f"{inp} ")
        try:
            f.seek(0)
            val_for_sum = [int(el) for el in f.read().split()]
            print(sum(val_for_sum))
        except ValueError:
            print("Вводить можно только числа")
