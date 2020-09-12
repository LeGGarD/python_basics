from googletrans import Translator

with open("text_4.txt", 'r', encoding="utf-8") as f_r:
    content = [el for el in f_r]
    f_r.seek(0)
    print(f"{36 * '- '}\nСодержимое файла до перевода:\n{36 * '- '}\n{f_r.read()}\n")
    translator = Translator()
    trans = ""
    for translation in translator.translate(content, dest='ru', src='la'):
        trans += f"{translation.text}\n"

with open("text_4_2.txt", 'r+', encoding='utf-8') as f_w:
    f_w.write(trans)
    f_w.seek(0)
    print(f"{36 * '- '}\nСодержимое файла после перевода:\n{36 * '- '}\n{f_w.read()}")
