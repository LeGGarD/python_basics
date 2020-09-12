with open("text_1.txt", 'w', encoding='utf=8') as f:
    str_ = "sample"
    while bool(str_) is True:
        str_ = input("Введите строку, которую хотите добавить в файл: ")
        f.write(f"{str_}\n")
